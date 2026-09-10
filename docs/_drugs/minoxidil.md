---
layout: default
title: Minoxidil
parent: 僅模型預測 (L5)
nav_order: 482
evidence_level: L5
indication_count: 10
---

# Minoxidil
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

# Minoxidil: 중증 고혈압 치료제에서 유전성 두피 단순 저모증(Hypotrichosis Simplex)으로

## 한 문장 요약

Minoxidil은 본래 다른 항고혈압제에 반응하지 않는 중증(난치성) 고혈압 환자를 위한 경구 혈관확장제로 사용되어 온 약물입니다. TxGNN 모델은 **유전성 두피 단순 저모증(Hypotrichosis Simplex of the Scalp)**에 효과가 있을 수 있다고 예측하며, 현재 등록된 관련 임상시험은 없고 **3건의 사례보고(case report) 수준 문헌**만이 이 방향을 뒷받침합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 중증(난치성) 고혈압 — 경구 혈관확장제 (한국 허가 정보 없음) |
| 예측 신규 적응증 | 유전성 두피 단순 저모증 (Hypotrichosis Simplex of the Scalp) |
| TxGNN 예측 점수 | 99.9999% (모델 내 전체 순위 7위) |
| 근거 수준 | L3 |
| 한국 시판 현황 | 미허가 (미출시) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 이 약물에 대한 상세 작용기전(MOA) 데이터는 확보되지 않았습니다(Blocking data gap). 다만 근거 팩에 포함된 다른 관련 문헌들을 종합하면, minoxidil은 ATP 민감성 칼륨(K+) 통로 개방제로서 모낭 주변 소동맥을 확장시켜 국소 혈류를 늘리고, 모발 성장기(anagen phase)를 연장하며 VEGF를 상향조절하는 것으로 알려져 있습니다. 이 기전은 남성형 탈모(androgenetic alopecia) 치료에서 이미 확립되어 있습니다.

유전성 두피 단순 저모증은 CDSN 유전자(데스모솜 단백질 corneodesmosin) 변이로 발생하는 희귀 단일유전자 질환으로, 남성형 탈모와는 발병 기전이 다릅니다. 다만 두 질환 모두 모낭 생장주기 이상이라는 공통점이 있어, minoxidil의 anagen기 연장 작용이 이론적으로 확장 적용될 수 있다는 것이 근거 팩의 기전 추론(repurposing rationale)입니다. 그러나 이는 어디까지나 이론적 유추이며, 실제로는 개인 사례보고 3건 외에 체계적 임상 검증이 이루어진 바 없습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [35761391](https://pubmed.ncbi.nlm.nih.gov/35761391/) | 2022 | Case Report | Dermatologic therapy | 유전성 두피 단순 저모증 환자에서 경구 minoxidil과 성장인자 병용 치료 사례 |
| [39902296](https://pubmed.ncbi.nlm.nih.gov/39902296/) | 2024 | Case Series | Frontiers in genetics | CDSN 유전자 변이로 진단된 8세 남아 가족성 HSS 사례, 식물추출물+minoxidil 병용요법 보고 |
| [36651821](https://pubmed.ncbi.nlm.nih.gov/36651821/) | 2023 | Case Report | The Journal of dermatological treatment | 14세 환자, 혈소판 풍부 혈장(PRP) 주사와 국소 minoxidil 2% 병용으로 성공적 치료 |

## 한국 시판 정보

한국 내 허가 정보가 없습니다 (허가증 0건, 미출시).

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. (TFDA 수준의 경고/금기 정보는 아직 수집되지 않았습니다.)

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 신규 적응증인 유전성 두피 단순 저모증은 매우 희귀한 단일유전자 질환으로, 관련 임상시험이 전혀 등록되어 있지 않고 근거 수준이 사례보고 3건(L3)에 불과해 재창출 논의를 진전시키기에는 이릅니다. 또한 한국 내 허가 이력이 없고 안전성 경고·금기 정보(Blocking gap)도 확보되지 않아, 안전성 초기 평가(S1) 단계조차 완료되지 않은 상태입니다.

**진행하려면 필요한 것:**
- TFDA(또는 식약처) 공식 허가사항의 경고/금기 정보 확보 (Blocking data gap, DG001)
- DrugBank 등을 통한 상세 작용기전(MOA) 데이터 확보 (DG002)
- 유전성 두피 단순 저모증에 특화된 전임상 또는 소규모 임상 연구 설계
- (참고) 동일 근거 팩 내 "alopecia(일반/남성형 탈모)" 적응증은 완료된 Phase 3 RCT를 포함한 L1 수준 근거로 이미 "Proceed with Guardrails" 권고를 받고 있어, 재창출 우선순위를 이쪽과 비교 검토할 필요가 있습니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

