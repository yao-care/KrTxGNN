#!/usr/bin/env python3
"""nedrug 現行清單上的新品目依原收集規則補進證據包（2026-11-25 第六輪，用戶決定「新許可補收：全部照原規則補」）。

證據包的 tfda 紀錄有兩套收集規則（2026-03 基準清單＝data/raw/kr_fda_drugs.json 與 ItemPermitDetail.xlsx，只有완제의약품、沒有의약외품）：
  K＝src/krtxgnn/collectors/krfda.py：品目的 주성분（kr_fda_drugs.json 只記第一個成分）→ data/processed/drug_mapping.csv 的 DrugBank ID，
     跟證據包 tfda.drugbank_ids 相交就收；只收 kr_fda_drugs.json 的品目（全為정상），records 最多 20 筆、total_matches 算全部。
     證據包收集時用的對照有兩版（2026-10-12 rescue 前＝drug_mapping.csv.bak_20261012、之後＝drug_mapping.csv）。
  R＝scripts/rebuild_licenses_by_ingredient.py（2026-11-05）：品目成分全文任一成分去鹽類後等於頁名主體就收（各種狀態都收），
     只對原本不是部分紀錄、頁名不是無機鹽等（NO_REBUILD）的證據包做；records 最多 20 筆。R 證據包＝K 的結果再加 R 的結果。
每個證據包先逐包判定規則：照 K（cur／bak 兩版對照）或 K＋R 在 2026-03 基準清單上重算，張數（扣掉 excluded_records、excluded_ids）
正好等於 total_matches、現有紀錄都在重算結果裡的才算重現；重現不出來的整包不補（停損，列出）。
重算結果裡原收集器算進 total_matches、卻沒存成紀錄的品目先回填 tfda.records_not_stored（防重複計數），再補新品目。

新品目＝data/raw/mfds_cancel_status.json（每週排程 license_adapter.fetch() 下載的 nedrug 엑셀다운로드，2026-11-25 起存成分、
品목구분、완제/원료等欄位）裡不在基準清單的品目，收錄規則（第六輪訂的）：
  - 품목구분 不是 의약외품（基準清單沒有의약외품；의약외품是口罩、消毒用酒精、牙膏等）；
  - 완제/원료＝완제의약품（基準清單只有완제의약품；원료의약품是原料藥）；下載檔沒有這個欄位時一律不補（不猜）；
  - 허가일 晚於基準清單最後的허가일（2026-02-27）＝2026-03 之後的新許可；
  - K：第一個主成分（주성분영문 第一段，大寫＝kr_fda_drugs.json 的寫法）在該版 drug_mapping.csv 已有對照就沿用其 DrugBank ID，
       否則用產生 drug_mapping 的同一支 map_fda_drugs_to_drugbank；狀態要是정상（同 kr_fda_drugs.json）；
  - R（只對 R 證據包）：주성분영문 各段照 rebuild 的 base() 比對頁名主體；
  - config/bundle_record_exclusions.json 判為另一個有效成分的不收（record_exclusions.match_text，同收集器）。
每筆欄位同 rebuild（ingredients＝주성분영문，「/」換「;」），另記 source、added；mfds_kind 依現行清單的 주성분（「/」分隔、不重複名稱數）
判斷（kind_source 註明）。records 未滿 20 筆補進，滿了只記號碼在 records_not_stored，都算進 total_matches。只加不刪、可重複執行。
每週 license-refresh.yml 在 license_refresh 前跑（下載檔由上次排程存進 Release；失敗不擋排程）。
用法（repo 根目錄，先還原 data/）：python3 scripts/add_current_licenses.py [--dry-run] [--report out.tsv]
"""
from __future__ import annotations

import csv
import json
import re
import sys
import time
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))
import rebuild_licenses_by_ingredient as RB  # noqa: E402
from krtxgnn.regulatory import record_exclusions as RX  # noqa: E402

RAW = ROOT / "data/raw"
CAP = 20
TYPES = {"의약품", "한약(생약)제제등", "생물의약품", "마약류", "첨단바이오의약품"}  # 基準清單有的품목구분（沒有의약외품）
KIND_SOURCE = "nedrug 엑셀다운로드 주성분 (현행 목록 {d})"


def _mapping(path):
    """drugbank_id → {license_id}，與 original_ingredient（大寫）→ {drugbank_id}"""
    db2lic, ing2db = defaultdict(set), defaultdict(set)
    with open(path, encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            if str(r.get("mapping_success")).strip().lower() not in ("true", "1", "yes"):
                continue
            db = str(r.get("drugbank_id") or "").strip().upper()
            if db:
                db2lic[db].add(str(r.get("license_id") or "").strip())
                ing2db[str(r.get("original_ingredient") or "").strip().upper()].add(db)
    return db2lic, ing2db


class Mapper:
    """新字串用產生 drug_mapping 的同一支 map_fda_drugs_to_drugbank（同一份 drugbank_vocab）"""

    def __init__(self):
        self.cache = {}
        self.fn = None

    def __call__(self, s):
        if s not in self.cache:
            if self.fn is None:
                import pandas as pd
                from krtxgnn.mapping.drugbank_mapper import map_fda_drugs_to_drugbank
                self.pd, self.fn = pd, map_fda_drugs_to_drugbank
            df = self.fn(self.pd.DataFrame([{"주성분": s, "품목기준코드": "x", "품목명": ""}]))
            self.cache[s] = {str(x).upper() for x in df.get("drugbank_id", []) if x and str(x) != "None" and str(x) == str(x)}
        return self.cache[s]


def first_ing(rec):
    return str(rec.get("ingredients_en") or "").split("/")[0].strip().upper()


def kind_now(rec):
    parts = {re.sub(r"\s+", "", p) for p in str(rec.get("ingredients") or "").split("/") if p.strip()}
    return None if not parts else ("single" if len(parts) == 1 else "combo")


def main(argv):
    dry = "--dry-run" in argv
    rep = argv[argv.index("--report") + 1] if "--report" in argv else None
    today = time.strftime("%Y-%m-%d")
    cols = json.loads((RAW / "mfds_cancel_status_columns.json").read_text(encoding="utf-8"))
    cur = json.loads((RAW / "mfds_cancel_status.json").read_text(encoding="utf-8"))
    if len(cur) < 50000:
        raise SystemExit(f"nedrug 下載檔只有 {len(cur)} 筆，疑似不完整，不補")
    if not {"ingredients_en", "item_type", "finished_raw", "permit_date"} <= set(cols.get("saved") or {}):
        print(f"⚠ nedrug 下載檔沒有補收要用的欄位（存了 {sorted(cols.get('saved') or {})}）；這次不補")
        return 0
    status = {r["item_seq"]: r["status"] for r in cur if r.get("status")}
    prods = RB.load_products()                      # 基準清單（kr_fda_drugs.json＋ItemPermitDetail.xlsx）
    kr = {r["품목기준코드"] for r in json.loads((RAW / "kr_fda_drugs.json").read_text(encoding="utf-8"))}
    import openpyxl
    ws = openpyxl.load_workbook(RAW / "ItemPermitDetail.xlsx", read_only=True).active
    ws.reset_dimensions()
    rows = ws.iter_rows(values_only=True)
    head = [str(x or "").strip() for x in next(rows)]
    di = head.index("허가일자")
    cutoff = max(str(r[di] or "") for r in rows)       # 基準清單最後的허가일（20260227）
    cutoff = f"{cutoff[:4]}-{cutoff[4:6]}-{cutoff[6:8]}"
    skipped = defaultdict(int)
    new = []
    for r in cur:
        k = r["item_seq"]
        if k in prods:
            continue
        if (r.get("permit_date") or "") <= cutoff:
            skipped["허가일早於基準清單"] += 1
            continue
        if r.get("item_type") not in TYPES:
            skipped["품목구분=" + str(r.get("item_type"))] += 1
            continue
        if r.get("finished_raw") != "완제의약품":
            skipped["완제/원료=" + str(r.get("finished_raw"))] += 1
            continue
        if not r.get("ingredients_en"):
            skipped["주성분영문空白"] += 1
            continue
        new.append(r)
    maps = {"cur": _mapping(ROOT / "data/processed/drug_mapping.csv"),
            "bak": _mapping(ROOT / "data/processed/drug_mapping.csv.bak_20261012")}
    mapper = Mapper()
    index = {}
    for k, p in prods.items():
        for c in p["_comps"]:
            for keep in (False, True):
                index.setdefault((RB.base(c, keep_salt=keep), keep), set()).add(k)
    nindex = {}
    for r in new:
        for c in RB.components(str(r["ingredients_en"]).replace("/", ";")):
            for keep in (False, True):
                nindex.setdefault((RB.base(c, keep_salt=keep), keep), set()).add(r["item_seq"])
    newby = {r["item_seq"]: r for r in new}
    out_rows, stop, touched, n_add, n_ns, n_back = [], [], 0, 0, 0, 0
    for f in sorted((ROOT / "data/bundles").glob("*/drug_bundle.json")):
        name = f.parent.name
        b = json.loads(f.read_text(encoding="utf-8"))
        t = b.get("tfda") or {}
        recs = t.get("records") or []
        ids = [str(x).upper() for x in t.get("drugbank_ids") or []]
        if not recs and not ids:
            continue
        have = {str(r.get("license_id")) for r in recs}
        ns = set(t.get("records_not_stored") or [])
        exc = {str(r.get("license_id")) for r in t.get("excluded_records") or []} | set(t.get("excluded_ids") or [])
        tm = int(t.get("total_matches") or 0)
        terms, salt = RB.terms_for(name)
        r_ok = bool(terms) and not any(RB.NO_REBUILD.match(x) for x in terms)
        hit = set()
        if r_ok:
            for x in terms:
                hit |= index.get((x, salt), set())
            hit = {k for k in hit if k in status}
        # 判定過的規則存在 tfda.collection_rule（K-cur／K-bak／KR-cur／KR-bak），之後照用（回填 records_not_stored 後不再重判）
        saved = t.get("collection_rule")
        if saved:
            opts = [(saved.split("-")[1], saved.startswith("KR"))]
        else:
            rebuilt = any((r.get("source") or "") == RB.SOURCE for r in recs)
            opts = [(v, r_ok and (rebuilt or tm <= len(recs))) for v in ("cur", "bak")]
        rule = None
        for v, use_r in opts:
            ks = {lic for d in ids for lic in maps[v][0].get(d, ())} & kr
            h = hit if use_r else set()
            uni = ks | h | have | ns
            if len(uni - exc) == tm and have <= (ks | h | have):
                rule, base_set = v, uni - exc
                break
        if rule is None:
            if recs:
                stop.append(name)
            continue
        # 新品目
        cand = set()
        for r in new:
            if r["status"] != "정상":
                continue
            fi = first_ing(r)
            dbs = maps[rule][1].get(fi) or mapper(fi)
            if dbs & set(ids):
                cand.add(r["item_seq"])
        if use_r:
            for x in terms:
                cand |= nindex.get((x, salt), set())
        cand = {k for k in cand if not RX.match_text(name, str(newby[k]["ingredients_en"]).replace("/", ";"))}
        add_ids = sorted(cand - base_set - exc)
        back = sorted(base_set - have - ns)
        if not add_ids and not back:
            continue
        add = []
        for k in add_ids:
            r = newby[k]
            st = r["status"]
            p = {"license_id": k, "brand_name_zh": r.get("product") or "", "brand_name_en": r.get("product_en") or "",
                 "ingredients": str(r.get("ingredients_en") or "").replace("/", ";"),
                 "indication": f"https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/{k}/EE", "dosage_form": r.get("dosage_form") or "",
                 "manufacturer": r.get("company") or "", "license_holder": r.get("company") or "",
                 "approval_date": r.get("permit_date") or "", "expiry_date": "",
                 "status": st, "license_status": "valid" if st == "정상" else "cancelled",
                 "source": f"nedrug 엑셀다운로드 현행 목록 {cols.get('downloaded')} (new item after the 2026-03 baseline; "
                           f"{'K: drug_mapping.csv' + ('' if rule == 'cur' else '.bak_20261012') + ' DrugBank ID, same rule as collectors/krfda.py' if not use_r else 'K+R: krfda DrugBank ID / 2026-11-05 rebuild by ingredient'})",
                 "added": today}
            kd = kind_now(r)
            if kd:
                p.update(mfds_kind=kd, main_ingredients=r.get("ingredients"), kind_source=KIND_SOURCE.format(d=cols.get("downloaded")))
            add.append(p)
        add.sort(key=lambda p: (p["license_status"] != "valid", p.get("mfds_kind") != "single", p["license_id"]))
        room = max(0, CAP - len(recs))
        store, rest = add[:room], add[room:]
        new_ns = sorted(ns | set(back) | {p["license_id"] for p in rest})
        out_rows.append(f"{name}\t{rule}{'+R' if use_r else ''}\t{tm}\t{len(back)}\t{len(add)}\t{len(store)}\t"
                        + ";".join(f"{p['license_id']}:{p['brand_name_zh'][:30]}:{p['status']}" for p in add))
        touched += 1; n_add += len(add); n_ns += len(rest); n_back += len(back)
        if dry:
            continue
        t["collection_rule"] = ("KR-" if use_r else "K-") + rule
        t["records"] = recs + store
        if new_ns:
            t["records_not_stored"] = new_ns
        t["total_matches"] = tm + len(add)
        t["found"] = True
        b["tfda"] = t
        f.write_text(json.dumps(b, ensure_ascii=False, indent=2), encoding="utf-8")
    if rep:
        Path(rep).write_text("bundle\trule\told_total\tbackfilled_not_stored\tadded\tstored\tadded_items\n" + "\n".join(out_rows) + "\n",
                             encoding="utf-8")
    print(f"新品目候選 {len(new)} 個（不收：{dict(skipped)}）")
    print(f"補收 {touched} 個證據包：新品目 {n_add} 筆（存進 records {n_add - n_ns}、只算張數 {n_ns}）；回填 records_not_stored {n_back} 個"
          f"{'（試跑，沒寫檔）' if dry else ''}")
    print(f"停損（重算不出原 total_matches，不補）{len(stop)} 包：{', '.join(stop)}")
    return touched


if __name__ == "__main__":
    main(sys.argv[1:])
