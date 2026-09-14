---
layout: default
title: Treprostinil
parent: 僅模型預測 (L5)
nav_order: 699
evidence_level: L5
indication_count: 10
---

# Treprostinil
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

# Treprostinil: 폐동맥고혈압(PAH)에서 다수의 PAH 아형(선천성 심장병 동반·결합조직질환 동반 등)으로

## 한 문장 요약

Treprostinil은 합성 prostacyclin(PGI2) 유사체로, 국제적으로 원발성(특발성) 폐동맥고혈압(WHO Group 1 PAH) 치료에 사용되어 온 약물입니다. TxGNN은 총 10개의 신규 적응증 후보를 예측했으나, **최고 순위 후보(폐동정맥기형, 99.70%)는 근거 재검토 결과 KG 임베딩 유사도로 인한 위양성 가능성이 높다고 판단**되며, 실제로 임상시험·문헌 근거가 뒷받침하는 후보는 **선천성 심장병 동반 PAH**와 **결합조직질환 동반 PAH**(각 L2, Proceed with Guardrails)입니다. 다만 한국에는 현재 허가된 제품이 없고(미시판), 라벨 안전성 정보가 Blocking 등급 데이터 갭(DG001)으로 남아 있어 약물 수준에서 안전성 초기 평가(S1)조차 진행할 수 없는 상태입니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 특발성/원발성 폐동맥고혈압(PAH, WHO Group 1) — *국내 허가 자료 없음, 문헌 근거 기반* |
| TxGNN 최고 순위 예측 | 폐동정맥기형 (Pulmonary AVM) — **위양성 가능성 높음** (하단 "타당성" 참조) |
| TxGNN 예측 점수 (최고 순위) | 99.70% |
| 근거가 실제로 뒷받침하는 후보 | 선천성 심장병 동반 PAH, 결합조직질환 동반 PAH |
| 근거 수준 | L5 (최고 순위 후보) / **L2** (선천성 심장병·결합조직질환 동반 PAH) |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | **Hold** (약물 수준 Blocking 데이터 갭) / 개별 적응증은 하단 참조 |

---

## 전체 예측 후보 개요

| 순위 | 예측 적응증 | TxGNN 점수 | 근거 수준 | 권장 |
|------|-----------|-----------|----------|------|
| 1 | 폐동정맥기형 (Pulmonary AVM) | 99.70% | L5 | Hold *(위양성 의심)* |
| 2 | 선천성 심장병 동반 PAH | 99.60% | L2 | Proceed with Guardrails |
| 3 | 주혈흡충증 동반 PAH | 99.55% | L5 | Hold (근거 전무) |
| 4 | 결합조직질환 동반 PAH | 99.55% | L2 | Proceed with Guardrails |
| 5 | HIV 감염 동반 PAH | 99.55% | L3 | Research Question |
| 6 | 만성 용혈성 빈혈 동반 PAH | 99.55% | L5 | Hold (근거 전무) |
| 7 | 두피 단순 저모증 | 99.48% | L5 | Hold *(기전 무관, 위양성 의심)* |
| 8 | 선천성 저모증-밀리아 | 99.30% | L5 | Hold *(기전 무관)* |
| 9 | 치아/치주 기형 증후군 | 99.21% | L5 | Hold *(문헌이 치주염 일반 연구로 무관)* |
| 10 | Ambras형 선천성 전신 다모증 | 99.17% | L5 | Hold *(기전 무관)* |

> 순위 1, 7~10은 TxGNN score는 높지만 각 후보의 **repurposing_rationale 자체가 기전상 무관하거나 KG 노이즈일 가능성을 명시**하고 있어, 실질적인 재창출 신호라기보다 임베딩 아티팩트로 판단됩니다. 실제 가치 있는 신호는 순위 2, 4, 5로, 모두 기존에 알려진 **WHO Group 1 PAH 아형**입니다.

---

## 이 예측이 타당한 이유는?

**[Data Gap] 참고 — DG002**: 구조화된 MOA 필드는 비어 있으나, evidence pack 내 문헌·기전 서술을 통해 다음 내용이 확인됩니다.

Treprostinil은 합성 prostacyclin(PGI2) 유사체로 IP 수용체에 작용하여 **폐혈관 확장, 혈소판 응집 억제, 평활근 증식 억제** 효과를 나타내며, 이는 WHO Group 1 PAH 치료의 핵심 기전입니다(Simonneau 2002 등 초기 pivotal RCT부터 확인).

**선천성 심장병 동반 PAH**와 **결합조직질환 동반 PAH**는 모두 WHO Group 1 PAH의 하위 분류로, 원발성 PAH와 동일한 병태생리(내피기능 이상, 혈관수축·재형성)를 공유합니다. 따라서 treprostinil의 기전 외삽 타당성은 높으며, 실제로 두 후보 모두 treprostinil을 직접 사용한 코호트·RCT 하위분석 문헌이 존재합니다.

반면 **폐동정맥기형(순위 1)**은 혈관 구조 이상으로 인한 고유량 단락 병변으로, PAH의 혈관수축·재형성 기전과는 병태생리가 다릅니다. rationale 자체가 "질환명에 'pulmonary'가 공통으로 포함되어 발생한 KG 임베딩 유사도에 의한 위양성 가능성"을 명시하고 있어, 이 후보는 임상적으로 채택하기 어렵습니다. 저모증·다모증·치주질환 관련 후보(순위 7~10) 역시 IP 수용체 기전과 생물학적 연결고리가 없어 동일하게 노이즈로 판단됩니다.

---

## 임상시험 근거

### 선천성 심장병 동반 PAH (L2)

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT02261883](https://clinicaltrials.gov/study/NCT02261883) | Phase 2 | 조기 종료 | 42 | 신생아 지속성 폐고혈압(PPHN)에서 IV Remodulin(treprostinil) add-on 요법 평가. Grade A(직접 근거)이나 조기 종료·소규모로 근거 강도 제한적 |
| [NCT01383083](https://clinicaltrials.gov/study/NCT01383083) | N/A | 불명 | 42 | Iloprost(타 prostacyclin 유사체) 사용, 선천성 심장병 관련 PAH(아이젠멩거 생리)에서 안전성·혈역학 평가. Grade C(기전 유사 참고용, treprostinil 직접 근거 아님) |

### 결합조직질환 동반 PAH (L2)

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT02663895](https://clinicaltrials.gov/study/NCT02663895) | Phase 2 | 완료 | 12 | 전신경화증(SSc) 동반 석회화증에 경구 treprostinil 안전성·유효성 평가(pilot study). PAH 자체가 주요 종점은 아님 |

### HIV 감염 동반 PAH (L3)

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00494533](https://clinicaltrials.gov/study/NCT00494533) | Phase 4 | 조기 종료 | 45 | 인도 PAH 환자 대상 IV Remodulin(treprostinil) vs 위약. 원발성·HIV·결합조직질환 동반 PAH를 포괄하나 HIV 하위군 특이적 설계는 아님 |

---

## 문헌 근거

### 선천성 심장병 동반 PAH

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [29436381](https://pubmed.ncbi.nlm.nih.gov/29436381/) | 2018 | Cohort/Case series (Tier1) | Heart | 성인 선천성 심장병 동반 PAH에서 피하 treprostinil 12개월 치료 후 효능·안전성 평가 |
| [41201625](https://pubmed.ncbi.nlm.nih.gov/41201625/) | 2026 | Registry (COMPERA) | J Heart Lung Transplant | 고위험 PAH(선천성 심장병 동반군 포함)에서 비경구 prostacyclin 유사체 add-on 요법 495명 분석 |
| [23890862](https://pubmed.ncbi.nlm.nih.gov/23890862/) | 2013 | Cohort | Int J Cardiol | 성인 선천성 심장병 동반 PAH 8명에서 장기 지속 PGI2 투여의 혈역학·임상 효과 |
| [35000655](https://pubmed.ncbi.nlm.nih.gov/35000655/) | 2022 | Case series (Tier2) | Cardiol Young | 다운증후군(trisomy 21) 동반 선천성 심장병-PAH 환아에서 경구 selexipag→피하 treprostinil 전환 후 혈역학·운동능력 개선 |
| [18473715](https://pubmed.ncbi.nlm.nih.gov/18473715/) | 2008 | Review (Tier2) | Expert Opin Pharmacother | Treprostinil의 PAH 치료 전반(선천성 심장병 동반군 포함) 리뷰 |
| [35412560](https://pubmed.ncbi.nlm.nih.gov/35412560/) | 2022 | Review (Tier2) | JAMA | PAH 진단·치료 전반 리뷰 |
| [16919006](https://pubmed.ncbi.nlm.nih.gov/16919006/) | 2006 | Review (Tier3) | Eur J Clin Invest | 소아 PAH(선천성 심장병 동반 다수 포함) 치료 옵션 리뷰 |
| [21852894](https://pubmed.ncbi.nlm.nih.gov/21852894/) | 2009 | Cohort (Tier3) | Prog Pediatr Cardiol | 소아 PAH 원인 질환별(비선천성 심장병 포함) 개관 |

### 결합조직질환 동반 PAH

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [15302727](https://pubmed.ncbi.nlm.nih.gov/15302727/) | 2004 | RCT 하위분석 (Tier1) | Chest | 결합조직질환 동반 PAH 환자에서 피하 treprostinil의 효능·안전성 평가 |
| [11897647](https://pubmed.ncbi.nlm.nih.gov/11897647/) | 2002 | RCT Phase3 Pivotal (Tier1) | Am J Respir Crit Care Med | Treprostinil 지속 피하주입 이중맹검 위약대조 RCT(CTD 하위군 포함), Simonneau 등 |
| [38378970](https://pubmed.ncbi.nlm.nih.gov/38378970/) | 2024 | Systematic Review/Meta-analysis (Tier1) | Intern Emerg Med | 결합조직질환 동반 PAH 치료에 대한 RCT 메타분석 |
| [34462153](https://pubmed.ncbi.nlm.nih.gov/34462153/) | 2021 | Cohort (Tier2) | Rev Med Interne | Prostanoid 치료 받은 결합조직질환 동반 PAH 환자 특성 다기관 후향 연구 |
| [41594679](https://pubmed.ncbi.nlm.nih.gov/41594679/) | 2026 | Review (Tier2) | Biomolecules | 결합조직질환 동반 PAH 현재 치료전략 및 향후 전망 |
| [37765060](https://pubmed.ncbi.nlm.nih.gov/37765060/) | 2023 | Review (Tier2) | Pharmaceuticals | 결합조직질환 동반 PAH 치료 최신 동향 |
| [40005302](https://pubmed.ncbi.nlm.nih.gov/40005302/) | 2025 | Case report | Medicina | IV epoprostenol 불응성 전신경화증 동반 PAH-ILD에서 흡입 treprostinil 효과 |
| [37677880](https://pubmed.ncbi.nlm.nih.gov/37677880/) | 2023 | 후향 연구 | Am J Cardiol | Epoprostenol 부작용으로 IV treprostinil 전환한 PAH 환자군 분석 |

### HIV 감염 동반 PAH

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [14720012](https://pubmed.ncbi.nlm.nih.gov/14720012/) | 2003 | Review (Tier3) | Am J Respir Med | Prostanoid 계열 약물의 PAH(HIV 동반군 포함) 치료 개관 |
| [18473715](https://pubmed.ncbi.nlm.nih.gov/18473715/) | 2008 | Review (Tier3) | Expert Opin Pharmacother | Treprostinil의 PAH 치료 전반(HIV 동반군 포함) 리뷰 |
| [18260882](https://pubmed.ncbi.nlm.nih.gov/18260882/) | 2007 | Review (Tier3) | Kardiologiia | 원발성 및 결합조직질환·선천성 심장병·HIV 감염 동반 PAH에서 prostanoid 계열 대조시험 개관 |

> 그 외 후보(주혈흡충증·용혈성빈혈 동반 PAH, 저모증/다모증, 치아기형증후군)는 관련 임상시험 및 직접 문헌이 없거나(순위 3, 6), 첨부된 20편 문헌이 모두 일반 치주염 연구로 treprostinil과 무관합니다(순위 9). 저모증·다모증 후보(순위 7, 8, 10)는 관련 문헌이 전무합니다.

---

## 한국 시판 정보

한국에 등록된 허가 제품이 없습니다 (미시판, 허가증 0건).

---

## 안전성 고려사항

**[DG001 — Blocking 등급 데이터 갭]**: 국내 허가 라벨의 경고·금기 정보가 확보되지 않았습니다. 한국에서 미시판 상태이므로 참조할 국내 허가사항 자체가 없으며, 이로 인해 안전성 초기 평가(S1) 단계 진입이 불가능합니다. DDI 조회 결과도 데이터 없음(`not_found`)입니다.

진행을 위해서는 해외 원개발국(예: 미국 FDA, 유럽 EMA) 라벨의 경고·금기·상호작용 정보를 우선 확보하여 국내 허가 절차 이전 단계의 안전성 초기평가 자료로 활용할 필요가 있습니다.

---

## 결론 및 다음 단계

**결정: Hold** (약물 수준) / 개별 적응증은 **Proceed with Guardrails** (선천성 심장병 동반 PAH, 결합조직질환 동반 PAH)

**사유:**
- 과학적 근거만 보면 선천성 심장병 동반 PAH와 결합조직질환 동반 PAH는 기전적 타당성이 높고 L2 수준 근거(코호트, RCT 하위분석, 체계적 문헌고찰)를 갖추고 있어 Guardrails 하에 진행 가능한 수준입니다.
- 다만 (1) 한국 미시판으로 신규 적응증 확대가 아닌 신약 허가 절차 자체가 선행되어야 하고, (2) DG001(라벨 안전성 정보) Blocking 데이터 갭으로 S1 안전성 초기평가조차 불가능하여, 약물 수준에서는 **Hold**가 타당합니다.
- TxGNN 최고 순위 후보(폐동정맥기형)는 rationale 자체가 위양성 가능성을 지적하고 있어 채택 대상에서 제외합니다.

**진행하려면 필요한 것:**
- 해외(미국 FDA/EMA) 라벨 기반 경고·금기·DDI 정보 확보 (DG001 해소)
- 국내 신약 허가(또는 희귀의약품 지정) 절차 검토
- 선천성 심장병 동반 PAH, 결합조직질환 동반 PAH에 특화된 전향적 임상 데이터(현재는 소규모·조기종료 시험 또는 하위분석에 의존)
- HIV 감염 동반 PAH는 HIV 하위군 특이적 데이터 부재로 Research Question 단계 유지, 추가 문헌/레지스트리 조사 필요
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

