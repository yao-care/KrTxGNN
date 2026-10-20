---
layout: default
title: Risankizumab
parent: 모델 예측만 (L5)
nav_order: 657
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Risankizumab: 예측 신규 적응증 피부염 (Dermatitis) (근거 수준 L5). 기존 적응증: 허가 적응증 본문이 아닌 MFDS 허가문서 링크만 확인되어 구체적 적응증을 기재할 수 없음 (문헌상 판상 건선…"
monitor_inn: "Risankizumab"
predicted_indications: ["dermatitis", "neonatal dermatomyositis", "amyopathic dermatomyositis", "acrodermatitis chronica atrophicans", "acne keloid", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "hydroa vacciniforme, familial", "severe nonproliferative diabetic retinopathy"]
---

# Risankizumab
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

# Risankizumab: 판상 건선 등 IL-23 매개 질환에서 피부염(Dermatitis)으로

## 한 문장 요약

Risankizumab은 IL-23의 p19 소단위를 선택적으로 차단하는 단클론항체로, 한국에서 스카이리치라는 제품명으로 시판되고 있습니다.
TxGNN 모델은 **피부염(Dermatitis)**에 효과가 있을 수 있다고 예측하며, 현재 **2건의 임상시험**(아토피 피부염 Phase 2 포함)과 **20편의 문헌**이 이 방향과 관련되어 있습니다. 다만 아토피 피부염 Phase 2 시험의 효능 결과는 이번 데이터에서 확인되지 않았습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문이 아닌 MFDS 허가문서 링크만 확인되어 구체적 적응증을 기재할 수 없음 (문헌상 판상 건선, 건선성 관절염, 크론병 등으로 알려짐) |
| 예측 신규 적응증 | 피부염 (Dermatitis) |
| TxGNN 예측 점수 | 99.98% |
| 근거 수준 | L2 (완료된 Phase 2 무작위 대조 시험 1건, 아토피 피부염) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 5건 |
| 권장 결정 | Hold (추가 근거 확인 후 재검토) |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 DrugBank 등에서 확보되지 않았습니다. 다만 문헌에 따르면 risankizumab은 IL-23 p19 소단위를 표적으로 하는 인간화 IgG1 단클론항체이며, IL-23/Th17 축이 관여하는 염증성 피부질환에서 효능이 입증되어 있습니다.

피부염 중 아토피 피부염은 주로 Th2 경로가 중심이지만, Th22 및 일부 Th17 경로도 관여하는 것으로 알려져 IL-23/IL-22 차단이 이론적으로 가능합니다. 그러나 건선에 비해 기전적 근거는 약합니다. 또한 건선 환자에서 risankizumab 투여 중 습진양 발진이 나타났다는 증례 보고가 여러 건 있어, 피부염에 대한 효과가 일관되지 않을 수 있습니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT03706040](https://clinicaltrials.gov/study/NCT03706040) | Phase 2 | 완료 | 172 | 성인·청소년 중등도~중증 아토피 피부염에서 risankizumab의 안전성·효능을 평가한 무작위 이중맹검 위약대조 시험 (결과 수치는 제공 데이터에 없음) |
| [NCT07352566](https://clinicaltrials.gov/study/NCT07352566) | Phase 4 | 모집 예정 | 10 | 아토피 피부염·건선 약물을 피부에서 직접 시험하는 마이크로디바이스 연구로, 효능 근거는 아님 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [36588137](https://pubmed.ncbi.nlm.nih.gov/36588137/) | 2023 | RCT (Phase 2) | Dermatol Ther | 중등도~중증 아토피 피부염에서 IL-23·IL-22 차단의 근거를 바탕으로 한 위약대조 시험 (초록에 결과 없음) |
| [39668419](https://pubmed.ncbi.nlm.nih.gov/39668419/) | 2025 | 증례 보고 | Int J Dermatol | 아토피 피부염과 건선이 동반된 환자에서 dupilumab과 risankizumab 병용 효과 및 안전성 |
| [40856907](https://pubmed.ncbi.nlm.nih.gov/40856907/) | 2025 | 체계적 문헌고찰 | Am J Clin Dermatol | 홍피성 건선의 전신 치료 관리 |
| [40794374](https://pubmed.ncbi.nlm.nih.gov/40794374/) | 2025 | 체계적 문헌고찰 | Inflammopharmacology | 편평태선에서 인터루킨 억제제의 치료 효과와 역설적 효과 |
| [39201826](https://pubmed.ncbi.nlm.nih.gov/39201826/) | 2024 | 리뷰 | Children (Basel) | 소아 원형탈모, 건선, 아토피 피부염, 화농성 한선염의 생물학적 제제 |
| [33078990](https://pubmed.ncbi.nlm.nih.gov/33078990/) | 2020 | 리뷰 | Expert Opin Biol Ther | 소아 아토피 피부염의 최신·신규 생물학적 제제 |
| [41645692](https://pubmed.ncbi.nlm.nih.gov/41645692/) | 2026 | 증례 보고 | Dermatol Rep | IL-23 억제제로 유발된 역설적 습진에 upadacitinib 사용 |
| [33185530](https://pubmed.ncbi.nlm.nih.gov/33185530/) | 2020 | 증례 보고 | Eur J Dermatol | 건선 환자에서 risankizumab 치료 중 습진양 발진 |
| [36939506](https://pubmed.ncbi.nlm.nih.gov/36939506/) | 2023 | 증례 보고 | Ital J Dermatol Venereol | risankizumab 치료 중 발생한 습진양 발진 |
| [37014149](https://pubmed.ncbi.nlm.nih.gov/37014149/) | 2023 | 증례 보고 | J Cutan Med Surg | brodalumab 유발 습진양 반응 환자를 risankizumab으로 전환하여 관리 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201908205 | 스카이리치프리필드시린지주 | 프리필드시린지 주사제 | 허가문서 링크만 확인됨 (적응증 본문 미확인) |
| 202303132 | 스카이리치주 | 바이알 주사제 | 허가문서 링크만 확인됨 (적응증 본문 미확인) |
| 202303133 | 스카이리치카트리지주 | 프리필드카트리지·온바디인젝터 주사제 | 허가문서 링크만 확인됨 (적응증 본문 미확인) |
| 202201668 | 스카이리치프리필드시린지주150mg/mL | 프리필드시린지 주사제 | 허가문서 링크만 확인됨 (적응증 본문 미확인) |
| 202201669 | 스카이리치프리필드펜주150mg/mL | 프리필드펜 주사제 | 허가문서 링크만 확인됨 (적응증 본문 미확인) |

제조사는 모두 한국애브비(주)입니다.

## 안전성 고려사항

- **약물 상호작용**: 이번 데이터에서 총 78건의 상호작용이 확인되었으며, 주요(Major) 등급은 다음과 같습니다.
  - Adalimumab
  - Baricitinib
  - Certolizumab pegol
  - Cladribine
- 중등도(Moderate) 등급에는 tacrolimus, cyclosporine, azathioprine, roflumilast, anakinra, denosumab 및 일부 백신(파상풍 톡소이드, 탄저 백신, 콜레라 생백신 등)이 포함됩니다. 아연 제제는 경미(Minor) 등급입니다.
- 면역억제 계열 약물과 병용 시 감염 위험에 유의해야 하며, 생물학적 제제의 일반적 주의사항(결핵 선별검사, 감염 모니터링)이 적용될 수 있습니다.
- 경고 및 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
피부염(특히 아토피 피부염)에 대해 완료된 Phase 2 무작위 시험이 1건 있으나 효능 결과가 확인되지 않았고, 아토피 피부염은 Th2 중심 질환이라 기전적 근거도 건선보다 약합니다. 또한 risankizumab 투여 중 습진양 발진이 발생한 증례가 여러 건 보고되어 있어, 결과 확인 전에는 진행을 권장하기 어렵습니다.

**진행하려면 필요한 것:**
- NCT03706040 및 PMID 36588137의 1차·2차 평가변수 결과(효능 및 안전성) 확인
- 허가문서(MFDS 허가사항)의 적응증, 경고, 금기 본문 확보
- 작용 기전 데이터(DrugBank 등) 보강
- 습진양 발진 등 역설적 반응의 위험-이익 평가
- 피부염 중 어떤 아형(아토피 피부염 등)을 목표로 할지 명확화

> 참고: TxGNN 순위 7위인 건선(점수 99.96%)은 완료된 다수의 Phase 3 RCT(UltIMMa-1/2 등)로 뒷받침되는 기존 적응증으로, 새로운 재창출이 아니라 모델 예측의 타당성을 확인해 주는 사례입니다. 나머지 예측(신생아 피부근염, 무근육병성 피부근염, 만성 위축성 말단피부염, 여드름 켈로이드, 소아 간질성 폐질환, 가족성 종두양 수포증, 중증 비증식성 당뇨망막병증, 유건선)은 모델 점수만 있고 임상시험·문헌 근거가 없어 보류(Hold)가 적절합니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

