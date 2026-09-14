---
layout: default
title: Tadalafil
parent: 僅模型預測 (L5)
nav_order: 655
evidence_level: L5
indication_count: 8
---

# Tadalafil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# TADALAFIL: 적응증 정보 없음에서 Ambras형 선천성 전신 다모증으로

## 한 문장 요약

TADALAFIL(DrugBank ID: DB00820)은 이번 Evidence Pack에서 기존 적응증 및 작용 기전(MOA) 데이터가 확보되지 않은 상태입니다. TxGNN 모델은 1순위로 **Ambras형 선천성 전신 다모증(Ambras type hypertrichosis universalis congenita)**을 예측했으나, 이를 뒷받침하는 **임상시험 0건, 문헌 0편**으로 순수 모델 점수에만 의존한 결과입니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (미기재) |
| 예측 신규 적응증 | Ambras형 선천성 전신 다모증 (Ambras type hypertrichosis universalis congenita) |
| TxGNN 예측 점수 | 99.98% (rank 799) |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미상장 (시판되지 않음) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. Evidence Pack상 TADALAFIL의 original_moa는 확보되지 않았고, 기존 적응증 정보도 비어 있어 신규 적응증과의 연관성을 판단할 근거 자체가 없습니다.

Repurposing rationale에도 명시되어 있듯이, PDE5 억제와 선천성 전신 다모증 사이에는 생물학적으로 합리적인 연결고리가 확인되지 않으며, 이 예측은 **TxGNN 임베딩 잡음(embedding noise)일 가능성이 높다**고 평가되었습니다. 즉, 이 순위 1위 예측은 기전적으로도, 실증적으로도 뒷받침되지 않는 상태입니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 관련 문헌이 없습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

> ⚠️ 참고: TFDA 공식 첨부문서(경고·금기 사항)가 Blocking 등급 데이터 공백으로 지정되어 있어, 안전성 초기평가(S1) 단계 진입이 불가능한 상태입니다.

---

## 다른 예측 후보 요약 (참고)

이번 Evidence Pack에는 총 8개의 예측 적응증이 포함되어 있으며, 모두 **Hold** 판정을 받았습니다.

| 순위 | 질환명 | TxGNN 점수 | 근거 수준 | 비고 |
|-----|--------|----------|---------|------|
| 1 | Ambras형 선천성 전신 다모증 | 99.98% | L5 | 근거 없음, 노이즈 가능성 |
| 2 | 다모증 | 99.98% | L5 | 근거 없음 |
| 3 | 치주 병변 동반 기형 증후군 | 99.97% | L5 | 문헌 20편이나 모두 TADALAFIL 무관 (질환 키워드만 중복) |
| 4 | Dandy-Walker 기형 동반 증후군 | 99.97% | L5 | 근거 없음 |
| 5 | 고립성 유전성 모발 이상 | 99.96% | L5 | 근거 없음 |
| 6 | 가족성 고립성 속눈썹 과다증 | 99.65% | L5 | 근거 없음 |
| 7 | 척추측만성 심장질환 | 99.43% | L5 | 근거 없음 (폐동맥고혈압 적응증과의 간접 연관성은 있으나 직접 문헌 없음) |
| 8 | 뇌간 조짐 편두통 | 99.08% | **L4** | 문헌 1건은 **치료 효능이 아닌 부작용 사례보고**(TADALAFIL 유발 편두통 조짐) — 안전성 신호이지 적응증 후보 아님 |

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 8개 예측 적응증 전부가 L5(모델 예측만 존재) 또는 실질적으로 효능 근거가 되지 못하는 L4(부작용 사례보고)에 해당하며, 치료적 타당성을 뒷받침하는 임상시험·기전 데이터가 전무합니다.
- 유일하게 문헌이 존재하는 rank 8(편두통 조짐)도 치료 효과가 아닌 **약물 유발 부작용 신호**로, 오히려 안전성 모니터링이 필요한 항목입니다.
- TFDA 경고·금기 정보가 Blocking 등급 공백 상태로, 안전성 초기평가(S1)조차 진행할 수 없습니다.

**진행하려면 필요한 것:**
- TFDA 공식 첨부문서(경고, 금기, DDI) 확보 — Blocking gap 해소 필수
- DrugBank API를 통한 MOA 및 기존 적응증 데이터 보완
- rank 1~7 예측에 대한 최소한의 전임상/기전 문헌 확인, 확인되지 않으면 후보 목록에서 제외 검토
- rank 8(편두통 조짐)은 치료 후보가 아닌 **약물감시(pharmacovigilance) 이슈**로 별도 관리
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

