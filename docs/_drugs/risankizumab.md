---
layout: default
title: Risankizumab
parent: 僅模型預測 (L5)
nav_order: 604
evidence_level: L5
indication_count: 10
---

# Risankizumab
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

# Risankizumab: 건선(Psoriasis)에서 피부염(Dermatitis)으로

## 한 문장 요약

Risankizumab(Skyrizi)은 IL-23을 표적으로 하는 단클론항체로, 전세계적으로 건선·건선성 관절염·크론병 치료에 승인되어 있으나 한국 내 허가 자료는 확인되지 않았습니다.
TxGNN 모델은 **피부염(Dermatitis, 아토피피부염 포함)**에도 효과가 있을 수 있다고 예측하며(예측 점수 99.98%), 완료된 Phase 2 RCT 1건과 다수의 관련 문헌이 이를 뒷받침합니다.
다만 동일 계열 약물에서 "역설적 습진(paradoxical eczema)"이 부작용으로 보고된 문헌도 다수 존재해, 해석에 주의가 필요합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 건선(해외 승인 기준, 한국 허가 자료 없음) |
| 예측 신규 적응증 | 피부염 (Dermatitis, 주로 아토피피부염) |
| TxGNN 예측 점수 | 99.98% |
| 근거 수준 | L2 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

공식 MOA 데이터베이스 조회 결과는 아직 확보되지 않았으나(Data Gap), 수집된 문헌(PMID 38266061 등)에 따르면 Risankizumab은 IL-23의 p19 subunit에 결합하는 인간화 IgG1 단클론항체로, IL-23/Th17 경로를 억제하여 건선 등 염증성 질환의 병태생리를 조절합니다.

아토피피부염(AD)은 전통적으로 Th2 우세 질환으로 알려져 있지만, 최근 연구에서는 Th22와 일부 Th17 경로의 관여도 제시되고 있습니다(PMID 36588137). 이 때문에 IL-23/IL-22 차단이 AD에도 치료 효과를 가질 수 있다는 기전적 가설이 성립하며, 실제로 완료된 Phase 2 RCT(NCT03706040)가 이를 직접 검증했습니다.

**주의할 점**: 동일 계열(IL-23/IL-17 억제제) 약물에서 건선 치료 중 오히려 습진성 발진(paradoxical/eczematous eruption)이 유발된다는 사례 보고 및 리뷰가 다수 확인됩니다(PMID 33185530, 36939506, 41645692 등). 즉 "피부염과의 연관성"이 치료 효과인지, 역설적 부작용인지 문헌상 방향이 혼재되어 있어 추가 검증이 필요합니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT03706040](https://clinicaltrials.gov/study/NCT03706040) | Phase 2 | 완료 | 172 | 중등증~중증 성인/청소년 아토피피부염에서 안전성·유효성 평가 (핵심 근거) |
| [NCT07021495](https://clinicaltrials.gov/study/NCT07021495) | N/A (관찰) | 모집 중 | 840 | 아토피피부염·건선·화농성한선염 등 만성 면역매개 피부질환 바이오마커 프로파일링 |
| [NCT07352566](https://clinicaltrials.gov/study/NCT07352566) | Phase 4 | 모집 예정 | 10 | 아토피피부염·건선 대상 피내 마이크로디바이스를 이용한 국소 약물 전달 시험 |
| [NCT04908475](https://clinicaltrials.gov/study/NCT04908475) | Phase 4 | 완료 | 352 | 중등증 판상건선에서 Risankizumab vs Apremilast 비교(건선 위주, 참고용) |
| [NCT05969223](https://clinicaltrials.gov/study/NCT05969223) | Phase 4 | 완료 | 214 | 생식기/두피 건선 대상(건선 위주, 참고용) |
| [NCT04818385](https://clinicaltrials.gov/study/NCT04818385) | N/A (관찰) | 완료 | 240 | 대만 내 중등증~중증 만성 판상건선 코호트(건선 위주, 참고용) |
| [NCT07041112](https://clinicaltrials.gov/study/NCT07041112) | N/A (관찰) | 완료 | 1000 | 피부건선 생물학적 치료제 10년 생존율 유전-대사 인자 분석(건선 위주, 참고용) |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [36588137](https://pubmed.ncbi.nlm.nih.gov/36588137/) | 2023 | RCT | Dermatology and Therapy | 중등증~중증 아토피피부염 대상 Phase 2 RCT, IL-23/IL-22 차단 근거 제시 (핵심 근거) |
| [39668419](https://pubmed.ncbi.nlm.nih.gov/39668419/) | 2025 | Case series | International Journal of Dermatology | 아토피피부염+건선 동반 환자에서 Dupilumab+Risankizumab 병용 효과·안전성 |
| [33078990](https://pubmed.ncbi.nlm.nih.gov/33078990/) | 2020 | Review | Expert Opinion on Biological Therapy | 소아 아토피피부염 대상 생물학적제제 현황 및 개발 중인 후보 검토 |
| [39201826](https://pubmed.ncbi.nlm.nih.gov/39201826/) | 2024 | Review | Children (Basel) | 소아 원형탈모·건선·아토피피부염·화농성한선염 생물학적제제/소분자 치료 review |
| [38607726](https://pubmed.ncbi.nlm.nih.gov/38607726/) | 2024 | Review | Military Medicine | 건선·아토피피부염에서 전신 면역조절제 재평가 |
| [31098898](https://pubmed.ncbi.nlm.nih.gov/31098898/) | 2019 | Review | Drugs | Risankizumab 최초 글로벌 승인 리뷰(일본, 건선·건선성관절염·농포성건선·홍피성건선) |
| ⚠️ [33185530](https://pubmed.ncbi.nlm.nih.gov/33185530/) | 2020 | Case report | European Journal of Dermatology | 건선 환자에서 Risankizumab 치료 중 습진성 발진 발생 (역설적 반응) |
| ⚠️ [36939506](https://pubmed.ncbi.nlm.nih.gov/36939506/) | 2023 | Case report | Ital J Dermatol Venereol | Risankizumab 치료 중 습진성 발진 사례 |
| ⚠️ [41645692](https://pubmed.ncbi.nlm.nih.gov/41645692/) | 2026 | Case report | Dermatology Reports | IL-23 억제제(Risankizumab 등) 유발 역설적 습진에 Upadacitinib 사용 |
| ⚠️ [37014149](https://pubmed.ncbi.nlm.nih.gov/37014149/) | 2023 | Case series | J Cutan Med Surg | Brodalumab 유발 습진성 반응을 Risankizumab으로 전환하여 관리 |

⚠️ 표시 문헌은 "치료 효과"가 아닌 "역설적 습진 유발" 방향의 보고입니다.

## 한국 시판 정보

현재 한국 내 허가된 Risankizumab 제품 정보가 확인되지 않습니다 (미시판, 허가증 0건).

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

*(별도로, 문헌 근거상 IL-23 억제제 계열에서 역설적 습진/피부염 유발 사례가 보고되어 있어 — 위 임상근거 표 참조 — 신규 적응증 검토 시 이 방향성도 함께 평가해야 합니다.)*

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
아토피피부염을 직접 검증한 완료된 Phase 2 RCT(NCT03706040)와 이를 뒷받침하는 문헌(PMID 36588137)이 존재해 순수 모델 예측 이상의 근거 수준(L2)을 갖추고 있습니다. 다만 동일 기전 약물에서 반대 방향(피부염 유발)의 사례 보고가 다수 확인되어, 적응증 확장 검토 시 반드시 이 역설적 반응 가능성을 함께 평가해야 합니다.

**진행하려면 필요한 것:**
- TFDA(한국 식약처) 등재 여부 확인 및 허가사항 경고/금기 문서 확보 (DG001, Blocking)
- DrugBank 등 공식 소스를 통한 MOA 데이터 확보 (DG002, High)
- Phase 2 RCT(NCT03706040) 이후 Phase 3 후속 시험 진행 여부 확인
- 역설적 습진 발생률 및 위험군에 대한 체계적 문헌고찰(Systematic Review) 추가 확보
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

