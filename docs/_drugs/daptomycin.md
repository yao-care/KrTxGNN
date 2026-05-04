---
layout: default
title: Daptomycin
parent: 僅模型預測 (L5)
nav_order: 195
evidence_level: L5
indication_count: 10
---

# Daptomycin
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

# Daptomycin: 그람양성균 감염증에서 골관절염으로

---

## 한 문장 요약

Daptomycin은 그람양성균에 의한 피부 감염증, 균혈증, 우심 감염성 심내막염 치료에 사용되는 사이클릭 리포펩타이드 계열 항생제입니다. TxGNN 모델은 **골관절염(Osteoarthritis)**을 최우선 신규 적응증으로 예측하였으나, 문헌 분석 결과 이는 훈련 데이터에서 '골관절 감염(osteoarticular infection)'과 '골관절염(osteoarthritis)' 간 언어적 혼동에서 비롯된 위양성일 가능성이 높습니다. 현재 **0건의 임상시험**과 **10편의 문헌**이 검색되었으나, 모두 감염 치료 맥락에 해당하여 골관절염 직접 치료 근거로 볼 수 없습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 그람양성균 피부·연조직 감염증, 황색포도구균 균혈증, 우심 감염성 심내막염 |
| 예측 신규 적응증 | 골관절염 (Osteoarthritis) |
| TxGNN 예측 점수 | 99.86% |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

Daptomycin은 세균의 세포막에 칼슘 의존적으로 삽입되어 막 전위를 교란함으로써 그람양성균을 살균하는 항생제입니다. 임상에서는 허가 적응증(피부 감염, 균혈증, 심내막염) 외에도 인공관절 감염, 골수염 등 **골·관절계 감염(osteoarticular infection)** 치료에 광범위하게 사용됩니다. 이 점이 TxGNN 고득점의 근원적 원인으로 보입니다.

그러나 TxGNN이 예측한 **골관절염(osteoarthritis)은 퇴행성 관절질환**으로, 세균 감염과는 전혀 다른 병인을 가집니다. Daptomycin에는 연골 보호, 골 대사 조절, 또는 관절 퇴화 억제와 관련된 작용 기전이 알려져 있지 않습니다. 검색된 10편의 문헌 역시 예외 없이 '골관절 감염 치료제로서의 Daptomycin' 맥락이며, 골관절염 치료를 탐색한 연구는 단 한 편도 없습니다.

주목해야 할 사실은 **2순위 예측인 류마티스 관절염(Rheumatoid Arthritis, RA)**입니다. 2025년 발표된 전임상 연구에서 Daptomycin의 사이클릭 리포펩타이드 구조가 NF-κB 경로를 억제하고 TNF-α/IL-6/IL-1β 등 염증성 사이토카인을 감소시켜 콜라겐 유도 관절염(CIA) 동물모델에서 관절 증상을 개선함이 처음 보고되었습니다. 이는 항균 작용 이외의 별도 항염 경로를 시사하며, 본 보고서 후반부에서 별도 검토합니다.

---

## 임상시험 근거

현재 골관절염을 대상으로 한 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

검색된 10편의 문헌은 모두 골관절 **감염(infection)** 치료 맥락에서 Daptomycin을 다루며, 골관절염(퇴행성) 치료를 목적으로 한 연구가 아닙니다. 직접적인 재창출 근거로는 활용할 수 없으며, 참고용으로만 제시합니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|------|------|------|---------|
| [26235888](https://pubmed.ncbi.nlm.nih.gov/26235888/) | 2015 | 후향적 코호트 | Int J Antimicrob Agents | 고용량 Daptomycin(>6 mg/kg)의 복잡 골·관절 및 삽입물 관련 감염 치료 효능·안전성 평가 |
| [23312602](https://pubmed.ncbi.nlm.nih.gov/23312602/) | 2013 | 설문/단면 | Int J Antimicrob Agents | 인공관절 감염 관리 현황 조사 — 항생제 선택 선호도 및 Daptomycin 사용 포함 (556명 응답) |
| [23519823](https://pubmed.ncbi.nlm.nih.gov/23519823/) | 2013 | 후향적 연구 | Int Orthop | 고용량 Daptomycin + Rifampicin 병용요법의 그람양성 골관절 감염 안전성·유효성 평가 |
| [22511636](https://pubmed.ncbi.nlm.nih.gov/22511636/) | 2012 | 증례군 | J Antimicrob Chemother | 슬관절·고관절 인공관절 주위 감염(PJI)에서 Daptomycin 임상 경험 보고 |
| [22854340](https://pubmed.ncbi.nlm.nih.gov/22854340/) | 2012 | 체외 시험 | J Antibiotics | 인공관절 감염 황색포도구균·표피포도구균의 Daptomycin 항균 감수성 평가 |
| [25650692](https://pubmed.ncbi.nlm.nih.gov/25650692/) | 2015 | 후향적 미생물 | Surg Infect | 10년간 골관절 감염 포도구균 항생제 감수성 프로파일 변화 추적 |
| [17999973](https://pubmed.ncbi.nlm.nih.gov/17999973/) | 2008 | 후향적 코호트 | J Antimicrob Chemother | 황색포도구균 균혈증 관련 골관절 감염에서 Daptomycin vs. 표준 치료 임상 결과 비교 |
| [21477701](https://pubmed.ncbi.nlm.nih.gov/21477701/) | 2010 | 레지스트리 | Med Clin | 스페인 EU-CORE 데이터베이스 기반 Daptomycin 실제 사용 현황 분석 |
| [32206362](https://pubmed.ncbi.nlm.nih.gov/32206362/) | 2020 | 증례 보고 | Case Rep Orthop | 전슬관절치환술 예정 골관절염 환자에서 발견된 화농성 관절염 감별 진단 사례 |
| [41853106](https://pubmed.ncbi.nlm.nih.gov/41853106/) | 2026 | 증례 보고 | ASM Case Rep | 자연 관절 화농성 관절염의 희귀 원인균(Corynebacterium propinquum) 사례 보고 |

---

## 한국 시판 정보

Daptomycin은 현재 **한국 미출시** 약물입니다. 식품의약품안전처(MFDS) 허가 이력이 확인되지 않습니다.

---

## 🔍 주목: 2순위 예측 — 류마티스 관절염 (Research Question)

골관절염(1순위)이 위양성으로 판단되는 반면, **류마티스 관절염(RA, 2순위)**은 전임상 수준에서 독립적인 탐색 가치를 가집니다.

| 항목 | 내용 |
|------|------|
| TxGNN 예측 점수 | 99.84% |
| 근거 수준 | L4 |
| 임상시험 | 0건 |
| 관련 문헌 | 2편 (직접 근거) |
| 권장 결정 | Research Question |

**핵심 전임상 문헌:**

| PMID | 연도 | 유형 | 주요 발견 |
|------|------|------|---------|
| [39571268](https://pubmed.ncbi.nlm.nih.gov/39571268/) | 2025 | 동물모델 (CIA 마우스) | Daptomycin이 NF-κB 경로 억제 및 TNF-α/IL-6/IL-1β 감소를 통해 콜라겐 유도 관절염을 개선 — **항생제 외 항RA 효과 최초 보고** |
| [40923559](https://pubmed.ncbi.nlm.nih.gov/40923559/) | 2025 | 전임상/의약화학 | Daptomycin 구조 기반 신규 사이클릭 리포펩타이드 합성 및 최적화 — CLP-d2가 모체보다 우수한 항RA 효과 발휘 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

> **안전 신호 주의**: Daptomycin의 알려진 부작용인 **횡문근융해증(rhabdomyolysis)**이 고요산혈증을 유발하여 급성 통풍 발작으로 이어진 증례가 보고되었습니다 ([PMID 36693494](https://pubmed.ncbi.nlm.nih.gov/36693494/), 2023). 이는 치료 효과가 아닌 **부작용 사례**로, Daptomycin을 통풍 치료에 사용해서는 안 됩니다.

---

## 결론 및 다음 단계

### 1순위 예측 — 골관절염

**결정: Hold**

**사유:**
골관절염 예측은 TxGNN 훈련 데이터에서 '골관절 감염'과 '골관절염'의 의미 혼동으로 발생한 위양성으로 판단됩니다. Daptomycin에는 퇴행성 관절염 치료와 관련된 알려진 기전이 없으며, 10편의 검색 문헌 전부가 감염 치료 연구입니다.

**진행하려면 필요한 것:**
- 해당 없음 — 기전적 재창출 가능성 없음으로 추가 조사 불필요

---

### 2순위 예측 — 류마티스 관절염

**결정: Research Question**

**사유:**
2025년 발표된 동물모델 연구에서 Daptomycin이 NF-κB 억제를 통한 항염 효과로 CIA 관절염을 개선함이 처음 보고되었습니다. 사이클릭 리포펩타이드 구조 기반의 항염 후보 물질로서 기초과학 수준의 탐색 가치가 있으나, 인간 대상 데이터가 전무하여 현 단계에서 임상 진입은 시기상조입니다.

**진행하려면 필요한 것:**
- 작용 기전 상세 데이터 확보 (DrugBank 조회, 추가 문헌 분석)
- 한국 MFDS 허가 가능성 예비 검토
- 인간 세포 기반 in vitro 연구 설계 (RA 활막 세포 모델)
- CIA 동물모델 재현 실험 및 용량-반응 분석
- 류마티스내과 전문가 자문을 통한 임상적 타당성 평가

---

> **면책 고지**: 본 보고서는 연구 참고 목적으로만 제공되며, 의료 조언을 구성하지 않습니다. 약물 재창출 후보는 임상 검증을 거쳐야만 적용 가능합니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

