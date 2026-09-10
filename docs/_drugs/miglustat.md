---
layout: default
title: Miglustat
parent: 僅模型預測 (L5)
nav_order: 480
evidence_level: L5
indication_count: 10
---

# Miglustat
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

# Miglustat: 국내 미시판 상태에서 고셔병(Gaucher Disease)으로

## 한 문장 요약

Miglustat은 글로벌 임상 자료상 이미 1형 고셔병(Type 1 Gaucher Disease) 치료에 쓰이는 경구 기질감소요법(SRT) 약물이나, 국내(한국) 허가 자료는 확보되어 있지 않습니다(허가증 0건, 미시판). TxGNN 모델은 1순위로 **고셔병**을 예측했으며(예측 점수 99.88%), 이는 신규 발견이라기보다는 이미 알려진 적응증을 모델이 재확인한 결과에 가깝습니다. 현재 **4건의 관련 임상시험**과 **18편의 문헌**이 이 방향을 뒷받침합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 국내 허가 자료 없음(데이터 갭) — 다만 근거 자료상 해외에서는 이미 1형 고셔병 치료제로 승인되어 있음 |
| 예측 신규 적응증 | 고셔병 (Gaucher Disease) |
| TxGNN 예측 점수 | 99.88% |
| 근거 수준 | L1 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

Miglustat은 이미노당(iminosugar) 계열의 글루코실세라마이드 합성효소(glucosylceramide synthase) 억제제로, 기질감소요법(Substrate Reduction Therapy, SRT)에 해당합니다. 1형 고셔병은 GBA 유전자 결함으로 대식세포 리소좀 내에 글루코세레브로사이드가 축적되는 질환인데, miglustat은 이 기질의 합성 자체를 줄여 축적을 억제합니다.

이 기전적 연관성은 우연이 아니라 이미 확립된 사실입니다 — Miglustat(Zavesca)은 효소대체요법(ERT)에 적합하지 않은 경증~중등도 1형 고셔병 환자를 대상으로 해외에서 이미 승인된 적응증입니다. 따라서 이번 예측은 "새로운 가설"이라기보다 TxGNN 모델이 실제 승인 적응증을 정확히 재현했음을 보여주는 양성 대조(positive control) 성격이 강하며, 국내 관점에서는 "국내 미도입 약물의 도입/허가 검토" 성격의 후보로 이해하는 것이 정확합니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00319046](https://clinicaltrials.gov/study/NCT00319046) | Phase 3 | 완료 | 42 | ERT에서 miglustat 유지요법으로 전환 후 장기 유효성·안전성·내약성 평가(개방표지, 비교군 없음) |
| [NCT00041535](https://clinicaltrials.gov/study/NCT00041535) | Phase 1/2 | 완료 | 30 | 신경병증형 고셔병 환자 대상 무작위 대조 연구 |
| [NCT02520934](https://clinicaltrials.gov/study/NCT02520934) | NA | 상태 불명 | 19 | 고셔병 IIIB형에서 miglustat + ERT 병용요법 평가 |
| [NCT03822013](https://clinicaltrials.gov/study/NCT03822013) | Phase 3 | 중단 | 30 | 영아형 Sandhoff/Tay-Sachs 병(신경병증형 고셔병 인접군)에서 신경학적·전신 증상에 대한 효과 조사 |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [16247743](https://pubmed.ncbi.nlm.nih.gov/16247743/) | 2005 | Review/Guideline | American Journal of Hematology | 1형 고셔병에서 miglustat 사용에 대한 가이던스(전문가 패널) |
| [25812601](https://pubmed.ncbi.nlm.nih.gov/25812601/) | 2015 | Systematic Review | Cochrane Database of Systematic Reviews | 고셔병에서 ERT·SRT 치료 효과 체계적 고찰 |
| [35815393](https://pubmed.ncbi.nlm.nih.gov/35815393/) | 2023 | Systematic Review/Meta-analysis | Annals of Pharmacotherapy | 고셔병 약물치료에 대한 종단연구 체계적 고찰 및 메타분석 |
| [14605497](https://pubmed.ncbi.nlm.nih.gov/14605497/) | 2003 | Position Statement | Journal of Inherited Metabolic Disease | 1형(비신경병증형) 고셔병 관리에서 miglustat 역할에 대한 국제 전문가 성명 |
| [19210136](https://pubmed.ncbi.nlm.nih.gov/19210136/) | 2009 | Cohort | Current Medical Research and Opinion | 1형 고셔병에서 miglustat을 이용한 목표지향적 치료 |
| [12556220](https://pubmed.ncbi.nlm.nih.gov/12556220/) | 2003 | Review | Expert Opinion on Investigational Drugs | 1형 고셔병 증상 완화를 위한 기질감소요법으로서 miglustat |
| [12803930](https://pubmed.ncbi.nlm.nih.gov/12803930/) | 2003 | Review | Phil. Trans. R. Soc. B | 고셔병에서 기질감소요법의 임상 경험 |
| [14609352](https://pubmed.ncbi.nlm.nih.gov/14609352/) | 2003 | Drug Review | Drugs | Miglustat 약물 자체에 대한 종합 리뷰(고셔병 임상시험 결과 포함) |
| [28218669](https://pubmed.ncbi.nlm.nih.gov/28218669/) | 2017 | Review | Int J Mol Sci | 고셔병 병태생리·임상양상·치료법 전반에 대한 리뷰 |
| [24259734](https://pubmed.ncbi.nlm.nih.gov/24259734/) | 2013 | Review | Annals of Pharmacotherapy | 고셔병 역학·병태생리 및 치료옵션(ERT/SRT) 검토 |

---

## 한국 시판 정보

국내(한국) 허가 자료가 확인되지 않습니다 — 허가증 0건, 미시판 상태입니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

> 참고: 이번 Evidence Pack에서는 국내(식약처 상당 기관) 경고·금기 정보 확보가 **차단(Blocking) 등급 데이터 갭**으로 분류되어 있어(DG001), 안전성 초기 평가(S1) 단계 진입이 불가능한 상태입니다.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
고셔병에 대한 miglustat의 효능은 다수의 임상시험(Phase 1/2 RCT 포함)과 가이드라인급 문헌(전문가 패널 성명, Cochrane 체계적 고찰 등)으로 뒷받침되며, 해외에서 이미 승인된 적응증입니다. 다만 이는 "신규 발견"이 아니라 모델 검증(positive control) 성격이 강하고, 국내 허가·유통 정보가 전무하여 실제 국내 도입 가능성 검토가 우선 과제입니다.

**진행하려면 필요한 것:**
- 국내(식약처 상당 기관) 허가사항/경고·금기 문서 확보 (DG001, Blocking — S1 안전성 초기평가 진입 필수 조건)
- DrugBank 등에서 상세 작용기전(MOA) 데이터 확보 (DG002, High)
- 국내 도입 시 필요한 희귀질환 의약품 허가 경로 검토
- 순위 2~10위 예측 적응증(대부분 L5/Hold, 임상·문헌 근거 없음)은 현 시점에서 우선순위 낮음 — 추가 전임상/기전 검증 선행 필요
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

