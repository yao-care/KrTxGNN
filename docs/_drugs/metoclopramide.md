---
layout: default
title: Metoclopramide
parent: 僅模型預測 (L5)
nav_order: 476
evidence_level: L5
indication_count: 5
---

# Metoclopramide
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

# Metoclopramide: 위장운동 촉진(항구토)에서 위궤양(Gastric Ulcer)으로

## 한 문장 요약

Metoclopramide는 도파민 D2 수용체 길항 작용을 통해 위 배출을 촉진하는 항구토·위장운동 촉진제로 국제적으로 널리 사용되어 왔습니다. TxGNN 모델은 **위궤양(Gastric Ulcer)**에 효과가 있을 수 있다고 예측(점수 99.93%)하지만, 현재 **2건의 임상시험**과 **20편의 문헌** 중 궤양 치료 효능을 직접 입증하는 근거는 없고 대부분 위장관 운동 기전 연구입니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (한국 허가/시판 이력 없음, `original_indications` 미기재) |
| 예측 신규 적응증 | 위궤양 (Gastric Ulcer) |
| TxGNN 예측 점수 | 99.93% |
| 근거 수준 | L3 (S1 단계, "Research Question" — RCT 부재, 관찰·전임상 연구 중심) |
| 한국 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터는 확보되지 않았습니다(DrugBank 조회 필요, Blocking 아님이나 High 우선순위 데이터 갭). 다만 알려진 약리학 정보에 따르면 Metoclopramide는 도파민 D2 수용체 길항제이자 5-HT4 작용제/5-HT3 길항제로, 위 배출을 촉진하고 하부식도괄약근 압력을 높이는 **위장관 운동촉진제(prokinetic)**입니다. 이 기전은 제산·위산 분비 억제나 점막 보호·궤양 치유 촉진과는 무관합니다.

Evidence Pack에 포함된 재창출 근거(rationale)도 같은 결론을 뒷받침합니다: TxGNN의 높은 점수(0.999)는 지식그래프 상에서 이 약물이 "위장관 질환" 노드 군집과 폭넓게 연결되어 있기 때문일 가능성이 크며, 궤양 치료에 특이적인 생물학적 타당성을 반영한 것은 아닙니다. 실제로 문헌에서 확인되는 가장 근접한 임상적 역할은 **상부위장관 출혈(궤양 출혈 포함) 환자의 내시경 전 전처치**로, 위 내용물을 비워 시야를 개선하는 용도이지 궤양 자체를 치료하는 용도가 아닙니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT05746377](https://clinicaltrials.gov/study/NCT05746377) | Phase 4 | 상태 불명(UNKNOWN) | 60 | 상부위장관 출혈 환자의 내시경 전 metoclopramide 투여가 반복 내시경·중재 필요성 및 위벽 시야를 개선하는지 평가하는 이중맹검 RCT. 궤양 "치료" 효능이 아닌 내시경 전처치 목적이며, 결과 미발표. |
| [NCT03747107](https://clinicaltrials.gov/study/NCT03747107) | N/A | 완료 | 19 | 1차 의료 처방 안전성 개선 프로그램(P-DQIP) 연구로, 제목상 위궤양 치료와 직접적 연관성 없음(데이터베이스 키워드 오매칭 가능성, grade C). |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [16807979](https://pubmed.ncbi.nlm.nih.gov/16807979/) | 2006 | RCT | Yonsei Medical Journal | 복강경 부인과 수술 전 metoclopramide+ranitidine 정맥투여가 위 내용물에 미치는 영향 평가(이중맹검 RCT). 궤양 치료가 아닌 수술 전처치 연구. |
| [6336644](https://pubmed.ncbi.nlm.nih.gov/6336644/) | 1983 | Review | Annals of Internal Medicine | Metoclopramide의 약리학 및 임상 적용 전반 개관. 항구토·위장관 운동촉진 효과를 주된 임상 용도로 기술, 항궤양 효과는 언급되지 않음. |
| [19225](https://pubmed.ncbi.nlm.nih.gov/19225/) | 1977 | Review | Drugs | 위·십이지장궤양 치료 약물 전반에 대한 리뷰(초록 없음, 제목 기준 직접 관련). |
| [775822](https://pubmed.ncbi.nlm.nih.gov/775822/) | 1976 | 미분류 | ZFA (독일) | "Metoclopramide를 이용한 위·십이지장궤양 치료" (초록 없음, 제목 기준 직접 관련 — 1970년대 독일 문헌으로 현대적 근거수준 낮음). |
| [2730234](https://pubmed.ncbi.nlm.nih.gov/2730234/) | 1989 | 동물실험(전임상) | Arch Int Pharmacodyn Ther | 알비노 쥐에서 아스피린 유발/유문결찰 위궤양 모델에 metoclopramide 20·50mg/kg 투여 시 궤양 보호 효과 관찰, ranitidine과 비교. |
| [6436177](https://pubmed.ncbi.nlm.nih.gov/6436177/) | 1984 | 동물실험(전임상) | Indian J Physiol Pharmacol | 기니피그 3종 위궤양 모델에서 metoclopramide가 위산 분비에는 영향 없이 위 배출 촉진을 통해 보호 효과를 나타냄. |
| [4779253](https://pubmed.ncbi.nlm.nih.gov/4779253/) | 1973 | 미분류 | Curr Med Res Opin | 위궤양에서 흡연·metoclopramide·carbenoxolone sodium이 담즙 역류에 미치는 영향(초록 없음). |
| [6782467](https://pubmed.ncbi.nlm.nih.gov/6782467/) | 1981 | 미분류 | MMW | Domperidone·metoclopramide가 혈청 가스트린 및 위산 분비에 미치는 영향 교차 이중맹검 연구(건강 대상자 12명). 유의한 변화 없음(제산 기전 부재 뒷받침). |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. (한국 시판 이력 없음, TFDA 수준 경고·금기 자료 미확보 — Blocking 데이터 갭)

**기전적 주의사항**: Evidence Pack 내 다른 예측 적응증(peptic ulcer perforation, rank 5) 검토 과정에서, metoclopramide의 위장관 운동촉진 기전이 **천공 또는 장폐색 의심 환자에서는 이론상 상대적 금기**에 해당할 수 있다는 우려가 제기되었습니다. 위궤양 환자 중 천공·출혈 위험이 있는 경우 특히 주의가 필요합니다.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 근거 수준 L3로, 위궤양 치료 효능을 직접 입증하는 RCT가 없습니다. 유일한 관련 Phase 4 시험(NCT05746377)도 상태 불명이며 결과가 발표되지 않았습니다.
- 기전적으로 metoclopramide는 위산 억제·점막 보호·치유 촉진 작용이 없어, "궤양 치료제"로서의 생물학적 타당성이 약합니다. TxGNN 고득점은 위장관 질환 노드 군집화에 따른 결과일 가능성이 있습니다.
- TFDA 수준 경고·금기 자료가 없어 안전성 초기 평가(S1) 자체가 불가능한 Blocking 데이터 갭이 존재합니다.

**진행하려면 필요한 것:**
- TFDA(또는 현지 규제기관) 허가사항의 경고·금기 정보 확보 (DG001, Blocking)
- DrugBank 작용기전(MOA) 상세 자료 확보 (DG002)
- 위궤양(궤양 치유율 등) 효능을 직접 평가한 전향적 임상 근거 확보
- 한국 내 시판/허가 현황 재확인 (현재 미출시, 0건)
- (참고) TxGNN 예측 목록에는 gastroduodenitis, peptic ulcer disease, gastrojejunal ulcer, peptic ulcer perforation 등 4건의 추가 후보가 있으나 모두 임상시험 근거 없이 Hold 등급이며, 마지막 후보는 오히려 상대적 금기 가능성이 제기됨
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

