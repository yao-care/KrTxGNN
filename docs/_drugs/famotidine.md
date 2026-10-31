---
layout: default
title: Famotidine
parent: 모델 예측만 (L5)
nav_order: 338
evidence_level: L5
indication_count: 4
monitor_inn: "FAMOTIDINE"
predicted_indications: ["duodenal obstruction", "abnormality of glucagon secretion", "multiple endocrine neoplasia", "acne (disease)"]
last_modified_at: 2026-10-31
description: "Famotidine: 예측 신규 적응증 십이지장 폐색 (duodenal obstruction) (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/198700535/EE"
---

# Famotidine
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **4** 건
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

## Famotidine: H2 수용체 길항제 → 십이지장 폐색 (duodenal obstruction)
{: .text-alpha }

## 한 문장 요약

Famotidine은 위산 분비를 억제하는 H2 수용체 길항제 계열의 약물입니다.
TxGNN 모델은 **십이지장 폐색(duodenal obstruction)**에 효과가 있을 수 있다고 예측하지만, 이 질환을 직접 연구한 임상시험은 **0건**이며 관련 문헌 **2편**도 수술 증례 보고에 그칩니다.
따라서 현재는 모델 예측 단계의 가설로 보는 것이 적절합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/198700535/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202105231/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201401404/EE; 이 약은 위산과다, 속쓰림, 신트림에 사용합니다.; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202002958/EE; 이 약은 위산과다 및 속쓰림과 관련된 가슴앓이의 경감에  |
| 예측 신규 적응증 | 십이지장 폐색 (duodenal obstruction) |
| TxGNN 예측 점수 | 0.9999 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 18건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보로는 famotidine은 H2 수용체 길항제로 위산 분비를 줄이는 약물이며, 이 때문에 위·십이지장 궤양 관련 질환과 연관되어 예측 점수가 높게 나온 것으로 보입니다.

그러나 십이지장 폐색은 대개 구조적·기계적 원인(궤양 흉터, 크론병, 종양 등)으로 생기며, 산 억제만으로 폐색 자체가 해결된다는 근거는 없습니다. 검색된 문헌은 famotidine을 이 질환에 평가한 것이 아니라, 문합부 궤양과 십이지장 크론병의 수술 사례입니다. 따라서 뚜렷한 기전적 연결 고리는 확인되지 않았습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [8165479](https://pubmed.ncbi.nlm.nih.gov/8165479/) | 1994 | 증례 보고 | Surgical Endoscopy | 위공장문합술 후 발생한 거대 문합부 궤양. 폐색 등 합병증 가능성을 기술하며 famotidine 평가는 아님 |
| [9306611](https://pubmed.ncbi.nlm.nih.gov/9306611/) | 1997 | 증례 보고(수술) | Surgery Today | 십이지장 크론병으로 인한 위 출구 폐색의 수술 치료 1례. famotidine 평가는 아님 |

## 한국 시판 정보

허가 자료는 최소 20건이며 목록은 일부일 수 있습니다. 대부분의 적응증 항목은 문서 링크로만 기재되어 있어, 텍스트가 확인되는 주요 허가만 표시합니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202001760 | 파모텍스정10밀리그램 | 녹색의 원형 필름코팅정 | 위산과다, 속쓰림, 신트림 |
| 202105229 | 듀얼파모정 | 연두색의 장방형 필름코팅정 | 위산과다 및 속쓰림과 관련된 가슴앓이의 경감 |
| 202000704 | 티파딘정10mg | 연녹색의 원형 필름코팅정 | 위산과다, 속쓰림, 신트림 |
| 202002541 | 파모타제정10밀리그램 | 연녹색의 원형 필름코팅정제 | 위산과다, 속쓰림, 신트림 |
| 202502157 | 모틴주사액 | 주사제 | 허가 문서 링크로만 제공됨 |

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 조회되었으며, 대부분 중등도(Moderate) 수준입니다. 예: abiraterone, acalabrutinib, tramadol, amiodarone, amitriptyline, aripiprazole 등. 알루미늄 수산화물, alendronic acid는 경미(Minor) 수준입니다.

그 외 경고 및 금기는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
십이지장 폐색을 직접 연구한 임상시험이나 문헌이 없고, 확인된 문헌은 famotidine과 무관한 수술 증례 2건뿐입니다. 높은 TxGNN 점수(0.9999)만으로는 근거가 부족하며 뚜렷한 기전적 연결도 없습니다.

**진행하려면 필요한 것:**
- famotidine의 상세 작용 기전 데이터 보완
- 십이지장 폐색에서 famotidine을 평가한 임상 또는 전임상 연구 확인
- 한국 허가 문서(PDF)에서 경고·금기 및 적응증 텍스트 확보
- 시판 상태(취소 여부) 확인
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

