---
layout: default
title: Varenicline
parent: 모델 예측만 (L5)
nav_order: 779
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Varenicline: 예측 신규 적응증 편두통 (Migraine Disorder) (근거 수준 L5). 기존 적응증: 허가 적응증 텍스트 없음 (허가증에는 PDF 링크만 제공됨)"
monitor_inn: "varenicline"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "congenital hypotrichosis milia", "hypotrichosis simplex of the scalp", "diffuse alopecia areata", "alopecia", "open-angle glaucoma", "primary hereditary glaucoma", "headache disorder", "pulmonary hypertension"]
---

# Varenicline
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

# Varenicline: 금연 치료제에서 편두통으로 (예측 단계)

## 한 문장 요약

Varenicline은 니코틴 수용체에 작용하는 약물로, 한국에서 금연 보조 치료에 사용되는 것으로 알려져 있습니다(허가 적응증 원문은 이번 데이터에 텍스트로 포함되어 있지 않습니다).
TxGNN 모델은 **편두통(migraine disorder)**에 효과가 있을 수 있다고 예측하지만, 이를 직접 지지하는 **임상시험은 0건**이며 관련 문헌 1건도 심정지 증례 보고로 효능 근거가 아닌 안전성 신호입니다.
따라서 현재는 모델 예측만 있는 단계(L5)입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 텍스트 없음 (허가증에는 PDF 링크만 제공됨) |
| 예측 신규 적응증 | 편두통 (Migraine Disorder) |
| TxGNN 예측 점수 | 99.92% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 2건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 이번 자료에는 없습니다. 다만 일반적으로 varenicline은 α4β2 니코틴성 아세틸콜린 수용체의 부분 작용제이며 α7 수용체에서는 완전 작용제로 알려져 있습니다. 니코틴성 콜린 신호가 삼차신경혈관 경로와 중추 통증 처리에 영향을 줄 가능성은 이론적으로 가능합니다.

그러나 varenicline이 편두통에 효과가 있다는 직접 근거는 없습니다. 오히려 두통은 varenicline의 흔한 이상반응으로 보고되어 있어 이득 가능성에 불리한 정보입니다. 높은 TxGNN 점수는 지식 그래프상의 연관성에 기반한 계산상 예측일 뿐입니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [19585710](https://pubmed.ncbi.nlm.nih.gov/19585710/) | 2009 | 증례 보고 | Therapie | Varenicline 투여 중 심정지 증례. 효능 근거가 아닌 안전성 신호 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202301090 | 노코틴정0.5밀리그램(바레니클린옥살산염수화물) | 흰색의 장방형 필름코팅정 | 허가사항 PDF 참조 (한미약품) |
| 202301089 | 노코틴정1밀리그램(바레니클린옥살산염수화물) | 연한 파란색의 장방형 필름코팅정 | 허가사항 PDF 참조 (한미약품) |

## 안전성 고려사항

- **지식 그래프상 금기 관련 질환** (허가사항이 아닌 TxGNN 지식 그래프 기반): 불안장애, 신경증, 기분부전장애, 양극성장애, 주요 정동장애, 물질 남용/의존, 급성 관상동맥증후군, 말초혈관질환, 간헐적 파행, 말초동맥질환, 조현병
- **약물 상호작용**: 총 104건이 확인되었습니다. 이 중 Cimetidine은 경미(Minor) 수준이며, 그 외 Phentermine, Metformin, Glimepiride, Morphine, Omeprazole, Simvastatin, Prednisone, Epinephrine 등 다수는 등급이 미분류(Unknown)입니다.
- 편두통 예측과 관련하여, 두통이 varenicline의 흔한 이상반응으로 보고되어 있고 심정지 증례 보고도 있어 주의가 필요합니다.

허가사항의 경고 및 금기는 허가사항을 직접 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
편두통에 대한 임상시험과 효능 문헌이 없고, 두통이 오히려 이상반응으로 알려져 있어 예측을 뒷받침하지 못합니다. 높은 TxGNN 점수만으로는 진행하기 어렵습니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기) 원문 확보 및 분석
- 작용 기전(MOA) 데이터 보완
- 편두통에서의 전임상 또는 기전 연구 근거
- 두통 이상반응 위험과 이득의 비교 평가
- 정신과 질환 및 심혈관 질환 환자에 대한 안전성 검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

