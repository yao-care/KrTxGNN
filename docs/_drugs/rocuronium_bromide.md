---
layout: default
title: Rocuronium Bromide
parent: 僅模型預測 (L5)
nav_order: 286
evidence_level: L5
indication_count: 0
---

# Rocuronium Bromide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Rocuronium Bromide: 재창출 평가 — 데이터 보완 필요

## 한 문장 요약

Rocuronium Bromide는 신경근 차단제(Non-depolarizing Neuromuscular Blocking Agent)로, 전신마취 시 기관내삽관 및 수술 중 근이완 목적으로 전 세계적으로 사용되는 약물입니다.
이번 Evidence Pack에는 TxGNN 예측 적응증 데이터가 포함되어 있지 않아 재창출 후보 평가를 완료할 수 없으며, 핵심 데이터 수집 후 재평가가 필요합니다.
현재 임상시험 근거, 문헌 근거, 한국 허가 정보 모두 미확보 상태입니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 미확보 (한국 허가 데이터 수집 필요) |
| 예측 신규 적응증 | TxGNN 예측 미실행 |
| TxGNN 예측 점수 | 해당 없음 |
| 근거 수준 | L5 (모델 예측 데이터 없음) |
| 한국 시판 현황 | 데이터 오류 의심 — 未上市로 기재되었으나 재확인 필요 |
| 허가증 수 | 0건 (데이터 미수집) |
| 권장 결정 | Hold |

> ⚠️ **데이터 무결성 경고**: Rocuronium Bromide는 전 세계 주요국에서 허가된 마취보조제입니다. 한국 시판 현황이 "未上市(미시판)"로 기재된 것은 MFDS 데이터 수집 미완료에 의한 오류일 가능성이 높습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 적응증 데이터가 존재하지 않고, 작용 기전(MOA), 한국 규제 허가 현황, 안전성 경고·금기 데이터가 모두 누락되어 재창출 가능성에 대한 의미 있는 평가를 수행할 수 없습니다.

**진행하려면 필요한 것:**
- **[필수 - Blocking]** TxGNN 모델에 Rocuronium Bromide를 입력하여 예측 적응증 및 점수 생성
- **[필수 - Blocking]** MFDS(식품의약품안전처) 허가 데이터 재수집 — 국내 시판 여부 및 허가 적응증 확인
- **[높음]** DrugBank API를 통한 DrugBank ID 매핑 및 MOA 데이터 수집 (현재 `drugbank` 쿼리는 성공했으나 ID가 미매핑 상태)
- **[높음]** MFDS 허가사항(경고·금기) PDF 파싱을 통한 안전성 데이터 확보
- **[참고]** Rocuronium Bromide의 약리학적 특성상 재창출 후보군은 중추신경계 또는 면역·염증 관련 적응증일 가능성이 있으나, 이는 TxGNN 예측 후 검토 요망
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

