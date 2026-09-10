---
layout: default
title: Cerliponase Alfa
parent: 僅模型預測 (L5)
nav_order: 192
evidence_level: L5
indication_count: 10
---

# Cerliponase Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Cerliponase Alfa: CLN2 질환(TPP1 결핍증)에서 Scheie 증후군으로

## 한 문장 요약

Cerliponase alfa는 재조합 인체 TPP1(tripeptidyl peptidase 1) 효소대체요법제로, 뇌실내 투여를 통해 TPP1 효소가 결핍된 신경세포 밀랍유사지방갈색소증 2형(CLN2 질환) 환자를 치료하는 데 사용됩니다. TxGNN 모델은 **Scheie 증후군**에 효과가 있을 수 있다고 예측했으나(예측 점수 **99.98%**), 이를 뒷받침하는 임상시험이나 문헌은 **한 건도 없으며**, 자체 기전 분석에서도 두 질환의 원인 효소가 서로 다르다는 점이 확인되어 예측의 신뢰도는 낮습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | CLN2 질환 (TPP1 결핍증) — *허가증 데이터 없음, 근거자료 내 기전 설명에서만 확인* |
| 예측 신규 적응증 | Scheie 증후군 (Scheie syndrome) |
| TxGNN 예측 점수 | 99.98% |
| 근거 수준 | L5 (모델 예측만 존재, 실증 연구 없음) |
| 한국 시판 현황 | 미판매 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터는 확보되지 않았습니다([Data Gap]). 다만 근거자료의 기전 분석에 따르면, cerliponase alfa는 CLN2 질환 환자에게 결핍된 TPP1 효소를 보충하는 효소대체요법제이며, 뇌실내 투여라는 매우 특이적인 경로로 사용됩니다.

반면 Scheie 증후군은 MPS I(황산피부소증 1형)에 속하며, 원인 효소는 alpha-L-iduronidase로 TPP1과는 전혀 다른 효소입니다. 효소대체요법은 기질-효소 특이성이 매우 높기 때문에, 두 질환 사이에 기전상 교차 적용될 근거가 없습니다. 근거자료는 이 높은 예측 점수가 지식그래프 상 "lysosomal storage disease(리소좀 축적 질환)" 노드들이 서로 인접해 있는 데서 비롯된 군집 효과일 가능성이 크다고 명시하고 있습니다.

참고로 상위 10개 예측 적응증을 전체적으로 살펴보면, Gaucher 병(순위 5)을 제외한 9건 모두 임상시험·문헌이 전무하며(L5), Gaucher 병 관련 문헌 1건조차 cerliponase alfa의 실제 치료 효능을 다룬 것이 아니라 리소좀 축적 질환의 자연경과 모델링 리뷰 논문(PMID 41527340)입니다. 즉 이 예측 목록 전반이 "리소좀 축적 질환"이라는 상위 범주에서의 그래프 근접성에 기인할 가능성이 높습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

현재 한국에 허가된 Cerliponase alfa 제품이 없습니다 (미판매, 허가증 0건).

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. (한국 규제기관의 경고/금기 정보는 아직 확보되지 않았으며, 이는 안전성 초기 평가 진입을 막는 주요 데이터 공백[DG001, Blocking]입니다.)

## 결론 및 다음 단계

**결정: Hold**

**사유:**
Scheie 증후군에 대한 임상시험이나 문헌이 전혀 없고(L5), 자체 기전 분석에서도 원인 효소가 서로 달라(TPP1 vs. alpha-L-iduronidase) 기전상 타당성이 낮은 것으로 나타났습니다. 예측 점수가 높은 것은 실제 생물학적 연관성보다 지식그래프의 질환 범주 인접 효과에서 기인했을 가능성이 큽니다.

**진행하려면 필요한 것:**
- 한국 규제기관의 허가사항(경고/금기) 자료 확보 — 현재 S1 안전성 초기 평가 진입이 차단된 상태 (DG001)
- Cerliponase alfa의 상세 작용기전(MOA) 데이터 (DG002)
- Scheie 증후군을 포함한 MPS I에서 TPP1 관련 대체/보조 경로가 존재하는지에 대한 전임상 근거
- 지식그래프 노드 정의 재검토 (특히 순위 7 "Wolman disease with hypolipoproteinemia and acanthocytosis"와 같이 표준 명명법과 다른 복합 노드의 정확성 확인)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

