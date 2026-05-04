---
layout: default
title: Acyclovir
parent: 僅模型預測 (L5)
nav_order: 22
evidence_level: L5
indication_count: 10
---

# Acyclovir
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

# Acyclovir: 헤르페스 바이러스 감염에서 점상 상피 각막결막염 외 9개 신규 적응증으로

---

## 한 문장 요약

Acyclovir는 헤르페스 심플렉스 바이러스(HSV) 및 수두-대상포진 바이러스(VZV) 감염 치료에 확립된 항바이러스제로, 구순 헤르페스, 생식기 헤르페스, 대상포진 등의 치료에 전 세계적으로 사용됩니다.
TxGNN 모델은 **점상 상피 각막결막염(Punctate Epithelial Keratoconjunctivitis)**을 포함한 **10개 신규 적응증**에 효과가 있을 수 있다고 예측하며, 이 중 **보통 사마귀(Common Wart)**에서 **6건의 임상시험과 20편의 문헌**, **감염 후 신경통(Post-infectious Neuralgia)**에서 **12건의 임상시험**이 근거를 지지합니다.

---

## 전체 예측 개요

| 순위 | 예측 적응증 | TxGNN 점수 | 근거 수준 | 임상시험 | 문헌 | 권장 결정 |
|------|-----------|:----------:|:--------:|:-------:|:----:|:--------:|
| 1 | 점상 상피 각막결막염 | 99.67% | L4 | 0건 | 2편 | Research Question |
| 2 | 보통 사마귀 | 99.46% | L2 | 6건 | 20편 | Research Question |
| 3 | 감염 후 신경통 | 99.25% | L2 | 12건 | 0편 | **Proceed with Guardrails** |
| 4 | C형 간염 유발 간경변 | 99.23% | L5 | 0건 | 2편 | Hold |
| 5 | 호산구성 농포성 모낭염 | 99.22% | L5 | 0건 | 1편 | Hold |
| 6 | COVID-19 후유증 | 99.16% | L4 | 0건 | 20편 | Hold |
| 7 | 외음부 질 칸디다증 | 99.11% | L5 | 0건 | 4편 | Hold |
| 8 | 구진성 두드러기 | 99.09% | L5 | 0건 | 0편 | Hold |
| 9 | 안와 영역 질환 | 99.08% | L3 | 선별 필요 | 3편 | Research Question |
| 10 | 유행성 각막결막염 | 99.07% | L5 | 0건 | 0편 | Hold |

---

## 약물 기전 개요

Acyclovir는 구아노신 유사체 계열의 항바이러스제로, 바이러스성 티미딘 인산화효소(Thymidine Kinase, TK)에 의해 활성화됩니다. 인산화된 Acyclovir는 바이러스 DNA 중합효소를 선택적으로 억제하여 바이러스 복제를 차단합니다.

이 기전의 핵심적 함의는 다음과 같습니다. **TK를 보유하는 바이러스(HSV-1, HSV-2, VZV, EBV)**에는 효과적이지만, TK를 보유하지 않는 바이러스(HPV, HCV, CMV, 아데노바이러스)에는 표준 경로로는 활성을 갖지 않습니다. 이 사실은 아래 각 적응증의 기전 타당성 평가의 핵심 기준이 됩니다.

> 현재 이 Evidence Pack에는 상세 MOA 데이터가 수집되지 않았습니다. 위 기전 설명은 공개된 약리학적 근거에 기반합니다.

---

## 적응증 1: 점상 상피 각막결막염 (Punctate Epithelial Keratoconjunctivitis)

### 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 헤르페스 바이러스(HSV/VZV) 감염 |
| 예측 신규 적응증 | 점상 상피 각막결막염 (Punctate Epithelial Keratoconjunctivitis) |
| TxGNN 예측 점수 | 99.67% (전체 6,209위) |
| 근거 수준 | L4 |
| 한국 시판 현황 | 미허가 (허가증 0건) |
| 권장 결정 | Research Question |

### 이 예측이 타당한 이유는?

점상 상피 각막결막염(PEK)은 건성안, 콘택트렌즈, 세균 및 바이러스 감염 등 다양한 원인으로 발생합니다. 그 중 **HSV 각막염의 임상 표현형**으로 PEK가 나타날 수 있으며, Acyclovir는 HSV에 대한 확립된 항바이러스 활성을 보유하고 있어 간접적인 기전 연결고리를 형성합니다.

그러나 현재 제공된 근거에는 중요한 한계가 있습니다. 두 편의 문헌 모두 PEK에 대한 Acyclovir의 직접적 효능을 지지하지 않습니다. 1995년 문헌(PMID 7825685)은 AIDS 환자에서 나타난 **약물 유발 각막 지방 침착** 증례이며, 2011년 문헌(PMID 21934222)은 **미포자충(Microsporidium) 감염** 관련 연구로, 미포자충은 비바이러스성 병원체이므로 Acyclovir가 효과를 발휘할 수 없는 대상입니다.

기전적 연결고리는 간접 추론 수준에 머물러 있으며, 직접적인 임상시험이 전무한 상태입니다.

### 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|:---:|------|------|---------|
| [7825685](https://pubmed.ncbi.nlm.nih.gov/7825685/) | 1995 | Case Series | Am J Ophthalmol | AIDS 환자에서 약물 유발 각막 지방 침착 2증례; PEK에 대한 Acyclovir 직접 근거 없음 |
| [21934222](https://pubmed.ncbi.nlm.nih.gov/21934222/) | 2011 | Case Series | Indian J Pathol Microbiol | 미포자충 각막결막염 사례군; 비바이러스성 병원체로 Acyclovir 무효 |

---

## 적응증 2: 보통 사마귀 (Common Wart)

### 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 헤르페스 바이러스(HSV/VZV) 감염 |
| 예측 신규 적응증 | 보통 사마귀 (Common Wart) |
| TxGNN 예측 점수 | 99.46% (전체 8,958위) |
| 근거 수준 | L2 |
| 한국 시판 현황 | 미허가 (허가증 0건) |
| 권장 결정 | Research Question |

### 이 예측이 타당한 이유는?

보통 사마귀는 인유두종바이러스(HPV) 감염으로 발생합니다. HPV는 바이러스성 TK를 보유하지 않으므로, Acyclovir의 표준 항바이러스 기전(TK 의존성 DNA 중합효소 억제)으로는 HPV에 직접적 효과가 없습니다.

그러나 **병변 내 주사(Intralesional injection)** 방식에서 임상적 효능이 반복적으로 보고되고 있습니다. 제안된 작용 기전은 국소 세포면역 반응 활성화를 통한 HPV 감염 세포의 면역 매개 제거입니다—직접적인 항바이러스 효과가 아닌 **면역조절(Immunomodulation)** 기전입니다. 이 가설은 아직 완전히 규명되지 않았습니다.

근거의 강도는 주목할 만합니다. 2025년 *Archives of Dermatological Research*에 두 편의 비교 RCT(PMID 40488756, PMID 40056255)가 발표되었고, Phase 2/3 RCT(NCT06261684, n=92)를 포함한 여러 Phase 4 시험이 진행 중이거나 완료되었습니다. 기전상 불확실성이 남아 있어 "Go"가 아닌 "Research Question"으로 권장됩니다.

### 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|:----:|:----:|:-------:|---------|
| [NCT06261684](https://clinicaltrials.gov/study/NCT06261684) | Phase 2/3 | 불명 | 92 | 병변 내 Acyclovir vs 냉동요법 무작위 대조 시험; 족저 사마귀 안전성·유효성 비교 |
| [NCT05429151](https://clinicaltrials.gov/study/NCT05429151) | Phase 4 | 불명 | 40 | 병변 내 Acyclovir vs Candida 항원; 임상 및 피부경 평가 |
| [NCT07196670](https://clinicaltrials.gov/study/NCT07196670) | Phase 4 | 모집 예정 | 60 | Vitamin D vs Acyclovir 족저 사마귀 단일맹검 RCT; 재발률 포함 평가 |
| [NCT07448844](https://clinicaltrials.gov/study/NCT07448844) | Phase 4 | 모집 중 | 40 | 피부 사마귀(보통·족저·편평·조갑주위)에 Vitamin D3 vs Acyclovir 병변 내 주사 비교 |
| [NCT05324904](https://clinicaltrials.gov/study/NCT05324904) | NA | 불명 | 44 | 족저 사마귀에서 병변 내 Acyclovir vs Vitamin D3 효능·안전성 비교 |
| [NCT03465280](https://clinicaltrials.gov/study/NCT03465280) | N/A | 불명 | 400 | 재발성 호흡기 유두종(RRP) 등록 연구; 기도 내 HPV 관련 적응증으로 피부 사마귀와 직접 연관성 낮음 |

### 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|:---:|------|------|---------|
| [40488756](https://pubmed.ncbi.nlm.nih.gov/40488756/) | 2025 | Comparative RCT | Arch Dermatol Res | 병변 내 Acyclovir vs 5-FU 재발성 사마귀 치료 비교; 대부분 환자에서 완전 반응 달성 |
| [40056255](https://pubmed.ncbi.nlm.nih.gov/40056255/) | 2025 | Comparative RCT | Arch Dermatol Res | 병변 내 Acyclovir vs HPV 4가 백신, 완고성 피부 사마귀 60명 RCT; 유효성·안전성 평가 |
| [40889709](https://pubmed.ncbi.nlm.nih.gov/40889709/) | 2026 | RCT | J Am Acad Dermatol | 족저 사마귀 병변 내 Acyclovir vs 냉동요법 무작위 대조 시험 |
| [38822848](https://pubmed.ncbi.nlm.nih.gov/38822848/) | 2024 | RCT | Arch Dermatol Res | 병변 내 Acyclovir vs B형 간염 백신, 내성 족저 사마귀 48명 3군 RCT |
| [38793636](https://pubmed.ncbi.nlm.nih.gov/38793636/) | 2024 | Case Series | Viruses | HPV 관련 질환에서 Acyclovir/Valacyclovir 치료 후 완화 증례; 음경 콘딜로마 5례 포함 |
| [40740392](https://pubmed.ncbi.nlm.nih.gov/40740392/) | 2025 | Clinical Study | Indian J Dermatol | 족저 사마귀 병변 내 Acyclovir vs Candida 항원 임상·피부경 평가 |
| [37303436](https://pubmed.ncbi.nlm.nih.gov/37303436/) | 2023 | Clinical Study | Cureus | 병변 내 Acyclovir vs PPD 면역요법 비교; 다양한 바이러스 사마귀 유형 대상 |
| [34412535](https://pubmed.ncbi.nlm.nih.gov/34412535/) | 2022 | Clinical Study | J Cutan Med Surg | 병변 내 Acyclovir 피부 사마귀 치료 가능성 평가; DNA 바이러스에 대한 항바이러스 기전 가설 검토 |
| [26885794](https://pubmed.ncbi.nlm.nih.gov/26885794/) | 2016 | Case Report | J Drugs Dermatol | 대상포진 치료 목적 경구 Acyclovir 10일 투여 후 지속성 족저 사마귀 소실 증례 |
| [6467981](https://pubmed.ncbi.nlm.nih.gov/6467981/) | 1984 | Case Report | Cutis | Acyclovir 연고를 이용한 보통 사마귀(Verrucae vulgares) 치료 초기 임상 보고 |

---

## 적응증 3: 감염 후 신경통 (Post-infectious Neuralgia / PHN)

### 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 헤르페스 바이러스(HSV/VZV) 감염 |
| 예측 신규 적응증 | 감염 후 신경통 (Post-infectious Neuralgia) |
| TxGNN 예측 점수 | 99.25% (전체 11,568위) |
| 근거 수준 | L2 |
| 한국 시판 현황 | 미허가 (허가증 0건) |
| 권장 결정 | **Proceed with Guardrails** |

### 이 예측이 타당한 이유는?

대상포진 후 신경통(PHN)은 VZV 재활성화에 의해 신경절 및 신경섬유가 손상되어 발생합니다. Acyclovir 및 전구약물 Valacyclovir는 **급성기에 VZV 복제를 억제**함으로써 신경 손상의 정도와 염증 지속 기간을 줄여 PHN 발생률 및 중증도를 감소시키는 기전이 과학적으로 확립되어 있습니다.

이 적응증에서 가장 중요한 임상적 구분이 필요합니다. **현재 근거의 대부분은 급성 대상포진 치료를 통한 PHN '예방'에 집중**되어 있습니다. 이미 확립된 PHN의 '직접 치료'에 대한 Acyclovir의 효과는 상대적으로 근거가 약합니다. 임상 적용 계획 시 이 두 시나리오(예방 vs 치료)를 반드시 구분해야 합니다.

근거 수준은 강력합니다. n=1,257(NCT01229267) 및 n=5,305(NCT01254630)의 대형 Phase 3 완료 이중맹검 RCT가 존재하며, Acyclovir의 전구약물인 Valacyclovir가 직접 비교군으로 사용된 Phase 3 시험(NCT02412917)도 간접적 근거를 제공합니다.

### 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|:----:|:----:|:-------:|---------|
| [NCT01229267](https://clinicaltrials.gov/study/NCT01229267) | Phase 3 | 완료 | 1,257 | 자가조혈모세포이식 수용자 대상 비활성화 VZV 백신(V212) PHN 예방 이중맹검 RCT; 최고 수준 직접 근거 |
| [NCT01254630](https://clinicaltrials.gov/study/NCT01254630) | Phase 3 | 완료 | 5,305 | 고형종양 화학요법 환자 대상 V212 VZV 백신 PHN 예방 대규모 RCT |
| [NCT02412917](https://clinicaltrials.gov/study/NCT02412917) | Phase 3 | 종료 | 237 | FV-100 vs Valacyclovir(Acyclovir 전구약물) 급성 대상포진 PHN 예방 직접 비교; 간접 Acyclovir 효과 데이터 제공 |
| [NCT03134196](https://clinicaltrials.gov/study/NCT03134196) | Phase 4 | 완료 | 527 | Valacyclovir 장기 억제 치료 대상포진 안부 병변(HZO) 다기관 이중맹검 위약 대조 RCT |
| [NCT02151240](https://clinicaltrials.gov/study/NCT02151240) | Phase 4 | 완료 | 94 | Foscarnet vs Sodium Thiosulfate 대상포진 비교; PHN 발생률 관찰 포함 |
| [NCT01250561](https://clinicaltrials.gov/study/NCT01250561) | NA | 완료 | 133 | 급성 대상포진에서 표준 항바이러스제(Valacyclovir) + Gabapentin 병용요법의 PHN 예방 효과 |

---

## 적응증 9: 안와 영역 질환 (Disease of Orbital Region)

### 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 헤르페스 바이러스(HSV/VZV) 감염 |
| 예측 신규 적응증 | 안와 영역 질환 (Disease of Orbital Region) |
| TxGNN 예측 점수 | 99.08% (전체 13,524위) |
| 근거 수준 | L3 |
| 권장 결정 | Research Question |

### 이 예측이 타당한 이유는?

안와 영역 질환은 다양한 하위 질환을 포괄합니다. 그 중 **대상포진 안부 병변(Herpes Zoster Ophthalmicus, HZO, VZV 유발)**과 **HSV 바이러스성 포도막염**은 Acyclovir의 명확한 기전적 근거를 형성합니다. Acyclovir는 VZV/HSV 복제를 억제하여 급성 안와 염증, 각막 손상, 포도막염 및 안와 첨단 증후군 등의 후유증을 줄일 수 있습니다.

중요한 해석 주의사항: 검색된 임상시험 다수는 Acyclovir가 아닌 **Ganciclovir의 CMV 망막염 연구**입니다. Acyclovir를 직접 평가하는 시험은 HEDS I/II(NCT00000138, NCT00000139)와 바이러스성 포도막염 탐색 연구(NCT03389191)에 한정됩니다.

### 임상시험 근거 (Acyclovir 직접 관련 시험 선별)

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|:----:|:----:|:-------:|---------|
| [NCT00000139](https://clinicaltrials.gov/study/NCT00000139) | Phase 3 | 완료 | - | HEDS II: 경구 Acyclovir HSV 각막 궤양 조기 치료로 각막 간질염 및 이리도사이클리티스 진행 예방 평가 |
| [NCT00000138](https://clinicaltrials.gov/study/NCT00000138) | Phase 3 | 불명 | - | HEDS I: 경구 Acyclovir HSV 간질 각막염 및 이리도사이클리티스 치료 유효성·안전성 평가 |
| [NCT03134196](https://clinicaltrials.gov/study/NCT03134196) | Phase 4 | 완료 | 527 | Valacyclovir 장기 억제 치료 HZO 안부 병변(수지상 각막염, 간질 각막염, 내피 각막염, 홍채염) 다기관 이중맹검 RCT |
| [NCT03389191](https://clinicaltrials.gov/study/NCT03389191) | NA | 불명 | 30 | 경구 Acyclovir 난치성 바이러스성 포도막염 치료 직접 평가; 탐색적 소규모 연구 |

### 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|:---:|------|------|---------|
| [3493673](https://pubmed.ncbi.nlm.nih.gov/3493673/) | 1987 | Review | Am Fam Physician | 대상포진 안부 병변의 포도막염·각막염 합병증 검토; 경구 Acyclovir 예방적 효과 예비 결과 유망 |
| [35957932](https://pubmed.ncbi.nlm.nih.gov/35957932/) | 2021 | Case Report | Ghana Med J | HIV 환자에서 HZO 후 안와 첨단 증후군 발생 증례; Acyclovir 항VZV 치료 기전 설명 포함 |

---

## 보류 적응증 요약

이하 6개 적응증은 기전적 불일치 또는 근거 부재로 **Hold** 권장됩니다. 현재 시점에서 추가 자원 투입을 권장하지 않습니다.

| 적응증 | 근거 수준 | 보류 이유 |
|--------|:--------:|---------|
| **C형 간염 유발 간경변** | L5 | HCV는 RNA 바이러스(NS5B 복제 의존). Acyclovir의 TK/DNA 중합효소 표적이 RNA 바이러스에 무효. TxGNN 위양성(HCV 환자의 합병 HSV 감염 치료 공존 편향) |
| **호산구성 농포성 모낭염** | L5 | 면역 매개 염증성 피부질환으로 바이러스 병인 없음. 유일한 문헌은 2025년 선천성 EPF 증례 초록으로 Acyclovir 치료 미언급. 위양성(HIV-EPF와 HIV-HSV 치료의 그래프 위상 인접 편향) |
| **COVID-19 후유증** | L4 | EBV·HHV-6(Long COVID 주요 의심 바이러스)에 대한 Acyclovir 효과 제한적. 임상시험 등록 전무. 계산생물학 가설 1편(35446232) 외 직접 근거 없음. 관찰 유지 권고 |
| **외음부 질 칸디다증** | L5 | 진균 감염(주로 *Candida albicans*). Acyclovir는 항진균 활성 없음. 문헌은 '임신 중 성감염병 통합 관리' 맥락에서 VVC와 HSV를 동시 언급할 뿐, 직접 치료 근거 없음. 명확한 위양성 |
| **구진성 두드러기** | L5 | 곤충 자상에 의한 과민반응(면역 매개). 바이러스 병인 없음. 임상시험·문헌·기전 모두 부재. 명확한 위양성 |
| **유행성 각막결막염** | L5 | 아데노바이러스(혈청형 8, 19, 37형) 유발. 아데노바이러스는 TK 미보유로 Acyclovir 활성화 불가. 임상시험·문헌 부재. 명확한 위양성(각막결막염 질환 노드의 위상 인접성 편향) |

---

## 한국 시판 정보

Acyclovir는 현재 한국에서 허가된 제품이 없습니다.

| 항목 | 현황 |
|------|------|
| 시판 현황 | 미허가 |
| 허가증 수 | 0건 |
| 비고 | 재창출 연구 진행 시 신규 품목 허가 신청 또는 임상시험 계획 승인(IND) 절차 필요 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

공개 정보 기반 주요 고려사항:
- **신독성**: 고용량 정맥 투여 시 신기능 모니터링 필요; 신기능 저하 환자에서 용량 조절 필수
- **신경독성**: 고용량 정맥 투여 시 섬망, 경련 등 가능
- **병변 내 주사 적용 시**: 국소 통증, 부종, 홍반 등 주사 부위 반응 예상

---

## 결론 및 다음 단계

### 적응증 3: 감염 후 신경통

**결정: Proceed with Guardrails**

**사유:**
급성 대상포진에서 Acyclovir/Valacyclovir를 통한 PHN 예방에 대해 Phase 3 완료 대규모 RCT(n=1,257; n=5,305)가 존재하며, VZV에 대한 명확한 항바이러스 기전이 PHN 예방 메커니즘을 직접 지지합니다. L2 수준 근거로 임상 적용 타당성이 충분합니다.

**진행하려면 필요한 것:**
- 임상 적용 시나리오 명확화: 급성기 PHN 예방 vs 확립된 PHN 직접 치료 구분
- 한국 내 품목 허가 신청 또는 IND 신청
- PHN 직접 치료 효과에 대한 추가 연구 설계 고려

---

### 적응증 2: 보통 사마귀

**결정: Research Question**

**사유:**
기전 불확실성(HPV에 대한 표준 항바이러스 기전 무효)에도 불구하고, 병변 내 주사 방식의 임상 효능을 지지하는 Phase 2/3 및 Phase 4 RCT와 2025년 발표 비교 RCT가 L2 수준 근거를 형성합니다.

**진행하려면 필요한 것:**
- 면역조절 기전 규명을 위한 전임상·기전 연구
- 최적 투여 용량, 주사 간격 및 치료 기간에 대한 표준화 연구
- 한국 피부과 학회와의 연구 협력 체계 구축

---

### 적응증 1: 점상 상피 각막결막염

**결정: Research Question**

**사유:**
HSV 각막염의 표현형으로서 간접적 기전 연결고리만 존재하며, 직접적 임상시험 및 의미 있는 관련 문헌이 전무합니다. 추가 탐색이 필요하나 우선순위는 낮습니다.

**진행하려면 필요한 것:**
- HSV 유발 PEK에 특화된 소규모 탐색적 임상시험 설계
- PEK 병인 분류 연구(HSV 비율 파악)

---

### 적응증 9: 안와 영역 질환

**결정: Research Question**

**사유:**
HZO 및 HSV 포도막염에 대한 기존 근거(HEDS I/II)가 확립되어 있으나, 현재 검색된 임상시험 데이터가 Ganciclovir/CMV 연구와 혼재되어 있어 Acyclovir 특이적 효능 평가에 한계가 있습니다.

**진행하려면 필요한 것:**
- 안와 영역 질환의 하위 분류별 Acyclovir 적응증 세분화(HZO, HSV 포도막염 등)
- 기존 HEDS 데이터에 대한 체계적 문헌 검토

---

> **면책 조항**: 본 보고서는 연구 참고 목적으로만 작성되었으며 의료 조언을 구성하지 않습니다. 모든 약물 재창출 후보는 임상 검증을 거쳐야 합니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

