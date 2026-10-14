---
layout: default
title: Danazol
parent: 높은 근거 (L1-L2)
nav_order: 248
evidence_level: L2
indication_count: 10
---

# Danazol
{: .fs-9 }

근거 수준: **L2** | 예측 적응증: **10** 건
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

# Danazol: 허가 적응증에서 유방 섬유낭성 질환으로

## 한 문장 요약

Danazol은 한국에서 2개 허가증으로 시판 중인 합성 안드로겐 계열 약물입니다. 허가 적응증 문구는 문서 링크로만 확인되어 구체적인 질환명은 이 보고서에서 확인하지 못했습니다.
TxGNN 모델은 **유방 섬유낭성 질환(breast fibrocystic disease)**에 효과가 있을 수 있다고 예측하며, 현재 **2건의 임상시험**(모두 국소제형 시험)과 **20편의 문헌**이 이 방향을 지지합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가증에 링크 형태로만 기재되어 있어 본문 확인 불가 (허가사항 PDF 참조) |
| 예측 신규 적응증 | 유방 섬유낭성 질환 (breast fibrocystic disease) |
| TxGNN 예측 점수 | 99.9996% |
| 근거 수준 | L2 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 2건 |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 DrugBank에 등록되어 있지 않습니다. 알려진 정보에 따르면 Danazol은 항고나도트로핀 작용을 가진 합성 안드로겐입니다. 뇌하수체의 FSH/LH 분비를 억제하고 난소의 에스트로겐 생성을 낮추며, 유방 조직에도 직접 작용하는 것으로 알려져 있습니다.

유방 섬유낭성 질환은 에스트로겐 우세와 프로게스테론 결핍 같은 호르몬 환경과 관련이 있어, 주기적인 결절과 통증이 나타납니다. Danazol의 호르몬 억제 작용은 이러한 병태와 기전상 맞닿아 있습니다. 해외에서는 이 질환에 대한 치료제로 승인된 이력이 있으며, 2017년 시험관 연구에서는 Danazol이 섬유낭성 유방 세포(MCF10A)의 미토콘드리아 대사를 변화시키는 것으로 보고되었습니다.

다만 아래 두 임상시험은 국소 도포제(FP1198 및 국소 Danazol)를 평가한 것이어서, 경구 Danazol의 효능을 직접 입증하지는 않습니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00744276](https://clinicaltrials.gov/study/NCT00744276) | Phase 2 | 완료 | 60 | 섬유낭성 유방 질환 통증에서 국소 Danazol 3개 용량 vs 위약 (무작위, 이중맹검, 용량 탐색). 안전성 및 적정 용량 평가 |
| [NCT01105793](https://clinicaltrials.gov/study/NCT01105793) | Phase 2 | 완료 | 20 | 주기성 유방통에서 국소 FP1198의 안전성 및 임상 활성 평가 (공개 라벨, 소규모) |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [3074777](https://pubmed.ncbi.nlm.nih.gov/3074777/) | 1988 | 무작위 이중맹검 시험 | Aust N Z J Obstet Gynaecol | 80명의 주기성 양성 유방 이형성 여성에서 Danazol 200 mg 하루 2회 투여 시 통증, 압통, 결절이 유의하게 개선 |
| [6373293](https://pubmed.ncbi.nlm.nih.gov/6373293/) | 1984 | 이중맹검 교차시험 | Eur J Gynaecol Oncol | 중증 양성 유방증 38명 중 32명에서 Danazol 400 mg/일 투여 시 개선 |
| [6594009](https://pubmed.ncbi.nlm.nih.gov/6594009/) | 1984 | 코호트 | Acta Obstet Gynecol Scand Suppl | 중증 증상성 섬유낭성 유방 질환에서 Danazol 치료 및 장기 추적 |
| [7386553](https://pubmed.ncbi.nlm.nih.gov/7386553/) | 1980 | 임상연구 | Am J Obstet Gynecol | 양성 유방 질환 130명에서 100~400 mg/일 투여, 약 2/3에서 결절 소실 |
| [7409245](https://pubmed.ncbi.nlm.nih.gov/7409245/) | 1980 | 임상연구 | Fertil Steril | 100~400 mg/일, 3~6개월 투여로 섬유낭성 질환에서 효과 확인 |
| [7041729](https://pubmed.ncbi.nlm.nih.gov/7041729/) | 1982 | Review | Ann Intern Med | Danazol이 유방 낭성 질환 치료로 승인되었으며 대체로 내약성이 양호함 |
| [3511705](https://pubmed.ncbi.nlm.nih.gov/3511705/) | 1986 | Review | Am J Obstet Gynecol | 섬유낭성 유방 질환의 병태생리, 병리, 임상상 및 관리 |
| [16444894](https://pubmed.ncbi.nlm.nih.gov/16444894/) | 2005 | Review | J Reprod Med | 유방통의 치료 접근법 |
| [3314435](https://pubmed.ncbi.nlm.nih.gov/3314435/) | 1987 | Review | Am Fam Physician | 증상 완화 방법의 하나로 Danazol 치료 언급 |
| [28649033](https://pubmed.ncbi.nlm.nih.gov/28649033/) | 2017 | 시험관 연구 | Breast | Danazol이 섬유낭성 유방 MCF10A 세포의 미토콘드리아 대사를 변화시킴 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 198401028 | 영풍다나졸캡슐(수출용) | 캡슐제 | 허가사항 PDF 참조 (https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/198401028/EE) |
| 198401033 | 영풍다나졸200mg캡슐 | 캡슐제 | 허가사항 PDF 참조 (https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/198401033/EE) |

## 안전성 고려사항

- **약물 상호작용**: 데이터베이스에서 총 100건이 조회되었으며, 아래는 일부입니다.
  - **주요(Major)**: Cisapride
  - **중등도(Moderate)**: 혈당강하제 다수 (Acarbose, Alogliptin, Canagliflozin, Dapagliflozin, Empagliflozin, Glimepiride, Glipizide, Glyburide, 인슐린 등), GLP-1 계열 (Albiglutide, Dulaglutide, Exenatide), Budesonide, Eliglustat
- 문헌상 보고된 위험: Lovastatin과 병용 시 횡문근융해 및 췌장염 사례(PMID 18691993), 안드로겐성 이상반응, 최기형성(피임 필요)
- 허가사항의 경고 및 금기 정보는 이 보고서에 수집되지 않았으므로 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
유방 섬유낭성 질환에 대해 Danazol의 무작위 이중맹검 시험과 교차시험 등 다수의 임상 보고가 있고, 해외에서 승인된 이력도 있습니다. 다만 직접 근거는 1980년대 연구에 집중되어 있고, 등록된 임상시험 2건은 국소제형이어서 경구 제형의 근거로는 간접적입니다.

**진행하려면 필요한 것:**
- 허가사항 PDF에서 경고, 금기 및 허가 적응증 확인 (현재 안전성 선별 진행 불가 상태)
- 상세한 작용 기전 데이터 (DrugBank 등)
- 국소제형 시험(FP1198 등)과 경구 Danazol의 관계 확인
- 안드로겐성 이상반응, 최기형성(피임), 혈당강하제 및 스타틴 병용 시 모니터링 계획

## 참고: 기타 예측 적응증

| 순위 | 질환 | 근거 수준 | 권장 |
|------|------|----------|------|
| 2 | 무월경 (약리학적 효과, 자궁내막증 등에서의 월경 억제) | L3 | Proceed with Guardrails |
| 3 | 양성 유방 이형성 | L3 | Proceed with Guardrails |
| 9 | 유방 선증 (breast adenosis) | L3 | Research Question |
| 7 | 유방 농양 (1986년 증례 보고) | L4 | Research Question |
| 4~6, 8, 10 | 둔관 선증, 아포크린 선증, 유방 지방괴사, 수유 질환, 외음질염 | L4~L5 | Hold |
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

