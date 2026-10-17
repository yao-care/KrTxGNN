---
layout: default
title: Cemiplimab
parent: 모델 예측만 (L5)
nav_order: 200
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Cemiplimab: 예측 신규 적응증 담낭 선편평상피암 (gallbladder adenosquamous carcinoma) (근거 수준 L5). 기존 적응증: 허가증에 적응증 원문 대신 허가사항 문서 링크만 제공되어 있어 본문을 확인할 수 없습니다. 참고로 약리학 자료에는 피부 편평…"
monitor_inn: "Cemiplimab"
predicted_indications: ["gallbladder adenosquamous carcinoma", "rectal cloacogenic carcinoma", "external ear basal cell carcinoma", "adenosquamous prostate carcinoma", "urethral verrucous carcinoma", "pancreatic adenosquamous carcinoma"]
---

# Cemiplimab
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

# Cemiplimab: 허가 적응증에서 담낭 선편평상피암으로

## 한 문장 요약

Cemiplimab은 항 PD-1 항체로, 한국에서는 리브타요주로 허가되어 시판 중입니다. TxGNN 모델은 **담낭 선편평상피암(gallbladder adenosquamous carcinoma)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 직접 뒷받침하는 **임상시험은 0건**, **문헌도 0편**입니다. 따라서 모델 예측만 있는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가증에 적응증 원문 대신 허가사항 문서 링크만 제공되어 있어 본문을 확인할 수 없습니다. 참고로 약리학 자료에는 피부 편평세포암(CSCC)과 비소세포폐암이 기재되어 있습니다. |
| 예측 신규 적응증 | 담낭 선편평상피암 (gallbladder adenosquamous carcinoma) |
| TxGNN 예측 점수 | 99.99% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 확보되지 않았습니다. 다만 약리학 자료에 따르면 cemiplimab은 사람 PD-1(PDCD1, CD279)에 결합하는 항체로, PD-1/PD-L1 상호작용을 차단합니다(ELISA에서 IC50 1 nM 미만). 이 차단으로 종양에 대한 T세포 면역 반응이 회복될 수 있습니다.

담낭 선편평상피암은 편평세포 성분을 포함하는 종양입니다. 이 편평세포 성분이 PD-L1을 발현할 가능성이 있어, 피부 편평세포암에서 입증된 효능과 연결 지을 수 있습니다. 그러나 이는 TxGNN 지식 그래프 예측에서 추론한 가설일 뿐, 이 적응증에서 PD-L1 발현이나 반응을 확인한 자료는 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202203904 | 리브타요주(세미플리맙) | 주사제 (무색투명한 유리 바이알에 든 무색~연한 노란색 용액) | 허가사항 문서(식약처)를 참조하세요 |

## 안전성 고려사항

- **약물 상호작용**: 코르티코스테로이드 9종과 중등도(Moderate) 상호작용이 보고되어 있습니다. 면역 관문 억제제의 효과를 코르티코스테로이드가 약화시킬 수 있다는 점에 유의해야 합니다.
  - Hydrocortisone
  - Triamcinolone
  - Dexamethasone
  - Betamethasone
  - Budesonide
  - Prednisolone
  - Prednisone
  - Methylprednisolone
  - Deflazacort

주요 경고와 금기 정보는 이번 보고서에 수집된 데이터에 없으므로 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
담낭 선편평상피암에 대한 임상시험과 문헌이 없고 TxGNN 예측만 있어 근거 수준이 L5입니다. 허가사항의 경고·금기와 작용 기전 데이터도 확보되지 않아, 현 단계에서는 진행을 보류하는 것이 적절합니다.

**진행하려면 필요한 것:**
- 식약처 허가사항(경고·금기 포함)을 내려받아 확인
- DrugBank 등에서 작용 기전(MOA) 데이터 보완
- 담낭 선편평상피암에서의 PD-L1 발현 및 항 PD-1 치료 반응에 관한 문헌과 임상시험 검색
- 후순위 예측 중 근거가 상대적으로 있는 적응증 검토. 예컨대 외이 기저세포암은 증례 보고 1건(PMID 34157152, 2021)이 있어 L4로 평가되었으나, 이 또한 간접 근거이며 허가 상태와 핵심 시험 자료를 원문으로 확인해야 합니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

