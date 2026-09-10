---
layout: default
title: Polyethylene Glycol 400
parent: 僅模型預測 (L5)
nav_order: 562
evidence_level: L5
indication_count: 2
---

# Polyethylene Glycol 400
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Polyethylene Glycol 400: 적응증 없음(의약품 부형제)에서 기관지염으로(예측, 근거 미흡)

## 한 문장 요약

Polyethylene Glycol 400(PEG 400)은 자체 치료 적응증이 없는 의약품 부형제/용매이며, 한국에서 아직 시판되지 않았습니다. TxGNN 모델은 **기관지염(Bronchitis)**에 효과가 있을 수 있다고 예측했으나, 근거로 제시된 임상시험 5건을 검토한 결과 실제로는 전혀 다른 약물(Mircera, methoxy PEG-epoetin beta)에 대한 연구로 확인되어 **이 예측은 신뢰할 수 없는 명칭 혼동(false positive)**으로 판단됩니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 없음 (의약품 부형제/용매, 자체 적응증 미보유) |
| 예측 신규 적응증 | 기관지염 (Bronchitis) |
| TxGNN 예측 점수 | 99.58% |
| 근거 수준 | L5 (모델 예측만 있음, 실제 연구 없음) |
| 한국 시판 현황 | 미상시 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. PEG 400은 알려진 약리 활성이 없는 의약품 부형제/용매로, 발염·감염성 호흡기 질환인 기관지염을 치료할 기전적 근거가 존재하지 않습니다.

제시된 5건의 임상시험을 상세히 검토한 결과, 실제 연구 대상 약물은 **Mircera(methoxy polyethylene glycol-epoetin beta)**로, PEG 400과는 완전히 다른 약물 실체입니다. Mircera는 만성 신장질환 환자의 빈혈 교정을 위한 PEG화 적혈구생성인자(EPO)이며, 적응증 역시 기관지염과 무관합니다. 즉 이 예측은 약물명에 "polyethylene glycol" 문자열이 공통으로 포함되어 TxGNN 지식그래프에서 **명칭 혼동형 오탐(false positive)**이 발생한 사례로 판단됩니다. 실질적인 기전적 연관성은 확인되지 않습니다.

## 임상시험 근거

⚠️ **주의**: 아래 임상시험은 TxGNN이 근거로 제시했으나, 실제 연구 약물은 PEG 400이 아닌 Mircera(methoxy PEG-epoetin beta)이며 적응증도 만성 신장질환 빈혈로, 기관지염과 무관합니다. 참고용으로만 제시합니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 | 관련성 |
|---------|------|------|----------|---------|-------|
| [NCT00559273](https://clinicaltrials.gov/study/NCT00559273) | Phase 3 | 완료 | 307 | 투석 미실시 만성신장질환 환자에서 Mircera vs darbepoetin alfa 빈혈 교정 비교 | 낮음 (약물·적응증 불일치) |
| [NCT01309295](https://clinicaltrials.gov/study/NCT01309295) | N/A | 완료 | 250 | 투석 전·투석 중 CKD 환자에서 Mircera 실사용 안전성·유효성 관찰연구 | 낮음 (약물·적응증 불일치) |
| [NCT01519947](https://clinicaltrials.gov/study/NCT01519947) | Phase 4 | 완료 | 87 | 고도가 Mircera 용량 요구량에 미치는 영향 평가 | 낮음 (약물·적응증 불일치) |
| [NCT01379963](https://clinicaltrials.gov/study/NCT01379963) | N/A | 완료 | 780 | Mircera 치료 신성빈혈 환자의 6개월 후향적 혈색소 수치 보고 | 낮음 (약물·적응증 불일치) |
| [NCT01422824](https://clinicaltrials.gov/study/NCT01422824) | N/A | 완료 | 185 | 혈액투석 유지 ESA 치료 환자에서 Mircera 안전성·유효성 관찰연구 (STABILE) | 낮음 (약물·적응증 불일치) |

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

PEG 400은 현재 한국에서 시판되지 않아(미상시) 허가 정보가 없습니다.

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
근거 수준이 L5(모델 예측만 존재, 실제 연구 없음)이며, 제시된 임상시험 5건은 검토 결과 PEG 400이 아닌 별개 약물(Mircera)에 대한 연구로 확인되어 이 예측을 뒷받침할 실질적 근거가 없습니다. PEG 400 자체는 약리 활성이 없는 부형제로 기전적 타당성도 부족합니다.

**진행하려면 필요한 것:**
- PEG 400 고유의 작용 기전(MOA) 데이터 확보
- 한국 허가 및 안전성(경고·금기·DDI) 정보 확보
- 기관지염과 관련된 실제 PEG 400 대상 전임상/임상 근거 확인
- TxGNN 지식그래프의 약물명 명칭 혼동(entity disambiguation) 오류 재검토 및 재예측

---

### 부가 예측 후보 (참고)

TxGNN은 2순위로 **선천성 어린선양 홍피증(Congenital Ichthyosiform Erythroderma)**도 예측했습니다(점수 99.10%, 근거 수준 L5). 관련 임상시험·문헌은 없으며, PEG 400의 친수성 부형제 특성이 피부 보습에 도움이 될 수 있다는 추론적 연결에 불과합니다. 미상시 약물이며 근거가 전혀 없어 **Hold** 권고이며 별도 조사가 필요합니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

