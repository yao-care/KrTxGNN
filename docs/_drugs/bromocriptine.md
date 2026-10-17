---
layout: default
title: Bromocriptine
parent: 모델 예측만 (L5)
nav_order: 161
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Bromocriptine: 예측 신규 적응증 선천성 당화 장애… (근거 수준 L5). 기존 적응증: 허가 적응증 본문 확인 불가 (허가 문서 링크만 제공됨)"
monitor_inn: "Bromocriptine"
predicted_indications: ["congenital disorder of glycosylation with defective fucosylation", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "retinal dystrophy with or without extraocular anomalies", "atypical glycine encephalopathy", "myopia 26, X-linked, female-limited", "hydranencephaly (disease)", "myopia X-linked", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "schizophrenia", "syndromic myopia"]
---

# Bromocriptine
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
{: .fs-6 .fw-300 }

---

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 약사 평가 보고서

</div>

# Bromocriptine: 허가 적응증 정보 미확인에서 선천성 당화 장애(예측 1순위)로

## 한 문장 요약

Bromocriptine은 도파민 D2 수용체 작용제로, 한국에서는 팔로델정(삼일제약)으로 시판 중입니다. 다만 이번 데이터에는 허가 적응증 본문이 포함되어 있지 않습니다.
TxGNN 모델은 **선천성 당화 장애(fucosylation 결함형)**를 1순위 신규 적응증으로 예측하지만, 이를 뒷받침하는 **임상시험과 문헌은 없습니다(0건)**.
10개 예측 중 임상시험이 연결된 것은 조현병 1건뿐이며, 이 예측들은 대부분 모델 예측 수준에 머뭅니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문 확인 불가 (허가 문서 링크만 제공됨) |
| 예측 신규 적응증 | 선천성 당화 장애, fucosylation 결함형 (congenital disorder of glycosylation with defective fucosylation) |
| TxGNN 예측 점수 | 99.83% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 수집되지 않았습니다. 일반적으로 알려진 바로는 bromocriptine은 도파민 D2 수용체 작용제입니다. 이 작용은 프로락틴 분비 조절과 도파민 신호 전달에 관여합니다.

1순위 예측인 fucosylation 결함형 선천성 당화 장애는 당 사슬 부착 과정의 유전적 결함이며, 도파민 D2 작용과 연결되는 기전은 확인되지 않았습니다. 이 높은 점수는 지식 그래프 기반 예측일 뿐이며, 생물학적·임상적 근거가 없습니다.

참고로 상위 10개 예측 중 일부는 약리학적으로 느슨한 연관성이 있습니다.
- **망막 이영양증(3순위)**: 망막 생리에 도파민 신호가 관여합니다. 2024년 전임상 연구(PMID 39009597)에서 tamsulosin, metoprolol, bromocriptine 병용이 여러 망막병증 모델에서 효과를 보였습니다.
- **근시 관련 질환(5, 7, 10순위)**: 망막 도파민이 안구 성장 조절에 관여한다는 일반 개념만 있고, bromocriptine 고유의 근거는 없습니다.
- **조현병(9순위)**: 아래 임상시험 근거 항목에서 별도로 다룹니다.

## 임상시험 근거

1순위 예측 질환에 대해서는 현재 관련 임상시험 등록이 없습니다.

참고로 9순위 예측(조현병)에는 다음 시험이 연결되어 있습니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT03575000](https://clinicaltrials.gov/study/NCT03575000) | Phase 4 | 모집 예정 | 15 | 항정신병약 관련 내당능장애·인슐린 저항성에 대한 bromocriptine 추가 투여의 안전성·내약성을 평가하는 단일군 공개 소규모 시험. 정신병 증상이 아닌 대사 문제가 목표이며 결과는 아직 없음 |

## 문헌 근거

1순위 예측 질환에 대해서는 현재 관련 문헌이 없습니다.

참고로 3순위 예측(망막 이영양증)에 연결된 문헌은 다음과 같습니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [39009597](https://pubmed.ncbi.nlm.nih.gov/39009597/) | 2024 | 전임상 연구 | Nature Communications | tamsulosin, metoprolol, bromocriptine 병용이 GPCR 조절로 세포 내 cAMP와 Ca2+ 활성을 억제해 돌연변이와 무관하게 전임상 망막병증 모델을 개선함 |
| [1753674](https://pubmed.ncbi.nlm.nih.gov/1753674/) | 1991 | 증례 보고 | Klin Monatsbl Augenheilkd | Goldmann-Favre 증후군에서 cyclosporin A와 bromocriptine 병용 치료를 보고함. bromocriptine 단독 기여도는 구분 불가 |

9순위 예측(조현병)과 관련해서는 약리학 리뷰가 다수 있으나 효능을 입증하는 근거는 없습니다. 한 증례 보고(PMID 8120934)는 bromocriptine에 의한 조현병 유발이라는 안전성 신호를 기술했습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200410070 | 팔로델정(브로모크립틴메실산염) | 백색의 원형정제 | 허가 적응증 본문 확인 불가 (허가 문서 링크만 제공됨) |

## 안전성 고려사항

- **약물 상호작용**: 총 87건이 확인되었으며, 이 중 주요(Major) 등급은 다음과 같습니다.
  - Isometheptene
  - Lorcaserin
- 중등도(Moderate) 상호작용으로는 morphine, clarithromycin, dronabinol, lansoprazole, metoclopramide, promethazine, ethanol 등이 있습니다.
- 조현병 관련 문헌에서는 bromocriptine 투여 후 정신병 증상이 유발된 증례(PMID 8120934)가 보고되었습니다.

경고와 금기 등 그 밖의 안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
1순위 예측은 모델 점수만 높고 임상시험과 문헌이 전혀 없으며, 도파민 D2 작용과 fucosylation 결함 사이의 기전적 연결도 확인되지 않습니다. 상위 10개 예측 중에서는 망막 이영양증이 전임상·증례 수준의 근거(L4)로 연구 과제 후보가 될 수 있고, 조현병은 대사 보조요법이라는 제한된 틈새만 있습니다.

**진행하려면 필요한 것:**
- 허가 적응증, 경고, 금기 등 허가사항 문서(첨부문서)의 내용 확보 및 분석
- 작용 기전(MOA) 데이터 보완
- 1순위 질환에 대한 기전 연구 또는 전임상 근거
- 망막 이영양증은 bromocriptine 단독 효과를 분리해 검증하는 전임상 연구
- 조현병은 NCT03575000 결과 확인 및 정신병 악화 위험 평가
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

