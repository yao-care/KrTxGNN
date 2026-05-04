---
layout: default
title: Deferasirox
parent: 僅模型預測 (L5)
nav_order: 200
evidence_level: L5
indication_count: 5
---

# Deferasirox
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

# Deferasirox: 만성 철분 과부하에서 HIV 감염증으로

## 한 문장 요약

Deferasirox는 경구용 철 킬레이터(iron chelator)로, 수혈 의존성 빈혈 환자의 만성 철분 과부하 치료에 사용되는 약물입니다.
TxGNN 모델은 **HIV 감염증(HIV infectious disease)**에 효과가 있을 수 있다고 예측하며,
현재 **임상시험 0건**과 **문헌 2편**이 이 방향과 관련되어 있습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 만성 철분 과부하 (수혈 의존성 빈혈) |
| 예측 신규 적응증 | HIV 감염증 (HIV infectious disease) |
| TxGNN 예측 점수 | 99.40% |
| 근거 수준 | L4 |
| 한국 시판 현황 | ✗ 미등록 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 부재합니다. 알려진 정보에 따르면, Deferasirox는 경구 투여 가능한 트리아졸계 철 킬레이터로, 3가 철이온(Fe³⁺)과 고선택적으로 결합하여 담즙 및 소변으로 배설시킴으로써 조직 내 철분 과부하를 감소시킵니다.

HIV와 철분 대사의 연관성은 세포 수준 연구에서 일부 제안되고 있습니다. PMID 34550543 연구에 따르면, 내솔라이소좀 내 철분(endolysosomal iron)이 HIV-1 Tat 단백질의 올리고머화를 촉진하여 LTR 전사 활성화를 억제하는 것으로 나타났습니다. 이론적으로 Deferasirox에 의한 세포 내 유리 철분 감소가 이 균형에 영향을 미칠 가능성이 있습니다.

그러나 이 기전은 **양방향성**을 가져 해석이 복잡합니다. 세포 내 철분 감소는 바이러스 복제에 필요한 핵산 환원효소(ribonucleotide reductase) 활성을 저하시켜 복제를 억제할 수도 있지만, 동시에 Tat 단백질에 대한 철분의 억제 효과를 해제하여 LTR 전사를 오히려 촉진할 위험도 있습니다. 현재 문헌은 모두 기초과학 수준에 불과하며, 임상적 방향성은 불명확합니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [34550543](https://pubmed.ncbi.nlm.nih.gov/34550543/) | 2021 | 기초과학 (분자 기전 연구) | Journal of Neurovirology | 내솔라이소좀 철분이 HIV-1 Tat 올리고머화를 촉진하여 LTR 전사 활성화를 억제함; 세포 내 철분 상태가 HIV 복제를 조절하는 기전을 시사 |
| [16529348](https://pubmed.ncbi.nlm.nih.gov/16529348/) | 2006 | 약물 개요 (Drug Overview) | J Am Pharmacists Assoc | Deferasirox를 포함한 신약(ramelteon, tipranavir, nepafenac) 약리 및 임상 특성 개요 기술 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
HIV 감염증에 대한 Deferasirox의 적용 근거는 현재 기초과학 수준의 분자 기전 연구 2편에만 기반하며, 임상시험이 전무합니다. 더욱이 제안된 기전 자체가 양방향적이어서 치료 효과보다 HIV 전사를 촉진할 이론적 위험도 배제할 수 없습니다.

**진행하려면 필요한 것:**
- 작용 기전(MOA) 데이터 확보 — DrugBank API 조회를 통한 상세 기전 문서화
- 한국 허가 안전성 정보(경고, 금기, DDI) 수집 — 허가사항 PDF 해석 필요
- HIV 환자 대상 세포 및 동물 모델 전임상 연구 — 철분 감소 시 HIV 복제 억제 vs. 전사 촉진 중 어느 방향이 우세한지 기전 방향성 명확화
- 기전 방향성이 긍정적으로 확인될 경우 Phase 1/2 탐색 임상시험 설계 검토
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

