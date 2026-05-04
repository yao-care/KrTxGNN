---
layout: default
title: Desoximetasone
parent: 僅模型預測 (L5)
nav_order: 208
evidence_level: L5
indication_count: 10
---

# Desoximetasone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Desoximetasone: 염증성 피부질환에서 원형 탈모증으로

## 한 문장 요약

Desoximetasone은 중등도~강효 외용 코르티코스테로이드로, 원래 습진·건선 등 염증성 피부질환 치료에 사용되는 약물입니다.
TxGNN 모델은 **원형 탈모증(Alopecia Areata)**에 효과가 있을 수 있다고 예측하며,
현재 **0건의 임상시험**과 **1편의 문헌**(무작위 이중맹검 위약대조시험)이 이 방향을 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 염증성 피부질환 (한국 미허가) |
| 예측 신규 적응증 | 원형 탈모증 (Alopecia Areata) |
| TxGNN 예측 점수 | 99.92% |
| 근거 수준 | L2 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면, Desoximetasone은 외용 글루코코르티코이드 계열 약물로, 피부 국소 염증 반응 억제에 대한 효능이 입증되어 있어 기전상 원형 탈모증에도 적용 가능합니다.

원형 탈모증(AA)은 CD8+ T 세포가 모낭의 면역 특권 구역(hair follicle immune privilege)을 공격하는 자가면역 질환입니다. 외용 강효 코르티코스테로이드는 국소 Th1/Th2 염증 반응을 억제하고, IL-2 및 인터페론-γ를 감소시켜 모낭의 면역 특권을 회복시키는 것으로 알려져 있습니다.

동일 계열 약물인 clobetasol, betamethasone은 이미 AA의 1차 치료 표준으로 사용되고 있으며, Desoximetasone 0.25%에 대해서도 직접적인 RCT 근거가 존재합니다(PMID 11030789). 이러한 계열 일관성과 직접 임상 증거가 TxGNN 모델 예측의 기전적 타당성을 뒷받침합니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|------|------|------|---------|
| [11030789](https://pubmed.ncbi.nlm.nih.gov/11030789/) | 2000 | RCT | Archives of Dermatology | Desoximetasone 0.25% 크림을 이용한 원형 탈모증 치료의 무작위 이중맹검 위약대조시험 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
Desoximetasone 0.25%의 원형 탈모증 치료 효과를 직접 평가한 RCT 문헌이 존재하며, 동일 계열 외용 코르티코스테로이드의 AA 1차 치료 적용이 이미 확립되어 있어 기전적·임상적 근거가 충분합니다. 다만 한국 미허가 약물이므로 추가 규제 절차 및 안전성 데이터 보완이 선행되어야 합니다.

**진행하려면 필요한 것:**
- 상세한 작용 기전 데이터(MOA) 확보 — DrugBank API 조회 (DG002 해소)
- TFDA/MFDS 허가사항 확인 — 경고·금기·이상반응 목록 (DG001 해소)
- 한국 내 허가 경로 검토 (동일 계열 허가 약물 대비 비교 데이터 포함)
- 외용 코르티코스테로이드 장기 사용에 따른 피부 위축·모세혈관 확장 등 이상반응 모니터링 계획 수립
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

