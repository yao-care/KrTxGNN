---
layout: default
title: Vecuronium
parent: 모델 예측만 (L5)
nav_order: 781
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Vecuronium: 예측 신규 적응증 불면증 (Insomnia) (근거 수준 L5). 기존 적응증: 마취 시 근이완 (신경근 차단제)"
monitor_inn: "Vecuronium"
predicted_indications: ["insomnia (disease)", "irritable bowel syndrome", "neurocirculatory asthenia", "benign prostatic hyperplasia (disease)", "cauda equina syndrome", "headache disorder", "rhinitis", "anxiety", "trigeminal autonomic cephalalgia", "migraine disorder"]
---

# Vecuronium
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

# Vecuronium: 근이완(신경근 차단)에서 불면증으로

## 한 문장 요약

Vecuronium은 비탈분극성 신경근 차단제로, 전신마취 시 기관 삽관과 수술 중 근이완을 위해 사용되는 약입니다.
TxGNN 모델은 **불면증(Insomnia)**에 효과가 있을 수 있다고 예측하지만, 직접 뒷받침하는 근거는 **임상시험 1건(약동학 일반 연구)**뿐이며 문헌은 없습니다. 이 예측은 네트워크상의 연관성에서 나온 결과로 보이며 실질적인 근거는 매우 약합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 마취 시 근이완 (신경근 차단제) |
| 예측 신규 적응증 | 불면증 (Insomnia) |
| TxGNN 예측 점수 | 99.34% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 5건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 확보되지 않았습니다. 일반적으로 알려진 정보에 따르면 Vecuronium은 신경근 접합부의 니코틴성 아세틸콜린 수용체에 작용하는 비탈분극성 신경근 차단제입니다. 진정이나 수면 유도 작용이 없고, 수면 조절과 관련된 중추 기전도 알려져 있지 않습니다.

따라서 기존 적응증(근이완)과 불면증 사이에는 기전상 뚜렷한 연관성이 없습니다. 높은 예측 점수는 마취 관련 약물들과 함께 등장하는 네트워크상의 동시 출현 패턴에서 비롯된 것으로 해석됩니다. 오히려 진정 없이 근이완제만 투여하면 마비 상태에서 의식이 있는 상황(마취 중 각성)이 생길 수 있어 환자에게 해로울 수 있습니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01431326](https://clinicaltrials.gov/study/NCT01431326) | N/A | 완료 | 3,520 | 표준 치료로 투여된 소아 대상 연구 부족 약물의 약동학 연구. 불면증에 대한 Vecuronium의 효능 평가는 없음 (관련성 낮음) |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 198900195 | 베카론주(베쿠로늄브롬화물) | 바이알 (흰색 분말) | 허가사항 문서 참조 |
| 201403443 | 베크론주사4밀리그램(수출용) | 바이알 (결정성 가루) | 허가사항 문서 참조 |
| 199100162 | 베카론주10밀리그램 | 동결건조 분말 바이알 주사제 | 허가사항 문서 참조 |
| 201206851 | 베로늄주10mg(수출용) | 바이알 (용시 용해 주사제) | 허가사항 문서 참조 |
| 201403444 | 베크론주사10밀리그램(수출용) | 바이알 (결정성 가루) | 허가사항 문서 참조 |

## 안전성 고려사항

- **약물 상호작용**: 총 85건이 확인되었습니다. 주요 항목은 다음과 같습니다.
  - **Major**: Paromomycin, Kanamycin, Neomycin (아미노글리코사이드계, 신경근 차단 증강 가능)
  - **Moderate**: Magnesium sulfate, Magnesium chloride, Vancomycin, Doxycycline, Tetracycline, Minocycline, Amphotericin B, Hydrocortisone, Dexamethasone, Prednisone, Metoclopramide, Mannitol 등
  - **Minor**: Ranitidine

경고 및 금기 사항은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
불면증 예측은 모델 점수만 있을 뿐 효능을 뒷받침하는 임상시험이나 문헌이 없습니다. 약물의 기전상 진정·수면 작용이 없고 오히려 위험할 수 있어, 현 단계에서 재창출을 진행할 근거가 없습니다.

**진행하려면 필요한 것:**
- 불면증과 연결되는 기전적 가설 및 전임상 근거
- 상세한 약물 작용 기전(MOA) 데이터
- 허가사항(경고·금기)의 확인 및 안전성 검토
- 상위 예측(과민성 대장 증후군, 신경순환 무력증 등)과 마찬가지로 임상·문헌 근거가 없으므로, 필요하다면 다른 예측 적응증을 포함해 재평가
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

