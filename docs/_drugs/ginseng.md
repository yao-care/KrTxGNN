---
layout: default
title: Ginseng
parent: 모델 예측만 (L5)
nav_order: 375
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Ginseng: 예측 신규 적응증 약물 유발 골다공증 (Drug-induced Osteoporosis) (근거 수준 L5). 기존 적응증: 한방 생약 제제(십전대보탕, 인삼패독산…"
monitor_inn: "Ginseng"
predicted_indications: ["drug-induced osteoporosis", "acne (disease)", "severe nonproliferative diabetic retinopathy", "hemorrhagic disease of newborn", "cortical cataract", "nuclear senile cataract", "diabetic retinopathy", "amenorrhea (disease)", "craniostenosis cataract", "mature cataract"]
---

# Ginseng
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
{: .fs-6 .fw-300 }

---

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 약사 평가 보고서

</div>

# Ginseng(인삼): 한방 생약 제제에서 약물 유발 골다공증으로

## 한 문장 요약

Ginseng(인삼)은 십전대보탕, 인삼패독산, 보중익기탕 등 한방 생약 제제의 성분으로 한국에서 널리 시판되고 있습니다.
TxGNN 모델은 **약물 유발 골다공증(Drug-induced Osteoporosis)**에 효과가 있을 수 있다고 예측하지만, 현재 이 방향을 지지하는 **임상시험은 0건, 문헌도 0편**으로 모델 예측만 있는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 한방 생약 제제(십전대보탕, 인삼패독산, 보중익기탕 등)의 성분으로 허가됨. 허가 적응증 원문은 이번 보고서용 데이터에 포함되어 있지 않아 허가증 원문 확인이 필요함 |
| 예측 신규 적응증 | 약물 유발 골다공증 (Drug-induced Osteoporosis) |
| TxGNN 예측 점수 | 99.95% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Ginseng은 여러 한방 처방에 들어가는 생약 성분이며, 오랜 사용 이력이 있습니다. 진세노사이드(ginsenoside)가 일반적으로 뼈 재형성(bone remodeling)에 영향을 줄 수 있다는 제안이 있어, 기전상 골다공증에 적용될 가능성은 있습니다.

다만 이번 보고서용 데이터에는 약물 유발 골다공증에 특화된 시험, 문헌, 기전 근거가 없습니다. 기존 허가 적응증과 신규 적응증의 유사성 평가도 아직 이루어지지 않았습니다. 따라서 이 예측의 타당성은 모델 점수에만 의존하며, 그 외 근거로 뒷받침되지 않습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

허가증 20건이 모두 유효하며, 대표 5건은 다음과 같습니다. 허가 적응증은 허가증 원문 문서로만 제공되어 표에 요약하지 않았습니다.

| 허가번호 | 제품명 | 제형 | 제조사 |
|---------|------|------|-------|
| 197900047 | 데시텐과립(십전대보탕) | 흑갈색의 과립제 | (유)한풍제약 |
| 200004501 | 패감산과립(인삼패독산) | 회갈색의 과립 | 한솔신약(주) |
| 200005653 | 경방이중탕엑스과립 | 황갈색의 과립제 | 경방신약(주) |
| 202401570 | 진삼소음액 | 흑갈색의 액제 | 메딕스제약(주) |
| 199302420 | 광동마음정액(청심보혈탕) | 약간 혼탁한 갈색의 액제 | 광동제약(주) |

## 안전성 고려사항

- **약물 상호작용**: 총 83건이 기록되어 있습니다. 확인된 항목은 모두 중등도(Moderate)이며, 주로 다음 계열입니다.
  - 당뇨병 치료제: Metformin, Pioglitazone, Glimepiride, Acarbose, Canagliflozin, Dapagliflozin, Empagliflozin, Alogliptin, Linagliptin, Semaglutide, Dulaglutide 등
  - 인슐린 제제: Insulin glargine, degludec, detemir, aspart, glulisine 등
  - 기타: Acetylsalicylic acid(아스피린)

  당뇨병 환자나 항응고/항혈소판제 복용자에게 사용할 때는 혈당과 출혈 경향의 모니터링이 필요합니다.

그 외 경고·금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
약물 유발 골다공증에 대한 TxGNN 점수(99.95%)는 높지만, 임상시험과 문헌이 모두 없는 L5(모델 예측만 있음) 단계입니다. 작용 기전 데이터도 없어 현 시점에서 개발을 진행할 근거가 부족합니다.

**진행하려면 필요한 것:**
- 약물 유발 골다공증(예: 스테로이드 유발)과 인삼/진세노사이드의 관련성을 다룬 전임상 및 임상 문헌 검색
- 작용 기전 데이터 확보 (DrugBank 등)
- 허가증 원문에서 기존 적응증과 경고·금기 정보 확인
- 당뇨병 치료제, 항응고제 등과의 상호작용 관리 방안 수립

**참고:** 같은 예측 목록에서 **당뇨병성 망막병증(diabetic retinopathy, TxGNN 99.55%)**은 문헌 20편(전임상, 리뷰, 네트워크 약리학 중심)이 있고, 2026년 한국 홍삼의 무작위 이중맹검 임상시험 보고(PMID 42395017)도 있어 근거가 가장 많습니다. 우선순위를 다시 정한다면 이 적응증을 먼저 별도로 평가하는 것을 권장합니다. 다만 이 경우에도 근거 수준은 L4이며, 등록된 임상시험은 없습니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

