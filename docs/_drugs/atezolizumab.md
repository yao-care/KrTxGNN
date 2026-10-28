---
layout: default
title: Atezolizumab
parent: 모델 예측만 (L5)
nav_order: 95
evidence_level: L5
indication_count: 6
monitor_inn: "Atezolizumab"
predicted_indications: ["uterine ligament adenocarcinoma", "endocervical carcinoma", "adenoid cystic carcinoma of the cervix uteri", "uterine ligament serous adenocarcinoma", "signet ring cell variant cervical mucinous adenocarcinoma", "intestinal variant cervical mucinous adenocarcinoma"]
last_modified_at: 2026-10-23
description: "Atezolizumab: 예측 신규 적응증 자궁인대 선암 (근거 수준 L5). 기존 적응증: 허가 적응증 본문이 링크로만 제공되어 구체적 내용을 확인할 수 없음"
---

# Atezolizumab
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **6** 건
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

## Atezolizumab: 항종양 면역치료제에서 자궁인대 선암(Uterine Ligament Adenocarcinoma)으로
{: .text-alpha }

## 한 문장 요약

Atezolizumab은 PD-L1을 표적으로 하는 항체 의약품으로, 한국에는 티쎈트릭주라는 제품으로 허가되어 있습니다. TxGNN 모델은 **자궁인대 선암(uterine ligament adenocarcinoma)**에 효과가 있을 수 있다고 예측하며 점수는 매우 높습니다(0.9993). 그러나 이 질환을 직접 다룬 **임상시험은 0건, 문헌도 0건**이어서 현재는 모델 예측 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문이 링크로만 제공되어 구체적 내용을 확인할 수 없음 |
| 예측 신규 적응증 | 자궁인대 선암 |
| TxGNN 예측 점수 | 0.9993 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Atezolizumab은 PD-L1을 차단하는 항체입니다. PD-1/PD-L1 경로에 의한 T세포 억제를 풀어 항종양 면역 반응을 되살리는 방식으로 작용할 수 있습니다.

자궁인대 선암에 이 기전이 적용될 가능성은 있습니다. 부인과 선암에서 PD-L1 차단이 항종양 T세포 활성을 회복시킬 수 있다는 가설이 근거입니다. 다만 이 질환은 희귀한 부위 특이적 질환이어서, 다른 부인과 암에서 얻은 결과를 적용하는 것은 추정에 불과하며 검증되지 않았습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201700266 | 티쎈트릭주(아테졸리주맙) | 바이알 주사제 (무색 내지 연한 노랑 액체) | 본문 없이 [허가 문서 링크](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201700266/EE)만 제공됨 |

제조사는 (주)한국로슈이며 단일 성분 제품입니다. 허가 상태는 유효로 기록되어 있습니다.

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 면역치료(PD-L1 억제 항체). 기존 세포독성 화학요법 약물이 아님 |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 취급 방호 | 허가사항의 경고 및 주의사항을 참조하세요 |

## 안전성 고려사항

허가사항의 경고 및 금기 정보는 이번에 수집된 자료에 없으므로 허가사항을 참조하세요.

**약물 상호작용**: 총 75건이 확인되었으며, 주요 항목은 다음과 같습니다.
- **Major(주요)**: Adalimumab, Baricitinib, BCG 생균 백신(Tice 균주)
- **Moderate(중등도)**:
  - 코르티코스테로이드(Hydrocortisone, Prednisone, Dexamethasone, Methylprednisolone 등)
  - Roflumilast
  - Azathioprine
  - Alemtuzumab
  - Anakinra
  - 일부 백신(파상풍 톡소이드, 탄저 백신 등)

면역억제제나 백신과 병용할 때는 별도 검토가 필요합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
자궁인대 선암을 직접 다룬 임상시험과 문헌이 없어 근거가 모델 예측(L5)에 그칩니다. 안전성 및 허가 적응증 정보도 확보되지 않았습니다.

**진행하려면 필요한 것:**
- 허가 문서(PDF)에서 적응증, 경고, 금기 정보 확보
- DrugBank 등에서 작용 기전(MOA) 데이터 보완
- 자궁인대 선암에 대한 임상시험 및 문헌 추가 검색
- 인접 질환 자료의 참고. 같은 데이터에서 자궁경부 관련 예측(endocervical carcinoma)에는 Atezolizumab 임상시험 2건(Phase 2 병용 시험 1건, Phase 1 시험 1건)이 있습니다. 이는 이 질환의 직접 근거가 아니라 연구 가설을 세울 때의 참고 자료입니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

