---
layout: default
title: Paliperidone
parent: 모델 예측만 (L5)
nav_order: 531
evidence_level: L5
indication_count: 10
---

# Paliperidone
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

# Paliperidone: 조현병(정신분열병)에서 망막이영양증으로 — 근거 부족으로 보류 권고

## 한 문장 요약

Paliperidone(팔리페리돈)은 risperidone의 활성 대사체로 알려진 항정신병 약물이지만, 현재 데이터셋에는 공식 작용기전(MOA) 및 기존 적응증 기록이 확보되어 있지 않습니다.
TxGNN 모델은 1순위로 **망막이영양증(retinal dystrophy with or without extraocular anomalies)**에 효과가 있을 수 있다고 예측했으나, 관련 임상시험은 없고 문헌 14편은 모두 안과 구조적 질환(안와 감염, 복시, 선천성 안검하수 등)을 다룰 뿐 D2/5-HT2A 길항 기전과 무관해, **그래프 공출현(co-occurrence) 잡음일 가능성이 높습니다.**

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인되지 않음 (한국 미출시, 공식 적응증 기록 없음) |
| 예측 신규 적응증 | 망막이영양증 (Retinal Dystrophy with or without Extraocular Anomalies) |
| TxGNN 예측 점수 | 99.92% (rank 2174) |
| 근거 수준 | L5 (모델 예측만 있음, 실제 관련 연구 없음) |
| 한국 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | **Hold** |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터가 확보되어 있지 않습니다. 다만 일반적으로 알려진 정보에 따르면 Paliperidone은 risperidone의 활성 대사체로서 D2/5-HT2A 수용체 길항 기전을 가진 항정신병 약물이며, 조현병 치료제로 사용되어 온 계열입니다.

그러나 이번 1순위 예측인 망막이영양증은 이 기전과 **직접적인 연관성을 찾기 어렵습니다.** 지지 문헌 14편을 검토한 결과 대부분 안와 감염, 복시, 선천성 안검하수, 렌즈 선천 기형, 외안근 섬유증 등 안과 구조적·발달적 질환을 다루고 있으며, 정신약리학적 기전과의 접점이 없습니다. 이는 TxGNN 지식그래프 상에서 우연히 함께 언급된 노드 간 공출현(co-occurrence) 패턴을 학습한 결과로 추정되며, 실제 약리학적 재창출 근거로 보기 어렵습니다.

> **참고**: 동일 Evidence Pack 내 10순위 후보인 **치료저항성 조현병(treatment-refractory schizophrenia)**은 TxGNN 점수(99.80%)는 낮지만, Phase 4 임상시험 4건(그중 1건은 A등급 관련성, paliperidone palmitate 직접 연구)과 문헌 2편이 뒷받침하며, 원 약물 계열의 자연스러운 확장 적응증으로 근거 수준 **L2**, 권장 결정 **Proceed with Guardrails**로 평가됩니다. 실질적으로 재창출 가치가 있는 후보는 1순위가 아니라 이 후보일 가능성이 높습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review | Seminars in Ultrasound, CT, and MR | 안와 감염 및 부비동염 관련 봉와직염 병기 분류, 항정신병 약물과 무관 |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Seminars in Neurology | 복시(diplopia)의 안과/신경학적 평가 접근법 |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klinische Monatsblätter für Augenheilkunde | 선천성 안검하수의 병태생리 및 치료 |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan Journal of Ophthalmology | 수정체 형태 선천기형 개관 |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case Report | American Journal of Ophthalmology | 편측 은안구증(cryptophthalmia) 증례 |
| [24413161](https://pubmed.ncbi.nlm.nih.gov/24413161/) | 2014 | Case Report | Journal of Neuro-Ophthalmology | 선천성 활차-동안신경 연합운동 증례 |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Review | Documenta Ophthalmologica | Wagner-Stickler 증후군 복합체 개관 |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatric Radiology | 소아 안와 병변의 안구 병리 영상 소견 |
| [19826317](https://pubmed.ncbi.nlm.nih.gov/19826317/) | 2009 | Case Report | Optometry and Vision Science | 선천성 외안근 섬유증 증례 |
| [19064847](https://pubmed.ncbi.nlm.nih.gov/19064847/) | 2008 | Case Report | Archives of Ophthalmology | 안와 동정맥 기형 증례 시리즈 |

> 위 문헌은 모두 안과 구조적/선천성 질환을 다루며, Paliperidone의 약리 기전과 직접적 연관성은 확인되지 않습니다.

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

> **비고 (Blocking 데이터 갭)**: 한국 허가증상 경고문/금기사항 자료가 확보되지 않아 안전성 초기평가(S1) 단계 진입이 불가능한 상태입니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
망막이영양증에 대한 TxGNN 예측 점수는 매우 높으나(99.92%), 이는 실제 약리 기전과 무관한 지식그래프 공출현 패턴으로 판단됩니다. 관련 임상시험이 전무하고, 문헌 14편 모두 항정신병 기전과 연관성이 없어 근거 수준 L5(모델 예측만 존재)에 해당합니다.

**진행하려면 필요한 것:**
- Paliperidone의 공식 작용기전(MOA) 자료 확보 (DrugBank API 재조회, DG002)
- 한국 허가사항의 경고문/금기사항 자료 확보 (Blocking, DG001) — 안전성 초기평가 선행 조건
- 망막이영양증-항정신병 기전 간 실질적 연관성을 뒷받침할 전임상/기전 연구 필요 (현재 전무)
- **대안 권고**: 본 Evidence Pack 내 10순위 후보인 치료저항성 조현병(L2, Proceed with Guardrails)에 대해 별도의 상세 평가 보고서 작성을 권장함 — 동일 약물 계열 확장 적응증으로 임상시험 근거가 실제로 존재함
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

