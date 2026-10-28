---
layout: default
title: Bevacizumab
parent: 모델 예측만 (L5)
nav_order: 144
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Bevacizumab: 예측 신규 적응증 후두개 종양 (Epiglottis Neoplasm) (근거 수준 L5). 기존 적응증: 허가증에 적응증 원문이 아닌 링크만 제공되어 본문은 확인하지 못했습니다. 허가 원문 확인이 필요합니다"
monitor_inn: "Bevacizumab"
predicted_indications: ["epiglottis neoplasm", "benign neoplasm of tongue", "tumor of testis and paratestis", "benign neoplasm of hypopharynx", "benign neoplasm of floor of mouth", "cervical neuroblastoma", "cystic neoplasm", "nasal cavity inverting papilloma", "mesenchymoma", "schwannoma of jugular foramen"]
---

# Bevacizumab
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

## Bevacizumab: 기존 항암 적응증에서 후두개 종양(Epiglottis Neoplasm)으로
{: .text-alpha }

## 한 문장 요약

Bevacizumab은 VEGF-A를 억제하는 단클론항체로, 한국에서 항암 치료제로 허가·시판되고 있습니다.
TxGNN 모델은 **후두개 종양(Epiglottis Neoplasm)**에 효과가 있을 수 있다고 예측하지만, 이번에 수집된 데이터에는 이 적응증을 직접 지지하는 **임상시험이 0건, 문헌도 0건**입니다. 현재는 모델 예측만 있는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가증에 적응증 원문이 아닌 링크만 제공되어 본문은 확인하지 못했습니다. 허가 원문 확인이 필요합니다. |
| 예측 신규 적응증 | 후두개 종양 (Epiglottis Neoplasm) |
| TxGNN 예측 점수 | 0.9990 (전체 순위 2,682위) |
| 근거 수준 | L5 (모델 예측만 있음) |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 4건 (모두 유효, 단일제) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 수집되지 않았습니다. 다만 Bevacizumab은 VEGF-A를 억제하는 항체로 알려져 있습니다. 혈관신생에 의존하는 종양에서는 이 기전이 작용할 가능성이 있습니다.

후두개 종양은 두경부 종양에 속합니다. 두경부 종양은 혈관신생 의존성이 있다고 알려져 있어, 기전상 적용 가능성은 있습니다. 그러나 이번 데이터에는 후두개 종양에 대한 임상시험이나 문헌이 없습니다. 높은 예측 점수는 모델 예측일 뿐, 실제 효과를 입증하는 것은 아닙니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

허가증에는 적응증 원문이 아닌 PDF 링크만 있어, 아래 표의 적응증 항목은 원문 링크로 대체했습니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202203696 | 베그젤마주 (셀트리온) | 주사제 (바이알) | [허가증 원문 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202203696/EE) |
| 202200294 | 아림시스주 (알보젠코리아) | 주사제 (바이알) | [허가증 원문 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202200294/EE) |
| 202102237 | 온베브지주 (삼성바이오에피스) | 주사제 (바이알) | [허가증 원문 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202102237/EE) |
| 200710438 | 아바스틴주 (한국로슈) | 주사제 (바이알) | [허가증 원문 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200710438/EE) |

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적치료제 (항 VEGF 단클론항체). 기존 세포독성 화학요법제와는 다릅니다. |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요. |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요. |
| 모니터링 항목 | 허가사항의 경고 및 주의사항을 참조하세요. |
| 취급 방호 | 허가사항의 경고 및 주의사항을 참조하세요. |

## 안전성 고려사항

**약물 상호작용**: 총 22건이 확인되었고, 이 중 상세 내역이 있는 20건은 다음과 같습니다.
- **Major (5건)**: Deferiprone, Samarium (153Sm) lexidronam, Panitumumab, Sunitinib, Thalidomide
- **Moderate (15건)**: Palifermin, Strontium chloride Sr-89, 비스포스포네이트 계열(Alendronic acid, Risedronic acid, Etidronic acid, Ibandronate, Pamidronic acid, Tiludronic acid), Filgrastim, Pegfilgrastim, Sargramostim, Idelalisib, Radium Ra 223 dichloride, Romosozumab, Sodium phosphate monobasic (P32)

주요 경고와 금기는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
후두개 종양에 대한 임상시험과 문헌이 모두 없어 근거가 모델 예측뿐(L5)입니다. 기전상 가능성은 있지만 이를 뒷받침할 데이터가 없어 지금은 진행을 보류합니다.

**진행하려면 필요한 것:**
- 후두개 종양 또는 후두·두경부 종양에서 Bevacizumab의 효능을 다룬 임상시험과 문헌 확보
- 허가증 원문에서 기존 적응증, 경고, 금기 확인
- 상세한 작용 기전 데이터 확보
- 참고: 같은 예측 목록의 "낭성 종양(cystic neoplasm)"은 난소 종양 관련 Phase 3 시험과 체계적 문헌고찰이 있어 근거가 더 풍부합니다(L3). 다만 이 적응증도 질환 범주 매핑이 불명확하므로 별도 검토가 필요합니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

