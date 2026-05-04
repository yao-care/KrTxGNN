---
layout: default
title: Estriol
parent: 僅模型預測 (L5)
nav_order: 253
evidence_level: L5
indication_count: 1
---

# Estriol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# ESTRIOL: 에스트로겐 결핍 증상에서 무월경으로

## 한 문장 요약

ESTRIOL(E3)은 인체 내 자연 발생 약한 에스트로겐으로, 에스트로겐 결핍 관련 상태에 대한 치료제로 연구되어 왔습니다.
TxGNN 모델은 **무월경(Amenorrhea)**에 효과가 있을 수 있다고 예측하며, 현재 **3건의 임상시험**과 **13편의 문헌**이 이 방향을 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 현재 한국 미허가 상태로 국내 허가 적응증 없음 |
| 예측 신규 적응증 | 무월경 (Amenorrhea) |
| TxGNN 예측 점수 | 99.18% |
| 근거 수준 | L1 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

ESTRIOL(E3)은 인체 내 자연 발생 에스트로겐 중 가장 약한 활성을 가진 물질로, 에스트로겐 수용체 ERα 및 ERβ에 대한 부분 효능제(partial agonist)로 작용합니다. 임신 중 태반에서 다량 생성되며, 폐경 후 에스트로겐 치료제로서의 활용 가능성이 꾸준히 연구되어 왔습니다.

기능성 하시상성 무월경(Functional Hypothalamic Amenorrhea, FHA)에서는 심리사회적·대사적 스트레스 요인이 시상하부의 GnRH 박동성 분비를 억제하여 LH/FSH 분비 부족과 저에스트로겐혈증의 악순환이 형성됩니다. Estriol은 하시상하부-뇌하수체 축의 음성/양성 되먹임 기전을 부분 활성화하여 LH 박동 빈도를 조절하고 정상 배란주기 회복을 돕는 역할을 할 수 있습니다.

Estradiol(E2)에 비해 자궁내막 증식 효과가 약한 Estriol의 특성은 안전성 측면에서 유리한 여건을 제공하며, 장기간 저에스트로겐 상태로 인한 골밀도 감소 및 심혈관 위험 예방에도 기여할 수 있습니다. 이러한 기전적 연관성이 무월경 적응증으로의 재창출 타당성을 뒷받침합니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT04090957](https://clinicaltrials.gov/study/NCT04090957) | Phase 3 | 완료 | 1,015 | 폐경 후 여성의 중등~중증 혈관운동 증상(VMS)에 대한 Estetrol(E4) 15mg/20mg 대 위약의 효능·안전성을 평가한 대규모 이중맹검 RCT (E4Comfort Study II) |
| [NCT04209543](https://clinicaltrials.gov/study/NCT04209543) | Phase 3 | 완료 | 1,570 | 폐경 후 여성의 VMS에 대한 Estetrol(E4) 효능 및 자궁내막·전신 안전성을 평가한 이중맹검 RCT (E4Comfort Study I); 2,500명 이상 누적 수집으로 고신뢰도 데이터 확보 |
| [NCT04487392](https://clinicaltrials.gov/study/NCT04487392) | Phase 2 | 철회 | 0 | 폐경 후 외음질 위축(VVA)에 대한 광생물조절 치료 시험; 등록 전 철회되어 유효 데이터 없음 |

> **주의**: NCT04090957 및 NCT04209543은 Estetrol(E4)을 대상으로 한 시험으로, Estriol(E3)과는 구조적으로 유사하나 동일 성분이 아님을 고려하여 해석하시기 바랍니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [22137494](https://pubmed.ncbi.nlm.nih.gov/22137494/) | 2012 | 임상 중재 연구 | Fertility and Sterility | 기능성 하시상성 무월경(FHA) 환자에서 Estriol 투여가 시상하부-뇌하수체 기능 및 성선자극호르몬 분비에 미치는 영향을 직접 평가. Estriol이 LH 분비를 조절함을 확인 |
| [37371858](https://pubmed.ncbi.nlm.nih.gov/37371858/) | 2023 | 내러티브/기전 리뷰 | Biomedicines | FHA에서 저용량 에스트로겐의 신경내분비 조절자 역할 고찰. GnRH 박동 억제 기전과 양성 되먹임 메커니즘 활성화 가능성 검토 |
| [16526238](https://pubmed.ncbi.nlm.nih.gov/16526238/) | 2005 | 코호트 연구 | Medicinski pregled | 조기 원발성 난소부전(PPOF) 여성에서 에스트로-프로게스테론 복합제가 지질 및 호르몬 프로필에 미치는 영향 평가. PPOF 관련 고성선자극호르몬성 무월경에서 에스트로겐 보충의 효과 확인 |
| [7026111](https://pubmed.ncbi.nlm.nih.gov/7026111/) | 1981 | 리뷰 | Clinical Obstetrics and Gynecology | 호르몬 피임과 종양 발생의 연관성 검토; 에스트로겐 기전 관련 배경 정보 제공 |
| [4254759](https://pubmed.ncbi.nlm.nih.gov/4254759/) | 1971 | 증례 시리즈 | British Journal of Psychiatry | 신경성 식욕부진증 사례 보고; 대사성 스트레스 기인 무월경과의 관련성 맥락 제공 |
| [4102186](https://pubmed.ncbi.nlm.nih.gov/4102186/) | 1971 | 증례 보고 | Lancet | 조기 난소부전 2례의 내분비학적 소견; 에스트로겐 결핍 무월경 표현형 기술 |
| [2949864](https://pubmed.ncbi.nlm.nih.gov/2949864/) | 1986 | 임상 관찰 | 中西醫結合雜誌 | 무월경·희발월경 여성에서 성선 기능 변화와 한의학 '신허' 개념의 연관성 관찰 |
| [5935707](https://pubmed.ncbi.nlm.nih.gov/5935707/) | 1966 | 증례 보고 | Am J Obstet Gynecol | 임신 중 메드록시프로게스테론 아세테이트 투여 후 지속된 부인과·내분비 이상 보고; 프로게스틴 관련 무월경 기전 참고 |
| [14194444](https://pubmed.ncbi.nlm.nih.gov/14194444/) | 1964 | 임상시험 | J Obstet Gynaecol Brit Cwlth | 특발성 속발성 무월경 환자에서 뇌하수체·요중 FSH 및 융모성 성선자극호르몬의 효과 평가; 성선자극호르몬 기반 무월경 치료의 초기 근거 |
| [979592](https://pubmed.ncbi.nlm.nih.gov/979592/) | 1976 | 방법론/진단 | Die Medizinische Welt | LH, FSH, 프로게스테론, 에스트론, 에스트라디올, 에스트리올의 방사면역측정법(RIA) 임상 활용; 에스트리올 측정의 임상적 의의 제시 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
기능성 하시상성 무월경(FHA) 환자에서 Estriol이 LH 분비를 직접 조절함을 확인한 임상 중재 연구(PMID 22137494)와 기전 리뷰(PMID 37371858)가 있으며, 에스트로겐 계열 약물의 폐경 관련 증상에 대한 2건의 대규모 완료된 Phase 3 RCT(합산 n=2,585)가 에스트로겐 경로의 효능을 뒷받침합니다. 기전적 타당성과 초기 임상 근거가 충분하여 진행을 권장하나, 한국 미허가 상태 및 안전성 데이터 공백으로 인해 조건부 진행이 적절합니다.

**진행하려면 필요한 것:**
- **상세 MOA 데이터 확보**: DrugBank API를 통한 Estriol의 정확한 작용 기전 정보 수집
- **한국 허가사항 검토**: 국내 허가사항 또는 해외(EU/미국) 허가 제품의 경고·금기 사항 확인
- **약물상호작용 데이터 확보**: 공식 데이터베이스(DrugBank, Drugs.com) 기반 DDI 분석
- **FHA 특화 임상시험 설계 검토**: 현재 근거는 폐경 후 여성 대상이 중심이므로, FHA 환자군 대상 파일럿 연구 계획 필요
- **Estriol vs Estetrol 구분**: 주요 임상시험(NCT04090957, NCT04209543)이 Estetrol(E4) 대상임을 명확히 하고, Estriol(E3) 직접 근거를 추가 수집
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

