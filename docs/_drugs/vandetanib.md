---
layout: default
title: Vandetanib
parent: 높은 근거 (L1-L2)
nav_order: 778
evidence_level: L2
indication_count: 10
last_modified_at: 2026-10-28
description: "Vandetanib: 예측 신규 적응증 신세포암 (Renal Cell Carcinoma) (근거 수준 L5). 기존 적응증: 허가증에 적응증 원문이 텍스트로 제공되지 않아 확인 불가 (허가사항 문서 링크만 제공됨)"
monitor_inn: "Vandetanib"
predicted_indications: ["renal cell carcinoma (disease)", "renal cell carcinoma associated with Xp11.2 translocations/TFE3 gene fusions", "renal cell carcinoma associated with neuroblastoma", "unclassified renal cell carcinoma", "renal pelvis carcinoma", "clear cell renal carcinoma", "childhood kidney cell carcinoma", "renal carcinoma", "angiolipoma", "familial spontaneous pneumothorax"]
---

# Vandetanib
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

## Vandetanib: 한국 허가 적응증에서 신세포암(Renal Cell Carcinoma)으로
{: .text-alpha }

## 한 문장 요약

Vandetanib은 VEGFR-2, EGFR, RET 티로신 키나제를 억제하는 경구 항종양제로, 한국에서 단일제 형태(카프렐사정)로 허가되어 시판 중입니다. TxGNN 모델은 **신세포암(Renal Cell Carcinoma)**에 효과가 있을 수 있다고 예측하며, 현재 **4건의 임상시험**(대부분 소규모 또는 조기 종료된 2상)과 **5편의 문헌**(대부분 리뷰 및 전임상)이 이 방향을 부분적으로 지지합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가증에 적응증 원문이 텍스트로 제공되지 않아 확인 불가 (허가사항 문서 링크만 제공됨) |
| 예측 신규 적응증 | 신세포암 (Renal Cell Carcinoma) |
| TxGNN 예측 점수 | 0.9992 |
| 근거 수준 | L2 (3상 근거 없음, 완료된 2상 시험이 있으나 소규모·단일군 또는 간접적 모집단) |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 2건 |
| 권장 결정 | Hold (연구 질문 단계로 추가 근거 필요) |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 DrugBank 등에서 확보되지 않았습니다. 다만 이 보고서를 위해 수집된 자료에 따르면, Vandetanib은 VEGFR-2, EGFR, RET 티로신 키나제를 억제하는 다중 키나제 억제제입니다.

신세포암, 특히 투명세포 신세포암에서는 VHL 유전자 불활성화로 HIF가 안정화되고 VEGF가 과발현됩니다. 따라서 VEGFR-2 억제를 통한 혈관신생 차단은 기전상 타당한 접근이며, 이미 승인된 여러 신세포암 치료제(TKI)도 같은 경로를 표적으로 합니다.

다만 완료된 2상 시험은 규모가 작거나 특정 유전적 하위군(VHL병)에 한정되어 있고, 두 건은 매우 적은 환자 수로 조기 종료되었습니다. 기존 승인 TKI 대비 이점을 보여주는 3상 근거도 없습니다. 기존 적응증과 신규 적응증 간 유사성 평가는 아직 이루어지지 않았습니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00566995](https://clinicaltrials.gov/study/NCT00566995) | Phase 2 | 완료 | 37 | VHL병 및 신장 종양 환자 대상 단일군 시험. VHL/VEGF 축을 직접 겨냥하나 희귀 유전 질환 집단이며 결과 수치는 제공되지 않음 |
| [NCT01372813](https://clinicaltrials.gov/study/NCT01372813) | Phase 2 | 종료(조기 중단) | 3 | 진행성 투명세포 신세포암 대상. 3명만 등록되어 해석 가능한 효능 자료 없음 |
| [NCT02495103](https://clinicaltrials.gov/study/NCT02495103) | Phase 1/2 | 종료(조기 중단) | 7 | HLRCC/SDH 관련 신장암 및 산발성 유두상 신세포암에서 Vandetanib + Metformin 병용. 7명 등록으로 효능 결론 불가 |
| [NCT01191892](https://clinicaltrials.gov/study/NCT01191892) | Phase 2 | 완료 | 82 | 시스플라틴 부적합 진행성 요로상피암에서 Carboplatin/Gemcitabine ± Vandetanib 무작위 시험. 신우암을 포함할 수 있으나 일반 신세포암에는 간접적이며 결과는 제공되지 않음 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [40779213](https://pubmed.ncbi.nlm.nih.gov/40779213/) | 2025 | Review | Clin Exp Metastasis | 전이성 푸마르산 수화효소 결핍 신세포암의 대사·후성유전 표적 치료. 표준 치료가 없으며 여러 2상 시험이 표적치료 병용을 평가 중 |
| [26677336](https://pubmed.ncbi.nlm.nih.gov/26677336/) | 2015 | Review | OncoTargets Ther | Nintedanib 중심의 항혈관신생제 개관. Vandetanib을 포함한 항혈관신생 TKI가 여러 암에서 승인되었음을 언급 |
| [42107510](https://pubmed.ncbi.nlm.nih.gov/42107510/) | 2026 | Review | Pharmacol Res | RET 주도 갑상선암·폐암에서의 RET 억제제 개관. 신세포암 효능과는 직접 관련 없음 |
| [24451769](https://pubmed.ncbi.nlm.nih.gov/24451769/) | 2012 | Review | ASCO Educ Book | 진행성 갑상선암의 전신 치료. Vandetanib이 수질 갑상선암에서 승인된 배경 설명 |
| [31043488](https://pubmed.ncbi.nlm.nih.gov/31043488/) | 2019 | 전임상 | Mol Cancer Res | TFE3 Xp11.2 전좌 신세포암 마우스 모델. 새로운 치료 표적을 제시하나 Vandetanib 자체의 효과를 평가한 것은 아님 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201307454 | 카프렐사정300밀리그램(반데타닙) | 필름 코팅정 (타원형) | 적응증 원문 미제공 (허가사항 문서 참조) |
| 201307453 | 카프렐사정100밀리그램(반데타닙) | 필름 코팅정 (원형) | 적응증 원문 미제공 (허가사항 문서 참조) |

두 제품 모두 (주)사노피-아벤티스코리아가 보유한 유효한 단일제 허가입니다.

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적치료제 (다중 티로신 키나제 억제제: VEGFR-2, EGFR, RET) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | QT 간격 연장 위험(심전도, 전해질), 간기능, 단백뇨 (VEGFR TKI 계열 문헌 근거) |
| 취급 방호 | 허가사항의 경고 및 주의사항을 참조하세요 |

## 안전성 고려사항

- **주요 경고**: 허가사항 기반 경고 정보는 확보되지 않았습니다. 다만 계열 효과 및 문헌에서 QT 간격 연장 위험, 간독성, 단백뇨, 치료 관련 사망 위험(VEGFR TKI 메타분석), 광독성이 보고되어 있어 주의가 필요합니다.
- **약물 상호작용**: 총 100건이 확인되었으며, 이 중 주요(Major) 등급은 다음과 같습니다.
  - Clarithromycin
  - Levofloxacin
  - Dolasetron
  - Palonosetron
  - Picosulfuric acid
  - Polyethylene glycol (전해질 포함 3350)
  - Sodium sulfate

  중등도(Moderate) 상호작용으로는 Famotidine, Metformin, Loperamide, Dexamethasone, Bisacodyl, Lactitol 등이 있습니다. QT 연장 약물 및 전해질 이상을 유발하는 약물과의 병용에 특히 유의해야 합니다.

나머지 안전성 정보(금기 등)는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
신세포암에 대한 기전적 근거(VHL-HIF-VEGF 축)는 타당하지만, 완료된 2상 시험은 소규모 단일군(VHL병, n=37)이거나 간접적 모집단이고, 직접 관련된 두 건은 3명, 7명으로 조기 종료되었습니다. 3상 근거가 없고 기존 승인 TKI 대비 이점도 입증되지 않았으며, QT 연장 등 안전성 부담이 있어 현 단계에서는 연구 질문 수준으로 보는 것이 적절합니다. 신세포암 하위 유형 중 연관 예측(소아 신세포암, 신경모세포종 연관 신세포암, 혈관지방종, 가족성 자연기흉 등)은 임상·문헌 근거가 전혀 없어 보류가 적절합니다.

**진행하려면 필요한 것:**
- 허가사항(MFDS 첨부문서) 확보 및 분석: 경고, 금기, 허가 적응증 확인 (현재 차단 수준의 자료 공백)
- DrugBank 등에서 작용 기전 데이터 보충
- NCT00566995(VHL병 2상)의 결과 데이터 확인 및 반응률·무진행생존 평가
- 기존 승인 신세포암 TKI와 비교한 효능·안전성 검토, 필요 시 적절한 설계의 추가 2상 시험
- QT 연장, 간독성, 단백뇨에 대한 모니터링 계획 수립
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

