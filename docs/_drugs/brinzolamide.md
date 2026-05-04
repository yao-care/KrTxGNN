---
layout: default
title: Brinzolamide
parent: 僅模型預測 (L5)
nav_order: 149
evidence_level: L5
indication_count: 1
---

# Brinzolamide
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

# Brinzolamide: 개방각 녹내장/고안압증에서 원발성 유전성 녹내장으로

## 한 문장 요약

Brinzolamide는 제2형 탄산탈수효소 억제제(CAI)로, 원래 개방각 녹내장 및 고안압증 치료에 사용되는 국소 안과용 약물입니다.
TxGNN 모델은 **원발성 유전성 녹내장(Primary Hereditary Glaucoma)**에도 효과가 있을 수 있다고 예측하며(예측 점수: 99.48%),
현재 **임상시험 및 관련 문헌은 없으나** 이미 검증된 안압 강하 기전과 직접적인 병태생리 연관성이 예측을 뒷받침합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 개방각 녹내장, 고안압증 |
| 예측 신규 적응증 | 원발성 유전성 녹내장 (Primary Hereditary Glaucoma) |
| TxGNN 예측 점수 | 99.48% |
| 근거 수준 | L4（기전 연구 기반） |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

Brinzolamide는 섬모체 상피세포의 제2형 탄산탈수효소(Carbonic Anhydrase II)를 억제하여 중탄산나트륨 분비를 차단하고, 이를 통해 방수(aqueous humor) 생성을 줄여 안압(IOP)을 낮춥니다. 이 기전은 개방각 녹내장과 고안압증에서 이미 임상적으로 충분히 검증되어 있습니다.

원발성 유전성 녹내장의 핵심 병태생리는 **섬유주(trabecular meshwork) 발달 이상**으로 인한 방수 유출 저항 증가 및 안압 상승입니다. 이 병인 메커니즘은 Brinzolamide의 방수 생성 억제 작용점과 직접 대응하므로, 이번 예측은 교차 기전 재창출이 아닌 **동일 약리 경로의 적응증 확장(category extension)**에 해당합니다. 기전적 타당성은 높게 평가됩니다(TxGNN score: 0.9948).

다만 임상 현실에서 원발성 유전성 녹내장의 1차 치료는 **수술(goniotomy, trabeculotomy)**이 주를 이루며, CAI 계열 약물은 수술 전후 보조적 안압 강하 목적으로 활용됩니다. 현재 이 유전 아형에 특화된 임상시험이나 발표 문헌이 존재하지 않아 근거 축적이 필요한 상황입니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 관련 문헌이 없습니다.

---

## 한국 시판 정보

Brinzolamide는 현재 한국에서 허가 및 시판 이력이 없습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 점수(99.48%)와 기전적 연관성이 명확하나, 원발성 유전성 녹내장에 대한 임상시험 및 문헌 근거가 전혀 없고, 한국 내 허가·안전성 데이터도 부재합니다. 기전상 타당성은 충분하지만, 현 단계에서 즉각 진행은 어렵습니다.

**진행하려면 필요한 것:**
- 식품의약품안전처(MFDS) 허가 여부 및 약물 경고·금기사항 확인
- 상세 작용 기전(MOA) 데이터 확보 (DrugBank API 조회 권장)
- 원발성 유전성 녹내장 환자군을 대상으로 한 관찰 연구 또는 임상시험 계획 수립
- 유전 아형별 안전성 모니터링 계획 마련
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

