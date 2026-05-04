---
layout: default
title: Etonogestrel
parent: 僅模型預測 (L5)
nav_order: 260
evidence_level: L5
indication_count: 5
---

# Etonogestrel
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Etonogestrel: 피임에서 무월경으로

---

## 한 문장 요약

Etonogestrel은 Implanon/Nexplanon으로 알려진 피하 이식형 피임제의 활성 성분으로, 원래 피임 목적으로 사용됩니다.
TxGNN 모델은 **무월경(Amenorrhea)**에 효과가 있을 수 있다고 예측하며,
현재 **1건의 완료된 Phase 3 임상시험**과 **1편의 관련 문헌**이 이 방향을 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 피임 (Implanon 피하 이식형 피임제) |
| 예측 신규 적응증 | 무월경 (Amenorrhea) |
| TxGNN 예측 점수 | 99.84% |
| 근거 수준 | L2 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

Etonogestrel은 합성 프로게스틴(황체호르몬 유사체)으로, 황체호르몬 수용체(PR)에 강력하게 결합하여 LH 급등(LH surge)을 99% 이상 억제함으로써 배란을 차단합니다. 이 강력한 황체호르몬 활성은 자궁내막에 위축성 변화를 유발하여 월경이 소실되는 무월경(amenorrhea)으로 이어집니다. 이는 피임 작용의 부가적 효과이자, 이미 약리학적으로 충분히 입증된 현상입니다.

Implanon 사용자 중 약 20~30%가 삽입 후 1년 이내에 무월경을 경험하는 것으로 보고되어 있습니다. 이를 근거로 자궁내막증(endometriosis)이나 중증 생리통 관리 등의 상황에서 '치료적 무월경 유도(therapeutic amenorrhea induction)' 목적으로 활용될 수 있다는 논의가 이어지고 있습니다.

다만 현재 등록된 임상시험은 피임 효능(Pearl Index)을 주요 평가변수로 설계되어 있으며, 무월경은 이차 평가변수(secondary endpoint)로 다루어지고 있습니다. 무월경 자체를 독립적인 치료 적응증으로 접근한 연구는 아직 제한적이므로, 기전적 타당성과 임상 설계 간의 간극을 고려해야 합니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT04626596](https://clinicaltrials.gov/study/NCT04626596) | Phase 3 | 완료 | 498 | Etonogestrel 피하 이식 피임제(MK-8415)의 허가 3년 이후 4~5년차 확장 사용 시 피임 효능 및 안전성 평가. 무월경은 주요 이차 평가변수로 포함되어 있으며, 데이터 품질 높음 |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [10549446](https://pubmed.ncbi.nlm.nih.gov/10549446/) | 1999 | RCT | Contraception | 단일 이식봉(Implanon) vs 6캡슐(Norplant) 피임 이식제 무작위 다기관 비교 연구(중국, 여성 200명). 피임 효능 동등, 출혈 양상 및 무월경 발생률 직접 보고. Implanon 군에서 무월경 비율 확인 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
Etonogestrel의 황체호르몬 수용체(PR) 결합을 통한 무월경 유도 기전은 약리학적으로 명확히 확립되어 있으며, 완료된 Phase 3 임상시험(n=498)이 관련 근거를 제공합니다. 다만 무월경이 독립적인 주요 평가변수가 아닌 이차 결과로만 측정되었고, 한국 내 미시판 상태임을 고려하여 조건부 진행을 권장합니다.

**진행하려면 필요한 것:**
- 작용 기전(MOA) 상세 데이터 확보 (DrugBank API 조회)
- 한국 식약처(MFDS) 허가사항 및 안전성 정보 확보
- 무월경 자체를 주요 평가변수로 설정한 독립적 임상시험 문헌 추가 탐색 (자궁내막증·생리통 적응증 관련)
- 한국 내 시판 허가 전략 수립 (현재 허가증 없음)

---

> **면책 고지**: 본 보고서는 연구 참고 목적으로만 작성되었습니다. 이 내용은 의료 조언을 구성하지 않으며, 모든 약물 재창출 후보는 임상 검증 이후에만 적용될 수 있습니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

