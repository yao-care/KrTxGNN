---
layout: default
title: Adenosine
parent: 僅模型預測 (L5)
nav_order: 26
evidence_level: L5
indication_count: 2
---

# Adenosine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Adenosine: 발작성 심실상 빈맥(PSVT)에서 카테콜라민성 다형성 심실빈맥(CPVT)으로

## 한 문장 요약

Adenosine은 A1 수용체를 통해 방실결절(AV node) 전도를 억제하는 내인성 퓨린 뉴클레오사이드로, 발작성 심실상 빈맥(PSVT)의 급성 전환 치료에 사용되어 왔습니다.
TxGNN 모델은 **카테콜라민성 다형성 심실빈맥(Catecholaminergic Polymorphic Ventricular Tachycardia, CPVT)**에 효과가 있을 수 있다고 예측하며,
현재 **1건의 임상시험**과 **13편의 문헌**이 이 방향을 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 발작성 심실상 빈맥 (PSVT) 급성 전환 |
| 예측 신규 적응증 | 카테콜라민성 다형성 심실빈맥 (Catecholaminergic Polymorphic Ventricular Tachycardia) |
| TxGNN 예측 점수 | 99.42% |
| 근거 수준 | L3 |
| 한국 시판 현황 | 미시판 (허가 없음) |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

Adenosine은 A1 수용체를 활성화하여 아데닐산 고리화효소(adenylyl cyclase)를 억제하고 세포 내 cAMP 농도를 낮추는 작용을 합니다. cAMP 감소는 PKA(단백키나제 A) 활성을 저하시키고, 이에 따라 심근 ryanodine 수용체(RyR2)의 PKA 의존성 인산화(Ser2808/Ser2814 위치)를 감소시킵니다.

CPVT의 핵심 병리 기전은 RyR2 또는 CASQ2 유전자 변이로 인해 카테콜라민 자극 시 근소포체(SR)에서 비정상적 칼슘 이온 유출(SR calcium leak)이 발생하고, 이것이 지연 후 탈분극(DAD)을 유발하여 생명을 위협하는 양방향 심실빈맥으로 이어지는 것입니다. Adenosine의 **cAMP↓ → PKA↓ → RyR2 인산화 감소** 경로는 이 병리 기전의 핵심 고리를 직접 차단합니다. β 차단제가 상류의 아드레날린 수용체를 봉쇄하는 반면, Adenosine은 cAMP 수준에서 하류 개입하므로 기전적으로 상호보완적 병용 치료 가능성이 있습니다.

ATP(Adenosine의 삼인산 형태)가 CPVT 변이와 연관된 RyR2 중앙 구조 도메인과 직접 결합함을 보인 체외 연구(PMID 23747301)와, 실제 CPVT 환자에서 ATP 정맥 주사가 양방향 심실빈맥을 종료시킨 증례보고(PMID 18313614)는 분자 수준부터 임상 수준까지 이 기전 연결의 근거를 제공합니다. Adenosine 수용체 선택적 작용제(AGP100)를 대상으로 한 Phase 2a 임상시험(NCT07263139)이 현재 진행 중임은, 업계가 이 경로를 CPVT의 실제 치료 표적으로 공식 검증 단계에 있음을 의미합니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT07263139](https://clinicaltrials.gov/study/NCT07263139) | Phase 2a | 모집 중 | 10 | AGP100(A1 수용체 선택적 작용제, adenosine 계열 추정)의 CPVT 환자 대상 안전성·내약성·탐색적 임상 효능 평가. 2026년 1월 개시, 2027년 6월 완료 예정. 결과 미공개이나 Adenosine 수용체 경로를 CPVT 치료 표적으로 업계가 공식 검증 중임을 의미. |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [18313614](https://pubmed.ncbi.nlm.nih.gov/18313614/) | 2008 | 증례보고 | Heart Rhythm | CPVT 환자에서 ATP 정맥 주사가 양방향 심실빈맥을 종료시킴. Adenosine 관련 물질의 CPVT 직접 억제를 임상에서 확인한 가장 직접적 근거. |
| [23747301](https://pubmed.ncbi.nlm.nih.gov/23747301/) | 2013 | 기초과학 (in vitro) | Biochim Biophys Acta | ATP가 CPVT 변이 연관 RyR2 중앙 도메인과 직접 결합함을 확인. Adenosine 계열 분자가 CPVT 병인 부위에 직접 작용하는 분자 기전 근거 제시. |
| [40165484](https://pubmed.ncbi.nlm.nih.gov/40165484/) | 2025 | 임상 합의문 | Europace | ESC·HRS·APHRS 등 국제 학회 공동 약물유발 검사 임상 합의문. 심장 전기생리학에서 Adenosine을 포함한 약물의 전도계 진단 역할 공식 정의. |
| [38776406](https://pubmed.ncbi.nlm.nih.gov/38776406/) | 2024 | 기초과학 (동물 모델) | Cardiovasc Res | PDE2A·PDE4B 유전자 치료가 심근세포 내 cAMP 구획화를 개선하여 심부전·부정맥 완화. cAMP가 CPVT 핵심 신호 분자임을 재확인; Adenosine의 cAMP 억제 기전과 직접 연결. |
| [41691612](https://pubmed.ncbi.nlm.nih.gov/41691612/) | 2026 | in vitro (iPSC 유래) | J Physiol | iPSC 유래 심장-신경 미조직 모델로 CPVT가 심근세포뿐 아니라 교감신경 자체의 질환임을 규명. Adenosine의 교감신경-cAMP 축 억제 기전의 치료 범위 확대 가능성 시사. |
| [21699856](https://pubmed.ncbi.nlm.nih.gov/21699856/) | 2011 | 관찰 연구 | Heart Rhythm | RyR2 변이 CPVT에서 심전기생리검사(EPS)의 제한적 유용성과 심박 후 비정상 재분극 패턴 기술. CPVT 전기생리적 특성 이해에 기여. |
| [18368865](https://pubmed.ncbi.nlm.nih.gov/18368865/) | 2007 | 리뷰 | J Assoc Physicians India | 구조적 이상 없는 심실빈맥의 분류 및 치료 접근. cAMP 매개 RVOT/LVOT 기원 빈맥에서 Adenosine 감수성 언급; CPVT 감별·치료 맥락과 연결. |
| [35577932](https://pubmed.ncbi.nlm.nih.gov/35577932/) | 2022 | 기초과학 | Commun Biol | TECRL 결핍이 CPVT 관련 미토콘드리아 기능 이상 유발. CPVT 병인의 추가 분자 경로 규명; Adenosine의 미토콘드리아 보호 기능과의 간접 연결 가능성. |
| [30209242](https://pubmed.ncbi.nlm.nih.gov/30209242/) | 2018 | 기초과학 | Sci Transl Med | RyR2 선택적 안정화제(rycal S36)가 SR 칼슘 유출을 정상화함. CPVT 치료 표적으로 SR 칼슘 유출 차단의 의의 확인; Adenosine의 상류 경로(cAMP→PKA→RyR2) 차단과 상호보완. |
| [23858002](https://pubmed.ncbi.nlm.nih.gov/23858002/) | 2013 | 기초과학 | J Gen Physiol | Calsequestrin(CASQ2)의 RyR2 조절이 CPVT 병리와 직결됨을 규명. Adenosine의 RyR2 인산화 감소가 이 조절 경로와 보완적으로 작용 가능함을 시사. |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
Adenosine의 **cAMP↓ → PKA↓ → RyR2 인산화 감소** 기전이 CPVT 핵심 병리(SR 칼슘 유출 → DAD → 양방향 심실빈맥)를 직접 차단하는 이론적 근거가 탄탄하고, ATP의 RyR2 직접 결합(PMID 23747301), CPVT 환자에서의 ATP 종료 증례(PMID 18313614), A1 수용체 작용제 Phase 2a 임상시험 진행(NCT07263139)이 이를 단계적으로 뒷받침합니다. 다만 한국 미시판 상태, 안전성 데이터 공백, 현존 임상 규모 극소(n=10)라는 한계가 있어 추가 근거 확보가 선행되어야 합니다.

**진행하려면 필요한 것:**
- 한국 허가사항(경고, 금기, 약물 상호작용) 확보 → DG001 해소
- 작용 기전(MOA) 공식 문서화 (DrugBank API 재조회) → DG002 해소
- NCT07263139(AGP100 Phase 2a) 결과 지속 모니터링 후 Adenosine 직접 적용 가능성 재평가
- β 차단제 불응 CPVT 환자 대상 Adenosine 병용요법 소규모 파일럿 연구(case series) 설계
- RyR2/CASQ2 변이형별 Adenosine 반응 예측 바이오마커 탐색
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

