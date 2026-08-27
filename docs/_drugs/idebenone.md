---
layout: default
title: Idebenone
parent: 僅模型預測 (L5)
nav_order: 309
evidence_level: L5
indication_count: 10
---

# Idebenone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Idebenone: 기존 적응증 미상에서 간성 포르피린증(Hepatic Porphyria)으로

## 한 문장 요약

Idebenone은 DrugBank(DB09081)에 등록된 약물이나, 국내 허가 및 원 적응증(original indication) 데이터가 현재 확보되지 않은 상태입니다.
TxGNN 모델은 **간성 포르피린증(Hepatic Porphyria)**에 효과가 있을 수 있다고 예측하지만, 이를 뒷받침하는 임상시험이나 문헌은 현재 전혀 없으며, 모델 예측 단독 근거(L5)에 그칩니다. 이 예측을 포함해 총 10건의 후보 적응증이 도출되었으나 전부 동일한 근거 수준(L5)·의사결정 단계(S0)입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정보 없음 (원 적응증 데이터 미확보) |
| 예측 신규 적응증 | 간성 포르피린증 (Hepatic Porphyria) |
| TxGNN 예측 점수 | 99.92% |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미상시 (국내 허가증 없음) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 Idebenone의 상세한 작용기전(MOA) 데이터가 확보되어 있지 않습니다 (DrugBank API 재조회 필요). 국내 허가 이력도 없어 원 적응증 정보 역시 확인되지 않습니다.

TxGNN이 제시한 기전적 근거(repurposing rationale)에 따르면, 간성 포르피린증과의 연결고리는 Idebenone이 가진 것으로 알려진 미토콘드리아 전자전달계 지지 및 항산화 작용에 기반한 **이론적 추론**입니다. 즉, 포르피린증 관련 간세포 산화 스트레스·미토콘드리아 기능 이상을 완화할 가능성이 있다는 가설이나, 포르피린증의 주요 병인은 heme 합성효소(주로 ALA synthase 경로) 결핍이며, 전자전달계 조절과의 직접적 인과관계는 규명된 바 없습니다.

정리하면 이 예측은 순수히 지식그래프 기반 추론(L5, 모델 예측만 존재)이며, 실제 임상 또는 전임상 근거는 전혀 없는 상태입니다. 참고로 함께 도출된 나머지 9건의 후보(portal hypertension, portal vein thrombosis, copper-associated cirrhosis 등 간 관련 질환 다수, 그리고 면역성 근염 계열 질환들) 역시 대부분 "간 질환 노드 군집 효과"로 추정되는 간접적 연관성에 그치며, 4순위(idiopathic copper-associated cirrhosis)가 상대적으로 기전 합리성이 가장 높고, 8순위(희귀 유전 증후군)는 지식그래프 노이즈일 가능성이 높다고 평가되었습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

Idebenone은 국내 미상시 상태이며, 등록된 허가증이 없어 제시할 허가 목록이 없습니다.

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
간성 포르피린증에 대한 예측은 모델 추론(L5)만 존재하며 임상시험·문헌·전임상 근거가 전무합니다. 또한 안전성 정보(경고·금기) 확보가 차단(Blocking) 등급 데이터 갭으로 지정되어 있어, 안전성 초기 평가(S1) 단계 진입 자체가 불가능한 상태입니다.

**진행하려면 필요한 것:**
- 국내(또는 원산지) 규제기관 첨부문서(라벨) 확보 및 경고/금기 사항 파싱 (DG001, Blocking — S1 진입 필수 선행 조건)
- DrugBank API를 통한 작용기전(MOA) 데이터 확보 (DG002, High — 기전 연관성 분석에 필요)
- 간성 포르피린증 관련 전임상/사례 보고 문헌의 지속적 모니터링 (현재 0건)
- 10건 후보 중 상대적으로 기전 합리성이 높은 4순위(idiopathic copper-associated cirrhosis)를 우선 추적 대상으로 검토
- 8순위(희귀 유전 증후군) 등 기전 연관성이 낮은 후보는 우선순위에서 제외 검토
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

