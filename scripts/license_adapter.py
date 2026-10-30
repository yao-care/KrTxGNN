"""KR（MFDS 의약품안전나라 nedrug）許可證下載與狀態對應，給 license_refresh_20261029.py 用（2026-10-30）。

來源：nedrug 搜尋頁的「엑셀다운로드」（POST https://nedrug.mfds.go.kr/searchDrug/getExcel，免登入、免 service key；
先 GET /searchDrug 取 cookie，每批 10,000 筆，以 ExcelRowdata／ExcelRowdata2 位移）。xlsx 欄位：품목기준코드（唯一鍵，＝證據包 license_id）、
취소/취하（정상／취하／폐업／유효기간만료／행정(취소)…）。
寫回：status＝취소/취하 原文（정상 寫成空白以外的「정상」）；license_status：정상→valid，其他→cancelled（韓文字樣不在 reviewer 的註銷字樣裡）。
注意：Kr 頁面的狀態列目前依規則固定寫「Unknown (source lacks cancellation status)」（舊來源沒有註銷狀態）；
這份新來源有註銷狀態，要不要改掉這條規則另案決定，排程先只更新證據包。新檔沒有的品目保留原狀態。
"""
import io
import time

import openpyxl
import requests

RAW_FILE = "raw/mfds_cancel_status.json"
BASE = "https://nedrug.mfds.go.kr"
BATCH = 10000


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
        n = 0
        for row in rows:
            rec = dict(zip(head, row))
            k = str(rec.get("품목기준코드") or "").strip()
            if k:
                out.append({"item_seq": k, "status": str(rec.get("취소/취하") or "").strip()}); n += 1
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
    return out


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
