---
layout: default
title: Ketoconazole
parent: 僅模型預測 (L5)
nav_order: 416
evidence_level: L5
indication_count: 1
---

# Ketoconazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Ketoconazole: 항진균 적응증에서 여드름(Acne)으로

## 한 문장 요약

Ketoconazole은 이미다졸계 항진균제입니다. TxGNN 모델은 **여드름(Acne)**에 효과가 있을 수 있다고 예측하며, 현재 **1건의 진행 중인 임상시험**과 **15편의 문헌**(주로 기전 연구·관찰 연구)이 이 방향을 뒷받침하고 있으나, 확증적 RCT는 아직 없습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 자료 없음 (원 적응증 정보 미제공, 일반적으로 항진균제로 알려짐) |
| 예측 신규 적응증 | 여드름 (Acne) |
| TxGNN 예측 점수 | 99.80% |
| 근거 수준 | L3 (관찰 연구/기전 연구 수준) |
| 한국 시판 현황 | ✗ 미판매 (허가 없음) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

Ketoconazole은 이미다졸계 항진균제로, CYP450 효소(lanosterol 14α-demethylase 및 부신/성선 스테로이드 합성효소)를 억제합니다. 이 작용은 여드름과 두 가지 경로로 연결될 수 있습니다: (1) 피부 국소적으로 Malassezia(Pityrosporum) furfur를 억제하여, 흔히 심상성 여드름과 혼동되거나 동반되는 진균성 모낭염을 개선할 가능성, (2) 전신 투여 시 부신·성선의 스테로이드 생성을 억제해 안드로겐/코르티솔 농도를 낮춤으로써 고안드로겐 관련 여드름(PCOS, Cushing 증후군 동반 여드름 등)에 이론적 이점이 있을 가능성입니다.

다만 두 경로 모두 기전상으로는 타당하지만, 근거 강도와 적응증 정의(진균성 모낭염 vs. 심상성 여드름)가 완전히 일치하지는 않습니다. 또한 경구 ketoconazole은 심각한 간독성 및 QT 연장 위험이 알려져 있어, 효익 추론에 앞서 안전성 재평가가 우선되어야 합니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT07237763](https://clinicaltrials.gov/study/NCT07237763) | NA (연구자 주도) | 진행 중 (신규 모집 없음) | 52 | 경증 면포성·구진농포성 여드름에서 외용 ketoconazole 2% 크림과 adapalene 2% 크림의 효능을 비교, ketoconazole이 부작용이 적고 순응도가 높은 레티노이드 대체제가 될 수 있는지 평가 중 (결과 미공개) |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [33216275](https://pubmed.ncbi.nlm.nih.gov/33216275/) | 2021 | RCT (SONICS 3상 하위분석) | Pituitary | Levoketoconazole이 Cushing 증후군 환자의 임상 징후·증상 및 환자보고결과를 개선 |
| [28111792](https://pubmed.ncbi.nlm.nih.gov/28111792/) | 2017 | 실험연구 (in vitro) | Microbiology and Immunology | Ketoconazole이 여드름 원인균 P. acnes의 리파아제 활성을 억제, 항생제 대체 가능성 시사 |
| [20045949](https://pubmed.ncbi.nlm.nih.gov/20045949/) | 2010 | 실험연구 (in vitro) | Biological & Pharmaceutical Bulletin | 여드름 환자 유래 P. acnes에 대한 azole계 항진균제의 시험관 내 항균 활성 평가 |
| [12566804](https://pubmed.ncbi.nlm.nih.gov/12566804/) | 2003 | Review | Dermatology (Basel) | 중등도~중증 여드름의 전신 치료 옵션 개관, 항생제 내성 문제 언급 |
| [8593718](https://pubmed.ncbi.nlm.nih.gov/8593718/) | 1995 | 관찰 연구 (증례군) | Clinical and Experimental Dermatology | 여드름으로 오진되기 쉬운 Pityrosporum 모낭염 62례 분석 및 치료 경과 |
| [8090657](https://pubmed.ncbi.nlm.nih.gov/8090657/) | 1993 | Cohort | Polski Tygodnik Lekarski | PCOS 고안드로겐혈증에서 호르몬 병용요법으로 여드름·다모증 감소 |
| [19445767](https://pubmed.ncbi.nlm.nih.gov/19445767/) | 2009 | Review | BMJ Clinical Evidence | 다낭성난소증후군(PCOS) 개관, 여드름 등 동반 증상 기술 |
| [8255067](https://pubmed.ncbi.nlm.nih.gov/8255067/) | 1993 | Review | The Keio Journal of Medicine | Pityrosporum ovale와 관련 피부질환(모낭염, 지루피부염 등) 개관 |
| [8629828](https://pubmed.ncbi.nlm.nih.gov/8629828/) | 1996 | Case Report | Archives of Dermatology | 신생아 Malassezia furfur 농포증과 신생아 여드름의 연관성 보고 |
| [23600337](https://pubmed.ncbi.nlm.nih.gov/23600337/) | 2013 | Review | FP Essentials | 영유아 흔한 피부발진(신생아 여드름 포함) 개관 |

## 결론 및 다음 단계

**결정: Hold**

**사유:**
현지 허가 자료가 없어(未上市, 허가증 0건) 안전성 초평가(S1)를 진행할 수 없으며(DG001, Blocking), 근거 수준도 L3(관찰·기전 연구)에 그치고 여드름 적응증을 직접 검증하는 임상시험은 아직 소규모·비정식 단계(NCT07237763)입니다. 경구 ketoconazole의 알려진 간독성·QT 연장 위험을 고려하면 지금 단계에서 진행을 권고하기 어렵습니다.

**진행하려면 필요한 것:**
- TFDA(또는 해당 관할 규제기관) 공식 라벨의 경고/금기 정보 확보 (DG001 해소)
- DrugBank API를 통한 정확한 작용기전(MOA) 확인 (DG002 해소)
- NCT07237763 결과 발표 대기 및 후속 확증적 RCT 확인
- 국소(외용) vs 전신 투여 경로별 안전성·효능 데이터 구분 확보
- 간독성 및 QT 연장 위험에 대한 별도 안전성 평가
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

