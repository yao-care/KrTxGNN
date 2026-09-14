---
layout: default
title: Ticagrelor
parent: 僅模型預測 (L5)
nav_order: 677
evidence_level: L5
indication_count: 10
---

# Ticagrelor
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

# Ticagrelor: 급성관상동맥증후군에서 두개내동맥경화증으로

## 한 문장 요약

Ticagrelor는 P2Y12 수용체 억제제 계열 항혈소판제로, 원래 급성관상동맥증후군(ACS) 및 말초동맥질환에서 혈전성 심혈관 사건 예방에 사용되어 왔습니다. TxGNN 모델은 **두개내동맥경화증(Intracranial Arteriosclerosis)**에 효과가 있을 수 있다고 예측하며, 현재 **11건의 임상시험**(이 중 완료된 Phase 3 RCT 1건, 진행 중인 Phase 3 RCT 1건 포함)과 **3편의 문헌**이 이 방향을 지지합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 급성관상동맥증후군(ACS)/말초동맥질환 등 혈전성 심혈관질환 (원 개발사 글로벌 승인 적응증 기준, 한국 미허가) |
| 예측 신규 적응증 | 두개내동맥경화증 (Intracranial Arteriosclerosis) |
| TxGNN 예측 점수 | 99.97% |
| 근거 수준 | L2 |
| 한국 시판 현황 | 미판매 (허가 없음) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

Ticagrelor의 공식 작용기전(MOA) 데이터는 현재 확보되지 않았습니다(DG002, High). 다만 근거팩 내 예측 근거 설명에 따르면, Ticagrelor는 P2Y12 수용체를 억제하여 혈소판 응집을 차단하는 약물이며, 기존에는 급성관상동맥증후군(ACS) 및 PCI 후 혈전 예방을 위한 핵심 항혈소판제로 사용되어 왔습니다.

두개내동맥경화증(ICAD)은 뇌 내 동맥의 죽상경화반 형성으로 혈류가 감소하고 국소 혈전이 발생하는 질환으로, 병태생리학적으로 혈소판 의존성 혈전 형성이 핵심 기전입니다. 현재 임상 지침에서는 clopidogrel + aspirin 이중항혈소판요법(DAPT)이 증상성 ICAD의 표준 치료로 널리 사용되고 있습니다.

Ticagrelor는 clopidogrel과 동일한 P2Y12 억제제 계열이지만, prodrug 대사 과정이 필요 없고 CYP2C19 유전자 변이로 인한 clopidogrel 저반응(resistance) 환자에서도 안정적인 효과를 보이는 것으로 알려져 있습니다. 이는 ICAD 환자군에서 clopidogrel 대체 옵션으로서 기전적 타당성을 뒷받침하며, 실제로 CAPTIVA(NCT05047172) 등 두개내동맥협착 특이적 Phase 3 시험이 이미 진행 중입니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01732822](https://clinicaltrials.gov/study/NCT01732822) | Phase 3 | 완료 | 13,885 | 말초동맥질환 환자에서 ticagrelor vs clopidogrel의 심혈관사망/심근경색/허혈성뇌졸중 예방효과 비교 |
| [NCT05047172](https://clinicaltrials.gov/study/NCT05047172) | Phase 3 | 진행 중(비모집) | 1,683 | CAPTIVA 시험 — 두개내혈관 동맥협착에서 rivaroxaban/ticagrelor 병용 vs clopidogrel 단독의 1년 허혈성뇌졸중·뇌출혈·혈관사망 예방효과 비교, 질환 특이성 최고 |
| [NCT02605447](https://clinicaltrials.gov/study/NCT02605447) | Phase 4 | 완료 | 2,009 | 출혈 고위험군 PCI 환자에서 3개월 DAPT 안전성 평가 |
| [NCT06714526](https://clinicaltrials.gov/study/NCT06714526) | NA | 모집 중 | 100 | 증상성 두개내동맥경화질환에서 유전형 기반 P2Y12 억제제 선택 vs 기존 clopidogrel 치료 비교 |
| [NCT04948749](https://clinicaltrials.gov/study/NCT04948749) | NA | 모집 중 | 792 | DREAM-PRIDE — 증상성 ICAS에서 약물용출스텐트+적극적 약물치료 vs 표준 약물치료의 재발성 뇌졸중 예방 비교 |
| [NCT01813435](https://clinicaltrials.gov/study/NCT01813435) | Phase 3 | 완료 | 15,991 | GLOBAL LEADERS — 스텐트 삽입 후 ticagrelor 단독요법 vs 표준 DAPT의 항혈소판 전략 비교 |
| [NCT06058130](https://clinicaltrials.gov/study/NCT06058130) | NA | 상태 불명 | 2,171 | 급성허혈성뇌졸중+비판막성심방세동+두개내외동맥협착 환자에서 항응고+항혈소판 병용요법 비교 |
| [NCT07354828](https://clinicaltrials.gov/study/NCT07354828) | N/A | 모집 예정 | 3,500 | 관상동맥 재관류술 DAPT 기반 품질관리지표 최적화 연구 |
| [NCT06857045](https://clinicaltrials.gov/study/NCT06857045) | NA | 철회됨 | 0 | 두개내 시롤리무스용출스텐트 후 3개월 vs 6개월 DAPT 비교 (철회로 자료 없음) |
| [NCT03620760](https://clinicaltrials.gov/study/NCT03620760) | Phase 4 | 상태 불명 | 2,036 | 약물용출스텐트 삽입 후 불안정형협심증 환자에서 저용량 vs 표준용량 ticagrelor 효능/안전성 비교 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [39862061](https://pubmed.ncbi.nlm.nih.gov/39862061/) | 2025 | Trial Protocol | International Journal of Stroke | CAPTIVA 시험 설계 및 초기 진행상황 — 증상성 두개내동맥경화협착(ICAS)에서 clopidogrel+aspirin 표준요법 대비 다른 이중항혈전요법 조합의 우월성 검증 목적 |
| [38252758](https://pubmed.ncbi.nlm.nih.gov/38252758/) | 2024 | Review | Stroke | 두개내동맥경화증 최신 개관 — 서론, 주요 소견 및 지식 격차 정리 |
| [39658130](https://pubmed.ncbi.nlm.nih.gov/39658130/) | 2025 | Cohort | Journal of Neurointerventional Surgery | 신경중재시술에서 저용량 ticagrelor(60mg bid)+aspirin 병용요법과 표준 aspirin+clopidogrel 요법 비교 경험 보고 |

## 한국 시판 정보

Ticagrelor는 현재 한국에서 허가된 제품이 없습니다(미판매, 허가증 0건). 따라서 국내 공식 허가 적응증 및 라벨 정보를 확인할 수 없습니다.

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. (한국 미판매로 국내 경고·금기·약물상호작용 자료가 확보되지 않았으며, 이는 안전성 초기 평가(S1) 진입을 막는 Blocking 등급 데이터 공백(DG001)으로 분류되어 있습니다.)

## 결론 및 다음 단계

**결정: Hold**

**사유:**
두개내동맥경화증에 대한 근거 수준은 L2(완료된 Phase 3 RCT 1건)로 중간 수준이며, 질환 특이적 Phase 3 시험(CAPTIVA, NCT05047172)이 진행 중이지만 완료 시점은 2028년으로 아직 상당 기간 남아 있습니다. 또한 Ticagrelor는 한국에서 미판매 상태이며, 국내 안전성 경고/금기 정보 부재가 Blocking 등급 데이터 공백으로 지정되어 있어 안전성 초기 평가(S1) 자체에 진입할 수 없는 상태입니다.

**진행하려면 필요한 것:**
- CAPTIVA(NCT05047172) 등 질환 특이적 Phase 3 임상시험 결과 발표 대기
- 식약처(MFDS) 허가사항 또는 원 개발사 글로벌 라벨의 경고·금기 정보 확보 (DG001, Blocking)
- DrugBank API를 통한 상세 작용기전(MOA) 데이터 확보 (DG002, High)
- 약물상호작용(DDI) 데이터베이스 재조회
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

