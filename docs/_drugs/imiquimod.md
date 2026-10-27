---
layout: default
title: Imiquimod
parent: 모델 예측만 (L5)
nav_order: 419
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Imiquimod: 예측 신규 적응증 전암성 신생물 (pre-malignant neoplasm) (근거 수준 L5). 기존 적응증: 허가 적응증 원문 텍스트가 확보되지 않음 (식약처 허가정보 링크만 확인됨)"
monitor_inn: "Imiquimod"
predicted_indications: ["pre-malignant neoplasm", "benign neoplasm of buccal mucosa", "cervical neuroblastoma", "odontogenic cyst", "benign neoplasm of tongue", "nasopharyngeal teratoma", "cystic neoplasm", "inner ear neoplasm", "neoplasm of major salivary gland", "schwannoma of jugular foramen"]
---

# Imiquimod
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

## Imiquimod: 국소 면역조절제에서 전암성 신생물로
{: .text-alpha }

## 한 문장 요약

Imiquimod은 국내에서 크림제(알다라크림)로 시판 중인 TLR7 작용제 계열의 국소 면역조절제입니다.
TxGNN 모델은 **전암성 신생물(pre-malignant neoplasm)**에 효과가 있을 수 있다고 예측하며, 현재 **2건의 임상시험(Phase 3)**과 **9편의 문헌**이 이 방향을 지지합니다. 다만 두 임상시험 모두 규모가 작아(각각 20명, 9명) 직접 근거의 강도는 제한적입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 원문 텍스트가 확보되지 않음 (식약처 허가정보 링크만 확인됨) |
| 예측 신규 적응증 | 전암성 신생물 (pre-malignant neoplasm) |
| TxGNN 예측 점수 | 99.92% |
| 근거 수준 | L1 (아래 참고) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | Proceed with Guardrails |

> **근거 수준에 대한 참고**: 완료된 Phase 3 시험은 1건(NCT00175643, 20명, 단일군)뿐이며, 다른 Phase 3 시험은 9명 등록 후 조기 종료되었습니다. 엄격한 판정 규칙(완료된 Phase 3 RCT 2건 이상)으로는 L1 요건을 충족하지 못하므로, 실제 근거 강도는 L1보다 낮게 해석해야 합니다. 이 점이 가드레일을 두고 진행해야 하는 주된 이유입니다.

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 데이터베이스에서 확보되지 않았습니다. 다만 알려진 정보에 따르면 Imiquimod은 TLR7 작용제로, 국소 투여 시 IFN-α, TNF-α, IL-12 분비를 유도하여 선천 및 적응 항종양 면역을 활성화합니다.

이러한 면역 활성화는 광선각화증, 자궁경부·외음부·항문의 상피내 신생물 등 전암성 상피 병변에 직접 관련됩니다. 광선각화증에 대한 사용 경험과 외음부·항문 상피내 신생물에 대한 Cochrane 체계적 문헌고찰이 생물학적 타당성을 뒷받침합니다.

다만 두 Phase 3 시험의 규모가 작고 그중 하나는 조기 종료되어, 직접적인 효능 근거는 제한적입니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00175643](https://clinicaltrials.gov/study/NCT00175643) | Phase 3 | 완료 | 20 | 두부 광선각화증에서 Imiquimod 5% 크림 주 3회, 1~2주기 투여의 안전성·효과 지속 기간을 평가한 공개 라벨 연구 (단일군) |
| [NCT02329171](https://clinicaltrials.gov/study/NCT02329171) | Phase 3 | 조기 종료 | 9 | 고등급 자궁경부 상피내 신생물(CIN 2-3)에서 국소 Imiquimod의 효과를 평가한 무작위 대조 시험. 9명 등록 후 종료되어 결론적 근거 부족 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [23235673](https://pubmed.ncbi.nlm.nih.gov/23235673/) | 2012 | Review (Cochrane) | Cochrane Database Syst Rev | 항문관 상피내 신생물의 중재법 고찰 |
| [21491403](https://pubmed.ncbi.nlm.nih.gov/21491403/) | 2011 | Review (Cochrane) | Cochrane Database Syst Rev | 고등급 외음부 상피내 신생물의 내과적 중재법 고찰 |
| [26516853](https://pubmed.ncbi.nlm.nih.gov/26516853/) | 2015 | Review | Int J Mol Sci | 비흑색종 피부암에 대한 광역동요법 병용 치료 |
| [20505896](https://pubmed.ncbi.nlm.nih.gov/20505896/) | 2010 | Review | Skin Therapy Lett | 광선각화증의 현재 관리법 (파괴적, 국소 및 시술적 치료) |
| [15584683](https://pubmed.ncbi.nlm.nih.gov/15584683/) | 2004 | Review | Semin Cutan Med Surg | 비흑색종 피부암 및 전구 병변의 국소 치료 전략 (fluorouracil, diclofenac, imiquimod, PDT) |
| [30284955](https://pubmed.ncbi.nlm.nih.gov/30284955/) | 2019 | Case report | Int J STD AIDS | 신장 이식 환자의 고등급 외음부 상피내 신생물을 Imiquimod 5%로 성공적으로 치료 |
| [15601490](https://pubmed.ncbi.nlm.nih.gov/15601490/) | 2004 | Case report | Int J STD AIDS | 음경 보웬양 구진증을 Imiquimod 5% 크림으로 치료하여 소실 |
| [29500135](https://pubmed.ncbi.nlm.nih.gov/29500135/) | 2018 | Preclinical | Urol Oncol | TLR7 작용제(TMX-101, TMX-202)의 방광 내 투여 약동학·약력학 (쥐 모델) |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200710217 | 알다라크림(이미퀴모드) (동아에스티) | 크림 (백색 또는 미황색) | 허가 적응증 원문은 [식약처 허가정보](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200710217/EE) 참조 |

## 세포독성

Imiquimod은 세포독성 화학요법제가 아니라 국소 면역반응 조절제이므로, 이 섹션은 해당하지 않습니다.

## 안전성 고려사항

- **지식그래프 기반 금기 관련 질환** (허가사항 문구가 아닌 예측 모델 지식그래프 기준): 광발작 반응, 광과민성 질환, 자가면역질환, 이식편대숙주병, 일광화상
- **약물 상호작용**: 59건이 조회되었으나 상호작용 수준은 모두 미분류입니다. 주요 항목은 Pantoprazole, Morphine, Omeprazole, Lansoprazole, Prednisone, Simvastatin, Warfarin, Clopidogrel, Hydroxychloroquine 등입니다. 국소 제형이므로 임상적 의미는 별도 확인이 필요합니다.

허가사항상의 경고 및 금기는 식약처 허가사항을 직접 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
Imiquimod은 TLR7 매개 면역 활성화라는 타당한 기전과 광선각화증 및 상피내 신생물에 대한 Cochrane 문헌고찰·증례 근거를 갖추고 있습니다. 그러나 직접 근거인 Phase 3 시험이 소규모(20명)이거나 조기 종료(9명)되어 근거가 확정적이지 않으므로 보호 장치를 두고 진행해야 합니다.

**진행하려면 필요한 것:**
- 식약처 허가사항(적응증, 경고, 금기) 원문 확보 및 분석. 현재 가장 큰 차단 요인입니다.
- DrugBank 등에서 작용 기전(MOA) 데이터 보완
- 충분한 규모의 무작위 대조 시험 근거 추가 확인 (특히 상피내 신생물 대상)
- 광과민성·자가면역질환 환자 등 지식그래프상 금기 관련 인구집단에 대한 안전성 모니터링 계획

**참고: 기타 예측 적응증**
- 구강 협측 점막 양성 신생물: L4, 임상시험 없음, 전임상·증례 위주. 구강 유두종증의 악성 전환 사례가 보고되어 연구 질문 수준(Research Question)입니다.
- 치성 낭종: 근거는 Gorlin 증후군의 기저세포암 치료에 대한 것으로 간접적이며, 보류(Hold)입니다.
- 경부 신경모세포종, 비인두 기형종, 주타액선 신생물, 경정맥공 신경초종, 내이 신생물, 혀 양성 신생물, 낭성 신생물: 모델 예측 외에 직접 근거가 없거나 부적합하여 보류(Hold)입니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

