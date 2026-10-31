---
layout: default
title: Pemigatinib
parent: 모델 예측만 (L5)
nav_order: 587
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-31
description: "Pemigatinib: 예측 신규 적응증 다발성 내분비 종양 (multiple endocrine neoplasia) (근거 수준 L5). 기존 적응증: 확인 불가 (허가증에 적응증 본문 대신 허가사항 링크만 수록됨)"
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

Pemigatinib은 FGFR1-3 키나아제 억제제로, 한국에서 단일제 정제 3종이 허가되어 시판 중입니다. 다만 허가 적응증의 구체적 내용은 이번 보고서용 데이터에 텍스트로 포함되어 있지 않습니다.
TxGNN 모델은 **다발성 내분비 종양(multiple endocrine neoplasia)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 직접 뒷받침하는 **임상시험은 0건, 문헌도 0편**입니다. 따라서 모델 예측 수준의 가설입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (허가증에 적응증 본문 대신 허가사항 링크만 수록됨) |
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

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202301337 | 페마자이레정13.5밀리그램(페미가티닙) | 흰색~옅은 황백색 원형 정제 ("I", "13.5" 각인) | 허가사항 문서 참조 |
| 202301338 | 페마자이레정9밀리그램(페미가티닙) | 흰색~옅은 황백색 타원형 정제 ("I", "9" 각인) | 허가사항 문서 참조 |
| 202301339 | 페마자이레정4.5밀리그램(페미가티닙) | 흰색~옅은 황백색 원형 정제 ("I", "4.5" 각인) | 허가사항 문서 참조 |

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
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

