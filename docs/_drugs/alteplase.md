---
layout: default
title: Alteplase
parent: 僅模型預測 (L5)
nav_order: 47
evidence_level: L5
indication_count: 9
---

# Alteplase
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Alteplase: 급성 혈전 용해에서 후하벽 심근경색으로

## 한 문장 요약

Alteplase는 피브린 특이적 조직 플라스미노겐 활성제(tissue-type plasminogen activator, tPA)로, 급성 허혈성 뇌졸중·폐색전증 등 혈전색전성 질환의 치료에 전 세계적으로 사용되는 섬유소용해제입니다.
TxGNN 모델은 총 9가지 신규 적응증을 예측하였으며, 1순위로 **후하벽 심근경색(Posteroinferior Myocardial Infarction)**을 제시하고 있습니다.
1순위 적응증에 대한 현재 직접 근거는 **임상시험 0건**, **문헌 1편** 수준에 그치며, 중격 심근경색(rank 3) 및 혈전증(rank 8)에서는 보다 강한 L2 수준의 근거도 함께 확인됩니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 미허가 (현지 허가 데이터 없음) |
| 예측 신규 적응증 (1순위) | 후하벽 심근경색 (Posteroinferior Myocardial Infarction) |
| TxGNN 예측 점수 | 99.79% |
| 근거 수준 | L4 |
| 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Research Question |

---

## 9개 예측 적응증 전체 요약

| 순위 | 적응증 | TxGNN 점수 | 근거 수준 | 임상시험 | 문헌 | 권장 결정 |
|-----|--------|-----------|---------|---------|------|---------|
| 1 | 후하벽 심근경색 | 99.79% | L4 | 0건 | 1편 | Research Question |
| 2 | 후외측 심근경색 | 99.79% | L4 | 0건 | 3편 | Research Question |
| 3 | 중격 심근경색 | 99.77% | L2 | 1건 | 13편 | **Proceed with Guardrails** |
| 4 | 헤파린 보조인자 2 결핍증 | 99.72% | L4 | 0건 | 20편 | Hold |
| 5 | 선천성 관상동맥 기형 | 99.64% | L4 | 4건 | 5편 | Research Question |
| 6 | Factor V 과잉 자발혈전증 | 99.56% | L5 | 0건 | 0편 | Hold |
| 7 | 항트롬빈 결핍증 Type 2 | 99.56% | L5 | 0건 | 0편 | Hold |
| 8 | 혈전증 (Thrombophilia) | 99.43% | L2 | 9건 | 20편 | **Proceed with Guardrails** |
| 9 | 관상동맥 협착 | 99.14% | L3 | 7건 | 20편 | **Proceed with Guardrails** |

---

## 이 예측이 타당한 이유는?

Alteplase는 세린 프로테아제 계열의 재조합 당단백질로, 피브린(fibrin)에 선택적으로 결합한 후 플라스미노겐(plasminogen)을 플라스민(plasmin)으로 활성화하여 혈전의 피브린 기질을 직접 분해합니다. 이 피브린 특이적 섬유소용해 기전은 혈전성 혈관 폐색의 직접적 치료 표적에 작용하며, 급성 심근경색에서의 관상동맥 재개통 효과는 TAMI·GUSTO 등 대규모 시험을 통해 이미 확립된 바 있습니다.

후하벽 심근경색은 주로 우관상동맥(RCA) 또는 좌회선지(LCx)의 혈전성 폐색에 의해 발생합니다. 관상동맥 혈전이 원인인 경우 alteplase의 섬유소용해 기전이 이론적으로 적용 가능하며, 일반 급성 MI에서의 효능과 같은 기전적 연속선상에 있습니다. 다만 이 특정 해부학적 MI 아형을 직접 대상으로 설계된 임상시험은 현재까지 확인되지 않습니다.

현재 확인된 유일한 관련 문헌(PMID 16294818)은 alteplase 혈전용해 치료 **실패 후** 시행된 구조적 PTCA(Rescue PTCA)의 결과를 보고한 회고적 연구로, alteplase의 직접적 치료 효과를 평가한 자료가 아닌 간접 증거에 해당합니다. 후하벽 MI 아형에서 alteplase의 치료적 역할을 규명하기 위해서는 이 아형의 하위그룹 분석을 포함한 전향적 연구 설계가 필요합니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [16294818](https://pubmed.ncbi.nlm.nih.gov/16294818/) | 2005 | 회고적 임상연구 | Archivos de cardiologia de Mexico | 급성 심근경색 환자에서 혈전용해 치료(alteplase 포함) 실패 후 시행된 구조적 PTCA의 단기 임상·혈관조영 결과 기술 — alteplase 직접 치료 효과가 아닌 간접 근거 |

---

## 시판 정보

현재 허가된 시판 제품 없음 (미시판 상태, 허가증 0건).

---

## 안전성 고려사항

> 안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Research Question**

**사유:**
후하벽 심근경색 아형에 대한 alteplase의 직접적 임상 근거가 부재하며, 현재 유일한 관련 문헌은 alteplase 실패 사례를 다룬 간접 증거입니다. 기전적 타당성은 충분하나 이 특정 MI 아형을 대상으로 한 임상 데이터가 없어 L4 근거 수준에 해당합니다.

**진행하려면 필요한 것:**
- 후하벽 심근경색 환자를 포함한 전향적 임상시험 또는 기존 대규모 MI 시험의 하위그룹 분석 설계
- 작용 기전(MOA) 데이터 확보 (DrugBank API 조회 권고 — DG002)
- 허가사항 PDF 파싱을 통한 경고·금기 안전성 정보 확보 (TFDA 또는 현지 허가기관 — DG001)
- 9개 예측 적응증 중 L2 수준 근거를 보유한 **중격 심근경색(rank 3, TAMI-1 RCT 포함)** 및 **혈전증(rank 8, Phase 2 alteplase 직접 투여 시험 포함)**을 우선 임상 개발 대상으로 검토
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

