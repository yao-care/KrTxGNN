---
layout: default
title: Difluprednate
parent: 모델 예측만 (L5)
nav_order: 278
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
monitor_inn: "DIFLUPREDNATE"
predicted_indications: ["familial adrenal hypoplasia with absent pituitary luteinizing hormone", "seborrheic keratosis", "PAGOD syndrome", "vulvar inverted follicular keratosis", "adrenocortical insufficiency", "seborrheic dermatitis", "46,XY disorder of sex development", "necrobiosis lipoidica", "nephrotic syndrome", "iris disease"]
description: "Difluprednate: 예측 신규 적응증 LH 결핍을 동반한 가족성 부신 저형성증 (familial adrenal hypoplasia with absent pituitary luteinizing hormone) (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199501565/EE"
---

# Difluprednate
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

## Difluprednate: LH 결핍을 동반한 가족성 부신 저형성증 (familial adrenal hypoplasia with absent pituitary luteinizing hormone)
{: .text-alpha }

## 한 문장 요약

Difluprednate는 합성 부신피질호르몬(글루코코르티코이드 수용체 작용제)으로, 국내에서는 크림제로 허가되어 시판되고 있습니다. TxGNN 모델은 **LH 결핍을 동반한 가족성 부신 저형성증**에 효과가 있을 수 있다고 예측하지만, 현재 이를 지지하는 **임상시험은 0건, 문헌도 0편**입니다. 따라서 이 예측은 모델 점수에만 근거합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199501565/EE |
| 예측 신규 적응증 | LH 결핍을 동반한 가족성 부신 저형성증 (familial adrenal hypoplasia with absent pituitary luteinizing hormone) |
| TxGNN 예측 점수 | 0.9996 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 데이터베이스에 정리되어 있지 않습니다. 다만 약리학 자료에 따르면 difluprednate는 글루코코르티코이드 수용체(NR3C1)에 강하게 결합하는 작용제입니다(Ki 0.78 nM). 이 수용체 작용을 통해 염증을 억제합니다.

신규 적응증은 글루코코르티코이드 결핍이 핵심 문제인 유전성 내분비 질환입니다. 그래서 글루코코르티코이드 네트워크와의 연관성 때문에 모델 점수가 높게 나왔을 가능성이 큽니다. 그러나 이 약은 국소 투여용 강력 스테로이드로, 부신 기능 저하에 필요한 보충요법으로는 적합하지 않습니다. 따라서 기전상 타당하다고 보기 어렵고, 임상적 근거도 없습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 199501565 | 리베카크림(디플루프레드네이트) | 백색 크림제 | 허가 문서 링크만 확인되며 적응증 본문은 확인되지 않음 |

## 안전성 고려사항

- **약물 상호작용**: 등록된 약물 간 상호작용은 없고, 약리학적 표적으로 글루코코르티코이드 수용체(작용제)만 확인되었습니다.
- **지식그래프 기반 금기 질환** (허가사항이 아닌 TxGNN 지식그래프 기준): 고안압증, 단순헤르페스바이러스 각막염, 안결핵, 진균성 각막궤양

그 외 경고 및 금기 사항은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
임상시험과 문헌이 전혀 없고 근거 수준은 L5입니다. 국소 스테로이드는 부신 기능 부전의 보충요법으로 적합하지 않아 기전상으로도 타당성이 낮습니다.

**진행하려면 필요한 것:**
- 허가 적응증 본문 및 경고·금기 확인 (MFDS 허가사항 문서 확보)
- 상세한 작용 기전 데이터(MOA) 보완
- 이 질환에서 국소 투여 스테로이드의 타당성을 뒷받침하는 전임상·임상 근거. 현재로서는 기존 표준 보충요법(하이드로코르티손 등)이 있어 우선순위가 낮습니다.

### 참고: 다른 예측 적응증

상위 10개 예측 중 대부분은 근거가 없는 L5 수준이며 권장 결정은 Hold입니다. 예외는 다음과 같습니다.

- **홍채 질환(iris disease, 10위, 0.9916)**: 근거 수준 L4, 권장 결정 Research Question. 연관 문헌은 토끼 대상 전임상 약동학 연구 1편(PMID [21182429](https://pubmed.ncbi.nlm.nih.gov/21182429/), 2011, J Ocul Pharmacol Ther)뿐이며, 안구 조직 분포를 다룹니다. 이 적응증은 전방 포도막염 등 기존 안과 적응증과 크게 겹치므로 새로운 재창출 기회라기보다 허가 범위와의 중복으로 보는 것이 적절합니다. 허가사항 및 포도막염 임상시험과의 대조 확인이 필요합니다.
- **지루피부염(seborrheic dermatitis), 괴사성 지방유전증(necrobiosis lipoidica)**: 국소 스테로이드의 항염증 효과라는 계열 수준의 간접 근거만 있고, difluprednate 자체의 연구는 없습니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

