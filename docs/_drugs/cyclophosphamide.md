---
layout: default
title: Cyclophosphamide
parent: 모델 예측만 (L5)
nav_order: 240
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
monitor_inn: "CYCLOPHOSPHAMIDE"
predicted_indications: ["vertebral anomalies and variable endocrine and T-cell dysfunction", "retroperitoneal neoplasm"]
description: "Cyclophosphamide: 예측 신규 적응증 척추 이상 및 가변적 내분비·T세포 기능장애 (vertebral anomalies and variable endocrine and T-cell dysfunction) (근거 수준 L5). 기존 적응증: 1. 악성림프종 2. 다발성골수종 3. 백혈병 4. 신경모세포종 5. 난소암 6. 망막아종 7. 유방암"
---

# Cyclophosphamide
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **2** 건
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

## Cyclophosphamide: 척추 이상 및 가변적 내분비·T세포 기능장애 (vertebral anomalies and variable endocrine and T-cell dysfunction)
{: .text-alpha }

## 한 문장 요약

Cyclophosphamide는 세포독성과 면역억제 작용을 가진 알킬화 항종양제입니다.
TxGNN 모델은 **척추 이상 및 가변적 내분비·T세포 기능장애(vertebral anomalies and variable endocrine and T-cell dysfunction)**에 효과가 있을 수 있다고 예측합니다. 다만 이 질환을 직접 다룬 **임상시험과 문헌은 한 건도 없어** 모델 예측만 있는 상태입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 1. 악성림프종 2. 다발성골수종 3. 백혈병 4. 신경모세포종 5. 난소암 6. 망막아종 7. 유방암 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200906639/EE)) |
| 예측 신규 적응증 | 척추 이상 및 가변적 내분비·T세포 기능장애 (vertebral anomalies and variable endocrine and T-cell dysfunction) |
| TxGNN 예측 점수 | 0.9938 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 5건 / 전체 8건) |
| 허가증 수 | 8건 (유효 5건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Cyclophosphamide 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “작용기전은 완전히 규명되지 않았다. 그러나 종양 세포 DNA의 교차결합이 관여할 수 있다. 사이클로포스파미드의 활성 알킬화 대사체는 감수성이 있고 빠르게 증식하는 악성 세포의 성장을 방해한다.” 영어 원문: "The mechanism of action has not been fully characterized. However, cross-linking of tumor cell DNA may be involved. The active alkylating metabolites of cyclophosphamide interfere with the growth of susceptible rapidly proliferating malignant cells." ([DailyMed: Frindovyx (cyclophosphamide) prescribing information, AVYXA Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5ad8ea65-4c98-487a-9c8d-df778765ec5e), 버전 2026-08-26; 확인일 2026-11-19). Cyclophosphamide는 알킬화 항종양제이자 면역억제제로 알려져 있습니다. 이 질환과 연결되는 뚜렷한 기전적 근거는 확인되지 않았습니다.

이 질환은 척추 기형과 내분비 이상, T세포 기능 이상을 보이는 드문 선천성 증후군입니다. T세포 기능이 이미 저하된 환자에게 세포독성·면역억제 약물을 쓰면 오히려 해로울 수 있습니다. 높은 예측 점수는 계산상의 결과일 뿐이며, 임상적·기전적 타당성을 뒷받침하는 자료는 아닙니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 197600065 | 알키록산정(시클로포스파미드정) | 백색의 필름코팅정 | 제이더블유중외제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/197600065/EE) | 유효 |
| 199504135 | 엔독산주500mg(시클로포스파미드) | 흰색의 결정성 가루가 무색투명한 바이알에 든 주사제 | 부광약품(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199504135/EE) | 유효 |
| 200906637 | 코러스시클로포스파미드주500mg(시클로포스파미드)(수출용) | 백색의 분말이 든 무색 투명한 바이알 | 한국코러스(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200906637/EE) | 유효 |
| 200906638 | 코러스시클로포스파미드주200mg(시클로포스파미드)(수출용) | 백색의 분말이 든 무색 투명한 바이알 | 한국코러스(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200906638/EE) | 유효 |
| 200906639 | 코러스시클로포스파미드주1그람(시클로포스파미드)(수출용) | 백색의 분말이 든 무색 투명한 바이알 | 한국코러스(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200906639/EE) | 유효 |

위 표는 허가 8건 중 5건입니다.

<!-- licenses:end -->

허가 건수와 상태는 빠른 개요와 위 표에 있습니다. 허가 적응증 본문은 식약처 허가사항 문서에서 확인할 수 있습니다.

<!-- review:begin kr-lic-20261124c-cyclophosphamide-1 -->

> **검토 정정 (2026-11-24)**: 원래 문장: “5건 모두 단일 성분 제제이며 유효 상태입니다.” 식품의약품안전처 의약품안전나라(nedrug) 허가 자료(2026-11-23 데이터) 기준으로 수정했습니다: 이 사이트 자료의 성분란에는 일치한 성분만 기록되어 허가 품목별 단일 성분·복합 성분 여부를 확인할 수 없으므로, 단일·복합 표기를 빼고 건수는 쓰지 않고 빠른 개요와 「한국 시판 정보」의 표를 가리키도록 고쳤습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261124c-cyclophosphamide-1 -->

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 약물 (알킬화제, 질소 머스터드 계열) |
| 골수억제 위험 | 고 (호중구감소증 등 혈구감소 가능) |
| 구토 유발성 등급 | 중~고 (용량에 따라 다름) |
| 모니터링 항목 | CBC(분류 포함), 간·신기능, 전해질, 소변검사(출혈성 방광염 확인) |
| 취급 방호 | 세포독성 약물 취급 규정 준수 필요 (조제·투여 시 보호장비 착용) |

자세한 내용은 허가사항의 경고 및 주의사항을 참조하세요.

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 조회되었으며, 대부분 중등도(Moderate) 수준입니다. 주요 항목은 다음과 같습니다.
  - 항진균제: Amphotericin B (일반 제형, 지질복합체, 콜레스테릴 설페이트, 리포좀 제형)
  - 혈당강하제: Chlorpropamide, Acetohexamide, Glimepiride, Glipizide, Glyburide, Nateglinide, Repaglinide, Tolazamide, Tolbutamide, Troglitazone
  - 기타: Bupropion, Aprepitant, Metronidazole, Nitisinone
  - 경미(Minor) 수준: Levofloxacin, Ondansetron

허가사항상의 경고·금기 정보는 이번 데이터에 없으므로 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 이 질환을 직접 다룬 임상시험이나 문헌이 없고 모델 점수만 있어 근거 수준이 L5입니다.
- 면역억제 약물이 T세포 기능장애 환자에게 해로울 수 있다는 우려도 있습니다.

**진행하려면 필요한 것:**
- 이 질환에서 cyclophosphamide의 작용 기전을 뒷받침하는 전임상·기전 연구
- 이 질환의 병태생리(T세포 기능장애)와 면역억제 작용의 상충 여부에 대한 검토
- 질환을 직접 다룬 증례 보고나 임상 근거
- 허가사항(경고·금기)의 확인과 안전성 검토

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다. 작용 기전 자료가 없다는 문장은 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Frindovyx (cyclophosphamide) prescribing information, AVYXA Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5ad8ea65-4c98-487a-9c8d-df778765ec5e) |
| 2026-11-24 | 단일·복합 표기: “5건 모두 단일 성분 제제이며 유효 상태입니다.” → 확인할 수 없는 단일·복합 표기와 건수 삭제(건수는 빠른 개요와 표) | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

