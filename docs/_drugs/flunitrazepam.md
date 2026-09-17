---
layout: default
title: Flunitrazepam
parent: 모델 예측만 (L5)
nav_order: 329
evidence_level: L5
indication_count: 10
---

# Flunitrazepam
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

# Flunitrazepam: 국내 미허가 약물에서 불면증으로

## 한 문장 요약

Flunitrazepam은 벤조디아제핀계 약물로 국제적으로는 진정·수면 목적으로 사용되어 왔으나, 현재 **한국에는 허가된 제품이 없습니다** (미출시, 허가증 0건). TxGNN 모델은 **불면증(Insomnia)**에 효과가 있을 것으로 예측하며(예측 점수 99.89%), 1건의 관찰 코호트 임상시험과 11편의 문헌이 이 방향을 뒷받침합니다. 다만 RCT 근거가 없고 국내 허가사항(경고·금기) 자료가 확보되지 않아, 진행 전 반드시 보완이 필요합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 국내 허가 자료 없음 (해외에서는 벤조디아제핀계 진정수면제로 사용된 이력) |
| 예측 신규 적응증 | 불면증 (Insomnia) |
| TxGNN 예측 점수 | 99.89% |
| 근거 수준 | L3 (관찰 코호트 연구 + 다수 리뷰, RCT 없음) |
| 한국 시판 현황 | ✗ 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

Flunitrazepam은 전형적인 1,4-benzodiazepine 계열 약물로, GABA-A 수용체의 chloride channel을 양성 변구조 조절(positive allosteric modulation)하여 진정·수면 효과를 나타냅니다. 이는 벤조디아제핀 계열 약물군에서 이미 확립된 약리 기전이며, 원본 MOA 데이터는 [Data Gap]이지만 화학적 분류만으로도 기전 추정이 가능합니다.

다만 주의할 점은, TxGNN이 예측한 "불면증"이라는 신규 적응증은 사실 flunitrazepam이 해외에서 **이미 오랫동안 사용되어 온 전통적 용도**와 사실상 동일합니다. 즉 이번 예측은 새로운 기전적 발견이라기보다, "국내 미허가 상태에서 이미 검증된 해외 적응증을 국내에 도입할 수 있는가"라는 규제·시장 진입 질문에 가깝습니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT02648776](https://clinicaltrials.gov/study/NCT02648776) | N/A (관찰연구) | 불명(UNKNOWN) | 1,400 | 대만 학술의료센터에서 노인 대상 수면제(hypnotics) 처방 패턴, 질환 상태와의 연관성, 효능·안전성, 약동학/약유전학적 특성을 조사한 전향적 코호트 연구. Flunitrazepam을 포함한 수면제 전반을 다룸(비개입적 관찰연구, RCT 아님). |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [40195](https://pubmed.ncbi.nlm.nih.gov/40195/) | 1979 | 임상연구 | La Nouvelle presse medicale | Flunitrazepam이 기질적·기능적 수면장애에 미치는 작용을 다룬 연구(프랑스어 원문, 초록 미제공). |
| [430730](https://pubmed.ncbi.nlm.nih.gov/430730/) | 1979 | 임상관찰 | JAMA | Diazepam, flunitrazepam 등 5개 벤조디아제핀의 수면실험실 연구. 단기·야간 단회 투여 후 금단 시 반동성 불면(rebound insomnia) 발생을 보고. |
| [684426](https://pubmed.ncbi.nlm.nih.gov/684426/) | 1978 | 임상관찰 | Science | 3개 벤조디아제핀 수면제의 금단 후 반동성 불면 증후군을 최초로 기술. |
| [8519370](https://pubmed.ncbi.nlm.nih.gov/8519370/) | 1993 | 비교약리 연구 | European Respiratory Journal | 중증 COPD 환자에서 zolpidem, triazolam, flunitrazepam 1mg 단회 투여 시 동맥혈가스 및 호흡 조절에 미치는 급성 영향 비교. |
| [2883822](https://pubmed.ncbi.nlm.nih.gov/2883822/) | 1986 | Review | Acta Psychiatrica Scandinavica Suppl. | 노화에 따른 벤조디아제핀(flunitrazepam 포함) 약동학 변화 리뷰. 고령자에서 반응 증가 소견. |
| [2883820](https://pubmed.ncbi.nlm.nih.gov/2883820/) | 1986 | Review | Acta Psychiatrica Scandinavica Suppl. | 불면증 유형별 최적 수면제 특성과 다양한 벤조디아제핀의 임상적 사용 필요성을 논의. |
| [20171127](https://pubmed.ncbi.nlm.nih.gov/20171127/) | 2010 | 임상연구 | Sleep Medicine Reviews | 수면제가 신체 균형·기립 안정성에 미치는 영향, 낙상·고관절 골절 위험 증가 보고. |
| [14722706](https://pubmed.ncbi.nlm.nih.gov/14722706/) | 2004 | 동물연구 | Psychopharmacology | 수면장애 유발 흰쥐 모델에서 3종 수면제의 수면-각성 주기 영향 비교. |
| [6114852](https://pubmed.ncbi.nlm.nih.gov/6114852/) | 1981 | Review | Drugs | Triazolam 리뷰(주 대상 약물은 아니나 flunitrazepam 등 장기작용 수면제와 비교 언급). |

---

## 한국 시판 정보

현재 한국에는 Flunitrazepam의 허가 정보가 없습니다 (미출시, 허가증 0건).

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

> 참고: 본 Evidence Pack에서 key_warnings, contraindications, DDI 모두 자료 확보에 실패했습니다(DG001, Blocking 등급 — 안전성 초기 평가(S1) 진입 불가). 또한 다른 예측 적응증(불안장애 등) 근거 문헌 중 다수가 flunitrazepam의 오남용, 데이트 강간 약물(date rape drug)로서의 이력, 의존성/금단 반동 불면을 반복적으로 보고하고 있어, 후속 검토 시 규제·안전 관리 측면에서 별도로 고려할 필요가 있습니다.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
관찰 코호트 연구 1건과 다수의 국제 문헌(반동성 불면, 노인 약동학, 호흡 영향 등)이 flunitrazepam의 수면 관련 약리 효과를 일관되게 뒷받침하지만, RCT 근거가 없고(L3) 국내 허가사항·경고·금기 정보가 전무하여 안전성 초기 평가(S1)조차 진입할 수 없는 상태입니다.

**진행하려면 필요한 것:**
- TFDA(또는 국내 식약처) 허가사항 원문 확보 및 경고·금기 파싱 (DG001, Blocking — 최우선)
- DrugBank API를 통한 상세 작용기전(MOA) 확보 (DG002, High)
- 오남용·의존성·데이트 강간 약물 이력에 대한 위험관리계획(RMP) 검토
- 국내 도입 시 마약류/향정신성의약품 관리 규정 부합 여부 확인
- 불면증 적응증에 대한 RCT 수준 근거 추가 확보 또는 국내 임상시험 설계 검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

