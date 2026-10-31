---
layout: default
title: Carboplatin
parent: 모델 예측만 (L5)
nav_order: 184
evidence_level: L5
indication_count: 9
monitor_inn: "Carboplatin"
predicted_indications: ["rectum mucinous adenocarcinoma", "colon mucinous adenocarcinoma", "adult germ cell tumor", "cervical mucinous adenocarcinoma", "gallbladder mucinous adenocarcinoma", "endometrial mucinous adenocarcinoma", "villoglandular endometrial endometrioid adenocarcinoma", "endometrial mixed adenocarcinoma", "extrahepatic bile duct mucinous adenocarcinoma"]
last_modified_at: 2026-10-31
description: "Carboplatin: 예측 신규 적응증 직장 점액성 선암 (근거 수준 L5). 기존 적응증: 허가 문서 링크만 확인되며 적응증 본문은 확보되지 않음"
---

# Carboplatin
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

## Carboplatin: 기존 허가 적응증(허가 문서 참조)에서 직장 점액성 선암으로
{: .text-alpha }

## 한 문장 요약

Carboplatin은 백금계 항암화학요법제로, 한국에서 5건의 허가증이 등록되어 있습니다. 다만 이번에 정리한 데이터에는 허가 적응증의 본문이 없고 허가 문서 링크만 있습니다.
TxGNN 모델은 **직장 점액성 선암(rectum mucinous adenocarcinoma)**에 효과가 있을 수 있다고 예측하며 점수는 0.9928로 높습니다. 그러나 이 질환을 직접 다룬 **임상시험은 0건, 문헌도 0건**이어서 모델 예측만 있는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 문서 링크만 확인되며 적응증 본문은 확보되지 않음 |
| 예측 신규 적응증 | 직장 점액성 선암 |
| TxGNN 예측 점수 | 0.9928 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 5건 / 전체 5건) |
| 허가증 수 | 5건 (유효 5건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 일반적으로 알려진 바에 따르면 Carboplatin은 백금계 약물로, DNA에 결합해 가교를 형성하고 빠르게 증식하는 암세포의 분열을 억제합니다. 이론상 선암 세포에도 작용할 수 있습니다.

그러나 이 예측을 뒷받침하는 것은 TxGNN의 높은 예측 점수뿐입니다. 직장 점액성 선암에서 Carboplatin을 평가한 시험이나 문헌은 확인되지 않았습니다. 점액성 조직형은 일반적으로 항암제 감수성이 낮다고 알려져 있어, 기전만으로 효과를 단정하기 어렵습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 199201568 | 카보티놀주사 | 갈색 바이알(무색 투명한 용액) | 허가 문서 링크만 확인됨, 본문 미확보 |
| 200004907 | 카보틴주 (수출용) | 갈색 바이알(무색 투명한 용액) | 허가 문서 링크만 확인됨, 본문 미확보 |
| 200905067 | 칸플라틴주 (수출용) | 갈색 바이알(무색 투명한 용액) | 허가 문서 링크만 확인됨, 본문 미확보 |
| 199101108 | 네오플라틴주 | 갈색 바이알(무색 투명한 주사액) | 허가 문서 링크만 확인됨, 본문 미확보 |
| 200210228 | 화이자카보플라틴주10mg/ml | 바이알(무색 투명한 주사액) | 허가 문서 링크만 확인됨, 본문 미확보 |

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 약물 (백금계) |
| 골수억제 위험 | 일반적으로 높은 편이며 혈소판감소와 호중구감소가 대표적입니다. 이번 데이터에는 독성 정보가 없습니다. |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 혈구 검사(CBC), 신장 기능, 간 기능 |
| 취급 방호 | 세포독성 약물 취급 규정 준수 필요 |

## 안전성 고려사항

허가사항의 경고와 금기 정보는 이번 데이터에 포함되어 있지 않아 허가사항을 직접 확인해야 합니다.

**약물 상호작용**: 총 100건이 조회되었으며, 이 중 확인된 20건은 다음과 같습니다.
- **중등도**
  - 프로톤펌프억제제: rabeprazole, omeprazole, dexlansoprazole, esomeprazole, lansoprazole, pantoprazole
  - 항생제: kanamycin, neomycin, streptomycin, vancomycin, metronidazole, tinidazole
  - 스타틴: rosuvastatin, simvastatin
- **경미**: levofloxacin
- **등급 미확인**: calcitriol, glimepiride, mesalazine, doxycycline, clotrimazole

## 결론 및 다음 단계

**결정: Hold**

**사유:**
직장 점액성 선암에 대한 예측 점수는 높지만, 이를 직접 뒷받침하는 임상시험이나 문헌이 없어 근거 수준이 L5(모델 예측만 있음)입니다. 작용 기전, 허가 적응증 본문, 안전성 정보도 확보되지 않았습니다.

**진행하려면 필요한 것:**
- 허가 문서(MFDS 첨부문서)에서 적응증, 경고, 금기 정보 확보
- DrugBank 등에서 작용 기전 데이터 확보
- 직장 및 대장 점액성 선암에서 Carboplatin 효능을 직접 평가한 시험이나 문헌 탐색
- 같은 데이터에서 Carboplatin의 다른 예측 적응증(성인 생식세포종양, 자궁내막 혼합 선암 등)은 임상시험이 더 많으므로 별도 평가 권장
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

