---
layout: default
title: Cemiplimab
parent: 僅模型預測 (L5)
nav_order: 190
evidence_level: L5
indication_count: 10
---

# Cemiplimab
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

# Cemiplimab: 편평세포암(피부/폐)에서 담낭 선편평세포암으로

## 한 문장 요약

Cemiplimab은 anti-PD-1 checkpoint inhibitor로, 국제적으로 피부 편평세포암·기저세포암·비소세포폐암(NSCLC) 등 편평상피 또는 종양돌연변이부담이 높은 암종에 사용되어온 것으로 알려져 있습니다(단, 본 데이터셋에는 공식 MOA·적응증 정보가 확보되지 않음). TxGNN 모델은 **담낭 선편평세포암(Gallbladder Adenosquamous Carcinoma)**에 효과가 있을 수 있다고 예측(점수 99.99%, rank 485)하지만, 현재 이를 뒷받침하는 임상시험과 문헌은 **0건**입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 미확보 (허가 데이터 없음). 예측 근거 텍스트상 국제적으로 피부/폐 편평세포암, 기저세포암 등에 승인된 것으로 언급됨 |
| 예측 신규 적응증 | 담낭 선편평세포암 (Gallbladder Adenosquamous Carcinoma) |
| TxGNN 예측 점수 | 99.99% (rank 485) |
| 근거 수준 | L5 (모델 예측만 존재, 임상시험/문헌 없음) |
| 한국 시판 현황 | 미상 (허가 0건, 미판매) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터(MOA)는 확보되지 않았습니다(Data Gap). 다만 예측 근거 텍스트에 따르면 Cemiplimab은 anti-PD-1 checkpoint inhibitor로, 피부 편평세포암(cutaneous SCC), 기저세포암(BCC), 비소세포폐암(NSCLC) 등 편평상피 분화 또는 고종양돌연변이부담(TMB) 암종에서 이미 사용되고 있는 것으로 언급됩니다.

담낭 선편평세포암(adenosquamous carcinoma)은 명칭 그대로 종양 내 편평상피 분화 성분을 포함하고 있어, 이론적으로 PD-L1을 발현할 가능성이 있습니다. 그러나 이는 조직학적 유사성에 근거한 **기전상 유추**일 뿐이며, 담낭암이라는 특정 적응증에 대한 직접적 임상 근거는 전혀 없습니다.

참고로 동일 예측 배치에는 두경부(성문/성문상부/부비동)·폐·항문·귀·전립선 등 편평세포암 또는 유사 계열 종양 9건이 함께 상위권(rank 485~542)에 올라 있으며, 모두 동일한 "PD-1 억제제 → 편평상피/고TMB 종양" 기전 유추에 기반하고 있어 예측 패턴 자체는 일관되나, 개별 적응증 단위의 실증 근거는 아직 없습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 세포독성

Cemiplimab은 전통적 세포독성 화학요법이 아닌 면역관문억제제(anti-PD-1)로 분류됩니다.

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 면역치료 (anti-PD-1 checkpoint inhibitor) |
| 골수억제 위험 | 저 (checkpoint inhibitor 계열은 전형적 골수억제보다 면역관련 이상반응(irAE)이 특징적. 상세 독성 자료는 확보되지 않아 허가사항 참조 필요) |
| 구토 유발성 등급 | 저 |
| 모니터링 항목 | 갑상선/뇌하수체 등 내분비 기능, 간·신 기능, 폐렴·대장염 등 irAE 관련 증상 (checkpoint inhibitor 계열 일반 특성 기준) |
| 취급 방호 | 생물학적제제(단클론항체) 표준 정맥주사 취급 기준 적용, 세포독성 항암제 전용 방호 조치는 해당 없음 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. (TFDA 경고/금기/DDI 자료 모두 미확보 — DG001은 Blocking 등급으로 S1 안전성 초평가 진행 자체가 불가한 상태입니다.)

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측된 10개 적응증 모두 L5(모델 예측만 존재, 임상시험·문헌 0건) 단계에 머물러 있고, 한국 내 허가 이력도 전무합니다. 특히 TFDA 경고/금기 정보가 Blocking 등급 Data Gap으로 남아있어 안전성 초기 평가(S1) 자체를 진행할 수 없는 상태입니다.

**진행하려면 필요한 것:**
- TFDA 공식 첨부문서 확보 및 파싱 (DG001, Blocking)
- DrugBank API를 통한 공식 MOA/적응증 데이터 확보 (DG002)
- 담낭 선편평세포암 및 기타 상위 9개 후보 적응증에 대한 임상시험/문헌 검색 재실행
- 한국 내 시판·허가 현황 재확인
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

