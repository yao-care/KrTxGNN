---
layout: default
title: Olaparib
parent: 모델 예측만 (L5)
nav_order: 561
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Olaparib: 예측 신규 적응증 여성 유방암 (female breast carcinoma) (근거 수준 L5). 기존 적응증: 허가 적응증 원문은 링크 형태로만 제공되어 본문을 확인할 수 없음 (허가사항 참조 필요)"
monitor_inn: "OLAPARIB"
predicted_indications: ["female breast carcinoma"]
---

# Olaparib
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **1** 건
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

# Olaparib: 난소암 등 BRCA 변이 암에서 여성 유방암으로

## 한 문장 요약

Olaparib은 PARP 억제제로, 한국에서 린파자정(100mg, 150mg)으로 허가·시판되고 있습니다. TxGNN 모델은 **여성 유방암(female breast carcinoma)**에 효과가 있을 수 있다고 예측하며, 이 방향을 지지하는 **임상시험 30건**과 **문헌 20편**이 확인되었습니다. 이 중 Phase 3 무작위 대조시험(OlympiAD, OlympiA)이 포함되어 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 원문은 링크 형태로만 제공되어 본문을 확인할 수 없음 (허가사항 참조 필요) |
| 예측 신규 적응증 | 여성 유방암 (female breast carcinoma) |
| TxGNN 예측 점수 | 99.09% |
| 근거 수준 | L1 (문헌상 Phase 3 RCT 다수 확인, 아래 참고) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 2건 |
| 권장 결정 | Proceed with Guardrails |

> 참고: 근거 수준 L1은 문헌으로 확인된 Phase 3 RCT(OlympiAD, OlympiA)에 근거한 판정입니다. 위 임상시험 목록에서 완료된 Phase 3 시험은 난소암 대상 시험(NCT02282020)뿐이므로, 유방암 적응증의 L1 판정은 문헌에 의존합니다.

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 약리학적 정보에 따르면, Olaparib은 PARP 억제제로서 상동재조합 복구(HRR) 결핍 종양에서 합성 치사(synthetic lethality)를 일으킵니다. BRCA1/2 기능이 소실되면 이중가닥 손상 복구가 어려워지고, PARP 억제로 PARP 포획과 복구되지 않은 DNA 손상이 누적되어 종양세포가 사멸합니다.

이 기전은 생식세포 BRCA1/2 변이 유방암에 직접 적용됩니다. TBCRC 048 연구처럼 PALB2 등 다른 HRR 유전자 변이를 가진 하위군으로도 확장될 가능성이 있습니다. 높은 TxGNN 점수는 이러한 생물학적 근거와 일치합니다.

다만 효과는 바이오마커(생식세포 BRCA1/2 변이, HER2 음성)에 의존하므로, 선별되지 않은 유방암 전체로 일반화해서는 안 됩니다. 또한 유방암은 이미 여러 국가에서 olaparib의 승인 적응증일 가능성이 높아, 진정한 재창출이라기보다 적응증 확인에 가까울 수 있습니다. 한국 허가사항과 대조하여 확인해야 합니다.

## 임상시험 근거

관련성이 높은 시험을 중심으로 정리했습니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00679783](https://clinicaltrials.gov/study/NCT00679783) | Phase 2 | 완료 | 99 | BRCA 변이 유방암·난소암에서 olaparib(AZD2281)의 반응률을 평가한 비무작위 시험 |
| [NCT04683679](https://clinicaltrials.gov/study/NCT04683679) | Phase 2 | 모집 중 | 34 | 전이성 삼중음성 유방암에서 펨브롤리주맙+방사선요법에 olaparib 추가 여부 비교 |
| [NCT04330040](https://clinicaltrials.gov/study/NCT04330040) | Phase 4 | 완료 | 202 | 인도 환자 대상 시판 후 연구(난소암 및 생식세포 BRCA 변이 전이성 유방암) |
| [NCT01116648](https://clinicaltrials.gov/study/NCT01116648) | Phase 1/2 | 활성(모집 종료) | 155 | 재발성 삼중음성 유방암 등에서 cediranib+olaparib 병용 vs olaparib 단독 |
| [NCT02418624](https://clinicaltrials.gov/study/NCT02418624) | Phase 1 | 완료 | 25 | BRCA 변이 HER2 음성 진행성 유방암에서 카보플라틴+olaparib 병용의 권장 용량 탐색 |
| [NCT01623349](https://clinicaltrials.gov/study/NCT01623349) | Phase 1 | 완료 | 118 | 재발성 삼중음성 유방암·고등급 장액성 난소암에서 PI3K 억제제+olaparib 병용 안전성 |
| [NCT05358639](https://clinicaltrials.gov/study/NCT05358639) | Phase 1 | 활성(모집 종료) | 36 | 삼중음성 유방암 및 난소암에서 olaparib+navitoclax 병용 안전성 |
| [NCT03109080](https://clinicaltrials.gov/study/NCT03109080) | Phase 1 | 완료 | 24 | 삼중음성 유방암에서 olaparib+방사선요법 |
| [NCT07695259](https://clinicaltrials.gov/study/NCT07695259) | Phase 4 | 모집 중 | 45 | 고령 HER2 양성 유방암 신보조요법에서 olaparib+트라스투주맙+퍼투주맙 |
| [NCT01237067](https://clinicaltrials.gov/study/NCT01237067) | Phase 1 | 완료 | 77 | 재발성 여성암에서 olaparib+카보플라틴의 PK/PD 및 안전성 |

대부분이 초기 단계 또는 병용요법 시험이며, 일부(NCT04330040 등)는 유방암과의 직접 관련성을 추가 확인해야 합니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [34081848](https://pubmed.ncbi.nlm.nih.gov/34081848/) | 2021 | RCT | N Engl J Med | OlympiA: BRCA1/2 변이 조기 유방암에서 보조요법 olaparib 효과 |
| [36228963](https://pubmed.ncbi.nlm.nih.gov/36228963/) | 2022 | RCT | Ann Oncol | OlympiA 전체 생존율 분석: 고위험 조기 유방암(생식세포 BRCA1/2 변이)에서 보조 olaparib 평가 |
| [28578601](https://pubmed.ncbi.nlm.nih.gov/28578601/) | 2017 | RCT | N Engl J Med | OlympiAD: 생식세포 BRCA 변이 전이성 유방암에서 olaparib 효능 |
| [30689707](https://pubmed.ncbi.nlm.nih.gov/30689707/) | 2019 | RCT | Ann Oncol | OlympiAD 최종 전체 생존 및 내약성 결과(olaparib vs 의사 선택 화학요법) |
| [36893711](https://pubmed.ncbi.nlm.nih.gov/36893711/) | 2023 | RCT 추적 | Eur J Cancer | OlympiAD 연장 추적: 최종 분석 전체 생존 중앙값 olaparib 19.3개월 vs 17.1개월(P=0.513) |
| [33119476](https://pubmed.ncbi.nlm.nih.gov/33119476/) | 2020 | Phase 2 | J Clin Oncol | TBCRC 048: 체세포 BRCA1/2 또는 기타 HRR 유전자 변이 전이성 유방암에서 olaparib 반응 평가 |
| [34143979](https://pubmed.ncbi.nlm.nih.gov/34143979/) | 2021 | Phase 2 | Cancer Cell | I-SPY2: 더발루맙+olaparib+파클리탁셀이 HER2 음성 유방암에서 pCR률 증가 |
| [25366685](https://pubmed.ncbi.nlm.nih.gov/25366685/) | 2015 | 임상 연구 | J Clin Oncol | 생식세포 BRCA1/2 변이 진행성 암에서 olaparib 단독요법 |
| [29582690](https://pubmed.ncbi.nlm.nih.gov/29582690/) | 2018 | Review | Expert Rev Anticancer Ther | 유방암에서 olaparib의 기전, 약동학 및 임상 데이터 개관 |
| [35163586](https://pubmed.ncbi.nlm.nih.gov/35163586/) | 2022 | Review | Int J Mol Sci | 화학요법 저항성 삼중음성 유방암의 기전과 치료 전략 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201907537 | 린파자정100밀리그램(올라파립) | 노란색 내지 어두운 노란색의 양면이 볼록한 타원형의 필름코팅정 | 허가사항 참조 (원문은 MFDS 링크로만 제공) |
| 201907536 | 린파자정150밀리그램(올라파립) | 초록색 내지 회녹색의 양면이 볼록한 타원형의 필름코팅정 | 허가사항 참조 (원문은 MFDS 링크로만 제공) |

두 제품 모두 한국아스트라제네카(주)가 허가를 보유하고 있습니다.

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적치료제 (PARP 억제제) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 취급 방호 | 허가사항의 경고 및 주의사항을 참조하세요 |

## 안전성 고려사항

- **약물 상호작용**: 조회된 상호작용은 총 100건이며, 이 중 일부를 확인했습니다.
  - **Major**: Aprepitant, Dexamethasone, Clarithromycin
  - **Moderate**: Metformin, Alosetron, Bupropion, Cimetidine, Eluxadoline, Naldemedine, Metreleptin, Miconazole, Nitisinone, Cisapride, Clotrimazole, Glyburide, Ondansetron, Repaglinide, Rosuvastatin, Simvastatin
  - **Minor**: Prucalopride

주요 경고와 금기는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
생식세포 BRCA1/2 변이 유방암에서 Phase 3 RCT(OlympiAD, OlympiA)가 olaparib의 효과를 지지하며, 작용 기전도 타당합니다. 다만 효과가 바이오마커에 의존하므로 환자 선별이 필수입니다.

**진행하려면 필요한 것:**
- 한국 허가사항(MFDS 첨부문서) 확인: 유방암이 이미 허가 적응증인지 판단하고, 경고·금기 정보 확보
- 상세한 약물 작용 기전(MOA) 데이터 보완
- 생식세포 BRCA1/2 변이 검사 기반의 환자 선별 기준 마련 (HER2 음성 등)
- 주요 병용금기 약물(Major 수준 상호작용) 관리 계획 수립
- 유방암과의 관련성이 불분명한 시험(예: NCT04330040)의 적응증 일치 여부 검증
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

