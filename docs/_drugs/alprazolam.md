---
layout: default
title: Alprazolam
parent: 僅模型預測 (L5)
nav_order: 45
evidence_level: L5
indication_count: 3
---

# Alprazolam
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

# Alprazolam: 불안·공황장애에서 불면증으로

## 한 문장 요약

Alprazolam은 벤조다이아제핀 계열의 향정신성 의약품으로, 불안장애 및 공황장애 치료제로 전 세계에서 폭넓게 사용되어 왔습니다.
TxGNN 모델은 **불면증(Insomnia)**에 효과가 있을 수 있다고 예측하며, 예측 점수는 **99.81%**를 기록하였습니다.
현재 **7건의 임상시험**과 **18편의 문헌**이 이 방향을 지지하나, 근거 수준은 L3(관찰 연구·임상 기록 수준)에 해당합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 불안장애, 공황장애 (한국 미등재) |
| 예측 신규 적응증 | 불면증 (Insomnia) |
| TxGNN 예측 점수 | 99.81% |
| 근거 수준 | L3 (관찰 연구 또는 체계적 문헌고찰) |
| 한국 시판 현황 | 미등재 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

현재 Evidence Pack에 Alprazolam의 상세 작용기전(MOA) 데이터는 포함되어 있지 않습니다. 알려진 정보에 따르면 Alprazolam은 벤조다이아제핀(BZD) 계열 약물로서 **GABA-A 수용체의 양성 알로스테릭 조절제(positive allosteric modulator)**로 작용합니다. 구체적으로 GABA-A 수용체의 염소 이온(Cl⁻) 채널 개방 빈도를 증가시켜 중추신경계 억제 효과를 나타내며, 이를 통해 수면 잠복기 단축 및 비-REM(NREM) 수면 연장 효과를 발휘합니다.

불안장애와 불면증은 높은 공존이환율(comorbidity)을 보이는 질환군입니다. 불안으로 인한 수면 개시 곤란 증상에 Alprazolam의 GABAergic 억제 기전이 효과적으로 작용할 수 있으며, 이는 기전상 타당한 연결입니다. 실제로 혈액투석(ESRD) 환자의 수면장애를 대상으로 Alprazolam과 멜라토닌을 직접 비교한 임상 연구(PMID 33403184)가 수행되었고, 관상동맥 질환 동반 불면증 환자에서 Alprazolam을 대조군으로 설정한 통합치료 연구(PMID 39183410)도 존재합니다.

다만, BZD 계열은 만성 사용 시 서파 수면(Slow-wave sleep)과 REM 수면을 억제하고 내성(tolerance) 및 신체 의존성(physical dependence) 형성 위험이 높습니다. 이로 인해 현행 국제 수면 지침(AASM 등)에서는 BZD를 불면증 **1차 치료로 권장하지 않으며**, 단기·한시적 용도에 한해 조건부 사용을 허용하는 입장입니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01584440](https://clinicaltrials.gov/study/NCT01584440) | Phase 2 | 완료 | 220 | AVP-923(덱스트로메토르판/퀴니딘)의 알츠하이머 환자 초조(agitation) 증상에 대한 이중맹검·안위약 대조 RCT. 수면 연계 행동 평가 포함 |
| [NCT02648776](https://clinicaltrials.gov/study/NCT02648776) | N/A | 불명 | 1,400 | 대만 3차 의료기관 노인 수면장애 환자에서 안면제(hypnotics) 처방 패턴 및 위험-효익 평가 전향적 코호트. BZD 계열 포함 다종 수면제 비교 |
| [NCT00266409](https://clinicaltrials.gov/study/NCT00266409) | Phase 4 | 완료 | 418 | GAD·공황장애 환자에서 Niravam™(alprazolam ODT)+SSRI/SNRI 병용 vs SSRI/SNRI 단독 치료 반응 시간 비교. 212개 기관 다기관 공개 RCT |
| [NCT04572750](https://clinicaltrials.gov/study/NCT04572750) | N/A | 완료 | 170 | 전자 자기관리 패킷을 통한 BZD(Xanax 등) 감량·중단 촉진 연구. 불안·수면 문제로 처방된 BZD 중단 개입 효과 평가 |
| [NCT03327506](https://clinicaltrials.gov/study/NCT03327506) | Phase 4 | 불명 | 128 | 부인과 복강경 수술 전야 불안 관리: 최면 요법 vs Alprazolam 전투약 직접 비교. STAI-Y 척도로 수면 전 불안 상태 평가 |
| [NCT01146600](https://clinicaltrials.gov/study/NCT01146600) | Phase 2 | 완료 | 26 | Clarithromycin의 특발성 과다수면증(Hypersomnia) 치료 효능 평가. Alprazolam은 비주요 개입으로 포함 |
| [NCT01893632](https://clinicaltrials.gov/study/NCT01893632) | Phase 2 | 조기 종료 | 2 | Gabapentin의 벤조다이아제핀 의존성 치료 효능 평가. 조기 종료(n=2)로 결론 도출 불가 |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [33403184](https://pubmed.ncbi.nlm.nih.gov/33403184/) | 2020 | Comparative RCT | Cureus | 혈액투석(ESRD) 환자 수면장애에서 **Alprazolam vs 멜라토닌 직접 비교 RCT**. 수면 질·주간 졸림 개선 효과 및 안전성 평가 |
| [39183410](https://pubmed.ncbi.nlm.nih.gov/39183410/) | 2024 | RCT (통합의학) | Medicine | 관상동맥 질환 동반 불면증 환자(n=116)에서 독맥구 뜸·이침+Alprazolam 통합치료의 심장기능 및 신경전달물질(세로토닌·도파민) 영향 평가 |
| [37801512](https://pubmed.ncbi.nlm.nih.gov/37801512/) | 2023 | 전임상 연구 | Aging | 마우스 반복 Alprazolam 투여 시 미토콘드리아 기능 저하 및 해마 의존 기억 강화 장애 기전 분석 (프로테오믹스, 439개 단백질) |
| [36692463](https://pubmed.ncbi.nlm.nih.gov/36692463/) | 2023 | 메타분석 | Acta Pharmaceutica | 노인 만성 비감염성 질환 환자에서 안정제(tranquilizers) 유형별 효능·부작용 체계적 메타분석. BZD 계열 용량·안전성 근거 포함 |
| [35041261](https://pubmed.ncbi.nlm.nih.gov/35041261/) | 2022 | RCT | Brain and Behavior | 알츠하이머 동반 수면장애 노인 환자에서 에스조피클론의 수면 질·인지기능 개선 효과 무작위 대조시험 |
| [37984023](https://pubmed.ncbi.nlm.nih.gov/37984023/) | 2024 | 역학·예측 모델 | Value in Health Regional Issues | 크로아티아 10년간 BZD 사용 추세 및 경제적 부담. 불안·불면·기분장애별 처방 패턴과 장기 위험(알츠하이머, 낙상, 의존) 분석 |
| [38363887](https://pubmed.ncbi.nlm.nih.gov/38363887/) | 2024 | 횡단면 연구 | Medicine | COVID-19 생존자의 불면증 실태 조사. ISI 척도로 불면증 중증도 및 영향 요인(나이·기저질환·심리적 스트레스) 분석 |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | 리뷰 | Expert Opin Drug Metab Toxicol | 항불안제(BZD 포함) 약물동태 종합 리뷰. Alprazolam의 흡수·분포·대사(CYP3A4)·반감기 특성 정리 |
| [35493764](https://pubmed.ncbi.nlm.nih.gov/35493764/) | 2022 | 코호트 연구 | JHEP Reports | 간경변 환자에서 졸피뎀 감량 시 낙상·골절 위험 감소 효과 확인. BZD 계열 수면제 안전성 관리 시사점 제공 |
| [25532388](https://pubmed.ncbi.nlm.nih.gov/25532388/) | 2014 | 실세계 분석 | China J Chinese Materia Medica | 불면증 환자 1,067건의 공존 질환(고혈압 26.9%, 뇌경색 19.5% 등) 및 서양·한방 약물 병용 처방 패턴 실세계 분석 |

---

## 한국 시판 정보

현재 한국에 등재된 Alprazolam 허가품목이 없습니다 (시판 현황: **미등재**, 허가건수: **0건**).

Alprazolam(Xanax®)은 미국 FDA 및 유럽 EMA에서 불안장애·공황장애 치료제로 허가되어 있으나, 이번 Evidence Pack 기준 한국 식품의약품안전처(MFDS) 등재 데이터는 확인되지 않습니다. 한국 내 도입 검토 시 MFDS 신규 허가 절차가 필요합니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
Alprazolam의 GABA-A 수용체 억제 기전은 불면증 증상(수면 잠복기 단축)에 기전적으로 타당하며, 혈액투석 환자 대상 직접 비교 연구(PMID 33403184) 등 일부 임상 근거가 존재합니다. 그러나 현 근거 수준은 L3에 그치고, BZD 계열 특유의 내성·의존성 및 장기 수면구조 교란 위험이 있어 반드시 명확한 사용 가이드라인을 갖춘 상태에서 검토해야 합니다.

**진행하려면 필요한 것:**
- Alprazolam 상세 작용기전(MOA) 데이터 확보 (DrugBank DB00404 API 조회)
- 한국 MFDS 허가사항(경고·금기·약물상호작용) 확인 (Data Gap DG001·DG002 해소)
- 불면증 특화 무작위 대조시험(RCT) 데이터 추가 검색 (단기 vs 장기 처방 비교 포함)
- 내성·의존·남용 가능성 대비 위험 관리 계획(Risk Management Plan) 수립
- 현행 수면장애 치료 지침(AASM, 대한수면학회) 대비 Alprazolam의 역할 위치 검토

---

> **참고 — 추가 예측 적응증**: Evidence Pack 내 3순위 예측 적응증인 **광장공포증(Agoraphobia)**은 TxGNN 예측 점수 99.56%이며, Phase 3 다기관 RCT(n=526, PMID 3282478), Cochrane 네트워크 메타분석(PMID 38014714) 등 **L1 수준의 강력한 근거**를 보유합니다. 결정 단계 S3(Proceed with Guardrails)로, 불면증(L3/S2)보다 근거 기반이 현저히 강합니다. 추후 별도 보고서 작성을 권장합니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

