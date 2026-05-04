---
layout: default
title: Salicylic Acid
parent: 僅模型預測 (L5)
nav_order: 303
evidence_level: L5
indication_count: 10
---

# Salicylic Acid
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

# Salicylic acid: 각질용해제에서 유두상 결막염으로

## 한 문장 요약

Salicylic acid는 각질용해(keratolytic) 및 항염 특성으로 피부과 영역(여드름, 건선, 각화증 등)에서 오랫동안 사용되어 온 유기산이나, 이번 데이터 패키지에는 공식 허가 적응증 기록이 존재하지 않습니다.
TxGNN 모델은 **유두상 결막염(Papillary Conjunctivitis)**에 효과가 있을 수 있다고 예측하나,
현재 **임상시험 0건**·**문헌 0편**으로 근거가 전무하며 모델 예측만 존재하는 상태입니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 정보 없음 (미시판) |
| 예측 신규 적응증 | 유두상 결막염 (Papillary Conjunctivitis) |
| TxGNN 예측 점수 | 99.88% |
| 근거 수준 | L5 |
| 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면, Salicylic acid는 COX 경로 억제를 통한 항염 작용과 각질층 단백질 결합 분해를 통한 각질용해 작용을 가진 유기산으로, 피부과 적응증에서의 효능이 오랫동안 입증되어 있습니다.

유두상 결막염(Papillary Conjunctivitis)은 과민 반응 또는 면역 매개 염증에 의해 결막에 유두 형성이 나타나는 안과 질환입니다. Salicylic acid의 COX 억제 항염 특성이 이론적으로는 결막 염증 개입 공간을 시사하지만, 실제 눈에 직접 적용 시 자극성·조직 독성 우려가 크며 기전 관련성은 매우 제한적입니다.

현재 유두상 결막염에 대한 임상 적용 기록이 전혀 없으며, 안과용 제형으로서의 안전성 및 내약성 데이터 역시 존재하지 않습니다. 이 예측은 지식 그래프 내 네트워크 근접성에 의한 결과일 가능성이 높습니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 관련 문헌이 없습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
이번 데이터 패키지에서 예측된 10개 적응증 전체가 임상시험·문헌 근거 없음(L5)이며, 대다수는 희귀 유전성 골격 발달 질환(brachydactyly, brachyolmia, pseudoachondroplasia 등)으로 Salicylic acid와의 생물학적 합리성이 결여된 모델 오탐(false positive) 가능성이 높습니다. 1순위 예측인 유두상 결막염 역시 기전 연결성이 미약하고 안과 적용 안전성 데이터가 전무합니다.

**진행하려면 필요한 것:**
- MOA 데이터 확보 (DrugBank API 조회 권장)
- 허가 적응증 및 안전성·금기 정보 확인 (허가 취득국 허가사항 PDF 분석)
- 기전 합리성이 가장 높은 **척추관절염(spondyloarthropathy)** 적응증(10순위)에 대해 NSAIDs 계열과의 기전 유사성을 중심으로 추가 탐색 검토 가능
- 안과 적용 가능성 검토 시 눈 자극성·독성에 대한 전임상 안전성 근거 확보 필수
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

