---
layout: default
title: Haloperidol
parent: 모델 예측만 (L5)
nav_order: 398
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Haloperidol: 예측 신규 적응증 조현병 (Schizophrenia) (근거 수준 L5). 기존 적응증: 허가 적응증 본문이 데이터에 포함되어 있지 않음 (허가증 원문 링크만 확인됨)"
---

# Haloperidol
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
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

# Haloperidol: 조현병 치료제로서의 기존 적응증과 TxGNN 예측 신규 적응증 (조현병)

## 한 문장 요약

Haloperidol은 도파민 D2 수용체를 차단하는 전형적(1세대) 항정신병약물로, 한국에서 이미 시판 중입니다.
TxGNN 모델은 **조현병(schizophrenia)**에 효과가 있을 것으로 예측하며(점수 99.96%), 이 예측을 **임상시험 34건**과 **문헌 20편**이 뒷받침합니다.
다만 조현병은 이미 확립된 표준 사용 영역이므로, 이 결과는 신규 재창출이라기보다 기존 임상 사용을 모델이 재확인한 것에 가깝습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문이 데이터에 포함되어 있지 않음 (허가증 원문 링크만 확인됨) |
| 예측 신규 적응증 | 조현병 (Schizophrenia) |
| TxGNN 예측 점수 | 99.96% |
| 근거 수준 | L1 (완료된 Phase 3 임상시험 다수) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 12건 (모두 단일제, 유효) |
| 권장 결정 | Proceed with Guardrails |

> 참고: 이 보고서의 근거 수준은 위 판정 규칙의 형식 요건(완료된 Phase 3 시험 ≥2건)에 따라 L1로 분류했습니다. 다만 해당 시험 대부분은 haloperidol이 대조약으로 쓰인 비교 시험입니다.

## 이 예측이 타당한 이유는?

Haloperidol은 강력한 도파민 D2 수용체 길항제입니다. 중뇌변연계(mesolimbic) 경로에서 D2를 차단하면 조현병의 양성 증상(환각, 망상)이 줄어드는 것으로 알려져 있으며, 이것이 항정신병약물의 확립된 작용 기전입니다. 다만 DrugBank 기반의 상세 작용 기전 데이터는 이번 자료에 포함되어 있지 않습니다.

조현병은 haloperidol의 전통적인 사용 영역입니다. 따라서 이 예측은 새로운 적응증 발굴이 아니라 기존 임상 현실과 일치하는 결과로 해석하는 것이 맞습니다.

같은 기전은 조현양상장애(schizophreniform disorder, 예측 2위, 99.92%)와 정신병적 장애(psychotic disorder, 예측 8위, 99.89%)에도 적용됩니다. 두 질환 모두 임상시험·문헌 근거가 있으나 대부분 조현병 혼합 집단 시험에서 나온 간접 근거입니다.

반면 3위 이하 예측 중 선천성 글리코실화 장애, 망막 이영양증, 무뇌수두증, X-연관 근시, 샤르코-마리-투스병 1G형, 증후군성 근시 등은 기전적 연결이 뚜렷하지 않고 임상시험·문헌이 없거나 동물 연구 2편 정도에 그칩니다. 이들은 계산상 예측에 불과하며 근거 수준 L5, 권장 결정은 Hold입니다.

## 임상시험 근거

조현병 관련 시험 중 관련성이 높은 것을 정리했습니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00191555](https://clinicaltrials.gov/study/NCT00191555) | Phase 4 | 완료 | 360 | 기존 항정신병약물로 안정된 만성 조현병 환자에서 olanzapine vs haloperidol 이중맹검 장기 비교 |
| [NCT00723606](https://clinicaltrials.gov/study/NCT00723606) | Phase 3 | 완료 | 376 | 조현병 초조 증상에서 ziprasidone 근주 vs haloperidol 비교 |
| [NCT00156104](https://clinicaltrials.gov/study/NCT00156104) | Phase 3 | 완료 | 460 | 급성 악화 조현병에서 asenapine vs 위약, haloperidol 양성대조 |
| [NCT00866645](https://clinicaltrials.gov/study/NCT00866645) | Phase 2/3 | 완료 | 240 | 조현병 초조에서 levosulpiride 근주 vs haloperidol 근주 |
| [NCT00455234](https://clinicaltrials.gov/study/NCT00455234) | Phase 3 | 완료 | 300 | 정신과 응급에서 olanzapine 근주 vs haloperidol + promethazine |
| [NCT00797277](https://clinicaltrials.gov/study/NCT00797277) | Phase 3 | 완료 | 67 | 급성 초조 조현병에서 olanzapine 근주 vs haloperidol + lorazepam 근주 (공개, 소규모) |
| [NCT00156065](https://clinicaltrials.gov/study/NCT00156065) | Phase 3 | 완료 | 187 | asenapine 장기 연장 시험, haloperidol 양성대조 |
| [NCT00044044](https://clinicaltrials.gov/study/NCT00044044) | Phase 2 | 완료 | 356 | 급성 악화 조현병에서 SM-13496 vs 위약 및 haloperidol |
| [NCT01164059](https://clinicaltrials.gov/study/NCT01164059) | Phase 4 | 완료 | 149 | 신세대 항정신병약물 vs 저용량 haloperidol/flupentixol 효과 비교 |
| [NCT01161277](https://clinicaltrials.gov/study/NCT01161277) | Phase 4 | 완료 | 54 | aripiprazole과 haloperidol의 중뇌변연계 기능 영향 fMRI 연구 (기전 근거) |

> 위 시험 대부분은 haloperidol을 대조약으로 사용한 비교 시험이어서, haloperidol 자체의 효능을 직접 입증하는 근거라기보다 간접 근거입니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [11406070](https://pubmed.ncbi.nlm.nih.gov/11406070/) | 2001 | Cochrane 체계적 문헌고찰 | Cochrane Database Syst Rev | 조현병에서 haloperidol vs 위약 |
| [38958149](https://pubmed.ncbi.nlm.nih.gov/38958149/) | 2024 | Cochrane 체계적 문헌고찰 | Cochrane Database Syst Rev | 조현병 및 스펙트럼 장애에서 경구 haloperidol vs olanzapine |
| [18254045](https://pubmed.ncbi.nlm.nih.gov/18254045/) | 2008 | Cochrane 체계적 문헌고찰 | Cochrane Database Syst Rev | 조현병에서 haloperidol vs chlorpromazine |
| [10796438](https://pubmed.ncbi.nlm.nih.gov/10796438/) | 2000 | Cochrane 체계적 문헌고찰 | Cochrane Database Syst Rev | 조현병에서 haloperidol decanoate(지속형 주사제) |
| [31006114](https://pubmed.ncbi.nlm.nih.gov/31006114/) | 2019 | Cochrane 체계적 문헌고찰 | Cochrane Database Syst Rev | 안정된 조현병 환자의 haloperidol 중단 효과 |
| [11552769](https://pubmed.ncbi.nlm.nih.gov/11552769/) | 2001 | 이중맹검 시험 통합분석 | Int Clin Psychopharmacol | risperidone vs haloperidol 등, 12개 이중맹검 시험 통합 |
| [11823268](https://pubmed.ncbi.nlm.nih.gov/11823268/) | 2002 | 임상 비교 연구 | Am J Psychiatry | 만성 조현병·조현정동장애에서 clozapine, olanzapine, risperidone, haloperidol 비교 |
| [12363115](https://pubmed.ncbi.nlm.nih.gov/12363115/) | 2002 | 임상 연구 | J Clin Psychiatry | aripiprazole 및 haloperidol vs 위약 |
| [7575103](https://pubmed.ncbi.nlm.nih.gov/7575103/) | 1995 | 임상 연구 | Arch Gen Psychiatry | 혈장 haloperidol 농도(5~11 ng/mL)와 임상 효과 |
| [15342619](https://pubmed.ncbi.nlm.nih.gov/15342619/) | 2004 | 임상 연구 | J Clin Pharmacol | haloperidol 근주 시 QT 간격 영향 (안전성 관련) |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 198500618 | 명인할로페리돌정1.5밀리그램 | 정제 (백색 원형) | 허가 적응증 본문 미확인 (허가증 원문 참조) |
| 198500715 | 페리돌정3밀리그램 | 정제 (황색 원형) | 허가 적응증 본문 미확인 (허가증 원문 참조) |
| 198400475 | 페리돌정10밀리그램 | 정제 (청색 원형) | 허가 적응증 본문 미확인 (허가증 원문 참조) |
| 198301325 | 페리돌주 | 주사제 (앰플) | 허가 적응증 본문 미확인 (허가증 원문 참조) |
| 198700673 | 명인할로페리돌주사 | 주사제 (앰플) | 허가 적응증 본문 미확인 (허가증 원문 참조) |

전체 12건의 허가증 중 대표 5건만 나열했으며, 정제 7종 외에 주사제 2종이 포함됩니다.

## 안전성 고려사항

**약물 상호작용** (총 100건 조회, 일부 표시)
- **Major(중대)**: bupropion, morphine, clarithromycin, dolasetron
- **Moderate(중등도)**: famotidine, epinephrine, hydrocortisone, amphotericin B, hyoscyamine, loperamide, aprepitant, atropine, glycopyrronium 등

문헌에서는 haloperidol 근주 시 QT 간격 연장이 보고되었으므로(PMID 15342619), QT 연장을 일으킬 수 있는 약물(예: dolasetron, clarithromycin)과 병용할 때 주의가 필요합니다.

경고 및 금기 사항은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
조현병은 haloperidol의 확립된 사용 영역이며, Cochrane 체계적 문헌고찰과 다수의 Phase 3/4 비교 시험이 이를 뒷받침합니다. 다만 신규 재창출이 아니라 기존 적응증의 재확인이고, 시험 대부분이 대조약 사용 연구이므로 일정한 안전장치를 두고 진행하는 것이 적절합니다.

**진행하려면 필요한 것:**
- 한국 허가사항(첨부문서)에서 허가 적응증, 경고, 금기 사항 확인 및 정리 (현재 확인되지 않아 안전성 선별을 진행할 수 없음)
- 상세 작용 기전 데이터 보완
- QT 연장 위험과 Major 등급 약물 상호작용에 대한 모니터링 계획
- 조현양상장애·정신병적 장애 등 인접 적응증은 조현병 혼합 집단 시험 근거만 있으므로 별도 직접 근거 확인
- 3위 이하 비정신과 질환 예측(근시, 망막 이영양증 등)은 근거가 없어 Hold로 유지
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

