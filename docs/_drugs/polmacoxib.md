---
layout: default
title: Polmacoxib
parent: 모델 예측만 (L5)
nav_order: 610
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Polmacoxib: 예측 신규 적응증 골관절염 감수성 (osteoarthritis susceptibility) (근거 수준 L5). 기존 적응증: 골관절염 (허가증에 적응증 원문 대신 허가 문서 링크만 수록되어 있어, 문헌과 시판 현황을 근거로 기재)"
monitor_inn: "Polmacoxib"
predicted_indications: ["osteoarthritis susceptibility", "osteoarthritis", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "pseudoachondroplasia", "myosclerosis", "brachyolmia", "arthropathy", "spondyloarthropathy, susceptibility to", "ankylosing spondylitis"]
---

# Polmacoxib
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
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

# Polmacoxib: 골관절염에서 골관절염 감수성(예측 신규 적응증)으로

## 한 문장 요약

Polmacoxib은 COX-2와 탄산탈수효소(CA)를 동시에 억제하는 NSAID로, 한국에서 골관절염 치료제로 허가되어 시판 중입니다.
TxGNN 모델의 최상위 예측은 **골관절염 감수성(osteoarthritis susceptibility)**이지만, 이는 이미 허가된 골관절염 적응증과 사실상 같은 개념으로 보이며 이 예측을 직접 뒷받침하는 임상시험과 문헌은 **0건**입니다. 참고로 2순위 예측인 골관절염에는 **7편의 문헌**(Phase 3 RCT 포함)이 있으나, 이는 기존 적응증의 재확인입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 골관절염 (허가증에 적응증 원문 대신 허가 문서 링크만 수록되어 있어, 문헌과 시판 현황을 근거로 기재) |
| 예측 신규 적응증 | 골관절염 감수성 (osteoarthritis susceptibility) |
| TxGNN 예측 점수 | 99.999% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 10건 (모두 단일제, 유효) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 이번 자료에 포함되어 있지 않습니다. 다만 수집된 문헌(PMID 26095375, 41100334)에 따르면 Polmacoxib은 COX-2와 탄산탈수효소 I/II를 동시에 억제하는 약물입니다. COX-2 억제는 프로스타글란딘 매개 염증과 통증을 줄이며, CA와의 결합은 약물을 적혈구 등 CA 발현 조직에 농축시켜 전신 노출과 심혈관 위험을 낮출 수 있다고 알려져 있습니다.

그러나 "골관절염 감수성"은 골관절염에 대한 유전적 취약성을 뜻하는 용어로, 독립적으로 치료할 수 있는 임상 질환이 아닙니다. 지식 그래프에서 골관절염을 대신하는 항목일 가능성이 높아, 이미 허가된 적응증을 재확인한 것에 가깝습니다. 따라서 진정한 의미의 재창출 발견으로 보기 어렵습니다.

참고로 상위 10개 예측 중 나머지는 다음과 같이 정리됩니다.
- **희귀 유전성 골격 질환** (acromesomelic dysplasia Hunter-Thompson형, brachyolmia, brachyolmia-amelogenesis imperfecta 증후군, pseudoachondroplasia): COX-2/CA 억제와의 뚜렷한 기전적 연결이 없고 근거도 없습니다. Pseudoachondroplasia는 조기 관절 퇴행과 통증이 동반되어 증상 완화 목적의 이론적 가능성만 있습니다.
- **Myosclerosis**: 기전적 연결과 근거가 모두 없습니다.
- **관절병증(arthropathy)**: 골관절염을 포함하는 넓은 범주로, 연결된 문헌이 모두 골관절염 관련이어서 간접 근거에 그칩니다.
- **척추관절병증 감수성, 강직성 척추염**: NSAID 계열의 사용 근거는 있으나 Polmacoxib 고유의 근거는 없습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

예측 1순위(골관절염 감수성)에 연결된 문헌은 없습니다. 아래는 2순위 예측인 골관절염에 연결된 문헌으로, 기존 적응증의 근거입니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [29201297](https://pubmed.ncbi.nlm.nih.gov/29201297/) | 2017 | RCT (Phase III) | Clin Orthop Surg | 골관절염 환자에서 Polmacoxib 2 mg을 위약(우월성) 및 celecoxib 200 mg(비열등성)과 비교해 진통 효과와 안전성 평가 |
| [39545640](https://pubmed.ncbi.nlm.nih.gov/39545640/) | 2024 | RCT | Pain Manag | 인도 환자의 경증~중등도 고관절/무릎 골관절염에서 Polmacoxib 2 mg과 celecoxib 200 mg의 효능·안전성 비교 |
| [41257112](https://pubmed.ncbi.nlm.nih.gov/41257112/) | 2025 | 전향적 단일군 연구 | Cureus | 인도 환자의 고관절/무릎 골관절염에서 효과, 작용 발현, 내약성 평가 |
| [34974943](https://pubmed.ncbi.nlm.nih.gov/34974943/) | 2022 | 집단 약동학/약력학 분석 | Clin Ther | 건강인과 골관절염 환자에서 Polmacoxib의 약동학·약력학 특성 탐색 |
| [41100334](https://pubmed.ncbi.nlm.nih.gov/41100334/) | 2025 | Review | J Assoc Physicians India | 골관절염과 급성 통증에서 COX-2/CA 이중 억제제의 안전성과 효능 고찰 |
| [38765421](https://pubmed.ncbi.nlm.nih.gov/38765421/) | 2024 | Review | Cureus | 골관절염 치료에서 신형 NSAID로서의 Polmacoxib 고찰 |
| [26095375](https://pubmed.ncbi.nlm.nih.gov/26095375/) | 2015 | 기전/전산 연구 | Protein Pept Lett | 밀도범함수이론 등을 이용한 celecoxib 및 CG100649의 COX-2/CA-II 이중 억제 기전 분석 |

## 한국 시판 정보

허가증에는 적응증 원문 대신 식약처 허가 문서 링크만 수록되어 있어, 적응증 칸에는 별도 요약을 기재하지 않았습니다.

| 허가번호 | 제품명 | 제형 | 제조/판매사 |
|---------|------|------|-----------|
| 201907587 | 아셀렉스정2밀리그램 | 필름코팅정 | 씨지인바이츠(주) |
| 201500622 | 아셀렉스캡슐2밀리그램 | 경질캡슐 | 씨지인바이츠(주) |
| 202202394 | 아셀콕스캡슐2밀리그램 | 경질캡슐 | (주)대웅제약 |
| 202202343 | 폴시브캡슐2밀리그램 | 경질캡슐 | (주)이든파마 |
| 202202344 | 폴콕스캡슐2밀리그램 | 경질캡슐 | (주)넥스팜코리아 |

이 외에 동일 성분의 경질캡슐 5건(건폴렉스, 페콕시브, 폴마콕스, 폴비트, 폴마렉스)이 더 허가되어 있습니다.

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
1순위 예측인 "골관절염 감수성"은 치료 가능한 독립 질환이 아니라 이미 허가된 골관절염의 대리 항목으로 보이며, 이 예측을 직접 뒷받침하는 임상시험과 문헌이 없어 근거 수준은 L5입니다. 참고로 기존 적응증인 골관절염에서는 Phase 3 RCT를 포함한 근거가 있어(L1, 단 신규 적응증이 아님) 해당 적응증의 유지는 타당하지만 재창출 후보로서의 가치는 없습니다.

**진행하려면 필요한 것:**
- 재창출 대상을 "감수성" 용어가 아닌 구체적이고 치료 가능한 질환으로 재정의 (예: 관절병증의 특정 하위 유형, 강직성 척추염)
- 강직성 척추염 등 후보에 대한 Polmacoxib 고유 근거 확보 (파일럿 또는 용량 탐색 연구)
- 허가사항(경고·금기 등) 확인 및 안전성 검토
- 작용 기전(MOA) 데이터 보완 (DrugBank 등 공식 출처)
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

