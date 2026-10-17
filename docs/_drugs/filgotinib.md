---
layout: default
title: Filgotinib
parent: 모델 예측만 (L5)
nav_order: 346
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Filgotinib: 예측 신규 적응증 HER2 양성 유방암 (HER2 positive breast carcinoma) (근거 수준 L5). 기존 적응증: 허가증에 적응증 텍스트가 없고 허가사항 문서 링크만 제공되어 있어, 허가사항을 직접 확인해야 합니다"
monitor_inn: "Filgotinib"
predicted_indications: ["HER2 positive breast carcinoma", "thrombocytopenia", "hereditary thrombocytopenia with normal platelets", "marcothrombocytopenia with mitral valve insufficiency", "transient neonatal thrombocytopenia", "dense granule disease", "multiple endocrine neoplasia", "homozygous familial hypercholesterolemia", "progesterone-receptor negative breast cancer", "progesterone-receptor positive breast cancer"]
---

# Filgotinib
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

# Filgotinib: 관련 적응증에서 HER2 양성 유방암으로

## 한 문장 요약

Filgotinib은 선택적 JAK1 억제제로, 한국에서 단일제로 허가되어 시판 중입니다.
TxGNN 모델은 **HER2 양성 유방암(HER2 positive breast carcinoma)**에 효과가 있을 수 있다고 예측하지만, 현재 이 방향을 지지하는 **임상시험은 0건**, **문헌도 0편**이어서 모델 예측 단계에 머물러 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가증에 적응증 텍스트가 없고 허가사항 문서 링크만 제공되어 있어, 허가사항을 직접 확인해야 합니다. |
| 예측 신규 적응증 | HER2 양성 유방암 (HER2 positive breast carcinoma) |
| TxGNN 예측 점수 | 98.88% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 2건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 이 보고서용으로 수집된 자료에 없습니다. 다만 약리학 자료에 따르면 Filgotinib은 JAK1을 주 표적으로 하는 억제제이며, JAK2, JAK3, TYK2도 표적 단백질로 확인됩니다. 임상 개발은 류마티스 관절염, 크론병, 궤양성 대장염을 중심으로 진행되었고, 2020년 9월 EU와 일본에서 중등도~중증 류마티스 관절염에 승인되었습니다.

JAK/STAT 신호 전달은 유방암 생물학에 관여하는 것으로 알려져 있습니다. 그러나 JAK1 억제와 HER2 구동 질환 사이의 직접적인 연결고리는 확인된 바 없습니다. 높은 TxGNN 점수는 계산상의 예측일 뿐이며, 이를 뒷받침하는 임상시험이나 문헌이 없습니다. 기존 적응증(자가면역 염증성 질환)과 유방암의 연관성도 아직 평가되지 않았습니다.

참고로 상위 10개 예측 중 7개는 혈소판감소증 관련 질환이며, 유방암 아형이 3개입니다. 이 중 일반 혈소판감소증에서만 문헌 2편이 확인되었으나 간접적인 내용입니다. 한 편은 IL-6와 선택적 JAK 차단을 다룬 리뷰이고, 다른 한 편은 filgotinib 투여 후 면역매개 혈소판감소증이 발생한 증례 보고입니다. 후자는 치료 효과가 아닌 이상반응 신호로, 혈소판감소증 방향의 재창출에는 불리합니다. 두 문헌은 초록이 잘려 있어 원문 확인이 필요합니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202201296 | 지셀레카정100밀리그램 (필고티닙말레산염) | 베이지색 장방형 필름코팅정 (“GSI”/“100” 음각) | 허가사항 문서 참조 |
| 202201295 | 지셀레카정200밀리그램 (필고티닙말레산염) | 베이지색 장방형 필름코팅정 (“GSI”/“200” 음각) | 허가사항 문서 참조 |

두 제품 모두 한국에자이(주)가 보유한 유효 단일제 허가입니다.

## 안전성 고려사항

- **약리학적 표적**: JAK1, JAK2, JAK3, TYK2 (약물 간 상호작용이 아닌 표적 단백질 정보)
- **규제 관련 이력**: 2020년 8월 미국 FDA는 200 mg 용량의 정자 농도 독성 우려로 류마티스 관절염 승인 신청에 대해 보완 요구서(CRL)를 발행했습니다.
- **혈소판감소증 신호**: 궤양성 대장염 환자에서 filgotinib 투여 시작 후 면역매개 혈소판감소증이 보고되었습니다(증례 보고, 인과성 불확실). 혈소판 수 모니터링이 권고됩니다.

그 밖의 경고 및 금기 사항은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
HER2 양성 유방암 예측은 TxGNN 점수(98.88%)만 있고 임상시험과 문헌이 전혀 없는 L5 단계입니다. JAK1 억제와 HER2 구동 질환의 직접적인 기전 연결도 확인되지 않았습니다. 또한 안전성 검토에 필요한 허가사항 경고·금기 정보가 확보되지 않았습니다.

**진행하려면 필요한 것:**
- 한국 허가사항(첨부문서)의 적응증, 경고, 금기 정보 확보
- DrugBank 등에서 상세한 작용 기전(MOA) 데이터 확보
- JAK1 억제와 HER2 양성 유방암 사이의 기전 연구 또는 전임상 근거(세포주·동물 모델)
- 유방암 관련 임상시험 및 문헌 추가 탐색
- 혈소판감소증을 포함한 혈액학적 안전성 평가와 JAK 억제제 계열 위험(암, 심혈관, 혈전, 감염) 검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

