#!/usr/bin/env python3
"""證據包每筆許可證紀錄依 MFDS ItemPermitDetail.xlsx 주성분명寫單方／複方（2026-11-25，用戶第五輪決定）。

規則在 src/krtxgnn/regulatory/ingredients.py。可重複執行；只寫 mfds_kind／main_ingredients／kind_source 三欄（欄名理由見 ingredients.py），
excluded_records 也一起寫（排除的紀錄留著當依據）。品目不在 2026-03 的 ItemPermitDetail.xlsx（之後新許可）就不寫 mfds_kind，
reviewer 對這種證據包照舊標 kind_undeterminable（事實層不給單方張數），--report 列出。
每週排程（.github/workflows/license-refresh.yml）在 license_refresh 前跑。
用法（repo 根目錄，先還原 data/）：python3 scripts/set_record_kind.py [--check] [--report out.tsv]
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from krtxgnn.regulatory import ingredients as I  # noqa: E402


def main(argv):
    check = "--check" in argv
    rep = argv[argv.index("--report") + 1] if "--report" in argv else None
    main_ = I.load_main(ROOT / "data/raw")
    files = sorted((ROOT / "data/bundles").glob("*/drug_bundle.json"))
    if not files:
        sys.exit("✗ data/bundles 沒有證據包（先還原 data/）")
    changed, recs, unknown, rows = 0, 0, 0, []
    for f in files:
        b = json.loads(f.read_text(encoding="utf-8"))
        reg = b.get("tfda") or {}
        r, ex = reg.get("records") or [], reg.get("excluded_records") or []
        n = I.apply(r, main_) + I.apply(ex, main_)
        recs += len(r)
        miss = [x["license_id"] for x in r if not x.get("mfds_kind")]
        unknown += len(miss)
        if miss:
            rows.append(f"{f.parent.name}\t{len(miss)}\t{','.join(miss)}")
        if n:
            changed += 1
            if not check:
                f.write_text(json.dumps(b, ensure_ascii=False, indent=2), encoding="utf-8")
    if rep:
        Path(rep).write_text("bundle\tunknown\tids\n" + "\n".join(rows) + "\n", encoding="utf-8")
    print(f"單方／複方（{I.SOURCE}）：{'待改' if check else '改了'} {changed} 個證據包；紀錄 {recs} 筆，"
          f"檔內沒有（之後新許可，判斷不了）{unknown} 筆、{len(rows)} 個證據包")
    if check and changed:
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1:])
