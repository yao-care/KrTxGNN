---
layout: default
title: Gefitinib
parent: 僅模型預測 (L5)
nav_order: 343
evidence_level: L5
indication_count: 10
---

# Gefitinib
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

# Gefitinib: 비소세포폐암(NSCLC)에서 치은섬유종증으로

## 한 문장 요약

Gefitinib은 한국 허가·원 적응증 데이터가 Evidence Pack에 없으나(Data Gap), 첨부 문헌에서는 일관되게 EGFR 티로신 키나제 억제제(EGFR-TKI)로서 비소세포폐암(NSCLC) 치료에 사용되는 약물로 기술됩니다. TxGNN 모델은 **치은섬유종증(Fibromatosis, Gingival)**에 효과가 있을 수 있다고 예측했으나, 현재 이를 지지하는 **임상시험이나 문헌이 전혀 없습니다**.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 한국 허가 정보 없음 (문헌 기준: 비소세포폐암, NSCLC) |
| 예측 신규 적응증 | 치은섬유종증 (Fibromatosis, Gingival) |
| TxGNN 예측 점수 | 99.89% |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미판매 (시판되지 않음) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터(공식 MOA 필드)는 확보되지 않았습니다(Data Gap). 다만 Evidence Pack에 포함된 문헌들(예: PMID 24794908, 12841190, 23140355)은 gefitinib을 EGFR을 표적하는 티로신 키나제 억제제로, 화학저항성 비소세포폐암 환자 치료에 임상적으로 사용된다고 일관되게 기술하고 있습니다.

치은섬유종증(gingival fibromatosis)은 잇몸 조직의 섬유성 과증식을 특징으로 하는 희귀 질환으로, EGFR 신호전달 억제와의 기전적 연관성이 문헌상 확인되지 않습니다. 실제로 해당 예측에는 뒷받침하는 임상시험도, 문헌도 전혀 존재하지 않으며, 원 데이터의 rationale에서도 "TxGNN 모델의 고점수 예측일 뿐, 외부 검증 근거가 없는 noise match"로 명시하고 있습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 세포독성

Gefitinib은 문헌상 EGFR 표적치료제(EGFR-TKI)로 분류되는 항종양약입니다.

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적치료제 (EGFR 티로신 키나제 억제제) — 문헌 근거 |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 문헌상 보고된 이상반응 기준: QT 간격 연장(PMID 34474028, 37258113), 간질성 폐질환(PMID 20942679, 20949670, 22076388), 피부 독성(PMID 18931563, 16489842), 심장독성(PMID 21184253, 19734999) — 심전도, 흉부영상, 피부상태 모니터링 권장 |
| 취급 방호 | 경구용 표적항암제로, 세포독성 약물 취급 규정 준수 권장 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
치은섬유종증에 대한 예측은 TxGNN 모델 점수만 존재할 뿐, 이를 뒷받침하는 임상시험이나 문헌이 전무합니다(L5). 기전적 연관성도 확인되지 않아 현시점에서 진행 근거가 부족합니다.

**진행하려면 필요한 것:**
- TFDA(대만) 허가사항 상 경고/금기 정보 확보 — 현재 Blocking 등급 Data Gap으로 안전성 초기 평가(S1) 진입 불가
- 공식 작용 기전(MOA) 데이터 확보 (DrugBank API 조회)
- 치은섬유종증-EGFR 경로 간 기전적 타당성을 뒷받침할 전임상/기전 연구
- (참고) 본 Evidence Pack에는 근거 수준이 상대적으로 높은 후보도 존재합니다 — lung hilum carcinoma, lung germ cell tumor (모두 L3/S1, Research Question 단계). 이들은 별도 검토를 권장합니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

