---
layout: default
title: Agomelatine
parent: 모델 예측만 (L5)
nav_order: 30
evidence_level: L5
indication_count: 7
monitor_inn: "Agomelatine"
predicted_indications: ["benign paroxysmal torticollis of infancy", "agoraphobia", "neurotic disorder", "Ohdo syndrome and variants", "ligneous conjunctivitis", "blepharophimosis - intellectual disability syndrome, Ohdo type", "Keppen-Lubinsky syndrome"]
last_modified_at: 2026-10-23
description: "Agomelatine: 예측 신규 적응증 영아 양성 발작성 사경 (근거 수준 L5). 기존 적응증: 허가 적응증 본문이 데이터에 텍스트로 제공되지 않음(허가 문서 링크만 확인됨). 약리학 자료상 임상 용도는 주요 우울장애"
---

# Agomelatine
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **7** 건
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

## Agomelatine: 우울증 계열 적응증에서 영아 양성 발작성 사경으로
{: .text-alpha }

## 한 문장 요약

Agomelatine은 한국에서 허가된 단일 성분 제제(아고틴정 25밀리그램)로 시판되는 약이며, 약리학 자료상 주요 우울장애 치료에 사용되는 약물입니다.
TxGNN 모델은 **영아 양성 발작성 사경(benign paroxysmal torticollis of infancy)**에 효과가 있을 수 있다고 예측하지만, 이 질환을 직접 다룬 임상시험과 문헌은 **0건**입니다.
따라서 근거 수준은 L5(모델 예측만 있음)이며, 현재는 보류(Hold)가 적절합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문이 데이터에 텍스트로 제공되지 않음(허가 문서 링크만 확인됨). 약리학 자료상 임상 용도는 주요 우울장애 |
| 예측 신규 적응증 | 영아 양성 발작성 사경 |
| TxGNN 예측 점수 | 0.9996 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가 건수 | 1건 (단일 성분 1건, 유효) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 확보되어 있지 않습니다. 다만 약리학 자료에는 Agomelatine이 멜라토닌 MT1·MT2 수용체와 세로토닌 5-HT2A·2B·2C 수용체를 표적으로 하는 것으로 기록되어 있으며, 주요 우울장애 치료에 쓰이는 약물로 분류됩니다.

영아 양성 발작성 사경은 편두통 스펙트럼 및 CACNA1A 이온채널 이상과 관련된 드물고 자연 소실되는 소아 발작성 질환입니다. 멜라토닌 작용제/5-HT2C 길항 약리와 이 질환의 병태생리를 연결하는 타당한 약리학적 근거는 확인되지 않습니다. 또한 영아를 대상으로 한 연구도 없습니다. 높은 TxGNN 점수는 TxGNN 모델(딥러닝)이 산출한 값으로, 모델이 학습한 관련 질환 간 유사성을 반영할 수 있을 뿐 생물학적 근거는 아닙니다.

## 안전성 고려사항

- **약물 상호작용/표적 정보**: 약리학 데이터에는 5-HT2A, 5-HT2B, 5-HT2C, MT1, MT2 수용체 5개 표적이 기록되어 있습니다. 이는 수용체 표적 정보이며, 개별 약물 간 상호작용 등급은 제공되지 않았습니다.

그 외 경고·금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 질환에 대한 임상시험과 문헌이 없고 기전적 연결고리도 확립되지 않아 모델 예측 단계(L5)에 머물러 있습니다. 대상이 영아라는 점에서 안전성 근거 없이 진행하기 어렵습니다.

**진행하려면 필요한 것:**
- 허가사항(MFDS 첨부문서)의 경고·금기 정보 확보
- 상세한 작용 기전(MOA) 데이터 확보
- 영아 양성 발작성 사경과 멜라토닌/5-HT2C 경로의 연관성에 대한 전임상 또는 기전 근거
- 소아·영아 대상 안전성 자료
- 참고: 후순위 예측 중 광장공포증(agoraphobia)은 불안 스펙트럼 질환으로 간접적 타당성이 있어, 우선 검토할 후보로 고려할 수 있습니다(현재 직접 근거는 없음).
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

