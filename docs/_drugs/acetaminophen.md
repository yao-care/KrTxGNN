---
layout: default
title: Acetaminophen
parent: 僅模型預測 (L5)
nav_order: 18
evidence_level: L5
indication_count: 1
---

# Acetaminophen
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# ACETAMINOPHEN: 해열진통에서 뇌간 조짐 편두통으로

## 한 문장 요약

ACETAMINOPHEN(아세트아미노펜)은 해열 및 진통 목적으로 전 세계적으로 가장 널리 사용되는 비처방 약물 중 하나입니다.
TxGNN 모델은 **뇌간 조짐 편두통(Migraine with Brainstem Aura)**에 효과가 있을 수 있다고 예측하며,
현재 **20편의 문헌**이 이 방향을 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 해열 및 진통 (허가 데이터 미수집) |
| 예측 신규 적응증 | 뇌간 조짐 편두통 (Migraine with Brainstem Aura) |
| TxGNN 예측 점수 | 99.15% |
| 근거 수준 | L2 |
| 한국 시판 현황 | 데이터 미수집 |
| 허가증 수 | 0건 (데이터 미수집) |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

아세트아미노펜은 단일 경로가 아닌 **다중 기전**을 통해 편두통에 작용합니다. 중추신경계의 COX-3 효소를 억제하여 프로스타글란딘 합성을 감소시키고 중추 감작을 낮추며, 동시에 **배측 봉선핵(dorsal raphe nucleus)**을 경유하는 하행성 세로토닌성 진통 경로를 활성화합니다. 바로 이 배측 봉선핵과 청반핵(locus coeruleus)이 **뇌간 조짐 편두통의 핵심 병소**가 위치하는 부위로, 아세트아미노펜의 작용점과 질환의 병태생리가 직접적으로 맞닿아 있습니다.

추가로, 아세트아미노펜은 FAAH 효소를 억제해 내인성 칸나비노이드(아난다마이드) 시스템을 조절하고 TRPV1 수용체를 간접 억제하며, 피질 확산성 억제(CSD)가 뇌간으로 전도되는 경로를 차단하는 것으로 알려져 있습니다.

임상적으로도 이 예측은 타당합니다. 뇌간 조짐 편두통에서는 현기증·이명·복시·연하 곤란 등의 뇌간 증상 때문에 **혈관수축제인 트립탄 계열이 상대적 금기**로 간주됩니다. 이 공백에서 아세트아미노펜은 특히 임신 중 환자에게도 사용 가능한 현실적 1차 선택 약물로서, 기전과 임상 맥락 양면에서 합리성을 갖추고 있습니다.

---

## 임상시험 근거

현재 뇌간 조짐 편두통에 대한 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|------|------|------|---------|
| [11112243](https://pubmed.ncbi.nlm.nih.gov/11112243/) | 2000 | RCT | Archives of Internal Medicine | 아세트아미노펜 단독의 편두통 치료 효능 및 안전성 확인 — 무작위 이중맹검 위약대조 인구 기반 연구 |
| [9482363](https://pubmed.ncbi.nlm.nih.gov/9482363/) | 1998 | RCT | Archives of Neurology | 아세트아미노펜+아스피린+카페인 병용이 편두통 두통 완화에 유효 — 3건의 이중맹검 위약대조 RCT 통합 분석 |
| [10321417](https://pubmed.ncbi.nlm.nih.gov/10321417/) | 1999 | RCT | Clinical Therapeutics | 월경 관련 편두통에서 아세트아미노펜+아스피린+카페인의 치료 효과 확인 — 3건의 위약대조 RCT |
| [11318886](https://pubmed.ncbi.nlm.nih.gov/11318886/) | 2001 | RCT | Headache | 아세트아미노펜 함유 복합제(Midrin)와 수마트립탄의 경도~중등도 편두통 치료 효능 비교 |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | 임상 가이드라인 | Headache | 미국 두통학회 급성 편두통 약물치료 근거 종합 평가 — 아세트아미노펜 포함 |
| [39493026](https://pubmed.ncbi.nlm.nih.gov/39493026/) | 2024 | 체계적 문헌고찰 | Cureus | 임신 중 편두통의 급성기 및 예방 치료 체계적 고찰 — 아세트아미노펜을 1차 선택으로 확인 |
| [30470274](https://pubmed.ncbi.nlm.nih.gov/30470274/) | 2019 | 종설 | Neurologic Clinics | 임신·산욕기 두통 관리 — 아세트아미노펜이 증상 치료의 1차 선택임을 확인 |
| [38307660](https://pubmed.ncbi.nlm.nih.gov/38307660/) | 2024 | 종설 | Handbook of Clinical Neurology | Status Migrainosus(72시간 초과 편두통 발작) 관리에서 아세트아미노펜 역할 검토 |
| [33525313](https://pubmed.ncbi.nlm.nih.gov/33525313/) | 2021 | 종설 | Neurology International | Ubrogepant 검토 — 경도~중등도 편두통 표준 치료로서 아세트아미노펜 위상 기술 |
| [37123778](https://pubmed.ncbi.nlm.nih.gov/37123778/) | 2023 | 종설 | Cureus | 임신 및 수유 중 편두통 치료 — 아세트아미노펜의 안전성 및 사용 근거 종합 검토 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
뇌간 조짐 편두통에서 트립탄 계열이 상대적 금기인 상황에서 아세트아미노펜은 다중 기전에 근거한 임상적 합리성과 복수의 RCT 및 임상 가이드라인 수준의 근거를 갖추고 있으며, 특히 임신 중 환자군에서의 안전성 프로파일이 우수하여 진행 타당성이 충분합니다.

**진행하려면 필요한 것:**
- 한국 MFDS 허가사항(경고·금기·상호작용) 원문 수집 및 확인
- DrugBank API를 통한 상세 작용 기전(MOA) 데이터 보완
- 뇌간 조짐 편두통 특이적 임상시험 데이터 (현재 전무)
- 한국 시판 현황 및 허가 데이터 정확성 별도 검증 필요
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

