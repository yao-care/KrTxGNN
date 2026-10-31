---
layout: default
title: Sulindac
parent: 모델 예측만 (L5)
nav_order: 708
evidence_level: L5
indication_count: 9
monitor_inn: "Sulindac"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "brachyolmia", "myosclerosis", "pseudoachondroplasia", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "WHIM syndrome", "hypermobility of coccyx"]
last_modified_at: 2026-10-31
description: "Sulindac: 예측 신규 적응증 말단중간이형성증 헌터-톰슨형 (근거 수준 L5). 기존 적응증: 확인 불가 (허가 적응증 본문 없이 허가 문서 링크만 제공됨)"
---

# Sulindac
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

## Sulindac: 기존 적응증 정보 미확인에서 말단중간이형성증 헌터-톰슨형으로
{: .text-alpha }

## 한 문장 요약

Sulindac은 비스테로이드성 소염진통제(NSAID)로, 국내에는 단일 성분 허가 1건이 등록되어 있습니다. 다만 이번 보고서용으로 모은 데이터에는 허가 적응증의 본문이 없습니다(문서 링크만 확인됨).
TxGNN 모델은 **말단중간이형성증 헌터-톰슨형(acromesomelic dysplasia, Hunter-Thompson type)**에 효과가 있을 수 있다고 예측하지만, 이를 지지하는 **임상시험은 0건**, **문헌도 0편**입니다. 모델 예측만 있는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (허가 적응증 본문 없이 허가 문서 링크만 제공됨) |
| 예측 신규 적응증 | 말단중간이형성증 헌터-톰슨형 |
| TxGNN 예측 점수 | 0.9992 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 1건 / 전체 1건) |
| 허가증 수 | 1건 (유효 1건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 일반적으로 Sulindac은 COX-1/COX-2를 억제하는 NSAID로 알려져 있으며, 활성 대사체인 sulfide는 Wnt/β-catenin 신호 등 COX와 무관한 작용도 보고되어 있습니다. 다만 이는 이번 데이터에서 확인된 내용이 아니라 일반적인 약리학 지식입니다.

이 질환은 BMP 신호 경로에 속한 GDF5 유전자의 기능 상실 변이로 생기는 골격 이형성증입니다. Sulindac의 약리와 GDF5 결핍을 이어 주는 경로는 현재 데이터로 뒷받침되지 않습니다. 높은 TxGNN 점수는 희귀 골격질환 노드 간의 네트워크 근접성을 반영한 결과일 가능성이 큽니다. 약리학적 타당성을 의미하는 것은 아닙니다.

### 참고: 다른 예측 후보

| 순위 | 질환 | 점수 | 기전 연결성 |
|------|------|------|-----------|
| 2 | 단지증-법랑질형성부전 증후군 | 0.9990 | 확립된 연결 없음 |
| 3 | 단지증(Brachyolmia) | 0.9990 | 확립된 연결 없음 |
| 4 | 근경화증(Myosclerosis) | 0.9989 | 약하고 추측적 (항염 작용 가능성만 있음) |
| 5 | 가성연골무형성증 | 0.9985 | 확립된 연결 없음 |
| 6 | 단지증-합지증 증후군 | 0.9982 | 확립된 연결 없음 |
| 7 | 결손형 소안구증-근위부 단축 이형성 증후군 | 0.9981 | 확립된 연결 없음 |
| 8 | WHIM 증후군 | 0.9974 | 확립된 연결 없음 (CXCR4 길항 작용 없음) |
| 9 | 꼬리뼈 과가동성 | 0.9956 | 간접적·추측적 (NSAID의 대증적 통증 완화) |

9개 후보 모두 임상시험과 문헌이 없습니다. 증상 완화라는 측면에서는 꼬리뼈 과가동성이 가장 그럴듯하지만, 이 역시 예측 단계에 머물러 있습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 197900123 | 크리돌정100밀리그람(설린닥) | 진한 황색의 육각형 필름 코팅정 | 적응증 본문 없음 (허가 문서 링크만 확인됨) |

## 안전성 고려사항

허가사항 중 경고·금기 정보는 이번 데이터에 포함되지 않았으므로, 안전성 정보는 허가사항을 참조하세요.

**약물 상호작용** (DDInter 기준, 총 100건 중 일부 20건 확인)
- **중등도(Moderate)**: Hydrocortisone, Dexamethasone, Betamethasone, Triamcinolone, Budesonide(스테로이드계), Acetylsalicylic acid, Metformin, Glimepiride, Chlorpropamide, Mesalazine, Balsalazide, Potassium citrate, Potassium bicarbonate, Picosulfuric acid, Sodium sulfate, Polyethylene glycol(전해질 포함)
- **경미(Minor)**: Famotidine, Ranitidine, Cimetidine, Linaclotide

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 점수는 매우 높지만 이를 뒷받침하는 임상시험과 문헌이 없고, 기전상 연결도 확인되지 않아 근거 수준은 L5입니다. 또한 허가 적응증과 안전성 정보가 확인되지 않은 상태입니다.

**진행하려면 필요한 것:**
- 허가 적응증 및 경고·금기 정보 확보 (식약처 허가사항 문서를 내려받아 분석)
- 작용 기전(MOA) 데이터 보완 (DrugBank 조회)
- GDF5/BMP 경로와 Sulindac 사이의 연관성에 대한 전임상 근거 탐색
- 해당 질환 대상 임상시험 및 문헌 조사
- 시판 상태(취소 여부) 확인
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

