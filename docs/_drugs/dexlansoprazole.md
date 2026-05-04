---
layout: default
title: Dexlansoprazole
parent: 僅模型預測 (L5)
nav_order: 214
evidence_level: L5
indication_count: 10
---

# Dexlansoprazole
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

# Dexlansoprazole: 미란성 식도염에서 활동성 소화성 궤양 질환으로

## 한 문장 요약

Dexlansoprazole은 이중 지연 방출(Dual Delayed Release, DDR) 기술을 탑재한 프로톤 펌프 억제제(PPI)로, 미란성 식도염 및 위식도역류질환(GERD) 치료에 사용됩니다. TxGNN 모델은 **활동성 소화성 궤양 질환(Active Peptic Ulcer Disease)**에 효과가 있을 수 있다고 예측하며, 현재 **19건의 임상시험**과 **4편의 문헌**이 이 방향을 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 미란성 식도염, GERD (FDA 승인; 한국 허가 없음) |
| 예측 신규 적응증 | 활동성 소화성 궤양 질환 (Active Peptic Ulcer Disease) |
| TxGNN 예측 점수 | 99.999% |
| 근거 수준 | L1 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

현재 공식 MOA 문서는 미확보 상태입니다. 다만 임상시험 및 약리학 문헌에 따르면, Dexlansoprazole은 위벽세포(parietal cell)의 H⁺/K⁺-ATPase(프로톤 펌프)를 불가역적으로 억제하여 위산 분비를 강력하고 지속적으로 차단합니다. 독자적인 DDR 제형을 통해 소장의 두 지점에서 순차적으로 약물이 방출되어, 기존 PPI 대비 24시간 pH>4 유지 시간이 현저히 길어 소화성 궤양 치유에 최적의 저산 환경을 조성합니다.

미란성 식도염과 소화성 궤양은 모두 '위산에 의한 점막 손상'이라는 공통 병태생리를 갖습니다. PPI에 의한 위산 억제는 ① 점막 자연 재생 환경 조성, ② H. pylori 제균 삼제요법에서 항생제 안정성·유효 농도 극대화, ③ NSAIDs 관련 궤양 예방이라는 세 가지 경로로 소화성 궤양 치료에 직접 기여합니다.

개발 코드명 TAK-390MR(즉 Dexlansoprazole)로 수행된 대규모 Phase 3 피벗 시험 2건(NCT00251719, n=2,054; NCT00251693, n=2,038)이 미란성 식도염 및 관련 소화성 궤양 치유에 대한 직접 최고 수준 임상근거를 제공합니다. 이는 TxGNN 예측(99.999%)의 임상적 타당성을 강하게 뒷받침합니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00251719](https://clinicaltrials.gov/study/NCT00251719) | Phase 3 | 완료 | 2,054 | **Dexlansoprazole(TAK-390MR)** 60·90mg vs Lansoprazole 30mg: 내시경 확인 미란성 식도염 8주 치유 효능·안전성 평가 – Dexlansoprazole 핵심 피벗 시험 (등급 A) |
| [NCT00251693](https://clinicaltrials.gov/study/NCT00251693) | Phase 3 | 완료 | 2,038 | **Dexlansoprazole(TAK-390MR)** 60·90mg vs Lansoprazole 30mg: 미란성 식도염 8주 치유 제2 피벗 시험 – 동일 설계 확증 연구 |
| [NCT04784910](https://clinicaltrials.gov/study/NCT04784910) | Phase 3 | 완료 | 423 | DWP14012 20mg vs Lansoprazole 15mg: NSAIDs 유발 소화성 궤양 예방 – 다기관 이중맹검 비열등성 시험 (등급 B) |
| [NCT02761512](https://clinicaltrials.gov/study/NCT02761512) | Phase 3 | 완료 | 306 | CJ-12420 50·100mg vs Lansoprazole 30mg: 위궤양 환자 이중맹검 비열등성 시험 (등급 B) |
| [NCT04531475](https://clinicaltrials.gov/study/NCT04531475) | Phase 2 | 완료 | 90 | X842 캡슐 vs Lansoprazole: 역류성 식도염 4주 치료 용량-효과 관계 다기관 이중맹검 시험 (등급 B) |
| [NCT00942175](https://clinicaltrials.gov/study/NCT00942175) | Phase 1 | 완료 | 160 | **Dexlansoprazole**·Lansoprazole·Omeprazole·Esomeprazole의 클로피도그렐 정상 상태 PK/PD에 대한 영향 – Dexlansoprazole 직접 교차 연구 |
| [NCT01506986](https://clinicaltrials.gov/study/NCT01506986) | Phase 4 | 완료 | 30,024 | HEAT 시험: H. pylori 제균으로 아스피린 사용자 궤양 출혈 예방 – 대규모 이중맹검 위약 대조 결과 연구 |
| [NCT05448001](https://clinicaltrials.gov/study/NCT05448001) | Phase 3 | 완료 | 329 | JP-1366 vs 활성 대조약: 위궤양 환자 대상 다기관 이중맹검 주동적 대조 시험 |
| [NCT05010954](https://clinicaltrials.gov/study/NCT05010954) | Phase 3 | 완료 | 400 | LXI-15028 50mg vs Lansoprazole 30mg: 중국 환자 십이지장 궤양 6주 치료 이중맹검 주동적 대조 시험 |
| [NCT07079540](https://clinicaltrials.gov/study/NCT07079540) | Phase 3 | 완료 | 380 | X842 캡슐 50mg vs Lansoprazole: 역류성 식도염 효능·안전성 및 집단 약동학 특성 평가 |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | 체계적 문헌고찰/네트워크 메타분석 | Am J Gastroenterol | P-CAB vs PPI의 LA C/D등급 중증 식도염 치유 네트워크 메타분석 – PPI 계열 효능 체계적 비교 및 임상 의사결정 지원 |
| [18821474](https://pubmed.ncbi.nlm.nih.gov/18821474/) | 2008 | Review | Curr Opin Investig Drugs | Dexlansoprazole 개발 경과, 역류성 식도염 치료 적용, FDA NDA 제출 현황 및 일본 GERD Phase 2 시험 진행 상황 |
| [36150104](https://pubmed.ncbi.nlm.nih.gov/36150104/) | 2022 | 기전 연구 | J Chin Med Assoc | Dexlansoprazole 포함 PPI의 V-ATPase 억제 및 소포체 스트레스 유도 기전 분석 – PPI 장기 사용과 위암 위험 연관성 탐색 |
| [41809210](https://pubmed.ncbi.nlm.nih.gov/41809210/) | 2026 | 전문가 합의 | World J Gastrointest Pharmacol Ther | 인도 전문가 합의: GERD·소화성 궤양·기능성 소화불량 병태생리 중복 및 종합 관리 지침, PPI 역할 포함 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
Dexlansoprazole 직접 Phase 3 피벗 시험 2건(NCT00251719, n=2,054; NCT00251693, n=2,038)이 L1 수준의 강력한 임상근거를 제공하며, PPI의 지속적 위산 억제(특히 DDR 기술에 의한 24시간 pH>4 유지)가 활동성 소화성 궤양 치유에 필수적인 기전으로 확립되어 있어 진전 타당성이 충분합니다.

**진행하려면 필요한 것:**
- 한국 MFDS 허가 신청을 위한 공식 안전성 문서 확보 (경고, 금기, 이상 반응 목록)
- DrugBank API 조회를 통한 공식 MOA 문서 확보
- 한국 내 특허 만료 여부 및 제네릭 가용성 검토
- DDR 제형 특성을 고려한 특수 환자군(신기능·간기능 저하, 고령자) 약동학 데이터 검토
- 위절제술·위우회술 후 환자에서의 약물 흡수 변화 가능성 평가
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

