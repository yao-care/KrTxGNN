---
layout: default
title: Dostarlimab
parent: 僅模型預測 (L5)
nav_order: 231
evidence_level: L5
indication_count: 10
---

# Dostarlimab
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

# Dostarlimab: 자궁내막암에서 난소종양으로

## 한 문장 요약

Dostarlimab은 PD-1을 차단하는 인간화 단클론항체로, FDA에서 불일치 복구 결핍(dMMR)/고빈도 미소부수체 불안정성(MSI-H) 재발성·진행성 자궁내막암 치료제로 승인된 면역 관문 억제제입니다(현재 한국 미허가).
TxGNN 모델은 **난소종양(Ovarian Neoplasm)**에 효과가 있을 수 있다고 예측하며,
현재 **19건의 임상시험**과 **13편의 문헌**이 이 방향을 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 자궁내막암(dMMR/MSI-H) — FDA 승인, 한국 미허가 |
| 예측 신규 적응증 | 난소종양 (Ovarian Neoplasm) |
| TxGNN 예측 점수 | 50% |
| 근거 수준 | L1 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

Dostarlimab은 PD-1(programmed death-1) 수용체를 표적으로 하는 인간화 IgG4 단클론항체입니다. PD-1/PD-L1 신호 축은 종양 세포가 면역 감시를 회피하는 핵심 경로로, dostarlimab이 이를 차단하면 종양 내 침윤 T 세포(TIL)의 기능이 회복되어 항종양 면역 반응이 재활성화됩니다. 이 기전은 RUBY Phase 3 시험을 통해 자궁내막암에서 임상적으로 검증되었으며, 유사한 면역 미세환경을 공유하는 난소암에 직접 적용됩니다.

난소암, 특히 dMMR/MSI-H 아형 및 BRCA 돌연변이 관련 고동종재조합결핍(HRD) 종양에서는 높은 종양 돌연변이 부담(TMB)과 신생항원 풍부성으로 인해 면역치료 반응성이 이론적으로 우수합니다. PARP 억제제(niraparib)와의 병용은 HRD 관련 면역원성 세포 사멸(ICD)을 유도하고 STING 경로를 활성화하여 PD-1 차단의 효과를 증폭시키는 시너지가 여러 Phase 2/3 임상시험을 통해 탐색되고 있습니다.

자궁내막암과 난소암은 부인과계 종양으로서 PD-L1 발현, dMMR 상태, BRCA 변이 등 면역치료 관련 분자 특성을 상당 부분 공유합니다. 자궁내막암에서 확립된 dostarlimab의 임상적 근거는 난소암으로의 적응증 확장을 위한 강력한 생물학적 토대가 되며, NItCHE·FIRST/ENGOT-OV44 등 Phase 3 임상시험이 이를 직접 검증 중입니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT04679064](https://clinicaltrials.gov/study/NCT04679064) | Phase 3 | UNKNOWN | 427 | NItCHE(MITO 33): niraparib + dostarlimab vs 의사선택 화학요법, 백금 재투여 불가 재발 난소·난관·복막암 무작위 대조 시험 |
| [NCT03602859](https://clinicaltrials.gov/study/NCT03602859) | Phase 3 | ACTIVE_NOT_RECRUITING | 1,400 | FIRST/ENGOT-OV44: 1차 치료에서 백금 기반 화학요법 + dostarlimab + niraparib vs 표준치료, Stage III/IV 비점액성 상피성 난소암 |
| [NCT06023862](https://clinicaltrials.gov/study/NCT06023862) | Phase 2 | RECRUITING | 198 | DOVE(APGOT-OV07/ENGOT-ov80): dostarlimab 단독 vs +bevacizumab vs 비백금 화학요법 3개군 무작위 비교, 재발 부인과 투명세포암종 |
| [NCT03651206](https://clinicaltrials.gov/study/NCT03651206) | Phase 2/3 | RECRUITING | 138 | niraparib + dostarlimab vs niraparib 단독 vs 화학요법, 재발 난소·자궁 육종암(국제 다기관 무작위) |
| [NCT03574779](https://clinicaltrials.gov/study/NCT03574779) | Phase 2 | COMPLETED | 77 | OPAL: niraparib ± dostarlimab ± bevacizumab, 재발 난소암 다코호트 우산 연구 (완료) |
| [NCT05065021](https://clinicaltrials.gov/study/NCT05065021) | Phase 2 | UNKNOWN | 40 | Re-VOLVE: PARP 억제제 진행 후 실시간 유전체 내성 평가 기반 dostarlimab 포함 치료 전략 결정 |
| [NCT06065462](https://clinicaltrials.gov/study/NCT06065462) | Phase 1/2 | RECRUITING | 21 | dostarlimab + LB-100(PP2A 억제제) 병용, 난소 투명세포암종 대상 기전 혁신 접근 |
| [NCT02715284](https://clinicaltrials.gov/study/NCT02715284) | Phase 1 | ACTIVE_NOT_RECRUITING | 730 | TSR-042(dostarlimab) 최초 인체 투여 용량 증량 연구, 고형종양 전반 안전성·PK·초기 효능 확립 |
| [NCT04673448](https://clinicaltrials.gov/study/NCT04673448) | Phase 1 | ACTIVE_NOT_RECRUITING | 18 | BRCA 돌연변이 유방·췌장·난소암에서 niraparib + dostarlimab 병용 Phase 1b |
| [NCT03307785](https://clinicaltrials.gov/study/NCT03307785) | Phase 1 | COMPLETED | 60 | niraparib + TSR-042 ± bevacizumab ± 백금 기반 화학요법 용량 탐색, 조합 안전 용량 확립 (완료) |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [40461381](https://pubmed.ncbi.nlm.nih.gov/40461381/) | 2025 | Phase 3 대형 임상 | Ann Oncol | FIRST/ENGOT-OV44: 1차 진행성 난소암에서 dostarlimab + niraparib + 백금 기반 화학요법 병용 효과 평가 |
| [34607820](https://pubmed.ncbi.nlm.nih.gov/34607820/) | 2021 | Phase 3 RCT | Int J Gynecol Cancer | NItCHE(MITO 33): 백금 불가 재발 난소암에서 niraparib + dostarlimab vs 의사선택 화학요법, 무작위 3상 설계 및 근거 |
| [39710508](https://pubmed.ncbi.nlm.nih.gov/39710508/) | 2025 | Phase 2 RCT | J Gynecol Oncol | DOVE: 재발 부인과 투명세포암종에서 dostarlimab ± bevacizumab vs 비백금 화학요법 3개군 무작위 비교 |
| [37890345](https://pubmed.ncbi.nlm.nih.gov/37890345/) | 2023 | Phase 2 | Gynecol Oncol | MOONSTONE/GOG-3032: BRCA 야생형 백금 저항성 재발 난소암에서 niraparib + dostarlimab 효능·안전성·삶의 질 |
| [38754056](https://pubmed.ncbi.nlm.nih.gov/38754056/) | 2024 | Phase 2 | JCO Precis Oncol | OPAL 코호트 A: 전처치 백금 저항성 난소암에서 niraparib + dostarlimab + bevacizumab 3제 병용 결과 보고 |
| [39322611](https://pubmed.ncbi.nlm.nih.gov/39322611/) | 2025 | PRO 분석 | Int J Gynecol Cancer | RUBY 시험 dMMR/MSI-H 하위군: dostarlimab + 화학요법의 무진행생존 개선 및 환자보고결과(삶의 질) |
| [38679402](https://pubmed.ncbi.nlm.nih.gov/38679402/) | 2024 | Review | Crit Rev Oncol Hematol | Dostarlimab 개발 성공 사례 및 주요 임상시험 종합 검토: PD-1/PD-L1 경로 억제, FDA 승인 근거 요약 |
| [35751489](https://pubmed.ncbi.nlm.nih.gov/35751489/) | 2022 | Review | Acta Obstet Gynecol Scand | 부인과암에서 PD-1·CTLA-4 면역관문억제제 임상시험 종합 검토 |
| [37993659](https://pubmed.ncbi.nlm.nih.gov/37993659/) | 2023 | 기초/전환 연구 | Scientific Reports | 전이성 부인과암 TIL의 전 세계 공유 TCR 레퍼토리 분석, PD-L1·BRCA 기반 면역치료 반응 바이오마커 탐색 |
| [35245004](https://pubmed.ncbi.nlm.nih.gov/35245004/) | 2022 | Review | J Gynecol Oncol | 2021년 부인과암 주요 임상 연구 진보 요약 (난소암·자궁경부암 면역치료 포함) |

---

## 세포독성

Dostarlimab은 전통적 세포독성 화학요법이 아닌 면역 관문 억제제(Immune Checkpoint Inhibitor)이며, 항종양제로 분류됩니다.

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 면역치료 — Anti-PD-1 단클론항체 (세포독성 화학요법과 구별) |
| 주요 독성 프로파일 | 면역 관련 이상 반응(irAEs): 내분비 이상(갑상선염·부신기능부전·뇌하수체염), 간독성, 면역 매개 폐렴, 대장염, 신경계 irAE |
| 골수억제 위험 | 저 (단독 투여 기준); niraparib 병용 시 혈소판감소증·호중구감소증 모니터링 필요 |
| 구토 유발성 등급 | 저 |
| 모니터링 항목 | TSH·유리 T4(갑상선), 코르티솔(부신), AST·ALT·빌리루빈(간), 공복혈당·HbA1c(면역 매개 당뇨), CBC, 호흡기 증상 시 폐기능 |
| 취급 방호 | 표준 단클론항체 취급 지침 준수; 전통 세포독성 약물 특별 방호 불필요 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

> **중요 안전성 신호 (문헌 근거):** 2건의 증례 시리즈(PMID [34993356](https://pubmed.ncbi.nlm.nih.gov/34993356/), [40642102](https://pubmed.ncbi.nlm.nih.gov/40642102/))에서 dostarlimab 투여 후 면역 매개 뇌수막뇌염 및 기존 부종양성 소뇌 변성 악화가 보고되었습니다. PD-1 차단에 의한 T 세포 과활성화가 신경계 자가면역 반응을 유발하거나 기존 부종양 증후군을 악화시킬 수 있으므로, 신경계 증상 발생 시 즉각적인 irAE 감별 진단 및 스테로이드 기반 관리 프로토콜 적용이 필요합니다.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
난소종양에 대해 dostarlimab ± niraparib 병용 요법을 평가하는 복수의 Phase 2/3 임상시험이 진행 중이며, NItCHE(N=427)·FIRST/ENGOT-OV44(N=1,400) 등 Phase 3 무작위 대조 시험 설계가 이미 존재하여 근거 수준 L1을 충족합니다. 자궁내막암에서 확립된 dMMR/MSI-H 바이오마커 기반 효능 근거와 공유된 부인과 종양 면역 미세환경을 고려하면, 임상적 진전이 충분히 정당화됩니다.

**진행하려면 필요한 것:**
- DrugBank API를 통한 dostarlimab 상세 MOA 데이터 확보 (DG002 해소)
- 한국 식품의약품안전처(MFDS) TFDA 허가사항 조회 및 irAE 경고·금기 데이터 보완 (DG001 해소)
- irAE 모니터링·관리 프로토콜 수립 (특히 신경계 irAE 조기 식별 및 등급화 포함)
- niraparib 병용 시 혈액독성(혈소판감소증·호중구감소증) 추가 모니터링 계획
- 환자 선택 전략 수립: dMMR/MSI-H 상태, BRCA1/2 변이, HRD 점수 등 예측 바이오마커 기반 선별 기준
- NItCHE(MITO 33) 및 FIRST/ENGOT-OV44 최종 결과 업데이트 지속 추적
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

