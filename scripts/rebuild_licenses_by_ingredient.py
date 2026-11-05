"""KR 證據包依成分（鹽類／酯類／水合物寫法）補收許可證紀錄（2026-11-05，用戶核准；全程不用 AI）。

原本的許可證紀錄來自 src/krtxgnn/collectors/krfda.py：成分名 → drug_mapping.csv 的 DrugBank ID → 許可證，
所以主성분寫成鹽類／酯類的品目（RETINOL PALMITATE、SUCRALFATE HYDRATE、HYDROUS BENZOYL PEROXIDE…）對到別的
DrugBank ID 或沒對上，沒收進本藥（vitamin_a 只收到 1 張已만료的비나폴로，頁面就寫成미시판；依主성분查有 51 張정상）。

來源（Release 裡的 data/raw，不另外下載）：
- data/raw/kr_fda_drugs.json（主성분、品目名、제형、업체명）與 data/raw/ItemPermitDetail.xlsx（영문성분명）：成分全文。
- data/raw/mfds_cancel_status.json（nedrug 全庫 취소/취하，許可證排程每週更新）：狀態。정상→valid，其他→cancelled（同 license_adapter）。

做法：
1. 本藥成分名：頁名（bundle 目錄名）去掉鹽類／酯類／水合物字尾得到主體（alfuzosin_hydrochloride → alfuzosin），另加同一成分的別名（SYN）。
   頁名本身帶鹽類或 dl-／d-／l- 前綴時，只收同一個鹽／同一寫法（含水合物寫法），不收其他鹽。
2. 品目成分欄（; 或 / 分隔）任一成分去掉鹽類／酯類／水合物字尾後等於本藥主體 → 收（複方也收，與原收集器相同，單方排前面）。
3. 只補收、不刪原有紀錄；原本就是部分紀錄（total_matches 多於 records）的頁不動（看不到被截掉的那些，無法判斷是否重複）。
   無機鹽、單一元素、葡萄糖等（NO_REBUILD）不補收。
4. 張數：total_matches＝原紀錄與新紀錄的不重複品目數；records 超過 20 筆時有效在前、單方在前取 20 筆（頁面寫「최소 N건」）。
5. 補收的紀錄寫 source＝SOURCE，原紀錄不改。
用法（repo 根目錄）：python3 scripts/rebuild_licenses_by_ingredient.py [--dry-run] [--report out.tsv] [頁 ...]
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUNDLES = ROOT / "data/bundles"
RAW = ROOT / "data/raw"
SOURCE = "MFDS 주성분 by ingredient (kr_fda_drugs.json + ItemPermitDetail.xlsx, 2026-11-05 rebuild)"
CAP = 20

SALT = (r"hydrochloride|hcl|hydrobromide|besylate|besilate|maleate|mesylate|mesilate|tartrate|bitartrate|fumarate|hemifumarate|succinate|"
        r"citrate|acetate|diacetate|dipropionate|propionate|valerate|butyrate|phosphate|sulfate|sulphate|nitrate|lactate|gluconate|palmitate|"
        r"hydrate|monohydrate|dihydrate|trihydrate|tetrahydrate|pentahydrate|hexahydrate|sesquihydrate|hemihydrate|anhydrous|hydrous|"
        r"sodium|potassium|calcium|magnesium|disodium|dipotassium|cilexetil|axetil|medoxomil|dihydrochloride|bromide|chloride|iodide|"
        r"tosylate|edisylate|pamoate|embonate|stearate|oleate|mandelate|camsylate|xinafoate|furoate|aceponate|hyclate|trometamol|tromethamine|"
        r"arginine|lysine|meglumine|olamine|erbumine|tert butylamine|benzathine|procaine|esylate|napadisilate")
SALT_RX = re.compile(r"\b(" + SALT + r")\b")
HYD_RX = re.compile(r"\b(hydrate|monohydrate|dihydrate|trihydrate|tetrahydrate|pentahydrate|hexahydrate|sesquihydrate|hemihydrate|anhydrous|hydrous)\b")
# 同一成分的別名（頁名主體 → 成分欄可能的主體寫法）
SYN = {"vitamin a": ["retinol"], "retinol": ["vitamin a"], "acetaminophen": ["paracetamol"], "paracetamol": ["acetaminophen"],
       "ascorbic acid": ["vitamin c"], "cholecalciferol": ["vitamin d3"], "ergocalciferol": ["vitamin d2"],
       "thiamine": ["vitamin b1"], "riboflavin": ["vitamin b2"], "pyridoxine": ["vitamin b6"], "cyanocobalamin": ["vitamin b12"],
       "tocopherol": ["vitamin e"], "alpha tocopherol": ["vitamin e", "tocopherol"], "epinephrine": ["adrenaline"],
       "norepinephrine": ["noradrenaline"], "acetylsalicylic acid": ["aspirin"], "levothyroxine": ["thyroxine"],
       "glyceryl trinitrate": ["nitroglycerin"], "nitroglycerin": ["glyceryl trinitrate"]}
NO_REBUILD = re.compile(r"^(calcium|copper|magnesium|zinc|iron|iodine|potassium|sodium|chromium|selenium|manganese|fluoride|chloride|"
                        r"phosphorus|phosphate|water|glucose|dextrose|oxygen|nitrogen|sodium chloride|potassium chloride|hydrogen peroxide)$")


def norm(x):
    return " ".join(re.sub(r"[^a-z0-9]+", " ", str(x or "").lower()).split())


def base(x, keep_salt=False):
    """成分主體：去掉鹽類／酯類／水合物字尾（keep_salt 時只去水合物）"""
    t = norm(x) if keep_salt else re.sub(r"^(dl|d|l)( alpha)? (?=[a-z]{4})", "", norm(x))  # dl-／d-／l- 前綴：頁名帶前綴時只收同一寫法
    t = (HYD_RX if keep_salt else SALT_RX).sub(" ", t)
    return " ".join(t.split())


def components(text):
    return [c for c in (norm(p) for p in re.split(r"[;/]|\s\+\s", str(text or ""))) if c]


def load_products():
    prods = {}
    for r in json.loads((RAW / "kr_fda_drugs.json").read_text(encoding="utf-8")):
        r = {x: ("" if y is None or (isinstance(y, float) and y != y) else str(y)) for x, y in r.items()}  # NaN → 空字串
        k = r.get("품목기준코드", "").strip()
        if k:
            prods[k] = {"license_id": k, "brand_name_zh": r.get("품목명") or "", "brand_name_en": r.get("영문품목명") or "",
                        "ingredients": r.get("주성분") or "", "indication": r.get("효능효과") or "", "dosage_form": (r.get("제형") or "").strip(),
                        "manufacturer": r.get("업체명") or "", "license_holder": r.get("업체명") or "", "approval_date": "", "expiry_date": "",
                        "_comps": components(r.get("주성분"))}
    ipd = RAW / "ItemPermitDetail.xlsx"
    if ipd.exists():
        import openpyxl
        ws = openpyxl.load_workbook(ipd, read_only=True).active
        ws.reset_dimensions()
        rows = ws.iter_rows(values_only=True)
        head = [str(x or "").strip() for x in next(rows)]
        for row in rows:
            d = dict(zip(head, row))
            k = str(d.get("품목일련번호") or "").strip()
            if not k:
                continue
            comps = components(d.get("영문성분명"))
            if k in prods:
                prods[k]["_comps"] = sorted(set(prods[k]["_comps"]) | set(comps))
            else:
                prods[k] = {"license_id": k, "brand_name_zh": str(d.get("품목명") or ""), "brand_name_en": str(d.get("품목 영문명") or ""),
                            "ingredients": str(d.get("영문성분명") or "").replace("/", ";"), "indication": "",
                            "dosage_form": str(d.get("성상") or "").strip(), "manufacturer": str(d.get("업체명") or ""),
                            "license_holder": str(d.get("업체명") or ""), "approval_date": "", "expiry_date": "", "_comps": comps}
    return prods


def terms_for(page):
    full = norm(page.replace("_", " "))
    salt_named = base(full) != base(full, keep_salt=True)
    b = base(full, keep_salt=salt_named)
    out = {b} | set(SYN.get(b, []))
    return {t for t in out if len(t) >= 4}, salt_named


def main(argv):
    dry = "--dry-run" in argv
    rep = argv[argv.index("--report") + 1] if "--report" in argv else None
    only = [a for a in argv if not a.startswith("--") and (rep is None or a != rep)]
    status = {r["item_seq"]: r["status"] for r in json.loads((RAW / "mfds_cancel_status.json").read_text(encoding="utf-8")) if r.get("status")}
    prods = load_products()
    index = {}
    for k, p in prods.items():
        for c in p["_comps"]:
            for keep in (False, True):
                index.setdefault((base(c, keep_salt=keep), keep), set()).add(k)
    rows, changed = [], 0
    for f in sorted(BUNDLES.glob("*/drug_bundle.json")):
        page = f.parent.name
        if only and page not in only:
            continue
        terms, salt_named = terms_for(page)
        if not terms or any(NO_REBUILD.match(t) for t in terms):
            continue
        b = json.loads(f.read_text(encoding="utf-8"))
        reg = b.get("tfda") or {}
        recs = reg.get("records") or []
        if int(reg.get("total_matches") or 0) > len(recs):
            continue  # 原本就是部分紀錄
        have = {str(r.get("license_id") or "").strip() for r in recs}
        hit = set()
        for t in terms:
            hit |= index.get((t, salt_named), set())
        new = sorted(k for k in hit - have if k in status)  # nedrug 全庫沒有的品目（已刪除的舊號）不收
        if not new:
            continue
        add = []
        for k in new:
            p = {x: y for x, y in prods[k].items() if not x.startswith("_")}
            st = status[k]
            p.update(status=st, license_status="valid" if st == "정상" else "cancelled", source=SOURCE)
            add.append(p)
        allr = recs + add
        ncomp = lambda r: len([c for c in re.split(r"[;/]", str(r.get("ingredients") or "")) if c.strip()])  # noqa: E731
        allr.sort(key=lambda r: (r.get("license_status", "valid") != "valid", ncomp(r) > 1))
        b["tfda"] = dict(reg, found=True, records=allr[:CAP], total_matches=len(allr))
        nv0 = sum(1 for r in recs if r.get("license_status", "valid") == "valid")
        nv1 = sum(1 for r in add if r["license_status"] == "valid")
        rows.append(f"{page}\t{len(recs)}\t{nv0}\t{len(add)}\t{nv1}\t{','.join(sorted(terms))}\t{';'.join(p['license_id'] + ':' + p['status'] for p in add[:30])}")
        changed += 1
        if not dry:
            f.write_text(json.dumps(b, ensure_ascii=False, indent=2), encoding="utf-8")
    if rep:
        Path(rep).write_text("page\told_records\told_valid\tadded\tadded_valid\tterms\tadded_ids\n" + "\n".join(rows) + "\n", encoding="utf-8")
    print(f"補收 {changed} 個證據包，新增 {sum(int(r.split(chr(9))[3]) for r in rows)} 筆紀錄（有效 {sum(int(r.split(chr(9))[4]) for r in rows)}）")


if __name__ == "__main__":
    main(sys.argv[1:])
