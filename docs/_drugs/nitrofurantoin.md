---
layout: default
title: Nitrofurantoin
parent: 僅模型預測 (L5)
nav_order: 311
evidence_level: L5
indication_count: 10
---

# Nitrofurantoin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Nitrofurantoin: 요로감염(UTI)에서 류마티스 관절염으로

## 한 문장 요약

Nitrofurantoin은 니트로푸란(nitrofuran) 계열의 항균제로, 일반적으로 요로감염(UTI) 치료에 사용되어 온 약물입니다.
TxGNN 모델은 **류마티스 관절염(Rheumatoid Arthritis)**에 효과가 있을 수 있다고 예측(점수 99.89%)하지만,
확보된 **문헌 12편**을 검토한 결과 치료 효능이 아니라 **간질성 폐섬유화·RA 악화 위험 등 안전성 경고**를 시사하는 내용이 대부분이며, 관련 **임상시험은 0건**입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 요로감염(UTI) *(일반 약리학적 정보이며, 국내 허가 데이터는 확인되지 않음)* |
| 예측 신규 적응증 | 류마티스 관절염 (Rheumatoid Arthritis) |
| TxGNN 예측 점수 | 99.89% |
| 근거 수준 | L4 (단, 치료 효능이 아닌 안전성 신호 중심) |
| 한국 시판 현황 | 미출시 (시판 안 됨) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터가 없습니다. 알려진 정보에 따르면 Nitrofurantoin은 니트로푸란 계열 항균제로 세균 효소계를 손상시켜 살균 작용을 하는 약물이며, 항염증이나 면역조절 기전은 보고된 바 없습니다.

수집된 문헌을 검토한 결과, 이번 예측을 뒷받침하는 치료적 근거는 확인되지 않았습니다. 오히려 두 가지 방향의 안전성 신호가 두드러집니다: ① Nitrofurantoin은 약물유발 간질성 폐섬유화(interstitial lung fibrosis/ILD)를 일으키는 것으로 알려진 약물 중 하나이며, RA 환자에서 이러한 폐질환은 감별진단이 필요한 중요한 합병증으로 다뤄집니다. ② 자기대조 환자군 연구(self-controlled case series, PMID 31222078)에서는 항생제 노출이 RA **악화(flare)**와 연관된다는 결과가 나와, 오히려 위험 증가 방향을 시사합니다.

종합하면, TxGNN의 높은 예측 점수는 실제 치료 기전이 아니라 "Nitrofurantoin—부작용(폐섬유화)—RA" 라는 공통 노드를 통해 지식그래프 상에서 형성된 **간접 연결(노이즈)**일 가능성이 높습니다. 즉 부작용 관련 문헌이 치료 연관 근거로 오인되었을 소지가 큽니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [31222078](https://pubmed.ncbi.nlm.nih.gov/31222078/) | 2019 | 자기대조 환자군 연구 | Scientific Reports | 항생제 노출과 RA 악화(flare)의 연관성 분석. 방향성은 위험 증가 쪽 |
| [3335140](https://pubmed.ncbi.nlm.nih.gov/3335140/) | 1988 | 코호트 | Chest | RA 환자의 간질성 폐섬유화 입원 사례, 예후 불량과 연관 |
| [35145797](https://pubmed.ncbi.nlm.nih.gov/35145797/) | 2022 | 증례 보고 | Cureus | RA 환자에서 Methotrexate+Nitrofurantoin 병용으로 비가역적 폐섬유화 발생 |
| [15195196](https://pubmed.ncbi.nlm.nih.gov/15195196/) | 2004 | 리뷰 | Saudi Med J | 약물유발 폐섬유화 개관, Nitrofurantoin과 RA를 각각 원인/소인으로 병기 |
| [25362778](https://pubmed.ncbi.nlm.nih.gov/25362778/) | 2014 | 리뷰 | La Revue du praticien | 약물유발 간질성 폐질환 개관, Nitrofurantoin 포함 |
| [41635325](https://pubmed.ncbi.nlm.nih.gov/41635325/) | 2026 | 증례 보고 | Cureus | 자가면역성 간염 감별진단 목록에 Nitrofurantoin·RA 언급 |
| [11937933](https://pubmed.ncbi.nlm.nih.gov/11937933/) | 2002 | 증례 보고 | Ann Dermatol Venereol | Nitrofurantoin 등 약물유발 타액선염 사례 (RA와 직접 연관성 낮음) |

*나머지 5편(PMID 899886, 8104358, 4608019, 5401858, 4933314)은 초록이 없거나 RA와의 직접적 연관성이 확인되지 않아 제외했습니다.*

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

> 참고: 본 Evidence Pack의 다른 예측 적응증 검토 과정에서, Nitrofurantoin은 **메트헤모글로빈혈증(methemoglobinemia)** 유발이 문헌상 명확히 확인되는 약물로 나타났습니다(신생아·G6PD 결핍자 특히 주의). 이는 치료 기회가 아니라 **기존에 알려진 위해 반응**이므로 임상 적용 검토 시 반드시 유의해야 합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 점수는 99.89%로 높지만, 실제 문헌 근거는 RA 치료 효능이 아니라 Nitrofurantoin의 알려진 부작용(간질성 폐섬유화, RA 악화 가능성)을 다루고 있습니다. 관련 임상시험이 전무하고, 기전적 연결고리도 없어 지식그래프 노이즈(부작용 문헌의 오인 매칭)일 가능성이 높습니다.

**진행하려면 필요한 것:**
- TFDA(국내 규제기관) 허가사항·경고문 확보 — 현재 Blocking 데이터 갭 (DG001)
- DrugBank 기반 상세 작용기전(MOA) 확인 — 현재 High 우선순위 데이터 갭 (DG002)
- 문헌 12편에 대한 relevance 재분류 완료(현재 다수 "pending" 상태)
- 국내 시판 여부 재확인 (현재 허가 0건으로 기록됨)
- 참고로 본 Evidence Pack의 예측 적응증 2~10위 역시 모두 Hold로 평가되었으며, 대부분 초희귀 유전질환(지식그래프 잡음) 또는 methemoglobinemia와 같은 기존 부작용과의 오인 매칭으로 판단됩니다. 별도 후보로서 추가 검토할 가치는 낮습니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

