---
layout: default
title: Zanubrutinib
parent: 모델 예측만 (L5)
nav_order: 790
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-31
description: "Zanubrutinib: 예측 신규 적응증 골수성 백혈병 (Myeloid leukemia) (근거 수준 L5). 기존 적응증: 허가 적응증 본문은 허가증 링크로만 제공되어 구체적 내용을 확인할 수 없음 (B세포 악성 종양 계열로 추정)"
monitor_inn: "ZANUBRUTINIB"
predicted_indications: ["myeloid leukemia", "vertebral anomalies and variable endocrine and T-cell dysfunction", "ganglioneuroblastoma (disease)", "retroperitoneal neoplasm", "Ewing sarcoma", "neuroblastoma"]
---

# Zanubrutinib
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **6** 건
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

## Zanubrutinib: B세포 악성 종양에서 골수성 백혈병으로
{: .text-alpha }

## 한 문장 요약

Zanubrutinib은 BTK(브루톤 티로신 키나제) 억제제로, 한국에서 B세포 악성 종양 치료제로 허가되어 시판 중입니다.
TxGNN 모델은 **골수성 백혈병(myeloid leukemia)**에 효과가 있을 수 있다고 예측하지만, 이 질환을 직접 뒷받침하는 임상시험은 없습니다. 관련 임상시험 1건은 병용 파트너로만 언급되며, 문헌 대부분은 림프구성 질환(CLL/SLL 등)에 관한 것입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문은 허가증 링크로만 제공되어 구체적 내용을 확인할 수 없음 (B세포 악성 종양 계열로 추정) |
| 예측 신규 적응증 | 골수성 백혈병 (Myeloid leukemia) |
| TxGNN 예측 점수 | 0.9965 |
| 근거 수준 | L5 (직접 근거가 부족하여 기전 수준의 간접 근거만 존재) |
| 한국 시판 현황 | 시판 중 (유효 허가 1건 / 전체 1건) |
| 허가증 수 | 1건 (유효 1건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Zanubrutinib은 선택성이 높은 차세대 BTK 억제제이며, BTK 신호전달은 B세포 악성 종양(CLL/SLL, 발덴스트롬 마크로글로불린혈증 등)과 밀접하게 관련됩니다.

TxGNN 모델(딥러닝)의 높은 점수는 CLL 같은 림프구성 백혈병에서의 확립된 활성과 '백혈병'이라는 관련 질환 간에 모델이 학습한 유사성을 반영한 것일 수 있으며, 생물학적 근거는 아닙니다. BTK는 B세포 질환의 핵심 표적이지만 골수성 백혈병에서의 의존성은 확립되지 않았습니다. 일부 전임상 연구에서 AML 모세포에 BTK가 발현된다고 보고되었으나, 이번에 수집된 데이터로는 뒷받침되지 않습니다. 따라서 기전상 타당성은 제한적입니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT05665530](https://clinicaltrials.gov/study/NCT05665530) | Phase 1 | 완료 | 86 | 재발/불응성 혈액 악성 종양에서 CDK9 억제제 PRT2527 단독 또는 zanubrutinib·venetoclax 병용의 안전성·효능 평가. Zanubrutinib은 병용 파트너이며 골수성 백혈병에 대한 직접 근거는 아님 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [39647999](https://pubmed.ncbi.nlm.nih.gov/39647999/) | 2025 | RCT | J Clin Oncol | 미치료 CLL/SLL에서 zanubrutinib vs 벤다무스틴+리툭시맙 (SEQUOIA, 중앙 5년 추적) |
| [34959482](https://pubmed.ncbi.nlm.nih.gov/34959482/) | 2021 | Review | Pharmaceutics | 만성 백혈병(CML, CLL)에서의 TKI 치료 개관 |
| [36402930](https://pubmed.ncbi.nlm.nih.gov/36402930/) | 2023 | Review | Leukemia | 발덴스트롬 마크로글로불린혈증에서 BTK 억제제 활용 |
| [37150651](https://pubmed.ncbi.nlm.nih.gov/37150651/) | 2023 | Review | Clin Lymphoma Myeloma Leuk | BTK 억제제 투여 환자의 B형간염 재활성화 |
| [42192981](https://pubmed.ncbi.nlm.nih.gov/42192981/) | 2026 | Review | Cancers | CLL에서 BTK 억제제의 저감마글로불린혈증 및 감염 위험 |
| [36400069](https://pubmed.ncbi.nlm.nih.gov/36400069/) | 2023 | Cohort | Lancet Haematol | 이전 BTK 억제제 불내성 B세포 악성 종양에서 zanubrutinib의 2상 단일군 시험 |
| [40334067](https://pubmed.ncbi.nlm.nih.gov/40334067/) | 2025 | Cohort | Blood Adv | ibrutinib/acalabrutinib 불내성 CLL/SLL에서 zanubrutinib의 내약성과 효능 (업데이트) |
| [40829104](https://pubmed.ncbi.nlm.nih.gov/40829104/) | 2026 | Cohort | Blood Adv | del(17p)/TP53 변이 CLL/SLL에서 zanubrutinib의 효능과 안전성 |
| [36325357](https://pubmed.ncbi.nlm.nih.gov/36325357/) | 2022 | Case report | Front Immunol | 발덴스트롬 마크로글로불린혈증과 B-ALL이 공존한 희귀 증례 |

위 문헌은 대부분 CLL/SLL 등 림프구성 질환에 관한 것으로, 골수성 백혈병에 대한 직접적 근거는 확인되지 않았습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202200854 | 브루킨사캡슐80밀리그램(자누브루티닙) | 흰색 내지 미백색의 불투명한 경질캡슐 | 허가증 원문 참조 (제조사: 비원메디슨코리아) |

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적치료제 (BTK 억제제) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 허가사항의 경고 및 주의사항을 참조하세요 (일반적으로 CBC 등 혈액학적 검사 고려) |
| 취급 방호 | 허가사항의 경고 및 주의사항을 참조하세요 |

## 안전성 고려사항

- **약물 상호작용**: 총 100건의 상호작용이 확인되었으며, 그중 주요(Major) 등급 항목은 다음과 같습니다.
  - Aprepitant, 아세틸살리실산(아스피린), Dexamethasone, Clarithromycin, Cobicistat, Deferasirox, Deferiprone, Samarium (153Sm) lexidronam, Ibritumomab tiuxetan, Tositumomab (I-131)
  - 중등도(Moderate) 항목 예: Cimetidine, Miconazole, Clotrimazole, Fenfluramine, Sibutramine, Troglitazone 등
- **문헌상 안전성 시사점**: BTK 억제제 투여 시 B형간염 재활성화, 저감마글로불린혈증 및 감염 위험이 보고되어 있습니다.

허가사항상의 경고·금기 정보는 이번 데이터에 포함되지 않았으므로 허가사항을 직접 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
골수성 백혈병에 대한 직접적인 임상시험이나 문헌이 없고, TxGNN 모델(딥러닝)의 높은 점수(0.9965)는 림프구성 백혈병 등 관련 질환 간에 모델이 학습한 유사성을 반영한 것일 수 있으며, 생물학적 근거는 아닙니다. BTK 신호전달은 B세포 질환의 표적이므로 골수성 백혈병에 대한 기전적 근거도 불충분합니다.

**진행하려면 필요한 것:**
- 허가 적응증 및 경고·금기 등 허가사항 원문 확보 (MFDS 첨부문서 PDF 분석)
- 상세한 작용 기전(MOA) 데이터 확보
- AML 등 골수성 질환에서 BTK 의존성을 보여주는 전임상 근거 검토
- 골수성 백혈병 환자를 대상으로 한 임상시험 근거 탐색 (현재 관련 시험은 병용 파트너로 언급된 1상 시험 1건뿐)
- 주요 약물 상호작용(CYP3A 관련 약물 등)에 대한 안전성 검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

