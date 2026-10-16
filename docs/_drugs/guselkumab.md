---
layout: default
title: Guselkumab
parent: 모델 예측만 (L5)
nav_order: 397
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Guselkumab: 예측 신규 적응증 약물유발 골다공증 (Drug-induced osteoporosis) (근거 수준 L5). 기존 적응증: 허가증에는 적응증 본문 대신 문서 링크만 있어 허가 적응증 문구를 확인하지 못했습니다. 문헌상 주 사용 질환은 판상 건선입니다"
monitor_inn: "Guselkumab"
predicted_indications: ["drug-induced osteoporosis", "severe nonproliferative diabetic retinopathy", "psoriasis", "diabetic retinopathy", "renal osteodystrophy", "ulcerative colitis (disease)", "congenital hypotrichosis with juvenile macular dystrophy", "primary release disorder of platelets", "Glanzmann thrombasthenia", "non-renal secondary hyperparathyroidism"]
---

# Guselkumab
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

# Guselkumab: 건선(IL-23 억제제)에서 약물유발 골다공증으로

## 한 문장 요약

Guselkumab은 IL-23 p19 소단위를 선택적으로 억제하는 단클론항체로, 주로 건선 등 면역매개 염증질환 치료에 사용됩니다.
TxGNN 모델은 **약물유발 골다공증(Drug-induced osteoporosis)**에 효과가 있을 수 있다고 예측했습니다.
그러나 이 적응증을 직접 뒷받침하는 **임상시험은 0건, 문헌도 0편**이어서 모델 예측만 있는 상태입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가증에는 적응증 본문 대신 문서 링크만 있어 허가 적응증 문구를 확인하지 못했습니다. 문헌상 주 사용 질환은 판상 건선입니다. |
| 예측 신규 적응증 | 약물유발 골다공증 (Drug-induced osteoporosis) |
| TxGNN 예측 점수 | 99.84% |
| 근거 수준 | L5 (모델 예측만 있음) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 3건 (모두 유효, 단일제) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 DrugBank 등 데이터베이스에는 정리되어 있지 않습니다. 다만 문헌에 따르면 guselkumab은 IL-23의 p19 소단위를 억제하는 완전 인간 단클론항체입니다. IL-23/Th17 축은 건선 병태생리의 핵심입니다.

IL-23/IL-17 신호는 뼈 리모델링과 이론적으로 연결될 수 있습니다. 그러나 guselkumab이 글루코코르티코이드 등 약물로 인한 골소실에 효과가 있다는 직접 근거는 이번에 수집한 자료에 없습니다. 따라서 이 예측은 기전상 가능성이 있다는 가설 수준입니다. 건선과 약물유발 골다공증 사이의 질환 유사성 평가도 아직 이루어지지 않았습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202104066 | 트렘피어원프레스오토인젝터주 (구셀쿠맙, 유전자재조합) | 오토인젝터 장착 프리필드시린지 주사제 | 허가 문서 링크만 확인됨 (적응증 본문 미확인) |
| 201801604 | 트렘피어프리필드시린지주 (구셀쿠맙, 유전자재조합) | 프리필드시린지 주사제 | 허가 문서 링크만 확인됨 (적응증 본문 미확인) |
| 202502173 | 트렘피어정맥주사 (구셀쿠맙, 유전자재조합) | 유리바이알 정맥주사제 | 허가 문서 링크만 확인됨 (적응증 본문 미확인) |

세 제품 모두 제조사는 (주)한국얀센입니다.

## 안전성 고려사항

- **허가사항 경고·금기**: 이번에 수집한 자료에서 확인되지 않았습니다. 허가사항을 직접 참조하세요.
- **약물 상호작용**: 조회된 상호작용은 총 100건입니다. 그중 주요 항목은 다음과 같습니다.
  - **Major**: Adalimumab
  - **Moderate**: Simvastatin, Warfarin, Apixaban, Rivaroxaban, Dicoumarol, Tacrolimus, Theophylline, Roflumilast, Lidocaine, Fentanyl, Hydrocodone, Nifedipine, 파상풍 톡소이드 백신
  - **Minor**: 아연 제제 (황산아연, 아세트산아연, 글루콘산아연, 염화아연)

## 다른 예측 적응증 참고

모델이 함께 예측한 질환 중 근거가 있는 것은 아래 두 가지입니다. 이 표는 위의 1순위 예측과는 별개의 평가입니다.

| 예측 질환 | TxGNN 점수 | 근거 수준 | 주요 근거 | 권장 결정 |
|---------|-----------|---------|---------|---------|
| 궤양성 대장염 | 99.70% | L1 | Phase 3 QUASAR와 ASTRO 시험이 [PMID 39706209](https://pubmed.ncbi.nlm.nih.gov/39706209/), [PMID 41544637](https://pubmed.ncbi.nlm.nih.gov/41544637/)에 보고됨. 관련 Phase 3 시험이 다수 진행 중 (예: [NCT05528510](https://clinicaltrials.gov/study/NCT05528510), [NCT04033445](https://clinicaltrials.gov/study/NCT04033445)) | Proceed with Guardrails |
| 건선 | 99.75% | L1 | VOYAGE 1·2 등 완료된 Phase 3 RCT 다수 ([PMID 28057360](https://pubmed.ncbi.nlm.nih.gov/28057360/), [PMID 28057361](https://pubmed.ncbi.nlm.nih.gov/28057361/)) | Proceed with Guardrails |

- **궤양성 대장염**: 한국 허가 적응증에 포함되는지 확인되지 않았으므로, 진행 전에 허가 상태 확인이 필요합니다.
- **건선**: 기존에 사용되는 적응증으로 보이므로 신규 재창출이라기보다 기존 사용의 재확인에 가깝습니다.
- **그 외 예측 질환**: 당뇨망막병증, 신성 골이영양증, 혈소판 질환 등 나머지는 모두 근거 수준 L5로, 임상시험과 문헌이 없고 기전 근거도 약해 Hold입니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
약물유발 골다공증은 점수(99.84%)는 높지만 임상시험과 문헌이 전혀 없는 모델 예측 단계입니다. 직접적인 기전 근거도 확인되지 않았습니다.

**진행하려면 필요한 것:**
- IL-23 차단과 골대사(약물유발 골소실) 관련 전임상 또는 기전 연구
- 골다공증 환자군을 대상으로 한 관찰 연구 또는 탐색적 임상시험
- 허가 적응증 본문과 경고·금기를 포함한 허가사항 확인
- 상세 작용 기전(MOA) 데이터 보완
- 우선순위 조정 검토: 근거가 확보된 궤양성 대장염을 먼저 평가하는 방안
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

