---
layout: default
title: Roxithromycin
parent: 僅模型預測 (L5)
nav_order: 295
evidence_level: L5
indication_count: 10
---

# Roxithromycin
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

# Roxithromycin: 세균 감염증에서 나병(Leprosy)으로

## 한 문장 요약

Roxithromycin은 마크로라이드계 항생제로, 원래 세균성 호흡기 감염증 및 피부 감염증 치료에 사용됩니다.
TxGNN 모델은 **나병(Leprosy)**에 효과가 있을 수 있다고 예측하며,
현재 **0건의 임상시험**과 **5편의 문헌**이 이 방향을 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 세균 감염증 (호흡기·피부 감염) |
| 예측 신규 적응증 | 나병 (Leprosy) |
| TxGNN 예측 점수 | 99.70% |
| 근거 수준 | L4 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

Roxithromycin은 마크로라이드계 항생제로, 세균의 50S 리보솜 소단위에 가역적으로 결합하여 단백질 합성을 억제합니다. 주목할 약동학적 특성은 조직/혈장 농도비(>10)가 매우 높아 대식세포 등 식세포 내에 고농도로 축적된다는 점입니다.

나병의 원인균인 *Mycobacterium leprae*는 대식세포 내 세포내 기생균입니다. 세포 내 고농도 축적이라는 Roxithromycin의 특성은 이 기생 양식과 기전적으로 높은 적합성을 보이며, 1988–1991년 사이 수행된 여러 체외 및 마우스 실험에서 Roxithromycin이 *M. leprae*에 대해 직접적인 항균·살균 활성을 나타냄이 실험적으로 확인되었습니다. 추가로, 항염증 및 면역조절 특성(IL-1β·TNF-α 억제, 카라기난 부종 억제)이 나병의 면역 병리에도 이론적 관련성을 가집니다.

다만, 동일 계열의 Clarithromycin이 감염 부위에서 더 높은 약물 농도를 달성하여 Roxithromycin보다 우월한 효능을 보인다는 비교 연구 결과가 있어 개발 차별화 근거 확보가 필요합니다. 현재까지 나병에 대한 인체 임상시험은 존재하지 않습니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|------|------|------|---------|
| [1648889](https://pubmed.ncbi.nlm.nih.gov/1648889/) | 1991 | Animal Study | Antimicrob Agents Chemother | 마우스 발바닥 감염 모델에서 Roxithromycin이 *M. leprae*에 일관된 살균 활성을 나타냄; 동일 계열 Clarithromycin이 감염 부위 농도 우위로 더 높은 효능 보임 |
| [3072920](https://pubmed.ncbi.nlm.nih.gov/3072920/) | 1988 | In vitro / Animal | Antimicrob Agents Chemother | 신규 마크로라이드계 약물의 *M. leprae* 체외 활성 평가; ATP 풀·지방산 산화·PGL-I 합성 억제로 Roxithromycin의 항균 활성 확인 |
| [2665640](https://pubmed.ncbi.nlm.nih.gov/2665640/) | 1989 | In vitro | Antimicrob Agents Chemother | 마우스 복강 대식세포 내 *M. leprae*에 대한 25종 이상 항균제 신속 평가; Roxithromycin의 세포내 활성 확인 |
| [10481449](https://pubmed.ncbi.nlm.nih.gov/10481449/) | 1999 | Clinical Commentary / Review | Nihon Hansenbyo Gakkai | Roxithromycin의 항나병균 활성과 항염증·면역조절 기전(카라기난 부종 억제, 염증성 사이토카인 억제) 동시 보고 |
| [12762831](https://pubmed.ncbi.nlm.nih.gov/12762831/) | 2003 | Review | Am J Clin Dermatol | 피부 감염에서 마크로라이드계 약물 선택 및 임상 적용 가이드; 부작용·약물 상호작용·Roxithromycin 적응증 정리 |

---

## 한국 시판 정보

Roxithromycin은 현재 한국에서 허가된 제품이 없습니다 (허가증 0건, 미시판).

---

## 안전성 고려사항

**⚠️ 항암제와의 음성 상호작용 경고**

PMID [37971309](https://pubmed.ncbi.nlm.nih.gov/37971309/) (2023년, 체외 연구)에 따르면, 마크로라이드계 약물(Roxithromycin 포함)은 MDR1/P-gp 및 CYP3A4 억제를 통해 HER2 양성 유방암 표준치료제인 T-DM1(trastuzumab emtansine)의 리소솜 내 세포독성 활성화를 유의하게 방해합니다. 이는 Roxithromycin이 현행 항암 화학요법의 효능을 저하시킬 수 있음을 시사하며, 암 환자에서의 병용 투여에 안전 우려가 있습니다.

그 외 경고, 금기, 약물 상호작용 등의 안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
Roxithromycin의 *M. leprae* 항균 활성은 1980–90년대 체외·동물 실험(L4)에서만 확인되었으며, 인체 임상시험 데이터가 전혀 없습니다. 동일 계열의 Clarithromycin이 이미 효능 우위를 보이고 있고, 한국 미시판 약물이라는 규제 장벽도 존재하여 즉각적인 개발 진행보다 추가 연구 질문 설정이 우선됩니다.

**진행하려면 필요한 것:**
- 작용 기전 상세 데이터 확보 (DrugBank MOA 조회)
- Clarithromycin 대비 Roxithromycin의 약리학적 차별점 검토 (약동학·독성 프로파일 비교)
- WHO 나병 치료 가이드라인(리팜피신·답손·클로파지민 표준요법)과의 병용 가능성 검토
- 한국 MFDS 허가 경로 타당성 검토 (현재 0건)
- 인체 타당성 연구(Phase 1/2) 설계 방안 수립
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

