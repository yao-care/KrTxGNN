---
layout: default
title: Fluorometholone
parent: 모델 예측만 (L5)
nav_order: 358
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Fluorometholone: 예측 신규 적응증 감염성 전방 포도막염 (infectious anterior uveitis) (근거 수준 L5). 기존 적응증: 허가 적응증 원문이 링크 형태로만 제공되어 구체적인 문구를 확인할 수 없습니다. 허가사항 참조가 필요합니다(안구 염증성 결막…"
monitor_inn: "Fluorometholone"
predicted_indications: ["postinfectious vasculitis", "post-bacterial disorder", "otitis externa", "infective urethral stricture", "post-infectious syndrome", "punctate epithelial keratoconjunctivitis", "infection-related hemolytic uremic syndrome", "Chagas cardiomyopathy"]
---

# Fluorometholone
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

# Fluorometholone: 안구 표면 염증에서 감염성 전방 포도막염으로

## 한 문장 요약

Fluorometholone은 글루코코르티코이드 계열의 점안제로, 안구 염증성 질환 치료에 사용되어 왔습니다.
TxGNN 모델은 **감염성 전방 포도막염(infectious anterior uveitis)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 직접 지지하는 **임상시험은 0건**이고 간접적인 **문헌 1편**만 확인되었습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 원문이 링크 형태로만 제공되어 구체적인 문구를 확인할 수 없습니다. 허가사항 참조가 필요합니다(안구 염증성 결막염에 사용되는 약물로 알려져 있음). |
| 예측 신규 적응증 | 감염성 전방 포도막염 (infectious anterior uveitis) |
| TxGNN 예측 점수 | 99.98% |
| 근거 수준 | L4 (간접 문헌만 있음, 직접 시험 없음) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 20건 |
| 권장 결정 | Hold (연구 질문 단계) |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Fluorometholone은 글루코코르티코이드 수용체(NR3C1)에 작용하는 합성 스테로이드로, 항염증 효과를 나타냅니다. 이는 안구 염증성 결막염에서의 사용과 일치합니다.

전방 포도막염은 안구 내 염증 질환이므로, 항염증 기전상 적용 가능성은 있습니다. 다만 검색된 유일한 문헌(PMID 29739028)은 **비감염성** 포도막염에서의 국소 스테로이드를 다룬 것으로, 감염성 포도막염에 대해서는 간접 근거일 뿐입니다. 또한 이 문헌에서 포도막염의 1차 선택 약물은 prednisolone acetate 1%로 언급되어, Fluorometholone은 상대적으로 투과성이 낮은 편입니다.

감염성 포도막염에서는 스테로이드가 감염을 악화시킬 수 있어 항균 치료를 병행해야 합니다. TxGNN 점수는 매우 높지만 모델 예측일 뿐입니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [29739028](https://pubmed.ncbi.nlm.nih.gov/29739028/) | 2018 | Review | Klin Monbl Augenheilkd | 비감염성 포도막염에서 국소 스테로이드와 NSAID의 역할 정리. 전방 포도막염에서 국소 스테로이드가 효과적이며, prednisolone acetate 1%가 1차 선택. Fluorometholone은 안내 투과성이 상대적으로 낮음 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201707502 | 플루아이점안액0.1% | 현탁액(점안제) | 허가사항 참조 |
| 200100630 | 풀아이론점안액0.1% | 수성 현탁액(점안제) | 허가사항 참조 |
| 201207413 | 후메토론플러스점안액 | 현탁액(점안제) | 허가사항 참조 |
| 201306498 | 플루빈점안액0.1% (1회용/다회용) | 수성 현탁액(점안제) | 허가사항 참조 |
| 201007735 | 디겐타안연고 (겐타마이신 + 플루오로메톨론) | 안연고 | 허가사항 참조 |

위 표는 전체 20건 중 일부이며, 모든 허가는 유효 상태입니다. 허가 적응증은 식약처(MFDS) 허가사항 문서에 게재되어 있습니다.

## 안전성 고려사항

- **약물 상호작용**: 12건이 조회되었으며, 상호작용 등급은 대부분 미분류입니다. 조회된 약물은 Doxycycline, Salbutamol, Cyclosporine, Acetaminophen, Digoxin, Brimonidine, Cephalexin, Alendronic acid, Acyclovir, Diazepam, Fenofibrate 등입니다.
- **신규 적응증 관련 유의점**: 감염성 포도막염 및 감염성 각결막염에서는 스테로이드 사용 시 항균 치료를 병행하고 안압을 모니터링해야 합니다.

그 외 경고 및 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 점수는 매우 높지만 직접적인 임상시험이 없고, 유일한 문헌은 비감염성 포도막염에 관한 간접 근거입니다. 감염성 상황에서는 스테로이드가 감염을 악화시킬 위험이 있어 연구 질문 단계로 두는 것이 적절합니다.

**진행하려면 필요한 것:**
- 식약처 허가사항(경고·금기 포함) 확보 및 분석
- 작용 기전(MOA) 데이터 보완
- 감염성 전방 포도막염에서 Fluorometholone을 항균제와 병용한 효능·안전성 임상 근거
- 비감염성 포도막염에서의 다른 스테로이드(예: prednisolone acetate)와의 비교 자료
- 안압 상승 및 감염 악화 위험에 대한 모니터링 계획
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

