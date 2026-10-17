---
layout: default
title: Epinephrine
parent: 모델 예측만 (L5)
nav_order: 315
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-15
description: "Epinephrine: 예측 신규 적응증 폐쇄성 폐질환 (Obstructive Lung Disease) (근거 수준 L5). 기존 적응증: 허가증에 적응증 원문이 포함되어 있지 않아 확인 불가 (허가사항 PDF 링크만 제공됨)"
monitor_inn: "EPINEPHRINE"
predicted_indications: ["obstructive lung disease", "Rienhoff syndrome", "respiratory malformation"]
---

# Epinephrine
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **4** 건
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

# Epinephrine: 기관지 확장·아나필락시스 응급 치료제에서 폐쇄성 폐질환으로

## 한 문장 요약

Epinephrine(에피네프린)은 비선택적 아드레날린 작용제로, 한국에서 주사제 형태로 허가되어 사용되고 있습니다.
TxGNN 모델은 **폐쇄성 폐질환(Obstructive Lung Disease)**에 효과가 있을 수 있다고 예측하며, 현재 **15건의 임상시험**과 **20편의 문헌**이 이 방향과 관련되어 있습니다. 다만 이 적응증은 해외에서 흡입제(천식 OTC 제품)로 이미 사용되고 있어 엄밀한 의미의 신규 재창출이라기보다 기존 사용에 가깝습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가증에 적응증 원문이 포함되어 있지 않아 확인 불가 (허가사항 PDF 링크만 제공됨) |
| 예측 신규 적응증 | 폐쇄성 폐질환 (Obstructive Lung Disease) |
| TxGNN 예측 점수 | 99.71% |
| 근거 수준 | L1 (완료된 Phase 3 임상시험 4건 있음. 단, 아래 참고) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 8건 |
| 권장 결정 | Proceed with Guardrails |

> 참고: 완료된 Phase 3 시험은 천식 대상 흡입제(E004) 연구이며, 한국에서 허가된 주사제와는 투여 경로가 다릅니다. 근거 수준 L1은 흡입제 기준으로 해석해야 합니다.

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Epinephrine은 비선택적 아드레날린 작용제입니다. 베타-2 수용체 활성화로 기관지 평활근이 이완되어 기관지 확장이 일어나고, 알파-1 수용체 활성화로 혈관 수축을 통해 점막 부종이 줄어듭니다.

이러한 기전은 천식과 같은 가역적 기도 폐쇄에 직접적인 근거가 됩니다. 미국에서는 흡입형 Epinephrine(Primatene Mist, E004 HFA-MDI)이 천식용 OTC 제품으로 이미 판매되고 있습니다. 세기관지염에 대한 근거는 상대적으로 약하고 결과도 일관되지 않습니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01357642](https://clinicaltrials.gov/study/NCT01357642) | Phase 3 | 완료 | 373 | 천식 환자에서 Epinephrine HFA 흡입제의 12주 효능·안전성 (위약 및 Primatene Mist 대비) |
| [NCT01476904](https://clinicaltrials.gov/study/NCT01476904) | Phase 3 | 완료 | 208 | 천식 환자 대상 3개월 안전성 연장 시험 (이중맹검) |
| [NCT01460511](https://clinicaltrials.gov/study/NCT01460511) | Phase 3 | 완료 | 70 | 4~11세 천식 소아에서 E004 4주 효능·안전성 |
| [NCT01737905](https://clinicaltrials.gov/study/NCT01737905) | Phase 3 | 완료 | 28 | 소아 천식에서 E004 단회 투여 교차 시험 |
| [NCT01705964](https://clinicaltrials.gov/study/NCT01705964) | Phase 4 | 완료 | 49 | 중증 소아 천식 악화에서 근육주사 Epinephrine 보조요법 |
| [NCT01834820](https://clinicaltrials.gov/study/NCT01834820) | Phase 4 | 완료 | 120 | 세기관지염 소아에서 Epinephrine·덱사메타손·고장성 식염수 병용 (예비 연구) |
| [NCT00817466](https://clinicaltrials.gov/study/NCT00817466) | Phase 4 | 불명 | 500 | 12개월 미만 급성 세기관지염 흡입 치료 비교 |
| [NCT00114478](https://clinicaltrials.gov/study/NCT00114478) | 해당 없음 | 불명 | 600 | 세기관지염에서 Epinephrine과 Albuterol 비교 |
| [NCT00622817](https://clinicaltrials.gov/study/NCT00622817) | 해당 없음 | 완료 | 65 | 세기관지염에서 Epinephrine 흡입 vs 비강 충혈제거 점비액 |
| [NCT04207840](https://clinicaltrials.gov/study/NCT04207840) | Phase 4 | 완료 | 28 | Primatene Mist 흡입 vs 근육주사 Epinephrine의 전신 노출 비교 (약동학) |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [35093318](https://pubmed.ncbi.nlm.nih.gov/35093318/) | 2022 | RCT | J Pediatr | 중환자실 세기관지염 소아에서 코르티코스테로이드와 Epinephrine 흡입 병용의 양압 지지 기간 단축 평가 |
| [33893229](https://pubmed.ncbi.nlm.nih.gov/33893229/) | 2021 | 네트워크 메타분석 | Pediatrics | 급성기 세기관지염 중재 간 비교 효능 평가 |
| [21678340](https://pubmed.ncbi.nlm.nih.gov/21678340/) | 2011 | 체계적 문헌고찰 (Cochrane) | Cochrane Database Syst Rev | 세기관지염에 대한 Epinephrine 효과 평가 |
| [14974006](https://pubmed.ncbi.nlm.nih.gov/14974006/) | 2004 | 체계적 문헌고찰 (Cochrane) | Cochrane Database Syst Rev | 세기관지염에서 기관지확장제의 단기 효과 |
| [35953216](https://pubmed.ncbi.nlm.nih.gov/35953216/) | 2022 | Review | Emerg Med Clin North Am | 응급실에서의 천식·COPD 악화 평가 및 관리 |
| [30488718](https://pubmed.ncbi.nlm.nih.gov/30488718/) | 2019 | Review | Expert Rev Respir Med | 소아 세기관지염의 치료 전략 (라세미 Epinephrine 등) |
| [21157348](https://pubmed.ncbi.nlm.nih.gov/21157348/) | 2011 | Review | Curr Opin Pediatr | 세기관지염 관리 최신 동향 |
| [23393929](https://pubmed.ncbi.nlm.nih.gov/23393929/) | 2012 | Review | Duodecim | 세기관지염 개요 (필요 시 라세미 Epinephrine 흡입) |
| [20876171](https://pubmed.ncbi.nlm.nih.gov/20876171/) | 2010 | 경제성 평가 | Pediatrics | 세기관지염 소아에서 Epinephrine·덱사메타손의 비용효과 |
| [11940264](https://pubmed.ncbi.nlm.nih.gov/11940264/) | 2002 | Review | Crit Care | 중증 천식 임상 리뷰 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201708377 | 젝스트프리필드펜주150마이크로그램(에피네프린타르타르산염) | 1회용 프리필드 펜 주사제 | 허가사항 PDF 참조 |
| 201708378 | 젝스트프리필드펜주300마이크로그램(에피네프린타르타르산염) | 1회용 프리필드 펜 주사제 | 허가사항 PDF 참조 |
| 201904387 | 에피네프린프리필드시린지주1:10,000 | 프리필드 시린지 주사제 | 허가사항 PDF 참조 |
| 198400285 | 제일에피네프린주사액 | 앰플 주사제 | 허가사항 PDF 참조 |
| 196900031 | 대한에피네프린주사액 | 앰플 주사제 | 허가사항 PDF 참조 |

그 외 보스민액(197200086), 제일약품에피네프린주(수출용, 202103993), 휴온스에피네프린주(수출용, 201101498)가 허가되어 있습니다.

## 안전성 고려사항

- **금기 관련 참고 (지식 그래프 기반, 허가 문서 아님)**: 고혈압, 간부전, 간질, 신장 질환, 당뇨병, 당뇨병성 케토산증, 양성 전립선 비대증, 심방세동, 관상동맥 질환, 심근경색, 심장 전도 질환, 호흡부전, 폐쇄각 녹내장, 중증 근무력증, 갑상선기능항진증 등이 약물-질환 금기 관계로 연결되어 있습니다.
- **약물 상호작용**: 총 100건이 확인되었으며, 일부는 **Major** 등급입니다.
  - Major: Amitriptyline, Amoxapine
  - Moderate (일부): 베타차단제(Acebutolol, Atenolol, Betaxolol), 베타-2 작용제(Formoterol, Salbutamol, Arformoterol), 당뇨병 치료제(Acarbose, Alogliptin, Albiglutide), 자극제(Methylphenidate, Amphetamine, Atomoxetine), 항정신병약(Amisulpride, Aripiprazole, Asenapine)

허가사항의 경고 및 금기는 이번 데이터에서 확인되지 않았으므로 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
천식 대상 Phase 3 시험이 다수 완료되었고 기전도 명확하지만, 이 근거는 흡입제에 대한 것입니다. 한국 허가 제품은 모두 주사제이므로 투여 경로 차이를 고려한 접근이 필요합니다. 세기관지염 근거는 약하고 일관성이 부족합니다.

**진행하려면 필요한 것:**
- 한국 허가사항(적응증, 경고, 금기) 확보 및 분석
- 투여 경로 적합성 검토 (주사제 vs 흡입제)
- 작용 기전 데이터 보완
- 심혈관 질환, 당뇨, 고혈압 환자 등 고위험군 안전성 모니터링 계획
- Major 상호작용 약물(삼환계 항우울제 등) 병용 관리 방안

---

### 참고: 기타 예측 적응증

| 순위 | 예측 적응증 | TxGNN 점수 | 근거 수준 | 권장 |
|------|-----------|-----------|----------|------|
| 2 | 음식 의존성 운동 유발 아나필락시스 | 99.57% | L4 | Research Question |
| 3 | Rienhoff 증후군 | 99.57% | L5 | Hold |
| 4 | 호흡기 기형 | 99.56% | L3 | Research Question |

- **음식 의존성 운동 유발 아나필락시스**: 아나필락시스의 1차 응급 치료제라는 점에서 기전 연관성이 강하나, 해당 아형에 대한 임상시험은 없고 문헌은 리뷰와 증례 중심입니다.
- **Rienhoff 증후군**: 임상시험과 문헌이 없고 기전적 근거도 불분명하여 모델 예측만 존재합니다.
- **호흡기 기형**: 유일한 시험(NCT05006235)은 신생아 일과성 빈호흡 대상 Phase 1이라 구조적 기형과는 간접적으로만 관련되며, 검색된 문헌 대부분도 관련성이 낮습니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

