---
layout: default
title: Cholic Acid
parent: 僅模型預測 (L5)
nav_order: 164
evidence_level: L5
indication_count: 10
---

# Cholic Acid
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

# Cholic Acid: 담즙산 합성 장애에서 HIV 감염 질환으로

## 한 문장 요약

Cholic Acid는 체내에서 자연 생성되는 1차 담즙산으로, 국제적으로 담즙산 합성 결함(Bile Acid Synthesis Disorder) 치료에 사용되나 한국에서는 아직 허가되지 않은 약물입니다.
TxGNN 모델은 **HIV 감염 질환(HIV Infectious Disease)**에 효과가 있을 수 있다고 예측(예측 점수 99.79%)하였으나, 이를 직접 지지하는 임상시험 및 문헌 근거는 현재 **전혀 존재하지 않습니다**.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 담즙산 합성 장애 (국제 허가, 한국 미허가) |
| 예측 신규 적응증 | HIV 감염 질환 (HIV Infectious Disease) |
| TxGNN 예측 점수 | 99.79% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. Cholic Acid는 콜레스테롤로부터 효소적으로 합성되는 1차 담즙산(primary bile acid)으로, 담즙산 합성 결함 환자에서 독성 담즙산 중간대사물의 생성을 억제하고 정상적인 담즙 흐름과 지용성 비타민 흡수를 회복시키는 보충 요법으로 사용됩니다. 미국 FDA는 2015년 Cholbam® (cholic acid 캡슐)을 담즙산 합성 효소 결핍에 의한 담즙산 합성 장애 치료제로 승인하였습니다.

HIV 감염 질환과의 기전적 연관성과 관련하여, 담즙산이 핵내 수용체(FXR, TGR5)를 통해 장내 면역 조절 및 장 상피 장벽 기능에 관여한다는 연구들이 있으며, HIV 감염 환자에서 장내 마이크로바이옴 변화 및 담즙산 대사 이상이 보고된 바 있습니다. 그러나 Cholic Acid가 HIV에 대해 직접적인 항바이러스 효과 또는 임상적으로 유의미한 면역 조절 효과를 갖는다는 기전적·임상적 근거는 현재 문헌으로 확인되지 않습니다.

TxGNN 모델은 생물의학 지식 그래프(Knowledge Graph) 기반의 링크 예측 알고리즘으로 높은 예측 점수를 산출하였으나, 이 예측은 직접적인 임상 관찰 없이 네트워크 기반 추론에 의한 것으로, 독립적인 실험적·임상적 검증이 반드시 필요합니다.

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
HIV 감염 질환에 대한 Cholic Acid의 효능을 지지하는 임상시험 및 문헌 근거가 전무하며, 기전적 연관성도 현재 확립되어 있지 않습니다. 한국 내 허가 및 시판 이력이 없어 안전성 프로필 역시 별도 확인이 필요하며, 현재는 TxGNN 모델 예측만 존재하는 L5 수준입니다.

**진행하려면 필요한 것:**
- 작용 기전(MOA) 데이터 확보 (DrugBank DB02659 API 조회)
- HIV 감염과 담즙산 수용체(FXR/TGR5) 신호 경로 연관성에 관한 전임상 문헌 체계적 탐색
- 한국 내 안전성 정보 확보 (MFDS 허가사항 또는 FDA Prescribing Information 참조)
- 근거 수준 L3 이상(관찰 연구 또는 체계적 문헌고찰) 확보 후 개발 타당성 재평가
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

