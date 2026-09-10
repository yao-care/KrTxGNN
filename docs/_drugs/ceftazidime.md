---
layout: default
title: Ceftazidime
parent: 僅模型預測 (L5)
nav_order: 186
evidence_level: L5
indication_count: 10
---

# Ceftazidime
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

Evidence Pack을 검토한 결과, TxGNN 점수 1위(hyperamylasemia)는 문헌 1편(간접적 항생제 예방 효과 논의)뿐이라 근거가 거의 없고, 실질적으로 검증 가능한 근거는 rank 4(요로감염, L1)와 rank 9(중이염, L3)에 집중되어 있습니다. 이에 보고서는 근거 강도가 가장 높은 요로감염을 중심으로 작성하고, 나머지 후보의 신뢰도를 함께 명시합니다.

---

# Ceftazidime: 항균 스펙트럼 내 그람음성균 감염에서 요로감염(UTI)으로

## 한 문장 요약

Ceftazidime(DB00438)은 그람음성균 감염 치료에 사용되어 온 3세대 세파로스포린 계열 항생제입니다(정확한 원 적응증 목록은 데이터 공백). TxGNN 모델이 제시한 10개 예측 적응증 중 실질적 임상 근거가 가장 강한 것은 **요로감염(Urinary Tract Infection)**이며, 현재 **17건의 임상시험**과 **20편의 문헌**이 이를 뒷받침합니다. 다만 이는 ceftazidime의 기존 항균 스펙트럼 내 적용에 해당하여, 엄밀한 의미의 "노후 의약품 재창출"이라기보다 **기존 용도의 근거 재확인**에 가깝습니다.

참고로 TxGNN 점수 자체가 가장 높았던 hyperamylasemia(rank 1), polyclonal hyperviscosity syndrome(rank 2), congenital analbuminemia(rank 3) 등은 문헌·임상시험이 전무하거나 기전상 연관성이 없어(L4~L5, Hold) 신뢰할 수 없는 예측으로 판단됩니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (원 적응증·한국 허가 정보 모두 미확보) |
| 예측 신규 적응증 | 요로감염 Urinary Tract Infection (disease) |
| TxGNN 예측 점수 | 99.41% (rank 9,554) |
| 근거 수준 | L1 |
| 한국 시판 현황 | 미상시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold (근거는 강하나 안전성 데이터 공백으로 초기 심사 진입 불가) |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터는 확보되지 않았습니다(Drug_Level 데이터 공백, High 심각도). 다만 Ceftazidime은 알려진 대로 3세대 세파로스포린 계열 항생제로, 세균의 penicillin-binding proteins(PBPs)를 억제해 세포벽 합성을 차단하는 방식으로 작용합니다.

요로감염의 주요 원인균(대장균, 클렙시엘라, 녹농균 등 그람음성간균)은 ceftazidime의 핵심 항균 스펙트럼 안에 있습니다. 즉 이 예측은 새로운 기전적 확장이 아니라, 이미 확립된 항균 활성이 요로감염 치료에도 적용되는 것을 재확인하는 성격이 강합니다. 실제로 ceftazidime 단독 및 ceftazidime-avibactam 병용요법을 복잡성 요로감염(cUTI)에 적용한 Phase 2~4 임상시험이 다수 존재합니다.

부차적으로, rank 9 감염성 중이염(중이염, 특히 녹농균성 만성화농성중이염)도 L3 수준의 실질적 근거(문헌 15편, 다수의 소아·성인 대상 소규모 임상연구)를 보이며, "Research Question" 단계로 추가 조사 가치가 있습니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00921024](https://clinicaltrials.gov/study/NCT00921024) | Phase 2 | 완료 | 129 | IV CXA-101 vs Ceftazidime, 복잡성 UTI(신우신염 포함) 안전성·유효성 비교 RCT — 관련성 A등급 |
| [NCT00690378](https://clinicaltrials.gov/study/NCT00690378) | Phase 2 | 완료 | 137 | NXL104/Ceftazidime vs 대조군, 복잡성 UTI 입원 성인 대상 유효성 평가 |
| [NCT02497781](https://clinicaltrials.gov/study/NCT02497781) | Phase 2 | 완료 | 97 | 소아(3개월~18세) 복잡성 UTI에서 Ceftazidime-Avibactam vs Cefepime 안전성·PK·유효성 |
| [NCT04628572](https://clinicaltrials.gov/study/NCT04628572) | N/A | 완료 | 189 | Ceftazidime-Avibactam 실사용 후향적 분석, 그람음성균 감염 치료 패턴·안전성 |
| [NCT01430910](https://clinicaltrials.gov/study/NCT01430910) | Phase 1 | 완료 | 43 | Ceftazidime-Avibactam(CAZ104) 건강인 대상 PK 및 약물상호작용 연구 |
| [NCT04882085](https://clinicaltrials.gov/study/NCT04882085) | Phase 4 | 완료 | 60 | CAZ-AVI vs 최적표준치료(BAT), 카바페넴내성 그람음성균 감염(cUTI 포함) 중국 성인 대상 |
| [NCT03147807](https://clinicaltrials.gov/study/NCT03147807) | N/A | 완료 | 75 | BetaLACTA 검사 기반 카바페넴 조기 감량, 폐·요로·혈류감염 포함 ICU 연구 |
| [NCT04278404](https://clinicaltrials.gov/study/NCT04278404) | N/A | 모집 중 | 5,000 | 소아·청년 대상 미충분 연구 약물(ceftazidime 포함 추정) PK/PD/안전성 광범위 연구 |
| [NCT05733104](https://clinicaltrials.gov/study/NCT05733104) | N/A | 모집 중 | 600 | Zavicefta(CAZ-AVI) 시판 후 안전성·유효성 관찰 연구, 복부·요로·폐렴 포함(한국 MFDS 요구) |
| [NCT05258851](https://clinicaltrials.gov/study/NCT05258851) | Phase 3 | 중단 | 29 | CAZ-AVI vs Colistin, 카바페넴내성 장내세균 감염 중환자 비열등성 RCT (조기종료) |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [32094128](https://pubmed.ncbi.nlm.nih.gov/32094128/) | 2020 | RCT | Antimicrob Agents Chemother | Meropenem-Vaborbactam vs Ceftazidime-Avibactam, 카바페넴내성 장내세균 감염(요로감염 포함) 비교 |
| [33618353](https://pubmed.ncbi.nlm.nih.gov/33618353/) | 2021 | Cohort | Clin Infect Dis | CAZ-AVI의 KPC 생성 폐렴간균 감염 치료 후향적 다기관 관찰연구 |
| [39817442](https://pubmed.ncbi.nlm.nih.gov/39817442/) | 2025 | Review/Network Meta-analysis | J Comp Eff Res | 복잡성 UTI 및 급성 신우신염 치료 옵션 효능 비교 체계적 문헌고찰 |
| [40530972](https://pubmed.ncbi.nlm.nih.gov/40530972/) | 2025 | PK/PD Modeling | Antimicrob Agents Chemother | Aztreonam-Avibactam(유사 계열) cUTI 포함 용량 최적화 모델링 |
| [38185380](https://pubmed.ncbi.nlm.nih.gov/38185380/) | 2024 | Cohort/Surveillance | Am J Infect Control | INICC 45개국 630개 ICU 의료관련감염 데이터, 요로감염 포함 |
| [30219824](https://pubmed.ncbi.nlm.nih.gov/30219824/) | 2019 | Review | Clin Infect Dis | Ceftazidime-Avibactam 등 신장 용량 조절 관련 고찰 |
| [38688353](https://pubmed.ncbi.nlm.nih.gov/38688353/) | 2024 | Review | Int J Antimicrob Agents | 다제내성 그람음성간균 감염 치료 실무 가이드 (이탈리아·프랑스 학회) |
| [35787918](https://pubmed.ncbi.nlm.nih.gov/35787918/) | 2022 | Review | Int J Antimicrob Agents | 다제내성 그람음성균 신약 임상 데이터, CAZ-AVI 포함 |
| [37873539](https://pubmed.ncbi.nlm.nih.gov/37873539/) | 2023 | 미분류 | Open Med (Warsaw) | 만성신질환 환자 요로감염 유병률 및 항생제 감수성 조사 |
| [35734948](https://pubmed.ncbi.nlm.nih.gov/35734948/) | 2022 | 미분류 | Pediatrics | 3세대 세팔로스포린 내성 소아 요로감염 치료·역학 |

## 한국 시판 정보

현재 한국에 시판 중인 Ceftazidime 허가 제품이 없습니다(허가증 0건, 미상시판).

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. (주요 경고, 금기, DDI 데이터가 모두 미확보 상태이며, 특히 TFDA/한국 규제기관 인허가 경고·금기 정보 부재는 Blocking 등급 데이터 공백으로 분류되어 있어 안전성 초기 심사(S1) 자체가 불가능합니다.)

## 결론 및 다음 단계

**결정: Hold**

**사유:**
요로감염 적응증 자체의 임상 근거는 L1 수준으로 강하지만(17건 임상시험, 20편 문헌, 다수의 Phase 2~4 RCT), (1) 한국 내 시판 허가가 전무하고, (2) 허가사항 경고/금기 정보가 Blocking 등급 데이터 공백으로 안전성 초기 심사(S1)조차 진행할 수 없는 상태입니다. 근거는 있으나 규제·안전성 정보 부재로 다음 단계 진행이 불가합니다.

**진행하려면 필요한 것:**
- TFDA/한국 식약처 원본 허가사항(경고·금기) PDF 확보 및 파싱 (DG001, Blocking)
- DrugBank API를 통한 정확한 작용기전(MOA) 확인 (DG002, High)
- DDI 데이터베이스 재조회 (현재 not_found 상태)
- 국내 수입/시판 가능성 검토 (현재 허가 0건)
- 부차 후보인 감염성 중이염(rank 9, L3)에 대한 최신 대조군 연구 존재 여부 추가 확인
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

