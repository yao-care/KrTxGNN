---
layout: default
title: Aflibercept
parent: 모델 예측만 (L5)
nav_order: 28
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Aflibercept: 예측 신규 적응증 내사시 (Esotropia) (근거 수준 L5). 기존 적응증: 허가증 링크만 제공되어 구체적인 적응증 문구는 확인되지 않음 (허가사항 참조 필요)"
monitor_inn: "Aflibercept"
predicted_indications: ["esotropia", "esophageal varices with bleeding", "esophageal varices without bleeding", "varicose disease", "urethral calculus", "adenosine deaminase deficiency", "hemorrhagic disease of newborn", "ectomesenchymoma", "malignant cutaneous granular cell skin tumor", "middle ear neuroendocrine tumor"]
---

# Aflibercept
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
{: .fs-6 .fw-300 }

---

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 약사 평가 보고서

</div>

# Aflibercept: 안과 혈관 질환에서 사시(내사시)로

## 한 문장 요약

Aflibercept는 VEGF-A, VEGF-B, PlGF를 차단하는 VEGF 트랩 계열 약물로, 한국에서는 주사제로 허가되어 시판 중입니다.
TxGNN 모델은 **내사시(Esotropia)**에 효과가 있을 수 있다고 예측하지만, 현재 이 예측을 직접 뒷받침하는 **임상시험은 0건**, **문헌도 0건**입니다.
즉, 이 예측은 모델 점수에만 의존하는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가증 링크만 제공되어 구체적인 적응증 문구는 확인되지 않음 (허가사항 참조 필요) |
| 예측 신규 적응증 | 내사시 (Esotropia) |
| TxGNN 예측 점수 | 99.38% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 11건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 수집되지 않았습니다. 알려진 정보에 따르면 Aflibercept는 VEGF-A, VEGF-B, PlGF에 결합하는 VEGF 트랩이며, 한국에서는 안구 내 주사제 등 여러 제형의 주사제로 허가되어 있습니다.

내사시는 안구 운동(사시) 질환으로, VEGF에 의해 유발되는 병리가 확립되어 있지 않습니다. 따라서 높은 TxGNN 점수(99.38%)는 생물학적 근거라기보다, Aflibercept로 치료하는 다른 안과 질환과의 네트워크상 근접성을 반영한 것으로 보입니다.

그 외 상위 10개 예측(식도 정맥류, 정맥류, 일부 종양 등)도 대부분 직접적인 임상 근거가 없습니다. 식도 정맥류는 이론상 VEGF 관련 혈관신생 근거가 있으나, 전신 VEGF 억제는 출혈 위험이 있어 출혈성 상태에서는 안전성 우려가 큽니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202500560 | 아필리부프리필드시린지 | 프리필드시린지 주사제 | 허가사항 참조 |
| 201306324 | 아일리아주사 | 바이알 주사제 | 허가사항 참조 |
| 202400753 | 아일리아주8밀리그램 | 바이알 주사제 | 허가사항 참조 |
| 202400392 | 아필리부주40밀리그램/밀리리터 | 바이알 주사제 | 허가사항 참조 |
| 202502500 | 비젠프리주사 | 바이알 주사제 | 허가사항 참조 |

이 외에도 총 11건의 유효 허가가 있으며, 모두 단일 성분 제제입니다.

## 안전성 고려사항

- **약물 상호작용**: 총 78건이 확인되었습니다. 주요(Major) 등급 예로는 Deferiprone, Samarium (153Sm) lexidronam, Adalimumab, Baricitinib, Certolizumab pegol, Cladribine, Clozapine이 있습니다. 중등도(Moderate) 등급 예로는 Roflumilast, Chloramphenicol, Zidovudine, Azathioprine, Anakinra 등이 있습니다.

경고 및 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
내사시에 대한 임상시험과 문헌이 없고 VEGF 억제와의 기전적 연결도 불분명하여, 근거 수준은 L5(모델 예측만 존재)입니다. 현 단계에서 개발을 진행할 근거가 부족합니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기) 확보: 안전성 검토를 진행하기 위한 필수 선행 자료
- 상세 작용 기전(MOA) 데이터 확보
- 내사시와 VEGF 경로의 연관성을 보여주는 전임상 또는 기전 연구
- 종양(예: 외배엽간엽종, 신경내분비종양)이나 식도 정맥류 등 기전적으로 더 타당한 후보에 대한 우선순위 재검토 (단, 정맥류는 출혈 위험 평가 필요)
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

