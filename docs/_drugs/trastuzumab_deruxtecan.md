---
layout: default
title: Trastuzumab Deruxtecan
parent: 모델 예측만 (L5)
nav_order: 755
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Trastuzumab Deruxtecan: 예측 신규 적응증 약물 유발 골다공증 (drug-induced osteoporosis) (근거 수준 L5). 기존 적응증: 허가 적응증 본문이 확인되지 않음 (허가 문서 링크만 제공됨)"
monitor_inn: "TRASTUZUMAB DERUXTECAN"
predicted_indications: ["drug-induced osteoporosis"]
---

# Trastuzumab Deruxtecan
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **1** 건
{: .fs-6 .fw-300 }

---

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 약사 평가 보고서

</div>

# Trastuzumab Deruxtecan: HER2 양성 종양에서 약물 유발 골다공증으로

## 한 문장 요약

Trastuzumab deruxtecan은 HER2를 표적으로 하는 항체-약물 접합체(ADC)로, 한국에서 엔허투주라는 제품명으로 시판되고 있습니다. TxGNN 모델은 **약물 유발 골다공증(drug-induced osteoporosis)**에 효과가 있을 수 있다고 예측하지만, 이를 뒷받침하는 **임상시험은 0건, 문헌도 0편**입니다. 모델 예측만 존재하는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문이 확인되지 않음 (허가 문서 링크만 제공됨) |
| 예측 신규 적응증 | 약물 유발 골다공증 (drug-induced osteoporosis) |
| TxGNN 예측 점수 | 99.31% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

이 보고서를 위해 정리된 데이터에는 상세한 작용 기전 정보가 없습니다. 일반적으로 알려진 바에 따르면, trastuzumab deruxtecan은 HER2 표적 항체에 topoisomerase I 억제 payload(deruxtecan, exatecan 유도체)를 결합한 ADC입니다. 다만 이는 제공된 자료가 아닌 일반 지식에 근거한 설명입니다.

HER2 표적화 또는 topoisomerase I 억제가 약물 유발 골다공증의 예방·치료와 연결되는 생물학적 경로는 확인되지 않습니다. 기존 적응증(종양)과 신규 적응증(골대사 질환) 사이에도 기전상 뚜렷한 연관성을 제시하기 어렵습니다. 오히려 세포독성 payload는 골 회전율에 부정적 영향을 줄 가능성이 있어, 근거 없이 치료 역할을 기대하기는 어렵습니다. TxGNN 점수(0.993)는 그래프 기반 예측일 뿐이며 어떤 시험이나 문헌으로도 뒷받침되지 않습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202203608 | 엔허투주100mg (트라스투주맙데룩스테칸) | 동결 건조 주사제 (바이알, 주사용수에 용해) | 허가 문서 링크로만 제공되어 적응증 본문 확인 불가 |

제조사는 한국다이이찌산쿄(주)입니다.

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 항체-약물 접합체 (topoisomerase I 억제 payload 포함) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 취급 방호 | 세포독성 약물 취급 규정 준수 필요 |

## 안전성 고려사항

허가사항의 경고·금기 정보는 확보되지 않았습니다. 상세 안전성 정보는 허가사항을 참조하세요.

**약물 상호작용**: 총 42건이 확인되었으며, 그중 주요 항목은 다음과 같습니다.

- **Major**: Deferiprone, Samarium (153Sm) lexidronam, Adalimumab, Baricitinib, Certolizumab pegol, Cladribine, Leflunomide, Natalizumab
- **Moderate**: Palifermin, Strontium chloride Sr-89, Roflumilast, Chloramphenicol, Alefacept, Alemtuzumab, Anakinra, Azathioprine, Canakinumab, Dimethyl fumarate, Niraparib

면역억제제 및 골수억제 가능 약물과의 병용이 다수 포함되어 있습니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
임상시험과 문헌 근거가 전혀 없고 모델 예측(L5)만 존재합니다. 기전상 연결고리도 확인되지 않으며, 세포독성 payload가 오히려 골 건강에 불리할 수 있습니다.

**진행하려면 필요한 것:**
- 허가 문서에서 기존 적응증, 경고, 금기 정보 확보 (MFDS 허가사항 PDF 파싱)
- 상세 작용 기전(MOA) 데이터 확보 (DrugBank 조회)
- HER2 또는 topoisomerase I 억제와 골대사 사이의 기전적 연결 가능성에 대한 전임상 근거
- 약물 유발 골다공증 관련 임상시험 또는 문헌 근거 탐색
- 투여 경로 호환성 및 기존 약물과의 유사성 평가
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

