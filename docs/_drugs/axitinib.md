---
layout: default
title: Axitinib
parent: 모델 예측만 (L5)
nav_order: 110
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Axitinib: 예측 신규 적응증 신경모세포종 관련 신세포암 (renal cell carcinoma associated with neuroblastoma) (근거 수준 L5). 기존 적응증: 허가 적응증 원문이 문서 링크로만 제공되어 본문 확인 불가 (한국 허가 문서 참조). 문헌상 진행성 신세포암"
---

# Axitinib
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

# Axitinib: 신세포암(RCC)에서 신세포암 희귀 아형으로

## 한 문장 요약

Axitinib은 VEGFR 1-3을 선택적으로 억제하는 경구 티로신 키나제 억제제로, 한국에서 인라이타정이라는 이름으로 시판 중입니다. TxGNN 모델은 **TFE3 융합 관련 신세포암(Xp11.2 전좌 신세포암)** 등 신세포암의 희귀 아형을 상위 예측으로 제시했지만, 이 중 임상시험이 있는 것은 소규모 Phase 2 시험 1건뿐입니다. 상위 예측 중 임상시험과 문헌이 풍부한 "신세포암(renal carcinoma)"은 이미 허가된 적응증의 확인에 해당하므로 신규 재창출 근거로 보기 어렵습니다.

> **보고서 해석 시 유의점:** TxGNN 점수 1위 항목(신경모세포종 관련 신세포암)은 근거가 전혀 없습니다. 임상시험과 문헌이 많은 항목은 6위의 "신세포암"인데, 이는 기존 적응증이므로 재창출 사례가 아닙니다. 이 보고서는 1위 예측을 기준 항목으로 표시하되, 실질적 검토 가치가 있는 후보(2위, 9위)를 함께 정리합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 원문이 문서 링크로만 제공되어 본문 확인 불가 (한국 허가 문서 참조). 문헌상 진행성 신세포암 |
| 예측 신규 적응증 (1위) | 신경모세포종 관련 신세포암 (renal cell carcinoma associated with neuroblastoma) |
| TxGNN 예측 점수 | 99.90% |
| 근거 수준 | L5 (1위 항목 기준) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 2건 |
| 권장 결정 | Hold (1위 항목 기준) |

**주요 후보별 요약**

| 순위 | 예측 질환 | TxGNN 점수 | 근거 수준 | 권장 |
|-----|---------|-----------|---------|-----|
| 1 | 신경모세포종 관련 신세포암 | 99.90% | L5 | Hold |
| 2 | Xp11.2 전좌/TFE3 융합 신세포암 | 99.90% | L2 | Research Question |
| 3 | 분류불능 신세포암 | 99.90% | L4 | Research Question |
| 4 | 소아 신세포암 | 99.87% | L4 | Research Question |
| 5 | 지방육종 | 99.87% | L4 | Research Question |
| 9 | 집합관암 | 99.81% | L2 | Research Question |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 DrugBank 항목에 수록되어 있지 않습니다. 다만 수집된 문헌에 따르면 Axitinib은 VEGF 수용체 1, 2, 3을 강력하고 선택적으로 억제하여 혈관신생, 전이, 종양 성장을 억제하는 약물입니다.

신세포암, 특히 투명세포 아형은 VHL 유전자 변이로 HIF-α가 축적되고 VEGF가 과발현되어 혈관이 풍부한 종양을 형성합니다. 따라서 VEGFR 억제는 이 질환군에서 기전상 타당합니다. 예측된 상위 질환 대부분이 신세포암의 희귀 아형이므로, 높은 TxGNN 점수는 지식 그래프에서 일반 신세포암 노드와 가깝다는 점을 반영한 것으로 보입니다.

다만 1위 항목(신경모세포종 관련 신세포암)과 10위 항목(가족성 자연기흉)은 근거가 전혀 없고, 후자는 FLCN 유전자-신장 종양 연관성에 따른 네트워크 근접성일 가능성이 높아 치료적 근거로 보기 어렵습니다.

## 임상시험 근거

1위 예측 질환에 대해서는 현재 관련 임상시험 등록이 없습니다. 아래는 가장 관련성이 높은 후보 질환의 시험입니다.

**2위: Xp11.2 전좌/TFE3 융합 신세포암**

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT03595124](https://clinicaltrials.gov/study/NCT03595124) | Phase 2 | 진행 중 (모집 종료) | 15 | TFE/전좌 신세포암에서 axitinib+nivolumab vs nivolumab 단독 비교. 결과 미발표 |

**9위: 집합관암**

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT06211114](https://clinicaltrials.gov/study/NCT06211114) | Phase 2 | 모집 중 | 30 | 기존 치료받은 진행성 집합관암에서 면역관문억제제+axitinib 평가. 결과 미발표 |

**참고: 6위 "신세포암" (기존 허가 적응증, 재창출 아님)**

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00678392](https://clinicaltrials.gov/study/NCT00678392) | Phase 3 | 완료 | 723 | AXIS: 전이성 신세포암 2차 치료에서 axitinib vs sorafenib |
| [NCT02853331](https://clinicaltrials.gov/study/NCT02853331) | Phase 3 | 완료 | 861 | KEYNOTE-426: pembrolizumab+axitinib vs sunitinib 1차 치료 |
| [NCT04394975](https://clinicaltrials.gov/study/NCT04394975) | Phase 3 | 완료 | 421 | toripalimab+axitinib vs sunitinib 1차 치료 |
| [NCT01693822](https://clinicaltrials.gov/study/NCT01693822) | Phase 2 | 완료 | 65 | A-PREDICT: 신절제 부적합 전이성 신세포암에서 axitinib |
| [NCT00835978](https://clinicaltrials.gov/study/NCT00835978) | Phase 2 | 완료 | 213 | 용량 적정 여부에 따른 axitinib 비교 이중맹검 |
| [NCT03494816](https://clinicaltrials.gov/study/NCT03494816) | Phase 2 | 완료 | 24 | NAXIVA: 정맥 침범 신세포암에서 수술 전 axitinib |
| [NCT05969496](https://clinicaltrials.gov/study/NCT05969496) | Phase 2 | 모집 중 | 17 | IVC 종양혈전 동반 신세포암 수술 전 pembrolizumab+axitinib |
| [NCT05817903](https://clinicaltrials.gov/study/NCT05817903) | Phase 2 | 모집 중 | 118 | nivolumab+ipilimumab 유도 후 axitinib 추가 강화 |

## 문헌 근거

1위 예측 질환에 대해서는 현재 관련 문헌이 없습니다. 아래는 후보 질환별 주요 문헌입니다.

**소아 신세포암 (4위)**

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [31012542](https://pubmed.ncbi.nlm.nih.gov/31012542/) | 2019 | Review | Pediatr Blood Cancer | 진행성 소아 신세포암은 치료 데이터가 부족함 |
| [26279736](https://pubmed.ncbi.nlm.nih.gov/26279736/) | 2015 | Case report | Can Urol Assoc J | 12세 악성 상피양 혈관근지방종에서 sunitinib, everolimus, axitinib 순차 사용. 성인 프로토콜 적용 가능성 시사 |

**지방육종 (5위)**

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [27822137](https://pubmed.ncbi.nlm.nih.gov/27822137/) | 2016 | 전임상 | Sarcoma | 점액양 지방육종 세포주에서 axitinib의 항혈관신생 및 항종양 활성 확인 |

**집합관암 (9위)**

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [35428926](https://pubmed.ncbi.nlm.nih.gov/35428926/) | 2022 | Review | Urologie | 집합관암에서 nivolumab+axitinib 및 방사선 병용이 생존 연장. 단일 증례 기반 |
| [35773144](https://pubmed.ncbi.nlm.nih.gov/35773144/) | 2022 | 후향적 코호트 | Urol Oncol | 전이성 집합관암의 임상병리 특성, 치료 반응, 예후 인자 분석 |
| [30779529](https://pubmed.ncbi.nlm.nih.gov/30779529/) | 2019 | RCT (간접 근거) | N Engl J Med | KEYNOTE-426. 주로 투명세포 신세포암 대상 |
| [30779531](https://pubmed.ncbi.nlm.nih.gov/30779531/) | 2019 | RCT (간접 근거) | N Engl J Med | JAVELIN Renal 101. 주로 투명세포 신세포암 대상 |

**참고: 기존 허가 적응증(신세포암) 관련 RCT**

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [30779529](https://pubmed.ncbi.nlm.nih.gov/30779529/) | 2019 | RCT | N Engl J Med | Pembrolizumab+axitinib이 sunitinib 대비 우월 |
| [30779531](https://pubmed.ncbi.nlm.nih.gov/30779531/) | 2019 | RCT | N Engl J Med | Avelumab+axitinib vs sunitinib 1차 치료 |
| [40750932](https://pubmed.ncbi.nlm.nih.gov/40750932/) | 2025 | RCT (5년 추적) | Nat Med | KEYNOTE-426 5년 생존 및 바이오마커 분석 |
| [37872020](https://pubmed.ncbi.nlm.nih.gov/37872020/) | 2024 | RCT | Ann Oncol | RENOTORCH: toripalimab+axitinib vs sunitinib |
| [39706335](https://pubmed.ncbi.nlm.nih.gov/39706335/) | 2025 | RCT (최종 분석) | Ann Oncol | JAVELIN Renal 101 최종 분석 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201206553 | 인라이타정5밀리그램(엑시티닙) | 빨간색 삼각형모양의 필름코팅정제 | 허가 문서 링크 참조 (본문 미확인) |
| 201206552 | 인라이타정1밀리그램(엑시티닙) | 빨간색 타원형모양의 필름코팅정제 | 허가 문서 링크 참조 (본문 미확인) |

두 제품 모두 한국화이자제약(주)이 제조하며 단일제로 유효 상태입니다.

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적치료제 (VEGFR 티로신 키나제 억제제) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 취급 방호 | 허가사항의 경고 및 주의사항을 참조하세요 |

## 안전성 고려사항

**약물 상호작용** (수집된 데이터 100건 중 일부 표시):

- **Major**: Clarithromycin, Dexamethasone
- **Moderate**: Aprepitant, Clotrimazole, Miconazole, Naltrexone
- **Minor**: 제산제 및 위산분비억제제 계열 (Famotidine, Ranitidine, Cimetidine, Nizatidine, Rabeprazole, Esomeprazole, Lansoprazole, Dexlansoprazole, 수산화알루미늄, 탄산칼슘, 마그네슘 제제 등)

경고 및 금기 정보는 허가사항을 참조하세요. 허가증 본문을 확인하지 못해 이 항목은 아직 검증되지 않았습니다.

## 결론 및 다음 단계

**결정: Hold** (1위 예측 기준). 후보 중 Xp11.2/TFE3 신세포암과 집합관암은 **Research Question** 단계로 추가 검토할 가치가 있습니다.

**사유:**
- 1위 예측(신경모세포종 관련 신세포암)은 임상시험과 문헌이 모두 없으며, 높은 점수는 일반 신세포암 노드와의 근접성을 반영한 것으로 보입니다.
- 근거가 가장 많은 "신세포암"은 이미 허가된 적응증이어서 재창출 사례가 아니라 양성 대조 기준에 해당합니다. TFE3 신세포암(n=15)과 집합관암(n=30) 시험은 소규모이고 결과가 아직 발표되지 않았습니다.

**진행하려면 필요한 것:**
- 한국 허가증(MFDS) 첨부문서를 내려받아 허가 적응증, 경고, 금기 정보 확보 (현재 안전성 선별을 진행할 수 없는 차단 수준의 공백)
- DrugBank에서 작용 기전(MOA) 데이터 확보
- NCT03595124(TFE3 신세포암)와 NCT06211114(집합관암) 결과 발표 모니터링
- 희귀 아형에 대한 근거 확보를 위한 후향 코호트 또는 증례 문헌 추가 검색
- 소아 신세포암은 소아 용량과 안전성이 확립되지 않았으므로 별도의 안전성 평가 필요
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

