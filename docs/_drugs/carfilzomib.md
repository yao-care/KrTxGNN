---
layout: default
title: Carfilzomib
parent: 僅模型預測 (L5)
nav_order: 177
evidence_level: L5
indication_count: 5
---

# Carfilzomib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Carfilzomib: 다발골수종에서 흑색종(Melanoma)으로

## 한 문장 요약

Carfilzomib은 문헌 근거상 다발골수종(Multiple Myeloma) 표준 치료제로 확인되는 불가역적 프로테아좀 억제제입니다.
TxGNN 모델은 **흑색종(Melanoma)**에 효과가 있을 수 있다고 예측하며, 현재 관련 임상시험은 없지만 **5편의 전임상/기전 문헌**이 이 방향을 뒷받침합니다.
동일 예측군 상위권에 흑색종 아형(CMM7, 소아 연수막 흑색종, 상피양세포 포도막 흑색종, 외음부 흑색종)이 반복적으로 등장해 신호가 수렴하는 양상이나, 이들 아형 자체는 임상시험·문헌 근거가 전무합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 다발골수종 (Multiple Myeloma) — *문헌 PMID 27016342에서 "frontline anti-myeloma drug"로 확인, 허가사항 원문(MOA)은 데이터 미확보* |
| 예측 신규 적응증 | 흑색종 (Melanoma) |
| TxGNN 예측 점수 | 99.03% |
| 근거 수준 | L4 |
| 한국 시판 현황 | ✗ 미시판 (허가 없음) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 Carfilzomib의 상세 작용기전(MOA) 데이터는 확보되지 않았습니다(Data Gap, DG002). 다만 문헌 근거를 통해 프로테아좀 억제제로서 26S 프로테아좀을 불가역적으로 차단하여 잘못 접힌 단백질 축적, ER stress 유발, NF-κB 경로 억제를 통해 세포사멸(apoptosis)을 유도하는 기전이 확인됩니다.

TxGNN 예측 상위 5개 후보가 모두 흑색종 관련 질환(CMM7 흑색종 감수성 유전자좌, 소아 연수막 흑색종, 상피양세포 포도막 흑색종, 외음부 흑색종, 일반 흑색종)이라는 점은 지식그래프 상에서 흑색종이라는 질환군과의 연결성이 뚜렷함을 시사합니다. 다만 이 중 실제 문헌 근거가 존재하는 것은 일반 흑색종(melanoma) 하나뿐이며, 나머지 4건(CMM7·소아 연수막 흑색종·포도막 흑색종·외음부 흑색종)은 임상시험·문헌이 전혀 없는 순수 모델 예측(L5, Hold)입니다. 특히 CMM7은 독립된 임상 질환이 아닌 흑색종 감수성 유전자좌로, 치료 표적으로서의 임상적 실체가 불명확합니다.

일반 흑색종에 대해서는 B16-F1 흑색종 세포주에서 bortezomib과의 병용 시 apoptosis 증강(PMID 33671902), 분자도킹/동역학 시뮬레이션을 통한 흑색종 표적 친화성(PMID 36134605), 흑색종 세포 생존 관련 유전자 조절 기전(PMID 31540997) 등 기전적 개연성을 지지하는 전임상 근거가 존재하나, 모두 세포주/in silico 수준이며 인체 임상 근거는 없습니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [33671902](https://pubmed.ncbi.nlm.nih.gov/33671902/) | 2021 | 체외실험(전임상) | Biology | B16-F1 흑색종 세포에서 carfilzomib+bortezomib 병용이 caspase 3/8/9/12 활성화를 통한 apoptosis를 증강 |
| [36134605](https://pubmed.ncbi.nlm.nih.gov/36134605/) | 2023 | 인실리코(분자도킹/시뮬레이션) | J Biomol Struct Dyn | 10개 암종(흑색종 포함) 대상 18개 키나아제 표적에 대한 기존 약물 재창출 도킹/동역학 스크리닝 |
| [31540997](https://pubmed.ncbi.nlm.nih.gov/31540997/) | 2019 | 체외실험(기전연구) | Mol Cancer Res | ZFAND2A(AIRAP) 유전자가 인간 흑색종 세포 생존 및 프로테아좀 스트레스 반응을 조절, E3-ligase cIAP2 관여 |
| [29581547](https://pubmed.ncbi.nlm.nih.gov/29581547/) | 2018 | 체외실험(PROTAC) | Leukemia | BET 계열 단백질 표적 PROTAC이 다발골수종 전임상 모델에서 활성 (프로테아좀 분해 기전 공유) |
| [27016342](https://pubmed.ncbi.nlm.nih.gov/27016342/) | 2016 | 체외실험(간접기전) | Matrix Biol | Bortezomib·carfilzomib 등 골수종 1차 치료제가 NF-κB 경로 활성화를 통해 heparanase 발현 유도, 침습성 표현형과 연관 |

---

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적치료제 (Proteasome Inhibitor 계열) — 문헌상 다발골수종 1차 치료제로 확인 |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 취급 방호 | 허가사항의 경고 및 주의사항을 참조하세요 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
흑색종 적응증에 대한 근거는 세포주/in silico 수준의 전임상 데이터(L4)에 그치며 인체 임상시험이 전무합니다. 또한 TFDA 경고·금기 정보가 Blocking 수준으로 미확보되어 안전성 초평(S1) 진입 자체가 불가능하며, 한국 내 허가·시판 이력도 없습니다.

**진행하려면 필요한 것:**
- TFDA 허가사항(경고·금기) 확보 및 파싱 (DG001, Blocking)
- DrugBank MOA 상세 데이터 확보 (DG002)
- 흑색종 동물모델(in vivo) 또는 초기 임상시험 근거
- 한국 내 허가 가능성 검토 (현재 미시판)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

