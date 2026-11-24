#!/usr/bin/env python3
"""「## 한국 시판 정보」段落的許可證表改由程式依證據包產生（2026-11-24，用戶決定；全程不用 AI）。

為什麼：以前這張表是報告（AI）寫的自由格式表（多數是「| 허가번호 | 제품명 | 제형 | 허가 적응증 |」，沒有狀態欄，
少數有「상태」欄寫死「유효」），每週許可證排程只改得到概覽表的狀態列與張數列，表裡寫死的狀態與選列跟著 MFDS 資料變動就過期。
改成程式表後，每週排程（scripts/license_adapter.py 的 sync_tables 掛鉤）依同一套規則重排，gate 依快照驗內容。

表格（比照 HkTxGNN／SgTxGNN／UkTxGNN 的程式表）：
- 段落裡原有的第一張表（不論原欄位）換成「| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |」；資料是證據包 tfda.records
  （식품의약품안전처 의약품안전나라 nedrug 허가 자료），欄位照 MFDS 原文（韓文，不翻譯）：제품명＝품목명、성상＝성상（證據包 dosage_form）、
  업체명＝허가 업체、허가사항＝허가사항 PDF（證據包 indication 是 nedrug pdfDownload 網址時才有連結，否則「—」）。
- 狀態欄：跟事實層同一套判斷（reviewer drug_evidence_pack._local_regulatory：license_status、취소/취하 原文、有效期限已過）；
  有效寫「유효」（本站既有寫法）；註銷寫 MFDS 취소/취하 原文（취하、유효기간만료、행정(취소)、폐업…），沒有原文而因有效期限已過算註銷的寫「유효기간만료」。
- 單方／複方不列：本站證據包 ingredients 只記比對到的那個成分（例 올멕포스에이치정 只記 AMLODIPINE BESYLATE），判斷不了。
- 選列與順序：換表當時報告原表列出的허가번호（config/license_table_pins.json，依原表順序）在前——正文常寫「주요 허가 5건」
  「5건만 표시했습니다. 나머지는 …」，換成別的列會對不上；其餘（以及原本沒有表的頁）依程式排序：有效在前、註銷在後，再依허가번호。
  原表的號碼不在證據包裡的（2026-11-24 有 9 頁各 1 個）照樣不列，由程式排序的下一列補上。
- 列數＝原表列數（最多 20 列）；總數多於列數時，表下加一句「위 표는 허가 M건 중 N건입니다.」，
  證據包只收了部分허가（事實層 partial，total_matches 大於紀錄數）時寫「위 표는 허가 최소 M건 중 N건입니다.」（M＝證據包收的紀錄數，同概覽表「최소 M건」），
  列完了全部收錄紀錄時寫 PART_ALL。
- 段落裡沒有表的頁：在標題下補程式表（min(5, 總數) 列）；證據包沒有任何紀錄時補 NONE_LINE。
- 表以外的文字不動（正文張數由 scripts/rewrite_license_counts.py 依快照事實層改寫）。
程式區塊標記：程式表（連同表下說明句，或 NONE_LINE）前後各一行「<!-- licenses:begin -->」「<!-- licenses:end -->」（前後空行）。
兩種來源：證據包（run()，需要 data/bundles）；快照（run(from_snapshot=True)：snapshots/kr_licenses.json.gz 的 rows／nrows／partial，
不需要 data/，給 apply_drug_reviews.py 與 build_license_snapshot.py 結尾用；只重排已有程式區塊、或段落有表的頁）。
program_rows 給 scripts/build_license_snapshot.py（快照存最多 20 列）；carry_block 給 scripts/sync_notes_to_docs.py 重寫整頁時移植舊頁的程式區塊；
run 給 scripts/license_adapter.py 的 sync_tables。
用法（repo 根目錄）：python3 scripts/sync_license_tables.py [--from-snapshot] [--dry-run] [頁 ...]
"""
import gzip
import json
import re
import sys
import types
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SECS = ("한국 시판 정보", "시판 정보")
HEAD = ["| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |", "|------|------|------|------|------|------|"]
NONE_LINE = "식품의약품안전처 의약품안전나라(nedrug) 허가 자료(이 보고서에 쓴 자료)에는 이 약 성분의 허가가 없습니다."
SHOW = "위 표는 허가 {m}건 중 {n}건입니다."
SHOW_PART = "위 표는 허가 최소 {m}건 중 {n}건입니다."
PART_ALL = "이 자료에는 허가의 일부(최소 {m}건)만 수록되어 있습니다."
SHOW_RX = re.compile(r"^(위 표는 허가 (최소 )?\d+건 중 \d+건입니다\.|이 자료에는 허가의 일부\(최소 \d+건\)만 수록되어 있습니다\.)$")
# 換表前報告在舊表下寫的「只講表上列了幾筆」的整行說明句（2026-11-24 有 4 頁：doxorubicin、kallidinogenase、latanoprost、zaltoprofen）：
# 跟程式說明句重複，換表時拿掉；只認整行完全是這種句子的（句中另有事實的不動）
CAPTION_RX = re.compile(r"^(위 표는 (전체 |주요 |대표 )?(허가 )?(\d+건 중 )?\d+건(만)? ?(을 |만 )?(나열|표시)한 것입니다\.|위 표에는 주요 \d+건만 나열했습니다\.)$")
BEGIN = "<!-- licenses:begin -->"
END = "<!-- licenses:end -->"
MAX_ROWS = 20
ST_VALID = "유효"
PDF = re.compile(r"^https://nedrug\.mfds\.go\.kr/pbp/cmn/pdfDownload/[0-9A-Za-z]+/[A-Za-z]+$")
SNAP = ROOT / "snapshots" / "kr_licenses.json.gz"


def cell(x, cap=None):
    s = re.sub(r"\s+", " ", str(x or "").replace("|", "/")).strip()
    return s[:cap].rstrip() + "…" if cap and len(s) > cap else s


_LR = None


def _local_regulatory(bundle):
    """事實層同一套判斷（dump_license_facts 用的就是這個函式）"""
    global _LR
    if _LR is None:
        sys.path.insert(0, str(ROOT / "src"))
        from krtxgnn.reviewer.drug_evidence_pack import DrugEvidencePackGenerator as G
        _LR = G._local_regulatory
    return _LR(types.SimpleNamespace(**bundle))


def status_label(rec, st):
    if st == "valid":
        return ST_VALID
    s = cell(rec.get("status"))
    if s and s != "정상":
        return s
    return "유효기간만료" if st == "cancelled" else "취소"


def table_rows(bundle, pins=()):
    """全部可列的列（字串）：pins（原表選列）依序在前，其餘依程式排序（有效在前，再依허가번호）"""
    recs = (bundle.get("tfda") or {}).get("records") or []
    if not recs:
        return []
    st = {x["license_number"]: x["status"] for x in _local_regulatory(bundle).get("licenses", [])}
    seen = {}
    for r in recs:
        k = str(r.get("license_id") or "").strip()
        if k and k not in seen:
            seen[k] = r
    u = sorted(seen.values(), key=lambda r: (st.get(str(r["license_id"]).strip()) != "valid", str(r["license_id"]).strip()))
    rank = {k: i for i, k in enumerate(pins or [])}
    u.sort(key=lambda r: rank.get(str(r["license_id"]).strip(), len(rank)))  # 穩定排序：沒選的保持程式排序
    rows = []
    for r in u:
        k = str(r["license_id"]).strip()
        name = cell(r.get("brand_name_zh") or r.get("brand_name_en"), 80) or "—"
        form = cell(r.get("dosage_form"), 40) or "—"
        holder = cell(r.get("license_holder") or r.get("manufacturer"), 40) or "—"
        ind = str(r.get("indication") or "").strip()
        doc = f"[허가사항 문서]({ind})" if PDF.match(ind) else "—"
        rows.append(f"| {k} | {name} | {form} | {holder} | {doc} | {status_label(r, st.get(k, 'valid'))} |")
    return rows


def is_partial(bundle):
    tf = bundle.get("tfda") or {}
    return int(tf.get("total_matches") or 0) > len(tf.get("records") or [])


def block_for(rows, n=None, partial=False, m=None):
    """程式區塊的內容（不含標記）：n 列的表＋說明句；n 預設 min(5, 總數)；沒有任何紀錄時是 NONE_LINE 一句"""
    if not rows:
        return [NONE_LINE]
    m = len(rows) if m is None else m
    n = min(5, len(rows)) if n is None else min(n, len(rows))
    out = HEAD + rows[:n]
    if partial:
        out += ["", SHOW_PART.format(m=m, n=n) if n < m else PART_ALL.format(m=m)]
    elif m > n:
        out += ["", SHOW.format(m=m, n=n)]
    return out


def program_rows(bundle, pins=()):
    """快照用：(程式表最多可列的列, 全部可列的列數, partial)"""
    rows = table_rows(bundle, pins)
    return rows[:MAX_ROWS], len(rows), is_partial(bundle)


PINS_FILE = ROOT / "config" / "license_table_pins.json"
_PINS = None


def pins_for(stem):
    global _PINS
    if _PINS is None:
        _PINS = json.loads(PINS_FILE.read_text(encoding="utf-8")).get("pins", {}) if PINS_FILE.exists() else {}
    return _PINS.get(stem) or _PINS.get(stem.replace("-", "_")) or _PINS.get(stem.replace("_", "-")) or []


def strip_marks(lines):
    return [l for l in lines if l.strip() not in (BEGIN, END)]


def wrap(block):
    return [BEGIN, ""] + block + ["", END]


def bounds(lines):
    """第一個市場段落（## 한국 시판 정보）的 (標題下一行, 段落結尾)；沒有回 (None, None)"""
    for i, ln in enumerate(lines):
        m = re.match(r"^(#{2,3}) (.+?)\s*$", ln)
        if m and m.group(2) in SECS:
            lv = len(m.group(1))
            j = next((k for k in range(i + 1, len(lines)) if re.match(rf"^#{{1,{lv}}} ", lines[k])), len(lines))
            return i + 1, j
    return None, None


def _first_table(lines, a, b):
    tb = [k for k in range(a, b) if lines[k].startswith("|")]
    if not tb:
        return None, None
    x = y = tb[0]
    while y + 1 < b and lines[y + 1].startswith("|"):
        y += 1
    return x, y


def table_ids(text):
    """市場段落第一張表的허가번호（依序）；給建 pins 用"""
    lines = strip_marks(text.replace("\r\n", "\n").split("\n"))
    a, b = bounds(lines)
    if a is None:
        return None
    x, y = _first_table(lines, a, b)
    if x is None:
        return None
    out = []
    for ln in lines[x + 2:y + 1]:
        m = re.search(r"\b\d{9}\b", ln.strip().strip("|").split("|")[0])
        if m and m.group(0) not in out:
            out.append(m.group(0))
    return out


def process(text, rows, partial=False, m=None, add_if_missing=True):
    """回傳新內容（沒變回 None）"""
    lines = strip_marks(text.split("\n"))
    a, b = bounds(lines)
    if a is None:
        t2 = add_section("\n".join(lines), rows, partial, m) if add_if_missing else None
        return t2 if t2 and t2 != text else None
    x, y = _first_table(lines, a, b)
    if x is None:
        if not add_if_missing:
            return None
        rest = [l for l in lines[a:b] if l.strip() != NONE_LINE and not SHOW_RX.match(l.strip())]
        lines = lines[:a] + [""] + wrap(block_for(rows, None, partial, m)) + [""] + rest + lines[b:]
    else:
        n = min(MAX_ROWS, max(1, y - x - 1))
        rest = [l for l in lines[y + 1:b] if not SHOW_RX.match(l.strip()) and l.strip() != NONE_LINE and not CAPTION_RX.match(l.strip())]
        lines = lines[:x] + ([""] if lines[x - 1].strip() else []) + wrap(block_for(rows, n, partial, m)) + [""] + rest + lines[b:]
    t2 = re.sub(r"\n{3,}", "\n\n", "\n".join(lines))
    return t2 if t2 != text else None


# 2026-11-24 第三輪（用戶決定，比照 JpTxGNN 第二輪）：公開頁沒有「## 한국 시판 정보」段落、但證據包有허가紀錄的，補一個段落放程式表。
# 位置：「## 안전성 고려사항」之前（預測頁的固定順序）；沒有就「## 결론 및 다음 단계」之前；再沒有（已知用途頁）就「## 면책 조항」之前。
# noindex 頁與證據包沒有紀錄的頁不補。
ADD_BEFORE = ("안전성 고려사항", "결론 및 다음 단계", "면책 조항")


def add_section(text, rows, partial=False, m=None):
    fm = text.split("---", 2)[1] if text.startswith("---") else ""
    if re.search(r"^noindex:\s*true", fm, re.M) or not rows:
        return None
    lines = text.split("\n")
    heads = {mm.group(1): i for i, l in enumerate(lines) for mm in [re.match(r"^## (.+?)\s*$", l)] if mm}
    at = next((heads[h] for h in ADD_BEFORE if h in heads), None)
    if at is None:
        return None
    sec = ["## " + SECS[0], ""] + wrap(block_for(rows, None, partial, m)) + [""]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(lines[:at] + sec + lines[at:]))


def carry_block(old_text, new_text):
    """sync_notes_to_docs.py 重寫整頁時用：舊頁的程式區塊移植到新頁的市場段落，取代新頁模型寫的第一張表；
    新頁段落沒有表時接在標題下。舊頁沒有程式區塊就原樣回傳新頁。"""
    old = old_text.replace("\r\n", "\n").split("\n")
    if BEGIN not in old or END not in old:
        return new_text
    blk = old[old.index(BEGIN):old.index(END) + 1]
    lines = strip_marks(new_text.split("\n"))
    a, b = bounds(lines)
    if a is None:
        return new_text
    x, y = _first_table(lines, a, b)
    if x is None:
        out = lines[:a] + [""] + blk + [""] + lines[a:]
    else:
        rest = [l for l in lines[y + 1:b] if not SHOW_RX.match(l.strip()) and not CAPTION_RX.match(l.strip())]
        out = lines[:x] + [""] + blk + [""] + rest + lines[b:]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out))


def bundle_file(stem):
    for key in dict.fromkeys((stem, stem.replace("-", "_"), stem.replace("_", "-"))):
        f = ROOT / "data/bundles" / key / "drug_bundle.json"
        if f.exists():
            return f
    return None


def _snapshot():
    return json.loads(gzip.open(SNAP).read().decode("utf-8")).get("drugs", {}) if SNAP.exists() else {}


def run(only=None, dry=False, from_snapshot=False):
    """全站（或 only 指定的頁）重排程式表。回傳改到的頁（檔名去 .md）。
    證據包模式：沒有 data/bundles 就什麼都不做。快照模式：只處理快照裡有 rows 的頁，不在段落沒有表的頁補表。"""
    changed = []
    snap = _snapshot() if from_snapshot else None
    if not from_snapshot and not (ROOT / "data/bundles").is_dir():
        return changed
    for page in sorted((ROOT / "docs/_drugs").glob("*.md")):
        if only and page.stem not in only:
            continue
        raw = page.read_bytes().decode("utf-8")
        if "layout: id_redirect" in raw[:3000] or 'http-equiv="refresh"' in raw[:3000]:
            continue
        if from_snapshot:
            e = snap.get(page.stem)
            if not e or "rows" not in e:
                continue
            rows, m, partial = e["rows"], e.get("nrows", len(e["rows"])), bool(e.get("partial"))
            add = False
        else:
            bf = bundle_file(page.stem)
            if bf is None:
                continue
            b = json.loads(bf.read_text(encoding="utf-8"))
            rows = table_rows(b, pins_for(page.stem))
            m, partial, add = len(rows), is_partial(b), True
        crlf = "\r\n" in raw[:500]
        new = process(raw.replace("\r\n", "\n"), rows, partial, m, add)
        if new is None:
            continue
        changed.append(page.stem)
        if not dry:
            page.write_bytes((new.replace("\n", "\r\n") if crlf else new).encode("utf-8"))
    return changed


if __name__ == "__main__":
    a = sys.argv[1:]
    ch = run({x for x in a if not x.startswith("--")} or None, "--dry-run" in a, "--from-snapshot" in a)
    print(f"許可證表{'（試跑）' if '--dry-run' in a else ''}{'（依快照）' if '--from-snapshot' in a else ''}改 {len(ch)} 頁")
