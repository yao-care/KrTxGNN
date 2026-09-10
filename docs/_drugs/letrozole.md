---
layout: default
title: Letrozole
parent: 僅模型預測 (L5)
nav_order: 436
evidence_level: L5
indication_count: 10
---

# Letrozole
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

# Letrozole: 미출시 약물에서 유방암(Female Breast Carcinoma) 적응증 확증으로

## 한 문장 요약

Letrozole은 폐경 후 여성의 호르몬수용체 양성(HR+) 유방암 치료에 사용되는 제3세대 비스테로이드성 방향화효소(아로마타제) 억제제입니다. 국내 허가 데이터베이스 기준으로는 현재 허가 품목이 전혀 없어 미출시 상태이지만, TxGNN 모델은 이미 국제적으로 확립된 적응증인 **유방암(Female Breast Carcinoma)**을 가장 높은 예측 점수(99.98%)로 제시하며, **80건 이상의 임상시험**과 **20편 이상의 문헌**(다수의 대규모 Phase 3 RCT 포함)이 이를 강력히 뒷받침합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (국내 허가 이력 없음) — 해외에서는 폐경 후 HR+ 유방암 표준 내분비요법으로 확립되어 있음 |
| 예측 신규 적응증 | 유방암 (Female Breast Carcinoma) |
| TxGNN 예측 점수 | 99.98% |
| 근거 수준 | L1 |
| 국내 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

Letrozole은 방향화효소(aromatase)를 억제하여 안드로스텐디온/테스토스테론이 에스트론/에스트라디올로 전환되는 것을 차단합니다. 이를 통해 폐경 후 여성의 전신 에스트로겐 농도를 낮추고, 에스트로겐 신호에 의존해 증식하는 HR+ 유방암 세포의 성장을 직접적으로 억제합니다. 이는 추정 기전이 아니라 이미 확립된 이 약물의 핵심 작용기전입니다.

다만 본 Evidence Pack에서는 국내 허가 이력이 전혀 확인되지 않아(미출시, 허가증 0건) "기존 적응증"에 해당하는 규제 데이터를 제시할 수 없었습니다(DrugBank MOA 필드 자체도 데이터 공백으로 표시됨). TxGNN이 1순위로 예측한 "유방암"은 사실 letrozole이 해외에서 이미 표준치료로 확립된 적응증과 동일합니다. 즉 이번 결과는 완전히 새로운 질환으로의 재창출이라기보다, **국내 미출시 상태를 해소하고 이미 국제적으로 검증된 적응증으로 시장에 진입할 근거가 충분함을 재확인**하는 성격에 가깝습니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00073528](https://clinicaltrials.gov/study/NCT00073528) | Phase 3 | 완료 | 1,286 | ER/PgR+ 진행성·전이성 유방암에서 lapatinib+letrozole vs letrozole 단독의 효능·내약성 비교 (등급 A) |
| [NCT00330317](https://clinicaltrials.gov/study/NCT00330317) | Phase 3 | 완료 | 300 | 폐경 후 HR+ 원발 유방암에서 최적의 수술 전 letrozole 투여기간을 평가, 유방보존술 가능성 확대 (등급 A) |
| [NCT00004205](https://clinicaltrials.gov/study/NCT00004205) | Phase 3 | 완료 | 8,028 | 폐경 후 ER/PgR+ 유방암에서 letrozole vs tamoxifen 보조내분비요법을 비교한 대규모 확증 연구 |
| [NCT04546009](https://clinicaltrials.gov/study/NCT04546009) | Phase 3 | 진행중(모집종료) | 992 | ER+/HER2- 국소진행성·전이성 유방암에서 giredestrant+palbociclib vs letrozole+palbociclib 비교 |
| [NCT03820830](https://clinicaltrials.gov/study/NCT03820830) | Phase 3 | 진행중(모집종료) | 405 | HR+/HER2- 국소재발 유방암에서 palbociclib+내분비요법 보조치료 vs 내분비요법 단독 |
| [NCT00963729](https://clinicaltrials.gov/study/NCT00963729) | Phase 3 | 완료 | 756 | 폐경 후 원발 유방암에서 화학요법 vs letrozole 포함 내분비요법 신보조요법 비교 |
| [NCT03969121](https://clinicaltrials.gov/study/NCT03969121) | Phase 3 | 완료 | 141 | 수술 가능 HR+/HER2- 원발 유방암에서 palbociclib+내분비요법 vs 위약+내분비요법 신보조요법 |
| [NCT05439499](https://clinicaltrials.gov/study/NCT05439499) | Phase 3 | 상태 불명 | 434 | HR+/HER2- 진행성 유방암 1차 치료에서 FCN-437c+letrozole/anastrozole±goserelin vs 위약 비교 (등급 B) |
| [NCT04095364](https://clinicaltrials.gov/study/NCT04095364) | Phase 3 | 진행중(모집종료) | 450 | 난소·복막 저등급 장액성암(Stage II-IV)에서 paclitaxel/carboplatin+letrozole 유지요법 vs letrozole 단독 (적응증은 상이하나 letrozole 병용) |
| [NCT06223698](https://clinicaltrials.gov/study/NCT06223698) | Phase 3 | 모집 전 | 3,832 | HR+ 유방암 환자 대상 확장 보조내분비요법(tamoxifen→AI 전환 전략) 효과를 평가하는 대규모 등록기반 RCT |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [32683565](https://pubmed.ncbi.nlm.nih.gov/32683565/) | 2020 | RCT | Breast Cancer Res Treat | PALOMA-1 전체생존 결과 — palbociclib+letrozole vs letrozole 단독, ER+/HER2- 진행성 유방암 1차 치료 |
| [31838010](https://pubmed.ncbi.nlm.nih.gov/31838010/) | 2020 | RCT | Lancet Oncology | CORALLEEN — luminal B 조기유방암에서 신보조 ribociclib+letrozole vs 화학요법 비교 Phase 2 RCT |
| [16382061](https://pubmed.ncbi.nlm.nih.gov/16382061/) | 2005 | RCT | NEJM | 폐경 후 조기유방암에서 letrozole vs tamoxifen 보조내분비요법 비교(대규모 확증 연구) |
| [20095792](https://pubmed.ncbi.nlm.nih.gov/20095792/) | 2010 | Review | Expert Opin Drug Metab Toxicol | Letrozole의 약력학·약동학·임상 효능 및 안전성 총설 |
| [16500235](https://pubmed.ncbi.nlm.nih.gov/16500235/) | 2006 | Review | Breast | 진행성 유방암 및 신보조요법에서 letrozole 개발 및 활용에 대한 총설 |
| [17696797](https://pubmed.ncbi.nlm.nih.gov/17696797/) | 2007 | 미분류 | Expert Opin Pharmacother | 유방암에서 letrozole의 현재 및 향후 역할에 대한 임상적 함의 논의 |
| [19445563](https://pubmed.ncbi.nlm.nih.gov/19445563/) | 2009 | 미분류 | Expert Opin Pharmacother | 조기유방암에서 anastrozole·letrozole·exemestane 3제 비교 총설 |
| [35378469](https://pubmed.ncbi.nlm.nih.gov/35378469/) | 2022 | 미분류 | Curr Probl Cancer | HR+ 진행성 유방암에서 palbociclib+letrozole의 반응 예측인자 및 예후인자 분석 |
| [34645649](https://pubmed.ncbi.nlm.nih.gov/34645649/) | 2022 | 미분류 | Clin Cancer Res | ER+/HER2- 유방암에서 palbociclib+letrozole 반응·저항성 바이오마커 연구 |
| [36243120](https://pubmed.ncbi.nlm.nih.gov/36243120/) | 2022 | 미분류 | Life Sciences | Letrozole의 약리학, 독성 및 잠재적 치료 효과에 대한 종합 리뷰 |

## 국내 시판 정보

현재 국내에는 Letrozole의 허가 품목이 없습니다 (미출시, 허가증 0건).

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 호르몬(내분비) 계열 항종양제(방향화효소 억제제) — fluoropyrimidine/platinum/taxane 등 전형적 세포독성 화학요법에는 해당하지 않음 |
| 골수억제 위험 | 낮음 — 아로마타제 억제제 계열은 골수억제를 거의 유발하지 않으며, 관절통·골밀도 감소·안면홍조가 주된 부작용 |
| 구토 유발성 등급 | 낮음 — 경구 호르몬제제로 최소 최토성(minimal emetogenic risk) 군에 해당 |
| 모니터링 항목 | 골밀도(BMD), 지질프로파일, 간기능 — 전형적 세포독성 화학요법 대비 CBC 모니터링 필요성은 낮음 |
| 취급 방호 | 경구 비세포독성 제제로 정맥주사 세포독성 약물에 준하는 특별 취급 규정은 불필요 |

*(위 표는 방향화효소 억제제 계열의 일반적 약리 특성에 근거한 것으로, 본 Evidence Pack의 국내 허가사항 안전성 데이터(DG001, Blocking)와는 별개입니다. 실제 처방·조제 시 허가사항을 반드시 확인하세요.)*

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
유방암(HR+)에 대한 letrozole의 효능은 NCT00004205(n=8,028), NCT00073528(n=1,286) 등 대규모 완료 Phase 3 RCT와 다수의 병용요법 연구로 이미 확증 수준(L1)의 근거를 갖추고 있습니다. 다만 국내에는 아직 허가 품목이 전무하여, 이는 신규 적응증 재창출이 아니라 미출시 상태 해소를 위한 시장 진입 검토에 가깝습니다.

**진행하려면 필요한 것:**
- TFDA/MFDS 등 규제기관 공식 허가사항(경고·금기·DDI) 확보 — 현재 Blocking 등급 데이터 공백(DG001)으로 안전성 초기평가(S1) 진행 불가
- DrugBank 등 공식 소스를 통한 MOA 데이터 보완(DG002) — 현재는 임상시험 근거로부터 유추한 기전 설명에 의존
- 국내 시장 진입을 위한 정식 허가 신청 경로 및 일정 검토
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

