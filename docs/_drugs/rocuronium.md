---
layout: default
title: Rocuronium
parent: 모델 예측만 (L5)
nav_order: 663
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
description: "Rocuronium: 예측 신규 적응증 편두통 (Migraine disorder) (근거 수준 L5). 기존 적응증: 마취 시 신경근 차단(허가 문서 링크만 제공되어 상세 적응증 문구는 확인되지 않음)"
monitor_inn: "Rocuronium"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "cauda equina syndrome", "atrophoderma vermiculata", "ulerythema ophryogenesis", "obsolete neurogenic bladder (disease)", "irritable bowel syndrome", "sciatic neuropathy", "headache disorder"]
---

# Rocuronium
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

## Rocuronium: 신경근 차단에서 편두통으로?
{: .text-alpha }

## 한 문장 요약

Rocuronium은 비탈분극성 신경근 차단제로, 마취 시 근이완을 위해 주사제로 사용되는 약물입니다. TxGNN 모델은 **편두통(migraine disorder)**에 효과가 있을 수 있다고 예측했지만, 이 예측을 직접 뒷받침하는 임상시험이나 문헌은 없습니다. 근거 수준은 **L5(모델 예측만 있음)**이며, 기전상 연관성도 확인되지 않았습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 마취 시 신경근 차단(허가 문서 링크만 제공되어 상세 적응증 문구는 확인되지 않음) |
| 예측 신규 적응증 | 편두통 (Migraine disorder) |
| TxGNN 예측 점수 | 0.9990 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 11건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

Rocuronium은 신경근접합부의 니코틴성 아세틸콜린 수용체를 경쟁적으로 차단하는 비탈분극성 신경근 차단제입니다. 현재 상세한 작용 기전 데이터는 별도로 수집되지 않았으며, 위 내용은 일반적으로 알려진 약리 정보입니다.

편두통의 병태생리는 CGRP, 삼차신경혈관 활성화, 피질 확산성 억제와 관련이 있고, rocuronium의 작용 기전과는 직접적인 연결고리가 없습니다. 이론적으로는 두개주위 근육 긴장을 줄일 가능성을 생각해 볼 수 있으나, 이는 추측일 뿐 데이터로 뒷받침되지 않습니다. 또한 치료 용량에서 혈액뇌장벽을 의미 있게 통과하지 못하므로 중추신경계 작용도 기대하기 어렵습니다.

따라서 0.9990에 가까운 높은 점수는 TxGNN 모델(딥러닝)이 관련 질환 사이에서 학습한 유사성을 반영한 것일 수 있으며, 생물학적 근거는 아닙니다. 같은 편두통 계열의 다른 예측(뇌간 조짐 편두통 등)과 두통 질환도 같은 맥락으로 해석됩니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01431326](https://clinicaltrials.gov/study/NCT01431326) | N/A | 완료 | 3,520 | 소아에서 표준 치료로 투여된 연구 미진 약물의 약동학 조사. 편두통 효능을 평가하는 설계가 아니며 관련성 낮음(C등급) |

## 문헌 근거

편두통에 대한 직접 문헌은 없습니다. 아래는 상위 예측 중 하나인 두통 질환(headache disorder)에서 확인된 간접 문헌입니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [23812022](https://pubmed.ncbi.nlm.nih.gov/23812022/) | 2014 | 임상 연구(마취/ECT) | The journal of ECT | 전기경련요법 후 근육통·두통에 대해 succinylcholine과 rocuronium-sugammadex를 비교. 두통 치료제로서의 평가가 아님 |
| [24196089](https://pubmed.ncbi.nlm.nih.gov/24196089/) | 2013 | Case report | Pediatric emergency care | 두개내압 상승 소아의 신속 순차 삽관 사례. 두통 치료와 무관 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201108958 | 로큐니움주사 | 주사제(바이알) | 허가 문서 참조 |
| 202300447 | 로큐바주 | 주사제(바이알) | 허가 문서 참조 |
| 201205961 | 로카론주 | 주사제(바이알) | 허가 문서 참조 |
| 201102622 | 로큐론주 | 주사제(바이알) | 허가 문서 참조 |
| 202008328 | 로니움주사 | 주사제(바이알) | 허가 문서 참조 |

## 안전성 고려사항

- **약물 상호작용**: 총 73건이 확인되었습니다. 주요 항목은 다음과 같습니다.
  - **Major**: Paromomycin, Kanamycin, Neomycin (아미노글리코시드계 항생제, 신경근 차단 증강 가능)
  - **Moderate**: Doxycycline, Tetracycline, Minocycline, Vancomycin, Amphotericin B, Magnesium sulfate, Magnesium chloride, Mannitol, Metoclopramide, 코르티코스테로이드(Hydrocortisone, Dexamethasone, Betamethasone, Triamcinolone, Prednisone) 등
  - **Minor**: Ranitidine

경고 및 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
편두통 예측은 TxGNN 모델(딥러닝)의 점수만 있을 뿐 직접적인 임상시험이나 문헌이 없고, 기전상 연결고리도 없습니다. 이 점수는 모델이 관련 질환 사이에서 학습한 유사성을 반영한 것일 수 있으며, 생물학적 근거는 아닙니다. 전신 신경근 차단은 호흡 마비 위험이 있어 만성 질환 치료로 적합하지 않습니다.

**진행하려면 필요한 것:**
- 편두통에 대한 기전적 근거 또는 전임상 데이터
- 편두통 환자를 대상으로 한 직접적인 임상 근거
- 허가사항의 경고·금기 정보 확인
- 상세 작용 기전 데이터 보완
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

