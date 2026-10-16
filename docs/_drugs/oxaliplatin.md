---
layout: default
title: Oxaliplatin
parent: 모델 예측만 (L5)
nav_order: 567
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-15
description: "Oxaliplatin: 예측 신규 적응증 악성 흉막 중피종 (Malignant Pleural Mesothelioma) (근거 수준 L5). 기존 적응증: 허가 적응증 원문은 이번 데이터에 텍스트로 포함되지 않았습니다(허가증 링크만 확인됨)"
monitor_inn: "OXALIPLATIN"
predicted_indications: ["malignant pleural mesothelioma", "malignant epithelioid mesothelioma", "sarcomatoid mesothelioma", "malignant visceral pleura tumor"]
---

# Oxaliplatin
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **4** 건
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

# Oxaliplatin: 대장암에서 악성 흉막 중피종으로

## 한 문장 요약

Oxaliplatin은 백금 계열 항암제로, 한국에서 주로 대장암 등 소화기 암 치료에 사용되어 왔습니다. TxGNN 모델은 **악성 흉막 중피종(Malignant Pleural Mesothelioma)**에 효과가 있을 수 있다고 예측하며, 현재 **3건의 임상시험**(직접 관련 2건)과 **19편의 문헌**이 이 방향을 일부 지지합니다. 다만 대부분 소규모 단일군 2상 연구입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 원문은 이번 데이터에 텍스트로 포함되지 않았습니다(허가증 링크만 확인됨) |
| 예측 신규 적응증 | 악성 흉막 중피종 (Malignant Pleural Mesothelioma) |
| TxGNN 예측 점수 | 99.68% |
| 근거 수준 | L2 (완료된 Phase 2 시험이 있으나 단일군·소규모이며 무작위 대조시험은 아님) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 20건 |
| 권장 결정 | Hold (추가 연구 질문 단계) |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터는 수집되지 않았습니다. 알려진 정보에 따르면 Oxaliplatin은 DACH 리간드를 가진 3세대 백금 제제로, DNA에 가교(intrastrand adduct)를 형성하여 DNA 합성과 복구를 억제하고 빠르게 분열하는 종양세포의 세포사멸을 유도합니다.

백금 제제(시스플라틴, 카르보플라틴)는 중피종 치료의 기본 축입니다. 따라서 같은 계열인 Oxaliplatin도 기전상 적용 가능성이 있습니다. 또한 DACH 리간드 부가물은 불일치 복구(mismatch repair) 체계에 덜 인식되어, 일부 시스플라틴 내성 상황에서 활성을 유지할 가능성이 있습니다.

그러나 gemcitabine, raltitrexed, vinorelbine과의 병용 Phase 2 연구들에서 보고된 활성은 보통 수준이며, 표준 요법인 백금-페메트렉시드 대비 우월성을 보인 Phase 3 RCT는 없습니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00859469](https://clinicaltrials.gov/study/NCT00859469) | Phase 2 | 완료 | 29 | 흉막/복막 중피종 1·2차 치료에서 Oxaliplatin + Gemcitabine의 반응률 평가. 비무작위 소규모 시험 |
| [NCT00996385](https://clinicaltrials.gov/study/NCT00996385) | Phase 2 | 불명 | 29 | 기치료 흉막/복막 중피종에서 Bortezomib + Oxaliplatin 단일군 시험. 결과 신뢰도 제한적 |
| [NCT07532902](https://clinicaltrials.gov/study/NCT07532902) | Phase 1 | 모집 중 | 60 | MTAP 결손 고형암 바스켓 시험. Oxaliplatin은 배경 요법이며 간접 근거 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [14609447](https://pubmed.ncbi.nlm.nih.gov/14609447/) | 2003 | Phase II | Clin Lung Cancer | 악성 흉막 중피종 25명에서 Gemcitabine + Oxaliplatin 활성 평가 |
| [12525529](https://pubmed.ncbi.nlm.nih.gov/12525529/) | 2003 | Phase II | J Clin Oncol | Raltitrexed + Oxaliplatin 병용이 악성 중피종에서 활성 있는 요법으로 보고 |
| [15639727](https://pubmed.ncbi.nlm.nih.gov/15639727/) | 2005 | Phase II | Lung Cancer | 미치료 중피종 1차 치료로 Vinorelbine + Oxaliplatin 평가 |
| [11989592](https://pubmed.ncbi.nlm.nih.gov/11989592/) | 2001 | Phase II (파일럿) | Tumori | 수술 불가 흉막 중피종에서 Oxaliplatin + Raltitrexed 파일럿 결과 |
| [19091133](https://pubmed.ncbi.nlm.nih.gov/19091133/) | 2008 | 관찰 연구 | J Occup Med Toxicol | 페메트렉시드 치료 후 환자에서 Oxaliplatin ± Gemcitabine의 효능·안전성 |
| [15893013](https://pubmed.ncbi.nlm.nih.gov/15893013/) | 2005 | Phase II | Lung Cancer | 2차 치료로 Raltitrexed + Oxaliplatin은 객관적 반응이 없어 비활성으로 판단 |
| [15261443](https://pubmed.ncbi.nlm.nih.gov/15261443/) | 2004 | Review | Lung Cancer | 중피종 화학요법의 과거 결과와 최신 동향 정리 |
| [12610498](https://pubmed.ncbi.nlm.nih.gov/12610498/) | 2003 | Review | Br J Cancer | 중피종 화학요법의 Phase II-III 결과 종합 |
| [12601280](https://pubmed.ncbi.nlm.nih.gov/12601280/) | 2003 | Review | Curr Opin Oncol | 페메트렉시드-백금 병용 등 최신 화학요법 개관 |
| [25028262](https://pubmed.ncbi.nlm.nih.gov/25028262/) | 2015 | 전임상 | Hum Exp Toxicol | 중피종 세포주에서 EF24·RAD001이 백금 제제 효과를 증강 |

문헌 결과는 엇갈립니다. 1차 치료 병용 요법에서는 활성이 보고되었으나, 2차 치료에서는 반응이 없었던 연구도 있습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200600006 | 오엑스피주100밀리그램 | 동결건조분말 바이알 | 허가증 원문 링크만 확인되며 적응증 텍스트는 별도 확인 필요 |
| 200500036 | 오엑스피주 | 동결건조분말 바이알 | 위와 동일 |
| 200603902 | 엘록사틴주5밀리그램/밀리리터 | 액상 바이알 | 위와 동일 |
| 200712404 | 옥사플린주100밀리그램 | 동결건조분말 바이알 | 위와 동일 |
| 200604181 | 벨록사주100밀리그램 | 동결건조분말 바이알 | 위와 동일 |

전체 20건이 모두 단일성분 유효 허가이며, 이 중 일부는 수출용입니다.

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 약물 (백금 계열) |
| 골수억제 위험 | 중등도 (일반적으로 알려진 수준이며, 허가사항의 경고 및 주의사항을 참조하세요) |
| 구토 유발성 등급 | 중등도 |
| 모니터링 항목 | CBC(분류 포함), 간·신기능, 전해질, 말초신경병증 평가 |
| 취급 방호 | 세포독성 약물 취급 규정 준수 필요 |

## 안전성 고려사항

- **관련 질환(지식그래프 기반 금기 정보, 허가 문구 아님)**: 신장 질환, 간 질환, 담낭 질환, 말초신경계 질환·말초신경병증, 간질성 폐질환, 폐섬유화 등
- **약물 상호작용**: 총 100건이 확인되었으며, 이 중 **중대(Major)** 수준은 Dolasetron입니다. 중등도(Moderate) 상호작용으로는 Famotidine, Amphotericin B, Loperamide, Mesalazine, Metronidazole, Clarithromycin, Vancomycin, Kanamycin, Levofloxacin, Palonosetron 등이 있습니다.

허가사항 기반의 경고·금기 정보는 이번 데이터에서 확보되지 않았으므로 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
백금 계열의 기전적 타당성과 복수의 Phase 2 연구가 있으나, 모두 소규모 단일군 연구이고 결과가 엇갈리며 표준 요법 대비 우월성을 보인 Phase 3 RCT가 없습니다. 현 단계에서는 임상 적용보다 추가 연구 질문으로 다루는 것이 적절합니다.

**진행하려면 필요한 것:**
- 허가사항 원문(경고, 금기, 적응증) 확보 및 분석
- DrugBank 등에서 작용 기전(MOA) 데이터 보완
- 표준 백금-페메트렉시드 요법과 비교하는 무작위 시험 설계 검토
- 면역항암제 병용 등 최신 표준 치료 맥락에서의 위치 평가
- 신기능·간기능·말초신경병증·간질성 폐질환 환자에 대한 안전성 모니터링 계획

**참고:** 순위 2~4위 예측 적응증(상피형 중피종, 육종형 중피종, 악성 내장 흉막 종양)은 중피종 하위 유형별 직접 근거가 부족하며, 대부분 복막 질환 관련 간접 근거에 의존합니다. 육종형 및 내장 흉막 종양은 Hold 상태입니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

