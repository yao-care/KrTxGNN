---
layout: default
title: Miglustat
parent: 높은 근거 (L1-L2)
nav_order: 516
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-15
description: "Miglustat: 예측 신규 적응증 고셔병 (Gaucher disease) (근거 수준 L1). 기존 적응증: 허가 적응증 원문이 링크로만 제공되어 구체적 문구를 확인할 수 없음 (근거 문헌상 경증~중등도 제1형 고셔병)"
monitor_inn: "Miglustat"
predicted_indications: ["autosomal ichthyosis syndrome with fatal disease course", "cholesteryl ester storage disease", "Krabbe disease", "metachromatic leukodystrophy", "Wolman disease with hypolipoproteinemia and acanthocytosis", "encephalopathy due to prosaposin deficiency", "Tay-Sachs disease", "benign neoplasm of adrenal gland", "recessive X-linked ichthyosis"]
---

# Miglustat
{: .fs-9 }

근거 수준: **L1** | 예측 적응증: **10** 건
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

## Miglustat: 고셔병에서 고셔병(및 GM2 강글리오사이드증 등 인접 질환)으로
{: .text-alpha }

## 한 문장 요약

Miglustat은 한국에서 자베스카캡슐100밀리그램으로 시판 중인 경구 약물로, 글루코실세라마이드 합성효소를 억제하는 기질 감소 요법제입니다.
TxGNN 모델은 **고셔병(Gaucher disease)**에 효과가 있을 것으로 가장 높게 예측했으며, 현재 **2건의 임상시험**과 **20편의 문헌**이 이 방향을 지지합니다.
다만 고셔병은 이미 허가된 적응증과 일치하므로 엄밀한 의미의 재창출은 아니며, 실질적인 재창출 후보는 **테이-삭스병(Tay-Sachs disease)** 등 신경병증성 당스핑고지질 축적 질환입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 원문이 링크로만 제공되어 구체적 문구를 확인할 수 없음 (근거 문헌상 경증~중등도 제1형 고셔병) |
| 예측 신규 적응증 | 고셔병 (Gaucher disease) |
| TxGNN 예측 점수 | 99.88% |
| 근거 수준 | L1 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | Proceed with Guardrails |

> 참고: 예측 2~10위에는 테이-삭스병(99.75%), 크라베병, 이염성 백질이영양증 등이 포함됩니다. 이 중 테이-삭스병만 임상시험과 문헌 근거가 있으며(L1), 나머지는 모델 예측만 있는 L5 수준이라 보류(Hold)에 해당합니다.

## 이 예측이 타당한 이유는?

현재 DrugBank 기반의 상세 작용 기전 데이터는 없습니다. 다만 약리학 데이터에서 miglustat은 **UDP-글루코스 세라마이드 글루코실트랜스퍼레이스(UGCG)**를 표적으로 하는 합성 이미노당 억제제로 확인됩니다. 글루코실세라마이드 합성을 줄여, 글루코세레브로시다제 결핍으로 쌓이는 기질의 양을 낮추는 기질 감소 요법입니다.

고셔병에서는 이것이 이미 확립된 기전이므로 이번 예측은 사실상 허가 적응증을 재확인한 것입니다. 한편 테이-삭스병에서는 같은 원리로 GM2 강글리오사이드 공급을 줄일 수 있고, miglustat이 혈액뇌장벽을 통과한다는 점이 신경병증성 표현형에 의미가 있습니다. 반면 콜레스테릴 에스터 축적병, 볼만병 등 지질 기질이 다른 질환은 기전적 연관성이 약합니다.

## 임상시험 근거

**고셔병**

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00319046](https://clinicaltrials.gov/study/NCT00319046) | Phase 3 | 완료 | 42 | 안정적 제1형 성인 환자에서 효소대체요법 후 miglustat 유지요법의 장기 효능·안전성·내약성 평가 (비교군 없는 공개 연구) |
| [NCT02520934](https://clinicaltrials.gov/study/NCT02520934) | 해당 없음 | 불명 | 19 | 고셔병 IIIB형에서 miglustat과 효소대체요법 병용 평가 |

**테이-삭스병 / GM2 강글리오사이드증**

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00672022](https://clinicaltrials.gov/study/NCT00672022) | Phase 3 | 완료 | 10 | 영아형 GM2 강글리오사이드증에서 약동학·안전성·내약성 평가 (효능 평가 아님) |
| [NCT03822013](https://clinicaltrials.gov/study/NCT03822013) | Phase 3 | 조기 종료 | 30 | 영아형 샌드호프병·테이-삭스병에서 신경학적·전신 증상 개선 평가, 종료되어 효능 결론 제한적 |
| [NCT02030015](https://clinicaltrials.gov/study/NCT02030015) | Phase 4 | 조기 종료 | 16 | miglustat과 케톤 식이 병용(Syner-G), 병용 설계로 miglustat 단독 효과 분리 어려움 |
| [NCT00418847](https://clinicaltrials.gov/study/NCT00418847) | Phase 2 | 완료 | 5 | 소아·청소년형 GM2 강글리오사이드증에서 약동학 및 내약성 평가 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [19346952](https://pubmed.ncbi.nlm.nih.gov/19346952/) | 2009 | RCT | Genet Med | 후기 발병 테이-삭스병에서 miglustat의 12개월 무작위 대조 연구 및 24개월 연장 투여. 신경학적 평가변수에서 뚜렷한 임상 이득은 확인되지 않음 |
| [25812601](https://pubmed.ncbi.nlm.nih.gov/25812601/) | 2015 | 체계적 문헌고찰 | Cochrane Database Syst Rev | 고셔병에서 효소대체요법과 기질 감소 요법의 비교 평가 |
| [35815393](https://pubmed.ncbi.nlm.nih.gov/35815393/) | 2023 | 체계적 문헌고찰·메타분석 | Ann Pharmacother | 고셔병 약물 치료의 효과 평가 |
| [37209042](https://pubmed.ncbi.nlm.nih.gov/37209042/) | 2023 | 체계적 문헌고찰 | Eur J Neurol | GM2 강글리오사이드증에서 miglustat의 효능·안전성 평가 |
| [16247743](https://pubmed.ncbi.nlm.nih.gov/16247743/) | 2005 | 가이드라인 | Am J Hematol | 제1형 고셔병에서 miglustat 사용 지침 |
| [19210136](https://pubmed.ncbi.nlm.nih.gov/19210136/) | 2009 | 코호트 | Curr Med Res Opin | 제1형 고셔병에서 miglustat의 목표 지향적 치료 |
| [14609352](https://pubmed.ncbi.nlm.nih.gov/14609352/) | 2003 | 리뷰 | Drugs | 제1형 고셔병에서 간·비장 용적을 유의하게 감소시킴 |
| [42794762](https://pubmed.ncbi.nlm.nih.gov/42794762/) | 2026 | 리뷰 | Int J Mol Sci | 신경병증성 리소좀 축적 질환에서 miglustat의 생물학적 근거, 임상 근거, 재창출의 한계 |
| [16434676](https://pubmed.ncbi.nlm.nih.gov/16434676/) | 2006 | 증례 | Neurology | 영아형 테이-삭스병 2례에서 신경학적 악화를 막지 못했으나 뇌척수액 내 약물 농도 확인 및 대두증 예방 관찰 |
| [21779792](https://pubmed.ncbi.nlm.nih.gov/21779792/) | 2011 | 리뷰 | J Inherit Metab Dis | miglustat 치료 환자의 위장관 장애와 관리 방법 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200902328 | 자베스카캡슐100밀리그램(미글루스타트) | 경질캡슐 (백색~미백색 분말 함유) | 허가 적응증 원문이 링크로만 제공되어 요약 불가 (제조사: 한국얀센) |

## 안전성 고려사항

- **약물 상호작용**: 총 2건이 확인되었습니다.
  - Imiglucerase: 중등도(Moderate) 수준의 상호작용 (효소대체요법 병용 시 유의)
  - UDP-글루코스 세라마이드 글루코실트랜스퍼레이스(UGCG): 약리학적 표적 정보이며, 임상적 약물 상호작용이 아닌 작용 표적 관계
- **주요 모니터링 항목** (근거 문헌 기반): 진전, 위장관 증상(설사, 복부 팽만 등), 체중 감소, 말초신경병증

허가사항의 경고 및 금기 정보는 이번 데이터에 포함되지 않았으므로 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
고셔병은 이미 허가된 적응증으로 Phase 3 완료 시험과 다수의 체계적 문헌고찰이 있으나, 재창출의 새로운 가치는 제한적입니다. 테이-삭스병은 Phase 3 시험과 RCT가 있지만 후기 발병형 RCT에서 임상 이득이 불분명하고 영아형 시험은 소규모이거나 조기 종료되어 효능이 확립되지 않았으므로 연구 또는 동정적 사용 범위로 제한해야 합니다. 그 외 예측 질환(크라베병, 이염성 백질이영양증, 부신 양성 종양 등)은 모델 예측만 있어 보류가 적절합니다.

**진행하려면 필요한 것:**
- 허가 적응증 원문과 경고·금기 정보 확보 (식약처 허가사항 PDF 확인)
- 상세 작용 기전 데이터 보완 (DrugBank 등)
- 테이-삭스병에 대한 신경학적 효능을 입증할 대규모 대조 임상시험
- 진전, 위장관 증상, 체중, 말초신경병증을 포함한 안전성 모니터링 계획
- 효소대체요법 병용 시 상호작용 관리 방안
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

