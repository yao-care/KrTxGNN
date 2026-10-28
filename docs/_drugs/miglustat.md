---
layout: default
title: Miglustat
parent: 모델 예측만 (L5)
nav_order: 516
evidence_level: L5
indication_count: 10
monitor_inn: "Miglustat"
predicted_indications: ["autosomal ichthyosis syndrome with fatal disease course", "cholesteryl ester storage disease", "Krabbe disease", "metachromatic leukodystrophy", "Wolman disease with hypolipoproteinemia and acanthocytosis", "encephalopathy due to prosaposin deficiency", "Tay-Sachs disease", "benign neoplasm of adrenal gland", "recessive X-linked ichthyosis", "fatty acid hydroxylase-associated neurodegeneration"]
last_modified_at: 2026-10-23
description: "Miglustat: 예측 신규 적응증 치명적 경과의 상염색체 어린선 증후군 (근거 수준 L5). 기존 적응증: 허가 문서가 링크로만 제공되어 적응증 본문을 확인할 수 없습니다. 약리 데이터베이스에는 고셰병 치료에 사용된다고 기재되어 있…"
---

# Miglustat
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

## Miglustat: 당지질 저장질환 치료제에서 치명적 경과의 상염색체 어린선 증후군으로
{: .text-alpha }

## 한 문장 요약

Miglustat은 한국에서 자베스카캡슐100밀리그램(한국얀센)으로 허가된 단일성분 약물입니다. TxGNN 모델은 **치명적 경과의 상염색체 어린선 증후군(autosomal ichthyosis syndrome with fatal disease course)**에 효과가 있을 수 있다고 예측하지만, 이 질환을 직접 다룬 임상시험과 문헌은 **0건**입니다. 즉 모델 예측만 있는 단계입니다. 다만 같은 약물의 다른 예측 질환인 Tay-Sachs병에는 임상시험 4건과 문헌이 있어 아래에 따로 정리했습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 문서가 링크로만 제공되어 적응증 본문을 확인할 수 없습니다. 약리 데이터베이스에는 고셰병 치료에 사용된다고 기재되어 있으나, 허가 문구로 확인된 내용은 아닙니다. |
| 예측 신규 적응증 | 치명적 경과의 상염색체 어린선 증후군 |
| TxGNN 예측 점수 | 0.9983 |
| 근거 수준 | L5 (모델 예측만 있음) |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 1건 (유효 1건, 단일성분) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 수집되지 않았습니다. 다만 약리 데이터에 따르면 miglustat은 글루코실세라마이드 합성효소(UGCG)를 표적으로 하며, 당지질 합성을 줄이는 기질 감소 요법에 쓰입니다.

어린선증은 표피의 세라마이드와 지질 장벽 대사 이상과 관련이 있습니다. 당지질 합성을 조절하는 약물과 연결될 가능성은 생각해 볼 수 있습니다. 그러나 이는 추측 수준입니다. 이 질환에서 글루코실세라마이드 합성 억제가 도움이 된다는 직접적인 근거는 확인되지 않았습니다.

## 임상시험 근거

현재 이 질환과 관련된 임상시험 등록이 없습니다.

## 문헌 근거

현재 이 질환과 관련된 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200902328 | 자베스카캡슐100밀리그램(미글루스타트) | 백색~미백색 분말을 함유한 상·하부 백색 경질캡슐 | 허가 문서 링크만 제공되어 본문을 확인할 수 없음 |

제조사는 (주)한국얀센이며 상태는 유효입니다.

## 안전성 고려사항

- **약물 상호작용**: Imiglucerase와의 병용이 중등도(Moderate) 수준의 상호작용으로 보고되어 있습니다(DDInter).
- 허가사항의 경고 및 금기 정보는 이번에 수집되지 않았습니다. 상세 안전성 정보는 허가사항을 참조하세요.

## 참고: 근거가 있는 다른 예측 질환 (Tay-Sachs병)

상위 10개 예측 중 근거가 확인된 질환은 Tay-Sachs병(TxGNN 점수 0.9975)뿐입니다. 나머지 질환은 모두 모델 예측만 있는 L5입니다. 여기에는 콜레스테릴 에스터 저장병, Krabbe병, 이염색성 백질이영양증 등이 포함됩니다.

Tay-Sachs병은 헥소사미니다제 A 결핍으로 GM2 강글리오사이드가 축적되는 질환입니다. Miglustat은 뇌혈관장벽을 통과하고 이 축적 물질의 합성을 줄이므로 기전상 잘 맞습니다.

**임상시험**

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 내용 |
|---------|------|------|----------|---------|
| [NCT00672022](https://clinicaltrials.gov/study/NCT00672022) | Phase 3 | 완료 | 10 | 영아형 GM2 강글리오시드증에서 약동학·안전성·내약성 평가 |
| [NCT03822013](https://clinicaltrials.gov/study/NCT03822013) | Phase 3 | 조기 종료 | 30 | 영아형 Sandhoff병·Tay-Sachs병의 신경학적·전신 증상 개선 평가 |
| [NCT00418847](https://clinicaltrials.gov/study/NCT00418847) | Phase 2 | 완료 | 5 | 소아·청소년형 GM2 강글리오시드증에서 약동학과 내약성 평가 |
| [NCT02030015](https://clinicaltrials.gov/study/NCT02030015) | Phase 4 | 조기 종료 | 16 | 케톤식이와 병용하는 Syner-G 요법 (병용 설계라 miglustat 단독 효과 판단이 어려움) |

**주요 문헌**

| PMID | 연도 | 유형 | 저널 | 내용 |
|------|-----|------|------|------|
| [19346952](https://pubmed.ncbi.nlm.nih.gov/19346952/) | 2009 | RCT | Genet Med | 후기 발병형 Tay-Sachs병에서 miglustat의 12개월 무작위 대조 연구 (결과 수치는 확인되지 않음) |
| [37209042](https://pubmed.ncbi.nlm.nih.gov/37209042/) | 2023 | 체계적 문헌고찰 | Eur J Neurol | GM2 강글리오시드증에서 miglustat의 효능과 안전성 평가 |
| [16434676](https://pubmed.ncbi.nlm.nih.gov/16434676/) | 2006 | 증례 | Neurology | 영아형 환자 2명에서 신경학적 악화를 막지 못했으나, 뇌척수액 내 약물 농도 확인 및 두개 확대 예방이 관찰됨 |
| [42794762](https://pubmed.ncbi.nlm.nih.gov/42794762/) | 2026 | Review | Int J Mol Sci | 신경병증성 리소좀 저장질환에서 miglustat의 근거와 재창출의 한계 |

데이터에서 부여된 근거 수준은 L1이지만, 완료된 Phase 3 RCT가 2건 이상이라는 기준은 충족하지 못합니다. 완료된 Phase 3 시험은 10명 규모의 약동학·안전성 시험 1건이고, 다른 Phase 3 시험은 조기 종료되었습니다. 따라서 보수적으로는 L2~L3 수준으로 보는 것이 적절합니다. 위 시험과 문헌의 실제 효능 결과는 확인되지 않았습니다. 영아형 환자에서는 위장관 부작용으로 사용이 제한된다는 보고가 있습니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 1순위 예측인 치명적 경과의 상염색체 어린선 증후군은 임상시험·문헌 근거가 전혀 없고 기전 연결도 추측 수준이어서 L5에 해당합니다.
- 허가 적응증 본문과 경고·금기 정보도 확보되지 않아 안전성 검토를 진행할 수 없습니다.

**진행하려면 필요한 것:**
- 식약처 허가사항(적응증, 경고, 금기)의 본문 확보
- DrugBank 등에서 작용 기전(MOA) 데이터 확보
- 어린선증에서 글루코실세라마이드 합성 억제의 타당성을 보여주는 전임상 근거
- 근거가 있는 Tay-Sachs병을 우선 검토하는 경우, 위 RCT·체계적 문헌고찰·종료된 Phase 3 시험의 실제 결과와 위장관 부작용·신경병증 안전성 확인
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

