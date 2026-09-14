---
layout: default
title: Tenoxicam
parent: 僅模型預測 (L5)
nav_order: 668
evidence_level: L5
indication_count: 10
---

# Tenoxicam
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

# Tenoxicam: 기존 적응증 미확인에서 류마티스 관절염으로

## 한 문장 요약

Tenoxicam은 oxicam 계열 NSAID로, 한국 내 허가 및 규제 데이터가 확보되지 않아 기존 승인 적응증을 확인할 수 없습니다. TxGNN 모델은 **류마티스 관절염(Rheumatoid Arthritis)**에 효과가 있을 것으로 예측하며, 현재 **1건의 임상시험**과 **20편 이상의 문헌**(1980~90년대 다수의 RCT 포함)이 이를 지지합니다. 다만 이 문헌들은 tenoxicam이 이미 오래전부터 류마티스 관절염 치료에 사용되어 온 NSAID임을 보여주고 있어, 진정한 의미의 "신규 적응증"이라기보다 **기존 약물 계열 효능의 재확인**에 가깝다는 점에 유의해야 합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (규제 데이터 미비 — 다만 문헌상 NSAID로서 관절염 계열 질환에 전통적으로 사용됨) |
| 예측 신규 적응증 | 류마티스 관절염 (Rheumatoid Arthritis) |
| TxGNN 예측 점수 | 99.90% |
| 근거 수준 | L1 |
| 한국 시판 현황 | 미시판 (허가 없음) |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

현재 DrugBank 등에서 확보된 상세 작용기전(MOA) 데이터는 없습니다. 다만 확보된 문헌에 따르면 tenoxicam은 oxicam 계열 비스테로이드성 항염증제(NSAID)로, COX-1/COX-2를 비선택적으로 억제하여 프로스타글란딘 합성을 줄이는 명확한 항염증·진통 기전을 가지고 있습니다. 이는 류마티스 관절염의 병태생리(활막 염증, 프로스타글란딘 매개 통증)와 직접적으로 연관됩니다.

다만 중요한 주의점이 있습니다. 문헌 근거의 상당수가 1985~1996년 사이의 piroxicam·aceclofenac·naproxen 등과의 비교 RCT로, tenoxicam이 이미 국제적으로 류마티스 관절염 치료제로 널리 사용되어 온 이력을 보여줍니다. 즉 이 예측은 새로운 치료 영역을 발굴했다기보다, **기존에 확립된 NSAID 계열 효능을 TxGNN이 재확인**한 결과일 가능성이 높습니다. 한국에서는 현재 허가 이력이 없어 실제 재창출 가치는 "국내 도입 가능성 검토" 관점에서 평가해야 합니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT05508451](https://clinicaltrials.gov/study/NCT05508451) | NA | 완료 | 80 | 양악수술 환자의 수술 후 통증에서 Tenoxicam, Paracetamol, 병용요법의 진통 효과 비교. RA 특이적 시험은 아니며 통증 관리 관점의 지지 근거. |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [1593574](https://pubmed.ncbi.nlm.nih.gov/1593574/) | 1992 | RCT | J Rheumatol | RA 환자 102명, Tenoxicam 20mg vs Piroxicam 20mg 1일1회 비교 — 유효성·안전성 동등 |
| [8894360](https://pubmed.ncbi.nlm.nih.gov/8894360/) | 1996 | RCT | Clin Rheumatol | RA 환자 292명, Aceclofenac vs Tenoxicam 3개월 다기관 RCT — 양군 모두 임상지표 개선 |
| [2292331](https://pubmed.ncbi.nlm.nih.gov/2292331/) | 1990 | Multicentre trial | J Int Med Res | 일반진료 2,963명 대상 12주 투여 — 통증·뻣뻣함 개선, 장기 복약 지속률 양호 |
| [3915889](https://pubmed.ncbi.nlm.nih.gov/3915889/) | 1985 | Clinical trial | Eur J Rheumatol Inflamm | RA·관절증 79명, 직장 좌제(20mg/day) 6주 개방연구 — 임상 유효성 확인 |
| [3915885](https://pubmed.ncbi.nlm.nih.gov/3915885/) | 1985 | Clinical evaluation | Eur J Rheumatol Inflamm | OA/RA/강직척추염 대상 Piroxicam 이중맹검 비교 — 동등 이상 효과 |
| [1711963](https://pubmed.ncbi.nlm.nih.gov/1711963/) | 1991 | Review | Drugs | RA·OA·강직척추염 등 류마티스 질환 전반에서 유효성·내약성 확인 |
| [8137596](https://pubmed.ncbi.nlm.nih.gov/8137596/) | 1994 | Review (PK) | Clin Pharmacokinet | 경구 완전흡수, 혈장단백결합 99%, 약동학 특성 정리 |
| [3262939](https://pubmed.ncbi.nlm.nih.gov/3262939/) | 1988 | PK study | Ther Drug Monit | RA/OA 환자의 활막액-혈장 약동학 분포비 결정요인 분석 |
| [8187453](https://pubmed.ncbi.nlm.nih.gov/8187453/) | 1994 | Mechanistic study | Clin Rheumatol | RA 환자·건강대조군의 호중구 화학주성에 대한 영향 평가 |
| [41419140](https://pubmed.ncbi.nlm.nih.gov/41419140/) | 2026 | 최신 제형 연구 | Eur J Pharm Sci | Baricitinib+Tenoxicam 나노스폰지 겔 — RA 국소치료용 신규 전달체 개발 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
류마티스 관절염에 대한 tenoxicam의 효능을 지지하는 다수의 RCT(1990년대 다기관 시험 포함)가 존재해 근거 수준은 L1로 높지만, 한국 내 허가 이력이 전무하고 TFDA/허가사항상 경고·금기 정보가 확보되지 않아(Blocking 등급 데이터 갭) 안전성 초기평가(S1) 단계로 진입할 수 없는 상태입니다. 또한 이 적응증이 실질적으로 "신규"인지, 아니면 기존 NSAID 계열의 이미 확립된 용도인지 별도 확인이 필요합니다.

**진행하려면 필요한 것:**
- 허가 라벨(경고·금기사항) 확보 — S1 안전성 초기평가의 필수 선결 조건 (Blocking)
- DrugBank 등을 통한 정확한 MOA·약물 분류 데이터 확보
- 국제 허가 현황 비교를 통해 류마티스 관절염이 tenoxicam의 기존 승인 적응증인지 여부 검증 (진정한 재창출 여부 확인)
- DDI 및 금기 정보 확보 후 정식 안전성 평가 진행
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

