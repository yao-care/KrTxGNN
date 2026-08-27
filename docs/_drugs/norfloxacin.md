---
layout: default
title: Norfloxacin
parent: 僅模型預測 (L5)
nav_order: 315
evidence_level: L5
indication_count: 10
---

# Norfloxacin
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

# Norfloxacin: 세균 감염증(항균제)에서 다클론성 과점도증후군(Polyclonal Hyperviscosity Syndrome)으로

## 한 줄 요약

Norfloxacin은 평가팩 내 근거 텍스트들을 통해 확인되는 바로는 DNA 이중나선 회전효소(DNA gyrase)/토포이소머라제 IV를 억제하는 **플루오로퀴놀론계 항균제**입니다(단, 정식 승인 적응증 원문 자료는 제공되지 않음). TxGNN 모델은 최상위 순위로 **다클론성 과점도증후군(Polyclonal Hyperviscosity Syndrome)**을 예측(점수 99.70%)했으나, 이를 뒷받침하는 임상시험이나 문헌은 전무하며, 평가팩 자체의 기전 분석에서도 "생물학적 연관성 없음, 지식그래프 임베딩 유사도에 의한 잡음(noise) 가능성"으로 명시되어 있습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 자료 없음 (승인 적응증 원문 미기재; 근거 텍스트상 세균 감염증 치료용 항균제로 확인) |
| 예측 신규 적응증 | 다클론성 과점도증후군 (Polyclonal Hyperviscosity Syndrome) |
| TxGNN 예측 점수 | 99.70% |
| 근거 수준 | L5 (모델 예측만 있음, 실제 연구 없음) |
| 한국 시판 현황 | ✗ 미상시 (허가 없음) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

Norfloxacin의 상세 작용기전(MOA) 데이터는 이번 평가팩에서 확보되지 않았습니다(Data Gap, 심각도 High). 다만 예측 근거 텍스트 전반에서 반복적으로 "Norfloxacin은 플루오로퀴놀론계로 DNA 이중나선 회전효소/토포이소머라제 IV를 억제하는 항균 기전을 가진다"는 설명이 확인되어, 항균 목적의 약물임은 분명합니다.

그러나 최상위 예측 적응증인 다클론성 과점도증후군은 면역글로불린 과다로 인한 혈액 점도 상승 질환으로, 항균 기전과 연결되는 알려진 생물학적 경로가 없습니다. 평가팩의 기전 분석 역시 "TxGNN 高分僅反映知識圖譜嵌入相似性，缺乏生物學支持(TxGNN 고득점은 지식그래프 임베딩 유사도만을 반영하며 생물학적 근거가 부족함)"이라고 명시하고 있어, 이 예측은 현재로서는 기전적 타당성을 인정하기 어렵습니다.

참고로 평가팩에 포함된 10개 예측 후보 중에서는 **10순위 "패혈성 페스트(septicemic plague)"**가 가장 근거 수준이 높습니다(L3, S2, "Research Question"). 동일 계열 약물인 ciprofloxacin·levofloxacin이 FDA Animal Rule(인체 RCT가 윤리적으로 불가능한 경우 동물시험 기반 승인)에 따라 페스트 치료·노출 후 예방에 이미 승인되어 있어, 플루오로퀴놀론 계열 효과(class effect)로서의 생물학적 개연성이 존재합니다. 다만 norfloxacin 자체의 경구 생체이용률·조직 침투도가 기승인 약물과 동등한지는 별도 검증이 필요합니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 관련 문헌이 없습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. 다만 본 약물은 현재 국내(한국) 미상시 상태로 참조 가능한 국내 허가 라벨이 존재하지 않으며, TFDA 등 규제기관의 경고문/금기사항 자료 확보가 Blocking 등급 Data Gap(DG001)으로 지정되어 있어 S1 안전성 초기 평가 단계 진입이 현재 불가능합니다.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
최상위 예측 적응증(다클론성 과점도증후군)은 임상시험·문헌 근거가 전무하고, 평가팩 자체 분석에서도 기전적 연관성이 부정되어 TxGNN 임베딩 유사도에 의한 통계적 잡음일 가능성이 높습니다. 또한 이 약물은 국내 미상시 상태이며 MOA·안전성 자료가 모두 Data Gap(각각 High, Blocking 등급)으로 남아 있어, 어떤 방향으로도 다음 단계(S1 안전성 초기평가) 진입 요건을 충족하지 못합니다.

**진행하려면 필요한 것:**
- TFDA(현지 규제기관) 허가 라벨의 경고문·금기사항 자료 확보 (DG001, Blocking — S1 진입 필수 선행 조건)
- DrugBank 등을 통한 상세 작용기전(MOA) 자료 확보 (DG002, High)
- 다클론성 과점도증후군 방향은 현재 근거 부족으로 추가 조사 우선순위를 낮게 두는 것을 권장
- 대안으로 패혈성 페스트(10순위, L3/S2) 방향을 검토할 경우, norfloxacin의 인체 약동학(경구 생체이용률, 조직 침투도) 자료를 기승인 플루오로퀴놀론(ciprofloxacin, levofloxacin)과 비교 검증 필요
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

