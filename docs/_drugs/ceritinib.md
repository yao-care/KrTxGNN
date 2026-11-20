---
layout: default
title: Ceritinib
parent: 모델 예측만 (L5)
nav_order: 201
evidence_level: L5
indication_count: 9
monitor_inn: "CERITINIB"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "hamartoma of lung", "lung benign neoplasm", "pulmonary sulcus neoplasm", "lung germ cell tumor", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome", "junctional epidermolysis bullosa"]
last_modified_at: 2026-11-20
description: "Ceritinib: 예측 신규 적응증 치은 섬유종증 (fibromatosis, gingival) (근거 수준 L5). 기존 적응증: 역형성 림프종 인산화효소 (ALK) 양성 국소 진행성 또는 전이성 비소세포폐암의 치료"
---

# Ceritinib
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **9** 건
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

## Ceritinib: ALK/ROS1 키나아제 억제제 → 치은 섬유종증 (fibromatosis, gingival)
{: .text-alpha }

## 한 문장 요약

Ceritinib은 ALK/IGF-1R/ROS1을 억제하는 키나아제 억제제 계열의 항암제입니다.
TxGNN 모델은 **치은 섬유종증(fibromatosis, gingival)**에 효과가 있을 수 있다고 예측하지만, 이 질환을 직접 다룬 임상시험과 문헌은 **0건**입니다. 현재는 모델 예측만 있는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 역형성 림프종 인산화효소 (ALK) 양성 국소 진행성 또는 전이성 비소세포폐암의 치료 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201500142/EE)) |
| 예측 신규 적응증 | 치은 섬유종증 (fibromatosis, gingival) |
| TxGNN 예측 점수 | 0.9986 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 1건 / 전체 1건) |
| 허가증 수 | 1건 (유효 1건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Ceritinib 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “세리티닙은 키나제 억제제이다. 임상적으로 유의한 농도에서 생화학적 또는 세포 분석을 통해 확인된 세리티닙의 억제 표적에는 ALK, 인슐린 유사 성장인자 1 수용체(IGF-1R), 인슐린 수용체(InsR) 및 ROS1이 포함된다.” 영어 원문: "Ceritinib is a kinase inhibitor. Targets of ceritinib inhibition identified in either biochemical or cellular assays at clinically relevant concentrations include ALK, insulin-like growth factor 1 receptor (IGF-1R), insulin receptor (InsR), and ROS1." ([DailyMed: Zykadia (ceritinib) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=fff5d805-4ffd-4e8e-8e63-6f129697563e), 버전 2026-10-28; 확인일 2026-11-19). 알려진 정보에 따르면 ceritinib은 ALK, IGF-1R, ROS1을 표적으로 하는 키나아제 억제제입니다.

그러나 이러한 표적 억제와 치은 섬유종증의 발병 기전 사이에서 확인된 연관성은 없습니다. 높은 예측 점수는 계산 모델의 결과일 뿐이며, 이를 뒷받침하는 임상시험이나 문헌이 없어 기전상 타당성을 주장하기 어렵습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201500142 | 자이카디아캡슐150밀리그램(세리티닙) | 상부 파랑색 하부 흰색의 불투명 경질 캡슐 | 허가 문서 링크만 기재되어 있어 적응증 텍스트는 확인되지 않음 |

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적치료제 (키나아제 억제제) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 취급 방호 | 허가사항의 경고 및 주의사항을 참조하세요 |

## 안전성 고려사항

- **약물 상호작용**: 이번 조회에서 총 100건의 상호작용이 확인되었으며, 이 중 일부를 아래에 정리했습니다.
  - 주요(Major) 등급: triamcinolone, budesonide
  - 중등도(Moderate) 등급: acarbose, famotidine, ranitidine, rabeprazole, omeprazole, hydrocortisone, dexamethasone, betamethasone, metformin, pioglitazone, alogliptin, albiglutide, canagliflozin, loperamide, aprepitant, bisacodyl 등

경고와 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
치은 섬유종증에 대한 임상시험과 문헌이 전혀 없고, 기전상 연결고리도 확인되지 않았습니다. 높은 예측 점수만으로는 진행을 정당화하기 어렵습니다.

**진행하려면 필요한 것:**
- ALK/IGF-1R/ROS1 억제와 치은 섬유종증 병태생리 간 연관성에 대한 기전 연구
- 전임상 연구 등 이 질환을 직접 다루는 근거
- 한국 허가사항(경고, 금기, 적응증)의 확보 및 검토
- 상세한 약물 작용 기전(MOA) 데이터

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Zykadia (ceritinib) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=fff5d805-4ffd-4e8e-8e63-6f129697563e) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

