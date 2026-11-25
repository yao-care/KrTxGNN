#!/usr/bin/env python3
"""證據包收錯品項移出（2026-11-25 第五輪，用戶決定「收錯的藥全部排除並接進排程」；比照 CHTxGNN 第三輪）。

依 config/bundle_record_exclusions.json（規則在 src/krtxgnn/regulatory/record_exclusions.py），把 data/bundles/*/drug_bundle.json 裡
「同一個 DrugBank ID、但其實是另一個有效成分」的紀錄從 tfda.records 移到 tfda.excluded_records（附 excluded＝第一次排除日、
excluded_reason、excluded_basis），不刪資料。
原收集器只存前 20 筆（total_matches 是全部張數）：沒存成紀錄、但算進 total_matches 的同類品目，依原收集器的同一套對照
（drug_mapping.csv 本藥 DrugBank ID 的品目 ∩ data/raw/kr_fda_drugs.json）找出，記在 tfda.excluded_ids，一併從張數扣掉。
移出後原收集器的其他品目（同一套對照、不在排除規則裡）依原收集器的順序（有效在前、單方在前）補回 records，最多 20 筆，
每筆記 source、added；total_matches＝留下的紀錄與這套對照其餘品目的不重複數。
只移不刪、可重複執行（已移出的不再扣）。每週 license-refresh.yml 在 license_refresh 前先跑；改完要重算證據包事實層與快照。
用法（repo 根目錄，先還原 data/）：python3 scripts/exclude_mismatched_records.py [--dry-run]
"""
import csv
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))
from krtxgnn.regulatory import ingredients as ING  # noqa: E402
from krtxgnn.regulatory import record_exclusions as RX  # noqa: E402

CAP = 20
SOURCE = "MFDS drug_mapping.csv DrugBank ID (same rule as collectors/krfda.py), backfilled after excluding mismatched records 2026-11-25"


def _mapping():
    out = {}
    with open(ROOT / "data/processed/drug_mapping.csv", encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            if str(r.get("mapping_success")).strip().lower() not in ("true", "1", "yes"):
                continue
            db, lic = str(r.get("drugbank_id") or "").strip().upper(), str(r.get("license_id") or "").strip()
            if db and lic:
                out.setdefault(db, {}).setdefault(lic, set()).add(r.get("normalized_ingredient") or "")
    return out


def run(dry=False):
    from rebuild_licenses_by_ingredient import load_products  # 原收集器同一套欄位（kr_fda_drugs.json＋ItemPermitDetail.xlsx）
    today = time.strftime("%Y-%m-%d")
    mp, prods, main = _mapping(), None, None
    status = {r["item_seq"]: r["status"] for r in json.loads((ROOT / "data/raw/mfds_cancel_status.json").read_text(encoding="utf-8")) if r.get("status")}
    moved, touched = 0, []
    for f in sorted((ROOT / "data" / "bundles").glob("*/drug_bundle.json")):
        name = f.parent.name
        if RX.bundle_key(name) not in RX.rules():
            continue
        b = json.loads(f.read_text(encoding="utf-8"))
        t = b.get("tfda") or {}
        keep, out = [], []
        for r in t.get("records") or []:
            rule = RX.match(name, r)
            (out if rule else keep).append(dict(r, excluded=today, excluded_reason=rule["reason"], excluded_basis=rule["basis"]) if rule else r)
        # 原收集器的同一套對照：本藥 DrugBank ID 的品目（只算 kr_fda_drugs.json 有的，同收集器）
        if prods is None:
            prods = load_products()
        uni = {}
        for db in t.get("drugbank_ids") or []:
            for lic, ings in mp.get(db, {}).items():
                if lic in prods:
                    uni.setdefault(lic, set()).update(ings)
        have = {str(r.get("license_id")) for r in keep} | {str(r.get("license_id")) for r in out} \
            | {str(r.get("license_id")) for r in t.get("excluded_records") or []}
        ex_ids = sorted(set(t.get("excluded_ids") or []) | {lic for lic, ings in uni.items() if lic not in have
                                                             and any(RX.match_text(name, i) for i in ings)})
        rest = sorted(lic for lic, ings in uni.items() if lic not in have and lic not in ex_ids and lic in status)
        new_ex = [x for x in ex_ids if x not in set(t.get("excluded_ids") or [])]
        if not out:
            continue  # 只有收集器層級的規則（證據包目前沒有收錯的紀錄，例 amlodipine 的 S-amlodipine）：不動證據包
        add = []
        if len(keep) < CAP and rest:
            if main is None:
                main = ING.load_main(ROOT / "data/raw")
            cand = []
            for lic in rest:
                p = {x: y for x, y in prods[lic].items() if not x.startswith("_")}
                st = status[lic]
                p.update(status=st, license_status="valid" if st == "정상" else "cancelled", source=SOURCE, added=today)
                ING.apply([p], main)
                cand.append(p)
            cand.sort(key=lambda r: (r["license_status"] != "valid", r.get("mfds_kind") != "single", r["license_id"]))
            add = cand[:CAP - len(keep)]
        total = len({str(r.get("license_id")) for r in keep} | set(rest))
        for r in out:
            print(f"  {name}: 移出 {r.get('license_id')} {str(r.get('brand_name_zh'))[:40]}（{str(r.get('ingredients'))[:50]}）")
        print(f"  {name}: 未存成紀錄的同類品目 {len(new_ex)} 個記進 excluded_ids；補回 {len(add)} 筆；total_matches {t.get('total_matches')}→{total}")
        moved += len(out)
        touched.append(name)
        if dry:
            continue
        t["records"] = keep + add
        t["excluded_records"] = (t.get("excluded_records") or []) + out
        t["excluded_ids"] = ex_ids
        t["total_matches"] = total
        t["found"] = bool(t["records"])
        b["tfda"] = t
        f.write_text(json.dumps(b, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"證據包收錯品項：移出 {moved} 筆（{len(touched)} 個證據包）{'（試跑，沒寫檔）' if dry else ''}")
    return touched


if __name__ == "__main__":
    run(dry="--dry-run" in sys.argv[1:])
