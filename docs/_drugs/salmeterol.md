---
layout: default
title: Salmeterol
parent: 모델 예측만 (L5)
nav_order: 683
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-15
description: "Salmeterol: 예측 신규 적응증 기관지염 (Bronchitis) (근거 수준 L5). 기존 적응증: 허가증에 적응증 원문이 제공되지 않았습니다. 허가사항 링크만 확인되며, 일반적으로 천식·COPD에 사용되는 흡입제입니다"
---

# Salmeterol
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **7** 건
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

# Salmeterol: 천식·만성 폐쇄성 폐질환에서 기관지염으로

## 한 문장 요약

Salmeterol은 지속성 β2 작용제로, 한국에서는 플루티카손프로피오네이트와의 흡입 복합제 형태로 허가·시판되고 있습니다. TxGNN 모델은 **기관지염(bronchitis)**에 효과가 있을 수 있다고 예측하며, 현재 **9건의 임상시험**과 **20편의 문헌**이 이 방향을 다룹니다. 다만 여기서 기관지염은 급성이 아닌 만성 기관지염/COPD를 뜻하므로, 새로운 적응증이라기보다 기존 사용 범위의 연장에 가깝습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가증에 적응증 원문이 제공되지 않았습니다. 허가사항 링크만 확인되며, 일반적으로 천식·COPD에 사용되는 흡입제입니다. |
| 예측 신규 적응증 | 기관지염 (Bronchitis) |
| TxGNN 예측 점수 | 99.92% |
| 근거 수준 | L1 (완료된 Phase 3 임상시험이 여러 건 있으나, 일부는 간접 근거) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 6건 |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 salmeterol은 지속성 β2 아드레날린 수용체 작용제로, cAMP를 매개로 기도 평활근을 이완시켜 기관지를 확장합니다. 또한 점액섬모 청소율을 높일 수 있어 만성 기관지염의 증상(기침, 객담)과 관련이 있습니다.

기관지염은 COPD의 한 표현형(만성 기관지염)에 해당하며, COPD 환자를 대상으로 한 Phase 3 임상시험에서 salmeterol 또는 salmeterol/fluticasone의 효능이 여러 차례 평가되었습니다. 따라서 이 예측은 완전히 새로운 용도가 아니라 이미 확립된 호흡기 질환 적응증의 연장으로 보는 것이 적절합니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT02173691](https://clinicaltrials.gov/study/NCT02173691) | Phase 3 | 완료 | 584 | COPD에서 tiotropium, salmeterol, 위약의 6개월 기관지확장 효능·안전성 비교 |
| [NCT00269087](https://clinicaltrials.gov/study/NCT00269087) | Phase 3 | 완료 | 122 | 만성 기관지염·폐기종 포함 COPD에서 salmeterol/fluticasone 50/500µg 56주 장기 안전성 평가 |
| [NCT00268177](https://clinicaltrials.gov/study/NCT00268177) | Phase 3 | 완료 | 130 | COPD에서 salmeterol/fluticasone 대 위약의 13주 기관지 항염증 효과 비교 |
| [NCT00269126](https://clinicaltrials.gov/study/NCT00269126) | Phase 3 | 완료 | 150 | COPD에서 두 약물 효과 비교 (상세 비교 내용은 확인되지 않음) |
| [NCT00064415](https://clinicaltrials.gov/study/NCT00064415) | Phase 3 | 완료 | 799 | arformoterol 12개월 장기 안전성 연구 (salmeterol은 간접 비교 대상으로 추정) |
| [NCT00064402](https://clinicaltrials.gov/study/NCT00064402) | Phase 3 | 완료 | 741 | arformoterol의 12주 기관지확장 효과 (salmeterol은 비교 대상으로 추정, 간접 근거) |
| [NCT00403286](https://clinicaltrials.gov/study/NCT00403286) | Phase 2 | 완료 | 457 | fluticasone/formoterol 용량 탐색 (salmeterol 복합제 대비, 간접 근거) |
| [NCT01361984](https://clinicaltrials.gov/study/NCT01361984) | Phase 4 | 불명 | 20 | 분무 arformoterol과 salmeterol 건조분말 흡입기의 흡기용량 비교 |
| [NCT00233051](https://clinicaltrials.gov/study/NCT00233051) | 해당 없음 | 조기 종료 | 20 | COPD에서 유도 객담 염증 매개물질을 약물 반응 바이오마커로 평가 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [17557771](https://pubmed.ncbi.nlm.nih.gov/17557771/) | 2007 | RCT | Thorax | COPD에서 salmeterol/fluticasone의 기도 염증 영향 평가 |
| [17196106](https://pubmed.ncbi.nlm.nih.gov/17196106/) | 2006 | 메타분석 | Respir Res | COPD에서 salmeterol 50µg 1일 2회가 위약/통상 치료보다 임상 지표 개선 |
| [15970448](https://pubmed.ncbi.nlm.nih.gov/15970448/) | 2006 | 임상시험 | Pulm Pharmacol Ther | 경증~중등도 만성 기관지염 환자 14명 대상 salmeterol의 점액섬모·기침 청소 효과 평가 |
| [15329047](https://pubmed.ncbi.nlm.nih.gov/15329047/) | 2004 | Review | Drugs | 만성 기관지염 관련 COPD에서 salmeterol/fluticasone 사용 검토 |
| [12970006](https://pubmed.ncbi.nlm.nih.gov/12970006/) | 2003 | 임상시험 | Chest | COPD에서 fluticasone 250µg/salmeterol 50µg 복합제와 위약·단독제 비교 |
| [19210134](https://pubmed.ncbi.nlm.nih.gov/19210134/) | 2009 | 코호트 | Curr Med Res Opin | 만성 기관지염 환자에서 fluticasone/salmeterol 시작 후 의료 이용 및 비용 비교 |
| [19124357](https://pubmed.ncbi.nlm.nih.gov/19124357/) | 2008 | 임상시험 | Ther Adv Respir Dis | COPD에서 arformoterol과 salmeterol의 12개월 안전성·내약성 평가 |
| [9916607](https://pubmed.ncbi.nlm.nih.gov/9916607/) | 1998 | 임상시험 | Clin Ther | 경증~중등도 COPD에서 흡입 salmeterol과 경구 theophylline 비교 |
| [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/) | 2015 | 가이드라인 | Basic Clin Pharmacol Toxicol | 핀란드 안정형 COPD 진단·약물치료 가이드라인 |
| [12236842](https://pubmed.ncbi.nlm.nih.gov/12236842/) | 2002 | Review | Br J Clin Pharmacol | 지속성 β2 작용제의 길항 작용 및 ICS 절감 효과 검토 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201400305 | 플루테롤흡입용캡슐500/50 (한미약품) | 흡입용 캡슐 | 허가사항 문서 링크 참조 |
| 201400307 | 플루테롤흡입용캡슐250/50 (한미약품) | 흡입용 캡슐 | 허가사항 문서 링크 참조 |
| 201400306 | 플루테롤흡입용캡슐100/50 (한미약품) | 흡입용 캡슐 | 허가사항 문서 링크 참조 |
| 201900814 | 콤포나콤팩트에어100/50 (대원제약) | 흡입제 | 허가사항 문서 링크 참조 |
| 201900815 | 콤포나콤팩트에어250/50 (대원제약) | 흡입제 | 허가사항 문서 링크 참조 |

## 안전성 고려사항

- **약물 상호작용**: 총 600건이 조회되었으며, 주요 항목은 다음과 같습니다.
  - Major: Clarithromycin
  - Moderate: Epinephrine, Famotidine, Acarbose, Isometheptene, Dolasetron, 일부 혈당강하제(Canagliflozin, Dapagliflozin, Empagliflozin, Alogliptin, Albiglutide, Dulaglutide, Chlorpropamide) 등
  - Minor: Hydrocortisone, Dexamethasone, Budesonide 등 코르티코스테로이드
- **지식그래프 기반 금기 관련 질환**: 고혈압, QT 연장 증후군, 간질, 고혈당, 단순포진 각막염, 뇌하수체 기능저하증, 골다공증 등이 연관되어 있습니다. 이는 허가사항 문구가 아닌 지식그래프 정보이므로 허가사항에서 확인이 필요합니다.
- **사용상 주의**: 천식에서는 LABA 단독요법을 피하고 흡입 코르티코스테로이드와 병용해야 하며, 심혈관계 영향을 모니터링해야 합니다.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
COPD/만성 기관지염 환자를 대상으로 한 여러 Phase 3 임상시험과 메타분석, RCT가 salmeterol 및 salmeterol/fluticasone의 효능과 안전성을 뒷받침합니다. 다만 이는 기존 적응증의 연장이며, 일부 시험은 비교약으로만 salmeterol을 포함해 간접 근거입니다. 급성 기관지염에 대한 근거는 아닙니다.

**진행하려면 필요한 것:**
- 한국 허가사항(적응증, 경고, 금기)의 확인 및 정리
- 상세 작용 기전 데이터 확보
- 적용 대상을 만성 기관지염/COPD로 명확히 한정
- 심혈관계 및 QT 연장 위험 환자에 대한 안전성 모니터링 계획
- 병용 시 Clarithromycin 등 Major 상호작용 관리 지침

---

**참고: 다른 예측 적응증 요약**

| 순위 | 예측 질환 | 근거 수준 | 권장 결정 | 비고 |
|----|---------|---------|---------|------|
| 3 | 폐쇄성 폐질환 | L1 | Proceed with Guardrails | 기존 적응증과 중복, 확인 성격 |
| 5 | 천식 | L1 | Proceed with Guardrails | 기존 적응증, ICS 병용 필수 |
| 2 | 호흡기 기형 | L4 | Hold | 구조적 기형에 대한 근거 없음 |
| 7 | 아토피 피부염 | L4 | Hold | 전임상·기전 근거만 있고 임상시험 없음 |
| 4 | Rienhoff 증후군 | L5 | Hold | 모델 예측만 존재 |
| 6 | 천식 관련 형질(감수성) | L5 | Hold | 유전적 감수성 형질로 치료 대상이 아님 |
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

