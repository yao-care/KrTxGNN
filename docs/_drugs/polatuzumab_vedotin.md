---
layout: default
title: Polatuzumab Vedotin
parent: 모델 예측만 (L5)
nav_order: 609
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Polatuzumab Vedotin: 예측 신규 적응증 HER2 양성 유방암 (HER2 positive breast carcinoma) (근거 수준 L5). 기존 적응증: 확인 불가 (허가 정보에 적응증 본문 대신 문서 링크만 수록됨)"
monitor_inn: "POLATUZUMAB VEDOTIN"
predicted_indications: ["HER2 positive breast carcinoma"]
---

# Polatuzumab Vedotin
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **1** 건
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

## Polatuzumab Vedotin: 기존 적응증에서 HER2 양성 유방암으로
{: .text-alpha }

## 한 문장 요약

Polatuzumab vedotin은 CD79b를 표적으로 하는 항체-약물 접합체(ADC)로, 한국에서 허가를 받아 시판 중입니다. 다만 이번 데이터에서는 허가 적응증의 구체적인 텍스트를 확인할 수 없었습니다.
TxGNN 모델은 **HER2 양성 유방암(HER2 positive breast carcinoma)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 지지하는 **임상시험은 0건**, **문헌도 0편**입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (허가 정보에 적응증 본문 대신 문서 링크만 수록됨) |
| 예측 신규 적응증 | HER2 양성 유방암 (HER2 positive breast carcinoma) |
| TxGNN 예측 점수 | 99.34% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 수록되어 있지 않습니다. 알려진 정보에 따르면 polatuzumab vedotin은 B세포 수용체 구성 요소인 CD79b를 표적으로 하고, 미세소관을 파괴하는 MMAE를 탑재한 ADC입니다. 이 정보는 일반적으로 알려진 약리 지식에 근거하며, 이번 데이터에서 확인된 값은 아닙니다.

HER2 양성 유방암에서 CD79b는 알려진 표적이 아닙니다. MMAE는 분열 중인 세포에 세포독성을 보이며 다른 ADC에도 쓰이지만, 이것만으로는 HER2 양성 유방암에 대한 종양 특이적 근거가 되지 않습니다. 0.993이라는 높은 점수는 계산상 예측일 뿐이며, MMAE라는 페이로드 계열이나 다른 유방암 ADC와의 네트워크 수준 연관성에서 비롯되었을 가능성이 큽니다. 검증된 기전에 근거한 것은 아닙니다.

또한 HER2 양성 유방암에는 trastuzumab, pertuzumab, T-DM1, trastuzumab deruxtecan 등 효과가 확립된 HER2 표적 치료제가 이미 있어, 이 약이 채울 뚜렷한 미충족 수요도 확인되지 않습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202007363 | 폴라이비주(폴라투주맙베도틴) | 주사제 (동결건조물 바이알, 조제액은 무색~미갈색의 투명한 액상) | 허가 적응증 본문은 수록되지 않았으며 허가사항 문서 참조 필요 |

제조사는 (주)한국로슈입니다.

## 안전성 고려사항

**약물 상호작용** (총 100건 조회, 일부 표시)
- **Major 등급**: Clarithromycin, Cobicistat, Deferiprone, Samarium (153Sm) lexidronam
- **Moderate 등급**: Aprepitant, Cimetidine, Naltrexone, Metronidazole, Miconazole, Rosuvastatin, Simvastatin, Tinidazole, Clotrimazole, Ticagrelor, Chloroquine, Disulfiram 등

주요 경고와 금기는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측을 뒷받침하는 임상시험과 문헌이 없고 근거 수준이 L5(모델 예측만 존재)입니다. CD79b는 HER2 양성 유방암의 알려진 표적이 아니며, 이미 효과적인 HER2 표적 치료제가 다수 있어 진행할 근거가 부족합니다.

**진행하려면 필요한 것:**
- 허가사항(경고, 금기, 적응증)의 확인 및 분석
- 작용 기전(MOA) 데이터 보완
- HER2 양성 유방암에서 CD79b 발현 여부 등 기전적 연관성을 입증하는 전임상 근거
- 관련 임상시험 또는 문헌 근거 확보
- 기존 HER2 표적 치료제 대비 이 약이 가질 이점에 대한 평가
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

