---
layout: default
title: Molsidomine
parent: 僅模型預測 (L5)
nav_order: 489
evidence_level: L5
indication_count: 10
---

# Molsidomine
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

# Molsidomine: 협심증(관상동맥질환)에서 혈관질환(Vascular Disease)으로

## 한 문장 요약

Molsidomine은 해외(유럽·아시아)에서 협심증·관상동맥질환 치료에 사용되어 온 일산화질소(NO) 공여체 계열 혈관확장제입니다. TxGNN 모델은 **혈관질환(Vascular Disease)**에 효과가 있을 것으로 예측하며, 현재 **2건의 임상시험**과 **20편의 문헌**이 이 방향을 지지합니다. 다만 이 예측은 완전히 새로운 영역이라기보다 기존에 알려진 적응증(협심증/관상동맥질환)이 더 넓은 범주로 재확인된 성격에 가깝습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 협심증/관상동맥질환 (해외 사용 근거, 한국 미허가 — 문헌 기반) |
| 예측 신규 적응증 | 혈관질환 (Vascular Disease) |
| TxGNN 예측 점수 | 99.9999% |
| 근거 수준 | L1 |
| 한국 시판 현황 | 미상 시판 (허가 없음) |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

Molsidomine은 sydnonimine 계열의 NO 공여 전구약물로, 간에서 대사되어 활성대사체 SIN-1이 되고 NO를 방출합니다. 이 NO가 혈관(특히 정맥 및 관상동맥) 평활근을 이완시켜 전부하를 낮추고 심근 허혈을 개선하는 것이 핵심 기전입니다(PMID 2242448, 8743336).

기존 적응증인 협심증/관상동맥질환과 예측된 신규 적응증 '혈관질환'은 사실상 같은 병태생리 범주에 속합니다. Evidence pack의 재창출 근거에서도 "이 적응증은 본질적으로 유럽/아시아에서 기존에 승인된 용도(협심증/관상동맥질환)이며, 진정한 의미의 신규 재창출이라기보다 '기존 용도의 재확인'에 해당한다"고 명시하고 있어, 기전상 타당성은 높지만 참신성은 제한적입니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01363661](https://clinicaltrials.gov/study/NCT01363661) | Phase 4 | 완료 | 165 | 안정형 협심증 환자에서 PCI 시행 후 12개월간 molsidomine 병용요법이 내피기능(RH-PAT 지표)을 위약 대비 개선하는지 평가한 이중맹검 무작위대조시험 |
| [NCT00382421](https://clinicaltrials.gov/study/NCT00382421) | N/A | 완료 | N/A | SWISSI 1 연구 — 무증상 심근허혈 환자에서 항협심증 약물요법(molsidomine 포함)과 위험인자 관리의 장기 예후 평가 개입 연구 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [9475269](https://pubmed.ncbi.nlm.nih.gov/9475269/) | 1998 | RCT (crossover) | J Cardiovasc Pharmacol | 안정형 협심증 90명 대상 다기관 이중맹검 위약대조 교차시험, molsidomine retard가 운동수행능력과 ST분절 하강을 유의하게 개선 |
| [2598982](https://pubmed.ncbi.nlm.nih.gov/2598982/) | 1989 | RCT | Eur J Clin Pharmacol | 관상동맥질환 24명에서 nifedipine 대비 molsidomine의 혈역학적 효과 비교, 폐동맥압·좌심실이완기말압 유의 감소 |
| [8438599](https://pubmed.ncbi.nlm.nih.gov/8438599/) | 1993 | Clinical Study (RCT-like) | Wien Klin Wochenschr | 말초동맥질환 20명에서 prostacyclin과 molsidomine 병용 시 섬유소용해·항혈소판 작용의 상승효과 확인 |
| [2651251](https://pubmed.ncbi.nlm.nih.gov/2651251/) | 1989 | RCT (crossover) | Fortschr Med | 관상동맥질환 20명 무작위 교차시험, gallopamil과 molsidomine 모두 뚜렷한 항허혈 효과, ST분절 하강 유의 감소 |
| [3665944](https://pubmed.ncbi.nlm.nih.gov/3665944/) | 1987 | Clinical Study | Eur Heart J | 관상동맥질환 11명 대상, molsidomine 급성·만성 투여 시 폐동맥압 및 운동능력에 미치는 효과와 내성 발생 여부 평가 |
| [6893896](https://pubmed.ncbi.nlm.nih.gov/6893896/) | 1981 | Clinical Study | Am J Cardiol | 운동유발 협심증 10명에서 molsidomine 정맥투여 후 안정시·운동시 혈역학적 효과 분석 |
| [6393621](https://pubmed.ncbi.nlm.nih.gov/6393621/) | 1984 | RCT (dose-response) | Z Kardiol | 관상동맥질환 12명 무작위 이중맹검 급성시험, 2/4/6mg 용량별 허혈성 ST분절 하강 감소 효과 및 지속시간 평가 |
| [11082214](https://pubmed.ncbi.nlm.nih.gov/11082214/) | 2000 | Review | Proc Soc Exp Biol Med | NO 공여체 전반의 약리학적 특성 고찰, 심근경색·혈소판기능·혈관신생에 대한 작용 정리 |
| [8743336](https://pubmed.ncbi.nlm.nih.gov/8743336/) | 1996 | PK Study | Clin Pharmacokinet | Molsidomine의 임상약동학 리뷰 — 빠른 흡수·가수분해, 경구 생체이용률 44–59% |
| [2242448](https://pubmed.ncbi.nlm.nih.gov/2242448/) | 1990 | Overview | Blood Vessels | 관상동맥질환 치료제로서 확립된 molsidomine의 SIN-1/NO 방출 기전 및 내성 현상 개관 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
관상동맥질환/협심증에 대한 molsidomine의 NO 공여 기전은 다수의 RCT와 완료된 Phase 4 시험(NCT01363661, 내피기능 개선)으로 뒷받침되어 근거 수준 L1으로 평가됩니다. 다만 이는 기존에 알려진 적응증의 재확인 성격이 강하고, 안전성 정보(경고·금기·DDI)가 전혀 확보되지 않아(DG001, Blocking) 안전성 초평가(S1) 진입이 불가능한 상태입니다.

**진행하려면 필요한 것:**
- 허가 당국 공식 경고·금기 정보 확보 (DG001, Blocking — S1 안전성 초평가 진입 필수조건)
- DrugBank 기반 공식 작용기전(MOA) 데이터 확보 (DG002, High)
- 한국 내 허가/시판 현황 확인 (현재 미상 시판, 허가 0건)
- 약물상호작용(DDI) 데이터베이스 재조회 (현재 not_found)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

