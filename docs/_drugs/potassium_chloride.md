---
layout: default
title: Potassium Chloride
parent: 僅模型預測 (L5)
nav_order: 566
evidence_level: L5
indication_count: 1
---

# Potassium Chloride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Potassium Chloride: 저칼륨혈증 전해질 보충에서 신세뇨관성 산증으로

## 한 문장 요약

Potassium Chloride(염화칼륨)는 저칼륨혈증 교정에 사용되는 전해질 보충제입니다.
TxGNN 모델은 **신세뇨관성 산증(Renal Tubular Acidosis)**에 효과가 있을 것으로 예측했으나(예측 점수 **99.87%**),
검토된 **9건의 임상시험**과 **20편의 문헌** 중 염화칼륨을 RTA 치료제로 직접 연구한 사례는 하나도 없으며,
오히려 기전상 우려가 제기되는 상황입니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정보 없음 (한국 허가 데이터 없음; 일반적으로 저칼륨혈증 전해질 보충제로 알려짐) |
| 예측 신규 적응증 | 신세뇨관성 산증 (Renal Tubular Acidosis) |
| TxGNN 예측 점수 | 99.87% |
| 근거 수준 | L5 (모델 예측만 있음, 실제 관련 연구 없음) |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터가 없습니다(DrugBank 조회 필요, DG002). 다만 일반적으로 알려진 정보에 따르면
Potassium Chloride는 칼륨 이온을 공급하는 전해질 보충제로, 저칼륨혈증 교정에 널리 사용됩니다.

TxGNN이 산출한 99.87%의 높은 점수는 "**RTA 환자에서 저칼륨혈증이 흔히 동반되어 칼륨 보충이 필요하다**"는
**증상 차원의 연관성**을 반영한 것으로 보이며, KCl이 RTA의 병리 기전을 직접 치료한다는 근거는 아닙니다.
RTA(특히 제1형 원위 RTA)의 핵심 병리는 신세뇨관의 산 배출/중탄산염 재흡수 장애로 인한 고염소성 대사성
산혈증이며, 표준 치료는 알칼리제(중탄산나트륨 또는 구연산칼륨)입니다. 구연산칼륨은 칼륨과 알칼리를
동시에 공급하지만, KCl은 칼륨만 공급하고 알칼리는 공급하지 않으며 추가되는 염소 이온은 이론적으로
고염소성 산혈증을 악화시킬 수 있습니다.

**결론적으로 이 연관성은 "질환 치료"가 아니라 "동반 증상(저칼륨혈증) 대증 처치"로 해석해야 하며,
기전적 연결고리는 약합니다.**

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT03644706](https://clinicaltrials.gov/study/NCT03644706) | Phase 3 | 종료(조기중단) | 3 | dRTA 대상 ADV7103(KCl 아님) 평가, 3명만 등록 후 중단, 근거력 매우 낮음 |
| [NCT00120731](https://clinicaltrials.gov/study/NCT00120731) | N/A | 철회 | 0 | 소아 고칼슘뇨증에서 구연산칼륨(potassium citrate) 연구, KCl과 약리학적으로 다름 |
| [NCT06750172](https://clinicaltrials.gov/study/NCT06750172) | N/A | 모집 중 | 33 | 원발성 알도스테론증 진단법 연구, KCl-RTA 치료와 무관 |
| [NCT07273838](https://clinicaltrials.gov/study/NCT07273838) | Phase 2 | 모집 중 | 130 | SGLT2 억제제와 심신증후군 연구, KCl과 무관 |
| [NCT01834768](https://clinicaltrials.gov/study/NCT01834768) | Phase 2 | 불명 | 31 | Eplerenone 안전성 연구, KCl과 무관 |
| [NCT01843309](https://clinicaltrials.gov/study/NCT01843309) | Phase 4 | 종료(조기중단) | 36 | Spironolactone으로 Amphotericin B 유발 전해질 이상 예방, KCl과 무관 |
| [NCT01894594](https://clinicaltrials.gov/study/NCT01894594) | Phase 1 | 종료(조기중단) | 7 | 겸상적혈구병에서 알칼리 요법(중탄산염 계열 추정) 평가, KCl 아님 |
| [NCT06867471](https://clinicaltrials.gov/study/NCT06867471) | N/A | 모집 중 | 43 | 외인성 케톤체가 만성신질환 단백뇨에 미치는 영향, KCl과 무관 |
| [NCT03354507](https://clinicaltrials.gov/study/NCT03354507) | N/A | 불명 | 40 | Topiramate 관련 산혈증에서 중탄산나트륨 사용, KCl 아님 |

**주의**: 위 9건 모두 Potassium Chloride를 RTA 치료제로 직접 평가한 시험이 아닙니다. 대부분 다른 약물(구연산칼륨, 중탄산나트륨, SGLT2 억제제 등)을 다루거나 KCl과 무관한 주제입니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [33459628](https://pubmed.ncbi.nlm.nih.gov/33459628/) | 2021 | Review (Tier 2) | Arch Esp Urol | dRTA와 신결석 진단/관리 개관, 표준 치료는 알칼리제(구연산칼륨 등) |
| [21314872](https://pubmed.ncbi.nlm.nih.gov/21314872/) | 2011 | Review (Tier 2) | Int J Clin Pract | 성인 RTA에 대한 임상 접근법, 근위/원위 RTA 유형별 치료 개관 |
| [17297212](https://pubmed.ncbi.nlm.nih.gov/17297212/) | 2007 | Review | Acta Med Indones | 저칼륨혈증 접근법 개관, 신장/신장외 손실 원인 감별 |
| [8694660](https://pubmed.ncbi.nlm.nih.gov/8694660/) | 1996 | Review | Arch Intern Med | RTA 병태생리 및 진단 개관 |
| [20228475](https://pubmed.ncbi.nlm.nih.gov/20228475/) | 2010 | Case Report | Neurol India | 호흡마비로 발현한 dRTA 증례, 중탄산나트륨 + 칼륨 보충으로 호전 |
| [34748193](https://pubmed.ncbi.nlm.nih.gov/34748193/) | 2022 | Case Report | J Nephrol | 임신 중 dRTA와 저칼륨성 주기성마비 증례 |
| [38445406](https://pubmed.ncbi.nlm.nih.gov/38445406/) | 2023 | Cohort | La Tunisie Med | 튀니지 dRTA 환자의 유전형-표현형 상관관계 |
| [783200](https://pubmed.ncbi.nlm.nih.gov/783200/) | 1976 | Cohort | J Clin Invest | 제1형 RTA에서 경구 중탄산칼륨으로 산혈증 교정, 나트륨 보존 장애 평가 |
| [37081692](https://pubmed.ncbi.nlm.nih.gov/37081692/) | 2023 | Review | Endocr J | PHA2를 제4형 RTA로 분류하는 문헌고찰 |
| [25377117](https://pubmed.ncbi.nlm.nih.gov/25377117/) | 2014 | Review | Nephron Physiol | 미네랄로코르티코이드가 산-염기 균형에 미치는 영향 |

**주의**: 위 문헌은 모두 RTA 자체 또는 관련 병태생리를 다루지만, **Potassium Chloride를 RTA 치료 약물로 직접 연구한 문헌은 없습니다**. 실제 치료로 언급되는 것은 중탄산나트륨, 구연산칼륨 등 알칼리를 포함한 제제입니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. (TFDA 라벨/경고·금기 정보 미확보 — DG001, Blocking)

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- TxGNN 예측 점수는 높지만(99.87%), 검토된 임상시험·문헌 중 Potassium Chloride를 RTA 치료제로 직접 연구한 사례가 전무합니다(근거 수준 L5).
- 기전 분석 결과, 이 예측은 "RTA에 저칼륨혈증이 동반되어 칼륨 보충이 필요하다"는 증상 연관성에 불과하며, KCl은 RTA의 핵심 병리(산 배출 장애)를 교정하지 못하고 오히려 염소 부하로 고염소성 산혈증을 악화시킬 이론적 우려가 있습니다.
- 한국 내 허가 정보(licenses=0건, 미시판)와 TFDA 경고/금기 데이터가 없어 안전성 초기평가(S1)조차 진행할 수 없습니다(DG001, Blocking).

**진행하려면 필요한 것:**
- TFDA(또는 국내 규제기관) 라벨 PDF 확보 및 경고·금기 정보 파싱 (DG001 해소)
- DrugBank API를 통한 상세 작용기전(MOA) 확인 (DG002 해소)
- Potassium Chloride(구연산칼륨이 아닌)를 RTA 또는 병발 저칼륨혈증 관리에 사용한 실제 임상 데이터/증례 확보
- 알칼리제 병용 여부 및 염소 부하에 따른 산혈증 악화 위험에 대한 별도 안전성 검토
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

