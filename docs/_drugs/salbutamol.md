---
layout: default
title: Salbutamol
parent: 모델 예측만 (L5)
nav_order: 680
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Salbutamol: 예측 신규 적응증 유두성 결막염 (Papillary Conjunctivitis) (근거 수준 L5)."
monitor_inn: "Salbutamol"
predicted_indications: ["papillary conjunctivitis", "nasal cavity disease", "pharyngitis", "acute laryngopharyngitis", "anaphylaxis", "common cold", "atopic conjunctivitis", "anorectal stricture", "obstructive lung disease"]
---

# Salbutamol
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

# Salbutamol: 기관지 확장제에서 유두성 결막염(Papillary Conjunctivitis)으로

## 한 문장 요약

Salbutamol은 베타-2 작용제 계열의 약물로, 한국에서는 정제와 흡입제 형태로 시판되고 있습니다. TxGNN 모델은 **유두성 결막염(Papillary Conjunctivitis)**에 효과가 있을 수 있다고 예측하지만(예측 점수 99.996%), 이 예측을 뒷받침하는 **임상시험은 0건, 문헌도 0편**입니다. 따라서 현재는 모델 예측만 있는 초기 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 예측 신규 적응증 | 유두성 결막염 (Papillary Conjunctivitis) |
| TxGNN 예측 점수 | 99.996% |
| 근거 수준 | L5 (모델 예측만 있음) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 5건 (모두 유효, 단일제) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 이 보고서에 정리된 자료로는 Salbutamol이 베타-2 아드레날린 작용제라는 점만 확인됩니다. 이 약은 기관지 평활근을 이완시키는 기관지 확장제로 알려져 있으며, 한국에서는 흡입제와 정제로 허가되어 있습니다.

결막염에 적용할 수 있다는 근거는 이론적 추정 단계입니다. 베타-2 작용제가 결막의 비만세포에서 매개물질 방출을 줄일 가능성은 있습니다. 그러나 이 가설을 직접 검증한 임상시험이나 문헌은 이번에 수집된 자료에 없습니다.

한국에서 허가된 제형은 정제, 흡입액, 정량분무흡입제 등이며 안구용 제형은 없습니다. 따라서 실제로 개발하려면 새로운 점안 제형이 필요합니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 198900576 | 대우살부타몰정 (대우제약) | 정제 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/198900576/EE) |
| 200607690 | 살부톨흡입액 (대한약품공업) | 흡입액 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200607690/EE) |
| 200209634 | 벤토린흡입액 (글락소스미스클라인) | 흡입액 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200209634/EE) |
| 199906869 | 벤토린에보할러 (글락소스미스클라인) | 정량분무흡입제 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199906869/EE) |
| 199907319 | 벤토린네뷸2.5mg (글락소스미스클라인) | 흡입액(앰플) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199907319/EE) |

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 확인되었습니다. 주요 항목은 다음과 같습니다.
  - 중등도(Moderate): Acarbose, Isometheptene, Famotidine, Epinephrine, Albiglutide, Acetohexamide, Alogliptin, Bisacodyl, Canagliflozin, Castor oil, Chlorpropamide, Cisapride, Clarithromycin, Dapagliflozin, Diethylpropion
  - 경미(Minor): Hydrocortisone, Beclomethasone dipropionate, Betamethasone, Budesonide, Dexamethasone

  혈당강하제 병용 시 혈당 변동, 에피네프린 등 교감신경 작용제 병용 시 심혈관 영향에 유의해야 합니다.

경고, 금기 등 그 밖의 안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
유두성 결막염에 대해서는 TxGNN 예측 점수만 높을 뿐 임상시험과 문헌이 전혀 없고, 기전상의 근거도 가설 수준입니다. 또한 허가된 제형에 점안제가 없어 지금 단계에서 개발을 진행하기는 어렵습니다.

**진행하려면 필요한 것:**
- 결막염에서 베타-2 작용제의 효과를 다룬 전임상·임상 문헌 조사
- 허가사항(경고·금기·적응증 텍스트)과 작용 기전 데이터 확보
- 점안 등 안구용 제형의 필요성 및 실현 가능성 검토
- 약물 상호작용(100건)과 심혈관·저칼륨혈증 위험 검토

**참고:** 이번 자료에는 같은 약물에 대한 다른 예측 적응증도 포함되어 있습니다. 그중 폐쇄성 폐질환(Obstructive lung disease)은 근거 수준 L1(완료된 Phase 3 시험 NCT02177253, 1,118명)로 가장 강하지만, 기존 허가 범위와 사실상 겹쳐 엄밀한 의미의 재창출은 아닙니다. 아나필락시스는 Phase 3 시험이 24명 등록 후 조기 종료되어 근거 수준이 L3에 머뭅니다. 이들은 별도 평가가 필요합니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

