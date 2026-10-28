---
layout: default
title: Lithium Carbonate
parent: 모델 예측만 (L5)
nav_order: 481
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Lithium Carbonate: 예측 신규 적응증 가성무형성증 (Pseudoachondroplasia) (근거 수준 L5). 기존 적응증: 확인 불가 (허가 적응증이 문서 링크로만 제공되어 본문을 확인하지 못함)"
monitor_inn: "LITHIUM CARBONATE"
predicted_indications: ["pseudoachondroplasia", "acromesomelic dysplasia, Hunter-Thompson type", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachyolmia", "myosclerosis", "brachyolmia-amelogenesis imperfecta syndrome", "brachydactyly-syndactyly syndrome", "Behr syndrome", "WHIM syndrome", "combined immunodeficiency due to moesin deficiency"]
---

# Lithium Carbonate
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

## 탄산리튬: 허가 적응증 정보 미확인에서 가성무형성증(Pseudoachondroplasia)으로
{: .text-alpha }

## 한 문장 요약

탄산리튬(Lithium Carbonate)은 한국에서 4건의 단일제 허가를 받아 시판 중인 약물이지만, 이번 데이터에는 허가 적응증의 본문 내용이 포함되어 있지 않습니다.
TxGNN 모델은 **가성무형성증(Pseudoachondroplasia)**에 효과가 있을 수 있다고 예측하며, 예측 점수는 매우 높습니다(0.9998).
그러나 이를 지지하는 **임상시험은 0건**이고, 1순위 질환에 대한 **문헌도 0건**이어서 모델 예측 수준의 근거에 머물러 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (허가 적응증이 문서 링크로만 제공되어 본문을 확인하지 못함) |
| 예측 신규 적응증 | 가성무형성증 (Pseudoachondroplasia) |
| TxGNN 예측 점수 | 0.9998 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 4건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 일반적으로 리튬은 GSK-3β를 억제하고 Wnt/β-catenin 신호전달을 조절하는 것으로 알려져 있으며, 이론적으로는 연골세포 생물학에 영향을 줄 수 있습니다.

가성무형성증은 COMP 유전자 변이로 소포체 스트레스와 연골세포 사멸이 일어나는 질환입니다. 리튬과 이 질환을 직접 연결하는 경로는 이번 데이터에서 확인되지 않았습니다. 따라서 높은 TxGNN 점수는 계산 모델의 예측일 뿐, 기전상 타당성이 검증된 것은 아닙니다.

참고로 2~7순위 예측도 대부분 골격 이형성증 계열(말단중간부 이형성증 Hunter-Thompson형, 단완증 등)이며, 마찬가지로 임상 또는 문헌 근거가 없습니다. 이후 순위에는 Behr 증후군, WHIM 증후군, 모에신 결핍 복합면역결핍증이 포함됩니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 1순위 예측 질환(가성무형성증)에 대한 관련 문헌이 없습니다.

참고로 6순위 예측인 단완증-법랑질형성부전 증후군에서 검색된 1편은 유전성 골격 질환 치료 전반을 다룬 일반 리뷰이며, 리튬에 특화된 근거는 아닙니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [31888683](https://pubmed.ncbi.nlm.nih.gov/31888683/) | 2019 | Review | Orphanet J Rare Dis | 유전성 골격 질환의 치료 환경 변화를 개괄한 리뷰 (6순위 예측 질환 관련, 리튬 특이적 근거 아님) |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201507389 | 명인탄산리튬정150밀리그램 | 분홍색의 원형 정제 | 허가사항 문서 참조 |
| 198500718 | 환인탄산리튬정 | 황색의 원형정제 | 허가사항 문서 참조 |
| 198500638 | 명인탄산리튬정300밀리그램 | 연두색의 원형 정제 | 허가사항 문서 참조 |
| 197300172 | 리단정(탄산리튬) | 흰색 또는 거의 흰색의 정제 | 허가사항 문서 참조 |

## 안전성 고려사항

허가사항 기반의 경고 및 금기 정보는 이번 데이터에 포함되어 있지 않으므로 허가사항을 참조하세요.

- **지식 그래프 기반 금기 질환** (허가 문구가 아닌 모델 지식 그래프의 약물-질환 관계): 신장 질환, 요관 농양, 인지 장애, 갑상선기능저하증, 점액부종, 선천성 갑상선기능저하증, 건선, 유사건선, 심장 돌연사, 심장 전도 질환, 요붕증(신경뇌하수체성·중추성 포함)
- **약물 상호작용**: 총 100건이 조회되었으며, 그중 일부를 아래에 정리했습니다.
  - **주요(Major)**: Bupropion, Lorcaserin
  - **중등도(Moderate)**: Acarbose, Famotidine, Albiglutide, Alogliptin, Metformin, Pioglitazone, Loperamide, Mesalazine, Morphine, Balsalazide, Metronidazole, Canagliflozin, Chlorpropamide, Potassium citrate, Clarithromycin
  - **경미(Minor)**: Doxycycline, Epinephrine, Acetylsalicylic acid
- 리튬은 치료 범위가 좁은 약물로 알려져 있어, 신규 적응증을 검토할 때는 혈중 농도 모니터링과 기형 유발 가능성(특히 사지·골격 질환 관련) 검토가 필요합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
가성무형성증을 포함한 상위 10개 예측 모두 임상시험과 직접 문헌이 없는 모델 예측(L5)입니다. 리튬과 해당 질환 사이의 기전적 연결도 이론적 추정에 불과하며, 허가 적응증과 안전성 정보도 아직 확보되지 않았습니다.

**진행하려면 필요한 것:**
- 한국 허가사항(적응증, 경고, 금기)의 본문 확보 및 분석
- 상세한 약물 작용 기전(MOA) 데이터 보완
- 가성무형성증 등 예측 질환에 대한 리튬 관련 전임상·기전 연구 문헌 조사
- 골격 질환 환자에서의 리튬 안전성(신기능, 갑상선, 심장 전도, 기형 유발성) 평가 계획
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

