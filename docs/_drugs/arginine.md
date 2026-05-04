---
layout: default
title: Arginine
parent: 僅模型預測 (L5)
nav_order: 82
evidence_level: L5
indication_count: 1
---

# Arginine
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

# Arginine: 아미노산 보충에서 위마비(Gastroparesis)로

## 한 문장 요약

Arginine(아르기닌)은 체내 필수 아미노산이자 일산화질소(NO) 합성의 전구체로, 영양 보충 및 호르몬 자극 검사 등에 활용되어 왔습니다.
TxGNN 모델은 **위마비(Gastroparesis)**에 효과가 있을 수 있다고 예측하며, 현재 **1건의 임상시험**과 **10편의 문헌**이 기전적 연관성을 지지합니다. 단, 문헌 전체가 동물 모델 연구로 구성되어 있어 인체 근거는 아직 없는 상태입니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 없음 (아미노산 영양 보충제) |
| 예측 신규 적응증 | 위마비 (Gastroparesis) |
| TxGNN 예측 점수 | 99.42% |
| 근거 수준 | L4 |
| 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

L-아르기닌(L-Arginine)은 일산화질소 합성효소(NOS)의 핵심 기질입니다. NOS는 L-아르기닌을 산화하여 일산화질소(NO)를 생성하며, 이 NO는 장관 억제성 신경(nitrergic neurons)의 주요 신경전달물질로 기능합니다. 이 경로는 위저부(gastric fundus)의 용적 수용성 이완(gastric accommodation)과 유문 괄약근 이완을 조율하는 데 필수적입니다.

L-아르기닌이 고갈되면 NO 생성이 감소하고, 억제성 신경근 전달이 차단되어 위 배출이 지연됩니다. 이것이 위마비(gastroparesis)의 핵심 병태생리입니다. PMID 25057793 (Reichardt et al., 2014, *Endocrinology*)은 이 경로를 직접 입증하였습니다. 덱사메타손 투여로 L-아르기닌이 고갈된 마우스에서 위마비가 유발되었으며, L-아르기닌을 보충하자 이 표현형이 역전되었습니다. TxGNN의 높은 예측 점수(0.9942)는 지식 그래프 내 Arginine ↔ NOS ↔ 장신경계 질환 간 강한 연결을 반영합니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01702051](https://clinicaltrials.gov/study/NCT01702051) | N/A | 알 수 없음 | 150 | 자체 췌도세포 이식 후 혈당 조절에 관한 관찰 연구. Arginine은 췌도 기능 평가를 위한 자극 검사 보조 수단으로 사용될 수 있으나, 위마비 치료를 주요 또는 이차 종점으로 평가하지 않음 (관련도 등급 C) |

> ⚠️ 검색된 임상시험 1건은 Arginine의 위마비 치료 효능을 직접 평가하지 않습니다. 위마비를 적응증으로 한 등록 임상시험은 현재 없습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [25057793](https://pubmed.ncbi.nlm.nih.gov/25057793/) | 2014 | 동물 모델 (기전) | Endocrinology | 글루코코르티코이드가 L-아르기닌 고갈을 통해 마우스 위마비를 유발; 아르기닌 보충으로 역전 확인 |
| [23639814](https://pubmed.ncbi.nlm.nih.gov/23639814/) | 2013 | 동물 모델 (기전) | Am J Physiol Gastrointest Liver Physiol | 테트라하이드로비옵테린(BH4) 결핍이 신생 마우스에서 위마비 유발; NOS-NO 경로와의 연관성 규명 |
| [35380456](https://pubmed.ncbi.nlm.nih.gov/35380456/) | 2022 | 동물 모델 | Am J Physiol Gastrointest Liver Physiol | 파킨슨병 쥐(6-OHDA) 모델에서 유문 괄약근 nitrergic 이완 장애 확인; nNOS·NO 경로 연관성 입증 |
| [19023028](https://pubmed.ncbi.nlm.nih.gov/19023028/) | 2009 | 동물 모델 | Am J Physiol Gastrointest Liver Physiol | 동기화 위 전기 자극(SGES)이 nitrergic 경로를 통해 위 용적 이완 장애를 개선 |
| [18312542](https://pubmed.ncbi.nlm.nih.gov/18312542/) | 2008 | 동물 모델 | Neurogastroenterol Motility | 당뇨병 BB-쥐 공장(jejunum)에서 nNOS 발현 감소와 장근 신경병증 특성 규명 |
| [31984783](https://pubmed.ncbi.nlm.nih.gov/31984783/) | 2020 | 동물 모델 | Am J Physiol Gastrointest Liver Physiol | 천골 신경 자극(SNS)이 척수 구심성·미주 원심성 경로를 통해 쥐의 위 용적 이완 증가 |
| [21193530](https://pubmed.ncbi.nlm.nih.gov/21193530/) | 2011 | 동물 모델 | Am J Physiol Gastrointest Liver Physiol | 고혈당이 결절 신경절 KATP 채널을 통해 위 운동을 억제하는 기전 규명 |
| [18322959](https://pubmed.ncbi.nlm.nih.gov/18322959/) | 2008 | 동물 모델 | World J Gastroenterol | 당뇨병성 위마비 마우스에서 그렐린 및 GHRP-6의 위 운동 효과 탐색 |
| [33867519](https://pubmed.ncbi.nlm.nih.gov/33867519/) | 2021 | 증례 보고 | Am J Case Reports | MELAS(미토콘드리아 질환) 환자에서 생활습관 개선 후 혈청 젖산 정상화 보고; 위마비와 간접적 연관 |
| [8194696](https://pubmed.ncbi.nlm.nih.gov/8194696/) | 1994 | 동물 모델 | Gastroenterology | 항원 자극 감작 쥐에서 지연된 위 배출 유발 기전 및 매개체 탐색 |

> ⚠️ 문헌 10편 전체가 동물 모델 또는 증례 보고이며, Arginine의 위마비 치료에 대한 인체 임상 근거(RCT·관찰 연구)는 현재 없습니다.

---

## 시판 정보

현재 허가된 시판 제품이 없습니다. 관련 허가 데이터를 제공할 수 없습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
L-아르기닌 → NOS → NO → nitrergic 신경 경로를 통한 위마비 치료의 기전적 근거는 설득력 있으나, 현재까지 인체 대상 임상 근거가 전무합니다. 확인된 임상시험 1건은 위마비 치료와 직접 무관하며, 문헌 10편 전체가 동물 모델 수준(L4)에 머물러 있어 지금 당장 임상 적용을 권장하기 어렵습니다.

**진행하려면 필요한 것:**
- 인체 대상 개념증명(Proof-of-Concept) 임상시험 설계 (당뇨병성 위마비 또는 특발성 위마비 환자군 대상)
- 상세 작용 기전(MOA) 데이터 확보 (DrugBank API 조회)
- 안전성 정보 확보 (허가사항 검토, TFDA 仿單 PDF 파싱)
- 최적 투여 경로 및 치료 용량 결정을 위한 추가 전임상 연구
- 기존 위장관 운동 촉진제(metoclopramide, domperidone)와의 병용 가능성 검토
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

