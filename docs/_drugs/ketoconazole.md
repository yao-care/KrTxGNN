---
layout: default
title: Ketoconazole
parent: 중등도 근거 (L3-L4)
nav_order: 448
evidence_level: L4
indication_count: 1
last_modified_at: 2026-11-24
description: "Ketoconazole: 예측 신규 적응증 여드름 (acne) (근거 수준 L4). 기존 적응증: 백선(체부백선, 완선, 족부백선), 피부칸디다증, 어루러기, 지루피부염 등 피부 진균증"
monitor_inn: "KETOCONAZOLE"
predicted_indications: ["acne (disease)"]
---

# Ketoconazole
{: .fs-9 }

근거 수준: **L4** | 예측 적응증: **1** 건
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

## Ketoconazole: 피부 진균증에서 여드름 (Acne)으로
{: .text-alpha }

## 한 문장 요약

Ketoconazole은 아졸계 항진균제로, 한국에서 백선, 피부칸디다증, 어루러기, 지루피부염 등 피부 진균증 치료에 사용되어 왔습니다.
TxGNN 모델은 **여드름(acne)**에 효과가 있을 수 있다고 예측하며, 현재 **1건의 임상시험**(Phase 구분 없음, 진행 중)과 **14편의 문헌**이 이 방향과 관련되어 있으나 대부분 간접 근거입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 백선(체부백선, 완선, 족부백선), 피부칸디다증, 어루러기, 지루피부염 등 피부 진균증 |
| 예측 신규 적응증 | 여드름 (acne) |
| TxGNN 예측 점수 | 0.9980 |
| 근거 수준 | L4 (전임상·기전 연구 수준의 근거만 있음) |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 19건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Ketoconazole 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “케토코나졸은 진균 세포막에서 라노스테롤을 에르고스테롤로 전환하는 데 관여하는 사이토크롬 P-450 의존성 효소인 라노스테롤 14α-탈메틸화효소를 억제함으로써 진균 세포막의 핵심 구성성분인 에르고스테롤의 합성을 차단한다. 그 결과 세포막 내에 메틸화된 스테롤 전구체가 축적되고 에르고스테롤이 고갈되어 진균 세포막의 구조와 기능이 약화된다.” 영어 원문: "Ketoconazole blocks the synthesis of ergosterol, a key component of the fungal cell membrane, through the inhibition of cytochrome P-450 dependent enzyme lanosterol 14α-demethylase responsible for the conversion of lanosterol to ergosterol in the fungal cell membrane. This results in an accumulation of methylated sterol precursors and a depletion of ergosterol within the cell membrane thus weakening the structure and function of the fungal cell membrane." ([DailyMed: ketoconazole prescribing information, Bryant Ranch Prepack](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4baebcab-a237-42c0-9183-6f447a44e371), 버전 2025-11-18; 확인일 2026-11-19). 다만 알려진 정보에 따르면 Ketoconazole은 진균의 lanosterol 14-alpha-demethylase(CYP51)를 억제하는 아졸계 항진균제입니다. 고용량에서는 사람의 스테로이드 합성 효소(CYP17A1, CYP11A1)도 억제하여 안드로겐 합성을 낮출 수 있습니다.

국소 투여 시에는 Malassezia(Pityrosporum) 집락을 줄여 모낭 염증을 완화할 수 있으며, 이것이 여드름 또는 여드름 유사 발진에 기여할 가능성이 있습니다. 또한 피지가 많은 부위에 생기는 지루피부염에 이미 사용되고 있다는 점도 간접적인 타당성을 더합니다. 실험실 연구에서는 Ketoconazole이 여드름의 원인균인 *P. acnes*의 성장과 리파제 활성을 억제한다고 보고되었습니다.

다만 TxGNN 점수(0.998)는 컴퓨터 예측일 뿐 임상 근거가 아닙니다. 전신 투여는 간독성, 부신 억제 위험, 그리고 CYP3A4 억제에 따른 많은 약물 상호작용으로 제한됩니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT07237763](https://clinicaltrials.gov/study/NCT07237763) | 해당 없음(NA) | 진행 중(모집 종료) | 52 | 경증 면포성·구진농포성 여드름에서 2% Ketoconazole 크림과 2% Adapalene 크림을 비교하는 무작위 대조시험. 아직 결과는 공개되지 않았습니다. |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [28111792](https://pubmed.ncbi.nlm.nih.gov/28111792/) | 2017 | 기전(in vitro) 연구 | Microbiol Immunol | Ketoconazole이 *P. acnes* 리파제 활성과 성장을 억제하여 항생제 내성 시대의 대안이 될 수 있음을 시사 |
| [20045949](https://pubmed.ncbi.nlm.nih.gov/20045949/) | 2010 | 기전(in vitro) 연구 | Biol Pharm Bull | 여드름 환자에서 분리한 *P. acnes*에 대한 아졸계 항진균제의 시험관 내 활성 평가 |
| [8593718](https://pubmed.ncbi.nlm.nih.gov/8593718/) | 1995 | 임상 관찰 | Clin Exp Dermatol | Pityrosporum 모낭염은 여드름으로 오진되는 경우가 많으며, 62명 환자에서 진단 및 치료 시도를 평가 |
| [12566804](https://pubmed.ncbi.nlm.nih.gov/12566804/) | 2003 | Review | Dermatology | 중등도~중증 여드름의 전신 치료 현황과 전망 |
| [8255067](https://pubmed.ncbi.nlm.nih.gov/8255067/) | 1993 | Review | Keio J Med | Pityrosporum ovale가 지루피부염, 어루러기 등 피부질환과 연관됨 |
| [8629828](https://pubmed.ncbi.nlm.nih.gov/8629828/) | 1996 | Case report | Arch Dermatol | 신생아 구진농포성 발진(신생아 여드름으로 불림)과 Malassezia furfur 감염의 연관성 시사 |

위 문헌은 대부분 간접 근거이며, 여드름에 대한 Ketoconazole의 효능을 직접 입증한 무작위 대조시험은 없습니다. 이 밖에 다낭성 난소 증후군, 영아 피부 발진 등을 다룬 문헌이 포함되어 있으나 관련성이 낮아 생략했습니다.

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 199301086 | 태극케토코나졸크림 | 흰색의 크림제 | 태극제약(주) | — | 유효 |
| 199702130 | 니트나졸크림(케토코나졸) | 백색의 친수성 크림제 | 한국넬슨제약(주) | — | 유효 |
| 199600829 | 비가졸액(케토코나졸) | 점성이 있는 담홍색의 액제 | 동성제약(주) | — | 유효 |
| 201802157 | 니조랄2%액(케토코나졸) | 빨간색-주황색의 액체 | (주)휴온스 | — | 유효 |
| 199602425 | 케스나졸크림(케토코나졸) | 백색 내지 유백색의 크림제. | 알파제약(주) | — | 유효기간만료 |

위 표는 허가 최소 20건 중 5건입니다.

<!-- licenses:end -->

이 외에도 수출용 정제·크림·액제 등 다수의 허가가 있으며, 총 20건이 유효합니다. 국내 허가 제품은 주로 외용제(크림, 액)입니다.

<!-- review:begin kr-lic-20261124c-ketoconazole-1 -->

> **검토 정정 (2026-11-24)**: 원래 문장: “국내 허가 제품은 주로 외용제(크림, 액)이며 모두 단일 성분제입니다.” 식품의약품안전처 의약품안전나라(nedrug) 허가 자료(2026-11-23 데이터) 기준으로 수정했습니다: 단일·복합 표기와 건수를 본문에 고정해 쓰지 않고, 매주 갱신되는 허가 자료를 반영하는 빠른 개요와 「한국 시판 정보」의 표를 가리키도록 고쳤습니다. 2026-11-25에 식품의약품안전처 품목허가 상세 자료(2026-03)의 주성분명으로 품목별로 다시 확인한 결과, 이 자료에 수록된 허가 품목은 모두 단일 성분 제제입니다. 이 자료에는 허가의 일부만 수록되어 있습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261124c-ketoconazole-1 -->

## 안전성 고려사항

- **주요 경고·금기**: 허가사항의 경고 및 금기 내용은 본 보고서용 자료에 포함되어 있지 않으므로 허가사항을 참조하세요.
- **지식 그래프상 금기 관련 질환**: QT 연장 증후군(가족성 포함), torsades de pointes, 간질환, 담낭질환, 부신 피질 기능부전(애디슨병), 피부 위축, 말초혈관질환, 무산증 등이 금기와 연관되어 있습니다. 이는 지식 그래프에서 도출된 정보이며 허가 라벨 문구가 아닙니다.
- **약물 상호작용**: 총 100건이 확인되었습니다(CYP3A4 억제가 주요 원인). 예시는 다음과 같습니다.
  - **Major**: Loperamide, Triamcinolone, Budesonide
  - **Moderate**: Famotidine, Ranitidine, Omeprazole, Rabeprazole, Dexamethasone, Hydrocortisone, Aprepitant, Pioglitazone, Alosetron 등
  - **Minor**: Amphotericin B

## 결론 및 다음 단계

**결정: Hold**

**사유:**
여드름에 대한 직접적인 임상 근거가 없고, 유일한 임상시험(NCT07237763)은 소규모이며 결과가 공개되지 않았습니다. 문헌은 대부분 시험관 내 연구와 간접 근거이고, 높은 TxGNN 점수는 컴퓨터 예측일 뿐입니다. 또한 전신 투여 시 간독성과 많은 약물 상호작용 위험이 있어, 국소 제형으로 한정한 검증이 우선입니다.

**진행하려면 필요한 것:**
- NCT07237763 시험 결과 확인 (2% Ketoconazole 크림 vs Adapalene 크림)
- 여드름에 대한 국소 Ketoconazole의 추가 무작위 대조시험 또는 체계적 문헌고찰
- 허가사항(경고·금기) 확보 및 안전성 검토
- 작용 기전 데이터 보완 (DrugBank 등)
- 국소 제형으로 한정할지 여부 결정 (전신 투여는 간독성·부신 억제·상호작용 위험으로 부적합 가능성이 큼)

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다. 작용 기전 자료가 없다는 문장은 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: ketoconazole prescribing information, Bryant Ranch Prepack](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4baebcab-a237-42c0-9183-6f447a44e371) |
| 2026-11-24 | 단일·복합 표기: “국내 허가 제품은 주로 외용제(크림, 액)이며 모두 단일 성분제입니다.” → 고정된 단일·복합 표기와 건수 삭제(건수는 빠른 개요와 표) | 정정 (2026-11-25 수정, 이전 판은 기록에 보존) | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

