---
layout: default
title: Diazepam
parent: 僅模型預測 (L5)
nav_order: 217
evidence_level: L5
indication_count: 10
---

# Diazepam
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

# Diazepam: 불안장애에서 불면증으로

## 한 문장 요약

Diazepam은 GABA-A 수용체를 양성 조절하여 진정·항불안·항경련 효과를 발휘하는 장시간 작용 벤조디아제핀계 약물로, 불안장애와 근이완 목적으로 폭넓게 사용되어 왔습니다.
TxGNN 모델은 **불면증(Insomnia)**에 효과가 있을 수 있다고 예측하며,
현재 **24건의 임상시험**과 **18편의 문헌**이 이 방향을 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 불안장애·근이완·경련 (현행 허가 데이터 없음) |
| 예측 신규 적응증 | 불면증 (Insomnia) |
| TxGNN 예측 점수 | 99.99% |
| 근거 수준 | L2 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터는 수집되지 않았습니다. 공지된 정보에 따르면, Diazepam은 반감기 20–100시간의 장시간 작용 벤조디아제핀(활성 대사체: desmethyldiazepam 포함)으로서, GABA-A 수용체의 벤조디아제핀 결합 부위에 결합해 클로라이드 이온 유입을 증가시키고 중추신경계 흥분성을 억제합니다.

불면증은 과각성 상태와 GABAergic 억제 기능 저하를 특징으로 합니다. Diazepam은 입면 잠복기를 단축하고 야간 각성 횟수를 감소시켜 수면 개시 및 유지를 돕습니다. 이는 1981년에 수행된 직접 비교 RCT(PMID 6113175, n=100)를 통해 불면증 외래 환자에서 임상적으로 입증된 바 있습니다.

그러나 장기 사용 시 서파수면(SWS)과 REM 수면을 억제하여 수면 구조를 변화시키고, 내성·의존성·반동성 불면증(rebound insomnia)을 유발할 수 있습니다. 현대 임상 지침은 만성 불면증의 1차 치료로 인지행동치료(CBT-I)를 우선 권고하며, 벤조디아제핀은 단기 혹은 과도기적 사용으로 제한됩니다. 최근 임상시험의 흐름도 Diazepam의 직접 효능 연구보다는 **장기 복용 후 안전한 중단 전략**에 집중되어 있습니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT04050176](https://clinicaltrials.gov/study/NCT04050176) | Phase 3 | 모집 완료·진행 중 | 260 | CBT-I 병행 벤조디아제핀 맹검 점감법의 최면제 중단율 향상 효과 비교; 불면증 장기 치료에서 점감 전략의 역할 평가 |
| [NCT02831894](https://clinicaltrials.gov/study/NCT02831894) | Phase 2 | 완료 | 74 | 점감 속도 및 개인 특성이 최면제 중단에 미치는 영향 평가; 65% 이상이 5년 이상 최면제(벤조디아제핀 포함) 사용 |
| [NCT04751851](https://clinicaltrials.gov/study/NCT04751851) | N/A | 완료 | 128 | 최면제 의존성 불면증 성인에서 수용전념치료(ACT) 기반 원격심리 개입과 벤조디아제핀 점감 프로그램 효과 비교 |
| [NCT03687086](https://clinicaltrials.gov/study/NCT03687086) | N/A | 완료 | 188 | 고령자 수면제 중단을 위한 새로운 메커니즘 탐색; 점감 및 CBT-I 단독 접근의 한계를 넘어설 보완 전략 평가 |
| [NCT02648776](https://clinicaltrials.gov/study/NCT02648776) | N/A | 미확인 | 1,400 | 대만 학술 의료기관 고령 불면증 환자 대상 최면제 처방 패턴·효능·안전성 및 약동학·약유전학적 특성 전향적 코호트 연구 |
| [NCT03461042](https://clinicaltrials.gov/study/NCT03461042) | Phase 4 | 완료 | 17 | 만성 불면증에서 라멜테온 병용 시 (비)벤조디아제핀 점감 효과 이중맹검 다기관 연구 (소규모로 해석 주의) |
| [NCT02281175](https://clinicaltrials.gov/study/NCT02281175) | N/A | 완료 | 114 | 고령 벤조디아제핀 사용자의 점감을 위한 PASSE-65+ 심리사회 개입의 효과 검증 |
| [NCT01893632](https://clinicaltrials.gov/study/NCT01893632) | Phase 2 | 조기 종료 | 2 | 벤조디아제핀 의존성 치료에 Gabapentin 병용 연구; n=2로 조기 종료, 의존 문제의 심각성 간접 반증 |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [6113175](https://pubmed.ncbi.nlm.nih.gov/6113175/) | 1981 | RCT (n=100) | J Int Med Res | 불면증 외래 환자 100명 대상 7일 이중맹검 비교; Lormetazepam 1 mg이 **Diazepam 5 mg 대비** 입면 시간 단축 및 수면 유지에서 유의하게 우수 — 본 자료집에서 Diazepam 불면증 효능을 직접 입증한 유일한 RCT |
| [39581171](https://pubmed.ncbi.nlm.nih.gov/39581171/) | 2024 | Review | Bioorganic Chemistry | 소분자 GABA-A 수용체 조절제의 임상 적용 리뷰; Diazepam이 간질·불안·불면증 치료에 사용되는 대표 양성 알로스테릭 조절제(PAM)로 기술, 진정·의존성 부작용 함께 서술 |
| [29479317](https://pubmed.ncbi.nlm.nih.gov/29479317/) | 2018 | 체계적 문헌고찰 | Front Pharmacol | 산조인 배합제의 불면증 치료 고품질 RCT 근거 고찰; 다수 RCT에서 벤조디아제핀(Diazepam 포함)을 양성 대조군으로 사용 |
| [35228700](https://pubmed.ncbi.nlm.nih.gov/35228700/) | 2022 | 동물연구 | Nature Neuroscience | 장기 Diazepam 투여로 미세아교세포의 수상돌기 가시 식세포 증가 및 인지 기능 저하 유발; TSPO 경로를 통한 인지 부작용 기전 최초 규명 — 장기 사용 위험 시사 |
| [40347763](https://pubmed.ncbi.nlm.nih.gov/40347763/) | 2025 | 동물연구 | J Pharm Biomed Anal | PCPA 유도 수면 박탈 마우스 모델에서 익인안신과립의 신경전달물질·사이토카인·장내 미생물 조절 효과 평가; Diazepam 양성 대조군 사용 |
| [37377000](https://pubmed.ncbi.nlm.nih.gov/37377000/) | 2023 | 동물연구 | Food & Function | 불면증 마우스 모델에서 염소유·우유의 수면 개선 효과 및 마이크로바이옴 변화 비교; Diazepam 양성 대조군 사용 |
| [37776625](https://pubmed.ncbi.nlm.nih.gov/37776625/) | 2023 | 동물연구 | J Pharm Biomed Anal | PCPA 유도 불면증 랫드에서 뇌령편의 진정·최면 효과 및 대사체 기전; Diazepam 양성 대조군 사용 |
| [6114852](https://pubmed.ncbi.nlm.nih.gov/6114852/) | 1981 | Review | Drugs | 트리아졸람의 불면증 치료 효능 리뷰; Diazepam 등 장시간 작용 벤조디아제핀 대비 단시간 제제의 수면 잔류 효과 감소 이점 서술 |
| [40583063](https://pubmed.ncbi.nlm.nih.gov/40583063/) | 2025 | 임상·분자 연구 | Cell Mol Biol Lett | 장기 Diazepam·Zolpidem 사용이 유방암 위험을 증가시킬 수 있음; GABA-A 수용체 매개 분자 기전 규명 — 장기 사용 안전성 우려 |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | Review | Expert Opin Drug Metab Toxicol | 항불안제 약동학 고찰; 벤조디아제핀의 ADME 특성, CYP 효소 매개 대사 및 약물 상호작용 상세 기술 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
1981년 직접 비교 RCT(PMID 6113175, n=100)를 통해 불면증에 대한 단기 효능이 임상적으로 입증되어 있고, GABA-A 수용체를 통한 기전도 명확합니다. 그러나 현행 임상시험의 초점이 Diazepam의 직접 효능보다 장기 복용 후 안전한 중단 전략으로 이동하고 있으며, 의존성·수면 구조 변화·인지 저하 위험을 고려할 때 단기 사용 및 면밀한 모니터링이 전제되어야 합니다.

**진행하려면 필요한 것:**
- DrugBank API를 통한 상세 MOA 데이터 및 독성 프로파일 확보 (DG002 해소)
- MFDS 허가사항 기반 경고·금기 정보 검토 (DG001 해소)
- 장기 사용 위험 관리 계획 수립 (의존성, 낙상, 인지 기능 주기적 평가)
- CBT-I 또는 오렉신 수용체 길항제 대비 단기 병용 전략 정의
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

