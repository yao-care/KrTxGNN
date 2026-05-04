---
layout: default
title: Eliglustat
parent: 僅模型預測 (L5)
nav_order: 241
evidence_level: L5
indication_count: 10
---

# Eliglustat
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

# Eliglustat: 고셔병 1형에서 치명적 경과의 선천성 어린선 증후군으로

## 한 문장 요약

Eliglustat(상품명 Cerdelga)은 글루코실세라마이드 합성효소(GCS) 억제제로, 희귀 대사질환인 고셔병 1형 치료에 전 세계적으로 사용되고 있으나 한국에는 아직 허가되지 않은 약물입니다.
TxGNN 모델은 **치명적 경과를 동반한 선천성 어린선 증후군(Autosomal Ichthyosis Syndrome with Fatal Disease Course)**에 효과가 있을 수 있다고 예측하며, 예측 점수는 98.42%에 달합니다.
그러나 현재 이 방향을 지지하는 **임상시험 및 문헌 근거는 전무**하며, 기전적 연관성도 이론적 수준에 머물러 있습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 고셔병 1형 (한국 미허가, 해외 승인) |
| 예측 신규 적응증 | 치명적 경과의 선천성 어린선 증후군 (Autosomal Ichthyosis Syndrome with Fatal Disease Course) |
| TxGNN 예측 점수 | 98.42% |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 데이터 갭으로 분류되어 있습니다. 알려진 정보에 따르면, Eliglustat은 글루코실세라마이드 합성효소(GCS, glucosylceramide synthase)를 경쟁적으로 억제하여 리소좀 내 글루코실세라마이드 축적을 감소시키는 기전으로 고셔병 1형에 효과를 나타냅니다. 이 기전은 스핑고지질(sphingolipid) 대사 경로 전반에 영향을 미칩니다.

일부 선천성 어린선병은 세라마이드 대사 결함과 연관성이 알려져 있습니다. 대표적으로 ABCA12 유전자 돌연변이는 각질층 지질 장벽을 구성하는 세라마이드 분포를 방해하여 중증 어린선(예: Harlequin ichthyosis)을 유발합니다. 이론적으로 GCS 억제를 통한 스핑고지질 대사 균형 조정이 피부 장벽 기능에 영향을 미칠 수 있다는 가설을 구성할 수 있습니다.

그러나 치명적 경과를 동반하는 상염색체 어린선 증후군과 Eliglustat의 GCS 억제 기전 간의 구체적인 병태생리적 연결고리는 현재까지 확립되어 있지 않습니다. TxGNN의 높은 예측 점수는 지식 그래프 내 스핑고지질–피부 장벽 경로 간 간접적 노드 연결에서 비롯된 것으로 추정되며, **기전 가설 강도: 낮음(간접적)**으로 평가됩니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 관련 문헌이 없습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
전체 상위 10개 예측 적응증 모두 임상시험 및 문헌 근거가 전무하고(근거 수준 L5), TxGNN 모델 예측만 존재합니다. 기전적 연관성은 간접적·이론적 수준에 머물며, 한국에서는 원래 적응증(고셔병 1형)조차 미허가 상태로 재창출 전에 원래 적응증의 허가 타당성을 먼저 검토해야 합니다.

**진행하려면 필요한 것:**
- Eliglustat 상세 작용 기전(MOA) 보완 — DrugBank API 및 허가 기관 자료 조회 필요
- 한국 허가 경로 및 안전성 데이터(MFDS 또는 FDA/EMA 허가 기관 자료) 확보
- 치명적 경과 어린선 증후군에서 GCS 억제 관련 전임상(세포·동물) 연구 탐색
- 스핑고지질-피부 장벽 경로 교차 연구 문헌 검토 (기전 가설 강도 상향 가능 여부 평가)
- 해당 희귀질환 환자 레지스트리 또는 자연경과 연구 데이터 검토
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

