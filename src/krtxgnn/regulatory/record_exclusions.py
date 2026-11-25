"""證據包收錯品項的排除規則（2026-11-25 第五輪，用戶決定；規則與依據在 config/bundle_record_exclusions.json，比照 CHTxGNN 第三輪）。

原收集器依 drug_mapping.csv 的 DrugBank ID 收許可證，同一個 ID 底下的另一個有效成分會被收進來（例 benfotiamine、fursultiamine
被收進 thiamine 的鹽類證據包）。規則：證據包名在規則的 bundles 裡，紀錄成分欄（「;」「/」分隔；本站＝drug_mapping.csv 的
normalized_ingredient）有一段符合 family、卻沒有一段符合 keep → 排除。scripts/exclude_mismatched_records.py 與
collectors/krfda.py 共用。
"""
from __future__ import annotations

import json
import re
from functools import lru_cache
from pathlib import Path

CONF = Path(__file__).resolve().parents[3] / "config" / "bundle_record_exclusions.json"


def _norm(s) -> str:
    return re.sub(r"\s+", " ", str(s or "").lower()).strip()


def bundle_key(name) -> str:
    return re.sub(r"[^a-z0-9-]+", "_", _norm(name)).strip("_")


@lru_cache(maxsize=None)
def rules() -> dict:
    """證據包名 → [規則]"""
    out = {}
    for r in json.loads(CONF.read_text(encoding="utf-8")).get("rules") or []:
        for b in r["bundles"]:
            out.setdefault(bundle_key(b), []).append(r)
    return out


def components(ingredients) -> list:
    return [_norm(c) for c in re.split(r"[;/]", str(ingredients or "")) if c.strip()]


def match_text(bundle, ingredients):
    comps = components(ingredients)
    for r in rules().get(bundle_key(bundle), ()):
        fam, keep = re.compile(r["family"]), re.compile(r["keep"])
        if any(fam.search(c) for c in comps) and not any(keep.search(c) for c in comps):
            return r
    return None


def match(bundle, rec):
    """這筆紀錄依規則該排除就回傳規則，否則 None"""
    return match_text(bundle, rec.get("ingredients"))
