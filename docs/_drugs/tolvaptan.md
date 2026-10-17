---
layout: default
title: Tolvaptan
parent: 모델 예측만 (L5)
nav_order: 746
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Tolvaptan: 예측 신규 적응증 다낭신질환 3형 (다낭간질환 동반 또는 비동반) (근거 수준 L5). 기존 적응증: 허가증 원문 링크만 제공되어 구체적인 적응증 문구를 확인할 수 없음 (허가사항 참조)"
monitor_inn: "Tolvaptan"
predicted_indications: ["renal-hepatic-pancreatic dysplasia", "karyomegalic interstitial nephritis", "thoracic malformation", "Joubert syndrome with renal defect", "adult familial nephronophthisis-spastic quadriparesia syndrome", "Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature"]
---

# Tolvaptan
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
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

# Tolvaptan: 허가 적응증에서 상염색체 우성 다낭신질환(PKD3 포함 다낭신 질환)으로

## 한 문장 요약

Tolvaptan은 선택적 바소프레신 V2 수용체 길항제로, 한국에서 4건의 단일제 허가를 받아 시판 중입니다. TxGNN 모델은 **다낭신질환 3형(다낭간질환 동반 또는 비동반)**에 효과가 있을 수 있다고 예측하며, 현재 등록된 임상시험은 없지만 **19편의 문헌**(핵심 Phase 3 RCT 2건 포함)이 이 방향을 지지합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가증 원문 링크만 제공되어 구체적인 적응증 문구를 확인할 수 없음 (허가사항 참조) |
| 예측 신규 적응증 | 다낭신질환 3형 (다낭간질환 동반 또는 비동반) |
| TxGNN 예측 점수 | 99.99% |
| 근거 수준 | L1 (ADPKD 전체 계열 기준의 직접 근거이며, PKD3에는 외삽) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 4건 |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 없습니다. 다만 문헌에 따르면 Tolvaptan은 선택적 바소프레신 V2 수용체 길항제입니다. 다낭신질환에서는 cAMP 신호가 높아져 낭종액 분비와 낭종 세포 증식이 촉진되는데, V2 수용체를 차단하면 신장 집합관 세포의 cAMP가 감소하여 낭종 성장과 eGFR 저하가 늦춰집니다.

PKD3(GANAB 관련 형태)는 ADPKD와 동일한 낭종 형성 경로를 공유합니다. 따라서 기전상 적용 가능성이 있습니다.

다만 주의할 점이 있습니다. 이번 데이터에는 임상시험 등록 정보가 없고, 핵심 Phase 3 시험(TEMPO 3:4, REPRISE)은 PKD1/PKD2 기반 ADPKD 대상입니다. 즉, 근거는 ADPKD 계열에는 직접적이지만 PKD3에는 외삽된 것입니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [23121377](https://pubmed.ncbi.nlm.nih.gov/23121377/) | 2012 | RCT | N Engl J Med | ADPKD 환자 대상 Tolvaptan 시험(TEMPO 3:4). V2 수용체 길항제가 신장 용적 증가와 신기능 저하를 늦춤 |
| [29105594](https://pubmed.ncbi.nlm.nih.gov/29105594/) | 2017 | RCT | N Engl J Med | 후기 ADPKD에서의 Tolvaptan 효능·안전성(REPRISE). 이전 시험에서 간효소·빌리루빈 상승 보고 |
| [39356039](https://pubmed.ncbi.nlm.nih.gov/39356039/) | 2024 | 체계적 문헌고찰 | Cochrane Database Syst Rev | ADPKD 진행 예방 중재법 평가 |
| [40126492](https://pubmed.ncbi.nlm.nih.gov/40126492/) | 2025 | Review | JAMA | ADPKD 종설. 가장 흔한 유전성 신질환 |
| [41771281](https://pubmed.ncbi.nlm.nih.gov/41771281/) | 2026 | Review | Lancet | Tolvaptan이 질병 조절 치료제로서 근거가 탄탄하며, 신부전 고위험군에서 조기 사용 지지 |
| [40844441](https://pubmed.ncbi.nlm.nih.gov/40844441/) | 2025 | Review | Am J Kidney Dis | ADPKD 핵심 커리큘럼. 위험도 예측으로 질병 조절 치료 대상 선별 |
| [40726372](https://pubmed.ncbi.nlm.nih.gov/40726372/) | 2025 | Review | Curr Opin Nephrol Hypertens | Tolvaptan이 유일한 FDA 승인 질병 진행 억제제이며 신규 치료제 파이프라인 증가 |
| [35487607](https://pubmed.ncbi.nlm.nih.gov/35487607/) | 2022 | Review | Clin Liver Dis | 다낭신/간질환. ADPKD에서 Tolvaptan이 신기능 저하와 낭종 성장을 늦출 수 있음 |
| [40268755](https://pubmed.ncbi.nlm.nih.gov/40268755/) | 2025 | Review | Ren Fail | ADPKD의 최근 유전학적·임상적 발전 개관 |
| [32392574](https://pubmed.ncbi.nlm.nih.gov/32392574/) | 2021 | 문헌 | Pediatr Res | 빠르게 진행하는 청소년·젊은 성인 ADPKD에서의 Tolvaptan 사용 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202203115 | 톨비스정15밀리그램(톨밥탄) | 파란색 원형 정제 | 허가사항 참조 |
| 202203114 | 톨비스정30밀리그램(톨밥탄) | 파란색 원형 정제 | 허가사항 참조 |
| 202004774 | 명인톨밥탄정15밀리그램 | 파란색 원형 정제 | 허가사항 참조 |
| 202202617 | 명인톨밥탄정30밀리그램 | 파란색 원형 정제 | 허가사항 참조 |

## 안전성 고려사항

- **지식그래프 기반 금기 질환** (허가사항 문구가 아닌 TxGNN 지식그래프 기준): 간부전, 간경변, 물질 남용/의존, 활동성 소화성 궤양, 탈수초성 질환
- **약물 상호작용**: 총 100건이 확인되었으며, 주요 항목은 다음과 같습니다.
  - Major: Clarithromycin
  - Moderate: Aprepitant, Dexamethasone, Eliglustat, Empagliflozin, Loperamide, Miconazole, Naltrexone, Rifaximin, Rolapitant, 칼륨 제제(구연산칼륨, 중탄산칼륨, 염화칼륨, 글루콘산칼륨) 등
  - Minor: Fidaxomicin, Naloxegol, Prucalopride
- **문헌에서 확인된 주의점**: 간효소 및 빌리루빈 상승(간독성), 아쿠아레시스 관련 이상반응, 다낭간질환 환자에서의 주의

허가사항의 경고 및 금기 정보는 이번 데이터에 포함되지 않았으므로 허가사항을 직접 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
ADPKD에서 Tolvaptan의 효능을 입증한 Phase 3 RCT 2건(TEMPO 3:4, REPRISE)과 다수의 종설이 있고, PKD3는 동일한 cAMP 매개 낭종 형성 경로를 공유합니다. 다만 PKD3 특이적 임상 근거는 없어 외삽에 해당하며, 간독성 관리가 필수입니다.

**진행하려면 필요한 것:**
- 한국 허가증의 적응증 및 경고·금기 문구 확인 (허가사항 PDF 분석)
- 상세한 약물 작용 기전(MOA) 데이터 보강
- PKD3(GANAB 관련) 환자에서의 효능 및 안전성 근거 확보
- 간효소 모니터링 체계(간독성 감시) 및 다낭간질환 환자 주의 계획
- Clarithromycin 등 주요 상호작용 약물 관리 방안

**참고: 기타 예측 적응증**
- 신장-간-췌장 이형성증, 핵거대 간질성 신염, 흉곽 기형 등 나머지 예측은 근거 수준이 L4~L5로, 임상시험이 없거나 간접 근거뿐이어서 현재 보류(Hold) 권고입니다.
- 주베르 증후군(신장 결손 동반)은 섬모병증으로서 cAMP 신호 이상이 PKD와 공통되나, 직접 근거가 없어 전임상 연구가 우선 필요한 연구 과제 수준입니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

