---
layout: default
title: Lurbinectedin
parent: 모델 예측만 (L5)
nav_order: 487
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Lurbinectedin: 예측 신규 적응증 다발성 내분비 종양 (multiple endocrine neoplasia) (근거 수준 L5). 기존 적응증: 허가 적응증 본문 텍스트는 확인되지 않았고 허가 문서 링크만 확인됨 (허가사항 참조)"
monitor_inn: "Lurbinectedin"
predicted_indications: ["multiple endocrine neoplasia", "HIV infectious disease", "rheumatoid arthritis", "amyotrophic lateral sclerosis", "cytomegalovirus infection", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "infectious bovine rhinotracheitis", "malignant catarrh", "Mills syndrome"]
---

# Lurbinectedin
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

# Lurbinectedin: 소세포폐암에서 다발성 내분비 종양으로

## 한 문장 요약

Lurbinectedin은 한국에서 젭젤카주(주식회사 보령)로 허가된 단일 성분 주사제로, 항종양 목적으로 사용되는 약물입니다.
TxGNN 모델은 **다발성 내분비 종양(multiple endocrine neoplasia)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 지지하는 **임상시험과 문헌은 각각 0건**입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문 텍스트는 확인되지 않았고 허가 문서 링크만 확인됨 (허가사항 참조) |
| 예측 신규 적응증 | 다발성 내분비 종양 (multiple endocrine neoplasia) |
| TxGNN 예측 점수 | 99.44% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 일반적으로 알려진 정보에 따르면, Lurbinectedin은 DNA minor groove에 결합하여 발암성 전사를 억제하는 항종양제이며, 재발성 소세포폐암(신경내분비 악성종양)에 승인된 약물입니다. 이 설명은 제공된 데이터가 아니라 일반 지식에 근거한 것입니다.

신경내분비 종양이라는 공통점 때문에 다발성 내분비 종양(MEN)과의 이론적 연관성은 생각해 볼 수 있습니다. 그러나 MEN은 MEN1, RET 등 유전자 변이에 의한 유전성 종양 증후군이며, 이번 예측은 지식 그래프 기반 점수일 뿐 임상적·문헌적 뒷받침이 없습니다.

참고로 TxGNN 상위 예측에는 HIV 감염, 류마티스 관절염, 근위축성 측삭경화증, 거대세포바이러스 감염 등 기전적 근거가 약한 질환과 수의학 질환이 다수 포함되어 있습니다. 이는 그래프 구조에서 비롯된 예측으로 보이며, 해석에 주의가 필요합니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202203642 | 젭젤카주(러비넥테딘) | 쓸 때 녹여 쓰는 주사제 (흰색 내지 거의 흰색 가루, 유리 바이알) | [허가사항 문서 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202203642/EE) |

제조사는 (주)보령입니다.

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 계열 항종양제 (DNA 결합, 전사 억제) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 (예측 근거 자료에서 골수억제와 간독성 우려가 언급됨) |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 허가사항의 경고 및 주의사항을 참조하세요 (일반적으로 CBC, 간기능 모니터링 고려) |
| 취급 방호 | 세포독성 약물 취급 규정 준수 필요 |

## 안전성 고려사항

허가사항의 경고 및 금기 정보는 이번 보고서에 수집되지 않았습니다. 안전성 정보는 허가사항을 참조하세요.

**약물 상호작용**: 약물 상호작용 조회에서 총 100건이 확인되었으며, 일부 주요(Major) 항목은 다음과 같습니다.
- **Major**: Aprepitant, Dexamethasone, Clarithromycin, Cobicistat, Deferiprone, Samarium (153Sm) lexidronam, Lumacaftor
- **Moderate**: Cimetidine, Naltrexone, Clotrimazole, Glycerol phenylbutyrate, Metreleptin, Troglitazone, Deferasirox, Palifermin, Strontium chloride Sr-89, Ticagrelor, Ivacaftor, Mercaptopurine
- **Minor**: Levofloxacin

항구토제로 흔히 쓰이는 Aprepitant와 Dexamethasone이 Major 상호작용으로 확인되므로, 병용 시 주의가 필요합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
다발성 내분비 종양에 대한 임상시험과 문헌이 없고 TxGNN 모델 예측만 있어 근거 수준이 L5입니다. 작용 기전과 허가 안전성 정보도 확보되지 않아 진행을 판단하기 어렵습니다.

**진행하려면 필요한 것:**
- 허가사항 문서(첨부문서)에서 경고, 금기, 허가 적응증 확인
- DrugBank 등에서 상세 작용 기전(MOA) 데이터 확보
- MEN(MEN1, RET 관련 신경내분비 종양)에 대한 전임상 또는 임상 근거 탐색
- 세포독성 약물로서의 골수억제·간독성 위험 대비 이익 평가
- 주요 병용약물(Aprepitant, Dexamethasone 등)과의 상호작용 관리 계획
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

