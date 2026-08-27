---
layout: default
title: Calcipotriol
parent: 僅模型預測 (L5)
nav_order: 162
evidence_level: L5
indication_count: 10
---

# Calcipotriol
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

# Calcipotriol: 원 적응증 미상에서 지루각화증(Seborrheic Keratosis)으로

## 한 문장 요약

Calcipotriol(DrugBank ID: DB02300)은 이번 Evidence Pack에 기존 승인 적응증 및 작용기전(MOA) 정보가 확보되어 있지 않은 약물입니다.
TxGNN 모델은 **지루각화증(Seborrheic Keratosis)**에 효과가 있을 수 있다고 예측하며(예측 점수 99.96%), 현재 이를 뒷받침하는 **임상시험이나 문헌은 전혀 없는** 순수 모델 예측 단계입니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (허가 이력·MOA 정보 미확보) |
| 예측 신규 적응증 | 지루각화증 (Seborrheic Keratosis) |
| TxGNN 예측 점수 | 99.96% (전체 순위 1337위) |
| 근거 수준 | L5 (모델 예측만 존재, 임상시험·문헌 없음) |
| 한국 시판 현황 | ✗ 미상영 (미출시) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용기전(MOA) 데이터가 없습니다. Evidence Pack에 포함된 예측 근거(repurposing rationale)에 따르면, 지루각화증은 표피 각질세포가 과도하게 증식하는 양성 병변이며, Calcipotriol이 비타민 D 수용체(VDR) 활성화를 통해 각질세포의 증식·분화를 조절하는 기전과 개념적으로 연결됩니다. 이 근거 자료는 이러한 기전이 건선(psoriasis)의 핵심 병리기전과 유사하다는 점을 근거로 들고 있으나, Calcipotriol이 건선 치료에 실제로 승인된 약물인지는 이번 Evidence Pack에서 확인되지 않았습니다.

다만 이 연관성은 어디까지나 기전 유추 수준이며, 이를 뒷받침하는 실제 임상시험이나 문헌은 전혀 없습니다. 또한 Calcipotriol은 외용 제형으로 알려져 있어, 실제 검증을 위해서는 국소 투여 시 병변 부위에 대한 적용 가능성 확인이 선행되어야 합니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 관련 문헌이 없습니다.

---

## 추가 예측 적응증 후보 (Rank 2–10)

이번 Evidence Pack(candidate_id: TW-DB02300-multi)은 단일 적응증이 아닌 여러 후보를 함께 담고 있어, 참고용으로 나머지 순위도 함께 제시합니다. **모든 후보가 임상시험·문헌 근거 없이 TxGNN 예측 점수만 존재하는 L5 단계**입니다.

| 순위 | 예측 적응증 | TxGNN 점수 | 권장 상태 | 비고 |
|------|------------|-----------|----------|------|
| 2 | 외음부 함입성 모낭성 각화증 (Vulvar Inverted Follicular Keratosis) | 99.94% | Research Question | 각질세포 분화 기전과 간접 연관, 근거 매우 제한적 |
| 3 | 외음질염 (Vulvovaginitis) | 99.74% | Hold | 감염·염증성 질환으로 약리기전 연결 약함 |
| 4 | 외음염 (Vulvitis) | 99.58% | Hold | 항염 기전 근거 없음 |
| 5 | 외음부 종양 (Vulvar Neoplasm) | 99.51% | Research Question | 비타민 D 유사체의 항증식 작용 이론 존재하나 실증 부족 |
| 6 | 외음부 궤양 (Ulceration of Vulva) | 99.50% | Hold | 상처 치유 촉진 근거 없음 |
| 7 | 외음부 편평상피종양 (Vulvar Squamous Neoplasm) | 99.43% | Research Question | VDR 경로와 상대적으로 직접적 연관 가능성 |
| 8 | 폐경 후 위축성 질염 (Postmenopausal Atrophic Vaginitis) | 99.37% | Hold | 표준 치료(에스트로겐)와 기전 불일치 |
| 9 | 골 파젯병 (Bone Paget Disease) | 99.20% | Hold | **주의**: Calcipotriol은 전신 칼슘대사 작용을 의도적으로 낮춘 약물로, 이 예측은 기전상 상충되는 잠재적 위양성(false positive)으로 판단됨 |
| 10 | 유방 섬유낭성 질환 (Breast Fibrocystic Disease) | 99.02% | Hold | 호르몬 기전 중심 질환으로 연관성 간접적 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

다만 본 Evidence Pack에는 **Blocking 등급 데이터 갭(DG001: TFDA 첨부문서 경고·금기사항 미확보)**이 존재하여, 안전성 초기평가(S1) 단계 자체에 진입할 수 없는 상태임을 유의해야 합니다. 약물 상호작용(DDI) 조회 결과도 "not_found"로, 확인된 상호작용 데이터가 없습니다.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
전체 예측 후보가 모두 근거 수준 L5(모델 예측만 존재, 임상시험·문헌 전무)이며, 작용기전(MOA)과 규제 안전성 정보(TFDA 경고/금기)가 Blocking 등급 데이터 갭으로 남아 있어 안전성 초기평가조차 진행할 수 없습니다. 또한 이 약물은 한국 내 시판 이력이 확인되지 않아 규제적 판단 근거도 부족합니다.

**진행하려면 필요한 것:**
- TFDA(또는 현지 규제기관) 공식 첨부문서 확보를 통한 경고·금기사항 해소 (Blocking, DG001)
- DrugBank API 등을 통한 상세 작용기전(MOA) 확보 (High, DG002)
- 1순위 후보(지루각화증)에 대한 전임상·임상 문헌 탐색 확대
- 골 파젯병 후보는 기전상 상충 가능성이 있어 별도 재검토 없이 후속 조사에서 제외 권장
- 국내(한국) 시판·허가 현황 재확인
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

