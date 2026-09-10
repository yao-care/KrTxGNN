---
layout: default
title: Laronidase
parent: 僅模型預測 (L5)
nav_order: 426
evidence_level: L5
indication_count: 2
---

# Laronidase
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Laronidase: 원 적응증 정보 공백에서 골격 침범 동반 리소좀 축적병(무코다당증 I형)으로

## 한 문장 요약

Laronidase(DrugBank ID: DB00090)는 재조합 α-L-iduronidase 효소대체요법제입니다. 국내 허가 정보와 기존 적응증 필드는 자료 공백 상태이나, TxGNN 모델은 **골격 침범을 동반한 리소좀 축적병(무코다당증 I형에 해당)**에 효과가 있을 것으로 예측하며, 현재 등록된 임상시험은 없지만 **4편의 문헌**이 이를 뒷받침합니다. 다만 이 예측 질환은 laronidase의 국제 공인 원 적응증(무코다당증 I형)과 사실상 동일 질환으로, 엄밀한 의미의 신규 재창출이라기보다 기존 적응증 자료 누락에 따른 재확인에 가깝습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 자료 없음 (drug.original_indications 공백, licenses 없음). 단 문헌상 국제 승인 적응증은 무코다당증 I형(헐러/헐러-셰이/셰이 증후군) |
| 예측 신규 적응증 | 골격 침범 동반 리소좀 축적병 (Lysosomal Storage Disease with Skeletal Involvement) |
| TxGNN 예측 점수 | 99.31% |
| 근거 수준 | L1 |
| 국내 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold (자료 보완 후 재평가) |

---

## 이 예측이 타당한 이유는?

작용기전(MOA) 상세 데이터 자체는 확보되지 않았지만, evidence pack의 근거 설명에 따르면 laronidase는 결핍된 리소좀 효소 α-L-iduronidase를 보충하는 효소대체요법(ERT)입니다. 이는 IDUA 유전자 결함과 그로 인한 글리코사미노글리칸(GAG) 축적이라는 무코다당증 I형의 분자병인과 정확히 대응하는 기전입니다.

예측된 신규 적응증 "골격 침범 동반 리소좀 축적병"은 명칭 자체가 무코다당증 I형의 임상적 특징(골격계 침범을 동반하는 리소좀 축적 질환)을 그대로 기술한 것으로, laronidase의 기존 국제 승인 적응증과 실질적으로 동일한 질환군입니다.

이 항목이 "신규 예측"으로 표시된 이유는 drug.original_indications 필드가 자료 공백 상태였기 때문이며, 실제 기전상 새로운 발견이 아니라 기존 적응증의 재확인으로 해석하는 것이 타당합니다. TxGNN이 높은 점수를 부여한 것도 이러한 기전 일치성을 반영한 결과로 보입니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다. (ClinicalTrials.gov, ICTRP 조회 결과 모두 0건)

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [12196045](https://pubmed.ncbi.nlm.nih.gov/12196045/) | 2002 | 리뷰/약물 개요 | BioDrugs | BioMarin의 laronidase 개발 개요, MPS I(헐러증후군 포함) 치료 목적의 효소대체요법, 미국/유럽 희귀의약품 지정 및 FDA 패스트트랙 |
| [25345091](https://pubmed.ncbi.nlm.nih.gov/25345091/) | 2014 | 리뷰 | Pediatric Endocrinology Reviews | 무코다당증 I형의 병태생리(α-L-iduronidase 결핍, GAG 축적) 및 질환 스펙트럼(헐러/셰이/헐러-셰이) 개괄 |
| [18758061](https://pubmed.ncbi.nlm.nih.gov/18758061/) | 2008 | 체외 기전 연구 | Biological & Pharmaceutical Bulletin | MPS I 환자 유래 섬유아세포에서 laronidase가 mannose-6-phosphate 수용체를 통해 용량 의존적으로 흡수되어 리소좀에서 축적 기질을 분해함을 확인 |
| [23127271](https://pubmed.ncbi.nlm.nih.gov/23127271/) | 2012 | 증례보고 | Pediatric Neurology | 경증 MPS I(셰이 증후군) 소아 환자의 6.5년 추적 관찰, 효소대체요법 시행 후 전반적 상태 악화 및 질환 진행 관찰 |

---

## 국내 시판 정보

국내 허가증이 없어 미출시 상태입니다 (허가증 수: 0건).

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

(주요 경고·금기·DDI 데이터 모두 자료 공백 상태이며, DG001은 "Blocking" 등급으로 S1 안전성 초기 평가 진입 자체를 막고 있습니다.)

---

## 결론 및 다음 단계

**결정: Hold (자료 보완 후 재평가)**

**사유:**
- 예측된 신규 적응증은 laronidase의 기존 국제 승인 적응증(무코다당증 I형)과 사실상 동일 질환이며, drug.original_indications 필드 공백으로 인해 "신규 재창출"로 오분류되었을 가능성이 높습니다. 재창출로서의 실질적 신규성은 낮습니다.
- 무엇보다 국내(허가사항) 경고·금기 정보가 완전히 부재하여(DG001, Blocking 등급) 안전성 초기 평가(S1) 자체를 진행할 수 없는 상태입니다. 문헌상 근거 수준(L1)은 높게 표시되어 있으나, 이는 안전성 검토 가능 여부와 별개입니다.
- 참고로 2순위 예측(산필리포 증후군, MPS III)은 표적 효소가 다른 기전 불일치 사례로, 근거 수준 L2·Hold 권고이며 지식그래프 상 "리소좀 축적병/GAG 대사" 질환군 근접성에 따른 오탐 가능성이 지적되었습니다.

**진행하려면 필요한 것:**
- 국내 허가사항 원문(경고/금기/DDI) 확보 — DG001 최우선 해소
- laronidase 상세 작용기전(MOA) 자료 확보 — DG002 해소
- drug.original_indications 필드 보완을 통한 실제 신규성 여부 재판정
- 국내 시판/허가 현황 재확인 (현재 0건, 미출시)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

