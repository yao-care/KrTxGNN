---
layout: default
title: Granisetron
parent: 僅模型預測 (L5)
nav_order: 366
evidence_level: L5
indication_count: 10
---

# Granisetron
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

# GRANISETRON: 오심·구토 예방에서 조증형 양극성 정동장애로

## 한 문장 요약

Granisetron(DB00889)은 선택적 5-HT3 수용체 길항제로, 원래 오심·구토 예방(항구토제) 목적의 약물로 알려져 있습니다.
TxGNN 모델은 **조증형 양극성 정동장애(Manic Bipolar Affective Disorder)**에 효과가 있을 수 있다고 예측하나(예측 점수 99.62%),
현재 이를 뒷받침하는 **임상시험이나 문헌은 전혀 없으며**, 근거 수준은 모델 예측만 존재하는 최하위 단계(L5)입니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (허가 정보 부재, 다만 약물 분류상 5-HT3 길항제/항구토제로 추정) |
| 예측 신규 적응증 | 조증형 양극성 정동장애 (Manic Bipolar Affective Disorder) |
| TxGNN 예측 점수 | 99.62% |
| 근거 수준 | L5 (모델 예측만 존재, 실제 임상/문헌 근거 없음) |
| 한국 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 Granisetron의 상세한 작용 기전(MOA) 데이터는 확보되어 있지 않습니다([Data Gap], DrugBank 재조회 필요). 다만 evidence pack 내 예측 근거 텍스트에 따르면, Granisetron은 선택적 5-HT3 수용체 길항제이며 항구토제로 사용되는 약물로 파악됩니다.

TxGNN이 제시한 기전적 연결고리는 다음과 같습니다: ondansetron 등 다른 5-HT3 길항제가 중뇌변연계 도파민 경로를 조절할 수 있다는 논의가 있었고, 이는 이론상 조증/기분장애의 도파민-세로토닌 불균형과 간접적으로 관련될 수 있다는 것입니다. 그러나 이는 **Granisetron 고유의 근거가 아니라 약물 클래스 전반에 대한 추론**이며, TxGNN의 높은 점수는 지식그래프 내 "5-HT3 길항제" 카테고리와 정신과 적응증 간의 공유 타깃/공발생 패턴을 반영한 결과일 가능성이 높습니다. 즉, 직접적인 약리학적 증거는 아직 없는 상태입니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 관련 문헌이 없습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

(TFDA 원본 첨부문서의 경고/금기 정보가 아직 확보되지 않은 상태이며, 이는 안전성 초기 평가(S1) 진입을 막는 Blocking 등급 데이터 공백으로 분류되어 있습니다.)

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
조증형 양극성 정동장애에 대해 Granisetron을 뒷받침하는 임상시험, 문헌, 또는 약물 고유의 기전 증거가 전혀 없습니다. TxGNN 점수는 높지만 근거 수준이 L5(모델 예측만 존재)로, 지식그래프 임베딩 유사도에 의한 예측일 가능성이 커 현시점에서는 진행 근거가 부족합니다.

**진행하려면 필요한 것:**
- TFDA 허가사항(경고/금기) 확보 — 현재 Blocking 등급 데이터 공백으로 S1 안전성 초기평가 자체가 불가능
- DrugBank 등에서 정확한 작용 기전(MOA) 데이터 확보
- 조증/양극성 장애와 관련된 전임상 또는 사례 보고 수준의 문헌 탐색 (현재 PubMed 검색 결과 0건)
- Granisetron 고유의 중추신경계 작용 관련 약리 데이터 확인 (현재 근거는 타 5-HT3 길항제로부터의 유추에 불과)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

