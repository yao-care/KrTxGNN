#!/usr/bin/env python3
"""證據包漏收的許可量測（2026-11-25 第五輪，用戶決定「adapter 存成分、量漏收」；只量、不改證據包）。

本藥的主성분코드：證據包紀錄（data/bundles/<藥>/drug_bundle.json 的 tfda.records）在 MFDS ItemPermitDetail.xlsx 주성분명裡
共同出現的 [M코드]（每筆都有的那一個；沒有共同代碼的證據包不量）。
現行清單：data/raw/mfds_cancel_status.json（每週排程 license_adapter.fetch() 下載的 nedrug 엑셀다운로드；2026-11-25 起存
ingredients 等欄位）。來源 A＝ItemPermitDetail.xlsx（2026-03 全量）的品目，來源 B＝現行清單裡 ItemPermitDetail.xlsx 沒有的
品目（之後新許可），依現行清單的成分欄比對本藥韓文成分名（同代碼在 ItemPermitDetail.xlsx 的寫法）。
漏收＝현행 정상、成分含本藥代碼（或名稱）、不在證據包 records／excluded_records／excluded_ids 的品目；
證據包只存部分紀錄（total_matches 多於 records）的，原收集器算進總數、沒存的品目無法分辨，另列「部分收錄」不算進漏收。
用法（repo 根目錄，先還原 data/）：python3 scripts/measure_missing_licenses.py [--json out.json]
"""
import collections
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from krtxgnn.regulatory import ingredients as ING  # noqa: E402

CODE = re.compile(r"\[(M\d+)\]([^|]*)")


def main(argv):
    out_json = argv[argv.index("--json") + 1] if "--json" in argv else None
    main_ = ING.load_main(ROOT / "data/raw")
    cur = json.loads((ROOT / "data/raw/mfds_cancel_status.json").read_text(encoding="utf-8"))
    status = {r["item_seq"]: r.get("status") for r in cur}
    cur_ing = {r["item_seq"]: str(r.get("ingredients") or "") for r in cur if r.get("ingredients")}
    by_code = collections.defaultdict(set)
    names = collections.defaultdict(set)
    for k, v in main_.items():
        for c, n in CODE.findall(v):
            by_code[c].add(k)
            names[c].add(n.strip())
    res, partial_res, nocode = {}, {}, []
    for f in sorted((ROOT / "data/bundles").glob("*/drug_bundle.json")):
        t = json.loads(f.read_text(encoding="utf-8")).get("tfda") or {}
        recs = t.get("records") or []
        if not recs:
            continue
        sets = [{c for c, _ in CODE.findall(main_.get(r["license_id"], ""))} for r in recs]
        common = set.intersection(*sets) if sets and all(sets) else set()
        if len(common) != 1:
            nocode.append(f.parent.name)
            continue
        code = next(iter(common))
        have = {str(r.get("license_id")) for r in recs + (t.get("excluded_records") or [])} | set(t.get("excluded_ids") or [])
        a = {k for k in by_code[code] if status.get(k) == "정상"} - have
        nm = {n for n in names[code] if len(n) >= 2}
        b = {k for k, v in cur_ing.items() if k not in main_ and status.get(k) == "정상"
             and any(n in [p.strip() for p in re.split(r"[|;,/·+]|\[M\d+\]", v)] for n in nm)} - have
        e = {"code": code, "ipd": sorted(a), "new": sorted(b), "records": len(recs), "total_matches": t.get("total_matches")}
        (partial_res if int(t.get("total_matches") or 0) > len(recs) else res)[f.parent.name] = e
    miss = {k: v for k, v in res.items() if v["ipd"] or v["new"]}
    summ = {"bundles_measured": len(res), "partial_bundles": len(partial_res), "no_single_code": len(nocode),
            "current_list_has_ingredients": bool(cur_ing), "current_items": len(cur), "current_items_not_in_ipd": sum(1 for k in status if k not in main_),
            "missing_bundles": len(miss), "missing_ipd": sum(len(v["ipd"]) for v in miss.values()),
            "missing_new": sum(len(v["new"]) for v in miss.values()),
            "partial_candidates_ipd": sum(len(v["ipd"]) for v in partial_res.values())}
    print(json.dumps(summ, ensure_ascii=False))
    if out_json:
        Path(out_json).write_text(json.dumps({"summary": summ, "missing": miss}, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main(sys.argv[1:])
