---
layout: default
title: Colchicine
parent: 모델 예측만 (L5)
nav_order: 233
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Colchicine: 예측 신규 적응증 열대열 말라리아 (Plasmodium falciparum malaria) (근거 수준 L5). 기존 적응증: 허가 적응증 본문을 확인할 수 없음 (MFDS 허가문서 링크만 제공됨)"
monitor_inn: "COLCHICINE"
predicted_indications: ["Plasmodium falciparum malaria", "dermatofibrosarcoma protuberans"]
---

# Colchicine
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **3** 건
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

# Colchicine: 허가 적응증 확인 불가에서 열대열 말라리아로

## 한 문장 요약

Colchicine은 한국에서 단일제 정제 2건으로 시판 중인 약물이며, 허가 적응증 본문은 링크로만 제공되어 데이터에서 직접 확인하지 못했습니다.
TxGNN 모델은 상위 예측으로 **열대열 말라리아(Plasmodium falciparum malaria)**를 제시했으나, 이를 직접 뒷받침하는 임상시험은 **0건**이고 colchicine을 직접 다룬 문헌도 없습니다. 근거는 사실상 모델 예측뿐입니다.

> 참고: 예측 2순위인 가족성 지중해열(FMF)은 colchicine의 확립된 표준 치료이므로 신규 적응증이라기보다 기존 용법일 가능성이 높습니다. 아래 결론에서 별도로 다룹니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문을 확인할 수 없음 (MFDS 허가문서 링크만 제공됨) |
| 예측 신규 적응증 | 열대열 말라리아 (Plasmodium falciparum malaria) |
| TxGNN 예측 점수 | 99.60% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 2건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 이 보고서에 수집되지 않았습니다. 다만 colchicine은 일반적으로 미세소관(microtubule) 중합을 억제하는 약물로 알려져 있습니다. 열대열 말라리아 원충도 세포골격과 세포분열에 튜불린과 미세소관 역학을 이용하므로, 기전상 일반적인 연결고리는 상정할 수 있습니다.

그러나 이 연결은 매우 일반적인 수준입니다. 검색된 문헌 2편은 colchicine의 항말라리아 효과를 시험한 연구가 아닙니다. 하나는 curcumin이 원충 미세소관을 교란한다는 2013년 전임상 연구이고, 다른 하나는 pfmdr1 유전자를 포유류 세포에 발현시켜 chloroquine 감수성을 본 1994년 연구입니다. 또한 colchicine은 치료역이 좁아, 항기생충 효과를 내는 농도에서 숙주 독성이 문제될 가능성이 있습니다. 0.996이라는 높은 점수는 계산상의 예측일 뿐입니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [23505424](https://pubmed.ncbi.nlm.nih.gov/23505424/) | 2013 | 전임상 (in vitro) | PLoS One | Curcumin이 열대열 말라리아 원충의 미세소관을 교란함. colchicine 자체를 시험한 연구는 아님 |
| [7511206](https://pubmed.ncbi.nlm.nih.gov/7511206/) | 1994 | 전임상 (세포 기반) | Mol Cell Biol | 원충 pfmdr1 발현이 포유류 세포의 chloroquine 감수성을 높임. 다제내성 수송체 연구로, colchicine 효능 자료는 아님 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 198801219 | 콜킨정(콜키신) | 엷은 황색의 원형 정제 | MFDS 허가문서 링크로만 제공되어 본문 확인 불가 |
| 201606824 | 콜키닌정(콜키신) | 엷은 황색의 원형 정제 | MFDS 허가문서 링크로만 제공되어 본문 확인 불가 |

## 안전성 고려사항

허가사항의 경고·금기 본문은 확보되지 않았으므로 안전성 정보는 허가사항을 참조하세요. 아래는 참고용 외부 자료에서 확인된 정보입니다.

- **지식그래프 기반 금기 관련 질환** (허가 문구가 아닌 TxGNN 지식그래프의 약물-질환 금기 연결 기준): 간부전, 혈액질환, 혈소판감소증, 백혈구감소증, 무과립구증, 호중구감소증, 재생불량성 빈혈, 소화성 궤양, 근병증/횡문근융해증, 설사성 질환, 신기능 장애, 급성 요산 신병증 등.
- **약물 상호작용** (총 100건 조회, 일부 예시):
  - 중증도 Major: Aprepitant, Clarithromycin, Eliglustat, Rolapitant, Rosuvastatin, Simvastatin, Cobicistat, Deferiprone
  - 중증도 Moderate: Metronidazole, Cimetidine, Eluxadoline, Miconazole, Tinidazole, Deferasirox, Fostamatinib, Ticagrelor, Chloroquine, Benznidazole, Disulfiram 등
  - 말라리아 맥락에서는 Chloroquine과의 병용이 중등도 상호작용으로 보고되어 있어 주의가 필요합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
열대열 말라리아 예측은 임상시험이 없고 직접적인 전임상 근거도 없는 모델 예측(L5)에 머뭅니다. colchicine의 좁은 치료역과 숙주 독성도 우려됩니다.

**진행하려면 필요한 것:**
- colchicine의 항말라리아 활성을 직접 평가한 in vitro/in vivo 전임상 자료 (원충 IC50와 숙주세포 독성 비교를 통한 치료지수 확인)
- MFDS 허가문서(허가 적응증, 경고, 금기)를 내려받아 확보
- DrugBank에서 작용 기전(MOA) 보완
- **FMF 예측 별도 검토:** 2순위인 가족성 지중해열(상염색체 우성 아형)은 colchicine의 표준 치료로 문헌에서 일관되게 확인됩니다. 다만 근거는 대부분 서술형 리뷰이고 임상시험 데이터는 없으며(L4), 상염색체 우성 아형 매핑 확인이 필요합니다. 한국 허가 적응증에 이미 포함되는지 확인한 뒤 신규 적응증 여부를 판단해야 합니다. 이 항목은 "Hold"가 아니라 연구 과제(Research Question)로 분류됩니다.
- 3순위인 피부섬유육종(dermatofibrosarcoma protuberans)은 임상시험과 문헌이 모두 없고 모델 점수만 있어(L5, Hold) 추가 근거 없이는 진행하지 않는 것이 적절합니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

