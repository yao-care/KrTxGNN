---
layout: default
title: Benzonatate
parent: 僅模型預測 (L5)
nav_order: 133
evidence_level: L5
indication_count: 2
---

# Benzonatate
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

# Benzonatate: 기침 억제에서 마미 증후군으로

## 한 문장 요약

Benzonatate는 전압의존성 나트륨 채널(VGSC)을 차단하는 국소마취제 계열 약물로, 기침 억제제로 알려져 있습니다. TxGNN 모델은 **마미 증후군(Cauda Equina Syndrome)**에 효과가 있을 수 있다고 예측하나, 현재 이를 지지하는 임상시험 및 문헌 근거는 전혀 확인되지 않았습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 정보 없음 (한국 미시판) |
| 예측 신규 적응증 | 마미 증후군 (Cauda Equina Syndrome) |
| TxGNN 예측 점수 | 99.66% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

상세한 작용 기전(MOA) 데이터가 확보되지 않았습니다. 알려진 정보에 따르면, Benzonatate는 국소마취제 계열(local anesthetic-type)의 비마약성 기침 억제제로, 전압의존성 나트륨 채널(VGSC) 차단을 통해 구심성 감각 신경의 과활성을 억제하고 기침 반사를 감소시키는 것으로 알려져 있습니다.

마미 증후군(Cauda Equina Syndrome, CES)은 요천추 신경근의 급성 압박으로 인해 극심한 신경병증성 통증, 방광·장 기능 장애, 하지 감각운동 결손이 동반되는 상태입니다. 이론적으로 Benzonatate의 VGSC 차단 기전은 이상 방전을 일으키는 감각 신경 충동을 약화시킬 수 있으며, 이는 mexiletine·lidocaine 등 나트륨 채널 차단제가 신경병증성 통증 치료에 활용되는 공통 기전과 유사합니다. 따라서 기전적 연관성은 **낮음~중등도**로 평가됩니다.

그러나 다음의 중요한 한계가 있습니다. ① CES의 1차 치료는 긴급 외과적 감압이며 약물의 역할은 극히 제한적입니다. ② 경구 투여 후 전신성 VGSC 차단 농도와 신경계 국소 작용 농도 사이의 차이가 크며, 신경계 침투율에 대한 보고가 없습니다. ③ 이를 뒷받침하는 동물 모델 또는 체외(in vitro) 연구가 현재 존재하지 않습니다.

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
TxGNN 예측 점수는 99.66%로 높으나, 이를 지지하는 임상시험 또는 문헌 근거가 전혀 없는 L5 수준이며, 마미 증후군은 외과적 응급 질환으로 약물 재창출의 적용 포지셔닝이 불명확합니다.

**진행하려면 필요한 것:**
- DrugBank API 또는 공식 허가 문서를 통한 상세 MOA 데이터 확보
- 경구 Benzonatate의 신경계 침투율 및 전신 VGSC 차단 농도 데이터 확인
- 마미 증후군 또는 관련 신경병증성 통증 동물 모델에서의 전임상 연구 수행
- 약물 재창출 포지셔닝 명확화 (예: 수술 후 잔류 신경통 보조 진통 등 구체적 시나리오)
- 안전성 정보 확보 (FDA/TFDA 허가사항 기반 경고·금기 사항 확인)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

