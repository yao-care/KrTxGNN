---
layout: default
title: Salsalate
parent: 僅模型預測 (L5)
nav_order: 304
evidence_level: L5
indication_count: 8
---

# Salsalate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Salsalate: 관절염에서 Hunter-Thompson형 말단중간 이형성증으로

## 한 문장 요약

Salsalate는 비아세틸화 살리실산염 계열의 비스테로이드성 소염진통제(NSAID)로, 류마티스 관절염·골관절염 등 만성 염증 질환 치료에 사용되어 온 약물입니다. TxGNN 모델은 **Hunter-Thompson형 말단중간 이형성증(Acromesomelic Dysplasia, Hunter-Thompson Type)**에 효과가 있을 수 있다고 예측하나, 이를 뒷받침하는 **임상시험 및 문헌 근거는 현재 전무하며(근거 수준 L5)**, 8개의 예측 적응증 중 기전 연관성이 가장 높은 후보는 8순위의 척추관절병증이나 이 역시 직접 근거가 부재한 상태입니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (한국 미등재) |
| 예측 신규 적응증 | Hunter-Thompson형 말단중간 이형성증 (Acromesomelic Dysplasia, Hunter-Thompson Type) |
| TxGNN 예측 점수 | 99.92% |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미상 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 JSON 데이터에 Salsalate의 상세 작용 기전(MOA) 정보가 포함되어 있지 않습니다. 알려진 정보에 따르면, Salsalate는 살리실산의 이중에스터(salicylsalicylic acid) 형태로 체내에서 두 분자의 살리실산으로 분해됩니다. 아스피린과 달리 COX 효소를 비가역적으로 차단하지 않으며, **IKKβ 억제를 통한 NF-κB 신호 차단**이 주요 항염증 기전으로 제시됩니다. 이 경로는 전신 인슐린 저항성과도 연관되어 대사 질환 연구에서도 주목받은 바 있습니다.

Hunter-Thompson형 말단중간 이형성증은 **GDF5/CDMP1 유전자 돌연변이**로 인해 BMP(뼈 형성 단백질) 신호 전달 경로가 결손되어 발생하는 희귀 유전성 골격 발달 이상입니다. 전완부 및 하퇴부의 현저한 단축이 특징이며, 태아기 발달 단계에서 고정되는 구조적 이상입니다.

Salsalate의 NF-κB 억제 기전은 BMP/GDF5 신호 결손과 직접적 연관성이 없습니다. 살리실산염이 골 대사에 간접적으로 영향을 미칠 가능성은 이론적으로 제기되나, 이 유전성 구조적 결함에 대한 기전적 연결고리는 극히 미약합니다. **모델 예측 점수(99.92%)가 높음에도 불구하고, 이는 지식 그래프 내 네트워크 구조에 기인한 것으로 해석되며 임상적 타당성은 낮습니다.**

> **주목할 후보**: 8개 예측 적응증 중 **척추관절병증(Spondyloarthropathy, rank 8, 근거 수준 L4)**이 기전상 가장 타당합니다. NSAID는 척추관절병증의 1차 표준 치료이며, Salsalate의 NF-κB 억제 → TNF-α/IL-17 감소 경로가 이 질환의 병태생리와 직접 연관됩니다.

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
1순위 예측 적응증인 Hunter-Thompson형 말단중간 이형성증은 GDF5/BMP 신호 결손으로 인한 희귀 유전성 골격 이상으로, Salsalate의 항염증(NF-κB 억제) 기전과 기전적 연관성이 극히 낮습니다. 임상시험 및 문헌 근거가 전무(L5)하고 한국 내 허가 데이터도 존재하지 않아 현재 단계에서 추진 근거가 불충분합니다.

**진행하려면 필요한 것:**
- **MOA 데이터 보완**: DrugBank API 조회를 통해 Salsalate 작용 기전 상세 확인
- **안전성 데이터 확보**: MFDS 또는 FDA/EMA 허가사항에서 경고·금기·이상반응 수집 (현재 Blocking 데이터 격차)
- **척추관절병증 별도 평가 권장**: rank 8의 Spondyloarthropathy에 대해 Salsalate 특이적 임상시험 및 문헌 재검색 — NSAID 계열로서 기전적 타당성이 가장 높으며, 별도 보고서 작성 검토 요망
- **전임상 근거 탐색**: NF-κB 억제가 연골·골격 발달에 미치는 영향에 관한 기초 연구 문헌 확인
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

