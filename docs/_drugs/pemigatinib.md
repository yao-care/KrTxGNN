---
layout: default
title: Pemigatinib
parent: 모델 예측만 (L5)
nav_order: 587
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
description: "Pemigatinib: 예측 신규 적응증 다발성 내분비 종양 (multiple endocrine neoplasia) (근거 수준 L5). 기존 적응증: 1회 이상의 전신치료를 받은 성인에서 FGFR2(fibroblast growth factor…"
monitor_inn: "Pemigatinib"
predicted_indications: ["multiple endocrine neoplasia", "amenorrhea (disease)", "HER2 positive breast carcinoma", "cytomegalovirus infection", "infectious bovine rhinotracheitis", "malignant catarrh", "amyotrophic lateral sclerosis", "amyotrohpic lateral sclerosis type 22", "axial spondylometaphyseal dysplasia"]
---

# Pemigatinib
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

## Pemigatinib: 허가 적응증에서 다발성 내분비 종양(MEN)으로
{: .text-alpha }

## 한 문장 요약

Pemigatinib은 FGFR1-3 키나아제 억제제로, 한국에서 정제가 허가되어 시판 중입니다(허가 건수와 상태는 빠른 개요 참조). 다만 허가 적응증의 구체적 내용은 이번 보고서용 데이터에 텍스트로 포함되어 있지 않습니다.
TxGNN 모델은 **다발성 내분비 종양(multiple endocrine neoplasia)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 직접 뒷받침하는 **임상시험은 0건, 문헌도 0편**입니다. 따라서 모델 예측 수준의 가설입니다.

<!-- review:begin kr-lic-20261124c-pemigatinib-1 -->

> **검토 정정 (2026-11-24)**: 원래 문장: “Pemigatinib은 FGFR1-3 키나아제 억제제로, 한국에서 단일제 정제 3종이 허가되어 시판 중입니다.” 식품의약품안전처 의약품안전나라(nedrug) 허가 자료(2026-11-23 데이터) 기준으로 수정했습니다: 단일·복합 표기와 건수를 본문에 고정해 쓰지 않고, 매주 갱신되는 허가 자료를 반영하는 빠른 개요와 「한국 시판 정보」의 표를 가리키도록 고쳤습니다. 2026-11-25에 식품의약품안전처 품목허가 상세 자료(2026-03)의 주성분명으로 품목별로 다시 확인한 결과, 이 자료에 수록된 허가 품목은 모두 단일 성분 제제입니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261124c-pemigatinib-1 -->

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 1회 이상의 전신치료를 받은 성인에서 FGFR2(fibroblast growth factor receptor 2, 섬유아세포 성장인자수용체2) 융합 또는 재배열이 존재하는 국소진행성 또는 전이성 담관암 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202301337/EE)) |
| 예측 신규 적응증 | 다발성 내분비 종양 (multiple endocrine neoplasia) |
| TxGNN 예측 점수 | 0.9971 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 3건 / 전체 3건) |
| 허가증 수 | 3건 (유효 3건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터는 수집되지 않았습니다. 알려진 정보에 따르면 Pemigatinib은 FGFR1-3을 억제하는 키나아제 억제제입니다. FGF/FGFR 신호전달은 일부 내분비 종양에서 연구된 바 있어 생물학적으로 전혀 근거가 없지는 않습니다.

그러나 이번에 수집된 자료에는 FGFR 억제와 다발성 내분비 종양을 직접 연결하는 임상시험이나 문헌이 없습니다. 기존 적응증과의 유사성 분석도 아직 진행되지 않았습니다. 높은 TxGNN 점수(0.9971)는 TxGNN 모델(딥러닝)이 산출한 값으로, 모델이 관련 질환 간에 학습한 유사성을 반영할 수 있을 뿐 생물학적 근거가 아니며, 효능의 증거로 해석해서는 안 됩니다.

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 202301337 | 페마자이레정13.5밀리그램(페미가티닙) | 한쪽 면에는 “I”, 다른 한쪽 면에는 “13.5”로 각인된 흰색 내지… | (주)한독 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202301337/EE) | 유효 |
| 202301338 | 페마자이레정9밀리그램(페미가티닙) | 한쪽 면에는 “I”, 다른 한쪽 면에는 “9”로 각인된 흰색 내지 옅은… | (주)한독 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202301338/EE) | 유효 |
| 202301339 | 페마자이레정4.5밀리그램(페미가티닙) | 한쪽 면에는 “I”, 다른 한쪽 면에는 “4.5”로 각인된 흰색 내지 옅… | (주)한독 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202301339/EE) | 유효 |

<!-- licenses:end -->

제조·판매사는 모두 (주)한독입니다.

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적치료제 (FGFR 키나아제 억제제) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 취급 방호 | 허가사항의 경고 및 주의사항을 참조하세요 |

## 안전성 고려사항

- **약물 상호작용**: 이번 보고서용 데이터에서 총 50건의 상호작용이 확인되었으며, 아래는 그중 일부입니다.
  - **Major**: Aprepitant, Dexamethasone, Clarithromycin, Cobicistat, Lumacaftor, Chloramphenicol, Erythromycin, Ketoconazole, Fluconazole
  - **Moderate**: Cimetidine, Metreleptin, Clotrimazole, Glycerol phenylbutyrate, Troglitazone, Deferasirox, Ivacaftor, Zafirlukast, Griseofulvin, Elagolix, Osilodrostat
  - 강력한 CYP3A4 억제제·유도제와의 병용 가능성이 있으므로 병용 약물 검토가 필요합니다.

주요 경고와 금기는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
다발성 내분비 종양에 대한 TxGNN 점수는 매우 높지만 임상시험과 문헌 근거가 전혀 없는 L5(모델 예측만 존재) 단계입니다. 허가사항의 경고·금기 정보도 확보되지 않아 안전성 심사 단계로 진행할 수 없습니다.

**진행하려면 필요한 것:**
- 허가사항(PDF) 확보 및 분석: 적응증, 경고, 금기 확인
- DrugBank 등에서 작용 기전(MOA) 데이터 확보
- FGFR 억제와 내분비 종양 사이의 기전적 연관성을 다룬 전임상·임상 문헌 탐색
- 관련 임상시험 등록 여부 확인
- 기존 적응증과의 유사성 및 투여 경로 적합성 평가

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-24 | 단일·복합 표기: “Pemigatinib은 FGFR1-3 키나아제 억제제로, 한국에서 단일제…” → 고정된 단일·복합 표기와 건수 삭제(건수는 빠른 개요와 표) | 정정 (2026-11-25 수정, 이전 판은 기록에 보존) | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

