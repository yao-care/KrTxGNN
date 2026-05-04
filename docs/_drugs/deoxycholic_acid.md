---
layout: default
title: Deoxycholic Acid
parent: 僅模型預測 (L5)
nav_order: 205
evidence_level: L5
indication_count: 3
---

# Deoxycholic Acid
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

# DEOXYCHOLIC ACID: 미허가에서 당뇨병성 신증으로

## 한 문장 요약

DEOXYCHOLIC ACID는 인체에서 자연적으로 생성되는 2차 담즙산으로, 현재 허가된 의약품 이력이 없습니다.
TxGNN 모델은 총 3개 적응증을 예측하였으며, 그 중 **당뇨병성 신증(Diabetic Nephropathy)**이 FXR/TGR5 담즙산 수용체 경로를 통한 기전적 연관성과 **20편의 문헌**으로 가장 강한 간접 근거를 보입니다.
1순위(autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome) 및 2순위(brain small vessel disease 1 with or without ocular anomalies)는 각각 L5 수준으로 근거가 불충분하여 Hold 판정입니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 이력 없음 |
| 예측 신규 적응증 | 당뇨병성 신증 (Diabetic Nephropathy) |
| TxGNN 예측 점수 | 99.32% |
| 근거 수준 | L4 |
| 시판 현황 | ✗ 미허가 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

DEOXYCHOLIC ACID는 1차 담즙산인 cholic acid에서 장내 세균에 의해 생성되는 2차 담즙산으로, 담즙산 대사의 핵심 구성 물질입니다. 현재 상세 작용 기전 데이터가 수집되지 않았으나, 담즙산 계열은 핵 수용체 **FXR(Farnesoid X Receptor)** 및 G 단백질 결합 수용체 **TGR5**의 내인성 리간드로 알려져 있습니다.

FXR과 TGR5는 신장 세뇨관 세포에서 높은 발현을 보이며, 활성화 시 항염증·항섬유화·산화 스트레스 억제 효과와 연관됩니다. 전임상 연구에서 FXR/TGR5 이중 작용제(INT-767)는 당뇨 마우스 모델의 신증 진행을 억제하였고, 구조적으로 유사한 담즙산인 UDCA(ursodeoxycholic acid)와 TUDCA(tauroursodeoxycholic acid)는 족세포 보호, SGLT2 발현 감소, ER 스트레스 억제를 통해 당뇨병성 신증을 개선함이 확인되었습니다. 실제 당뇨병성 신장질환 환자에서 담즙산 대사 이상이 단계적으로 확인된 대사체 연구(PMID: 39384774)는 이 경로 개입의 생물학적 타당성을 뒷받침합니다.

단, DEOXYCHOLIC ACID를 당뇨병성 신증에 직접 투여한 임상 또는 동물 연구는 현재 전무하며, 구조적 유사체(UDCA·TUDCA) 및 FXR/TGR5 작용제의 간접 근거에 기반한 기전 추론입니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|------|------|------|---------|
| [39384774](https://pubmed.ncbi.nlm.nih.gov/39384774/) | 2024 | 관찰/대사체 | Nutrition & Diabetes | 당뇨병성 신장질환 환자에서 담즙산 대사 이상의 단계적 진행 확인 |
| [29089371](https://pubmed.ncbi.nlm.nih.gov/29089371/) | 2018 | 동물 연구 | JASN | FXR/TGR5 이중 작용제(INT-767)가 당뇨·비만 유발 신증 진행을 차동·상승 경로로 억제 |
| [28696246](https://pubmed.ncbi.nlm.nih.gov/28696246/) | 2017 | 동물 연구 | JASN | FXR 촉진 및 TUDCA의 ER 스트레스 억제가 당뇨병성 세뇨관 병변에 보호 효과 |
| [27193377](https://pubmed.ncbi.nlm.nih.gov/27193377/) | 2016 | 동물 연구 | Biol Pharm Bull | UDCA가 산화 스트레스 억제를 통해 db/db 마우스 당뇨병성 신증 개선 |
| [26999661](https://pubmed.ncbi.nlm.nih.gov/26999661/) | 2016 | 세포 연구 | Lab Invest | UDCA가 ER 스트레스 억제로 고혈당 유발 족세포 아포토시스 예방 |
| [22429686](https://pubmed.ncbi.nlm.nih.gov/22429686/) | 2012 | 동물 연구 | Diabetes Res Clin Pract | UDCA가 당뇨 쥐 신장의 SGLT2 발현 및 산화 스트레스 유의하게 감소 |
| [36690052](https://pubmed.ncbi.nlm.nih.gov/36690052/) | 2023 | 동물 연구 | Eur J Pharmacol | TUDCA 단독 및 텔미사르탄 병용 시 당뇨병성 신장질환 개선 확인 |
| [27669287](https://pubmed.ncbi.nlm.nih.gov/27669287/) | 2016 | 동물 연구 | Nutrients | TUDCA 250 mg/kg 투여로 db/db 마우스 세뇨관 손상·혈당·단백뇨 유의 감소 |
| [37790634](https://pubmed.ncbi.nlm.nih.gov/37790634/) | 2023 | 동물 연구 | PeerJ | FXR 결손 시 당뇨 마우스에서 혈당 조절 이상 및 신장 손상 가속화 |
| [26655953](https://pubmed.ncbi.nlm.nih.gov/26655953/) | 2016 | 동물 연구 | J Biol Chem | FXR 활성화가 비만 단신장절제 마우스에서 신장 보호 효과 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
담즙산-FXR/TGR5 경로를 통한 신장 보호에 대한 간접적 전임상 근거가 존재하나, DEOXYCHOLIC ACID를 직접 사용한 당뇨병성 신증 임상 또는 동물 연구가 전무하고, 허가 이력이 없어 안전성 프로파일 확인이 불가합니다.

**진행하려면 필요한 것:**
- DEOXYCHOLIC ACID의 상세 MOA 및 FXR/TGR5 수용체 결합 친화도 데이터 확보
- MFDS/TFDA 허가사항 검토: 경고, 금기, 용량·투여 경로 정보
- 당뇨병성 신증 동물 모델(db/db 마우스 등)에서 DEOXYCHOLIC ACID 직접 투여 전임상 연구 설계
- UDCA·TUDCA 대비 FXR/TGR5 활성화 효능 비교 검토
- 경구 투여 시 신장 조직 도달 가능성(생체 이용률·신조직 분포) 평가
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

