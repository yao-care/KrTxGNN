---
layout: default
title: Ofloxacin
parent: 僅模型預測 (L5)
nav_order: 516
evidence_level: L5
indication_count: 10
---

# Ofloxacin
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

# Ofloxacin: 세균 감염증에서 패혈성 흑사병(Septicemic Plague)으로

## 한 문장 요약

Ofloxacin은 fluoroquinolone 계열 항생제로, 세균 감염증 치료에 사용되어 온 약물입니다. TxGNN 모델은 10개의 신규 적응증을 예측했지만, 이 중 7개(고아밀라아제혈증, 다클론성 과점도증후군 등 순위 상위권 다수)는 임상시험·문헌 근거가 전무하여 임베딩 편향에 의한 허위 양성으로 판단됩니다. 실제로 근거 수준이 가장 높은 예측은 **패혈성 흑사병(Septicemic Plague)**이며, 동일 계열 약물(ciprofloxacin, levofloxacin)이 이미 FDA Animal Rule 경로로 페스트 치료 적응증을 획득했다는 점에서 기전적·실증적 타당성이 확인됩니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 세균 감염증 (Fluoroquinolone계 항생제 — 상세 허가 적응증 데이터 없음) |
| 예측 신규 적응증 | 패혈성 흑사병 (Septicemic Plague) |
| TxGNN 예측 점수 | 99.79% (원 순위 8위, score 0.99791) |
| 근거 수준 | L3 |
| 한국 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

## ⚠️ TxGNN 예측 순위에 대한 주의사항

이 Evidence Pack의 TxGNN 순위 1~3위, 5위, 7위, 9위 예측(고아밀라아제혈증, 다클론성 과점도증후군, 선천성 무알부민혈증, 조혈계통 전악성질환, 후천성 말초신경병증 관련 혈액질환, 선천성 혈액질환)은 **임상시험·문헌·기전 근거가 전혀 없으며**, 각 예측의 rationale에도 "생물학적 타당성 佐證 없음", "임베딩 층위 유사 질환군 집적에 의한 偽相관 의심"이라고 명시되어 있습니다. 이는 TxGNN score만으로 적응증을 판단할 수 없다는 것을 보여주는 사례이므로, 본 보고서는 **실제 근거가 존재하는 예측(패혈성 흑사병)**을 중심으로 평가합니다. 다른 예측들은 하단 "전체 예측 적응증 요약"을 참고하십시오.

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터는 확보되어 있지 않습니다. 다만 일반적으로 알려진 바에 따르면, ofloxacin은 fluoroquinolone계 항생제로서 세균의 DNA gyrase 및 topoisomerase IV를 억제하여 DNA 복제를 차단하는 방식으로 항균 작용을 나타냅니다.

패혈성 흑사병의 원인균인 *Yersinia pestis*는 그람음성균으로, fluoroquinolone계 항생제에 대한 감수성이 실험적으로 확인되어 있습니다. 실제로 같은 계열의 ciprofloxacin과 levofloxacin은 인체 대상 RCT가 윤리적으로 불가능한 페스트에 대해 FDA의 Animal Efficacy Rule(동물모델 기반 승인 경로)을 통해 치료·노출 후 예방 적응증을 획득했습니다.

Ofloxacin 자체도 초기 동물모델 연구(1994, 2002)에서 페스트균에 대한 항균 활성 및 생체 내 방어 효과가 보고되어 있어, 동일 계열 내 항균 스펙트럼 확장 적용으로서 기전적 타당성이 있습니다. 다만 이는 완전히 새로운 기전을 발견한 것이 아니라 기존 항균 작용의 적용 범위 확장에 해당합니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다. (페스트는 발생 빈도가 낮고 인체 대상 RCT가 윤리적으로 어려워, 근거는 동물모델 연구 및 FDA Animal Rule 승인 자료에 의존합니다.)

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [32435803](https://pubmed.ncbi.nlm.nih.gov/32435803/) | 2020 | 동물모델/규제검토 | Clin Infect Dis | 아프리카녹색원숭이 폐페스트 모델 기반 FDA Animal Rule 항균제 승인 경과 |
| [16127904](https://pubmed.ncbi.nlm.nih.gov/16127904/) | 2002 | 동물모델 | Antibiotiki i khimioterapiia | Ofloxacin이 항원 결손·완전 페스트균주 실험감염에서 예방·치료 효과 확인 |
| [8203841](https://pubmed.ncbi.nlm.nih.gov/8203841/) | 1994 | 동물모델 | Antimicrob Agents Chemother | Ofloxacin 포함 다수 항생제의 마우스 전신 페스트 감염 치료 효능 비교 |
| [21347450](https://pubmed.ncbi.nlm.nih.gov/21347450/) | 2011 | 동물모델 | PLoS Negl Trop Dis | Levofloxacin이 영장류 모델에서 폐페스트를 완치시킴 (동일 계열 근거) |
| [32435805](https://pubmed.ncbi.nlm.nih.gov/32435805/) | 2020 | 동물모델 | Clin Infect Dis | Ciprofloxacin·Levofloxacin의 치료 개시 지연에 따른 효능 변화 |
| [21127743](https://pubmed.ncbi.nlm.nih.gov/21127743/) | 2010 | 동물모델 | Open Microbiol J | Fluoroquinolone계 항생제의 페스트·탄저·야토병 호흡기 감염 방어 효과 |
| [9517950](https://pubmed.ncbi.nlm.nih.gov/9517950/) | 1998 | 동물모델 | Antimicrob Agents Chemother | 마우스 폐페스트 모델에서 항생제 치료 효능 평가 |
| [17517837](https://pubmed.ncbi.nlm.nih.gov/17517837/) | 2007 | 동물모델 | Antimicrob Agents Chemother | Streptomycin 대비 Levofloxacin의 내성 선택 및 치료 효능 비교 |
| [10987101](https://pubmed.ncbi.nlm.nih.gov/10987101/) | 2000 | 동물모델 | Antibiotiki i khimioterapiia | Ofloxacin 등 fluoroquinolone 병용 긴급예방과 백신 병행 효과 검증 |
| [37748767](https://pubmed.ncbi.nlm.nih.gov/37748767/) | 2023 | Review | Am J Trop Med Hyg | 2010년대 이후 전세계 페스트 발생 현황 및 역학 개관 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. (본 Evidence Pack에는 경고·금기·DDI 데이터가 확보되지 않았으며, 이는 아래 결론의 Blocking 데이터 갭에 해당합니다.)

## 전체 예측 적응증 요약 (참고)

| 순위 | 예측 적응증 | TxGNN 점수 | 근거 수준 | 권장 |
|------|-----------|-----------|----------|------|
| 1 | 고아밀라아제혈증 | 99.91% | L5 | Hold |
| 2 | 다클론성 과점도증후군 | 99.91% | L5 | Hold |
| 3 | 선천성 무알부민혈증 | 99.90% | L5 | Hold |
| 4 | 혈액형 부적합 | 99.86% | L4 | Hold |
| 5 | 조혈계통 전악성질환 | 99.84% | L5 | Hold |
| 6 | 단클론감마글로불린병증 | 99.82% | L3 | Research Question |
| 7 | 후천성 말초신경병증 동반 혈액질환 | 99.80% | L5 | Hold |
| **8** | **패혈성 흑사병** | **99.79%** | **L3** | **Proceed with Guardrails** |
| 9 | 선천성 혈액질환 | 99.72% | L5 | Hold |
| 10 | 점상 상피성 각결막염 | 99.57% | L4 | Research Question |

*순위 6(단클론감마글로불린병증)의 근거는 ofloxacin이 아닌 levofloxacin(TEAMM 시험, 골수종 환자 감염 예방)에 기반하므로 약물 특이성 검증이 필요합니다. 순위 10(점상 상피성 각결막염)의 문헌은 미포자충·알레르기성 병인으로 ofloxacin 항균 기전과 직접 대응하지 않아 간접 근거로 분류됩니다.

## 결론 및 다음 단계

**결정: Proceed with Guardrails** (패혈성 흑사병 적응증 기준)

**사유:**
동일 계열 약물(ciprofloxacin, levofloxacin)이 FDA Animal Rule을 통해 페스트 치료·예방 적응증을 획득했고, ofloxacin 자체도 동물모델에서 항균 활성이 확인되어 기전적 타당성은 충분합니다. 다만 ofloxacin 특이적 근거는 levofloxacin/ciprofloxacin에 비해 상대적으로 오래되고 제한적이며, 인체 임상자료가 전무합니다.

**진행하려면 필요한 것:**
- TFDA/식약처 수준의 허가 경고·금기·DDI 데이터 확보 (현재 Blocking 데이터 갭, S1 안전성 초평가 진입 불가)
- 상세 작용기전(MOA) 데이터 확보 (DrugBank API 조회)
- Ofloxacin과 levofloxacin/ciprofloxacin 간 항균 스펙트럼·PK 차이에 대한 문헌 비교 검토
- 순위 6(단클론감마글로불린병증), 10(점상 각결막염)은 Research Question 단계로 별도 추적 필요
- 순위 1·2·3·5·7·9는 근거 부재로 현 단계에서 추가 조사 불필요 (Hold 유지)
- 한국 내 시판 계획 시 정식 허가 신청 경로 확인 (현재 미출시, 허가증 0건)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

