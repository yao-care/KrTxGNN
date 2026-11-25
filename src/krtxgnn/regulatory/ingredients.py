"""品目的單方／複方：依 MFDS ItemPermitDetail.xlsx 的주성분명逐品目判斷（2026-11-25，用戶第五輪決定）。

背景：證據包紀錄的 ingredients 欄只記收集器比對到的那個成分（例 아모크라주「AMOXICILLIN SODIUM」實為 amoxicillin＋clavulanate），
2026-11-24 起事實層把單方／複方標成不可判定。data/raw/ItemPermitDetail.xlsx（MFDS 2026-03 全量 44,072 品目，Release 帶著）的
「주성분명」欄列每個品目的全部有效成分（[M코드]名稱，以「|」分隔），可以逐品目判斷：
  - 不同 M 코드（沒有代碼時算不重複的名稱）只有 1 個＝single，2 個以上＝combo；
  - 品目不在檔內（2026-03 之後新許可）或주성분명空白＝判斷不了，不寫 kind（reviewer 照舊標 kind_undeterminable）；
    第六輪起 scripts/add_current_licenses.py 補收的新品目依 nedrug 현행 목록的주성분（「/」分隔、不重複名稱數）判斷，kind_source 以 nedrug 開頭，這裡不動。
證據包紀錄寫入 mfds_kind、main_ingredients（주성분명原文）、kind_source（reviewer 的 _local_regulatory 讀 mfds_kind 當 kind）。
欄名不用 kind：母目錄 known_use_filter._single_records 讀紀錄的 kind＝combo 會把複方的適應症排出已知用途，2026-11-25 量到
cilastatin、fluorometholone 兩頁各會多一個 kept 預測（頁面預測清單要跟著變），不在這次範圍，已回報待母目錄／用戶決定。
scripts/set_record_kind.py 全站套、
每週排程（license-refresh.yml）在 license_refresh 前跑、依成分重建（rebuild_licenses_by_ingredient.py）新增紀錄時也套。
"""
from __future__ import annotations

import re
from pathlib import Path

SOURCE = "MFDS ItemPermitDetail.xlsx 주성분명 (2026-03)"
_CODE = re.compile(r"\[(M\d+)\]")
FIELDS = ("mfds_kind", "main_ingredients", "kind_source")


def load_main(raw_dir) -> dict:
    """品目일련번호 → 주성분명原文（空白的不收）。讀不到檔就 raise（不准靜默當成沒有資料）。"""
    import openpyxl

    p = Path(raw_dir) / "ItemPermitDetail.xlsx"
    ws = openpyxl.load_workbook(p, read_only=True).active
    ws.reset_dimensions()
    rows = ws.iter_rows(values_only=True)
    head = [str(x or "").strip() for x in next(rows)]
    if "품목일련번호" not in head or "주성분명" not in head:
        raise RuntimeError(f"ItemPermitDetail.xlsx 欄位改變：{head[:12]}")
    i, j = head.index("품목일련번호"), head.index("주성분명")
    out = {}
    for row in rows:
        k, v = str(row[i] or "").strip(), str(row[j] or "").strip()
        if k and v:
            out[k] = v
    if len(out) < 30000:
        raise RuntimeError(f"ItemPermitDetail.xlsx 只讀到 {len(out)} 個品目的주성분명，疑似檔案不完整")
    return out


def components(text) -> list:
    parts = [p.strip() for p in str(text or "").split("|") if p.strip()]
    codes = [c for p in parts for c in _CODE.findall(p)]
    if codes and len(codes) == len(parts):
        return sorted(set(codes))
    return sorted({_CODE.sub("", p).strip() for p in parts})


def kind_of(text):
    n = len(components(text))
    return None if n == 0 else ("single" if n == 1 else "combo")


def apply(records, main) -> int:
    """依 main（load_main 的結果）寫每筆紀錄的 mfds_kind／main_ingredients／kind_source；查不到的拿掉這三欄。回傳改了幾筆。"""
    n = 0
    for r in records or []:
        lid = str(r.get("license_id") or "").strip()
        text = main.get(lid)
        if not text and str(r.get("kind_source") or "").startswith("nedrug"):
            continue  # 2026-11-25 第六輪：2026-03 之後的新品目由 scripts/add_current_licenses.py 依現行清單的주성분判斷，不在檔內就不動
        k = kind_of(text) if text else None
        want = {"mfds_kind": k, "main_ingredients": text, "kind_source": SOURCE} if k else {}
        cur = {x: r.get(x) for x in FIELDS if x in r}
        if cur == want:
            continue
        for x in FIELDS:
            r.pop(x, None)
        r.update(want)
        n += 1
    return n
