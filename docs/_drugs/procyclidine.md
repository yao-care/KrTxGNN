---
layout: default
title: Procyclidine
parent: 僅模型預測 (L5)
nav_order: 577
evidence_level: L5
indication_count: 10
---

# Procyclidine
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

# Procyclidine: 파킨슨병에서 소아기 발병 파킨슨병으로

## 한 문장 요약

Procyclidine은 원래 파킨슨병 및 약물 유발성 추체외로 증상 치료에 사용되어 온 항콜린성 약물입니다. TxGNN 모델은 **소아기 발병 파킨슨병 19A(juvenile onset Parkinson disease 19A)**에 효과가 있을 수 있다고 예측했지만, 이를 뒷받침하는 임상시험이나 문헌은 현재 없으며 모델 예측에만 의존하고 있습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (원본 적응증 정보 미확보) |
| 예측 신규 적응증 | 소아기 발병 파킨슨병 19A (Juvenile Onset Parkinson Disease 19A) |
| TxGNN 예측 점수 | 99.94% |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미상시 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 다만 약리학적으로 잘 알려진 사실에 따르면, Procyclidine은 항콜린성(무스카린 수용체 길항) 약물로, 선조체 내 아세틸콜린-도파민 불균형을 조절하여 파킨슨병 및 약물 유발성 추체외로 증상(EPS)의 진전·경직 완화에 오랫동안 사용되어 왔습니다.

1순위로 예측된 소아기 발병 파킨슨병 19A(PARK19A, DNAJC6 관련)는 시냅스 소포 운반 결함이 병리 기전인 단일유전자 질환으로, Procyclidine의 항콜린 기전과 직접적인 연관성은 없습니다. 진전·경직 등 임상 표현형이 고전적 파킨슨병과 겹치기 때문에 TxGNN이 높은 점수를 부여한 것으로 판단되며, 기전 특이적 근거는 부족합니다.

오히려 10순위로 예측된 **일반 파킨슨병(Parkinson disease)**이 Procyclidine의 실제 임상 사용과 기전적으로 가장 부합합니다. 이는 이미 알려진 용도의 재확인에 가까우며, 본 예측 목록 상위 항목들(희귀 유전성 파킨슨증후군, ADHD, Rasmussen 뇌염, 척수염 등)은 표현형 유사성에 따른 지식그래프 잡음(noise)일 가능성이 높습니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 관련 문헌이 없습니다.

> 참고: 2순위 예측 질환(비정형 소아 파킨슨증)에 대해 문헌 1건(PMID 39347240, Vitamin E와 항정신병약 유발 지연성운동장애/EPS 관련 증례보고)이 검색되었으나, Procyclidine 자체를 직접 다루지 않아 1순위 적응증에 대한 직접 근거로 사용할 수 없습니다.

---

## 한국 시판 정보

현재 한국(대만 규제 데이터 기준)에서 Procyclidine은 미상시 상태이며, 등록된 허가 정보가 없습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
1순위 예측 적응증(소아기 발병 파킨슨병 19A)은 TxGNN 점수는 높으나 뒷받침하는 임상시험이나 문헌이 전무하고, 병리 기전(시냅스 소포 운반 결함)이 Procyclidine의 항콜린 기전과 직접 연결되지 않아 순수 모델 예측(L5)에 그칩니다. 근거 부족으로 진행이 시기상조입니다.

**진행하려면 필요한 것:**
- TFDA 등 규제기관 허가사항 및 경고/금기 정보 확보 (현재 Blocking 데이터 갭)
- DrugBank를 통한 정확한 작용 기전(MOA) 데이터 확보
- PARK19A/DNAJC6 모델(세포·동물)에서 항콜린 약물의 증상 완화 효과에 대한 전임상 연구
- 필요 시 10순위 예측인 일반 파킨슨병(기존 잘 알려진 용도)을 우선 검토 대상으로 재평가
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

