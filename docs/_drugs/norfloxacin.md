---
layout: default
title: Norfloxacin
parent: 모델 예측만 (L5)
nav_order: 554
evidence_level: L5
indication_count: 10
monitor_inn: "NORFLOXACIN"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "punctate epithelial keratoconjunctivitis", "premalignant hematological system disease", "diffuse scleroderma", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague"]
last_modified_at: 2026-10-23
description: "Norfloxacin: 예측 신규 적응증 고아밀라아제혈증 (근거 수준 L5). 기존 적응증: 허가 적응증 본문이 확인되지 않음 (허가 문서 링크만 제공됨)"
---

# Norfloxacin
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
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

## Norfloxacin: 세균 감염에서 고아밀라아제혈증으로
{: .text-alpha }

## 한 문장 요약

Norfloxacin은 플루오로퀴놀론 계열 항균제로, 한국에서 단일 성분 제품으로 허가되어 있습니다. TxGNN 모델은 **고아밀라아제혈증(hyperamylasemia)**에 효과가 있을 수 있다고 예측하지만, 이를 직접 뒷받침하는 임상시험과 문헌은 **0건**입니다. 따라서 현재로서는 모델 예측만 있는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문이 확인되지 않음 (허가 문서 링크만 제공됨) |
| 예측 신규 적응증 | 고아밀라아제혈증 |
| TxGNN 예측 점수 | 0.9970 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 9건 (모두 단일 성분, 유효, 수출용) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 보고서 작성에 사용한 자료에 없습니다. 일반적으로 norfloxacin은 세균의 DNA gyrase와 topoisomerase IV를 억제하는 항균제로 알려져 있습니다.

고아밀라제혈증은 췌장, 침샘, 신장 등 여러 원인으로 나타나는 검사실 소견이며, 감염 자체를 적응증으로 하는 질환이 아닙니다. 항균제의 작용 기전과 이 질환 사이에서 뚜렷한 연결고리는 확인되지 않습니다. 높은 TxGNN 점수는 TxGNN 모델(딥러닝)에서 나온 예측일 뿐이며, 관련 질환 사이에서 모델이 학습한 유사성을 반영할 수 있으나 생물학적 근거는 아닙니다. 이를 지지하는 데이터는 없습니다.

참고로 순위 2~10위의 다른 예측(다클론성 과점성 증후군, 선천성 무알부민혈증, 확산형 피부경화증, 단클론감마병증 등)도 기전적 근거가 없거나 약합니다. 패혈성 페스트는 플루오로퀴놀론 계열의 항균 근거가 일부 있으나, norfloxacin은 전신 노출이 낮아 부적합할 가능성이 큽니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

허가 적응증 본문은 확인되지 않았고 허가 문서 링크만 제공되어, 적응증 칸에는 "허가 문서 참조"로 표기합니다. 모든 허가는 수출용입니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 199701631 | 파마노르플록사신캡슐200밀리그람(수출용) | 캡슐 | 허가 문서 참조 |
| 199703360 | 노플록신정400밀리그람(수출용) | 필름코팅정 | 허가 문서 참조 |
| 199702940 | 휴온스노르플록사신정400mg(수출용) | 필름코팅정 | 허가 문서 참조 |
| 198601049 | 유리스코정400밀리그람(수출용) | 제피정 | 허가 문서 참조 |
| 199701632 | 파마노르플록사신캡슐400밀리그람(수출용) | 캡슐 | 허가 문서 참조 |

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 조회되었으며, 주요(Major) 상호작용으로 다음 약물이 확인되었습니다.
  - 스테로이드: hydrocortisone, triamcinolone, dexamethasone, betamethasone
  - 기타: bupropion, chlorpropamide
- 중등도(Moderate) 상호작용으로는 혈당강하제(acarbose, metformin, pioglitazone, alogliptin, albiglutide, canagliflozin), famotidine, loperamide, 아스피린, 칼슘 제제 등이 있습니다.
- **지식 그래프상 금기 관계**: 허가사항이 아닌 지식 그래프에 기록된 관계입니다. QT 연장 증후군, torsades de pointes, 간부전·간질환, 신장질환, 간질(epilepsy), 정신질환, 말초신경병증, 힘줄염, 당뇨병, 횡문근융해증, 혈소판감소증, 빈혈 등이 포함됩니다.

허가사항의 경고 및 금기 정보는 확보되지 않았으므로 허가 문서를 직접 확인해야 합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
고아밀라아제혈증에 대한 임상시험과 문헌이 전혀 없고 기전적 연결고리도 확인되지 않아, 근거 수준은 L5(모델 예측만 존재)입니다. 안전성 면에서도 지식 그래프상 금기 관계가 많아 신중한 검토가 필요합니다.

**진행하려면 필요한 것:**
- 한국 허가 문서(PDF)에서 적응증, 경고, 금기 정보 확보
- DrugBank 등에서 작용 기전(MOA) 데이터 확보
- 고아밀라아제혈증과 norfloxacin의 연관성을 직접 다룬 연구 탐색
- 시판 및 취소 상태 확인
- 대안으로 근거가 상대적으로 있는 순위 10위(패혈성 페스트)는 연구 질문 수준에서 검토 가능하나, norfloxacin의 낮은 전신 노출이 한계임
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

