---
layout: default
title: Megestrol Acetate
parent: 모델 예측만 (L5)
nav_order: 498
evidence_level: L5
indication_count: 7
monitor_inn: "Megestrol acetate"
predicted_indications: ["hereditary breast ovarian cancer syndrome", "borderline epithelial tumor of ovary", "uterine carcinosarcoma", "placenta cancer", "ovarian clear cell adenocarcinoma", "ovarian cancer", "malignant dysgerminomatous germ cell tumor of ovary"]
last_modified_at: 2026-11-15
description: "Megestrol Acetate: 예측 신규 적응증 유전성 유방암·난소암 증후군 (hereditary breast ovarian cancer syndrome) (근거 수준 L5). 기존 적응증: 암 또는 AIDS 환자의 식욕부진, 악액질 또는 원인불명의 현저한 체중감소의 치료"
---

# Megestrol Acetate
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **7** 건
{: .fs-6 .fw-300 }

---

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 약사 평가 보고서

</div>

## Megestrol acetate: 프로게스틴 계열 호르몬제 → 유전성 유방암·난소암 증후군 (hereditary breast ovarian cancer syndrome)
{: .text-alpha }

## 한 문장 요약

Megestrol acetate는 프로게스테론 수용체를 통해 작용하는 합성 프로게스틴 계열 약물입니다.
TxGNN 모델은 **유전성 유방암·난소암 증후군(hereditary breast ovarian cancer syndrome)**에 효과가 있을 수 있다고 예측합니다.
다만 이 질환을 직접 다룬 **임상시험과 문헌은 각각 0건**이어서, 현재는 모델 예측 수준의 근거만 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 암 또는 AIDS 환자의 식욕부진, 악액질 또는 원인불명의 현저한 체중감소의 치료 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201202081/EE)) |
| 예측 신규 적응증 | 유전성 유방암·난소암 증후군 (hereditary breast ovarian cancer syndrome) |
| TxGNN 예측 점수 | 0.9989 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 16건 / 전체 17건) |
| 허가증 수 | 17건 (유효 16건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Megestrol Acetate 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “여러 연구자들이 메게스트롤아세테이트의 식욕 증진 특성과 악액질에서의 사용 가능성에 대해 보고하였다. 메게스트롤아세테이트가 식욕부진 및 악액질에서 효과를 나타내는 정확한 기전은 현재 알려져 있지 않다.” 영어 원문: "Several investigators have reported on the appetite enhancing property of megestrol acetate and its possible use in cachexia. The precise mechanism by which megestrol acetate produces effects in anorexia and cachexia is unknown at the present time." ([DailyMed: megestrol acetate prescribing information, Upsher-Smith Laboratories, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2dc921d5-e423-4379-a345-151e87d13651), 버전 2026-04-14; 확인일 2026-11-19). 일반적으로 megestrol acetate는 프로게스테론 수용체에 작용하는 프로게스틴 계열 약물로 알려져 있습니다.

그러나 유전성 유방암·난소암 증후군은 BRCA1/2 변이에 따른 **암 소인 증후군**입니다. 호르몬 표적이 뚜렷한 특정 종양 유형이 아니므로, 프로게스틴 치료와의 기전적 연결고리는 약합니다. 높은 예측 점수를 뒷받침할 임상적·문헌적 근거도 확인되지 않았습니다. 따라서 이 예측은 가설 수준으로 보는 것이 적절합니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

이 보고서를 위해 수집한 데이터 기준으로 유효 허가는 16건이며, 아래는 그중 주요 5건입니다. 나머지 허가도 모두 단일 성분 제제입니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201202081 | 애피트롤이에스내복현탁액 | 내복 현탁액 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201202081/EE) 참조 |
| 201706640 | 메게이트현탁액 | 현탁액 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201706640/EE) 참조 |
| 200807473 | 메게시아정40mg | 정제 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200807473/EE) 참조 |
| 200802700 | 메게시아현탁액 | 현탁액 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200802700/EE) 참조 |
| 200807474 | 메게시아정160mg | 정제 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200807474/EE) 참조 |

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 조회되었고, 확인된 항목은 모두 중등도(Moderate)입니다. 주요 항목은 다음과 같습니다.
  - 당뇨병 치료제: acarbose, metformin, pioglitazone, glimepiride, repaglinide, sitagliptin, linagliptin, saxagliptin, alogliptin, canagliflozin, dapagliflozin, empagliflozin, semaglutide, dulaglutide, albiglutide, chlorpropamide, 인슐린 제제(insulin aspart, insulin degludec)
  - 기타: aprepitant, clarithromycin

허가사항상의 경고 및 금기 정보는 이번 데이터에 포함되지 않았으므로, 해당 내용은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 이 질환을 직접 다룬 임상시험과 문헌이 없고 기전적 연결도 약해, 모델 점수(0.9989)만으로는 진행 근거가 부족합니다.

**진행하려면 필요한 것:**
- 유전성 유방암·난소암 증후군(BRCA 변이 보유자)에서 프로게스틴 치료의 효능·예방 가능성을 직접 평가한 연구
- 작용 기전(MOA) 데이터 보완
- 허가사항의 경고·금기 정보 확보 및 안전성 검토
- 당뇨병 치료제 병용 환자에 대한 상호작용 관리 계획

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: megestrol acetate prescribing information, Upsher-Smith Laboratories, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2dc921d5-e423-4379-a345-151e87d13651) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

