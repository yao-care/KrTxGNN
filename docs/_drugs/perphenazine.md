---
layout: default
title: Perphenazine
parent: 높은 근거 (L1-L2)
nav_order: 545
evidence_level: L2
indication_count: 10
---

# Perphenazine
{: .fs-9 }

근거 수준: **L2** | 예측 적응증: **10** 건
{: .fs-6 .fw-300 }

---

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 약사 평가 보고서

</div>

# Perphenazine: 항정신병 치료에서 불안장애로

> **참고**: TxGNN 원시 점수 기준 1~9위 예측(망막 이영양증, 증후군성 근시, 다소뇌회증 등 초희귀 선천성 질환)은 각 항목의 `repurposing_rationale`에서 "무합리 기전 연결", "KG embedding 공현 잡음"으로 명시적으로 배제되어 근거 수준 L5·권장 Hold로 판정되었습니다. 이에 본 보고서는 실제 임상시험·문헌 근거가 존재하는 **10위 예측(불안장애, L2/S2/Research Question)**을 평가 대상으로 삼았습니다.

## 한 문장 요약

Perphenazine은 페노티아진(phenothiazine)계 전형적 항정신병약물로, 도파민 D2 수용체 길항 작용을 주 기전으로 하며 정신병적 증상 치료에 사용되어 온 약물입니다. 다만 이번 Evidence Pack에는 공식 원 적응증 및 한국(또는 조사 대상국) 허가 정보가 존재하지 않습니다(미시판). TxGNN 모델은 **불안장애(Anxiety Disorder)**에도 효과가 있을 수 있다고 예측하며, 현재 **2건의 임상시험**과 **20편의 문헌**(이 중 다수가 perphenazine 병용요법을 직접 다룬 연구)이 이 방향을 뒷받침합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (허가 정보 없음; 약물 분류상 전형적 항정신병약물) |
| 예측 신규 적응증 | 불안장애 (Anxiety Disorder) |
| TxGNN 예측 점수 | 99.53% |
| 근거 수준 | L2 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터는 공식적으로는 [Data Gap]으로 표시되어 있습니다. 다만 근거 자료의 재창출 근거 설명에 따르면, Perphenazine은 페노티아진계 전형적 항정신병약물로 도파민 D2 수용체 길항이 주 기전이며, 부가적으로 α-아드레날린 및 히스타민 H1 수용체 길항 활성을 가져 진정(sedation) 효과를 나타냅니다.

1960년대에는 amitriptyline과의 복합제(Triavil®)로 "불안 동반 우울증(anxious-depressed)" 치료에 실제 사용된 이력이 있습니다. 이는 단순한 데이터베이스 외삽이 아니라 역사적으로 확립되었으나 현재는 임상에서 거의 쓰이지 않게 된 적응증입니다. 저용량 항정신병약물을 난치성 불안장애에 보조적으로 사용하는 것은 변연계 과흥분을 억제한다는 약리학적 근거도 일부 뒷받침합니다.

다만 관련 근거 대부분이 1950~70년대 문헌으로, 현대적 방법론(이중맹검 위약대조, 대규모 표본)을 갖춘 최신 연구가 부족하며, 해당 복합제 자체가 현재는 단종된 상태라는 한계가 있습니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT05646693](https://clinicaltrials.gov/study/NCT05646693) | Phase 2 | 상태 불명 (UNKNOWN) | 58 | 만성 이명 환자에서 항산화제 복합요법(Adepsique®: amitriptyline+perphenazine+diazepam)이 염증/산화스트레스 지표에 미치는 영향 평가. 불안장애 자체를 1차 목적으로 하지 않음 |
| [NCT02374567](https://clinicaltrials.gov/study/NCT02374567) | Phase 3 | 조기 종료 (TERMINATED) | 407 | 노인 정신과 입원환자 대상 향정신성 약물 치료의 안전성 및 이상반응 발생률 조사(약물감시 목적, 불안장애 유효성 평가 아님) |

두 시험 모두 perphenazine을 포함하나 불안장애 치료 효능을 직접 검증하는 시험은 아니며, 간접적 근거로만 활용 가능합니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [4867598](https://pubmed.ncbi.nlm.nih.gov/4867598/) | 1968 | RCT (이중맹검) | Psychosomatics | 신체 질환에 동반된 정신적 장애 치료: perphenazine-amitriptyline 병용의 불안·우울 개선 효과 |
| [13726172](https://pubmed.ncbi.nlm.nih.gov/13726172/) | 1961 | RCT | Am J Psychiatry | 신경증 및 과잉행동 아동에서 정신치료 단독 대비 perphenazine 병용 효과 비교 |
| [14401911](https://pubmed.ncbi.nlm.nih.gov/14401911/) | 1959 | RCT | J Ment Sci | 불안·우울 외래환자에서 perphenazine, sodium amylobarbitone, 위약 비교 |
| [14249358](https://pubmed.ncbi.nlm.nih.gov/14249358/) | 1964 | 임상연구 | J Med Assoc Georgia | 복합 우울-불안 환자에서 amitriptyline+perphenazine 병용요법 |
| [4886995](https://pubmed.ncbi.nlm.nih.gov/4886995/) | 1969 | 임상연구 (이중맹검) | Dis Nerv Syst | 정신병적/정신신경증적 우울증에서 thiothixene 대 perphenazine-amitriptyline 비교 |
| [4554486](https://pubmed.ncbi.nlm.nih.gov/4554486/) | 1972 | 대조 연구 | Psychopharmacologia | 혼합 불안-우울 신경증 외래환자에서 doxepin 대 amitriptyline-perphenazine 비교 |
| [13687810](https://pubmed.ncbi.nlm.nih.gov/13687810/) | 1960 | 임상연구 | Rassegna Studi Psichiatrici | 신경증 및 우울 증후군 치료에서 perphenazine의 증상학적 소견 |
| [17017818](https://pubmed.ncbi.nlm.nih.gov/17017818/) | 2006 | Review | J Clin Psychiatry | 전형/비전형 항정신병약물의 1차 및 동반 불안 증상/장애에 대한 효능 종설 |
| [13405719](https://pubmed.ncbi.nlm.nih.gov/13405719/) | 1957 | 예비 보고 | J Am Geriatr Soc | 고령자의 불안, 초조, 흥분 치료에서 perphenazine(trilafon) 사용 |
| [14149372](https://pubmed.ncbi.nlm.nih.gov/14149372/) | 1964 | Review/Commentary | Psychosomatics | 스트레스 및 불안 관리에서 페노티아진계 약물의 역할 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

(TFDA/관할 규제기관 경고·금기 사항 및 DDI 데이터가 확보되지 않은 Blocking Data Gap이 존재합니다.)

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
불안장애에 대한 근거는 1950~70년대의 RCT 및 임상연구(L2 수준)로 구성되어 있으나, 이는 현재 단종된 복합제(Triavil: perphenazine+amitriptyline)를 기반으로 한 것으로 현대적 방법론에 따른 재현 연구가 전무합니다. 또한 규제기관 경고/금기 사항 및 상세 작용기전(MOA) 데이터가 완전히 결여되어 있어(Blocking severity) 안전성 초기 평가(S1) 단계에 진입할 수 없으며, 해당 지역에는 현재 미시판 상태입니다.

**진행하려면 필요한 것:**
- TFDA(또는 관할 규제기관) 공식 경고·금기 사항 확보 (DG001, Blocking)
- DrugBank 기반 상세 작용기전(MOA) 데이터 확보 (DG002, High)
- 현대적 기준의 불안장애 대상 대조 임상시험 설계 검토 (기존 근거가 노후화된 병용요법 기반이므로)
- 국내(관할지역) 허가 및 시판 가능성 사전 검토 (현재 허가증 0건)
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

