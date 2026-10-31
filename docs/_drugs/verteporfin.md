---
layout: default
title: Verteporfin
parent: 모델 예측만 (L5)
nav_order: 783
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-31
description: "Verteporfin: 예측 신규 적응증 핵 DNA 이상에 의한 미토콘드리아 산화적 인산화 장애 (Mitochondrial oxidative phosphorylati… (근거 수준 L5). 기존 적응증: 허가 적응증 텍스트가 링크로만 제공되어 확인 불가 (식약처 허가사항 참조)"
monitor_inn: "VERTEPORFIN"
predicted_indications: ["mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies"]
---

# Verteporfin
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

## Verteporfin: 맥락막 신생혈관(허가 적응증 원문 미확인)에서 핵 DNA 이상에 의한 미토콘드리아 산화적 인산화 장애로
{: .text-alpha }

## 한 문장 요약

Verteporfin은 광역학 요법에 쓰이는 광감작제로, 한국에서 주사제(비쥬다인주사)로 허가·시판되고 있습니다. 다만 이번 데이터에서는 허가 적응증 본문이 링크로만 제공되어 구체적인 내용을 확인하지 못했습니다.
TxGNN 모델은 **핵 DNA 이상에 의한 미토콘드리아 산화적 인산화 장애**에 효과가 있을 수 있다고 예측합니다.
그러나 이를 뒷받침하는 **임상시험은 0건, 문헌도 0편**이며 모델 예측만 있는 상태입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 텍스트가 링크로만 제공되어 확인 불가 (식약처 허가사항 참조) |
| 예측 신규 적응증 | 핵 DNA 이상에 의한 미토콘드리아 산화적 인산화 장애 (Mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies) |
| TxGNN 예측 점수 | 0.9949 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 1건 / 전체 1건) |
| 허가증 수 | 1건 (유효 1건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Verteporfin은 벤조포르피린 유도체 광감작제입니다. 빛으로 활성화되면 활성산소종(ROS)이 생성되어 국소 혈관이 폐쇄되며, 이 원리로 광역학 요법에 사용됩니다. 전임상 연구에서는 빛 활성화 없이도 YAP-TEAD 전사 복합체를 억제할 수 있음이 보고되었습니다.

그러나 이 두 기전 모두 핵 DNA 이상에 의한 산화적 인산화(OXPHOS) 결손과의 연결은 입증되지 않았습니다. 예측 점수가 높은 것은 TxGNN 모델(딥러닝)이 관련 질환 간에 학습한 유사성을 반영한 결과일 수 있으며, 생물학적 근거는 아닙니다.

오히려 빛으로 생성되는 ROS가 미토콘드리아 기능 이상을 악화시킬 가능성이 있습니다. 또한 전신 질환인 미토콘드리아 질환은 국소 광역학 치료에 적합하지 않습니다. 이러한 우려는 추정 단계이며 검증되지 않았습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200307797 | 비쥬다인주사(베르테포르핀) | 무색투명한 바이알에 암녹색의 동결건조 분말이 든 주사제 | 식약처 허가사항 링크로만 제공되어 요약 불가 |

## 안전성 고려사항

- **지식 그래프상 금기 질환**: 유전성 포르피린증, 포르피린 대사 질환, 포르피린증, 간 질환, 담낭 질환. 이는 허가사항 본문이 아니라 TxGNN 지식 그래프(PrimeKG)의 약물-질환 금기 연결에서 가져온 정보입니다.
- **약물 상호작용**: 데이터상 총 100건이 확인되었으며, 아래는 그중 일부입니다. 대부분 중등도(Moderate)입니다.
  - 테트라사이클린계: Doxycycline, Tetracycline, Minocycline (외용 포함)
  - 설포닐유레아계 혈당강하제: Chlorpropamide, Glimepiride, Glipizide, Glyburide, Tolazamide, Acetohexamide, Tolbutamide
  - 기타: Acetylsalicylic acid, Levofloxacin, Mannitol, Sulfasalazine, Beta carotene, Papaverine
  - 경미(Minor): Polymyxin B

허가사항의 경고 및 금기 항목은 반드시 식약처 허가사항을 직접 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 점수는 높지만 지지하는 임상시험과 문헌이 전혀 없으며, 기전적 연결도 확인되지 않았습니다. 광 활성화로 생성되는 ROS가 미토콘드리아 기능 이상을 악화시킬 수 있고, 전신 질환에 국소 광역학 치료를 적용하기도 어렵습니다.

**진행하려면 필요한 것:**
- 식약처 허가사항(경고·금기 포함) 원문 확보 및 분석
- 상세한 작용 기전(MOA) 데이터 확보 (DrugBank 조회)
- 미토콘드리아 OXPHOS 결손 모델에서의 전임상 근거 (YAP-TEAD 억제 등 빛 비의존적 기전 포함)
- 투여 경로 적합성 평가 (현재 평가 보류 상태)
- 관련 임상시험 및 문헌 재검색
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

