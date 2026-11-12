"""正文許可證張數的程式改寫（2026-11-12 建，本站查核機制；概念比照 TwTxGNN page_postprocess.rewrite_count_prose，規則是本站韓文句型）。

用戶 2026-11-12 決定：正文裡「허가 N건」這類許可證張數敘述，由程式依許可證快照（snapshots/kr_licenses.json.gz 的 facts）改寫，
每週資料更新後跟著改，不逐筆寫查核紀錄（同 Tw：程式改寫的張數敘述是程式產生的正文）。

只改「句型明確、數字確定是本藥許可證張數」的地方，其餘一律不動：
  - 句子要有「허가」（在市場段落「한국 시판 정보」裡可不寫），且沒有試驗／文獻／交互作用／研究等字樣（那些「N건」不是許可證）。
  - 跳過：查核框（<!-- review -->）、程式許可證區塊（<!-- licenses -->）、表格列、標題、front matter、引用框以外的程式說明行；
    查核紀錄 replacement／anchor 所在的句子（改了紀錄會對不上）。
  - 整句不動（列在 skipped）：有保留（최소、일부일 수、전체 목록이 아닐）、出口用、劑型或廠商子集、「이력」、「이 외에」；
    事實層 partial（證據包只收部分許可證）的頁整頁不動。
  - 數字不動：顯示筆數（주요／그중／대표／위·아래 표／이 중／N건만、「M건 중 N건」的 N）。
角色：句中數字前後有「취소」→註銷；有「유효」→有效；有「단일」→單方（句中有「유효」用有效單方）；有「복합」→複方；其餘→總數。
同一行只要有一句含許可證數字而被略過，整行都不動（免得前後句數字對不上）。
同一句另有明確的有效／註銷數字時，沒有限定詞的數字確定是總數。
數字已等於該角色的任一合理讀法（沒有限定詞的「N건」＝總數或有效數）就不動；不等於時，兩種讀法相同才改，不同就列為 ambiguous。
原數字是 0 的句子（「허가 0건으로 조회된 것은…」這類建立在 0 張前提上的句子）不改、列為 zero-premise，要改請寫查核紀錄。
前提檢查：句子說「모두 유효」而有效≠總數、說「모두 단일」而單方≠總數（或有效單方≠有效）時整句不動、列出。
"""
from __future__ import annotations

import re

from . import site as C

SENT_SPLIT = re.compile(r"(?<=[.!?])\s+")
NUM = re.compile(r"(\d[\d,]*)(\s*)건")
LICENSE = re.compile(r"허가")
NOT_LICENSE = re.compile(r"임상|시험|문헌|상호작용|연구|논문|보고서|PMID|NCT|사례|증례|환자|DDI|이상반응|부작용|후보|예측|조회된 것은")
HEDGED = re.compile(r"최소|일부일 수|일부만|일부 기록|전체 목록이 아닐|전체 목록의 일부|이력|이 외에|외에도|이 밖에|그 외|위 외에|나머지|더 있|더 허가|추가로")
SUBSET = re.compile(r"수출용|내수용|제형|정제|주사제|캡슐|크림|겔|연고|외용|점안|시럽|패치|좌제|산제|과립|\(주\)|㈜|제조사|한국[가-힣]*\)")
DISPLAY_LEFT = re.compile(r"(주요|그중|그 중|대표|위에는|아래는|위 표|아래 표|이 중|중)\s*(허가\s*)?$")
BLOCK = re.compile(r"<!-- (review|licenses):begin.*?<!-- \1:end[^>]*-->", re.S)


def _role(s, a, b):
    left, right = s[max(0, a - 14):a], s[b:b + 8]
    if DISPLAY_LEFT.search(left) or right.startswith("만"):
        return "display"
    win = s[max(0, a - 14):b + 10]
    if "취소" in win:
        return "cancelled"
    if "복합" in win:
        return "combo"
    if "단일" in win:
        return "single"
    if "유효" in win:
        return "valid"
    return "total"


def _readings(role, f, sent, explicit=False):
    """(可接受的值, 改寫用的值)。改寫用的值是 None：兩種讀法不同、又沒有限定詞，判斷不了。"""
    t, v, c = f.get("total"), f.get("valid"), f.get("cancelled")
    st, vs = f.get("single_total"), f.get("valid_single")
    validctx = "유효" in sent
    if role == "cancelled":
        return {c}, c
    if role == "valid":
        return {v}, v
    if role == "single":
        if validctx:
            return {vs}, vs
        return {st, vs}, st if st == vs else None
    if role == "combo":
        ct = None if t is None or st is None else t - st
        cv = None if v is None or vs is None else v - vs
        if validctx:
            return {cv}, cv
        return {ct, cv}, ct if ct == cv else None
    if explicit:  # 同一句另有明確的有效／註銷數字：沒有限定詞的那個就是總數
        return {t}, t
    return {t, v}, t if t == v else None


def _premise_ok(sent, f):
    if re.search(r"모두[^.]{0,12}유효|유효합니다|유효 상태", sent) and f.get("valid") != f.get("total"):
        return False
    if re.search(r"모두[^.]{0,12}단일|단일[^.]{0,12}모두", sent):
        if "유효" in sent and f.get("valid_single") != f.get("valid"):
            return False
        if "유효" not in sent and f.get("single_total") != f.get("total"):
            return False
    return True


def rewrite_sentence(sent, f, market=False):
    """回傳 (新句子, 跳過理由或 None)。market：句子在本站市場段落（site.MARKET_SEC）裡，「N건」不寫「허가」也算許可證。"""
    if not ((LICENSE.search(sent) or market) and NUM.search(sent)) or NOT_LICENSE.search(sent):
        return sent, None
    if HEDGED.search(sent) or SUBSET.search(sent):
        return sent, "hedged/subset"
    nums = list(NUM.finditer(sent))
    # 「M건 중 N건」：N 是顯示筆數
    found = []
    for i, m in enumerate(nums):
        if i and re.match(r"\s*중\s*$", sent[nums[i - 1].end():m.start()]):
            continue
        found.append((m, _role(sent, m.start(), m.end())))
    explicit = any(r in ("valid", "cancelled") for _, r in found)
    subs = []
    for m, role in found:
        if role == "display":
            continue
        old = int(m.group(1).replace(",", ""))
        ok, v = _readings(role, f, sent, explicit)
        if old in ok:
            continue
        if v is None:
            return sent, "ambiguous"
        if old == 0:
            return sent, "zero-premise"
        subs.append((m, v))
    if not subs:
        return sent, None
    if not _premise_ok(sent, f):
        return sent, "premise"
    out, pos = [], 0
    for m, v in subs:
        out.append(sent[pos:m.start(1)])
        out.append(f"{v:,}" if "," in m.group(1) else str(v))
        pos = m.end(1)
    out.append(sent[pos:])
    return "".join(out), None


def _line(ln, f, protect, skipped, market=False):
    if ln.startswith(("|", "#")) or not ln.strip():
        return ln
    parts = SENT_SPLIT.split(ln)
    seps = SENT_SPLIT.findall(ln)
    new, held = [], False
    for s in parts:
        if any(p and (p in s or s in p) for p in protect):
            new.append(s)
            continue
        ns, why = rewrite_sentence(s, f, market)
        if why and NUM.search(s) and (LICENSE.search(s) or market):
            skipped.append((why, s.strip()))
            held = True
        new.append(ns)
    if held:  # 同一行有句子判斷不了：整行不動，免得改了一句、旁邊的句子對不上
        return ln
    out = new[0]
    for sep, s in zip(seps, new[1:]):
        out += sep + s
    return out


def rewrite(text, facts, protect=()):
    """text：整頁 markdown。facts：快照的 facts。回傳 (新內容, skipped)。front matter、查核框、程式區塊、表格不動。"""
    skipped = []
    if not facts or facts.get("partial"):
        return text, skipped
    protect = [p.strip() for p in protect if p and len(p.strip()) >= 6]
    fm_end = 0
    if text.startswith("---"):
        j = text.find("\n---", 3)
        fm_end = j + 4 if j > 0 else 0
    body = text[fm_end:]
    # 先把查核框與程式區塊換成佔位，逐行處理（記住目前在哪個 ## 段落），再換回來
    keep = []

    def hold(m):
        keep.append(m.group(0))
        return f"\x00{len(keep) - 1}\x00"
    body = BLOCK.sub(hold, body)
    lines, market = [], False
    for ln in body.split("\n"):
        if ln.startswith("## "):
            market = bool(C.MARKET_SEC.match(ln))
        lines.append(ln if "\x00" in ln else _line(ln, facts, protect, skipped, market))
    body = re.sub(r"\x00(\d+)\x00", lambda m: keep[int(m.group(1))], "\n".join(lines))
    return text[:fm_end] + body, skipped
