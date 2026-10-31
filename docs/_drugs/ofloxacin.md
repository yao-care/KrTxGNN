---
layout: default
title: Ofloxacin
parent: 모델 예측만 (L5)
nav_order: 559
evidence_level: L5
indication_count: 10
monitor_inn: "OFLOXACIN"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague", "congenital hematological disorder", "punctate epithelial keratoconjunctivitis"]
last_modified_at: 2026-10-31
description: "Ofloxacin: 예측 신규 적응증 다발성 과점성 증후군 (근거 수준 L5). 기존 적응증: 허가 문서가 링크로만 제공되어 적응증 본문을 확인할 수 없음 (항균제로 분류)"
---

# Ofloxacin
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

## Ofloxacin: 세균 감염 치료(항균제)에서 다발성 과점성 증후군으로
{: .text-alpha }

## 한 문장 요약

Ofloxacin은 플루오로퀴놀론계 항균제로, 한국에서 점안액·안연고·정제 등으로 시판되는 단일 성분 의약품입니다. TxGNN 모델은 **다발성 과점성 증후군(polyclonal hyperviscosity syndrome)**에 효과가 있을 수 있다고 예측했지만, 이를 뒷받침하는 **임상시험은 0건, 문헌도 0편**입니다. 이 예측은 모델 점수에만 근거한 가설 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 문서가 링크로만 제공되어 적응증 본문을 확인할 수 없음 (항균제로 분류) |
| 예측 신규 적응증 | 다발성 과점성 증후군 |
| TxGNN 예측 점수 | 0.9991 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 20건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 일반적으로 Ofloxacin은 세균의 DNA gyrase와 topoisomerase IV를 억제하는 항균제로 알려져 있습니다.

다발성 과점성 증후군은 면역글로불린 과다로 혈액 점도가 높아지는 상태로, 세균 증식과 관련된 질환이 아닙니다. 따라서 항균 기전과 이 질환 사이에서 설득력 있는 연결고리를 찾기 어렵습니다. 높은 TxGNN 점수는 TxGNN 모델(딥러닝)이 산출한 계산상의 예측일 뿐이며, 모델이 관련 질환 사이에서 학습한 유사성을 반영할 수 있으나 생물학적 근거는 아닙니다. 이를 지지하는 임상시험이나 문헌은 없습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

이 보고서를 위해 수집한 데이터에는 단일 성분 허가 20건(모두 유효)이 있으며, 이 중 주요 5건을 아래에 정리했습니다. 허가 적응증 본문은 허가 문서 링크로만 제공되어 요약할 수 없었습니다. 전체 목록은 일부일 수 있습니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 199203288 | 타리비드점안액 | 점안액 | 허가 문서 링크로만 제공됨 |
| 200404693 | 제뉴원오플록사신정 | 필름코팅정 | 허가 문서 링크로만 제공됨 |
| 201803948 | 오라록신점안액 | 점안액 | 허가 문서 링크로만 제공됨 |
| 199703570 | 안플레임정 | 필름코팅정 | 허가 문서 링크로만 제공됨 |
| 201708371 | 오페란안연고 | 안연고 | 허가 문서 링크로만 제공됨 |

## 안전성 고려사항

허가사항(첨부문서)의 경고·금기 정보는 이번 데이터에 포함되지 않았습니다. 상세 내용은 허가사항을 참조하세요.

- **지식 그래프상 금기 관계**: 아래는 라벨 문구가 아니라 지식 그래프(PrimeKG)에 기록된 관계입니다.
  - QT 연장 증후군, torsades de pointes
  - 간부전·간질환, 신장질환·신기능 장애
  - 간질
  - 말초신경병증, 중증 근무력증
  - 건염, 횡문근융해
  - 당뇨병, 당뇨병성 케톤산증
  - 혈소판감소증, 백혈구감소증
  - *Clostridium difficile* 대장염
- **약물 상호작용**: 총 100건이 조회되었고, 이 중 20건을 확인했습니다.
  - 주요(Major) 등급: hydrocortisone, dexamethasone, betamethasone, triamcinolone, bupropion, chlorpropamide
  - 중등도(Moderate) 등급: metformin, pioglitazone, acarbose 등 혈당강하제, 칼슘·칼륨 제제, 아스피린 등

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 다발성 과점성 증후군에 대한 임상시험과 문헌이 전혀 없고, 항균 기전과 질환의 병태생리 사이에 타당한 연결고리도 확인되지 않아 근거 수준은 L5입니다.
- 지식 그래프에는 말초신경병증 등의 금기 관계도 기록되어 있어, 근거 없이 진행하기에는 안전성 부담이 큽니다.

**진행하려면 필요한 것:**
- 작용 기전(MOA) 자료 확보 및 이 질환과의 기전적 연관성 검토
- 한국 허가사항(적응증, 경고, 금기) 본문의 확보와 분석
- 이 질환을 직접 다룬 전임상 또는 임상 근거
- 참고로 같은 데이터에서 예측된 다른 후보인 **패혈성 페스트(septicemic plague)**는 시험관 내 감수성 연구와 동물 실험이 있어 L4로 평가되었습니다. 우선순위를 높여 별도로 검토할 가치가 있습니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

