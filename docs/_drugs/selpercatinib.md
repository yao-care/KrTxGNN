---
layout: default
title: Selpercatinib
parent: 모델 예측만 (L5)
nav_order: 688
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Selpercatinib: 예측 신규 적응증 폐동맥 고혈압 (Pulmonary Hypertension) (근거 수준 L5). 기존 적응증: 허가 적응증 본문 확인 불가 (허가 문서 링크만 제공됨)"
monitor_inn: "SELPERCATINIB"
predicted_indications: ["pulmonary hypertension", "migraine disorder", "migraine with brainstem aura"]
---

# Selpercatinib
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **3** 건
{: .fs-6 .fw-300 }

---

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 약사 평가 보고서

</div>

## Selpercatinib: 허가 적응증 정보 미확인에서 폐동맥 고혈압으로
{: .text-alpha }

## 한 문장 요약

Selpercatinib은 선택적 RET 키나아제 억제제로, 한국에서 레테브모캡슐(40mg, 80mg)로 시판 중입니다. 다만 이번 보고서에 사용된 데이터에는 허가 적응증 본문이 담겨 있지 않습니다.
TxGNN 모델은 **폐동맥 고혈압(Pulmonary Hypertension)**에 효과가 있을 수 있다고 예측하지만, 이를 직접 지지하는 **임상시험은 0건**이며 관련 문헌 3편도 폐동맥 고혈압 치료와는 무관합니다. 실질적으로 모델 예측만 있는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문 확인 불가 (허가 문서 링크만 제공됨) |
| 예측 신규 적응증 | 폐동맥 고혈압 (Pulmonary Hypertension) |
| TxGNN 예측 점수 | 99.18% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 2건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Selpercatinib은 선택적 RET 키나아제 억제제이며, RET 융합 양성 폐암이나 수질성 갑상선암 같은 RET 변이 종양에 사용됩니다. 이번 데이터에서 확인되는 문헌도 이 영역에 집중되어 있습니다.

RET 억제와 폐혈관 리모델링 사이의 직접적인 기전적 연결고리는 이번 데이터에서 확인되지 않습니다. 폐동맥 평활근 세포의 증식 신호와 관련된 키나아제 경로를 가정해 볼 수는 있으나, 이는 추측일 뿐 근거로 뒷받침되지 않습니다.

또한 Selpercatinib은 이상반응으로 전신 고혈압을 일으키는 것으로 알려져 있습니다. 이는 폐동맥 고혈압과 다른 현상이며 치료 목적 사용을 지지하지 않습니다. 높은 TxGNN 점수(99.18%)는 지식 그래프 기반 예측일 뿐입니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

아래 문헌은 폐동맥 고혈압에 대한 직접 근거가 아니라 Selpercatinib 일반 문헌입니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [39372206](https://pubmed.ncbi.nlm.nih.gov/39372206/) | 2024 | 코호트 (실사용 약물감시) | Frontiers in Pharmacology | Pralsetinib과 Selpercatinib의 이상반응 프로파일 비교 |
| [34178121](https://pubmed.ncbi.nlm.nih.gov/34178121/) | 2021 | 후향적 코호트 | Therapeutic Advances in Medical Oncology | 접근 프로그램으로 치료받은 RET 융합 양성 비소세포폐암 환자의 실사용 분석 |
| [41918669](https://pubmed.ncbi.nlm.nih.gov/41918669/) | 2026 | 증례 보고 | Cureus | RET M918T 변이 MEN 2B 동반 전이성 수질성 갑상선암의 장기 관리와 표적치료 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202201000 | 레테브모캡슐40밀리그램(셀퍼카티닙) | 회색 불투명 경질캡슐 (“Lilly”, “3977”, “40 mg” 인쇄) | 허가 문서 참조 (적응증 본문 미확인) |
| 202200999 | 레테브모캡슐80밀리그램(셀퍼카티닙) | 밝은 청색 불투명 경질캡슐 (“Lilly”, “2980”, “80 mg” 인쇄) | 허가 문서 참조 (적응증 본문 미확인) |

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적치료제 (RET 키나아제 억제제) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 취급 방호 | 허가사항의 경고 및 주의사항을 참조하세요 |

## 안전성 고려사항

- **약물 상호작용**: 상호작용 조회 결과 총 100건이 확인되었으며, 이 중 일부를 소개합니다.
  - **Major 등급**: Famotidine, Ranitidine, Cimetidine, Rabeprazole, Omeprazole, Dexlansoprazole(위산 억제제), Aprepitant, Dexamethasone, Clarithromycin, Magnesium oxide
  - **Moderate 등급**: Hydrocortisone, Triamcinolone, Betamethasone, Budesonide, Pioglitazone, Saxagliptin, Loperamide, Bisacodyl, Polyethylene glycol

위산 억제제와의 병용이 여러 건 Major로 분류되어 있으므로, 병용 시 주의가 필요합니다. 경고 및 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
폐동맥 고혈압에 대한 임상시험과 직접 관련 문헌이 없고, 근거는 TxGNN 예측 점수뿐(L5)입니다. RET 억제와 폐혈관 질환 사이의 기전적 연결도 확인되지 않았으며, 이상반응으로서 전신 고혈압이 알려져 있어 신중해야 합니다.

**진행하려면 필요한 것:**
- 허가 문서에서 기존 적응증, 경고, 금기 확인
- 상세한 작용 기전(MOA) 데이터 확보
- RET 신호와 폐혈관 리모델링의 연관성을 보여주는 전임상 근거
- 폐동맥 고혈압 관련 임상시험 또는 관찰 연구 근거
- 혈압 상승 이상반응에 대한 안전성 평가

**참고 (다른 예측 적응증):** 편두통(Migraine Disorder, 99.17%)과 뇌간 전조 편두통(Migraine with Brainstem Aura, 99.05%)도 임상시험과 문헌이 모두 없는 L5 단계이며, Hold로 평가되었습니다. 특히 뇌간 전조 편두통은 상위 편두통 노드와의 근접성이 점수에 반영되었을 가능성이 있습니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

