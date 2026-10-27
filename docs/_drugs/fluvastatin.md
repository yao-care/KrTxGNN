---
layout: default
title: Fluvastatin
parent: 모델 예측만 (L5)
nav_order: 363
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Fluvastatin: 예측 신규 적응증 고지단백혈증 (hyperlipoproteinemia) (근거 수준 L5). 기존 적응증: 지질 이상(고콜레스테롤혈증 등). 허가 문서 원문은 링크로만 제공되어 본문은 확인하지 못했습니다"
monitor_inn: "Fluvastatin"
predicted_indications: ["hyperlipoproteinemia", "homozygous familial hypercholesterolemia", "hypercholesterolemia due to cholesterol 7alpha-hydroxylase deficiency", "familial hypercholesterolemia", "HIV infectious disease", "cholesterol-ester transfer protein deficiency", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "simian immunodeficiency virus infection"]
---

# Fluvastatin
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
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

## Fluvastatin: 지질강하제(스타틴)에서 고지단백혈증으로
{: .text-alpha }

## 한 문장 요약

Fluvastatin은 HMG-CoA 환원효소를 억제하는 스타틴계 약물로, 한국에서는 서방정(레스콜엑스엘)으로 시판되며 지질 이상 치료에 사용됩니다.
TxGNN 모델은 **고지단백혈증(hyperlipoproteinemia)**에 효과가 있을 것으로 예측하며(점수 99.99%), 연결된 임상시험은 **1건**, 문헌은 **20편**입니다.
다만 이 임상시험은 fluvastatin이 아닌 다른 약물(alirocumab)의 연구이고, 이 예측은 진정한 재창출이 아니라 이미 확립된 용도에 가깝습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 지질 이상(고콜레스테롤혈증 등). 허가 문서 원문은 링크로만 제공되어 본문은 확인하지 못했습니다. |
| 예측 신규 적응증 | 고지단백혈증 (hyperlipoproteinemia) |
| TxGNN 예측 점수 | 99.99% |
| 근거 수준 | L2 (fluvastatin 무작위 대조 문헌 기반, 연결된 등록 임상시험은 해당 없음) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

Fluvastatin은 간에서 콜레스테롤 합성을 담당하는 HMG-CoA 환원효소를 억제합니다. 그 결과 간 콜레스테롤 합성이 줄고 LDL 수용체가 증가하며 LDL 콜레스테롤이 감소합니다. 이 데이터에는 별도의 상세 작용 기전 항목이 없으므로, 위 설명은 스타틴 계열의 확립된 기전에 근거한 것입니다.

고지단백혈증은 LDL 콜레스테롤 등 지질단백이 높아지는 상태입니다. 따라서 LDL 수용체를 늘려 LDL을 낮추는 fluvastatin의 기전과 직접 맞닿아 있습니다. 즉 이 예측은 새로운 질환으로의 확장이 아니라 약의 본래 작용 영역에 해당합니다.

고지단백혈증을 직접 다룬 fluvastatin 문헌에는 원발성 고콜레스테롤혈증, 혼합형 고지혈증, 가족성 고콜레스테롤혈증 환자 연구가 포함됩니다. 이러한 연구들이 예측의 타당성을 뒷받침합니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | 완료 | 18 | 8~17세 동형접합 가족성 고콜레스테롤혈증 소아에서 alirocumab(PCSK9 항체)의 LDL-C 감소 효과를 평가한 공개 라벨 시험. fluvastatin과 무관하여 직접 근거는 아닙니다. |

참고로, 같은 계열의 질환인 가족성 고콜레스테롤혈증에는 fluvastatin을 직접 시험한 완료된 Phase 3 연구가 있습니다. 소아 이형접합 가족성 고콜레스테롤혈증 84명을 대상으로 한 [NCT00171236](https://clinicaltrials.gov/study/NCT00171236)입니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [11219479](https://pubmed.ncbi.nlm.nih.gov/11219479/) | 2001 | 무작위 비교시험 | Clin Ther | 원발성 고콜레스테롤혈증에서 fluvastatin 80 mg 서방형과 속방형의 효능·내약성 비교 |
| [15598476](https://pubmed.ncbi.nlm.nih.gov/15598476/) | 2004 | RCT (12개월, 이중맹검) | Clin Ther | 복합 고지혈증, 제2형 당뇨병, 관상동맥질환 환자에서 fluvastatin+fenofibrate 병용과 fluvastatin 단독 비교 |
| [17062478](https://pubmed.ncbi.nlm.nih.gov/17062478/) | 2006 | 임상시험 | Acta Paediatr | 소아·청소년 이형접합 가족성 고콜레스테롤혈증에서 fluvastatin의 효능과 안전성 |
| [10856536](https://pubmed.ncbi.nlm.nih.gov/10856536/) | 2000 | 무작위 이중맹검 임상시험 | Atherosclerosis | 관상동맥질환 및 혼합형 고지혈증 333명에서 fluvastatin+bezafibrate 병용의 지질 개선과 안전성(FACT 연구) |
| [8157036](https://pubmed.ncbi.nlm.nih.gov/8157036/) | 1993 | 이중맹검 임상시험 | Eur J Clin Pharmacol | 가족성 고콜레스테롤혈증 52명에서 고용량 fluvastatin의 효능과 안전성 |
| [7517835](https://pubmed.ncbi.nlm.nih.gov/7517835/) | 1994 | 공개 임상시험 | Drugs | 고령 고콜레스테롤혈증 여성 22명에서 fluvastatin 40 mg의 6주간 효능·안전성·내약성 |
| [7604789](https://pubmed.ncbi.nlm.nih.gov/7604789/) | 1995 | 임상 연구 | Am J Cardiol | 중국인 고콜레스테롤혈증 환자 31명에서 지질 프로필과 아포지단백 개선 |
| [10067240](https://pubmed.ncbi.nlm.nih.gov/10067240/) | 1998 | 비교 임상 연구 | Ter Arkh | 원발성 고지단백혈증에서 simvastatin과 fluvastatin의 지질 저하 효과 변동성 비교 |
| [7604794](https://pubmed.ncbi.nlm.nih.gov/7604794/) | 1995 | 임상 연구 | Am J Cardiol | 일본인 고콜레스테롤혈증 환자(이형접합 가족성 포함)에서 1년간 효능·안전성 평가 |
| [8462180](https://pubmed.ncbi.nlm.nih.gov/8462180/) | 1993 | 리뷰 | Circulation | 이상지질단백혈증 약물치료 25년을 개관하고 fluvastatin에 초점 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200108760 | 레스콜엑스엘서방정(플루바스타틴나트륨) | 황색의 원형 필름 코팅 서방정 | 허가 문서 링크로만 제공됨 ([허가 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200108760/EE)) |

제조사는 한국노바티스(주)이며 단일제로 유효한 허가입니다.

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 보고되어 있습니다. 확인된 항목 중 중등도(Moderate) 상호작용은 다음과 같습니다.
  - 다른 스타틴: rosuvastatin, simvastatin
  - 항감염제: metronidazole, tinidazole
  - 혈당강하제: nateglinide, glyburide
  - 그 외: aprepitant, oxandrolone, naltrexone, nitisinone, pectin
- 등급이 미상인 항목에는 calcitriol, doxycycline, cimetidine, famotidine, pantoprazole, acetylsalicylic acid 등이 있습니다.

그 밖의 경고·금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
fluvastatin은 고지단백혈증의 기전과 직접 맞닿은 기존 용도이고, 무작위 비교시험을 포함한 다수의 fluvastatin 문헌이 이를 지지합니다. 반면 연결된 등록 임상시험은 다른 약물(alirocumab)의 연구라 직접 근거가 되지 못하므로, 근거 수준은 L2에 머뭅니다.

**진행하려면 필요한 것:**
- 허가 적응증 원문과 경고·금기 정보 확인 (허가 문서 PDF 분석)
- fluvastatin 단독 효능을 직접 입증하는 임상시험 또는 연구 설계 확인 (문헌 상세 검토)
- 간효소와 CK 모니터링, 병용약물 상호작용 검토
- 작용 기전 데이터 보완 (DrugBank 등)

**참고:** 같은 데이터의 다른 예측 중 가족성 고콜레스테롤혈증은 fluvastatin을 직접 시험한 완료 Phase 3 근거(NCT00171236)가 있어 가장 탄탄합니다. 반면 HIV 감염은 소규모·예비 연구와 전임상 수준에 그쳐 추가 연구가 필요한 단계입니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

