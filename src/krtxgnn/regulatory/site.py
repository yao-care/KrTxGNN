"""本站（KrTxGNN）查核機制的在地設定（2026-11-12 建）：頁面文字、資料來源、頁首規則、許可證格式、歷史刪改提交。

同目錄 page_format／licenses／withdrawn 與 scripts/apply_drug_reviews.py、build_license_snapshot.py、reviews_from_edits.py、
check_original_indications.py 都讀這裡；核心流程比照 TwTxGNN 與 UsTxGNN，只有這份是本站自己的寫法。
本站的市場資料是식품의약품안전처（MFDS）의약품안전나라（nedrug）허가 자료（9 碼品目基準코드），頁面文字用韓文。
本站沒有程式產生的許可證表（市場段落的表是報告寫的），所以沒有程式區塊標記。
"""
import re

SITE = "KrTxGNN"
CODE = "kr"
BUNDLE_KEY = "tfda"  # 證據包裡本站市場資料的鍵（收集器沿用的欄位名）

# ---------- 頁首等級（page_format） ----------
LEVEL_LABELS = ["근거 수준"]
HEADER_LABEL = r"근거 수준"
WITHDRAWN = r"철회"
# 頁首規則：2026-11-12 實測 685 頁有總覽等級，頁首全部＝格裡第一個等級（主預測）；整格取最高會有 8 頁不同
HEADER_RULE = "first"
DESC_LEVEL_RE = re.compile(r"근거 수준 (L[1-5]|N/A)")


def desc_level_text(level):
    return "기존 용도만" if level == "N/A" else f"근거 수준 {level}"


DISCLAIMER_RE = re.compile(r"^## 면책 조항\b", re.M)

# ---------- 頁面文字（apply_drug_reviews） ----------
T = {
    "label": {"correct": "검토 정정", "annotate": "검토 주석", "rereview": "재검토 대기", "rereview_result": "재검토 결과"},
    "action": {"correct": "정정", "annotate": "주석 추가", "rereview": "재검토 표시",
               "section": "출처가 있는 단락 추가", "rereview_result": "재검토 완료",
               "header_level": "빠른 개요 기준으로 머리말 근거 수준 재계산",
               "description_level": "페이지 설명의 근거 수준을 머리말 근거 수준으로 변경"},
    "verdict": {"maintain": "유지", "downgrade": "하향", "upgrade": "상향", "withdraw": "철회"},
    "log_head": "## 검토 기록",
    "log_cols": "| 검토일 | 항목 | 처리 | 근거 |",
    "head": "> **{label} ({date})**: ",
    "originally": "원래 문장: “{claim}”",
    "source": "근거: {src}.",
    "decision": "결정 권고: {note}",
    "level_same": "근거 수준 {o} 유지",
    "level_change": "근거 수준 {o} → {n}",
    "table_updated": " 이 페이지의 {labels}은(는) 재검토 결과에 맞게 수정했으며, 원래 값은 아래 검토 기록에 있습니다.",
    "rereviewed": "재검토 표시 → 재검토 완료(재검토 결과 참조)",
    "hdr": "빠른 개요 기준으로 머리말 근거 수준 재계산({o} → {n})",
    "hdr_withdraw": "주 예측이 재검토에서 철회되어 머리말 근거 수준 재계산({o} → {n})",
    "listed_under": ", 「{t}」 목록으로 이동",
    "rr": "재검토: {v}, {c}",
    "tu": "; {l}: “{a}” → “{b}”",
    "desc": "페이지 설명의 「근거 수준 {o}」을(를) 「{n}」(으)로 변경(머리말 근거 수준을 따름; 다른 문구는 그대로, 원문은 기록에 보존)",
    "revised": " ({d} 수정, 이전 판은 기록에 보존)",
    "superseded": "프로그램이 생성한 허가 표로 대체됨(원래: {a})",
    "regen": "보고서가 다시 생성되어 이 문장이 없음({d}: {n}; 원래: {a})",
    "prog": "프로그램 수정 후 이 오류가 없음({d}: {n}; 원래: {a})",
    "wd": "검토 철회({d}: {n}; 원래: {a})",
    "intro": ("이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. "
              "정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다."),
    "intro_levels": "이 페이지의 검토 기록입니다. 머리말 근거 수준은 빠른 개요를 따르며, 모델 예측·개요 표·결론은 고쳐 쓰지 않았습니다.",
    "intro_rr": ("이 페이지의 검토 기록입니다. 정정은 기본적인 사실 진술에 한정되며 모델 예측 원문은 고쳐 쓰지 않았습니다. "
                 "근거 수준과 결정은 재검토 결과(하향·상향·철회)로만 바뀌었으며, 원래 값은 아래 표에 있습니다."),
}

# ---------- 許可證（licenses、build_license_snapshot） ----------
MARKET_SEC = re.compile(r"^## (?:한국 )?시판 정보\s*$")
ID_RE = re.compile(r"\b\d{9}\b")  # nedrug 품목기준코드（2026-11-12 依證據包實測：全部 9 碼數字）


def own_ids(tf):
    return sorted({str(r.get("license_id") or "").strip() for r in tf.get("records") or [] if r.get("license_id")})


# ---------- 刪改轉紀錄（reviews_from_edits） ----------
# 2026-10-31～11-05 的許可證刪改（git log docs/_drugs；排程狀態格、欄位名統一、排除表、AI 重產、description、表格空行不算）
COMMITS = ["d6384d19", "8144daef", "5bce24ee"]
# 期間內以 AI 整份重產報告或套排除表重寫段落的提交
REGEN_COMMITS = ["119fa760", "435b2dab", "d3987ba3", "0d077738", "be98e10f", "a888829f", "f6595a28", "5ead7426", "a68a00d4"]
SOURCES = [{"title": "식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보", "url": "https://nedrug.mfds.go.kr/searchDrug"}]
# 韓文句子以「다.」「요.」等結尾、後面接韓文字，句號加空白就斷句（小數點後沒有空白，不會被斷開）
SENT = re.compile(r"(?<=[.!?])\s+(?=\S)|\n")
PROGRAM_LINES = []
CLASSIFY = [
    ("tw", re.compile(r"대만|TFDA|Taiwan", re.I)),
    ("cancel", re.compile(r"취소|취하|말소|미시판|시판되지 않|시판하지 않|(?:허가|시판)(?:된|받은)? ?이력[^.]{0,4}없|허가되지 않|허가가 없|유효한 허가[^.]{0,6}없")),
    ("count", re.compile(r"\d+\s*건|\d+\s*개|모두 유효|전부 유효|허가증|유효합니다|유효")),
    ("combo", re.compile(r"단일 ?성분|복합(제|제제)?")),
]
SUMMARY = "삭제: “{text}”"
REGEN_NOTE = "2026년 11월 보고서가 다시 생성되어 이 문장이 더 이상 없음"


def reason_kind(reason):
    """人工清單（scripts/license_sentence_fixes.json）的中文理由 → 類別；判斷不了回 None（改用被刪文字分類）"""
    if re.search(r"台灣|TFDA|模板殘留", reason):
        return "tw"
    if re.search(r"취하|취소|註銷|查無|未上市", reason):
        return "cancel"
    if re.search(r"單方|複方", reason):
        return "combo"
    if re.search(r"張|有效|總數", reason):
        return "count"
    return None


def _fig(fc):
    if not fc or fc.get("total") is None:
        return ""
    return (f" 이 약의 허가는 {fc['total']}건(유효 {fc.get('valid') or 0}건)이며, 현재 수치는 빠른 개요와 「한국 시판 정보」의 표에 있습니다.")


def note_for(kind, date, fc):
    d = f"{date} 기준 식품의약품안전처(nedrug) 허가 자료"
    if kind == "tw":
        return "삭제: 대만 TFDA에 관한 템플릿 잔여 문구로, 이 한국 페이지와 관련이 없습니다."
    if kind == "cancel":
        return f"삭제: 허가가 취소되었거나 허가·시판되지 않는다고 했으나, 성분 기준으로 다시 맞춘 {d}와 맞지 않습니다." + _fig(fc)
    if kind == "count":
        return f"삭제: 허가 건수나 상태가 성분 기준으로 다시 맞춘 {d}와 맞지 않습니다." + _fig(fc)
    if kind == "combo":
        return f"삭제: 단일 성분·복합제 여부에 대한 설명이 {d}와 맞지 않습니다." + _fig(fc)
    return f"삭제: 성분 기준으로 다시 맞춘 {d}와 맞지 않습니다." + _fig(fc)


# ---------- 原適應症交叉驗證（check_original_indications） ----------
ORIG_LABELS = ["기존 적응증"]
ORIG_NONE_RE = re.compile(r"^\s*(정보 없음|없음|미기재|확인되지 않|N/A)")
ORIG_SPLIT_RE = re.compile(r"[;,/()·]+|\s및\s|\s또는\s")
