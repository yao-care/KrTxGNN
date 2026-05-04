---
layout: default
title: Ethosuximide
parent: 僅模型預測 (L5)
nav_order: 256
evidence_level: L5
indication_count: 1
---

# Ethosuximide
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

# Ethosuximide: 결신발작에서 신성 부적절 항이뇨 증후군으로

## 한 문장 요약

Ethosuximide는 T형 칼슘 채널을 차단하는 항경련제로, 전통적으로 결신발작(absence seizure) 치료에 사용되어 왔습니다.
TxGNN 모델은 **신성 부적절 항이뇨 증후군(Nephrogenic Syndrome of Inappropriate Antidiuresis, NSIAD)**에 효과가 있을 수 있다고 예측하며,
현재 이 방향을 지지하는 **임상시험 및 문헌은 없습니다**.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 결신발작 (Absence Seizure / Petit Mal Epilepsy) |
| 예측 신규 적응증 | 신성 부적절 항이뇨 증후군 (Nephrogenic Syndrome of Inappropriate Antidiuresis) |
| TxGNN 예측 점수 | 99.91% |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터가 제공되지 않았습니다. 알려진 정보에 따르면, Ethosuximide는 T형 전압 의존성 칼슘 채널(Cav3.x)을 차단하는 항경련제로, 시상(thalamus)의 비정상적 리듬 발화를 억제하여 결신발작을 조절합니다.

TxGNN이 제시하는 추정 기전 연결고리는 다음과 같습니다. NSIAD는 AVPR2(V2 바소프레신 수용체)의 기능 획득형 돌연변이로 인해 수용체가 지속적으로 활성화되고, 이로 인한 cAMP/PKA 신호 증가가 Aquaporin-2(AQP2)를 집합관 정단막으로 지속 전위시켜 자유수 과잉 재흡수 및 저나트륨혈증을 유발하는 X-연관 유전 질환입니다. 이론적으로 집합관 주세포에서 Cav3.x 채널이 기능적으로 발현된다면, Ethosuximide의 T형 채널 차단이 세포 내 Ca²⁺를 감소시켜 AQP2의 막 삽입을 줄이고 수분 저류를 완화할 수 있다는 추론입니다.

그러나 이 연결고리는 **극도로 추정적(speculative)**이며, 다음과 같은 핵심 증거 공백이 존재합니다: ① 신장 집합관에서의 Cav3.x 기능적 발현 미확인, ② V2R 지속 활성화 경로와 T형 칼슘 채널 간의 직접적 상호작용에 관한 문헌 부재, ③ Ethosuximide의 신세관 내 약동학 데이터 부재, ④ 돌연변이 V2R의 약물 반응 예측 불가. TxGNN의 고점수는 지식 그래프(KG)에서 '항경련제 → 이온 채널 → 신장 기능' 경로 매칭에 기인한 것으로, 직접적인 생물학적 검증을 반영하지 않습니다.

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
임상시험, 관찰 연구, 문헌 근거가 전무하며(L5), 제안된 기전 연결고리가 순수 추론 수준에 머물러 있습니다. 또한 Ethosuximide는 국내 미시판 약물로, 재창출을 진행하기 전 기초 데이터 확보가 선행되어야 합니다.

**진행하려면 필요한 것:**
- 신장 집합관 세포주 또는 동물 모델에서 Cav3.x 발현 및 Ethosuximide 효과 확인 (전임상 필수)
- NSIAD 환자 또는 AVPR2 돌연변이 유발 동물 모델에서의 개념 증명(proof-of-concept) 연구
- Ethosuximide의 신장 조직 분포 및 약동학 데이터
- 기존 표준치료(수분 제한, 저염식, urea 보충)와의 비교 프레임워크 설정
- DrugBank 기반 MOA 상세 데이터 및 TFDA/국내 허가사항 안전성 정보 수집
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

