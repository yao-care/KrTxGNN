---
layout: default
title: Deoxycholic Acid
parent: 모델 예측만 (L5)
nav_order: 261
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
description: "Deoxycholic Acid: 예측 신규 적응증 상염색체 우성 가족성 혈뇨-망막 세동맥 사행-구축 증후군 (autosomal dominant familial hematuri… (근거 수준 L5). 기존 적응증: 성인의 중등증 ~ 중증의 돌출되거나 과도한 턱밑 지방의 개선"
monitor_inn: "DEOXYCHOLIC ACID"
predicted_indications: ["autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "brain small vessel disease 1 with or without ocular anomalies", "diabetic nephropathy"]
---

# Deoxycholic Acid
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

## Deoxycholic Acid: 주사용 지방 감소제에서 상염색체 우성 가족성 혈뇨-망막 세동맥 사행-구축 증후군으로
{: .text-alpha }

## 한 문장 요약

Deoxycholic acid(데옥시콜산)는 한국에서 주사제 제품으로 허가되어 시판 중인 약물입니다(허가 건수와 상태는 빠른 개요 참조). 다만 허가 적응증 원문은 이번 데이터에 텍스트로 포함되어 있지 않습니다.
TxGNN 모델은 **상염색체 우성 가족성 혈뇨-망막 세동맥 사행-구축 증후군**에 효과가 있을 수 있다고 예측하지만, 이를 뒷받침하는 **임상시험은 0건, 문헌도 0편**입니다. 따라서 모델 점수에만 의존한 가설 단계입니다.

<!-- review:begin kr-lic-20261124c-deoxycholic_acid-2 -->

> **검토 정정 (2026-11-24)**: 원래 문장: “Deoxycholic acid(데옥시콜산)는 한국에서 8개 주사제 제품으로 허가되어 시판 중인 단일 성분 약물입니다.” 식품의약품안전처 의약품안전나라(nedrug) 허가 자료(2026-11-23 데이터) 기준으로 수정했습니다: 이 사이트 자료의 성분란에는 일치한 성분만 기록되어 허가 품목별 단일 성분·복합 성분 여부를 확인할 수 없으므로, 단일·복합 표기를 빼고 건수는 쓰지 않고 빠른 개요와 「한국 시판 정보」의 표를 가리키도록 고쳤습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261124c-deoxycholic_acid-2 -->

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 성인의 중등증 ~ 중증의 돌출되거나 과도한 턱밑 지방의 개선 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202402922/EE)) |
| 예측 신규 적응증 | 상염색체 우성 가족성 혈뇨-망막 세동맥 사행-구축 증후군 (autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome) |
| TxGNN 예측 점수 | 0.9949 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 8건 / 전체 8건) |
| 허가증 수 | 8건 (유효 8건) |
| 권장 결정 | Hold |

> 참고: 같은 약물에 대해 예측된 다른 후보로 "뇌 소혈관병 1형(안구 이상 동반 또는 비동반)"(점수 0.9949, L5, Hold)과 "당뇨병성 신증"(점수 0.9932, L4, Research Question)이 있습니다. 아래 상세 분석은 1순위 예측을 기준으로 하며, 다른 후보는 결론에서 간략히 다룹니다.

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Deoxycholic Acid 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “KYBELLA는 세포용해성 약물로서, 턱밑 지방과 관련된 중등도 내지 중증의 볼록함 또는 충만감이 있는 환자에서 턱밑 지방에 주사하면 세포막을 물리적으로 파괴하여 용해를 일으킨다.” 영어 원문: "KYBELLA is a cytolytic drug, which when injected into submental fat - in patients with moderate to severe convexity or fullness associated with submental fat - physically destroys the cell membrane causing lysis." ([DailyMed: Kybella (deoxycholic acid) prescribing information, Kythera Biopharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=fe431ed4-ea6f-4e99-b4bc-ec25ae7b8553), 버전 2026-09-11; 확인일 2026-11-19). 알려진 정보로는 데옥시콜산은 이차 담즙산이며, 지방세포에 대해 세포 용해(계면활성) 작용을 나타내고 담즙산 신호전달에도 관여합니다. 이 때문에 국소 지방 감소 목적의 주사제로 쓰입니다.

예측된 질환은 COL4A1 유전자와 관련된 희귀 혈관 기저막 질환입니다. 데옥시콜산의 약리 작용과 이 질환의 병태 사이에서 데이터상 확인되는 기전적 연결고리는 없습니다. 이 점수는 TxGNN 모델(딥러닝)에서 나온 것이며, 관련 질환들 사이에서 모델이 학습한 유사성을 반영했을 수 있을 뿐 생물학적 근거는 아닙니다.

따라서 높은 점수(0.9949)는 가설 생성의 출발점일 뿐이며, 기전상 타당하다고 판단할 근거는 현재 없습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 202402922 | 올리핏주(데옥시콜산) | 무색투명한 액이 무색투명한 바이알에 든 주사제 | (주)휴메딕스 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202402922/EE) | 유효 |
| 202105795 | 브이올렛주(데옥시콜산) | 무색투명한 액이 무색투명한 바이알에 든 주사제 | (주)대웅제약 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202105795/EE) | 유효 |
| 202502008 | 원더브이주(데옥시콜산) | 이물이 보이지 않는 무색투명한 액이 무색투명한 유리 바이알에 든 주사제 | (주)종근당 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202502008/EE) | 유효 |
| 202400198 | 벨라콜린주(데옥시콜산) | 무색투명한 액이 무색투명한 바이알에 든 주사제 | (주)엘지화학 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202400198/EE) | 유효 |
| 202501108 | 바이블주(데옥시콜산) | 무색투명한 액이 무색투명한 바이알에 든 주사제 | (주)한국비엠아이 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202501108/EE) | 유효 |

위 표는 허가 8건 중 5건입니다.

<!-- licenses:end -->

위 표에 주요 허가를 표시했으며, 허가 건수와 상태는 빠른 개요에 있습니다.

<!-- review:begin kr-lic-20261124c-deoxycholic_acid-1 -->

> **검토 정정 (2026-11-24)**: 원래 문장: “전체 8건 중 주요 5건만 표시했으며, 8건 모두 유효한 단일 성분 허가입니다.” 식품의약품안전처 의약품안전나라(nedrug) 허가 자료(2026-11-23 데이터) 기준으로 수정했습니다: 이 사이트 자료의 성분란에는 일치한 성분만 기록되어 허가 품목별 단일 성분·복합 성분 여부를 확인할 수 없으므로, 단일·복합 표기를 빼고 건수는 쓰지 않고 빠른 개요와 「한국 시판 정보」의 표를 가리키도록 고쳤습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261124c-deoxycholic_acid-1 -->

## 안전성 고려사항

- **약물 상호작용**: 데이터상 총 67건의 상호작용이 확인되었습니다. 표시된 항목은 모두 중등도(Moderate)이며, 주로 항응고제·항혈소판제·혈전용해제 계열입니다.
  - 항혈소판제: acetylsalicylic acid, clopidogrel, cilostazol, abciximab, cangrelor
  - 항응고제: apixaban, betrixaban, fondaparinux, dalteparin, danaparoid, argatroban, bivalirudin, desirudin
  - 혈전용해제: alteplase, anistreplase
  - 기타: antithrombin III, caplacizumab, ibritumomab tiuxetan, tositumomab
  - 이들 약물과 병용 시 출혈 위험 증가 가능성에 유의해야 합니다.

경고 및 금기 사항은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 점수는 매우 높지만 임상시험과 문헌이 전혀 없고, 약물과 질환 사이의 기전적 연결도 확인되지 않아 근거 수준이 L5에 머뭅니다. 현 단계에서는 추가 개발을 진행할 근거가 부족합니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기·허가 적응증) 확보: 현재 안전성 검토를 진행할 수 없는 차단 수준의 데이터 공백입니다.
- 데옥시콜산의 작용 기전(MOA) 데이터 확보 (DrugBank 조회)
- COL4A1 관련 혈관 기저막 질환과의 기전적 연결 가능성에 대한 전임상 근거
- 투여 경로 적합성 검토: 현재 허가 제형은 주사제뿐이며, 예측 질환에 필요한 투여 경로는 확인되지 않았습니다.
- **대안 후보 검토**: 당뇨병성 신증은 담즙산 대사 변화를 다룬 전임상·코호트 연구 4편(2021~2024)이 있어 L4 수준의 "연구 질문" 단계입니다. 다만 이 연구들은 데옥시콜산 자체를 치료제로 투여한 것이 아니며, 데옥시콜산은 세포독성·염증 유발 성격의 이차 담즙산이라 신장에서의 효과 방향도 불확실합니다. 뇌 소혈관병 1형은 1순위와 마찬가지로 근거가 없어 Hold입니다.

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다. 작용 기전 자료가 없다는 문장은 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Kybella (deoxycholic acid) prescribing information, Kythera Biopharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=fe431ed4-ea6f-4e99-b4bc-ec25ae7b8553) |
| 2026-11-24 | 단일·복합 표기: “전체 8건 중 주요 5건만 표시했으며, 8건 모두 유효한 단일 성분 허가…” → 확인할 수 없는 단일·복합 표기와 건수 삭제(건수는 빠른 개요와 표) | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |
| 2026-11-24 | 단일·복합 표기: “Deoxycholic acid(데옥시콜산)는 한국에서 8개 주사제 제품으…” → 확인할 수 없는 단일·복합 표기와 건수 삭제(건수는 빠른 개요와 표) | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

