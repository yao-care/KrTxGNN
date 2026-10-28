---
layout: default
title: Fludarabine
parent: 높은 근거 (L1-L2)
nav_order: 353
evidence_level: L2
indication_count: 10
last_modified_at: 2026-10-15
description: "Fludarabine: 예측 신규 적응증 형질세포 골수종 (Plasma Cell Myeloma) (근거 수준 L5). 기존 적응증: 허가 적응증 문구가 링크 형태로만 확인되어 구체적인 내용은 허가사항 참조 필요"
monitor_inn: "Fludarabine"
predicted_indications: ["plasma cell myeloma", "hyperthyroidism", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "indolent plasma cell myeloma", "resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta", "brain small vessel disease 1 with or without ocular anomalies", "myelodysplastic syndrome", "unclassified myelodysplastic syndrome", "partial deletion of the long arm of chromosome 5", "diabetic nephropathy"]
---

# Fludarabine
{: .fs-9 }

근거 수준: **L2** | 예측 적응증: **10** 건
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

## Fludarabine: 만성 림프구성 백혈병 등 혈액암에서 형질세포 골수종으로
{: .text-alpha }

## 한 문장 요약

Fludarabine은 퓨린 뉴클레오시드 유사체 계열의 항암제로, 한국에서 주사제로 허가·시판되고 있습니다.
TxGNN 모델은 **형질세포 골수종(다발골수종, Plasma Cell Myeloma)**에 효과가 있을 수 있다고 예측하며, 현재 **임상시험 29건**과 **문헌 19편**이 이 방향과 관련되어 있습니다. 다만 대부분은 fludarabine을 이식 전처치 또는 림프구 제거 요법의 일부로 사용한 연구이며, fludarabine 단독의 항골수종 효과를 직접 검증한 근거는 아닙니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 문구가 링크 형태로만 확인되어 구체적인 내용은 허가사항 참조 필요 |
| 예측 신규 적응증 | 형질세포 골수종 (Plasma Cell Myeloma) |
| TxGNN 예측 점수 | 0.9982 |
| 근거 수준 | L2 (조건부 해석, 아래 참조) |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 2건 |
| 권장 결정 | Proceed with Guardrails |

> **근거 수준 참고:** 이 보고서에 정리된 자료 기준으로 완료된 Phase 2/3 RCT는 확인되지 않았습니다. 다발골수종에서 fludarabine을 직접 평가한 완료 Phase 2 시험(NCT01008462 등)은 단일군 연구이며, 이식 전처치의 일부입니다. 따라서 L2는 상한선으로 보아야 하며, 엄밀하게 적용하면 L3~L4에 가깝습니다.

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 fludarabine은 DNA 합성을 억제하는 퓨린 뉴클레오시드 유사체로, 림프구계 세포에 세포독성을 나타냅니다. 같은 B세포 계열 종양이라는 점에서 다발골수종에도 적용될 여지가 있습니다.

실제 임상에서 fludarabine은 다발골수종의 단독 치료제가 아니라, cyclophosphamide와 함께하는 림프구 제거 요법(CAR-T 치료 전)이나 저강도 전처치(동종 조혈모세포이식 전)에 주로 쓰입니다. 전임상 연구에서는 골수종 세포주에 대한 항종양 활동이 보고되었으나(PMID 17976186, 다른 예측 질환 항목에서 확인), 골수종에서의 효과에 대해서는 논란이 있습니다.

따라서 이 예측은 "단독 항골수종제"보다는 "이식·세포치료의 전처치 기반 약물"로서의 가치로 해석하는 것이 타당합니다.

## 임상시험 근거

다발골수종과 직접 관련된 시험 중 fludarabine이 포함된 주요 시험입니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT03303950](https://clinicaltrials.gov/study/NCT03303950) | Phase 2 | 조기 종료 | 6 | 다발골수종/골수섬유증에서 busulfan·fludarabine 전처치 후 동종 이식. 6명 등록 후 종료 |
| [NCT01008462](https://clinicaltrials.gov/study/NCT01008462) | Phase 2 | 완료 | 16 | 고위험 림프종·골수종·CLL에서 자가이식 후 반일치 동종이식(fludarabine 전처치 포함) |
| [NCT01658319](https://clinicaltrials.gov/study/NCT01658319) | Phase 1 | 완료 | 20 | 재발·불응성 혈액암에서 fludarabine + methoxyamine(TRC102) 병용 |
| [NCT00309842](https://clinicaltrials.gov/study/NCT00309842) | Phase 2 | 완료 | 213 | 혼합 혈액질환에서 cyclophosphamide/fludarabine/TBI 전처치 후 제대혈 이식 |
| [NCT06045806](https://clinicaltrials.gov/study/NCT06045806) | Phase 3 | 모집 종료(진행 중) | 79 | 신규 진단 골수종에서 ide-cel + lenalidomide 유지요법 비교. fludarabine은 림프구 제거 구성요소일 뿐 |
| [NCT07764978](https://clinicaltrials.gov/study/NCT07764978) | Phase 3 | 모집 중 | 750 | AZD0120 CAR-T 공고요법 시험. fludarabine은 림프구 제거 배경 요법 |
| [NCT05020444](https://clinicaltrials.gov/study/NCT05020444) | Phase 1 | 모집 종료(진행 중) | 16 | TriPRIL CAR-T. fludarabine/cyclophosphamide를 림프구 제거에 사용 |
| [NCT00014508](https://clinicaltrials.gov/study/NCT00014508) | Phase 2 | 완료 | 정보 없음 | 다발골수종에서 자가이식 후 미니 동종이식 |

Phase 3 시험은 모두 CAR-T 치료를 평가하는 것이며 fludarabine 자체를 검증하는 것이 아닙니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [40972962](https://pubmed.ncbi.nlm.nih.gov/40972962/) | 2025 | 코호트 | Transplant Cell Ther | 재발·불응성 골수종에서 ide-cel 투여 전 fludarabine 노출량이 독성과 연관됨 (용량 설정에 중요) |
| [38483213](https://pubmed.ncbi.nlm.nih.gov/38483213/) | 2024 | Phase 1 | Am J Clin Oncol | 고위험·재발성 골수종에서 bortezomib/fludarabine/melphalan(±전신골수조사) 동종이식 전처치 |
| [17310135](https://pubmed.ncbi.nlm.nih.gov/17310135/) | 2007 | 후향적 분석 | Bone Marrow Transplant | 골수종 환자 34명에서 fludarabine/treosulfan 저독성 전처치의 실행 가능성 |
| [37701906](https://pubmed.ncbi.nlm.nih.gov/37701906/) | 2023 | Phase 2 | Leuk Res Rep | 골수종 2명·골수섬유증 4명 대상 분할 busulfan/fludarabine/cyclophosphamide 동종이식. 1년 비재발 사망률 33.3% |
| [1415309](https://pubmed.ncbi.nlm.nih.gov/1415309/) | 1992 | 리뷰 | Am J Med | 다발골수종과 만성 림프구성 백혈병의 유사점과 차이점 |
| [31058154](https://pubmed.ncbi.nlm.nih.gov/31058154/) | 2019 | 리뷰 | Front Med | 혈액암에서의 [18F]-fludarabine 영상 |
| [38576761](https://pubmed.ncbi.nlm.nih.gov/38576761/) | 2024 | 리뷰 | World J Transplant | 자가조혈모세포이식 전처치 요법과 CAR-T 치료 |

이 외 CAR-T 관련 문헌(PMID 39365257, 38659046, 35333600 등)은 fludarabine을 직접 평가한 것이 아니어서 생략했습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200801541 | 플루다라주(플루다라빈포스페이트) | 동결건조분말 주사제 (바이알) | 허가사항 참조(적응증 원문은 MFDS 문서 링크로만 제공) |
| 201402854 | 삼오플루다라빈주(플루다라빈포스페이트) | 분말 주사제 | 허가사항 참조(적응증 원문은 MFDS 문서 링크로만 제공) |

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 약물 (퓨린 뉴클레오시드 유사체 / 항대사제) |
| 골수억제 위험 | 고 (문헌상 상당한 골수억제 보고, PMID 23787174) |
| 구토 유발성 등급 | 저 (일반적 분류. 이 보고서 자료에는 직접 데이터 없음) |
| 모니터링 항목 | CBC(분획 포함), 간·신기능, 감염 징후, 신경독성 관찰 |
| 취급 방호 | 세포독성 약물 취급 규정 준수 필요 |

고용량 사용 시 비가역적 신경독성이 보고되었고(PMID 7525188), 치료 관련 골수형성이상증후군/급성 골수성 백혈병 위험도 보고되었습니다(PMID 20962860). 세부 사항은 허가사항의 경고 및 주의사항을 참조하세요.

## 안전성 고려사항

**약물 상호작용:** 이 보고서에 정리된 데이터에서 총 100건의 상호작용이 확인되었으며, 그중 상위 20건의 분류는 다음과 같습니다.
- **중등도(Moderate):** Metronidazole, Rosuvastatin, Simvastatin, Tinidazole
- **경미(Minor):** Levofloxacin
- **등급 미확인:** Doxycycline, Clotrimazole, Cimetidine, Amphotericin B, Dolasetron, Famotidine, Acetylsalicylic acid, Amoxicillin, Pantoprazole, Glimepiride, Morphine, Metformin, Omeprazole, Sucralfate, Palonosetron

주요 경고와 금기는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
Fludarabine은 다발골수종에서 동종이식 전처치와 CAR-T 림프구 제거 요법의 핵심 구성요소로 이미 쓰이고 있어 임상적 연관성은 분명합니다. 그러나 근거는 요법 전체에 대한 것이며 fludarabine 단독의 항골수종 효능을 입증하지 못했고, 직접 근거는 소규모·단일군·조기 종료 시험에 한정됩니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기·용법용량) 확보 및 검토: 이번 자료에서는 허가 문서 내용이 확인되지 않았습니다.
- 작용 기전(MOA) 데이터 보완
- 적응증을 "단독 항골수종제"가 아닌 "이식 전처치/림프구 제거 요법 구성요소"로 정의
- 신기능·골수기능에 따른 용량 조정과 노출량-독성 관계(PMID 40972962) 고려
- 골수억제, 신경독성, 감염 위험에 대한 모니터링 계획

---

### 참고: 기타 예측 적응증

| 예측 적응증 | TxGNN 점수 | 근거 수준 | 평가 |
|------|------|------|------|
| 무통성 형질세포 골수종 | 0.9976 | L5 | 전임상 항골수종 활성과 이식 전처치 근거가 있으나 혼합 질환 대상 시험이 대부분 |
| 골수이형성증후군 | 0.9975 | L2 | 이식 전처치 기반 요법으로 근거 풍부(무작위 Phase 3 비교 포함), 단독 치료 근거는 아님 |
| 분류되지 않은 골수이형성증후군 | 0.9969 | L5 | 단일 Phase 2 연구(treosulfan/fludarabine)만 존재 |
| 갑상선기능항진증 외 5개 질환(유전성 희귀질환, 당뇨병성 신증 등) | 99.68~0.9982 | L5 | 기전적 연관성이 확인되지 않아 보류(Hold). 모델 예측만 존재 |
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

