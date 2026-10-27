---
layout: default
title: Canakinumab
parent: 모델 예측만 (L5)
nav_order: 175
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Canakinumab: 예측 신규 적응증 간 경색 (Hepatic Infarction) (근거 수준 L5). 기존 적응증: 허가 적응증 본문이 문서 링크로만 제공되어 확인할 수 없음 (허가사항 참조)"
monitor_inn: "CANAKINUMAB"
predicted_indications: ["hepatic infarction", "hepatic veno-occlusive disease", "peliosis hepatis", "syndrome with combined immunodeficiency", "periodic fever-infantile enterocolitis-autoinflammatory syndrome", "extracutaneous mastocytoma", "Blau syndrome", "monosomy X", "liver angiosarcoma"]
---

# Canakinumab
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

## Canakinumab: 크리오피린 관련 주기열 증후군(CAPS)에서 간 경색(Hepatic Infarction)으로
{: .text-alpha }

## 한 문장 요약

Canakinumab은 인터루킨-1β(IL-1β)를 표적으로 하는 단클론항체이며, 한국에서는 일라리스주사액으로 허가되어 있습니다. 이 보고서를 위해 수집한 문헌에서는 CAPS 같은 자가염증 질환이 허가 적응증으로 언급됩니다.
TxGNN 모델은 **간 경색(hepatic infarction)**에 효과가 있을 수 있다고 가장 높은 순위로 예측했지만, 현재 이를 직접 지지하는 **임상시험은 0건**, **문헌도 0건**입니다. 따라서 모델 예측만 있는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문이 문서 링크로만 제공되어 확인할 수 없음 (허가사항 참조) |
| 예측 신규 적응증 | 간 경색 (Hepatic Infarction) |
| TxGNN 예측 점수 | 99.86% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 없습니다. 다만 Canakinumab은 IL-1β를 중화하는 항체로 알려져 있어, 이론상 허혈과 관련된 염증 반응을 조절할 가능성은 있습니다.

그러나 간 경색에 대해 IL-1β 차단이 효과가 있다는 직접적인 근거나 데이터는 없습니다. 기존 적응증인 자가염증 질환과 간 경색은 병태생리가 크게 달라, 기전상 연관성도 약합니다. 이 예측은 지식 그래프 기반 모델의 출력으로만 해석해야 합니다.

## 안전성 고려사항

**약물 상호작용**: 수집된 데이터에서 총 100건의 상호작용이 확인되었습니다. 주요 항목은 다음과 같습니다.

- **중등도**
  - 코르티코스테로이드: hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide, prednisolone, prednisone
  - 스타틴: simvastatin
  - 항응고제: warfarin, apixaban, rivaroxaban, dicoumarol
  - 방사성의약품·항체: ibritumomab tiuxetan, iobenguane(I-131), tositumomab 계열
- **경미**: 아연 제제(zinc acetate, gluconate, sulfate)

경고 및 금기 사항은 허가사항을 참조하세요.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201803269 | 일라리스주사액(카나키누맙, 유전자재조합) (한국노바티스) | 주사제 (바이알) | 허가사항 참조 |

## 참고: 근거가 있는 다른 예측 적응증

1순위 예측은 근거가 없지만, 같은 모델이 예측한 다른 적응증 중에는 근거가 확인된 것이 있습니다.

| 예측 적응증 | 순위 | 근거 수준 | 요약 | 권장 |
|-----------|-----|---------|------|-----|
| 가족성 지중해열 (FMF) | 6 | L1 | 완료된 Phase 3 시험 3건(NCT00991146, NCT01576367, NCT00685373)과 체계적 문헌고찰·메타분석이 있습니다. 시험은 주로 CAPS 대상이어서 FMF에 대한 직접성은 부분적입니다. FMF는 pyrin 염증복합체 이상으로 IL-1β가 과다 생성되는 질환입니다. | Proceed with Guardrails |
| Blau 증후군 | 8 | L3 | 증례 및 소규모 증례군(PMID 23124805 등)과 체계적 문헌고찰이 있으나, 대조 임상시험은 없습니다. | Research Question |

FMF는 colchicine 불응성 또는 불내성 환자로 제한하고 감염을 모니터링하며, 질환 코드(상염색체 우성형) 매핑을 확인하는 조건이 붙습니다. 나머지 예측 중 일부(예: 결합 면역결핍 증후군, monosomy X)는 검색된 문헌이 무관하거나 매핑 오류로 보여, 근거로 인정하기 어렵습니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
간 경색은 TxGNN 점수가 높지만 임상시험과 문헌이 모두 없고, 기전적 연결도 가설 수준입니다. 현재로서는 재창출 근거가 부족합니다.

**진행하려면 필요한 것:**
- 허혈성 간 손상에서 IL-1β 차단의 효과를 검증하는 전임상 또는 기전 연구
- 간 경색 관련 증례 보고나 관찰 연구 등 임상 근거
- 상세한 작용 기전 데이터와 허가사항(경고·금기) 확인
- 근거가 있는 FMF 등 다른 예측 적응증을 우선 검토할지 판단
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

