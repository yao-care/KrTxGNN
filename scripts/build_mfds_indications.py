#!/usr/bin/env python3
"""MFDS 허가사항 효능·효과 原文 → docs/_data/mfds_original_indications.json（2026-11-15 建）。

MFDS 의약품안전나라 허가 자료的效能·效果（EE_DOC）欄位是 PDF 下載網址，產線照抄，頁面「기존 적응증」與搜尋索引的
original 因此只有網址或「無法確認原文」。這支把證據包（data/bundles/<bundle>/drug_bundle.json）裡本藥單方許可證的
EE PDF 轉出的文字（母目錄 .claude/kr_mfds_ee_20261023.py 下載＋pdftotext 的快取，.claude/cache/kr_mfds_ee/<許可證號>.txt）
整理成一份資料檔，每筆附許可證號與 PDF 網址（來源）。不用模型、不改寫原文，只合併 PDF 換行與空白、相同段落去重。

用到這份資料的：
  - scripts/link_mfds_pdfs.py：快速總覽「기존 적응증」列（網址或「確認不到原文」的列）改成原文摘要＋PDF 連結，description 同步；
  - docs/data/search-index.json 的 original（SMART 結果卡的「기존 적응증」）。
PDF 不在快取的藥不寫（頁面維持 PDF 連結）。nedrug 會擋雲端主機，要補下載時在本機跑母目錄 kr_mfds_ee_20261023.py。

用法：python3 scripts/build_mfds_indications.py --bundles <data/bundles 目錄> --cache <kr_mfds_ee 快取目錄>
"""
import argparse
import gzip
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs/_data/mfds_original_indications.json"
SNAP = ROOT / "snapshots/kr_licenses.json.gz"
URL = re.compile(r"https://nedrug\.mfds\.go\.kr/pbp/cmn/pdfDownload/(\d+)/EE")
HANGUL = "가-힣"


def clean(text: str) -> str:
    t = text.replace("\r", "").replace("\f", "\n")
    t = re.sub(r"\n{3,}", " ", t)  # 3 個以上換行＝段落（標題與內文之間），留空白；2 個＝排版折行，下面依字元決定接不接
    t = re.sub(rf"(?<=[{HANGUL}0-9A-Za-z(,·ㆍ])\n+(?=[{HANGUL}0-9A-Za-z)])", lambda m: "" if "\n\n" in m.group(0) else " ", t)
    t = re.sub(r"\s*\n\s*", " ", t)
    return re.sub(r"[ \t]+", " ", t).strip()


def single_ingredient_records(bundle: dict):
    """證據包許可證紀錄裡的單方產品（同母目錄 .claude/known_use_filter._single_records：複方的適應症不能算到每個成分頭上）"""
    dr = (bundle or {}).get("drug") or {}
    stem = next((w for w in re.findall(r"[a-z]{5,}", str(dr.get("inn") or dr.get("name") or "").lower())), "")
    for v in (bundle or {}).values():
        if isinstance(v, dict) and isinstance(v.get("records"), list):
            for r in v["records"]:
                if not isinstance(r, dict):
                    continue
                ing = str(r.get("ingredients") or "")
                ings = [i for i in ing.split(";;") if i.strip()]
                if r.get("kind") == "combo" or len(ings) > 1 or str(r.get("active_ingredient") or "").count("[") > 1:
                    continue
                if stem and re.fullmatch(r"[A-Za-z0-9 ,.()\-]+", ing) and stem[:5] not in ing.lower():
                    continue
                yield r


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bundles", required=True)
    ap.add_argument("--cache", required=True)
    a = ap.parse_args()
    bundles, cache = Path(a.bundles), Path(a.cache)
    snap = json.loads(gzip.open(SNAP).read())["drugs"] if SNAP.exists() else {}
    idx = json.loads((ROOT / "docs/data/search-index.json").read_text(encoding="utf-8"))["drugs"]
    out, miss = {}, []
    for d in idx:
        slug = d["slug"]
        e = snap.get(slug) or snap.get(slug.replace("-", "_")) or {}
        f = bundles / (e.get("bundle") or slug.replace("-", "_")) / "drug_bundle.json"
        if not f.exists():
            continue
        b = json.loads(f.read_text(encoding="utf-8"))
        ids = []
        for rec in single_ingredient_records(b):
            m = URL.search(str(rec.get("indication") or ""))
            if m and m.group(1) not in ids:
                ids.append(m.group(1))
        texts, used = [], []
        for i in ids:
            c = cache / f"{i}.txt"
            if c.exists() and c.stat().st_size > 20:
                t = clean(c.read_text(encoding="utf-8", errors="replace"))
                if t and t not in texts:
                    texts.append(t)
                    used.append(i)
        if not texts:
            if ids:
                miss.append(slug)
            continue
        out[slug] = {"text": texts[0], "more_texts": len(texts) - 1, "license_ids": used,
                     "sources": [f"https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/{i}/EE" for i in used]}
    doc = {"_doc": "MFDS 허가사항 효능·효과 原文（PDF 轉文字）。scripts/build_mfds_indications.py 產生；text＝本藥第一張單方許可證的原文，"
                   "license_ids／sources＝來源許可證號與 PDF。不改寫原文。",
           "generated_from": {"bundles": "data/bundles（Release data-20261112-162414）", "cache": "母目錄 .claude/cache/kr_mfds_ee（2026-10-23 下載）"},
           "drugs": dict(sorted(out.items()))}
    OUT.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"寫入 {len(out)} 個藥；有 PDF 網址但快取沒有原文 {len(miss)} 個：{', '.join(miss[:20])}")


if __name__ == "__main__":
    sys.exit(main())
