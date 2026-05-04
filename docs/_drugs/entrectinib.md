---
layout: default
title: Entrectinib
parent: 僅模型預測 (L5)
nav_order: 248
evidence_level: L5
indication_count: 10
---

# Entrectinib
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

# Entrectinib: NTRK 융합 양성 고형종양에서 다발성 내분비선종양으로

## 한 문장 요약

Entrectinib은 TRKA/B/C, ROS1, ALK를 표적으로 하는 복합 타이로신 키나제 억제제로, 국제적으로 NTRK 융합 양성 고형종양 및 ROS1+ 비소세포폐암 치료에 승인되어 있습니다.
TxGNN 모델은 **다발성 내분비선종양(Multiple Endocrine Neoplasia, MEN)**에 효과가 있을 수 있다고 예측하나, 현재 MEN에 특이적인 임상시험은 없으며 **1편의 간접 기전 문헌**만이 이 방향을 부분적으로 지지합니다.
기전상 연결고리는 MEN2의 RET 경로를 통한 원거리 간접 추론에 그치며, 직접적인 임상 증거는 아직 없습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 국내 미허가 (국제: NTRK 융합 양성 고형종양 / ROS1+ 비소세포폐암) |
| 예측 신규 적응증 | 다발성 내분비선종양 (Multiple Endocrine Neoplasia) |
| TxGNN 예측 점수 | 98.58% |
| 근거 수준 | L4 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

Entrectinib은 TRKA/B/C, ROS1, ALK 세 가지 수용체 타이로신 키나제를 동시에 억제하는 표적치료제입니다. 종양 내 이 키나제들의 융합 유전자(NTRK1/2/3 융합, ROS1 재배열, ALK 재배열)가 활성화되면 구성적 증식 신호가 발생하며, Entrectinib은 이를 차단하여 항종양 효과를 나타냅니다. 단, 상세한 분자 약리 데이터(MOA)는 이번 Evidence Pack에 포함되지 않았으므로, DrugBank DB11986 및 국제 허가사항을 직접 참조하시기 바랍니다.

다발성 내분비선종양과의 연관성을 살펴보면, MEN은 크게 두 가지로 구분됩니다. **MEN2형**은 RET 원암유전자의 활성화 돌연변이(C634R, M918T 등)에 의해 구동되며 갑상선 수질암·갈색세포종·부갑상선항진증을 동반합니다. Entrectinib은 RET 키나제에 대한 억제 활성(IC₅₀ ~1,000 nM)을 갖고 있으나, 이는 선택적 RET 억제제 Selpercatinib(IC₅₀ ~0.92 nM)보다 약 1,000배 이상 낮은 효능입니다. **MEN1형**은 MEN1 종양억제 유전자 비활성화가 원인으로, TRK/ROS1/ALK 경로와 알려진 병리적 연결고리가 없습니다.

결론적으로, 이 예측은 지식 그래프 내에서 RET 경로 관련 노드가 Entrectinib의 범키나제 프로필과 간접 연결된 데서 비롯한 것으로, 현재로서는 **전임상 수준의 가설**에 해당합니다. MEN2에서 RET 선택적 억제제가 이미 표준치료로 자리잡은 상황을 고려하면, Entrectinib의 추가적 재창출 가치는 제한적입니다.

---

## 임상시험 근거

검색된 2건의 임상시험은 모두 MEN 특이적 설계가 아니며, 연관성 평가 등급 C(비관련 또는 유용한 데이터 없음)로 분류됩니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT04551495](https://clinicaltrials.gov/study/NCT04551495) | Phase 2 | 모집 완료 | 65 | ROSALINE: ROS1+ 침습성 소엽 유방암에서 Entrectinib + 내분비 치료 병용 신보조요법 연구. MEN 적응증과 직접 관련 없음 (등급 C) |
| [NCT03878524](https://clinicaltrials.gov/study/NCT03878524) | Phase 1 | 조기 종료 | 2 | SMMART PRIME: 광범위 정밀의학 적응 플랫폼 연구. 조기 종료(n=2)로 유효한 데이터 없음 (등급 C) |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [38438731](https://pubmed.ncbi.nlm.nih.gov/38438731/) | 2024 | Translational/Mechanistic | NPJ Precision Oncology | RET 구동 암(갑상선 수질암 포함)에서 Selpercatinib/Pralsetinib 치료 후 적응성 내성 기전 분석. 이차 RET 돌연변이 또는 대체 종양유전자 활성화가 내성 원인. Entrectinib의 약한 RET 억제 활성이 MEN2 맥락에서 간접적으로 언급되나, MEN 치료 목표를 직접 지지하지는 않음 |

---

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적치료제 (TRK/ROS1/ALK 선택적 타이로신 키나제 억제제) |
| 골수억제 위험 | 중등도 (호중구감소증·혈소판감소증이 TKI 계열의 알려진 부작용; PTTM 관련 혈소판 감소 사례 보고 있음) |
| 구토 유발성 등급 | 저~중등도 (경구 TKI 특성) |
| 모니터링 항목 | CBC (분획 포함), 간기능 검사, 신기능 검사, 심전도 (QTc 간격 연장 모니터링) |
| 취급 방호 | 허가사항의 경고 및 주의사항을 참조하세요 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
MEN 특이적 임상시험이 전무하고, 유일한 관련 문헌(PMID 38438731)은 RET 내성 기전 연구로 MEN 치료 효능을 직접 지지하지 않습니다. Entrectinib의 RET 억제 활성(IC₅₀ ~1,000 nM)은 기허가 선택적 RET 억제제 대비 현저히 낮아 MEN2에서 충분한 임상 효능을 기대하기 어려우며, MEN1과는 기전적 연결고리 자체가 없습니다.

**📌 추가 참고:** 본 Evidence Pack(TW-DB11986-multi)의 10개 예측 중, **8번 예측 '여성 유방암(Female Breast Carcinoma)'이 근거 수준 L2, "Proceed with Guardrails"**로 훨씬 높은 임상 근거를 보입니다 (Phase 2 임상시험 2건 등급 A 포함 5건, 문헌 7편). NTRK 융합 양성 유방암(분비성 유방암 등)의 경우 Entrectinib이 국제적으로 핵심 치료 후보이므로, 별도 심층 평가를 권장합니다.

**진행하려면 필요한 것:**
- 상세한 작용 기전(MOA) 데이터 수집 (DrugBank API DB11986 조회)
- 국내 허가사항 및 TFDA 仿單(첨부문서) 확보 (차단 데이터 갭 DG001 해소)
- MEN2에서 Entrectinib RET 억제 효능에 관한 전임상(세포주/동물 모델) 데이터 탐색
- 선택적 RET 억제제(Selpercatinib, Pralsetinib)와의 효능 비교 근거 검토
- 여성 유방암 예측(Rank 8)에 대한 별도 재창출 평가 보고서 작성 권장
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

