---
layout: default
title: Aminophylline
parent: 모델 예측만 (L5)
nav_order: 59
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Aminophylline: 예측 신규 적응증 편두통 (Migraine Disorder) (근거 수준 L5). 기존 적응증: 허가 적응증 본문이 확인되지 않음 (허가증에는 문서 링크만 수록)"
monitor_inn: "AMINOPHYLLINE"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "migraine with or without aura, susceptibility to", "atrophoderma vermiculata", "ulerythema ophryogenesis", "Prinzmetal angina", "pulmonary hypertension", "sciatic neuropathy", "hyperthyroidism", "kyphoscoliotic heart disease"]
---

# Aminophylline
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
{: .fs-6 .fw-300 }

---

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 약사 평가 보고서

</div>

# Aminophylline: 기관지 질환 치료제에서 편두통으로

## 한 문장 요약

Aminophylline은 크산틴 계열 약물로, 한국에서 서방정·정제·주사제로 시판되고 있으며 기존 허가 적응증은 이번 데이터에서 문서 링크로만 확인됩니다.
TxGNN 모델은 **편두통(Migraine Disorder)**에 효과가 있을 수 있다고 예측하지만, 현재 등록된 **임상시험은 0건**이고 관련 문헌은 **4편**(리뷰 1편, 증례 보고 등)에 그칩니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문이 확인되지 않음 (허가증에는 문서 링크만 수록) |
| 예측 신규 적응증 | 편두통 (Migraine Disorder) |
| TxGNN 예측 점수 | 99.88% |
| 근거 수준 | L4 (전임상·기전 수준의 근거) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 7건 |
| 권장 결정 | Hold (연구 질문 단계) |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 확보되지 않았습니다. 다만 문헌에 따르면 aminophylline은 비선택적 아데노신 수용체 길항제이자 포스포디에스테라아제 억제제로 알려져 있습니다.

2023년 리뷰는 편두통이 높은 아데노신 농도와 뇌 에너지 대사 장애와 연관될 수 있으며, aminophylline이 통증, 특히 경막 천자 후 두통에서 치료 효과를 보일 수 있다고 제시합니다. 또한 아데노신 작용제인 regadenoson이 편마비성 편두통을 유발한 증례가 보고되어, 아데노신 신호가 편두통에 관여한다는 가설을 간접적으로 뒷받침합니다.

다만 이는 기전적 추정과 소수의 보고에 근거한 것으로, 임상적 효능이 입증된 것은 아닙니다.

## 임상시험 근거

현재 편두통과 관련해 등록된 임상시험이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [38059379](https://pubmed.ncbi.nlm.nih.gov/38059379/) | 2023 | Review | Pain Management | 편두통이 아데노신 과다와 뇌 에너지 대사 장애와 관련될 수 있으며, aminophylline이 통증·경막 천자 후 두통에서 치료 효과를 보일 가능성 제시 |
| [34308528](https://pubmed.ncbi.nlm.nih.gov/34308528/) | 2022 | Case report | J Nucl Cardiol | 아데노신 A2A 작용제 regadenoson이 편마비성 편두통을 유발한 증례. 아데노신 경로의 관여를 시사 |
| [7728647](https://pubmed.ncbi.nlm.nih.gov/7728647/) | 1995 | Case report | Can J Cardiol | 과도한 아데노신 효과에 의한 X 증후군(심근성 편두통) 증례 |
| [14168418](https://pubmed.ncbi.nlm.nih.gov/14168418/) | 1964 | Review | Aggiornamenti Clinicoterapeutici | 두통 관련 고전 리뷰 (초록 없음) |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200001785 | 아스콘틴서방정(아미노필린수화물) | 서방정(제피정) | 허가 적응증 본문 확인 불가 |
| 197100030 | 대한아미노필린주사액(2.5%) | 주사제(앰플) | 허가 적응증 본문 확인 불가 |
| 200102995 | 휴온스아미노필린주사액 | 주사제(앰플) | 허가 적응증 본문 확인 불가 |
| 197500144 | 제일아미노필린주사액 | 주사제(앰플) | 허가 적응증 본문 확인 불가 |
| 197000102 | 대원아미노필린정(아미노필린수화물) | 정제 | 허가 적응증 본문 확인 불가 |

위 외에 소아용아스콘틴서방정, 아미필린주(수출용)가 있어 총 7건이 유효 상태입니다.

## 안전성 고려사항

**약물 상호작용**: 약물 상호작용 조회 결과 총 100건이 확인되었으며, 주요 항목은 다음과 같습니다.
- **Major**: Bupropion
- **Moderate**: Famotidine, Ranitidine, Cimetidine, Nizatidine(H2 차단제), Doxycycline, Tetracycline, Minocycline(테트라사이클린계), Clarithromycin, Hydrocortisone, Dexamethasone, Betamethasone, Triamcinolone, Budesonide(코르티코스테로이드) 등
- **Minor**: Lansoprazole

그 밖에 허가사항의 경고 및 금기는 허가 문서를 참조하세요.

**참고 (다른 예측 적응증 관련 신호)**: 변이형 협심증에서 aminophylline 중단이 관상동맥 연축을 유발한 보고가 있고, 갑상선기능항진증에서는 메틸크산틴이 진전을 악화시킬 수 있습니다.

## 결론 및 다음 단계

**결정: Hold (연구 질문 단계)**

**사유:**
TxGNN 점수는 높지만 편두통에 대한 임상시험이 없고, 근거는 리뷰 1편과 증례 보고 등 기전적·간접적 수준에 그칩니다. 또한 허가 적응증과 안전성 정보가 확인되지 않아 안전성 평가를 진행할 수 없습니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기·적응증) 확보: 식약처 의약품안전나라의 허가 문서 PDF 분석
- 작용 기전(MOA) 데이터 보완 (DrugBank 조회)
- 편두통에 대한 탐색적 임상시험 설계 (예: 경막 천자 후 두통 등 관련 군 대상 소규모 시험)
- 상호작용 위험이 큰 병용약(bupropion 등)과 편두통 치료제 병용 시 안전성 검토

### 참고: 기타 예측 적응증

| 순위 | 예측 적응증 | 점수 | 근거 수준 | 비고 |
|------|-----------|------|---------|------|
| 7 | 폐고혈압 | 99.23% | L3 | Phase 1 안전성 시험 1건(NCT01530464, ambrisentan 병용, 효능 평가 없음)과 소규모 혈역학 연구. 가장 근거가 많으나 RCT 근거 없음 |
| 6 | 프린츠메탈 협심증 | 99.33% | L4 | 관상동맥 연축 유발 보고가 있어 이득보다 위해 가능성 시사 |
| 9 | 갑상선기능항진증 | 99.06% | L4 | 약동학·생리학적 상호작용 연구뿐이며 치료 근거 없음. 빈맥·진전 악화 우려 |
| 2, 4, 5, 8, 10 | 기타(전조 증상 있는 뇌간 편두통, 위축성 피부증 등) | 99.0~99.8% | L5 | 모델 예측만 있고 근거 부족 |
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

