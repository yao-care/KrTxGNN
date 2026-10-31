---
layout: default
title: Famciclovir
parent: 모델 예측만 (L5)
nav_order: 337
evidence_level: L5
indication_count: 9
monitor_inn: "FAMCICLOVIR"
predicted_indications: ["post-infectious neuralgia", "sequela of COVID-19", "hepatitis C induced liver cirrhosis", "malignant pleural mesothelioma", "AIDS-related disorder", "malignant epithelioid mesothelioma", "chickenpox", "sarcomatoid mesothelioma", "malignant visceral pleura tumor"]
last_modified_at: 2026-10-31
description: "Famciclovir: 예측 신규 적응증 사후 감염성 신경통 (post-infectious neuralgia) (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201306322/EE"
---

# Famciclovir
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

## Famciclovir: 항바이러스제(펜시클로버 전구약물) → 사후 감염성 신경통 (post-infectious neuralgia)
{: .text-alpha }

## 한 문장 요약

Famciclovir는 체내에서 펜시클로버(penciclovir)로 전환되어 헤르페스 바이러스의 DNA 중합효소를 억제하는 항바이러스제입니다.
TxGNN 모델은 **사후 감염성 신경통(post-infectious neuralgia)**에 효과가 있을 수 있다고 예측하지만, 현재 이 질환을 직접 다룬 근거는 famciclovir를 시험하지 않은 **임상시험 1건**뿐이며 문헌은 없습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201306322/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201403232/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202200268/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200600500/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200500714/EE;  |
| 예측 신규 적응증 | 사후 감염성 신경통 (post-infectious neuralgia) |
| TxGNN 예측 점수 | 0.9975 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 20건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 수집되지 않았습니다. 알려진 정보에 따르면 famciclovir는 펜시클로버의 전구약물로, 수두대상포진바이러스(VZV)의 DNA 중합효소를 억제합니다.

이 기전은 급성 대상포진의 중증도를 줄일 수 있고, 그 결과 대상포진 후 신경통의 위험이나 지속 기간을 간접적으로 낮출 가능성이 있습니다. 다만 이는 기전에 근거한 추정일 뿐, famciclovir 자체가 이 질환에서 효과를 보였다는 직접 근거는 아닙니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT03120962](https://clinicaltrials.gov/study/NCT03120962) | 해당 없음 | 불명 | 140 | 대상포진 급성기에 옥시코돈을 조기 사용해 대상포진 후 신경통을 예방하는 연구. famciclovir는 시험 약물이 아니며 참고용 |

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201306322 | 팜시정250밀리그램 | 흰색의 원형 필름코팅정 | 허가 적응증 텍스트 미기재 |
| 201403232 | 팜시날정 | 흰색의 원형 필름코팅정 | 허가 적응증 텍스트 미기재 |
| 202200268 | 팜시론정750밀리그램 | 흰색의 장방형 필름코팅 정제 | 허가 적응증 텍스트 미기재 |
| 200600500 | 팜시르정250밀리그램 | 흰색 원형의 필름코팅정 | 허가 적응증 텍스트 미기재 |
| 200500714 | 클로비어정 | 흰색원형의 필름코팅정제 | 허가 적응증 텍스트 미기재 |

위 표는 전체 20건 중 5건만 나열한 것이며, 허가 기록은 일부만 포함되었을 수 있습니다.

## 안전성 고려사항

- **약물 상호작용**: 이번 보고서용으로 수집된 데이터에서 84건이 확인되었습니다. 예로 calcitriol, doxycycline, clotrimazole, pantoprazole, glimepiride, morphine, metformin, omeprazole 등이 있으며, 개별 위험 등급은 구분되어 있지 않습니다(등급 미상).

경고 및 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 이 질환을 직접 다룬 근거는 famciclovir를 평가하지 않은 임상시험 1건뿐이고 문헌이 없어, 현재는 모델 예측 수준(L5)에 머뭅니다.

**진행하려면 필요한 것:**
- famciclovir를 대상포진 후 신경통 예방·치료 목적으로 평가한 임상시험 또는 문헌
- 허가사항(경고·금기·적응증)의 확보 및 검토
- 작용 기전(MOA) 데이터 보완
- 병용 약물과의 상호작용 위험 등급 확인
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

