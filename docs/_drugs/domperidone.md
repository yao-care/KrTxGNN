---
layout: default
title: Domperidone
parent: 僅模型預測 (L5)
nav_order: 227
evidence_level: L5
indication_count: 1
---

# Domperidone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Domperidone: 오심·구토에서 신원성 부적절 항이뇨 증후군으로

## 한 문장 요약

Domperidone은 도파민 D2 수용체 길항제로, 원래 오심·구토 및 위장 운동 장애 치료에 사용되는 약물입니다.
TxGNN 모델은 **신원성 부적절 항이뇨 증후군(Nephrogenic Syndrome of Inappropriate Antidiuresis, NSIAD)**에 효과가 있을 수 있다고 예측하나,
현재 이를 지지하는 **임상시험 및 관련 문헌이 전무**합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 오심·구토, 위장 운동 장애 (허가 정보 미수집) |
| 예측 신규 적응증 | 신원성 부적절 항이뇨 증후군 (Nephrogenic Syndrome of Inappropriate Antidiuresis) |
| TxGNN 예측 점수 | 99.08% |
| 근거 수준 | L5 |
| 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면, Domperidone은 도파민 D2 수용체 길항제로서 위장관 운동 촉진 및 구토 중추 억제를 통해 오심·구토를 조절합니다. 혈액-뇌 장벽을 거의 통과하지 않아 중추 부작용이 적은 말초 작용 약물로 분류됩니다.

신원성 부적절 항이뇨 증후군(NSIAD)은 AVPR2(V2 수용체) 유전자의 기능 획득 돌연변이로 인해 발생하며, ADH(항이뇨호르몬) 수치가 낮거나 측정 불가임에도 부적절한 수분 저류와 저나트륨혈증이 나타나는 희귀 질환입니다. 도파민은 신장에서 나트륨 재흡수 억제 및 수분 배설 조절에 관여하는 것으로 알려져 있습니다.

그러나 Domperidone의 D2 수용체 길항 작용이 AVPR2 돌연변이 기반의 NSIAD 병태생리와 어떻게 기전적으로 연결되는지는 현재로서 불명확합니다. TxGNN 예측 점수(99.08%)는 매우 높지만, 이를 뒷받침하는 임상시험이나 문헌 근거가 전혀 확인되지 않아 해석에 신중한 접근이 필요합니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
임상시험 및 문헌 근거가 전무하고, 기전적 연관성이 불명확하며, MOA 및 안전성 핵심 데이터(경고·금기)가 수집되지 않아 재창출 타당성을 현 단계에서 판단할 수 없습니다.

**진행하려면 필요한 것:**
- 작용 기전(MOA) 데이터 수집 (DrugBank API 조회)
- 허가사항 경고 및 금기 정보 확보 (의약품 허가사항 PDF 파싱)
- NSIAD에서 도파민 신호 경로의 역할에 관한 전임상·기전 문헌 탐색
- Domperidone과 신장 수분 항상성 조절 연관성에 대한 탐색적 문헌 검색 (PubMed: domperidone + renal + water homeostasis)
- AVPR2 수용체와 도파민 D2 수용체 간 상호작용에 관한 기초연구 여부 확인
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

