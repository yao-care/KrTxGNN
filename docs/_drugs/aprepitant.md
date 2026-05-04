---
layout: default
title: Aprepitant
parent: 僅模型預測 (L5)
nav_order: 79
evidence_level: L5
indication_count: 10
---

# Aprepitant
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

# Aprepitant: 화학요법 유발 오심·구토에서 지주막하출혈로

> **다중 적응증 분석 보고서** | 총 10개 예측 적응증 포함 | 2026-04-05

---

## 한 문장 요약

Aprepitant는 Substance P의 NK1(뉴로키닌-1) 수용체를 선택적으로 차단하는 항구토제로, 화학요법 유발 오심·구토(CINV) 및 수술 후 오심·구토(PONV) 예방에 사용됩니다.
TxGNN 모델은 지주막하출혈을 포함한 **총 10개 질환**에 대한 재창출 가능성을 예측하였으나, **10개 모두 임상시험 근거가 없으며**, 수집된 문헌 21건 또한 전부 문헌 매칭 오류(false positive)로 확인되었습니다.
이 중 **지주막하출혈(SAH)**만이 NK1 길항 기전과 생물학적으로 의미 있는 연결고리를 가져 연구 가설 수립(S1) 단계 진행이 단독 권고됩니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 화학요법 유발 오심·구토(CINV), 수술 후 오심·구토(PONV) 예방 |
| 최우선 권고 적응증 | 지주막하출혈 (Subarachnoid Hemorrhage, 예측 9위) |
| TxGNN 예측 점수 | 99.85% (SAH) / 99.97% (1위 NSIAD) |
| 근거 수준 | L5 (전체 10개 적응증) |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold (SAH 단독: Research Question) |

---

## 이 예측이 타당한 이유는?

Aprepitant는 Substance P(SP)의 NK1(뉴로키닌-1) 수용체를 뇌 및 말초에서 선택적으로 차단합니다. 혈뇌장벽을 투과하는 특성 덕분에 중추신경계 내 SP/NK1 신호를 직접 억제할 수 있으며, 이 기전이 화학요법 유발 지연성 구역질 억제에 핵심적입니다. 동시에 이 혈뇌장벽 투과성은 중추신경계 질환에서의 이론적 적용 가능성을 제공합니다.

10개 예측 적응증 중 **지주막하출혈(SAH)**만이 이 기전과 의미 있는 연결고리를 가집니다. SAH 발생 후 뇌척수액 및 뇌실질 내 Substance P 수준이 현저히 상승하고, NK1 수용체 활성화가 뇌혈관 연축(cerebral vasospasm) 및 이차 뇌 손상(secondary brain injury)을 악화시킨다는 전임상 근거가 문헌상 존재합니다(본 데이터셋 미포함). Aprepitant의 혈뇌장벽 투과성은 이 적응증에서 특히 중요한 약동학적 이점입니다.

나머지 9개 적응증은 기전 연결고리가 없거나 고도로 추측적입니다. 1위 NSIAD는 AVPR2(V2R) 기능 획득 돌연변이에 의한 질환으로 NK1 시스템과의 연결은 극히 간접적입니다. 척추측만증성 심장병(7위)은 기계적 원인의 질환, Dandy-Walker 기형(8위)·Ambras형 다모증(5위)·유전성 모간 이상(10위)은 선천성 유전·구조 결손 질환으로 약리적 NK1 길항 치료의 이론적 근거 자체가 성립하기 어렵습니다.

---

## 예측 적응증 전체 현황

| 순위 | 질환명 | TxGNN 점수 | 기전 강도 | 임상시험 | 문헌 | 결정 |
|------|--------|-----------|---------|:------:|:----:|------|
| 1 | 부적절 항이뇨 신성 증후군 (NSIAD) | 99.97% | 극히 낮음 | 0 | 0 | Hold |
| 2 | 다모증 (Hypertrichosis) | 99.91% | 낮음 | 0 | 0 | Hold |
| 3 | 폐고혈압 (Pulmonary Hypertension) | 99.90% | 낮음 | 0 | 1 ⚠️ | Hold |
| 4 | 나병 (Leprosy) | 99.90% | 낮음 (간접) | 0 | 0 | Hold |
| 5 | Ambras형 선천 전신 다모증 | 99.87% | 매우 낮음 | 0 | 0 | Hold |
| 6 | 치아·치주 동반 기형 증후군 | 99.86% | 낮음 | 0 | 20 ⚠️ | Hold |
| 7 | 척추측만증성 심장병 | 99.86% | 없음 | 0 | 0 | Hold |
| 8 | Dandy-Walker 기형 증후군 | 99.86% | 없음 | 0 | 0 | Hold |
| **9** | **지주막하출혈 (SAH)** | **99.85%** | **중등도** | 0 | 0 | **Research Question** |
| 10 | 유전성 모간 이상 | 99.85% | 없음 | 0 | 0 | Hold |

> ⚠️ 문헌이 수집된 3위·6위 항목의 문헌은 모두 **문헌 매칭 오류(false positive)**로 실질적 근거로 인정할 수 없습니다.

---

## 임상시험 근거

현재 예측된 10개 적응증 모두에 대해 Aprepitant 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 예측된 10개 적응증 모두에 대해 Aprepitant와 직접 관련된 유효한 문헌이 없습니다.

다음은 데이터셋에 포함되었으나 문헌 매칭 오류로 판단된 항목입니다.

### 폐고혈압 (순위 3) — 1건

| PMID | 연도 | 유형 | 저널 | 오류 사유 |
|------|-----|------|------|---------|
| [28261651](https://pubmed.ncbi.nlm.nih.gov/28261651/) | 2016 | Phase I RCT | Oncology and Therapy | Pazopanib+Cisplatin 병용 고형종양 연구로, Aprepitant 및 폐고혈압과 무관 |

### 치아·치주 동반 기형 증후군 (순위 6) — 20건 전부 오류

| PMID | 연도 | 유형 | 저널 |
|------|-----|------|------|
| [35688447](https://pubmed.ncbi.nlm.nih.gov/35688447/) | 2022 | 임상 진료 지침 | J Clin Periodontol |
| [22057194](https://pubmed.ncbi.nlm.nih.gov/22057194/) | 2012 | 리뷰 | Diabetologia |
| [9495612](https://pubmed.ncbi.nlm.nih.gov/9495612/) | 1998 | 관찰 연구 | J Clin Periodontol |
| [37435999](https://pubmed.ncbi.nlm.nih.gov/37435999/) | 2023 | 리뷰 | Periodontology 2000 |
| [35420698](https://pubmed.ncbi.nlm.nih.gov/35420698/) | 2022 | 체계적 문헌고찰 | Cochrane Database |
| [39233377](https://pubmed.ncbi.nlm.nih.gov/39233377/) | 2024 | 리뷰 | Periodontology 2000 |
| [36883660](https://pubmed.ncbi.nlm.nih.gov/36883660/) | 2023 | 리뷰 | J Dental Research |
| [29193334](https://pubmed.ncbi.nlm.nih.gov/29193334/) | 2018 | 리뷰 | Periodontology 2000 |
| [12010523](https://pubmed.ncbi.nlm.nih.gov/12010523/) | 2002 | 근거 검토 | J Clin Periodontol |
| [38907216](https://pubmed.ncbi.nlm.nih.gov/38907216/) | 2024 | 리뷰 | J Nanobiotechnology |

(이외 10건 생략 — 모두 동일 패턴의 일반 치주병 배경 문헌)

> ⚠️ 위 21건 전부 일반 치주병 또는 관련 전신 질환 배경 연구로, Aprepitant·NK1 길항·Substance P의 구강 질환 적용과 무관합니다. 해당 질환에 대한 실질적 근거로 간주할 수 없습니다.

---

## 한국 시판 정보

현재 한국 내 Aprepitant 허가 품목이 없습니다. 재창출 연구 진행 시 별도의 시판 허가 취득이 필요합니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold (지주막하출혈에 대해서만 Research Question)**

**사유:**
- 예측된 10개 적응증 중 9개는 NK1/Substance P 시스템과 기전 연결이 없거나 고도로 추측적이며, 전임상 및 임상 근거가 전무합니다.
- 지주막하출혈만이 SAH 후 SP 상승 → NK1 수용체 활성화 → 뇌혈관 연축·이차 뇌 손상이라는 병태생리 경로와 NK1 길항 기전이 부합하고, Aprepitant의 혈뇌장벽 투과성이 약동학적으로 유리하게 작용합니다.
- 수집된 문헌 21건(폐고혈압 1건 + 치주 기형 증후군 20건)은 모두 문헌 매칭 오류로, 어떠한 예측 적응증에 대한 실질적 근거로도 인정할 수 없습니다.

**진행하려면 필요한 것:**

- **지주막하출혈 S1 진행 조건:**
  - SAH 동물 모델에서 NK1 길항제 효과 관련 전임상 문헌 체계적 수집 (본 데이터셋 미포함 문헌 별도 검색 필요)
  - Aprepitant 혈뇌장벽 투과율 및 뇌 내 NK1 수용체 점유율 정량 데이터 확인
  - SAH 코호트에서의 Substance P 농도 변화 관련 바이오마커 데이터 검토
- **데이터 갭 해소 (전체 적응증 공통):**
  - **DG001 (Blocking):** TFDA 허가사항 다운로드 및 경고·금기 데이터 확보
  - **DG002 (High):** DrugBank API를 통한 상세 MOA 데이터 확보
  - DDI 데이터 확보 (현재 0건)

---

> **면책 고지:** 본 보고서는 약물 재창출 연구 참고 목적으로만 작성되었으며, 의료적 처방이나 임상 결정을 구성하지 않습니다. 모든 재창출 후보는 적절한 임상 검증 과정을 거쳐야 합니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

