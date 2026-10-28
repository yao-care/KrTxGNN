---
layout: default
title: Isoniazid
parent: 모델 예측만 (L5)
nav_order: 439
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-28
description: "Isoniazid: 예측 신규 적응증 결막염 (Conjunctivitis) (근거 수준 L4). 기존 적응증: 결핵 (허가증 원문은 링크 형태로만 제공되어 세부 문구는 확인되지 않음)"
monitor_inn: "ISONIAZID"
predicted_indications: ["conjunctivitis"]
---

# Isoniazid
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **1** 건
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

## Isoniazid: 결핵에서 결막염으로
{: .text-alpha }

## 한 문장 요약

Isoniazid는 결핵 치료에 사용되는 항결핵제로, 한국에서 단일제 및 복합제 형태로 허가·시판되고 있습니다.
TxGNN 모델은 **결막염(Conjunctivitis)**에 효과가 있을 수 있다고 예측하지만, 현재 등록된 **임상시험은 0건**이며 문헌 12편은 대부분 부작용 보고나 결핵 관련 증례로 직접적인 치료 근거로는 부족합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 결핵 (허가증 원문은 링크 형태로만 제공되어 세부 문구는 확인되지 않음) |
| 예측 신규 적응증 | 결막염 (Conjunctivitis) |
| TxGNN 예측 점수 | 0.9936 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 3건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 일반적인 약리학 지식에 따르면 isoniazid는 결핵균에 특이적으로 작용하는 항결핵제입니다. KatG에 의해 활성화된 뒤 InhA를 억제하여 미코liq산(mycolic acid) 합성을 차단합니다.

결막염과의 연관성은 결핵 관련 질환에 한정됩니다. 결핵균 항원에 대한 과민반응인 플릭텐성 각결막염(phlyctenular keratoconjunctivitis)이나 드문 원발성 결막 결핵에서는 기저의 결핵균 감염을 치료·예방하는 방식으로 효과를 낼 수 있습니다. 방광 내 BCG 면역요법 후 발생한 반응성 관절염 및 결막염에도 항미코박테리아 작용을 통해 사용된 사례가 있습니다.

반면 일반적인 세균성, 바이러스성, 알레르기성 결막염에 대한 활성 근거는 없습니다. 검색된 일부 문헌은 isoniazid를 결막염 등 안구 부작용의 원인 가능성으로 다루고 있습니다. 따라서 매우 높은 TxGNN 점수는 계산상의 예측일 뿐, 일반 결막염에 대한 직접적인 임상 근거로 뒷받침되지 않습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

모든 문헌은 증례 보고, 리뷰, 오래된 현장 연구 수준이며 무작위 대조시험(RCT)은 없습니다. 치료 관련성이 있는 문헌을 우선하여 정리했습니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [14253168](https://pubmed.ncbi.nlm.nih.gov/14253168/) | 1965 | 코호트/예방 연구 | Am Rev Respir Dis | 알래스카 에스키모의 플릭텐성 각결막염에 대한 isoniazid 예방 효과 연구 (초록 없음) |
| [10641112](https://pubmed.ncbi.nlm.nih.gov/10641112/) | 1999 | 증례 연구 | Oftalmologia | 결핵성 각결막염 28례, 다수에서 투베르쿨린 반응 양성 및 림프절 결핵 동반 |
| [33607832](https://pubmed.ncbi.nlm.nih.gov/33607832/) | 2021 | 증례 보고 및 문헌고찰 | Medicine | 소아 원발성 부비동 결핵에 동반된 플릭텐성 각결막염 |
| [14089390](https://pubmed.ncbi.nlm.nih.gov/14089390/) | 1964 | 증례 보고 | Arch Ophthalmol | 결막의 원발성 결핵 (초록 없음) |
| [5103251](https://pubmed.ncbi.nlm.nih.gov/5103251/) | 1971 | 미분류 | Ann Oculist | 안구 결핵의 국소 치료에 isoniazid 사용 (초록 없음) |
| [10084171](https://pubmed.ncbi.nlm.nih.gov/10084171/) | 1999 | 증례 보고/증례 시리즈 | Rev Rhum | 방광 내 BCG 요법 후 난치성 관절병증에서 isoniazid의 유용성 |
| [12226788](https://pubmed.ncbi.nlm.nih.gov/12226788/) | 2002 | 증례 보고 | Dtsch Med Wochenschr | BCG 방광 내 주입 후 만성 반응성 관절염 및 결막염 |
| [1363080](https://pubmed.ncbi.nlm.nih.gov/1363080/) | 1992 | 리뷰 (부작용) | Optom Clin | 전신 약물의 안구 부작용 정리, 치료 근거 아님 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 199700049 | 신풍이소니아짓정(수출용) | 백색의 원형 정제 | 허가사항 참조 (수출용) |
| 198700084 | 리포믹스캅셀(리팜피신, 이소니코틴산히드라짓캅셀)(수출용) | 캡슐 (상의 흑색, 하의 주황색) | 허가사항 참조 (수출용) |
| 196200032 | 유한짓정100mg(이소니아지드) | 백색 원형 정제 | 허가사항 참조 |

## 안전성 고려사항

허가사항의 경고 및 금기 정보는 이번 자료에 포함되지 않았으므로 허가사항을 참조하세요.

- **지식그래프상 금기 관련 질환** (허가 문구가 아닌 TxGNN 지식그래프 기반): 간부전, 급성 간부전, 간질환, 간염, 포르피린증(유전성 포함), 담낭질환, 당뇨병, 당뇨병성 케토산증, 통풍, 말초신경계 질환, 말초신경병증, 약물 남용/의존, 느린 아세틸화(slow acetylation).
- **약물 상호작용**: 총 100건이 조회되었으며, 이 중 확인된 일부는 다음과 같습니다.
  - 중등도: acarbose, albiglutide, alogliptin, metformin, pioglitazone, canagliflozin, dapagliflozin, chlorpropamide 등 혈당강하제, cholecalciferol, calcifediol, calcitriol 등 비타민 D 계열, metronidazole, alosetron, budesonide, picosulfuric acid
  - 경미: hydrocortisone, triamcinolone, dexamethasone, betamethasone 등 코르티코스테로이드

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 점수는 높지만 임상시험이 없고, 문헌은 결핵 관련 결막염 증례와 부작용 보고에 한정되어 근거 수준이 L4에 그칩니다. 일반 결막염에 대한 치료 효과를 시사하는 직접 근거가 없으며 간독성·신경병증 등 전신 안전성 우려도 있어 보류가 타당합니다.

**진행하려면 필요한 것:**
- 허가증 PDF에서 허가 적응증, 경고, 금기 정보 확보 (현재는 링크만 있어 안전성 선별 불가)
- 상세한 작용 기전(MOA) 데이터 확보
- 결핵성(플릭텐성) 각결막염 등 범위를 좁힌 적응증 설정 및 현대 연구 근거 확인
- 안과 국소 투여 등 투여 경로 적합성 검토 (현재 한국 허가 제형은 모두 경구제)
- 안구 질환 환자에 대한 전신 안전성(간독성, 말초신경병증) 및 약물 상호작용 평가
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

