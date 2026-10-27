---
layout: default
title: Travoprost
parent: 모델 예측만 (L5)
nav_order: 757
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Travoprost: 예측 신규 적응증 내장 칼시필락시스 (visceral calciphylaxis) (근거 수준 L5). 기존 적응증: 녹내장 및 고안압증 (허가 적응증 원문은 허가증 링크로만 제공되어 일반적인 허가 용도로 기재)"
monitor_inn: "Travoprost"
predicted_indications: ["visceral calciphylaxis", "venous thoracic outlet syndrome", "arterial thoracic outlet syndrome", "neurogenic thoracic outlet syndrome", "vascular disease", "angiodysplasia of stomach", "blue toe syndrome", "lymphangiectasis", "idiopathic spontaneous coronary artery dissection", "hemangioendothelioma"]
---

# Travoprost
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

## Travoprost: 녹내장·고안압증에서 내장 칼시필락시스로
{: .text-alpha }

## 한 문장 요약

Travoprost는 프로스타글란딘 F2-알파 유사체(FP 수용체 작용제)로, 원래 녹내장과 고안압증의 안압 하강을 위한 점안제로 사용되었습니다.
TxGNN 모델은 **내장 칼시필락시스(visceral calciphylaxis)**에 효과가 있을 수 있다고 예측하지만, 이 질환을 직접 뒷받침하는 임상시험과 문헌은 **0건**입니다.
다만 예측 순위 5위인 "혈관 질환"에서는 10건의 임상시험과 20편의 문헌이 검색되었으나, 모두 녹내장(기존 적응증) 연구여서 신규 적응증의 근거로는 인정되지 않습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 녹내장 및 고안압증 (허가 적응증 원문은 허가증 링크로만 제공되어 일반적인 허가 용도로 기재) |
| 예측 신규 적응증 | 내장 칼시필락시스 (visceral calciphylaxis) |
| TxGNN 예측 점수 | 99.99998% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 4건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Travoprost는 프로스타글란딘 F2-알파 유사체로 FP 수용체를 활성화하며, 안구 조직에서 혈관 확장 작용을 보입니다. 안압 하강은 포도막공막 유출 증가로 일어나는 것으로 알려져 있습니다.

칼시필락시스(석회화 요독성 세동맥병증)와의 연결은 지식 그래프에 기반한 계산적 예측일 뿐입니다. 전신 혈관 석회화는 안구 국소 투여 약물과 기전상 거리가 멀고, 전임상·임상·문헌 근거가 없습니다. 따라서 이 예측은 현재로서는 가설 수준입니다.

상위 예측 질환(흉곽출구증후군, 혈관 질환, 위 혈관이형성증, 청색 발가락 증후군, 림프관확장증, 자발성 관상동맥 박리, 혈관내피종 등)도 대부분 혈관 질환 연관성에서 비롯된 것으로 보이며, 실제 근거는 없습니다. 위 혈관이형성증에서는 전신 혈관 확장이 출혈을 악화시킬 가능성도 이론적으로 제기됩니다.

## 임상시험 근거

내장 칼시필락시스에 대한 관련 임상시험 등록이 없습니다.

참고로 "혈관 질환" 예측(5위)에서 검색된 시험은 모두 녹내장·고안압증 연구로, 신규 적응증을 입증하지 않습니다. 가장 관련 있는 시험은 다음과 같습니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00308945](https://clinicaltrials.gov/study/NCT00308945) | Phase 4 | 완료 | 20 | Travoprost와 latanoprost가 녹내장 환자의 망막 혈관 직경과 맥락막 혈류에 미치는 영향 비교. 소규모이며 안구에 국한됨 |
| [NCT02136589](https://clinicaltrials.gov/study/NCT02136589) | Phase 4 | 완료 | 40 | Travoprost로 인한 결막 충혈에 대한 NSAID 전처치 효과 (부작용 연구) |
| [NCT00293800](https://clinicaltrials.gov/study/NCT00293800) | Phase 3 | 완료 | 173 | 개방각 녹내장·고안압증 치료 (허가 적응증) |
| [NCT00293761](https://clinicaltrials.gov/study/NCT00293761) | Phase 3 | 완료 | 109 | 개방각 녹내장·고안압증 치료 (허가 적응증) |
| [NCT00293787](https://clinicaltrials.gov/study/NCT00293787) | Phase 3 | 완료 | 156 | 개방각 녹내장·고안압증 치료 (허가 적응증) |
| [NCT00672997](https://clinicaltrials.gov/study/NCT00672997) | Phase 3 | 완료 | 301 | Travoprost/timolol 복합제의 안전성·안압 하강 효과 |
| [NCT00760539](https://clinicaltrials.gov/study/NCT00760539) | Phase 3 | 완료 | 87 | Travoprost/timolol 복합제 (일본), 위와 동일 설계 |
| [NCT02140060](https://clinicaltrials.gov/study/NCT02140060) | Phase 2 | 완료 | 327 | Travoprost/brinzolamide 복합제의 안압 하강 효과 |
| [NCT01510145](https://clinicaltrials.gov/study/NCT01510145) | Phase 4 | 완료 | 191 | Latanoprost에서 BAK 무첨가 travoprost로 전환 시 효능·내약성 |
| [NCT00047554](https://clinicaltrials.gov/study/NCT00047554) | 해당 없음 | 종료 | 336 | Travatan 사용 후 홍채 색소 변화 환자의 5년 안전성 추적 |

## 문헌 근거

내장 칼시필락시스에 대한 관련 문헌이 없습니다.

참고로 "혈관 질환" 예측에서 검색된 문헌은 대부분 녹내장 치료와 안구 표면 내약성에 관한 것이며, 신규 적응증 근거가 아닙니다. 혈관 관련 예측인 혈관내피종에서는 다음 증례 보고 1건만 있으며, 치료 효과가 아닌 이상반응을 보고합니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [19107053](https://pubmed.ncbi.nlm.nih.gov/19107053/) | 2008 | Case report | J Fr Ophtalmol | Sturge-Weber-Krabbe 증후군 환자에서 travoprost 점안 후 포도막 삼출과 망막박리 발생 |
| [22167538](https://pubmed.ncbi.nlm.nih.gov/22167538/) | 2012 | Meta-analysis | Eur J Ophthalmol | 프로스타글란딘-timolol 복합제 3종의 안압 하강 효과와 내약성 |
| [23231442](https://pubmed.ncbi.nlm.nih.gov/23231442/) | 2013 | Meta-analysis | J Ocul Pharmacol Ther | 프로스타글란딘 유사체와 timolol의 고정·비고정 복합요법 비교 |
| [31335731](https://pubmed.ncbi.nlm.nih.gov/31335731/) | 2019 | Review | Medicine | 녹내장 환자에서 travoprost 효능 평가 |
| [25867658](https://pubmed.ncbi.nlm.nih.gov/25867658/) | 2015 | Systematic Review | Curr Med Res Opin | 프로스타글란딘-timolol 복합제의 효능과 내약성 |
| [19019922](https://pubmed.ncbi.nlm.nih.gov/19019922/) | 2009 | Systematic Review | Br J Ophthalmol | Latanoprost와 travoprost·bimatoprost의 결막 충혈 비교 |
| [12648301](https://pubmed.ncbi.nlm.nih.gov/12648301/) | 2003 | Review | J Ocul Pharmacol Ther | 국소 프로스타글란딘 사용 시 결막 충혈 (travoprost에서 최대 50%) |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200109117 | 트라바탄점안액0.004% | 점안제 | 허가 적응증 원문은 허가증 참조 |
| 201604286 | 이즈바점안액0.003% | 점안제 | 허가 적응증 원문은 허가증 참조 |
| 200702090 | 듀오트라브점안액 | 점안제 | 허가 적응증 원문은 허가증 참조 |
| 202105922 | 트라보비젼사인점안액(1회용, 수출용) | 1회용 점안액 | 허가 적응증 원문은 허가증 참조 |

## 안전성 고려사항

- **약물 상호작용**: 49건이 조회되었으나 모두 위험 등급이 미확정입니다. 일부 예: calcitriol, pantoprazole, morphine, metformin, prednisone, simvastatin, aspirin.
- **지식 그래프상 금기 질환**: 포도막염, 홍채 질환, 모양체 질환, 범포도막염, 홍채염, 낭포황반부종, 황반망막부종 (허가 문구가 아닌 예측 모델의 그래프 정보).
- **이상반응 신호**: 결막 충혈이 흔하며(최대 50%), 홍채 색소 변화가 보고되었습니다. 혈관 기형 질환(Sturge-Weber-Krabbe 증후군) 환자에서 포도막 삼출이 보고되어 신중한 접근이 필요합니다.

허가사항의 경고 및 금기 원문은 확인되지 않았으므로 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
내장 칼시필락시스 예측은 모델 점수만 있을 뿐 임상·전임상·문헌 근거가 전혀 없으며(L5), 국소 안약의 FP 작용제 기전이 전신 혈관 석회화와 거리가 멉니다. 혈관 질환 관련 근거로 보이는 시험과 문헌도 모두 녹내장 연구여서 재창출 근거가 되지 않습니다.

**진행하려면 필요한 것:**
- 허가 적응증·경고·금기 원문 확보 (허가사항 PDF 파싱)
- DrugBank에서 작용 기전(MOA) 데이터 확보
- 칼시필락시스에서 FP 수용체 신호와 혈관 석회화 간 기전 연관성을 검증하는 전임상 연구
- 전신 노출이 필요한 질환에서 국소 안약 제형의 투여 경로 적합성 평가
- 상위 예측 질환 전반에 대한 체계적 문헌 검색 재수행
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

