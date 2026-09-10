---
layout: default
title: Propofol
parent: 僅模型預測 (L5)
nav_order: 581
evidence_level: L5
indication_count: 5
---

# Propofol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Propofol: 전신마취에서 편두통(Migraine)으로

## 한 문장 요약

Propofol은 정맥마취제로서 전신마취 유도 및 진정에 널리 사용되어 온 약물입니다(단, 본 Evidence Pack에는 공식 기존 적응증 데이터가 등록되어 있지 않아 일반적으로 알려진 용도 기준으로 기재).
TxGNN 모델은 **편두통(Migraine Disorder)**에 효과가 있을 수 있다고 예측하며, 현재 **5건의 임상시험**과 **20편의 문헌**이 이 방향을 지지하고, 그중 완료된 RCT와 체계적 문헌고찰이 포함되어 있습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 전신마취/진정 (일반적으로 알려진 용도; Evidence Pack 내 공식 적응증 데이터 없음) |
| 예측 신규 적응증 | 편두통 (Migraine Disorder) |
| TxGNN 예측 점수 | 99.69% |
| 근거 수준 | L2 |
| 한국 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

현재 Propofol의 상세한 작용 기전(MOA) 데이터는 Evidence Pack에 등록되어 있지 않습니다. 다만 관련 문헌 및 재창출 근거(repurposing_rationale)에 따르면, Propofol은 **GABA-A 수용체 작용제**로서 중추신경 억제 효과를 가지며, 편두통의 병태생리 핵심 기전 중 하나로 알려진 **피질확산억제(cortical spreading depression, CSD)**를 억제하는 작용이 보고되어 있습니다.

실제로 저용량(subanesthetic dose) Propofol은 소아·성인 응급실에서 난치성 편두통에 대한 "rescue therapy"로 다년간 임상 실무에서 사용되어 온 이력이 있으며, 관련 기전 연구(PMID 22390898)에서도 Propofol이 CSD를 억제함을 실험적으로 확인한 바 있습니다. 이는 TxGNN 예측의 생물학적 타당성을 뒷받침합니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01604785](https://clinicaltrials.gov/study/NCT01604785) | Phase 2/3 | 완료 | 74 | 소아 응급실 편두통 급성발작에 저용량 propofol 투여, 표준치료보다 안전하고 효과적일 가능성 시사 |
| [NCT02485418](https://clinicaltrials.gov/study/NCT02485418) | N/A | 완료 | 40 | 소아 편두통 급성발작 치료제로서 저용량 propofol 지속주입의 유효성 및 안전 용량 범위 평가 |
| [NCT02492295](https://clinicaltrials.gov/study/NCT02492295) | N/A | 조기중단 | 12 | 성인 난치성 중증 편두통에 저용량 propofol 투여, 표본 수 부족으로 조기 종료 |
| [NCT03789370](https://clinicaltrials.gov/study/NCT03789370) | N/A | 불명 | 130 | Sevoflurane 대비 propofol 마취 유지 시 수술 후 두통 발생률 비교(간접 관련) |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | Guideline/Review | Headache | 미국두통학회(AHS), 응급실 편두통 비경구 약물치료 가이드라인 갱신 |
| [29456086](https://pubmed.ncbi.nlm.nih.gov/29456086/) | 2018 | RCT | J Emerg Med | 소아 편두통에 저용량 propofol의 전향적 무작위대조시험, 부작용 프로파일 양호 및 재원기간 단축 가능성 |
| [31621134](https://pubmed.ncbi.nlm.nih.gov/31621134/) | 2020 | 체계적 문헌고찰 | Acad Emerg Med | 응급실 급성 편두통에서 propofol의 안전성·유효성에 대한 제한적 근거 종합 |
| [35402989](https://pubmed.ncbi.nlm.nih.gov/35402989/) | 2022 | RCT | Arch Acad Emerg Med | Propofol+Granisetron vs Propofol+Metoclopramide 비교, 급성 편두통 증상 관리 |
| [35573713](https://pubmed.ncbi.nlm.nih.gov/35573713/) | 2022 | RCT | Arch Acad Emerg Med | Sumatriptan 단독 대비 Sumatriptan+Propofol 병용의 급성 편두통 효능 평가 |
| [32705801](https://pubmed.ncbi.nlm.nih.gov/32705801/) | 2020 | RCT(Pilot) | Emerg Med Australas | 응급실 급성 편두통에서 procedural sedation 용량의 propofol vs 표준치료 비교 |
| [39364614](https://pubmed.ncbi.nlm.nih.gov/39364614/) | 2024 | 체계적 문헌고찰/네트워크분석 | Headache | 중증 급성 편두통 후 재발 방지를 위한 비경구 약제 효과 비교 |
| [24875925](https://pubmed.ncbi.nlm.nih.gov/24875925/) | 2015 | 체계적 문헌고찰(가이드라인) | Cephalalgia | 캐나다두통학회, 응급 환경에서 편두통 통증 치료 권고안 |
| [27454834](https://pubmed.ncbi.nlm.nih.gov/27454834/) | 2016 | 후향적 코호트 | Expert Rev Neurother | 난치성 편두통에서 저용량 propofol의 약물 프로파일 및 임상 경험 정리 |
| [10759925](https://pubmed.ncbi.nlm.nih.gov/10759925/) | 2000 | 초기 임상 경험 | Headache | 외래 두통클리닉에서 난치성 편두통에 대한 정맥 propofol의 독보적 유효성 최초 보고 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
저용량 Propofol의 편두통 치료 효과를 지지하는 완료된 RCT(PMID 29456086 등)와 체계적 문헌고찰이 다수 존재하며, CSD 억제라는 기전적 타당성도 확인됩니다. 다만 대부분의 임상시험이 소규모(n<100)이거나 조기 종료(NCT02492295)된 사례가 있어, 대규모 확증 임상시험 없이 바로 적응증 확대를 진행하기에는 근거가 제한적입니다.

**진행하려면 필요한 것:**
- 한국 내 Propofol 허가사항(경고, 금기, DDI) 확보 — 현재 Evidence Pack에 안전성 데이터 부재
- 상세 작용기전(MOA) 자료 확보 및 편두통 병태생리와의 연관성 정밀 검증
- 대규모 다기관 RCT를 통한 유효 용량 및 안전 프로파일 재확인
- 성인/소아 대상별 하위집단 분석(현재 근거는 대부분 소아 응급실 환경에 편중)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

