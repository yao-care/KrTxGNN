---
layout: default
title: Tenecteplase
parent: 僅模型預測 (L5)
nav_order: 665
evidence_level: L5
indication_count: 10
---

# Tenecteplase
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

Using superpowers 체크 결과 이 작업은 정의된 프롬프트 템플릿을 그대로 따르는 보고서 생성 작업이라 별도 skill 불필요 — 바로 작성합니다.

---

# Tenecteplase: 급성 심근경색(STEMI)에서 후측벽 심근경색(Posterolateral MI)으로

## 한 문장 요약

Tenecteplase는 fibrin-specific 혈전용해제(t-PA 변이체)로, 근거 자료 내 반복적으로 언급되는 기전 설명에 따르면 기존에 **급성 ST분절 상승 심근경색(STEMI)** 혈전용해 치료와 연관되어 있습니다. TxGNN 모델은 **후측벽 심근경색(Posterolateral Myocardial Infarction)**에 대해 99.87%의 예측 점수를 부여했으나, 이는 STEMI의 해부학적 아형 분류에 가까워 **지지하는 임상시험이나 문헌이 전혀 없는(L5)** 순수 모델 예측입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정보 없음 (한국 허가 자료 없음). 근거 자료 내 기전 설명상 급성 심근경색(STEMI) 혈전용해와 연관 |
| 예측 신규 적응증 | 후측벽 심근경색 (Posterolateral Myocardial Infarction) |
| TxGNN 예측 점수 | 99.87% |
| 근거 수준 | L5 (모델 예측만 있음, 실제 연구 없음) |
| 한국 시판 현황 | ✗ 미판매 (허가 없음) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

DrugBank의 구조화된 작용 기전(MOA) 필드는 현재 데이터 공백(DG002, High severity) 상태입니다. 다만 근거 자료의 예측 근거(rationale) 설명에 따르면, Tenecteplase는 fibrin-specific 재조합 조직 플라스미노겐 활성제(t-PA 변이체)로서 관상동맥 혈전을 용해하는 기전을 가지며, 이는 STEMI 치료와 기전적으로 높은 연관성이 있다고 기재되어 있습니다.

그러나 예측된 "후측벽 심근경색"은 독립된 질병이 아니라 **심근경색의 해부학적 위치에 따른 아형 분류**입니다. 즉 기존 적응증과 예측 신규 적응증이 사실상 같은 질병 범주에 속하며, 진정한 의미의 "재창출(repurposing)"이라기보다 TxGNN 지식그래프 상의 인접 노드 예측에 가깝습니다. 이 아형을 별도로 뒷받침하는 임상시험이나 문헌이 전혀 확인되지 않아, 기존 MI 치료 대비 우위를 판단할 근거가 없습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 점수는 높지만(99.87%), 지지하는 임상시험·문헌이 전무하고 예측 적응증이 기존 적응증(STEMI)의 해부학적 아형에 불과해 독립적인 임상적 의미를 판단할 수 없습니다. 또한 한국 내 허가 및 안전성 자료(TFDA 라벨/경고, DG001, Blocking)가 확보되지 않아 S1 안전성 초기 평가 단계에도 진입할 수 없는 상태입니다.

**진행하려면 필요한 것:**
- TFDA(관할 규제기관) 라벨의 경고·금기사항 확보 (DG001, Blocking)
- DrugBank API를 통한 공식 작용 기전(MOA) 데이터 확보 (DG002)
- 후측벽 심근경색 아형에 특이적인 임상 근거 확보 여부 확인

**참고:** 동일 근거 팩 내 5순위 후보인 "coronary stenosis"(관상동맥 협착)는 완료된 Phase 2 RCT(NCT00604695, ICE-T)와 관련 코호트 문헌을 보유해 L2/S2 단계로 평가되며, 별도 보고서로 다룰 가치가 있는 더 실질적인 신호입니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

