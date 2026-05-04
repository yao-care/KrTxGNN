---
layout: default
title: Cabergoline
parent: 僅模型預測 (L5)
nav_order: 158
evidence_level: L5
indication_count: 5
---

# Cabergoline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Cabergoline: 고프로락틴혈증에서 뇌하수체 선암종으로

---

## 한 문장 요약

Cabergoline은 도파민 D2/D3 수용체 고선택적 작용제로, 고프로락틴혈증 및 프로락틴 분비 선종(prolactinoma)의 1차 치료제로 사용되고 있습니다.
TxGNN 모델은 **뇌하수체 선암종(Pituitary Adenocarcinoma)**에 효과가 있을 수 있다고 예측하며(점수 99.06%),
현재 이 방향을 직접 지지하는 **임상시험 및 문헌 근거는 확보되어 있지 않으며**, 기전적 합리성에 근거한 연구 가설 단계입니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 고프로락틴혈증 / 프로락틴 분비 선종 (Prolactinoma) |
| 예측 신규 적응증 | 뇌하수체 선암종 (Pituitary Adenocarcinoma) |
| TxGNN 예측 점수 | 99.06% |
| 근거 수준 | L4 (기전 연구 기반) |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

Cabergoline은 뇌하수체 전엽의 도파민 D2 수용체를 자극하여 프로락틴 분비를 강력하게 억제하는 작용제입니다. 이 기전을 통해 고프로락틴혈증과 프로락틴 분비 선종(양성 뇌하수체 선종)에서 종양 축소 효과까지 나타내며, 수술을 대체하는 1차 약물 치료로 자리잡고 있습니다.

뇌하수체 선암종(pituitary adenocarcinoma)은 뇌·척수 전이를 동반하는 매우 드문 악성 뇌하수체 종양으로, 양성 선종과 생물학적 행동이 현저히 다릅니다. 그러나 일부 악성 및 침습성 뇌하수체 종양에서도 D2 수용체 발현이 확인되며, 도파민 작용제를 사용한 소수의 침습성 뇌하수체 종양 증례 보고가 존재합니다. TxGNN의 높은 예측 점수(0.9906)는 지식 그래프(KG) 내 뇌하수체–도파민 축의 강한 위상학적 연결을 반영한 것으로 해석됩니다.

다만, 양성 prolactinoma와 악성 adenocarcinoma 사이에는 분자적·임상적 차이가 뚜렷하며, 현재 직접적인 전향적 임상 근거는 개별 증례 보고 수준에 머물고 있습니다. 이번 예측은 도파민 수용체 발현이라는 기전적 연결 고리를 기반으로 한 연구 가설 단계로 평가됩니다.

---

## 임상시험 근거

현재 뇌하수체 선암종에 대한 Cabergoline 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 뇌하수체 선암종에 대한 Cabergoline 관련 문헌이 없습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
뇌하수체–도파민 D2 축의 기전적 연결은 개념적으로 타당하나, 뇌하수체 선암종에 대한 Cabergoline의 효능을 직접 지지하는 임상시험 또는 문헌 근거가 전무하고, 현재 한국 내 시판 허가 자체가 없어 추가 기초 연구가 선행되어야 합니다.

**진행하려면 필요한 것:**
- Cabergoline 상세 작용 기전(MOA) 데이터 확보 (DrugBank API 조회로 DG002 해소)
- 한국 허가사항(금기, 경고) 검토 (DG001 해소 — 현재 Blocking 데이터 갭)
- 악성 및 침습성 뇌하수체 종양에서의 D2 수용체 발현률 전임상 연구 검토
- 관련 개별 증례 보고에 대한 체계적 문헌 검색 (PubMed 수동 확장 검색)
- 향후 전임상 연구(in vitro/in vivo) 설계 검토
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

