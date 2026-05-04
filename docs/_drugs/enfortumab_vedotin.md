---
layout: default
title: Enfortumab Vedotin
parent: 僅模型預測 (L5)
nav_order: 245
evidence_level: L5
indication_count: 10
---

# Enfortumab Vedotin
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

# Enfortumab Vedotin: 요로상피암에서 HER2 양성 유방암으로

---

## 한 문장 요약

Enfortumab vedotin(EV)은 Nectin-4(PVRL4)를 표적으로 하는 항체-약물 복합체(ADC)로, 현재 국소 진행성/전이성 요로상피암(방광암) 치료에 FDA 승인을 받은 항암제입니다.
TxGNN 모델은 총 10개 적응증을 예측하였으며, 그 중 **HER2 양성 유방암(HER2 Positive Breast Carcinoma)**이 유일하게 임상시험 및 문헌 근거를 갖춘 실질적 재창출 후보로 확인됩니다.
현재 **4건의 임상시험**과 **4편의 문헌**이 이 방향을 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 요로상피암 (FDA 승인; 대만 미허가) |
| 예측 신규 적응증 | HER2 양성 유방암 (HER2 Positive Breast Carcinoma) |
| TxGNN 예측 점수 | 98.99% |
| 근거 수준 | L2 |
| 시판 현황 | 미허가 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 전체 예측 요약

이 보고서는 다중 적응증(multi-indication) 평가 패키지입니다. TxGNN이 예측한 상위 10개 적응증 및 권장 결정은 아래와 같습니다.

| 순위 | 예측 적응증 | TxGNN 점수 | 근거 수준 | 권장 결정 | 비고 |
|------|------------|-----------|---------|---------|------|
| 1 | 나병 (Leprosy) | 99.53% | L5 | Hold | 세균 감염 — ADC 기전 연결 없음 |
| 2 | 다발성 내분비 종양 (MEN) | 99.43% | L5 | Hold | KG 통용 '종양' 노드 과연결 추정 |
| 3 | 거대세포바이러스 감염 (CMV) | 99.36% | L5 | Hold | DNA 바이러스 감염 — ADC 무효 |
| 4 | 칸디다증 (Candidiasis) | 99.30% | L5 | Hold | 真菌 감염 — 유일 문헌은 EV 부작용 사례 |
| 5 | 뇌경색 (Cerebral Infarction) | 99.23% | L5 | Hold | 혈전/신경손상 — ADC 기전 완전 불일치 |
| 6 | HIV 감염 (HIV Infectious Disease) | 99.19% | L5 | Hold | 역전사바이러스 — 항바이러스 기전 없음 |
| 7 | 순수형 가족성 고콜레스테롤혈증 | 99.18% | L5 | Hold | 대사·유전 질환 — ADC 논리 없음 |
| 8 | 소 전염성 비기관염 (IBR) | 99.13% | L5 | Hold | **수의학적 질환** — 인체 적용 불가 |
| 9 | 악성 카타르 (Malignant Catarrh) | 99.13% | L5 | Hold | **수의학적 질환** — 인체 적용 불가 |
| **10** | **HER2 양성 유방암** | **98.99%** | **L2** | **✅ Proceed with Guardrails** | 임상시험 4건·문헌 4편 |

> **참고**: 순위 1–9의 높은 TxGNN 점수는 지식 그래프 내 면역 억제·피부·비특이적 종양 노드의 간접 연결에서 비롯된 것으로 추정됩니다. 생물학적 타당성이 없으며, 특히 순위 8·9는 수의학적 질환으로 인체 재창출 평가 대상에서 제외됩니다.

---

## 이 예측이 타당한 이유는?

Enfortumab vedotin은 Nectin-4(PVRL4)에 결합하는 완전 인간화 단클론항체에 MMAE(monomethyl auristatin E)를 링커로 연결한 ADC입니다. 종양 세포 표면의 Nectin-4에 결합 후 인터널리제이션이 일어나면 리소좀 내에서 링커가 절단되어 MMAE가 방출되고, MMAE는 미세소관 중합을 억제하여 G2/M 세포 주기 정지 및 아포토시스를 유발합니다.

HER2 양성 유방암 세포에서 Nectin-4는 약 58–75%의 발현율을 보이며, HER2 과발현과 양의 상관관계를 보입니다. 이는 EV가 trastuzumab emtansine(T-DM1)이나 trastuzumab deruxtecan(T-DXd) 같은 HER2 표적 ADC와 완전히 독립적인 표적 및 페이로드 기전을 제공함을 의미합니다. HER2 ADC에 내성을 보인 환자에서도 Nectin-4 발현이 유지되는 경우, EV는 유효한 구제 치료 전략이 될 수 있습니다.

EV-202 Phase 2 바스켓 시험(NCT04225117)이 HER2+ 유방암을 독립 코호트(Cohort H)로 포함한 것은 이 가설의 임상적 타당성을 직접 뒷받침하는 핵심 근거입니다. EV-202의 결과가 공개되면 현재 L2 근거 수준이 L1으로 상향 조정될 가능성이 있습니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT04225117](https://clinicaltrials.gov/study/NCT04225117) | Phase 2 | 모집 완료·진행 중 | 329 | **EV-202 바스켓 시험** — HER2+ 유방암 포함 다중 고형암 코호트에서 EV 단독(Cohort 1–8) 및 EV+펨브롤리주맙(Cohort 9) 병용의 ORR, OS, 안전성 평가. HER2+ 유방암 전용 코호트(Cohort H) 포함. 최고 직접 근거. |
| [NCT05097599](https://clinicaltrials.gov/study/NCT05097599) | Phase 2 | 조기 종료 | 11 | **StrataPATH 정밀의학 플랫폼** — 바이오마커 기반으로 FDA 승인 약물(EV 포함)을 새 적응증에 탐색. 입회 11명에 그쳐 조기 종료되어 데이터 가치 제한적. EV 재창출 개념을 지지. |
| [NCT07287995](https://clinicaltrials.gov/study/NCT07287995) | Phase 1b/2 | 모집 중 | 428 | **ASP2998(TROP2 ADC) + EV 병용** — TROP2 ADC인 ASP2998을 EV, 펨브롤리주맙, 카보플라틴과 병용하는 고형암 연구. EV가 병용 파트너로 포함됨. HER2+ 포함 다중 고형암 대상. |
| [NCT07309770](https://clinicaltrials.gov/study/NCT07309770) | Phase 2 | 모집 중 | 90 | **Trastuzumab Rezetecan(SYS6010)의 HER2+ 고형암 연구** — Extramammary Paget's Disease, 희귀 고형암, 요로상피암 3개 코호트. EV 직접 연구는 아니지만 HER2+ 종양에 대한 ADC 전략의 광범위한 적용 가능성을 시사. |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [41654096](https://pubmed.ncbi.nlm.nih.gov/41654096/) | 2026 | 체계적 고찰 / 실사용 근거 | Crit Rev Oncol Hematol | 최근 5년 승인 10개 항암제 실사용 근거 종합 — EV 포함. RCT 결과가 고령·동반질환 환자 등 실제 임상에서 어떻게 전환되는지 포괄적으로 평가. |
| [40614854](https://pubmed.ncbi.nlm.nih.gov/40614854/) | 2025 | 기전 연구 | Cancer Letters | 다배체 거대 암세포(PGCC)가 HER2 ADC(T-DM1, T-DXd, XMT-1522, Disitamab Vedotin) 내성을 매개함을 HER2+ 유방암(JIMT-1) 및 위암 세포주에서 규명. MMAE 계열 EV의 보완적 역할 가능성을 간접 시사. |
| [32315240](https://pubmed.ncbi.nlm.nih.gov/32315240/) | 2020 | 리뷰 | ASCO Educational Book | ADC 치료제의 부활 — 표적 선택, 항체, 링커, 페이로드 4가지 핵심 파라미터 포괄 검토. EV의 Nectin-4 표적·MMAE 페이로드 전략의 학문적 맥락 제공. |
| [41384708](https://pubmed.ncbi.nlm.nih.gov/41384708/) | 2026 | 리뷰 | Histopathology | 방광암 분자 병리 — KMT2D, KDM6A, TP53, PIK3CA, FGFR3 변이와 개인화 치료 통합 정리. EV 원래 적응증(방광암)의 분자적 배경 및 표적 치료 연계를 이해하는 데 참고. |

---

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | ADC (항체-약물 복합체) — MMAE(monomethyl auristatin E) 페이로드; 미세소관 중합 억제제 계열 (오리스타틴 유도체) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | CBC (분류 포함), 간신기능, 혈당 수치 (고혈당 보고), 말초신경병증 임상 평가 (MMAE 계열 표준 모니터링 항목) |
| 취급 방호 | 세포독성 약물 취급 규정 준수 필요 (항암제로 분류됨) |

---

## 안전성 고려사항

안전성 정보는 FDA 처방 정보(USPI)를 참조하세요. 대만/한국 허가사항은 현재 존재하지 않습니다.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
TxGNN이 예측한 10개 적응증 중 생물학적 타당성과 임상 근거를 모두 갖춘 유일한 후보는 **HER2 양성 유방암**입니다. Nectin-4의 HER2+ 유방암 내 높은 발현율(58–75%)과 HER2 ADC 내성 환자에서의 독립적 기전이 타당성을 뒷받침하며, EV-202 Phase 2 시험(NCT04225117)이 HER2+ 유방암 전용 코호트를 운영 중이라는 점이 핵심 근거입니다. 나머지 9개 예측은 감염성 질환(바이러스·세균·진균), 대사·유전 질환, 수의학적 질환으로 ADC 재창출 논리가 성립하지 않으므로 모두 Hold가 권고됩니다.

**진행하려면 필요한 것:**
- EV-202(NCT04225117) HER2+ 유방암 코호트 결과 공개 추적 모니터링 (근거 수준 L1 상향 가능성)
- EV의 상세 작용 기전 데이터 보완 (DrugBank API 조회 또는 FDA 라벨 파싱 — DG002 해소)
- 대만/한국 허가 전략 수립을 위한 규제 사전 상담 (현재 양국 미허가)
- Nectin-4 동반 진단(Companion Diagnostic) 필요 여부 규명
- 안전성 정보 수집 (TFDA/MFDS 허가 신청 시 필요 — DG001 해소)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

