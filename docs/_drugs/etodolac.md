---
layout: default
title: Etodolac
parent: 모델 예측만 (L5)
nav_order: 327
evidence_level: L5
indication_count: 6
monitor_inn: "Etodolac"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "hypermobility of coccyx"]
last_modified_at: 2026-10-28
description: "Etodolac: 예측 신규 적응증 말단중간이형성증 Hunter-Thompson형 (근거 수준 L5). 기존 적응증: 확인 불가 (허가 적응증 본문 없음, 허가 문서 링크만 확인됨)"
---

# Etodolac
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

## Etodolac: 기존 적응증 정보 부재에서 말단중간이형성증 헌터-톰슨형으로
{: .text-alpha }

## 한 문장 요약

Etodolac은 COX-2 선호성 비스테로이드 소염진통제(NSAID)이며, 한국에서 단일 성분 제제로 허가되어 있습니다. 다만 이 보고서에 사용된 데이터에는 허가 적응증의 본문이 없습니다.
TxGNN 모델은 **말단중간이형성증 Hunter-Thompson형(acromesomelic dysplasia, Hunter-Thompson type)**에 효과가 있을 수 있다고 예측합니다. 그러나 이를 직접 뒷받침하는 **임상시험은 0건, 문헌도 0편**이어서 모델 예측만 있는 상태입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (허가 적응증 본문 없음, 허가 문서 링크만 확인됨) |
| 예측 신규 적응증 | 말단중간이형성증 Hunter-Thompson형 |
| TxGNN 예측 점수 | 0.9997 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가 건수 | 10건 (모두 단일 성분, 유효) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 일반적으로 Etodolac은 COX-2 선호성 NSAID로 프로스타글란딘 합성을 줄여 염증과 통증을 완화하는 약물로 알려져 있습니다.

Hunter-Thompson형 말단중간이형성증은 GDF5(BMP 신호전달) 기능상실 변이로 생기는 희귀 골격 이형성증입니다. Etodolac은 GDF5/BMP 경로에 작용하는 것으로 알려져 있지 않아, 확립된 기전적 연결고리가 없습니다.

TxGNN 점수는 TxGNN 모델(딥러닝)이 산출한 값으로, 모델이 관련 질환 사이에서 학습한 유사성을 반영했을 가능성이 있으며 생물학적 근거는 아닙니다. NSAID가 이차적인 관절 통증을 완화할 수는 있지만, 이는 증상 완화일 뿐 질병 경과를 바꾸는 효과는 아닙니다.

같은 분석에서 예측된 다른 후보(점수순)는 다음과 같으며, 모두 L5이고 Hold입니다.

| 순위 | 질환 | TxGNN 점수 | 비고 |
|------|------|-----------|------|
| 2 | 단신증-법랑질형성부전 증후군 (brachyolmia-amelogenesis imperfecta syndrome) | 0.9997 | 확립된 기전 없음 |
| 3 | 근경화증 (myosclerosis) | 0.9997 | 기전 연결이 약하고 추측에 가까움 |
| 4 | 단신증 (brachyolmia) | 0.9996 | 확립된 기전 없음 |
| 5 | 가성연골무형성증 (pseudoachondroplasia) | 0.9993 | 증상 완화 수준의 간접 연결만 가능 |
| 6 | 미골 과운동성 (hypermobility of coccyx) | 0.9987 | 통증 완화 목적으로만 임상적 개연성이 있음 |

## 한국 시판 정보

허가 적응증 본문은 확인되지 않았고 허가 문서 링크만 있어, 적응증 열은 생략했습니다. 아래 10건은 모두 단일 성분 제제이며 상태는 유효입니다.

| 허가번호 | 제품명 | 제조사 | 비고 |
|---------|------|------|------|
| 199002184 | 아신돌캡슐200밀리그램 | 케이엠에스제약 | 수출용 |
| 201401037 | 엔터락캡슐 | 마더스제약 | 수출용 |
| 199400681 | 마카나캡슐 | 일화 | 수출용 |
| 201405864 | 엘토스캡슐 | 한국프라임제약 | 수출용 |
| 199302406 | 파비스에토돌락캅셀 | 한국파비스제약 | 수출용 |

위 표는 주요 5건만 나열한 것이며, 나머지 5건(코즈민캡슐, 에토락캡슐, 에토딘캡슐, 페노딘캡슐, 대우에토돌락캅셀)도 유효 허가입니다. 이 중 에토딘캡슐과 대우에토돌락캅셀은 제품명상 수출용 표기가 없습니다. 모든 제품의 제형은 경질캡슐입니다.

## 안전성 고려사항

허가사항의 경고 및 금기 정보는 이번 데이터에 없으므로 허가사항을 참조하세요.

**약물 상호작용** (DDInter 기준, 조회된 100건 중 일부):
- **중등도**: Acetylsalicylic acid, Hydrocortisone, Dexamethasone, Betamethasone, Budesonide, Triamcinolone, Metformin, Glimepiride, Repaglinide, Chlorpropamide, Mesalazine, Balsalazide, Potassium citrate, Potassium bicarbonate, Picosulfuric acid, Polyethylene glycol (전해질 함유 3350)
- **경미**: Famotidine, Ranitidine, Cimetidine, Linaclotide

## 결론 및 다음 단계

**결정: Hold**

**사유:**
6개 예측 후보 모두 직접 뒷받침하는 임상시험과 문헌이 없고, Etodolac의 기전과 연결되는 근거도 없습니다. 높은 점수는 TxGNN 모델(딥러닝)이 산출한 값일 뿐이며, 모델이 관련 질환 사이에서 학습한 유사성을 반영했을 가능성이 있고 생물학적 근거는 아닙니다. 허가 적응증과 안전성 정보도 확인되지 않았습니다.

**진행하려면 필요한 것:**
- 식약처 허가 문서에서 적응증, 경고, 금기 정보 확보 (현재 차단 수준의 데이터 공백)
- DrugBank 등에서 작용 기전(MOA) 확보
- 예측 질환별 임상시험 및 문헌 재검색
- 증상 완화 목적의 활용 가능성이 상대적으로 높은 미골 과운동성부터 우선 검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

