---
layout: default
title: Mitomycin
parent: 모델 예측만 (L5)
nav_order: 523
evidence_level: L5
indication_count: 7
last_modified_at: 2026-11-03
monitor_inn: "mitomycin"
predicted_indications: ["solid pseudopapillary carcinoma of pancreas", "osteoclastic giant cell tumor of pancreas", "pancreatic carcinoma with mixed differentiation", "mixed ductal-endocrine carcinoma of pancreas", "undifferentiated pancreatic carcinoma", "pancreatic intraductal papillary-mucinous neoplasm", "pancreatic acinar cell cystadenocarcinoma"]
description: "Mitomycin: 예측 신규 적응증 고형 가유두상 췌장암 (solid pseudopapillary carcinoma of pancreas) (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199201621/EE"
---

# Mitomycin
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

## Mitomycin: 고형 가유두상 췌장암 (solid pseudopapillary carcinoma of pancreas)
{: .text-alpha }

## 한 문장 요약

Mitomycin은 DNA를 교차결합시키는 알킬화 계열의 항종양제입니다.
TxGNN 모델은 **고형 가유두상 췌장암(solid pseudopapillary carcinoma of pancreas)**에 효과가 있을 수 있다고 예측합니다(예측 점수 0.9986).
다만 이 질환을 직접 다룬 임상시험이나 문헌은 현재 없어, 근거는 모델 예측 수준(L5)에 그칩니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199201621/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199701737/EE |
| 예측 신규 적응증 | 고형 가유두상 췌장암 (solid pseudopapillary carcinoma of pancreas) |
| TxGNN 예측 점수 | 0.9986 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 2건 / 전체 2건) |
| 허가증 수 | 2건 (유효 2건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 확보되지 않았습니다. 알려진 정보에 따르면 mitomycin은 DNA를 교차결합시키는 알킬화 세포독성 약물로, 암세포의 DNA 복제를 방해해 증식을 억제합니다.

이러한 일반적인 세포독성 기전은 췌장의 희귀 상피성 종양에도 이론상 적용될 수 있습니다. 그러나 이 종양에 대한 임상시험이나 문헌이 제시되지 않았으므로, 현재의 연관성은 모델 예측에 근거한 가설 단계입니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 199201621 | 한국유나이티드미토마이신씨주(수출용) | 동결건조 결정/분말 바이알(주사제) | 허가사항 문서 참조 |
| 199701737 | 한국유나이티드미토마이신씨주10밀리그람(수출용) | 동결건조 결정/분말 바이알(주사제) | 허가사항 문서 참조 |

두 건 모두 단일 성분 제제이며 현재 유효합니다.

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 약물 (DNA 교차결합 알킬화제) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | CBC(혈소판·백혈구 포함), 신기능 |
| 취급 방호 | 세포독성 약물 취급 규정 준수 필요 |

## 안전성 고려사항

- **약물 상호작용**: 총 193건의 상호작용이 조회되었습니다. 주요 항목은 다음과 같습니다.
  - 중대(Major): Deferiprone, Samarium (153Sm) lexidronam
  - 중등도(Moderate): Palifermin, Strontium chloride Sr-89, Fostamatinib
  - 경미(Minor): Levofloxacin
  - 그 외 Warfarin, Dexamethasone, Ondansetron 등은 등급이 미상입니다.
- **주의가 필요한 질환·상태**: 신장 질환, 혈소판감소증, 혈액응고 장애, 빈혈, 백혈구감소증, 용혈성 요독 증후군, 울혈성 심부전, 구내염 등이 관련 질환으로 확인되었습니다. 이는 허가사항 본문이 아닌 모델 데이터에서 도출된 정보이므로 허가사항 확인이 필요합니다.

허가사항의 경고 및 금기 정보는 별도로 확인해야 합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 예측 점수는 매우 높지만(0.9986) 이 질환을 직접 다룬 임상시험과 문헌이 없어 근거 수준이 L5입니다.
- 허가사항의 경고·금기 정보도 확보되지 않아 안전성 검토를 진행할 수 없습니다.

**진행하려면 필요한 것:**
- 식약처 허가사항(PDF) 확인 및 경고·금기 정보 정리
- 상세한 작용 기전(MOA) 데이터 확보
- 고형 가유두상 췌장암에서 mitomycin을 다룬 임상시험 또는 문헌 탐색
- 병용 가능성이 있는 약물과의 상호작용 검토

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

