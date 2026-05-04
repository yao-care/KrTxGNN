---
layout: default
title: Bimatoprost
parent: 僅模型預測 (L5)
nav_order: 141
evidence_level: L5
indication_count: 10
---

# Bimatoprost
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

# Bimatoprost: 녹내장/속눈썹 성장에서 탈모증으로

## 한 문장 요약

Bimatoprost는 합성 프로스타마이드 F2α 유사체로, 원래 녹내장(안압 강하) 치료 및 속눈썹 성장 촉진(Latisse®)에 사용됩니다.
TxGNN 모델은 **탈모증(Alopecia)**에 효과가 있을 것으로 예측하며,
현재 **10건의 임상시험**과 **20편의 문헌**이 이 방향을 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 녹내장/안압 상승, 속눈썹 성장 촉진 (Latisse®) |
| 예측 신규 적응증 | 탈모증 (Alopecia) |
| TxGNN 예측 점수 | 99.99% |
| 근거 수준 | L2 |
| 한국 시판 현황 | ✗ 미판매 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터가 부재하나, 문헌 및 임상 데이터에 기반한 맥락적 근거가 존재합니다. Bimatoprost는 합성 프로스타마이드 F2α 유사체로, 본래 녹내장 치료제로 승인되었습니다. 투여 중 관찰된 부작용인 속눈썹·눈 주변 모발의 이상 성장이 재창출의 핵심 단서가 되었으며, FDA는 이를 근거로 속눈썹 성장 촉진(eyelash hypotrichosis) 적응증으로 Latisse® 0.03%를 추가 승인하였습니다.

Bimatoprost는 모낭의 FP 수용체(프로스타글란딘 F2α 수용체) 및 EP3 수용체를 활성화하여 모낭 성장기(anagen phase)를 연장하고 모유두 세포의 증식을 촉진하는 것으로 알려져 있습니다. 두피 모낭은 속눈썹 모낭과 유사한 수용체 발현 패턴을 가지고 있어, 이미 검증된 속눈썹 성장 기전이 두피 탈모에도 적용 가능하다는 생물학적 연속성이 성립합니다.

남성형 탈모(AGA)와 여성형 탈모(FPHL)는 모두 모낭의 점진적 위축을 특징으로 하며, bimatoprost의 anagen 연장 효과가 이를 부분적으로 역전시킬 수 있다는 가설은 복수의 대규모 Phase 2 임상시험을 통해 탐색되었습니다. 특히 NCT01325337(남성 AGA, n=307)과 NCT01325350(여성 FPHL, n=306)은 현재까지 bimatoprost 탈모 분야에서 진행된 가장 규모 있는 임상시험으로, 임상적 실행 가능성을 직접적으로 뒷받침합니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01325337](https://clinicaltrials.gov/study/NCT01325337) | Phase 2 | 완료 | 307 | 남성 AGA에서 bimatoprost 3가지 용량 vs 차량(위약) 및 minoxidil 5% 비교 (이중맹검 RCT, 핵심 근거) |
| [NCT01325350](https://clinicaltrials.gov/study/NCT01325350) | Phase 2 | 완료 | 306 | 여성 FPHL에서 bimatoprost 3가지 용량 vs 차량 및 minoxidil 2% 비교 (이중맹검 RCT) |
| [NCT01904721](https://clinicaltrials.gov/study/NCT01904721) | Phase 2 | 완료 | 244 | 남성 AGA 안전성·유효성 다기관 확인 연구 (NCT01325337 교차 검증) |
| [NCT02170662](https://clinicaltrials.gov/study/NCT02170662) | Phase 2 | 완료 | 33 | 안드로겐 의존성 모낭에 대한 bimatoprost 효과 기전 탐색 (전립선 경로 직접 증거) |
| [NCT05600673](https://clinicaltrials.gov/study/NCT05600673) | Phase 1/2 | 완료 | 30 | 반흔성 탈모(AA)에서 CO2 분획 레이저 + bimatoprost 0.03% 병용 치료 효과 평가 |
| [NCT01023841](https://clinicaltrials.gov/study/NCT01023841) | Phase 4 | 완료 | 71 | 소아 속눈썹 탈락/저성장에서 bimatoprost 0.03% 안전성·유효성 (승인 후 감시 연구) |
| [NCT02848300](https://clinicaltrials.gov/study/NCT02848300) | Phase 1 | 완료 | 11 | AGA 두피 국소 PK 및 내약성 평가 (14일 1일 1회 투여, 전신 노출 낮음 확인) |
| [NCT01189279](https://clinicaltrials.gov/study/NCT01189279) | Phase 1 | 완료 | 42 | 탈모 환자 대상 신규 bimatoprost 제형 안전성 및 PK (제형 최적화 연구) |
| [NCT00187577](https://clinicaltrials.gov/study/NCT00187577) | 탐색 | 완료 | 14 | AA로 인한 속눈썹 소실에서 latanoprost vs bimatoprost 점안액 비교 (동류 약물 기준점 제공) |
| [NCT02676310](https://clinicaltrials.gov/study/NCT02676310) | Phase 1 | ⚠️ 조기 종료 | 53 | 남성 AGA 용량 점증 안전성·PK 연구 (종료 사유 불명 — 피부 자극/전신 노출 과다 등 안전성 이슈 여부 반드시 확인 필요) |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [40252129](https://pubmed.ncbi.nlm.nih.gov/40252129/) | 2025 | RCT/전향적 | Arch Dermatol Res | AA에서 CO2 레이저 + bimatoprost 병용 모발 재성장 촉진 효과 확인 |
| [37089845](https://pubmed.ncbi.nlm.nih.gov/37089845/) | 2023 | 전향적 비무작위 비교 연구 | Indian Dermatol Online J | 두피 AA에서 bimatoprost vs clobetasol propionate 직접 비교, bimatoprost 우위 결과 |
| [35278027](https://pubmed.ncbi.nlm.nih.gov/35278027/) | 2022 | 전향적 연구 | Dermatol Ther | 전두탈모(AT)·범발탈모(AU) 속눈썹 소실에서 bimatoprost 0.3mg/mL의 안전성·유효성 확인 |
| [32250713](https://pubmed.ncbi.nlm.nih.gov/32250713/) | 2022 | 체계적 문헌고찰 + 네트워크 메타분석 | J Dermatol Treat | 남녀 AGA 비수술 치료 효능 비교 분석 (bimatoprost 포함 옵션으로 평가됨) |
| [28264599](https://pubmed.ncbi.nlm.nih.gov/28264599/) | 2017 | 서술적 문헌고찰 | Expert Opin Investig Drugs | Bimatoprost의 속눈썹·눈썹·두피 탈모 치료 적용 전반 검토 (재창출 근거 최초 종합 요약) |
| [35040730](https://pubmed.ncbi.nlm.nih.gov/35040730/) | 2022 | 제형 연구 | Drug Delivery | 피부 투과성 향상 bimatoprost 국소 제형 개발 (피부 흡수량 4.6배↑, AGA 동물 모델 효과 검증) |
| [29863806](https://pubmed.ncbi.nlm.nih.gov/29863806/) | 2018 | 임상 진료 지침 | J Dermatol | 남성형·여성형 탈모 진단·치료 가이드라인 2017 일본판 (bimatoprost 신규 치료 후보로 언급) |
| [23104985](https://pubmed.ncbi.nlm.nih.gov/23104985/) | 2013 | 기전 해설/문헌고찰 | FASEB J | Bimatoprost 두피 탈모 적용 가능성에 대한 최초 기전 탐구 논문 (prostamide 경로 분석) |
| [37185388](https://pubmed.ncbi.nlm.nih.gov/37185388/) | 2023 | 문헌고찰 | Curr Oncol | 항암제 유발 탈모(CIA) 예방·치료 현황 검토 (bimatoprost CIA 적용 가능성 언급) |
| [29854658](https://pubmed.ncbi.nlm.nih.gov/29854658/) | 2018 | 문헌고찰 | Indian Dermatol Online J | 피부과 영역에서의 bimatoprost 적용 전반 개요 (탈모·색소침착 관련 신규 적응증 정리) |

---

## 한국 시판 정보

현재 한국 식약처(MFDS)에 Bimatoprost 성분의 허가 의약품이 없습니다. 탈모 적응증 개발 시 신규 허가 신청이 필요하며, FDA(Lumigan®, Latisse®) 및 EMA 기존 허가 데이터를 활용한 규제 전략 수립이 요구됩니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

> **⚠️ 핵심 위험 신호**: NCT02676310 (Phase 1, 남성 AGA 용량 점증 연구, n=53)이 조기 종료되었습니다. 종료 사유가 피부 자극·전신 흡수 과다 등 안전성 사유인지, 또는 행정적 원인인지 확인이 필요합니다. 이는 진행 여부 결정 전 반드시 검토해야 할 선결 사항입니다.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
남성 AGA(n=307, n=244)·여성 FPHL(n=306) 대상 복수의 Phase 2 RCT가 완료되어 임상적 실행 가능성이 확인되었으며, FDA 승인 속눈썹 성장 기전과의 생물학적 연속성이 뚜렷합니다. 단, Phase 3 데이터가 부재하고 한국 미판매 약물임을 감안하여 단계적 접근이 필요합니다.

**진행하려면 필요한 것:**
- NCT02676310 조기 종료 사유 확인 (안전성 이슈 여부 검증 — 차단적 위험 요소일 수 있음)
- MOA 상세 데이터 보충 (DrugBank API 조회)
- 한국 허가사항 경고·금기 정보 확보 (FDA/EMA Latisse® 및 Lumigan® 허가사항 기반)
- 한국 MFDS 신규 허가 규제 경로 분석 (국내 임상시험 요건 포함)
- Phase 3 임상시험 설계 및 목표 적응증(AGA 또는 FPHL) 우선순위 결정
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

