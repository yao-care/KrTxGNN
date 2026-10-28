---
layout: default
title: Metoclopramide
parent: 모델 예측만 (L5)
nav_order: 512
evidence_level: L5
indication_count: 2
monitor_inn: "METOCLOPRAMIDE"
predicted_indications: ["gastroduodenitis", "peptic ulcer perforation"]
last_modified_at: 2026-10-27
description: "Metoclopramide: 예측 신규 적응증 위십이지장염 (gastroduodenitis) (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/197200484/EE"
---

# Metoclopramide
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **2** 건
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

## Metoclopramide: 위장관 운동 촉진제(D2 길항·5-HT4 작용) → 위십이지장염 (gastroduodenitis)
{: .text-alpha }

## 한 문장 요약

Metoclopramide는 도파민 D2 수용체 길항과 5-HT4 수용체 작용을 통해 위장관 운동을 촉진하는 약물입니다.
TxGNN 모델은 **위십이지장염(gastroduodenitis)**에 효과가 있을 수 있다고 예측하지만, 이 질환 자체를 직접 연구한 임상시험이나 문헌은 확인되지 않았습니다. 현재 근거는 모델 예측 수준(L5)입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/197200484/EE |
| 예측 신규 적응증 | 위십이지장염 (gastroduodenitis) |
| TxGNN 예측 점수 | 0.9990 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 데이터에 없습니다. 다만 수집된 문헌에 따르면 metoclopramide는 도파민 D2 길항, 5-HT4 작용, 콜린성 전달 강화를 통해 위-십이지장 협응과 위 배출을 개선하는 위장관 운동 촉진제로 알려져 있습니다.

위십이지장염에는 운동 장애와 오심·구토가 동반될 수 있어, 이러한 증상 완화 측면에서 기전상 연관성을 생각해 볼 수 있습니다. 다만 이는 항염증 효과가 아니라 증상 완화 목적의 가설입니다.

수집된 근거는 사람의 위십이지장 운동 연구(PMID 7886398, 8179003)와 상부위장관 출혈 환자의 내시경 시야 확보 RCT(PMID 38059896, 42259699)입니다. 이들은 위십이지장염 치료가 아니라 운동 기능 또는 시술 보조를 다룬 연구이므로, 증상 완화나 질병 조절에 대한 근거는 간접적입니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

위십이지장염 자체를 직접 다룬 문헌은 없었으며, 아래는 관련성이 있는 주요 문헌입니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [38059896](https://pubmed.ncbi.nlm.nih.gov/38059896/) | 2024 | RCT | Am J Gastroenterol | 활동성 상부위장관 출혈 환자에서 내시경 위 시야 확보를 위한 정맥 metoclopramide의 효과 평가 |
| [42259699](https://pubmed.ncbi.nlm.nih.gov/42259699/) | 2026 | RCT | Rev Gastroenterol Mex | 상부위장관 출혈에서 고용량 metoclopramide 대 위약의 위십이지장 시야 확보 비교 |
| [7886398](https://pubmed.ncbi.nlm.nih.gov/7886398/) | 1994 | 생리학 연구 | Scand J Gastroenterol | cisapride와 metoclopramide가 사람의 식후·공복기 antroduodenal 운동에 미치는 영향 |
| [8179003](https://pubmed.ncbi.nlm.nih.gov/8179003/) | 1994 | 기전 연구 | Am J Physiol | 개에서 cisapride, metoclopramide, domperidone의 위십이지장 배출 수축 기전 비교 |
| [7072665](https://pubmed.ncbi.nlm.nih.gov/7072665/) | 1982 | 임상 관찰 | Am J Dis Child | 소아의 위정체·원인 불명 구토에서 metoclopramide가 위십이지장 운동을 증가시킴 |
| [6382574](https://pubmed.ncbi.nlm.nih.gov/6382574/) | 1984 | 리뷰 | Scand J Gastroenterol Suppl | 도파민 길항제가 상부위장관 운동에 미치는 영향 |
| [18321441](https://pubmed.ncbi.nlm.nih.gov/18321441/) | 2008 | Review | Curr Treat Options Gastroenterol | 오심·구토의 원인과 관리 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 197200484 | 맥페란정(메토클로프라미드) | 흰색의 원형 필름코팅정 | 적응증 텍스트가 기록되어 있지 않음 |

## 안전성 고려사항

- **약물 상호작용**: 조회된 상호작용은 총 100건이며, 이 중 주요 등급은 다음과 같습니다.
  - 주요(Major): Tramadol, Amisulpride
  - 중등도(Moderate): Fentanyl, Codeine, Dihydrocodeine, Alprazolam, Amitriptyline, Amantadine, Ethanol, Cetirizine 등 중추신경억제 및 진정 작용과 관련된 약물이 다수 포함됨
  - 경미(Minor): Acetaminophen

허가사항의 경고 및 금기 정보는 데이터에 없으므로 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
위십이지장염을 직접 연구한 임상시험이나 문헌이 없고, 확인된 연구는 운동 기능과 내시경 시야 확보에 관한 간접적 근거뿐입니다. 이 약의 효과는 증상 완화에 국한될 것으로 보이며, 질병 조절 근거는 없습니다.

**진행하려면 필요한 것:**
- 위십이지장염 환자를 대상으로 한 증상 개선 임상 근거
- 허가사항(경고·금기) 확보 및 안전성 검토
- 상세한 작용 기전(MOA) 데이터 보충
- 한국 허가 적응증 텍스트 및 시판 상태 확인
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

