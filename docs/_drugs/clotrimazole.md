---
layout: default
title: Clotrimazole
parent: 僅模型預測 (L5)
nav_order: 182
evidence_level: L5
indication_count: 3
---

# Clotrimazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Clotrimazole: 진균 감염에서 외음질염으로

## 한 문장 요약

Clotrimazole은 에르고스테롤 합성을 억제하는 광범위 아졸계 항진균제로, 전 세계적으로 무좀·어루러기·칸디다증 치료에 사용되어 왔습니다.
TxGNN 모델은 **외음질염(Vulvovaginitis)**을 가장 근거 수준이 높은 실행 가능 적응증으로 예측하며 (예측 점수 99.59%), 현재 **22건의 임상시험**과 **20편의 문헌**이 이를 지지합니다.
한국에는 현재 미상장 상태이나, 다수의 완료된 Phase 3 RCT를 포함한 L1 수준의 글로벌 근거가 한국 도입을 강력히 뒷받침합니다.

> **선정 근거**: TxGNN rank 1은 여드름(acne, 99.86%)이나 근거 수준 L4·Hold로 평가됨. 외음질염(rank 2, 99.59%)이 L1 근거와 함께 실행 가능한 1순위 후보로 선정됨.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 진균 감염 (칸디다증, 피부사상균증, 어루러기) |
| 예측 신규 적응증 | 외음질염 (Vulvovaginitis) |
| TxGNN 예측 점수 | 99.59% |
| 근거 수준 | L1 |
| 한국 시판 현황 | ✗ 미상장 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

Clotrimazole은 아졸계 항진균제로, 진균 세포막 필수 구성 성분인 에르고스테롤의 생합성을 차단합니다. 구체적으로 라노스테롤의 14α-탈메틸화를 촉매하는 CYP51 효소를 억제하여 에르고스테롤 고갈과 세포막 투과성 장애를 유발, 진균 성장을 억제합니다. *Candida albicans*, *C. glabrata*, *C. tropicalis* 등 주요 칸디다 균종에 대해 낮은 최소억제농도(MIC)를 나타내며, 질정·크림 외용 제형에서 전신 흡수가 극히 낮아 우수한 국소 안전성을 보입니다.

외음질염의 주요 원인 중 하나인 외음질 칸디다증(VVC)은 전 세계 가임기 여성의 약 75%가 일생에 한 번 이상 경험하는 흔한 진균 감염입니다. VVC의 80–90%가 *C. albicans*에 의해 발생하므로, 에르고스테롤 억제 기전은 이 질환의 병원균에 직접 적용됩니다. Clotrimazole 국소 투여(질정 100–500 mg, 크림 1–2%)는 미국 CDC·WHO·유럽 가이드라인에서 VVC 1차 치료제로 확립되어 있습니다.

TxGNN 고득점(99.59%)은 이러한 기전적 타당성과 정확히 일치합니다. Clotrimazole은 미국·일본·유럽 등 주요 국가에서 이미 VVC 허가를 보유한 성숙한 글로벌 표준 치료제이며, 한국 미상장이라는 규제 공백이 명확한 도입 기회를 형성합니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00755053](https://clinicaltrials.gov/study/NCT00755053) | Phase 3 | 완료 | 466 | Clotrimazole ovule 500mg vs 기존 질정 500mg 비열등성 확인 — Clotrimazole을 연구약으로 한 직접 Phase 3 근거 |
| [NCT02180828](https://clinicaltrials.gov/study/NCT02180828) | Phase 4 | 완료 | 240 | 중증 VVC에서 Clotrimazole 질정 vs Fluconazole 경구제 무작위 대조 시험 — 효능·안전성 직접 비교 |
| [NCT00313131](https://clinicaltrials.gov/study/NCT00313131) | Phase 3 | 완료 | 1,524 | Tinidazole+Fluconazole 단회 vs Metronidazole+Clotrimazole 병용 요법 비교 — Clotrimazole 포함 대형 실효성 RCT |
| [NCT01335373](https://clinicaltrials.gov/study/NCT01335373) | 관찰 연구 | 완료 | 13,024 | VVC 포함 질염 현실 세계 관찰 연구 — Clotrimazole이 비교 기준, 방대한 실사용 안전성 데이터 |
| [NCT03599323](https://clinicaltrials.gov/study/NCT03599323) | 상장후 | 완료 | 1,033 | Empecid L Cream(Clotrimazole 1%) 약국 지도하 안전성 조사 — 허가 신청 참고 가능한 PMS 데이터 |
| [NCT04699240](https://clinicaltrials.gov/study/NCT04699240) | Phase 4 | 완료 | 140 | 재발성 VVC에서 Clotrimazole 질정 + 경구 유산균 vs 단독 비교 — 재발 예방 병용 전략 근거 |
| [NCT02248506](https://clinicaltrials.gov/study/NCT02248506) | Phase 4 | 완료 | 56 | 급성 VVC 치료 후 임상·균학적 치료율 및 재발 추적 — 균학적 치료율 세부 데이터 |
| [NCT06835361](https://clinicaltrials.gov/study/NCT06835361) | Phase 2/3 | 모집 중 | 264 | Clotrimazole+Lactulose 복합 질좌제 vs Clotrimazole 단독 우월성 비교 — Clotrimazole 단독이 표준 대조군 |
| [NCT03115073](https://clinicaltrials.gov/study/NCT03115073) | Phase 2/3 | 완료 | 84 | ProF-001/Candiplus® 3개 용량 vs Clotrimazole 1% 질크림 용량-반응 비교 — Clotrimazole이 활성 대조약 |
| [NCT04813822](https://clinicaltrials.gov/study/NCT04813822) | Phase 2 | 불명 | 90 | Miconazole 2%+Domiphen 질크림 vs 활성 대조약 급성 VVC — 최종 결과 발표 여부 확인 필요 |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [41765149](https://pubmed.ncbi.nlm.nih.gov/41765149/) | 2026 | RCT | Complementary Therapies in Medicine | Clotrimazole 질크림 vs Prangos ferulacea 크림 VVC 직접 비교 — 최신 RCT, Clotrimazole이 표준 대조약 |
| [39824974](https://pubmed.ncbi.nlm.nih.gov/39824974/) | 2025 | RCT | Scientific Reports | Mycozin vs Clotrimazole 1% 삼중맹검 대등성 RCT (n=126) — 현행 표준 치료제로서 Clotrimazole 지위 재확인 |
| [30565745](https://pubmed.ncbi.nlm.nih.gov/30565745/) | 2019 | RCT | Mycoses | 재발성 VVC에서 유산균+락토페린 유지 치료 효능 RCT — Clotrimazole 기반 급성기 치료 후 유지 전략 |
| [27880086](https://pubmed.ncbi.nlm.nih.gov/27880086/) | 2017 | RCT | Women & Health | Calendula officinalis vs Clotrimazole 질크림 삼중맹검 RCT (n=150) — 임상·검사실 효능 직접 비교 |
| [3895960](https://pubmed.ncbi.nlm.nih.gov/3895960/) | 1985 | RCT | Am J Obstet Gynecol | Clotrimazole 1회 500mg vs 6일 100mg 질정 RCT (n=199) — 단회 고용량 요법 근거 확립 |
| [2644595](https://pubmed.ncbi.nlm.nih.gov/2644595/) | 1989 | 임상 연구 | Obstetrics and Gynecology | 재발성·만성 VVC에서 Clotrimazole 유지 치료 — 90.4% 임상 관해율, 월 1회 예방 요법 근거 |
| [24863842](https://pubmed.ncbi.nlm.nih.gov/24863842/) | 2014 | Review | J Applied Microbiology | Clotrimazole 포괄 리뷰 — 항진균 기전, VVC 임상 근거, 신규 용도 가능성 총정리 |
| [39419780](https://pubmed.ncbi.nlm.nih.gov/39419780/) | 2024 | 기전 연구 | J Applied Microbiology | Clotrimazole VVC 치료 후 질 세균총·지질 대사 변화 분석 — 미생물군 회복 기전 규명 |
| [1877264](https://pubmed.ncbi.nlm.nih.gov/1877264/) | 1991 | 임상 연구 | DICP: Annals of Pharmacotherapy | Fluconazole 3일 vs Clotrimazole 질정 급성 Candida 질염 비교 (n=185) — 경구 vs 국소 요법 근거 |
| [31106557](https://pubmed.ncbi.nlm.nih.gov/31106557/) | 2019 | Review | Minerva Ginecologica | 전신(Fluconazole)+국소(Clotrimazole) 병용 재발성 VVC 치료 리뷰 — 장기 재발 예방 접근법 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
외음질 칸디다증에 대한 Clotrimazole의 효능은 다수의 완료된 Phase 3 RCT 및 대규모 관찰 연구로 뒷받침되며(L1), 전 세계 임상 가이드라인에서 1차 치료제 지위를 보유합니다. 한국 미상장 상태는 신규 허가 기회를 의미하며, 방대한 글로벌 안전성 데이터가 규제 신청의 강력한 기반이 됩니다.

**진행하려면 필요한 것:**
- 작용 기전(MOA) 공식 데이터 확보 (DrugBank DB00257 API 조회)
- 한국 식약처(MFDS) 외음질 칸디다증 적응증 허가 전략 수립 및 브리징 스터디 필요 여부 검토
- 글로벌 안전성 데이터 패키지 정리 (CTD Module 4/5)
- 경고·금기 사항 확인 — 현재 데이터 갭(DG001), MFDS 심사 전 보완 필수
- **보류 적응증 요약**:
  - 여드름(acne, rank 1, L4): 독립적 임상 근거 부재 및 기전 연관성 미약 → 진행 보류
  - 폐경 후 위축성 질염(rank 3, L4): 핵심 병리가 에스트로겐 결핍으로 Clotrimazole 기전과 불일치 → 진행 보류
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

