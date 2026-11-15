#!/usr/bin/env python3
"""藥物頁「기존 적응증」的 MFDS PDF 網址改成連結文字（2026-11-15 建）。

MFDS 의약품안전나라 허가 자료的效能·效果（EE_DOC）欄位常常不是文字，而是 PDF 下載網址
（https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/<品目基準碼>/EE），產線照抄進頁面，結果：
  - 快速總覽「기존 적응증」列顯示一串網址；
  - front matter description（搜尋結果摘要）也是網址。
2026-11-15 起：docs/_data/mfds_original_indications.json（scripts/build_mfds_indications.py 依 MFDS PDF 轉出的原文）有本藥時，
「기존 적응증」列只有連結或寫「確認不到原文」的，改成「原文摘要（160 字內）＋[MFDS 허가사항 PDF](來源)」，description 同步成原文開頭；
本來就有原文的列不動。
其餘只改呈現，不改事實：
  - 表格列：每個裸網址換成 [MFDS 허가사항 PDF](網址)，網址不變；有文字的部分不動。
  - description：「기존 적응증: 」後面整段都是網址時，換成「MFDS 허가사항(PDF) 참조」；文字與網址混合時只拿掉網址部分。
查核紀錄的 replacement／anchor 所在的行不改（免得紀錄對不上）。search-index 的 original 欄位由母目錄
.claude/rebuild_search_index.py 的 clean_original() 拿掉網址。

誰會跑：scripts/apply_drug_reviews.py（非 --check 時結尾自動跑，所以 sync_notes_to_docs.py 與每週排程之後都會套上）。
gate：scripts/check_seo_docs.py 第 22 項（再跑一次不會變）。

用法：python3 scripts/link_mfds_pdfs.py [--check]
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DRUGS = ROOT / "docs" / "_drugs"
DATA = ROOT / "docs" / "_data" / "drug_reviews.json"
URL = r"https://nedrug\.mfds\.go\.kr/pbp/cmn/pdfDownload/[0-9A-Za-z]+/[A-Za-z]+"
LABEL = "MFDS 허가사항 PDF"
ROW = re.compile(r"^(\| 기존 적응증 \|)(.*)$", re.M)
BARE = re.compile(rf"(?<!\]\()(?<!<)({URL})")
DESC = re.compile(r'^(description:\s*".*?기존 적응증:\s*)(.*?)("\s*)$', re.M)
MFDS_DATA = ROOT / "docs" / "_data" / "mfds_original_indications.json"
CANNOT = re.compile(r"확인할 수 없|확인 불가|링크|PDF|허가증 참조|문구를 확인|제공되지 않|명시되지 않|기재되지 않|참조$")


def _mfds():
    if not MFDS_DATA.exists():
        return {}
    return {k.replace("-", "_"): v for k, v in json.loads(MFDS_DATA.read_text(encoding="utf-8")).get("drugs", {}).items()}


def _short(text, n):
    text = text.replace("|", "／").replace('"', "").strip()
    if len(text) <= n:
        return text
    cut = text[:n]
    i = max(cut.rfind(", "), cut.rfind(" "), cut.rfind("."))
    return (cut[:i] if i > n * 0.6 else cut).rstrip(" ,.;") + "…"


def _needs_text(value):
    plain = re.sub(r"\[[^\]]*\]\([^)]*\)", "", value).strip(" ;,")
    return (not plain) or bool(CANNOT.search(plain))


def _protected():
    out = {}
    if DATA.exists():
        for r in json.loads(DATA.read_text(encoding="utf-8")).get("records", []):
            out.setdefault(r["file"], []).extend(x for x in (r.get("replacement"), r.get("anchor")) if x)
    return out


def fix_text(text, protect=(), data=None):
    def row(m):
        line = m.group(0)
        if any(p and p in line for p in protect):
            return line
        cell = m.group(2).rstrip()
        if data and cell.endswith("|"):
            inner = cell[:-1].strip()
            want = f" {_short(data['text'], 160)} ([{LABEL}]({data['sources'][0]})) |"
            if inner == want[1:-2] or _needs_text(inner):  # 只有連結或「確認不到原文」→ MFDS 原文＋PDF 連結
                return m.group(1) + want
        return m.group(1) + BARE.sub(lambda u: f"[{LABEL}]({u.group(1)})", m.group(2))

    def desc(m):
        val = m.group(2)
        if data and (val.strip() == "MFDS 허가사항(PDF) 참조" or CANNOT.search(val) or re.fullmatch(rf"(\s*{URL}\s*[;；]?)+", val)):
            return m.group(1) + _short(data["text"], 60) + m.group(3)
        if not re.search(URL, val):
            return m.group(0)
        parts = [p.strip() for p in re.split(r"[;；]", val)]
        kept = [p for p in parts if p and not re.fullmatch(URL, p)]
        new = "; ".join(kept) if kept else "MFDS 허가사항(PDF) 참조"
        return m.group(1) + new + m.group(3)

    text = ROW.sub(row, text)
    return DESC.sub(desc, text, count=1)


def run(check=False, only=None):
    prot = _protected()
    mfds = _mfds()
    changed = []
    for p in sorted(DRUGS.glob("*.md")):
        if only and p.name not in only:
            continue
        t = p.read_text(encoding="utf-8")
        n = fix_text(t, prot.get(p.name, ()), mfds.get(p.stem.replace("-", "_")))
        if n != t:
            changed.append(p.name)
            if not check:
                p.write_text(n, encoding="utf-8")
    return changed


def check_errors():
    ch = run(check=True)
    return [f"藥物頁「기존 적응증」還有裸露的 MFDS PDF 網址 {len(ch)} 頁（{', '.join(ch[:5])}…），請跑 python3 scripts/link_mfds_pdfs.py"] if ch else []


if __name__ == "__main__":
    c = run(check="--check" in sys.argv)
    print(f"{'要改' if '--check' in sys.argv else '改了'} {len(c)} 頁")
    sys.exit(1 if c and "--check" in sys.argv else 0)
