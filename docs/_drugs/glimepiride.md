---
layout: default
title: Glimepiride
parent: 僅模型預測 (L5)
nav_order: 270
evidence_level: L5
indication_count: 9
---

# Glimepiride
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

以下是根據 Evidence Pack 生成的藥物再利用評估報告：

---

# Glimepiride: 제2형 당뇨병에서 Focal Stiff Limb Syndrome으로

## 한 문장 요약

Glimepiride는 췌장 β세포의 KATP 채널을 차단하여 인슐린 분泌를 촉진하는 설포닐우레아계 혈당강하제로, 제2형 당뇨병 치료에 사용됩니다.
TxGNN 모델은 **Focal Stiff Limb Syndrome(국소 경직 사지 증후군)**에 효과가 있을 수 있다고 예측하나,
현재 이를 지지하는 임상시험 및 문헌이 **전무**하며, 기전적 연결고리 또한 고도로 추론적입니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 제2형 당뇨병 (Type 2 Diabetes Mellitus) |
| 예측 신규 적응증 | Focal Stiff Limb Syndrome |
| TxGNN 예측 점수 | 99.75% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✗ 시판 안 됨 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 Evidence Pack에 상세한 작용 기전 데이터가 포함되어 있지 않습니다. 알려진 정보에 따르면, Glimepiride는 설포닐우레아계 약물로 췌장 β세포의 **ATP-감수성 칼륨(KATP) 채널**을 차단하여 인슐린 분비를 촉진하는 방식으로 제2형 당뇨병을 치료합니다. 또한 혈당 강하 외에 혈관 내피 기능 개선, 항산화 작용 등 췌장 외 효과도 보고된 바 있습니다.

Focal Stiff Limb Syndrome은 anti-amphiphysin 항체와 연관된 **자가면역성 GABAergic 신경계 질환**입니다. TxGNN의 예측 근거는 KATP 채널이 GABAergic 인터뉴런에도 발현된다는 점에서, 이론상 Glimepiride의 KATP 차단이 신경원 흥분성에 영향을 줄 수 있다는 추론에서 비롯됩니다.

그러나 이 연결고리는 **고도로 추론적**입니다. 제2형 당뇨병(췌장 내분비 기능 장애)과 Focal Stiff Limb Syndrome(중추 신경계 자가면역 질환)은 병태생리학적으로 매우 이질적이며, 직접적인 실험적·임상적 근거가 전혀 존재하지 않습니다. 동 질환의 표준 치료는 디아제팜, 바클로펜, IVIg로, 설포닐우레아계 사용 근거는 알려진 바 없습니다.

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
Glimepiride와 Focal Stiff Limb Syndrome의 연관성은 TxGNN 모델 예측에만 근거하며(L5), 이를 지지하는 임상시험, 관찰 연구, 전임상 연구가 전무합니다. 기전적 연결고리 또한 KATP 채널의 공유 발현이라는 간접적 추론에 그치며, 자가면역 신경계 질환에 대한 생물학적 타당성이 확인되지 않았습니다.

**진행하려면 필요한 것:**
- Glimepiride 공식 허가사항 내 경고·금기사항 확인 (현재 미수집)
- GABAergic 인터뉴런에서의 KATP 채널 조절 관련 전임상 연구 탐색
- Stiff person syndrome 계열 질환에 설포닐우레아계 약물의 생물학적 합리성을 검토하는 기초 연구 필요
- 한국 내 Glimepiride 허가 현황 재확인 (현재 등록 허가증 0건으로 조회됨)

---

> **⚠️ 주의**: 본 보고서는 연구 참고용이며 의료 조언을 구성하지 않습니다. 재창출 후보는 임상 검증을 거쳐야 합니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

