---
layout: default
title: Mogamulizumab
parent: 모델 예측만 (L5)
nav_order: 526
evidence_level: L5
indication_count: 7
last_modified_at: 2026-11-15
description: "Mogamulizumab: 예측 신규 적응증 전립선 요도 요로상피암 (Prostatic urethra urothelial carcinoma) (근거 수준 L5). 기존 적응증: 이전에 한 가지 이상의 전신요법을 받은 경험이 있는 균상식육종 또는 시자리증후군 성인 환자의 치료"
monitor_inn: "MOGAMULIZUMAB"
predicted_indications: ["prostatic urethra urothelial carcinoma", "kidney pelvis sarcomatoid transitional cell carcinoma", "infiltrating bladder urothelial carcinoma sarcomatoid variant", "renal pelvis papillary urothelial carcinoma", "human herpesvirus 8-related tumor", "ectomesenchymoma", "malignant cutaneous granular cell skin tumor"]
---

# Mogamulizumab
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **7** 건
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

## Mogamulizumab: 기존 적응증 확인 필요에서 전립선 요도 요로상피암으로
{: .text-alpha }

## 한 문장 요약

Mogamulizumab은 항 CCR4 단일클론항체로, 한국에서 주사제(포텔리지오주20밀리그램)로 시판 중입니다. 다만 이번에 정리된 데이터에는 허가 적응증의 본문이 포함되어 있지 않아 기존 적응증을 직접 확인할 수 없습니다.
TxGNN 모델은 **전립선 요도 요로상피암(prostatic urethra urothelial carcinoma)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 뒷받침하는 **임상시험은 0건**, **문헌도 0건**입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 이전에 한 가지 이상의 전신요법을 받은 경험이 있는 균상식육종 또는 시자리증후군 성인 환자의 치료 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202203641/EE)) |
| 예측 신규 적응증 | 전립선 요도 요로상피암 (Prostatic urethra urothelial carcinoma) |
| TxGNN 예측 점수 | 0.9944 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 1건 / 전체 1건) |
| 허가증 수 | 1건 (유효 1건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Mogamulizumab 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “모가물리주맙-kpkc는 탈푸코실화된 인간화 IgG1 kappa 단일클론항체로, 림프구의 여러 장기로의 이동에 관여하는 CC 케모카인에 대한 G 단백질 연결 수용체인 CCR4에 결합한다. 비임상 시험관내 연구에서 모가물리주맙-kpkc의 결합은 세포를 항체 의존성 세포 매개 세포독성(ADCC)의 표적으로 만들어 표적 세포의 고갈을 초래하는 것으로 나타났다.” 영어 원문: "Mogamulizumab-kpkc is a defucosylated, humanized IgG1 kappa monoclonal antibody that binds to CCR4, a G protein-coupled receptor for CC chemokines that is involved in the trafficking of lymphocytes to various organs. Non-clinical in vitro studies demonstrate mogamulizumab-kpkc binding targets a cell for antibody-dependent cellular cytotoxicity (ADCC) resulting in depletion of the target cells." ([DailyMed: Poteligeo (mogamulizumab-kpkc) prescribing information, Kyowa Kirin, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e53960ab-42a1-40d1-9c7d-eb013fe7f18f), 버전 2026-03-02; 확인일 2026-11-19). 알려진 정보에 따르면 Mogamulizumab은 CCR4를 표적으로 하는 단일클론항체이며, CCR4를 발현하는 세포(조절 T세포, Treg 포함)를 제거하는 것으로 알려져 있습니다. 이를 바탕으로 Treg 제거가 항종양 면역을 높여 요로상피암에서도 이론적으로 작용할 수 있다는 가설이 가능합니다.

다만 이는 가설 수준입니다. 이를 뒷받침하는 임상시험이나 문헌이 없고, 높은 점수는 TxGNN 모델(딥러닝)이 관련 질환 간에 학습한 유사성을 반영할 수 있을 뿐 생물학적 근거는 아닙니다. 기존 적응증과의 유사성 평가도 아직 이루어지지 않았습니다.

### 그 밖의 예측 후보

같은 방식으로 예측된 다른 후보도 모두 근거 수준 L5, 권장 결정 Hold입니다.

| 순위 | 예측 질환 | TxGNN 점수 | 비고 |
|-----|---------|-----------|------|
| 2 | 신우 육종양 이행세포암 | 0.9942 | 공격적 아형으로, 기존 적응증에서의 외삽이 어렵습니다. |
| 3 | 침윤성 방광 요로상피암 (육종양 변이형) | 0.9940 | 면역관문억제제와의 병용 가능성이 가설로만 제시됩니다. |
| 4 | 신우 유두상 요로상피암 | 0.9937 | 점수는 TxGNN 모델(딥러닝)에서 나온 것이며, 모델이 관련 질환 간에 학습한 유사성을 반영할 수 있으나 생물학적 근거는 아닙니다. |
| 5 | 인간 헤르페스바이러스 8 관련 종양 | 0.9924 | 면역저하 인구집단에서의 안전성 문제가 우려됩니다. |
| 6 | 외배엽성 간엽종 | 0.9915 | 기전상 뚜렷한 연관성이 확인되지 않습니다. |
| 7 | 악성 피부 과립세포 종양 | 0.9915 | 신경(슈반세포) 기원으로, T세포 유래가 아닙니다. |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202203641 | 포텔리지오주20밀리그램(모가물리주맙) | 주사제 (무색 투명한 유리 바이알에 든 무색 용액) | 허가 문서 참조 (본문 미확보) |

- 제조사: 한국쿄와기린(주)

## 안전성 고려사항

**약물 상호작용**: 총 83건이 확인되었으며, 아래는 그중 일부 주요 항목입니다.

| 중증도 | 상호작용 약물 |
|-------|------------|
| Major | Deferiprone, Samarium (153Sm) lexidronam, Adalimumab, Baricitinib |
| Moderate | Strontium chloride Sr-89, Roflumilast, Chloramphenicol, Zidovudine, Alefacept, Alemtuzumab, Anakinra, Azathioprine, Canakinumab 등 |
| Minor | 아연 제제 (황산아연, 아세트산아연, 글루콘산아연, 염화아연) |

면역억제제나 면역조절제와의 병용에서 주의가 필요해 보입니다. 경고 및 금기 사항은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 점수는 높지만 임상시험과 문헌 근거가 전혀 없는 모델 예측 단계(L5)입니다. 허가 적응증, 작용 기전, 경고·금기 정보도 확보되지 않아 안전성 검토를 시작할 수 없습니다.

**진행하려면 필요한 것:**
- 허가사항 문서(첨부문서)에서 적응증, 경고, 금기 정보 확보
- DrugBank 등에서 상세 작용 기전(MOA) 데이터 확보
- 요로상피암에서의 CCR4 발현 및 Treg 침윤에 관한 전임상·문헌 근거 조사
- 관련 임상시험 등록 현황 재검색
- 기존 적응증과 예측 적응증 간 유사성 평가 및 투여 경로 적합성 확인

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Poteligeo (mogamulizumab-kpkc) prescribing information, Kyowa Kirin, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e53960ab-42a1-40d1-9c7d-eb013fe7f18f) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

