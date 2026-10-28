---
layout: default
title: Etoposide
parent: 모델 예측만 (L5)
nav_order: 329
evidence_level: L5
indication_count: 10
monitor_inn: "Etoposide"
predicted_indications: ["well-differentiated fetal adenocarcinoma of the lung", "primary pulmonary lymphoma", "pulmonary blastoma", "Ewing sarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina", "rhabdomyosarcoma (disease)", "embryonal extrahepatic bile duct rhabdomyosarcoma", "parameningeal embryonal rhabdomyosarcoma", "extrahepatic bile duct rhabdomyosarcoma", "prostate embryonal rhabdomyosarcoma"]
last_modified_at: 2026-10-28
description: "Etoposide: 예측 신규 적응증 폐의 고분화 태아형 선암 (근거 수준 L5). 기존 적응증: 허가 적응증 본문 확인 불가 (허가사항 링크만 제공됨)"
---

# Etoposide
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

## Etoposide: 항종양 화학요법제에서 폐의 고분화 태아형 선암으로
{: .text-alpha }

## 한 문장 요약

Etoposide는 한국에서 단일성분 주사제로 허가된 항종양 화학요법제입니다. 다만 이 보고서용으로 수집한 데이터에는 허가 적응증 본문이 없고 허가사항 링크만 있습니다.
TxGNN 모델은 **폐의 고분화 태아형 선암(well-differentiated fetal adenocarcinoma of the lung)**에 효과가 있을 수 있다고 예측합니다.
그러나 이 질환을 직접 다룬 임상시험은 **0건**이고, 연결된 문헌 **1편**은 다른 질환인 폐모세포종(pulmonary blastoma) 증례보고입니다. 근거는 모델 예측 수준에 머뭅니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문 확인 불가 (허가사항 링크만 제공됨) |
| 예측 신규 적응증 | 폐의 고분화 태아형 선암 |
| TxGNN 예측 점수 | 0.9994 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 6건 (모두 단일성분 제제, 유효) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 이 보고서용으로 수집한 정보에 따르면, etoposide는 topoisomerase II 억제 기전을 가진 항종양제로 폐 악성종양(예: 소세포폐암)에서 활성이 알려져 있습니다. 이 때문에 폐에 생기는 증식성 종양에도 기전상 적용 가능성이 있습니다.

그러나 예측 점수가 높은 것은 지식 네트워크 기반 예측일 뿐입니다. 연결된 문헌은 고분화 태아형 선암을 구성 요소로 포함하는 폐모세포종 증례보고 한 편뿐이며, 이 질환 자체에서 etoposide의 효과를 보여주는 자료는 없습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [33107372](https://pubmed.ncbi.nlm.nih.gov/33107372/) | 2020 | 증례보고/문헌고찰 | The Journal of International Medical Research | 고전적 이상성(biphasic) 폐모세포종 1례를 보고했습니다. 우상엽 절제 후 nedaplatin과 paclitaxel로 보조 항암요법을 시행했으며, 표준 치료 지침이 없다고 기술합니다. 제공된 초록에는 etoposide에 대한 언급이 없습니다. |

## 한국 시판 정보

6건의 허가증이 모두 단일성분 제제이며 유효 상태입니다. 아래는 그중 5건입니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201003586 | 에토시드주(수출용) | 점성이 있는 맑은 액이 든 바이알 주사제 | 본문 미수록 (허가사항 링크만 제공) |
| 199000999 | 이피에스주 | 점성이 있는 맑은 액이 든 바이알 주사제 | 본문 미수록 (허가사항 링크만 제공) |
| 199101473 | 에토폴주 | 액이 든 갈색 앰플 | 본문 미수록 (허가사항 링크만 제공) |
| 200003750 | 토포주사(수출용) | 투명한 액이 든 앰플 또는 바이알 | 본문 미수록 (허가사항 링크만 제공) |
| 201201790 | 이티에스주(수출용) | 투명한 액이 든 갈색 바이알 주사제 | 본문 미수록 (허가사항 링크만 제공) |

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 약물 (topoisomerase II 억제제) |
| 골수억제 위험 | 골수억제 및 이차 백혈병에 대한 모니터링이 필요합니다. 상세 수치는 허가사항의 경고 및 주의사항을 참조하세요. |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요. |
| 모니터링 항목 | 혈구검사(CBC), 간·신기능 |
| 취급 방호 | 세포독성 약물 취급 규정 준수 필요 |

## 안전성 고려사항

- **주요 경고 및 금기**: 허가사항 본문을 확보하지 못했으므로 허가사항을 참조하세요.
- **약물 상호작용**: 총 100건이 확인되었습니다. 아래는 수집된 목록의 일부입니다.
  - 중등도(Moderate): Aprepitant, Metronidazole, Eliglustat, Rolapitant, Rosuvastatin, Simvastatin, Tinidazole
  - 경미(Minor): Levofloxacin
  - 등급 미상: Calcitriol, Vitamin A, Doxycycline, Cimetidine, Morphine 등

## 결론 및 다음 단계

**결정: Hold**

**사유:**
고분화 태아형 선암을 직접 연구한 임상시험이나 문헌이 없고, 연결된 증례보고도 다른 질환(폐모세포종)을 다루고 있어 근거 수준은 L5입니다. 높은 예측 점수만으로는 효능을 뒷받침할 수 없습니다.

**진행하려면 필요한 것:**
- 이 질환(또는 폐모세포종 아형)에서 etoposide 포함 요법을 직접 평가한 증례 시리즈나 임상시험
- 허가사항(경고, 금기, 허가 적응증 본문) 확보
- 상세 작용 기전(MOA) 데이터 보완

**참고:** 같은 데이터에는 Ewing 육종과 횡문근육종 예측도 있습니다. 이 두 질환은 etoposide 포함 요법을 직접 평가한 시험과 문헌이 있어 별도로 평가할 가치가 있습니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

