---
layout: default
title: Benralizumab
parent: 모델 예측만 (L5)
nav_order: 134
evidence_level: L5
indication_count: 5
monitor_inn: "BENRALIZUMAB"
predicted_indications: ["thrombocytopenia due to immune destruction", "dermatitis", "acne keloid", "neonatal dermatomyositis", "amyopathic dermatomyositis"]
last_modified_at: 2026-10-31
description: "Benralizumab: 예측 신규 적응증 면역 파괴에 의한 혈소판감소증 (thrombocytopenia due to immune destruction) (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201903766/EE"
---

# Benralizumab
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **5** 건
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

## Benralizumab: 항IL-5 수용체 알파 단일클론항체 → 면역 파괴에 의한 혈소판감소증 (thrombocytopenia due to immune destruction)
{: .text-alpha }

## 한 문장 요약

Benralizumab은 IL-5 수용체 알파(IL5RA)를 표적으로 하여 호산구와 호염기구를 감소시키는 단일클론항체입니다.
TxGNN 모델은 **면역 파괴에 의한 혈소판감소증(thrombocytopenia due to immune destruction)**에 효과가 있을 수 있다고 예측하지만, 현재 이 질환을 직접 다룬 **임상시험은 0건**, **문헌도 0편**으로 모델 예측 단계에 머물러 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201903766/EE |
| 예측 신규 적응증 | 면역 파괴에 의한 혈소판감소증 (thrombocytopenia due to immune destruction) |
| TxGNN 예측 점수 | 0.9934 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 1건 / 전체 1건) |
| 허가증 수 | 1건 (유효 1건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 없습니다. 이번 보고서를 위해 수집한 자료에 따르면, benralizumab은 IL-5 수용체 알파 subunit(IL5RA)에 결합하는 항체로, 항체 의존성 세포독성(ADCC)을 통해 호산구와 호염기구를 제거하는 것으로 알려져 있습니다.

그러나 호산구 감소와 혈소판 면역 파괴 사이의 직접적인 연결고리는 제공된 자료에서 확인되지 않습니다. 따라서 이 예측은 기전적으로 뒷받침되었다기보다 모델 점수에 근거한 가설 단계로 보아야 합니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201903766 | 파센라프리필드시린지주30밀리그램(벤라리주맙) | 프리필드시린지 주사제 | 적응증 텍스트가 문서 링크로만 기록되어 있어 요약 불가 |

## 안전성 고려사항

- **약물 상호작용**: 약리학 정보상 표적은 IL-5 수용체 알파 subunit(IL5RA)이며, 임상적으로 의미 있는 약물 간 상호작용 등급 정보는 없습니다.

그 외 경고·금기 등 안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
면역 파괴에 의한 혈소판감소증에 대해 제공된 임상시험과 문헌이 없고, 호산구 고갈과 혈소판 파괴 사이의 기전적 연관성도 확인되지 않았습니다. 모델 점수만으로는 진행 근거가 부족합니다.

**진행하려면 필요한 것:**
- 면역성 혈소판감소증과 IL-5/호산구 경로의 연관성을 보여주는 전임상·기전 연구
- 해당 질환을 직접 다룬 임상시험 또는 문헌 확보
- 허가사항 기반의 경고·금기 등 안전성 정보 확보
- 상세한 작용 기전(MOA) 데이터 보완
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

