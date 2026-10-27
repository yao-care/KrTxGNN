---
layout: default
title: Tenecteplase
parent: 모델 예측만 (L5)
nav_order: 724
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Tenecteplase: 예측 신규 적응증 후외측 심근경색 (Posterolateral Myocardial Infarction) (근거 수준 L5). 기존 적응증: 허가 적응증 원문이 링크(MFDS 허가 PDF)로만 제공되어 구체적 문구를 확인할 수 없음"
monitor_inn: "TENECTEPLASE"
predicted_indications: ["congenital coronary artery anomaly", "coronary stenosis", "partial deletion of the short arm of chromosome 16", "beta-thalassemia with other manifestations", "hemolytic anemia due to glucophosphate isomerase deficiency", "pyropoikilocytosis, hereditary", "pyruvate kinase deficiency of red cells"]
---

# Tenecteplase
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

## Tenecteplase: 급성 심근경색(ST 상승 심근경색)에서 후외측 심근경색으로
{: .text-alpha }

## 한 문장 요약

Tenecteplase는 섬유소 특이적 조직 플라스미노겐 활성화제로, 혈전 용해 목적의 주사제로 한국에서 허가되어 있습니다.
TxGNN 모델은 **후외측 심근경색(posterolateral myocardial infarction)**에 효과가 있을 수 있다고 예측하지만, 이 질환은 이미 알려진 심근경색 용도의 하위 유형에 가까워 실제 재창출이라고 보기 어렵습니다.
이 예측을 직접 뒷받침하는 **임상시험은 0건**, **문헌도 0편**입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 원문이 링크(MFDS 허가 PDF)로만 제공되어 구체적 문구를 확인할 수 없음 |
| 예측 신규 적응증 | 후외측 심근경색 (Posterolateral Myocardial Infarction) |
| TxGNN 예측 점수 | 99.87% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 tenecteplase는 섬유소 특이적 조직 플라스미노겐 활성화제 계열로, 혈전의 섬유소를 분해해 막힌 혈관의 흐름을 회복시킵니다. 급성 ST 상승 심근경색의 혈전 용해 치료로 확립되어 있습니다.

후외측 심근경색은 같은 질환(관상동맥 혈전성 폐색)의 해부학적 하위 유형입니다. 따라서 높은 예측 점수는 기전상 그럴듯합니다. 다만 새로운 질환으로의 확장이라기보다 기존 용도의 세분화에 가깝고, 이 용어에 대해 제공된 시험이나 문헌은 없습니다.

참고로 같은 예측 목록의 다른 항목 중 일부(염색체 결실, 적혈구 효소 결핍증 등)는 기전적 연관성이 없어 그래프 상의 인위적 연관으로 보입니다. 후순위 예측 중에서는 **관상동맥 협착(coronary stenosis)**이 소규모 연구(관상동맥 내 저용량 tenecteplase의 타당성·안전성 연구 등)로 L3 수준의 근거를 가장 많이 확보했습니다. 다만 이는 고정된 죽상경화성 협착이 아닌 혈전성 폐색에 대한 보조 요법에 해당합니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202502617 | 메탈라제주사25밀리그램(테넥테플라제) | 주사제 (바이알, 용액 조제용 동결건조 덩어리) | 허가사항 PDF 참조 (한국베링거인겔하임) |

## 안전성 고려사항

- **약물 상호작용**: 총 100건의 상호작용이 확인되었으며, 일부 주요 항목은 다음과 같습니다.
  - **Major**: Abciximab, Apixaban, Betrixaban, Acalabrutinib, Avapritinib, Deferasirox, Ibritumomab tiuxetan, Tositumomab
  - **Moderate**: 아스피린, Ibuprofen, Ketorolac, Celecoxib, Aminocaproic acid, Omega-3 지방산, Fenfluramine, Dexfenfluramine, Sibutramine
  - 항응고제·항혈소판제·NSAID와의 병용 시 출혈 위험 증가에 유의해야 합니다.

그 외 경고 및 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
후외측 심근경색은 이미 확립된 심근경색 적응증의 하위 유형이어서 진정한 재창출 후보로 보기 어렵습니다. 해당 용어에 대한 임상시험과 문헌이 없어 근거가 모델 예측(L5)에 그칩니다.

**진행하려면 필요한 것:**
- MFDS 허가사항(적응증, 경고, 금기) 확보 및 분석
- 작용 기전(MOA) 데이터 보완
- 기존 허가 적응증(급성 심근경색)에 후외측 심근경색이 이미 포함되는지 확인
- 재창출 가치가 있는 후보(예: 관상동맥 협착에서의 혈전성 병변 보조 요법)에 대한 추가 문헌 검토 및 임상시험 탐색
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

