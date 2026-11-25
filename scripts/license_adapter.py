"""KR（MFDS 의약품안전나라 nedrug）許可證下載與狀態對應，給 license_refresh_20261029.py 用（2026-10-30）。

來源：nedrug 搜尋頁的「엑셀다운로드」（POST https://nedrug.mfds.go.kr/searchDrug/getExcel，免登入、免 service key；
先 GET /searchDrug 取 cookie，每批 10,000 筆，以 ExcelRowdata／ExcelRowdata2 位移）。xlsx 欄位：품목기준코드（唯一鍵，＝證據包 license_id）、
취소/취하（정상／취하／폐업／유효기간만료／행정(취소)…）。
寫回：status＝취소/취하 原文（정상 寫成空白以外的「정상」）；license_status：정상→valid，其他→cancelled（韓文字樣不在 reviewer 的註銷字樣裡）。
2026-10-31（用戶決定）：Kr 頁面狀態列改依這份資料的註銷狀態，與其他站相同（原本固定寫 Unknown）。新檔沒有的品目保留原狀態。

2026-11-17（用戶要求確認 11-16 排程「新資料查不到」的 3 張）：nedrug 的엑셀다운로드 收全部正常品目，但취소/취하 的品目只收
취소일자在最近約 3 年內的（對照 2026-03 的 ItemPermitDetail.xlsx：취소일자 2023-11 中旬以前的品目全部不在 11-16 的下載檔，
2023-12 以後的全部在）——品目從下載檔消失＝취소日期滑出 3 年窗口，不是 MFDS 刪除紀錄。3 張（200607418、200800968、201310113）
都是 2023-11 취하／유효기간만료、證據包本來就是 cancelled。做法：
- fetch() 把下載檔的品目記成 CURRENT（少於 MIN_CURRENT 不判定），並從證據包收「原本就已註銷」的品目（PRIOR_CANCELLED）。
- confirmed_absent(lid)：下載成功、不在 CURRENT、而證據包原本就記為註銷＝MFDS 早已註銷、只是滑出下載窗口。
  原本是有效、卻不在下載檔的品目不推定（仍列為查不到）。
- preprocess：這種品目加 mfds_not_listed（第一次發現日），狀態不動；又出現在下載檔就取消標記。
"""
import io
import json
import time
from pathlib import Path

import openpyxl
import requests

RAW_FILE = "raw/mfds_cancel_status.json"
BASE = "https://nedrug.mfds.go.kr"
BATCH = 10000
REPO = Path(__file__).resolve().parents[1]
CURRENT: set = set()          # fetch() 填：下載檔的品目기준코드；空的就不判定
PRIOR_CANCELLED: set = set()  # fetch() 填：證據包裡原本就是 cancelled 的品目
MIN_CURRENT = 50000           # 2026-11-16 下載 95,254 筆


def _batch(s, start):
    data = {"searchYn": "true", "ExcelRowdata": str(start), "ExcelRowdata2": str(start + BATCH), "page": "1",
            "searchDivision": "detail", "excelSearchCnt": str(BATCH)}
    for attempt in range(4):
        try:
            r = s.post(BASE + "/searchDrug/getExcel", data=data, timeout=300)
            r.raise_for_status()
            if r.content[:2] != b"PK":
                raise RuntimeError("回傳的不是 xlsx")
            return r.content
        except Exception:
            if attempt == 3:
                raise
            time.sleep(15 * (attempt + 1))


def fetch():
    s = requests.Session()
    s.headers["User-Agent"] = "Mozilla/5.0 (compatible; TxGNN/1.0; research)"
    s.get(BASE + "/searchDrug", timeout=60)
    out, start, short_retry, empty = [], 0, 0, 0
    while True:
        ws = openpyxl.load_workbook(io.BytesIO(_batch(s, start)), read_only=True).active
        ws.reset_dimensions()  # 檔內的 dimension 只寫 A1，不重設會只讀到第一欄
        rows = ws.iter_rows(values_only=True)
        head = [str(x or "").strip() for x in next(rows)]
        if "품목기준코드" not in head or "취소/취하" not in head:
            raise RuntimeError(f"欄位改變：{head[:12]}")
        cols = _extra_cols(head)
        if start == 0:
            _write_columns(head, cols)
        n = 0
        for row in rows:
            rec = dict(zip(head, row))
            k = str(rec.get("품목기준코드") or "").strip()
            if k:
                e = {"item_seq": k, "status": str(rec.get("취소/취하") or "").strip()}
                for key, h in cols.items():
                    v = str(rec.get(h) or "").strip()
                    if v:
                        e[key] = v
                out.append(e); n += 1
        # 2026-10-30：GitHub runner 上某批會被限流、回傳不滿 1 萬筆就提早結束（只抓到七成）。
        # 不滿一批時先重抓同一批；連續兩批都是 0 筆才算到底
        if n < BATCH and short_retry < 2 and n > 0:
            short_retry += 1
            out = out[: len(out) - n]
            time.sleep(30)
            continue
        short_retry = 0
        empty = empty + 1 if n == 0 else 0
        if empty >= 2 or start > 300000:
            break
        start += BATCH
        time.sleep(3)
    CURRENT.clear(); PRIOR_CANCELLED.clear()
    if len(out) >= MIN_CURRENT:
        CURRENT.update(r["item_seq"] for r in out)
        PRIOR_CANCELLED.update(_prior_cancelled())
    return out


# 2026-11-25（第五輪，用戶決定「adapter 存成分」）：下載檔除了號碼與狀態，另存收集器比對要用的欄位（品名、업체、成分、허가일…），
# 寫進同一份 data/raw/mfds_cancel_status.json（Release 帶著），供 scripts/measure_missing_licenses.py 量漏收、之後補收用。
# nedrug 從雲端 session 連不到，欄名照 nedrug 엑셀다운로드的寫法用候選名對（第一個存在的欄）；實際表頭另存
# data/raw/mfds_cancel_status_columns.json，對不到成分欄時照常更新狀態（不擋排程），量測程式會回報「沒有成分欄」。
EXTRA = {
    "product": ("제품명", "품목명"),
    "product_en": ("제품영문명", "품목영문명", "영문제품명"),
    "company": ("업체명",),
    "ingredients": ("주성분", "주성분명", "성분명", "원료성분"),
    "ingredients_en": ("주성분영문", "주성분 영문", "영문성분명", "주성분영문명"),
    "ingredient_count": ("주성분수",),
    "permit_no": ("허가번호",),
    "permit_date": ("허가일", "허가일자"),
    "category": ("전문/일반", "전문일반", "전문의약품/일반의약품", "전문의약품"),
    "item_type": ("품목구분",),
    # 2026-11-25（第六輪，用戶決定「新品目補收、不收의약외품」）：補收程式 scripts/add_current_licenses.py 的收錄規則要看
    # 완제/원료（2026-03 基準清單 ItemPermitDetail.xlsx 只有완제의약품）、허가/신고、제형
    "finished_raw": ("완제/원료", "완제원료구분"),
    "permit_kind": ("허가/신고", "허가/신고구분"),
    "dosage_form": ("제형",),
    "product_class": ("품목분류",),
    "cancel_date": ("취소/취하일자", "취소일자"),
    "atc": ("ATC코드", "ATC 코드"),
}


def _extra_cols(head):
    hs = set(head)
    out = {k: next((c for c in cands if c in hs), None) for k, cands in EXTRA.items()}
    if not out["ingredients"]:  # 候選名都不在：取第一個含「성분」、不含「영문」的欄
        out["ingredients"] = next((h for h in head if "성분" in h and "영문" not in h and "첨가" not in h), None)
    return {k: v for k, v in out.items() if v}


def _write_columns(head, cols):
    p = REPO / "data/raw/mfds_cancel_status_columns.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps({"downloaded": time.strftime("%Y-%m-%d"), "header": head, "saved": cols}, ensure_ascii=False, indent=1),
                 encoding="utf-8")
    if "ingredients" not in cols:
        print(f"⚠ nedrug 엑셀다운로드 沒有對到成分欄（表頭：{head}）；只更新狀態", flush=True)


def _prior_cancelled():
    out = set()
    for f in (REPO / "data/bundles").glob("*/drug_bundle.json"):
        for r in (json.loads(f.read_text(encoding="utf-8")).get("tfda") or {}).get("records") or []:
            if r.get("license_status") == "cancelled" and r.get("status") and r.get("status") != "정상":
                out.add(str(r.get("license_id") or "").strip())
    return out


def confirmed_absent(lid):
    """給 license_refresh：下載檔沒有、證據包原本就記為註銷＝MFDS 早已註銷（滑出下載檔的 3 年窗口），不算查不到"""
    lid = str(lid).strip()
    return bool(CURRENT) and lid not in CURRENT and lid in PRIOR_CANCELLED


def preprocess(bundle):
    """confirmed_absent 的品目加 mfds_not_listed（第一次發現日），狀態不動；又出現在下載檔就取消。有改回 True"""
    if not CURRENT:
        return False
    today = time.strftime("%Y-%m-%d")
    ch = False
    for r in (bundle.get("tfda") or {}).get("records") or []:
        lid = str(r.get("license_id") or "").strip()
        if not lid:
            continue
        if lid in CURRENT:
            if r.pop("mfds_not_listed", None):
                ch = True
        elif lid in PRIOR_CANCELLED and not r.get("mfds_not_listed"):
            r["mfds_not_listed"] = today
            ch = True
    return ch


def validate(new, old):
    p = []
    if len(new) < 50000:
        p.append(f"只解析出 {len(new)} 筆（全庫約 9.5 萬），疑似格式或分批改變")
    if old and len(new) < 0.9 * len(old):
        p.append(f"筆數 {len(new)} 比上次 {len(old)} 少超過 10%")
    return p


def status_index(new):
    return {r["item_seq"]: r["status"] for r in new if r["status"]}


def record_id(rec):
    return str(rec.get("license_id") or "").strip()


def update(rec, new):
    cls = "valid" if new == "정상" else "cancelled"
    if rec.get("status") == new and rec.get("license_status") == cls:
        return False
    if not rec.get("status") and cls == "valid" and rec.get("license_status") in (None, "valid"):
        return False  # 原本空白（reviewer 視為有效）、現在仍正常：意義不變，不算變動
    rec["status"], rec["license_status"] = new, cls
    return True


# 2026-11-24（用戶決定）：「한국 시판 정보」的許可證表改由 scripts/sync_license_tables.py 依證據包產生（程式區塊 <!-- licenses:begin/end -->）。
# 每週排程（license_refresh_20261029.py 的 sync_tables 掛鉤）全站重排：狀態變了，狀態欄、排序與「위 표는 허가 M건 중 N건입니다.」都跟著變；
# 只重排程式區塊，表以外的正文不動（正文張數由 build_license_snapshot.py／apply_drug_reviews.py 結尾的 rewrite_license_counts.py 依快照改寫）。
# PAGE_NOTE：表格列以外、程式寫的行（說明句、區塊標記、沒有任何허가時的一句；2026-11-24 第三輪起含 add_section 補的市場段落標題），3b 自我檢查放行。
PAGE_NOTE = (r"^(## 한국 시판 정보|위 표는 허가 (최소 )?\d+건 중 \d+건입니다\.|이 자료에는 허가의 일부\(최소 \d+건\)만 수록되어 있습니다\.|"
             r"<!-- licenses:(begin|end) -->|"
             r"식품의약품안전처 의약품안전나라\(nedrug\) 허가 자료\(이 보고서에 쓴 자료\)에는 이 약 성분의 허가가 없습니다\.)$")


def sync_tables(site_dir, bundles=None):
    import importlib.util
    s = importlib.util.spec_from_file_location("kr_slt", Path(site_dir) / "scripts/sync_license_tables.py")
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return [(pg, "許可證表", "", "依證據包重排") for pg in m.run()]
