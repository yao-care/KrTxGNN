---
layout: default
title: Prasugrel
parent: 모델 예측만 (L5)
nav_order: 622
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
description: "Prasugrel: 예측 신규 적응증 폐고혈압 (Pulmonary Hypertension) (근거 수준 L5). 기존 적응증: 관상동맥중재술(percutaneous coronary intervention PCI)을 실시하였거나 실시할…"
monitor_inn: "Prasugrel"
predicted_indications: ["pulmonary hypertension", "migraine disorder", "migraine with brainstem aura", "kyphoscoliotic heart disease", "rheumatoid arthritis", "homozygous familial hypercholesterolemia", "hypoalphalipoproteinemia", "brachydactyly-syndactyly syndrome", "leprosy"]
---

# Prasugrel
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

## Prasugrel: 허가 적응증에서 폐고혈압으로
{: .text-alpha }

## 한 문장 요약

Prasugrel은 한국에서 에피언트정(5mg, 10mg)으로 허가·시판 중인 P2Y12 억제 항혈소판제입니다. TxGNN 모델은 **폐고혈압(Pulmonary Hypertension)**에 효과가 있을 수 있다고 예측하지만, 이를 직접 뒷받침하는 임상시험은 **0건**이고 관련 문헌 **2편**은 모두 간접적인 관찰 연구입니다. 따라서 현재는 모델 예측 수준의 근거만 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 관상동맥중재술(percutaneous coronary intervention PCI)을 실시하였거나 실시할 다음의 급성관상동맥증후군 환자에서 스텐트 혈전증을 포함한 혈전성 심혈관 사건(심혈관 질환으로 인한 사망, 치명적이지 않은심근경색 또는 치명적이지 않은 뇌졸중)의 발생율 감소 -… ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201004754/EE)) |
| 예측 신규 적응증 | 폐고혈압 (Pulmonary Hypertension) |
| TxGNN 예측 점수 | 0.9988 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 2건 / 전체 2건) |
| 허가증 수 | 2건 (유효 2건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Prasugrel 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “프라수그렐은 활성 대사체가 혈소판의 P2Y 12 계열 ADP 수용체에 비가역적으로 결합함으로써 혈소판 활성화 및 응집을 억제하는 억제제이다.” 영어 원문: "Prasugrel is an inhibitor of platelet activation and aggregation through the irreversible binding of its active metabolite to the P2Y 12 class of ADP receptors on platelets." ([DailyMed: Effient (prasugrel hydrochloride) prescribing information, Cosette Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=69ea2d58-5353-4222-b61f-cab976fa7e5e), 버전 2022-09-07; 확인일 2026-11-19). 알려진 정보에 따르면 Prasugrel은 P2Y12 수용체 길항제로 혈소판 응집을 억제하는 항혈소판제입니다.

혈소판 활성화와 폐혈관 내 국소 혈전 형성은 폐혈관 리모델링에 기여할 수 있어, 기전상 그럴듯한 연관성은 있습니다. 다만 이는 입증되지 않은 가설입니다. TxGNN 점수는 매우 높지만 이를 뒷받침하는 임상시험은 없습니다.

참고로 같은 모델이 예측한 다른 후보 중 **편두통**(2순위, 점수 0.9988)은 근거가 더 많습니다. 아래 "결론 및 다음 단계"에서 함께 다룹니다.

## 임상시험 근거

현재 폐고혈압과 관련된 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [21241206](https://pubmed.ncbi.nlm.nih.gov/21241206/) | 2011 | 코호트 | Curr Med Res Opin | 경피적 관상동맥 중재술을 받은 급성 관상동맥 증후군 환자에서 clopidogrel 사용·순응도·지속성 관련 요인 분석. 폐고혈압과는 직접 관련 없음 |
| [34713782](https://pubmed.ncbi.nlm.nih.gov/34713782/) | 2021 | 코호트 | Kardiologiia | COVID-19 이전 동반질환 약물치료가 사망 위험에 미치는 영향을 분석한 레지스트리 연구. 폐고혈압과는 직접 관련 없음 |

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 201004754 | 에피언트정10밀리그램(프라수그렐염산염) | 미황색의 육각형 모양 필름 코팅 정제 | 한국다이이찌산쿄(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201004754/EE) | 유효 |
| 201004753 | 에피언트정5밀리그램(프라수그렐염산염) | 황색의 육각형 모양 필름 코팅 정제 | 한국다이이찌산쿄(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201004753/EE) | 유효 |

<!-- licenses:end -->

두 제품 모두 한국다이이찌산쿄(주) 제조입니다(허가 건수와 상태는 빠른 개요와 위 표 참조).

<!-- review:begin kr-lic-20261124c-prasugrel-1 -->

> **검토 정정 (2026-11-24)**: 원래 문장: “두 제품 모두 한국다이이찌산쿄(주) 제조의 단일제이며 유효한 허가 상태입니다.” 식품의약품안전처 의약품안전나라(nedrug) 허가 자료(2026-11-23 데이터) 기준으로 수정했습니다: 단일·복합 표기와 건수를 본문에 고정해 쓰지 않고, 매주 갱신되는 허가 자료를 반영하는 빠른 개요와 「한국 시판 정보」의 표를 가리키도록 고쳤습니다. 2026-11-25에 식품의약품안전처 품목허가 상세 자료(2026-03)의 주성분명으로 품목별로 다시 확인한 결과, 이 자료에 수록된 허가 품목은 모두 단일 성분 제제입니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261124c-prasugrel-1 -->

## 안전성 고려사항

- **지식그래프 기반 금기 관련 질환** (허가사항 문구가 아닌 TxGNN 지식그래프 정보): 간부전, 저혈압, 혈액응고 질환, 뇌졸중, 뇌혈관 질환, 뇌경색, 혈소판감소성 자반증, 두개내 출혈, 일과성 허혈 발작, 척추기저동맥 부전 등
- **약물 상호작용** (총 100건 조회, 주요 항목):
  - 중대(Major): Deferasirox, Ibritumomab tiuxetan
  - 중등도(Moderate): Acetylsalicylic acid(아스피린), Morphine, Opium, Fenfluramine, Dexfenfluramine, Sibutramine
  - 경미(Minor): 양성자펌프억제제(Omeprazole, Esomeprazole, Pantoprazole 등), H2 차단제(Famotidine, Ranitidine 등), Bupropion

경고 및 금기의 정식 내용은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
폐고혈압 예측은 모델 점수에만 의존하며(L5), 임상시험이 없고 문헌도 간접적입니다. 또한 출혈 위험이 있는 항혈소판제이고 허가사항의 경고·금기 정보가 확보되지 않아 안전성 검토를 진행할 수 없습니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기) 확보 및 파싱 (현재 진행을 막는 핵심 공백)
- 작용 기전(MOA) 데이터 보충
- 폐고혈압에서 혈소판 P2Y12 억제의 효과를 보는 전임상 또는 탐색적 임상 근거
- 우선순위 재검토: 편두통(L3, 연구 질문 단계)과 전조가 있는 편두통은 레트로스펙티브 연구와 소규모 오픈라벨 연구(ticagrelor)가 있어 폐고혈압보다 근거가 앞섭니다. 다만 직접적인 prasugrel 무작위 시험 근거는 제한적이며, 관련 시험(NCT07629635)은 PFO 치료를 평가하는 진행 중 3상 시험(참여자 32명)으로 prasugrel 자체를 검증하는 것은 아닙니다.

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다. 작용 기전 자료가 없다는 문장은 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Effient (prasugrel hydrochloride) prescribing information, Cosette Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=69ea2d58-5353-4222-b61f-cab976fa7e5e) |
| 2026-11-24 | 단일·복합 표기: “두 제품 모두 한국다이이찌산쿄(주) 제조의 단일제이며 유효한 허가 상태입…” → 고정된 단일·복합 표기와 건수 삭제(건수는 빠른 개요와 표) | 정정 (2026-11-25 수정, 이전 판은 기록에 보존) | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

