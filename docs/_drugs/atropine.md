---
layout: default
title: Atropine
parent: 僅模型預測 (L5)
nav_order: 101
evidence_level: L5
indication_count: 2
---

# Atropine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# ATROPINE: 서맥·전처치에서 편두통으로

## 한 문장 요약

ATROPINE은 무스카린 수용체 길항제로, 주로 서맥 치료, 유기인 중독 해독 및 수술 전 전처치에 활용되어 왔으나 한국에는 현재 허가된 제품이 없습니다. TxGNN 모델은 **편두통(migraine disorder)**에 효과가 있을 수 있다고 예측하며, 현재 **임상시험은 없고 13편의 전임상·기전 문헌**이 부교감 신경 경로를 통한 연관 가능성을 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 서맥, 유기인 중독 해독, 수술 전 전처치 (한국 미허가) |
| 예측 신규 적응증 | 편두통 (migraine disorder) |
| TxGNN 예측 점수 | 99.56% |
| 근거 수준 | L4 |
| 한국 시판 현황 | ✗ 미허가 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터(MOA)는 확보되지 않은 상태입니다. 알려진 정보에 따르면, ATROPINE은 무스카린 아세틸콜린 수용체(M1–M5)의 경쟁적 길항제로, 부교감 신경 전달을 광범위하게 억제하여 심박수 증가, 분비물 감소, 동공 확대 등의 효과를 나타냅니다. 이 기전을 바탕으로 편두통과의 연관성은 세 가지 경로로 설명됩니다.

첫째, **부교감 신경 경로**: 편두통 발작 시 접형구개신경절(SPG)이 과활성화되어 아세틸콜린이 방출되고, 이는 경막 혈관 확장과 신경원성 염증을 유발합니다 (PMID:9344563). ATROPINE의 무스카린 차단이 이 경로를 억제할 수 있습니다. 둘째, **피질 확산성 탈분극(CSD) 조절**: 콜린성 시스템이 무스카린 수용체 활성화를 통해 CSD를 억제한다는 마우스 신피질 실험 근거가 있으며 (PMID:36485173), 편두통 선행 조짐(aura)의 발생에 개입 가능성을 시사합니다. 셋째, **중추 진통 협조**: 수마트립탄의 항통각 효과가 중추 콜린성 시스템에 의존하며, ATROPINE 투여 시 이 효과가 차단됨이 동물 실험에서 확인되었습니다 (PMID:8930196).

다만, 위 기전 근거의 대부분은 동물 모델에서 유래하며, 편두통 치료 맥락에서 ATROPINE 특유의 말초 부작용(구강 건조, 심박수 증가, 동공 산대)에 대한 내약성은 임상적으로 검증된 바 없습니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|------|------|------|---------|
| [36485173](https://pubmed.ncbi.nlm.nih.gov/36485173/) | 2024 | 기전/전임상 | Eur J Neuroscience | 콜린성 조절이 무스카린 수용체 활성화를 통해 마우스 신피질에서 CSD를 억제; 흥분/억제 균형 조절 및 편두통 아우라 억제 가능성 시사 |
| [9344563](https://pubmed.ncbi.nlm.nih.gov/9344563/) | 1997 | 동물 실험 | Experimental Neurology | 접형구개신경절 자극으로 쥐 경막 혈장 단백 누출 유발; ATROPINE 투여 시 신경원성 염증 유의하게 감소 |
| [8930196](https://pubmed.ncbi.nlm.nih.gov/8930196/) | 1996 | 동물 실험 | J Pharmacol Exp Ther | 수마트립탄의 항통각 효과는 중추 콜린성 시스템에 의존; ATROPINE 전처치로 항통각 효과가 차단됨 |
| [10193781](https://pubmed.ncbi.nlm.nih.gov/10193781/) | 1999 | 동물(ex vivo) | Br J Pharmacology | 기니피그 기저동맥에서 니코틴 유발 이완 연구에 ATROPINE 사용; 편두통 관련 약물의 혈관 작용 기전 탐색 |
| [15882801](https://pubmed.ncbi.nlm.nih.gov/15882801/) | 2005 | 동물 실험 | Neuroscience Letters | 중추 유발 안면 혈류 변화에서 CGRP 및 니코틴성 수용체 역할 확인; 삼차신경-콜린성 시스템 교차 조절 연관성 제시 |
| [2943405](https://pubmed.ncbi.nlm.nih.gov/2943405/) | 1986 | 임상 관찰 | Cephalalgia | 만성 발작성 반측두통 환자 4명에서 전신 ATROPINE 투여 후 발작 관련 발한·눈물·비강 분비물이 유의하게 감소 |
| [17186568](https://pubmed.ncbi.nlm.nih.gov/17186568/) | 2007 | 약리학 고찰 | J Applied Toxicology | ATROPINE 유도체 아니소다민(anisodamine)의 약리학적 특성 검토; ATROPINE 대비 독성이 낮고 혈관 작용 포함 |
| [1786517](https://pubmed.ncbi.nlm.nih.gov/1786517/) | 1991 | 동물 실험 | Br J Pharmacology | 에르고타민·DHE가 5-HT1C 수용체의 강력한 작용제임을 확인; 편두통 기전에서 세로토닌-콜린성 교차 조절 가능성 시사 |
| [21252](https://pubmed.ncbi.nlm.nih.gov/21252/) | 1977 | 기전 연구 | J Pharmacy Pharmacology | 베타-페닐에틸아민의 편두통 작용 기전 제안 (고전 연구; 콜린성 연관 경로 제시) |
| [40590589](https://pubmed.ncbi.nlm.nih.gov/40590589/) | 2024 | 증례 보고 | Pain Med Case Reports | 만성 편두통 환자에서 보툴리눔 독소 치료 후 두부 하수 증후군 발생; ATROPINE과 직접 관련 없으나 만성 편두통 치료 대안 탐색 맥락에서 참조 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
편두통에서 ATROPINE의 잠재적 역할을 지지하는 동물 실험 및 기전 연구가 일부 존재하지만, 임상시험 근거가 전혀 없고 한국 내 허가 제품도 없는 상황입니다. 안전성 데이터(주요 경고, 금기, 약물 상호작용) 전반에 걸쳐 데이터 공백이 존재하며, 편두통 치료 환경에서의 말초 부작용 내약성이 검증되지 않아 현 단계에서 진행 요건을 충족하지 못합니다.

**진행하려면 필요한 것:**
- 상세 작용 기전(MOA) 데이터 확보 (DrugBank API 조회 권장)
- 한국 허가 안전성 정보 확보 (허가사항 PDF 파싱 필요)
- 약물 상호작용 데이터 재조회 (DDI 쿼리 결과 not_found 상태 해소)
- 편두통 관련 ATROPINE 전임상 개념 증명(PoC) 연구 설계
- 말초 부작용 최소화를 위한 선택적 경로 제형(비강 내, 경피) 또는 뇌 선택성 높은 유도체(아니소다민 등) 검토
- 2차 예측 적응증인 **편두통 뇌간 선행 조짐(migraine with brainstem aura, TxGNN 점수 99.42%)** 또한 현재 L5 수준(모델 예측 단계)으로 별도 전임상 근거 확보가 필요함
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

