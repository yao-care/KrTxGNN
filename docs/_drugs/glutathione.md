---
layout: default
title: Glutathione
parent: 僅模型預測 (L5)
nav_order: 275
evidence_level: L5
indication_count: 10
---

# Glutathione
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

# Glutathione: 내인성 항산화제에서 경화성 담관염으로

## 한 문장 요약

Glutathione은 세포 내에서 자연 합성되는 삼펩타이드 항산화 물질로, 현재 한국에서 공식 승인된 치료 적응증이 없습니다.
TxGNN 모델은 **경화성 담관염(Sclerosing Cholangitis)**에 효과가 있을 수 있다고 예측하며,
현재 **20편의 문헌**이 이 방향을 지지하나 직접적인 임상시험 등록은 없습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 없음 (한국 미허가) |
| 예측 신규 적응증 | 경화성 담관염 (Sclerosing Cholangitis) |
| TxGNN 예측 점수 | 98.14% |
| 근거 수준 | L4 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면, Glutathione(GSH)은 γ-글루타밀-시스테이닐-글리신으로 구성된 내인성 삼펩타이드로, 세포 내 주요 항산화 방어 물질입니다. 활성산소종(ROS)을 직접 제거하고, glutathione S-transferase(GST)의 보조기질로서 독성 물질의 포합(conjugation) 및 해독 반응을 매개합니다.

원발성 경화성 담관염(PSC)은 담관의 진행성 염증 및 섬유화를 특징으로 하는 자가면역성 간담도 질환으로, 독성 담즙산과 활성산소에 의한 산화 손상이 핵심 병리 기전입니다. PSC 환자에서 glutathione S-transferase theta 1(GSTT1)이 자가항원으로 작용한다는 보고(PMID 18242955, 15041041)는 GST-glutathione 대사 이상이 PSC 면역 병리에 직접 관여함을 시사합니다. 담즙정체 마우스 대사체 분석에서는 glutathione 대사 경로가 현저히 변화하였고(PMID 30009888), β-catenin 결손 모델에서 glutathione이 산화 스트레스 조절의 핵심 분자임이 확인되었습니다(PMID 38967587).

다만 현재까지의 근거는 생물표지자·자가항원 수준에 머물러 있으며, glutathione을 직접 투여하는 전임상 또는 임상시험은 존재하지 않습니다. 기전적 타당성은 인정되나 치료제로서의 효능 검증이 필요한 초기 연구 단계입니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [18242955](https://pubmed.ncbi.nlm.nih.gov/18242955/) | 2008 | Case-Control | J Autoimmun | PSC에서 GSTT1이 자가항원으로 확인; GST-glutathione 대사 이상의 면역 병리적 역할 시사 |
| [15041041](https://pubmed.ncbi.nlm.nih.gov/15041041/) | 2004 | Clinical Study | J Autoimmun | 자가면역 간염에서 anti-GST A1-1 자가항체의 빈도 및 임상적 의의 규명 |
| [38967587](https://pubmed.ncbi.nlm.nih.gov/38967587/) | 2024 | Basic Science | Hepatol Commun | 담즙정체 간질환에서 β-catenin 결손 시 glutathione의 산화 스트레스 조절 핵심 역할 확인 |
| [29148959](https://pubmed.ncbi.nlm.nih.gov/29148959/) | 2017 | Clinical Observational | JPEN | PSC/UC 중복 환자에서 항산화 방어 저하 및 산화 스트레스 증가 보고 |
| [9053974](https://pubmed.ncbi.nlm.nih.gov/9053974/) | 1995 | Observational | Scand J Gastroenterol | PSC 32례에서 간내 구리·셀레늄 축적 및 이상 미량원소 대사 관찰 |
| [30009888](https://pubmed.ncbi.nlm.nih.gov/30009888/) | 2018 | Animal Model | Food Chem Toxicol | 담즙정체 마우스 대사체 분석에서 glutathione 대사 경로의 현저한 변화 확인 |
| [31377417](https://pubmed.ncbi.nlm.nih.gov/31377417/) | 2019 | Animal Model | Free Radic Biol Med | PSC 모델(Mdr2KO)에서 활성 알데히드 생성 증가 및 간문맥 주변부 항산화 반응 이상 |
| [9049444](https://pubmed.ncbi.nlm.nih.gov/9049444/) | 1997 | Clinical Study | Clin Chim Acta | 만성 간질환 279례에서 혈장 GST A1-1이 간세포 손상의 민감 지표임을 확인 |
| [22370917](https://pubmed.ncbi.nlm.nih.gov/22370917/) | 2012 | Pathology Study | Dig Dis Sci | PSC 담낭에서 thioredoxin 계열 산화환원 단백질이 이형성·악성화 바이오마커로 제시 |
| [39130146](https://pubmed.ncbi.nlm.nih.gov/39130146/) | 2023 | Basic Science | Gastro Hep Adv | PSC 초기 담관 세포에서 NR0B2 조절이상 확인; 오믹스 기반 PSC 병리 기전 이해 기여 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
경화성 담관염과 glutathione의 연관성은 GSTT1 자가항원 및 생물표지자 수준의 기전적 근거(L4)에 머물러 있으며, 직접적인 치료 효능을 검증한 임상시험이 전무합니다. 한국 내 미허가 물질로 규제 경로도 불명확하여 현 단계에서는 연구 과제로 분류됩니다.

**진행하려면 필요한 것:**
- Glutathione 상세 약리학적 작용 기전(MOA) 데이터 확보 (DrugBank API 조회)
- 담즙정체 동물 모델에서의 직접 투여 전임상 효능 연구 기획
- 경구·정맥 투여 시 간 분포 및 생체이용률 데이터 검토
- 한국 식품의약품안전처(MFDS) 허가 가능성 및 규제 경로 검토
- 안전성 프로파일 확보 (TFDA 또는 MFDS 허가사항 PDF 파싱을 통한 경고·금기 정보 수집)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

