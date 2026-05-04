---
layout: default
title: Durvalumab
parent: 僅模型預測 (L5)
nav_order: 235
evidence_level: L5
indication_count: 10
---

# Durvalumab
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

# Durvalumab: 면역항암 치료에서 전립선 요도 이행세포암으로

---

## 한 문장 요약

Durvalumab은 PD-L1 면역관문을 차단하는 단클론 항체로, 비소세포폐암·담도암 등 다양한 암종에서 글로벌 승인을 받은 면역항암제이나 한국에는 미허가 상태입니다.
TxGNN 모델은 **전립선 요도 이행세포암(Prostatic Urethra Urothelial Carcinoma)**에 효과가 있을 수 있다고 예측하며(예측 점수: 99.98%),
현재 이 특정 적응증에 대한 임상시험 및 문헌 근거는 확인되지 않아 자체 근거 수준은 L5에 해당합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 한국 미허가 (글로벌: 비소세포폐암, 담도암, 간세포암 등 다수 허가) |
| 예측 신규 적응증 | 전립선 요도 이행세포암 (Prostatic Urethra Urothelial Carcinoma) |
| TxGNN 예측 점수 | 99.98% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

Durvalumab은 PD-L1(Programmed Death-Ligand 1)에 선택적으로 결합하는 인간화 IgG1κ 단클론 항체입니다. Evidence Pack에 작용 기전 상세 데이터는 포함되어 있지 않으나, Durvalumab은 AstraZeneca의 Imfinzi®로 알려진 항 PD-L1 면역관문 억제제로, PD-L1/PD-1 및 PD-L1/CD80 신호 축을 차단함으로써 종양 미세환경 내 면역억제를 해제하고 T 세포 매개 항종양 반응을 회복시키는 기전을 갖습니다.

요로상피암(Urothelial Carcinoma)은 면역관문 억제제 치료에 반응하는 대표적 암종 중 하나로, 전반적으로 PD-L1 고발현 빈도가 높고 종양 돌연변이 부담(TMB)도 상대적으로 높습니다. 이러한 이유로 방광암·상부 요로 이행세포암을 포함한 광의의 요로상피암에 대한 다양한 면역관문 억제제 연구가 진행되어 왔으며, Durvalumab 역시 이 계열에서 임상 개발 이력을 갖고 있습니다.

다만, **전립선 요도 이행세포암은 요로상피암의 극히 드문 해부학적 아형**입니다. TxGNN 모델의 예측은 광의의 요로상피암에 대한 PD-L1 억제 기전의 유사성에 근거한 외삽(extrapolation)으로 해석되며, 이 특정 아형에서의 PD-L1 발현율 데이터는 현재 문헌에 존재하지 않습니다. 기전적 타당성은 존재하나, 직접적 임상 근거 없이는 진행을 권장하기 어렵습니다.

---

## 임상시험 근거

현재 전립선 요도 이행세포암(Prostatic Urethra Urothelial Carcinoma)에 대한 Durvalumab 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 전립선 요도 이행세포암(Prostatic Urethra Urothelial Carcinoma)에 대한 관련 문헌이 없습니다.

---

## 한국 시판 정보

Durvalumab은 현재 한국 내 허가 및 시판 이력이 없습니다. (허가증 0건, 시판 현황: 미시판)

---

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 면역치료 (Anti-PD-L1 면역관문 억제제 — 전통적 세포독성 약물 아님) |
| 골수억제 위험 | 낮음 (직접적 골수독성 기전 없음; 면역 관련 혈액학적 이상반응 가능) |
| 구토 유발성 등급 | 낮음 |
| 모니터링 항목 | 갑상선 기능, 간기능(AST/ALT/빌리루빈), 혈당, 부신 기능, 폐 기능(폐렴 감시), CBC (면역 관련 이상반응 조기 감지 목적) |
| 취급 방호 | 생물학적 제제 취급 규정 준수 필요; 전통적 세포독성 약물 수준의 격리 방호는 불필요 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 참고: 전체 예측 적응증 요약

본 보고서는 다중 적응증 예측 결과(TW-DB11714-multi)를 포함하고 있습니다. 아래는 상위 10개 예측 적응증 및 각 근거 수준 요약입니다.

| 순위 | 예측 적응증 | TxGNN 점수 | 근거 수준 | 임상시험 | 문헌 | 권장 결정 |
|------|-----------|-----------|---------|---------|------|---------|
| 1 | Prostatic Urethra Urothelial Carcinoma | 99.98% | L5 | 0건 | 0편 | Hold |
| 2 | Kidney Pelvis Sarcomatoid Transitional Cell Carcinoma | 99.98% | L4 | 1건 | 0편 | Research Question |
| 3 | Infiltrating Bladder Urothelial Carcinoma Sarcomatoid Variant | 99.98% | L3 | 2건 | 0편 | Research Question |
| 4 | Renal Pelvis Papillary Urothelial Carcinoma | 99.98% | L5 | 0건 | 0편 | Hold |
| 5 | Uterine Ligament Adenocarcinoma | 99.92% | L5 | 0건 | 0편 | Hold |
| 6 | **Endocervical Carcinoma** | 99.91% | **L2** | 2건 | 1편 | **Proceed with Guardrails** |
| 7 | Adenoid Cystic Carcinoma of the Cervix Uteri | 99.91% | L5 | 0건 | 0편 | Hold |
| 8 | Uterine Ligament Serous Adenocarcinoma | 99.91% | L5 | 0건 | 0편 | Hold |
| 9 | Signet Ring Cell Variant Cervical Mucinous Adenocarcinoma | 99.90% | L5 | 0건 | 0편 | Hold |
| 10 | Intestinal Variant Cervical Mucinous Adenocarcinoma | 99.90% | L5 | 0건 | 0편 | Hold |

> **주목할 적응증**: 순위 6위인 **자궁내경부암(Endocervical Carcinoma)**이 L2 수준으로 가장 강한 근거를 보유하며, 권장 결정이 **Proceed with Guardrails**로 상향됩니다. 아래 섹션에서 해당 근거를 별도로 제시합니다.

---

### 자궁내경부암 (Endocervical Carcinoma) — 상위 근거 적응증 상세

#### 이 예측이 타당한 이유는?

자궁내경부암(Endocervical Carcinoma)은 대부분 HPV(인유두종바이러스) 감염에 의해 구동되는 악성 종양입니다. HPV는 종양 세포의 PD-L1 발현을 인터페론 신호 경로를 통해 상향 조절하여 면역 억제적 종양 미세환경을 형성합니다. Durvalumab의 PD-L1/PD-1 축 차단 기전은 HPV 특이적 T 세포의 세포독성 기능을 회복시킬 수 있어 강한 기전적 합리성을 갖습니다.

추가적으로, 자궁경부암 방사선 치료 후 PD-L1 발현 상향 조절 및 면역원성 세포사(immunogenic cell death) 기전이 면역-방사선 병용 전략을 지지합니다. 이는 아래 임상시험(NCT03452332)의 설계 근거와 일치합니다.

#### 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT04065269](https://clinicaltrials.gov/study/NCT04065269) | Phase 2 | 모집 완료(결과 대기) | 174 | ATARI 시험: ATR 억제제(ceralasertib) + Olaparib 또는 Durvalumab 병용, ARID1A 결손 포함 부인과 암(자궁경부암 포함) 대상; DNA 손상 복구 결손 선별 환자군 |
| [NCT03452332](https://clinicaltrials.gov/study/NCT03452332) | Phase 1 | 완료 | 20 | 저분할 방사선 치료 + Durvalumab + Tremelimumab 병용, 재발/전이성 자궁경부암·질암·외음부암 대상; 방사선-면역 병용 초기 안전성 데이터 확보 |

#### 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [37467967](https://pubmed.ncbi.nlm.nih.gov/37467967/) | 2023 | Narrative Review | Biomedical Journal | 자궁경부 소세포 신경내분비암(SCNECC)의 분자 기전 및 치료 전략 고찰; HPV 관련성, 면역치료 가능성 포함 |

---

## 결론 및 다음 단계

### 주요 예측 적응증 (Rank 1: 전립선 요도 이행세포암)

**결정: Hold**

**사유:**
전립선 요도 이행세포암은 극히 드문 요로상피암 아형으로, 현재 Durvalumab에 대한 임상시험 및 문헌 근거가 전혀 없습니다(근거 수준 L5). PD-L1 발현율 등 기전적 연결 근거도 이 특정 해부학적 아형에서는 확인된 바 없어 현 단계에서 진행하기 어렵습니다.

**진행하려면 필요한 것:**
- 전립선 요도 이행세포암에서의 PD-L1 발현율 및 TMB 데이터
- 광의의 요로상피암 Durvalumab 임상시험 결과의 이 아형 외삽 타당성 검토
- Durvalumab 상세 작용 기전(MOA) 데이터 보충 (DrugBank API 조회 필요)
- 한국 허가사항 및 안전성 정보 확보 (MFDS 데이터 조회 필요)

---

### 우선 검토 권장 적응증 (Rank 6: 자궁내경부암)

**결정: Proceed with Guardrails**

**사유:**
자궁내경부암은 HPV-PD-L1 축의 강한 기전적 연결성을 보유하며, Phase 1 완료 임상시험(NCT03452332, n=20) 및 Phase 2 진행 중 대규모 시험(NCT04065269, n=174)이 근거를 뒷받침합니다. 근거 수준 L2로 본 Evidence Pack 내 최고 수준에 해당하며, 진행 가능한 연구 질문으로 발전시킬 여건이 갖추어져 있습니다.

**진행하려면 필요한 것:**
- NCT04065269 시험의 자궁내경부암 세부 코호트 결과 모니터링
- 한국 MFDS 허가 현황 및 보험 급여 조건 확인
- HPV+ 환자 선별 바이오마커(PD-L1 CPS, TMB) 기반 환자 선정 기준 수립
- 면역 관련 이상반응(irAE) 관리 프로토콜 및 한국 임상 가이드라인 검토
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

