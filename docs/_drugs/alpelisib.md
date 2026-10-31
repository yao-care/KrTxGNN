---
layout: default
title: Alpelisib
parent: 모델 예측만 (L5)
nav_order: 44
evidence_level: L5
indication_count: 1
monitor_inn: "Alpelisib"
predicted_indications: ["pulmonary hypertension"]
last_modified_at: 2026-10-31
description: "Alpelisib: 예측 신규 적응증 폐고혈압 (pulmonary hypertension) (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202103823/EE"
---

# Alpelisib
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **1** 건
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

## Alpelisib: PI3K 억제제 → 폐고혈압 (pulmonary hypertension)
{: .text-alpha }

## 한 문장 요약

Alpelisib은 PI3K 경로를 표적으로 하는 약물로, 한국에서 단일 성분 제제로 허가되어 있습니다.
TxGNN 모델은 **폐고혈압(pulmonary hypertension)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 직접 뒷받침하는 임상시험은 없으며 관련 문헌 1편도 치료 효과가 아닌 약물 유발 간질성 폐질환 사례 보고입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202103823/EE |
| 예측 신규 적응증 | 폐고혈압 (pulmonary hypertension) |
| TxGNN 예측 점수 | 0.9903 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 1건 / 전체 1건) |
| 허가증 수 | 1건 (유효 1건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. Alpelisib은 PI3K 경로를 표적으로 하는 약물로 알려져 있으며, PI3K 경로 활성화는 폐혈관 리모델링과 관련이 있어 이론적으로는 기전상 연결 고리가 있을 수 있습니다.

그러나 이는 가설 수준입니다. 폐고혈압에서 alpelisib의 치료 효과를 직접 검증한 연구는 확인되지 않았습니다. 오히려 확인된 유일한 문헌은 alpelisib 투여 후 간질성 폐질환이 발생한 사례로, 폐 독성 신호가 있어 사용에 신중해야 합니다. 높은 TxGNN 점수는 모델의 예측일 뿐 임상적 근거가 아닙니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [35730191](https://pubmed.ncbi.nlm.nih.gov/35730191/) | 2023 | 증례 보고 (이상반응) | Journal of Oncology Pharmacy Practice | 진행성 유방암 환자에서 alpelisib 유발 간질성 폐질환 사례. 치료 효과가 아닌 이상반응 보고 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202103823 | 피크레이정 50·150·200밀리그램 (한국노바티스) | 필름코팅정 | 허가 적응증 텍스트는 로컬 자료에 기재되어 있지 않음 |

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적치료제 (PI3K 억제제) |
| 골수억제 위험 | 관련 데이터 없음. 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 관련 데이터 없음. 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 취급 방호 | 허가사항의 경고 및 주의사항을 참조하세요 |

## 안전성 고려사항

- **주요 신호**: 문헌에서 alpelisib 유발 간질성 폐질환 사례가 보고되었습니다. 폐 질환 대상 사용 시 특히 유의해야 합니다.
- **약물 상호작용**: 총 100건이 확인되었으며, 일부 목록은 모두 중등도(Moderate) 수준입니다. 주요 항목은 다음과 같습니다.
  - 당뇨병 치료제: acarbose, albiglutide, alogliptin, metformin, pioglitazone, acetohexamide, canagliflozin, chlorpropamide, dapagliflozin, dulaglutide, empagliflozin, ertugliflozin, exenatide, glimepiride, glipizide
  - 기타: alosetron, bupropion, dexamethasone, dronabinol, fidaxomicin

## 결론 및 다음 단계

**결정: Hold**

**사유:**
폐고혈압에 대한 alpelisib의 효능을 직접 연구한 임상시험이나 문헌이 없어 근거 수준은 L5(모델 예측만 존재)입니다. 유일한 문헌은 폐 독성 이상반응 보고로, 치료 가능성보다 안전성 우려를 시사합니다.

**진행하려면 필요한 것:**
- 폐고혈압 모델에서의 전임상 연구 등 직접적인 기전·효능 근거
- 상세한 작용 기전(MOA) 데이터
- 허가사항(경고·금기) 확인 및 폐 독성에 대한 안전성 평가
- 한국 허가 적응증 및 시판 상태의 확인
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

