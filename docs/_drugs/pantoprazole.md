---
layout: default
title: Pantoprazole
parent: 높은 근거 (L1-L2)
nav_order: 578
evidence_level: L1
indication_count: 6
---

# Pantoprazole
{: .fs-9 }

근거 수준: **L1** | 예측 적응증: **6** 건
{: .fs-6 .fw-300 }

---

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 약사 평가 보고서

</div>

# Pantoprazole: 산 관련 위장관 질환에서 활동성 소화성 궤양으로

## 한 문장 요약

Pantoprazole은 위벽세포의 양성자 펌프(H+/K+ ATPase)를 억제하는 약으로, 한국에서는 에스-판토프라졸 제제(레토프라정)로 시판되고 있습니다.
TxGNN 모델은 **활동성 소화성 궤양(active peptic ulcer disease)**에 효과가 있을 수 있다고 예측하며, 현재 **1건의 임상시험**과 **20편의 문헌**이 이 방향을 지지합니다.
다만 이 예측은 기존 적응증과 기전이 같아 엄밀한 의미의 재창출이라기보다 허가 범위에 가까운 용도입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 원문은 첨부 문서 링크로만 제공되어 구체적인 내용을 확인할 수 없음 (산 관련 질환 치료제로 알려져 있음) |
| 예측 신규 적응증 | 활동성 소화성 궤양 (Active Peptic Ulcer Disease) |
| TxGNN 예측 점수 | 99.69% |
| 근거 수준 | L1 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 2건 |
| 권장 결정 | Proceed with Guardrails |

참고로 다른 예측 적응증의 평가는 다음과 같습니다.

| 순위 | 예측 적응증 | TxGNN 점수 | 근거 수준 | 권장 결정 |
|------|-----------|-----------|----------|---------|
| 1 | 활동성 소화성 궤양 | 99.69% | L1 | Proceed with Guardrails |
| 2 | 위공장 궤양 (gastrojejunal ulcer) | 99.63% | L3 | Research Question |
| 3 | 소화성 궤양 천공 | 99.63% | L3 | Research Question |
| 4 | 십이지장위 역류 | 99.27% | L3 | Research Question |
| 5 | 십이지장 폐쇄 | 99.21% | L5 | Hold |
| 6 | 십이지장 궤양 | 99.18% | L1 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 pantoprazole은 양성자 펌프 억제제(PPI)로, 위벽세포의 H+/K+ ATPase를 비가역적으로 억제하여 위산 분비를 줄입니다. 이를 통해 궤양 치유가 가능해집니다.

소화성 궤양은 위산이 점막 방어 기전을 압도해 생기는 대표적인 산 관련 질환입니다. 따라서 위산 분비를 억제하는 pantoprazole의 기전은 이 질환에 직접 적용됩니다. 이는 기존 적응증과 동일한 기전이므로 사실상 허가 범위 내 또는 이에 근접한 용도입니다.

반면 십이지장 폐쇄는 대부분 협착, 종괴 등 기계적 원인으로 생기므로 뚜렷한 기전적 연관성이 없습니다. 이 항목의 높은 점수는 치료 근거라기보다 십이지장 궤양과의 네트워크 근접성을 반영한 것으로 보입니다.

## 임상시험 근거

활동성 소화성 궤양(1순위 예측)에 대한 임상시험입니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT02084420](https://clinicaltrials.gov/study/NCT02084420) | Phase 3 | 완료 | 323 | 위·십이지장 궤양 및 H. pylori 양성 환자에서 ilaprazole vs pantoprazole 3제 요법(7일)의 제균 효과와 안전성 비교 (다기관, 무작위, 이중맹검) |

관련 질환인 십이지장 궤양에서는 다음과 같은 시험이 추가로 있습니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00374101](https://clinicaltrials.gov/study/NCT00374101) | Phase 3 | 완료 | 450 | 출혈성 소화성 궤양의 내시경 치료 후 PPI 고용량 vs 표준용량 비교 |
| [NCT00843063](https://clinicaltrials.gov/study/NCT00843063) | Phase 4 | 완료 | 161 | 아스피린 유발 궤양 재발 예방에서 famotidine vs pantoprazole 비교 |
| [NCT02551744](https://clinicaltrials.gov/study/NCT02551744) | 해당 없음 | 완료 | 101 | thienopyridine 사용자의 궤양 재발 예방에서 pantoprazole vs famotidine 비교 |
| [NCT02467621](https://clinicaltrials.gov/study/NCT02467621) | Phase 4 | 완료 | 3350 | 중환자실 스트레스 궤양 예방(SUP-ICU), 간접 근거 |
| [NCT00261300](https://clinicaltrials.gov/study/NCT00261300) | Phase 3 | 완료 | 100 | 만성 산 관련 증상에서 pantoprazole 장기 투여 |
| [NCT00001191](https://clinicaltrials.gov/study/NCT00001191) | Phase 2 | 완료 | 정보 없음 | 위산 과분비 환자에서 경구 omeprazole 및 정맥 pantoprazole |

## 문헌 근거

활동성 소화성 궤양 관련 문헌 중 주요 항목입니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [38384180](https://pubmed.ncbi.nlm.nih.gov/38384180/) | 2024 | RCT | Gut and Liver | 내시경 절제술 후 인공 궤양에서 tegoprazan 효과 평가 (활성 대조 다기관 시험) |
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | 체계적 문헌고찰/메타분석 | Am J Gastroenterol | LA grade C/D 식도염에서 P-CAB과 PPI의 치유 효능 비교 |
| [19938880](https://pubmed.ncbi.nlm.nih.gov/19938880/) | 2009 | Review | Clin Drug Investig | pantoprazole은 비가역적 양성자 펌프 억제제이며 약물 상호작용이 거의 없음 |
| [10638560](https://pubmed.ncbi.nlm.nih.gov/10638560/) | 2000 | 비교 시험 | Am J Gastroenterol | 브라질 십이지장 궤양 환자에서 pantoprazole vs ranitidine |
| [15244210](https://pubmed.ncbi.nlm.nih.gov/15244210/) | 2003 | 비교 시험 | Hepato-Gastroenterology | 활동성 십이지장 궤양 및 H. pylori 제균에서 lansoprazole vs pantoprazole |
| [11060758](https://pubmed.ncbi.nlm.nih.gov/11060758/) | 2000 | Review | Expert Opin Investig Drugs | 위·십이지장 궤양 치료의 최신 접근법 |
| [38652367](https://pubmed.ncbi.nlm.nih.gov/38652367/) | 2024 | 전임상 | Inflammopharmacology | 쥐 위궤양 모델에서 pantoprazole과 중간엽 줄기세포 병용 효과 |

십이지장 궤양에 대한 직접 근거는 다음과 같습니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [7569755](https://pubmed.ncbi.nlm.nih.gov/7569755/) | 1995 | RCT | Scand J Gastroenterol | 급성 십이지장 궤양에서 pantoprazole vs ranitidine (다기관) |
| [7614102](https://pubmed.ncbi.nlm.nih.gov/7614102/) | 1995 | RCT | Eur J Gastroenterol Hepatol | 급성 십이지장 궤양 치유율에서 pantoprazole 40mg vs omeprazole 20mg 비교 |
| [7781461](https://pubmed.ncbi.nlm.nih.gov/7781461/) | 1995 | RCT | Dig Dis Sci | 급성 십이지장 궤양 276명 대상 pantoprazole 40mg vs ranitidine 300mg |
| [8180294](https://pubmed.ncbi.nlm.nih.gov/8180294/) | 1994 | 통합분석 | Aliment Pharmacol Ther | 십이지장 궤양 5건 비교시험 통합 결과, 2주·4주 치유율에서 ranitidine보다 유의하게 우수 |
| [8882382](https://pubmed.ncbi.nlm.nih.gov/8882382/) | 1996 | Review | Drugs | 단기 치료(8주 이내)에서 ranitidine보다 우수하고 omeprazole과 동등 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201208632 | 레토프라정10밀리그램(에스-판토프라졸나트륨삼수화물) | 분홍색 장용성 필름코팅 타원형 정제 | 허가 문서 링크로만 제공되어 상세 적응증 확인 불가 |
| 201205628 | 레토프라정20밀리그램(에스-판토프라졸나트륨 삼수화물) | 노란색 장용성 필름코팅 타원형 정제 | 허가 문서 링크로만 제공되어 상세 적응증 확인 불가 |

두 제품 모두 안국약품(주)이 제조하며, 단일제로 유효한 허가 상태입니다.

## 안전성 고려사항

- **약물 상호작용**: 총 597건이 확인되었습니다. 이 중 주요(Major) 등급은 다음과 같습니다.
  - Acalabrutinib
  - Atazanavir

  중등도(Moderate) 등급에는 hydrochlorothiazide, atorvastatin, fenofibrate, bumetanide, amphotericin B, bosutinib, alpelisib, apalutamide, armodafinil 등이 있습니다.
- **지식그래프상 금기 질환** (허가사항이 아닌 지식그래프 기반): 골다공증, 폐경 후 골다공증, 골절, 악성 빈혈. PPI 장기 사용 시 골 건강 및 비타민 B12 흡수와 관련된 우려를 반영한 것으로 보이며, 실제 허가사항에서 확인이 필요합니다.

허가사항의 경고 및 금기는 허가증 원문에서 확인해야 합니다.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
활동성 소화성 궤양과 십이지장 궤양은 pantoprazole의 기존 작용 기전과 일치하는 질환이며, 완료된 Phase 3 시험과 다수의 이중맹검 비교시험이 뒷받침합니다. 다만 1순위 예측의 직접 근거는 H. pylori 제균 시험 1건에 한정되고, 허가사항 원문을 확인하지 못했습니다.

**진행하려면 필요한 것:**
- 허가사항 원문(경고, 금기, 적응증)을 내려받아 확인하여 허가 범위와의 일치 여부 검토
- 상세한 약물 작용 기전 데이터 보완
- 에스-판토프라졸(레토프라정)과 pantoprazole 라세미체의 근거 적용 가능성 검토. 제공된 근거는 대부분 pantoprazole 일반 제제에 대한 것입니다.
- 장기 사용 시 골 건강과 비타민 B12 모니터링 계획, 주요 상호작용 약물(atazanavir, acalabrutinib 등) 병용 관리 방안
- 위공장 궤양과 소화성 궤양 천공은 직접 근거가 부족하여 추가 연구 필요
- 십이지장 폐쇄는 기전적 근거가 없어 보류 권장
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

