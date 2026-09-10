---
layout: default
title: Isoniazid
parent: 僅模型預測 (L5)
nav_order: 408
evidence_level: L5
indication_count: 1
---

# Isoniazid
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

# Isoniazid: 결핵에서 결막염으로

## 한 문장 요약

Isoniazid(이소니아지드)는 결핵(특히 잠복결핵감염 예방화학요법)에 사용되어 온 항결핵제입니다.
TxGNN 모델은 **결막염(Conjunctivitis)**에 효과가 있을 수 있다고 예측하며(예측 점수 99.36%),
현재 **임상시험 1건**(단, 결막염이 아닌 원 적응증 관련 시험)과 **문헌 20편**(대부분 결핵성 안질환 관련 증례보고)이 검색되었으나, 아직 관련성 분류가 완료되지 않은 상태입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 결핵 (잠복결핵감염 예방화학요법) — 한국 허가 정보 없음 |
| 예측 신규 적응증 | 결막염 (Conjunctivitis) |
| TxGNN 예측 점수 | 99.36% |
| 근거 수준 | L4 |
| 한국 시판 현황 | 미판매 (미허가) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 Isoniazid의 상세 작용 기전(MOA) 데이터가 확보되지 않았습니다([Data Gap]). 다만 검색된 임상시험 정보에 따르면, Isoniazid는 결핵균 감염 및 잠복결핵감염(LTBI)의 표준 치료·예방 약물(예: 5mg/kg 9개월 요법, 또는 rifapentine 병용 3HP 요법)로 사용되어 왔습니다.

결막염과의 연관성은 기전적 유사성이라기보다는 **질병 자체의 연관성**에서 비롯됩니다. 검색된 문헌 다수는 결핵균 감염이 결막에 직접 침범하거나(원발성 결막결핵), 결핵에 대한 과민반응으로 발생하는 안검결막염(phlyctenular keratoconjunctivitis)을 유발할 수 있음을 보고하며, 이 경우 Isoniazid가 원인 치료 또는 예방 목적으로 사용된 사례가 다수 존재합니다. 즉, "결막염 치료제로서의 신규 기전"이라기보다 "결핵성 결막 병변에 대한 원인 치료" 성격에 가깝습니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT04094012](https://clinicaltrials.gov/study/NCT04094012) | Phase 3 | 완료 | 490 | 잠복결핵감염(LTBI) 치료에서 3HP(주 1회 rifapentine+isoniazid, 12회) vs 1HP 요법의 전신 약물반응 발생률 비교. **결막염을 직접 평가한 시험은 아니며, 원 적응증(결핵 예방)에 대한 시험임** |

> 주의: 검색된 유일한 임상시험은 "isoniazid + conjunctivitis" 키워드로 검출되었으나 실제로는 결핵 예방요법 관련 시험으로, 결막염 적응증을 직접 뒷받침하지는 않습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [5103251](https://pubmed.ncbi.nlm.nih.gov/5103251/) | 1971 | 미분류 | Annales d'oculistique | 안결핵(ocular tuberculosis)의 국소 치료에 Isoniazid 사용 |
| [14253168](https://pubmed.ncbi.nlm.nih.gov/14253168/) | 1965 | 미분류 | Am Rev Respir Dis | 알래스카 에스키모 집단의 안검결막염(phlyctenular keratoconjunctivitis)에서 Isoniazid 예방요법 연구 |
| [10641112](https://pubmed.ncbi.nlm.nih.gov/10641112/) | 1999 | 미분류 | Oftalmologia | 안검결막염과 림프절결핵 관련 28례 분석 |
| [25433746](https://pubmed.ncbi.nlm.nih.gov/25433746/) | 2014 | 미분류 | Can J Ophthalmol | 결막 인상소체증(phlyctenulosis)이 결핵 발병의 전조 징후로 재조명됨 |
| [33607832](https://pubmed.ncbi.nlm.nih.gov/33607832/) | 2021 | 미분류 | Medicine | 소아 비부비동결핵 동반 안검결막염 증례 및 문헌고찰 |
| [17133069](https://pubmed.ncbi.nlm.nih.gov/17133069/) | 2006 | 미분류 | Cornea | 만성 충혈로 나타난 결막결핵 증례 |
| [26692731](https://pubmed.ncbi.nlm.nih.gov/26692731/) | 2015 | 미분류 | Middle East Afr J Ophthalmol | 무안구와(anophthalmic socket)에서의 결핵성 결막염 증례 |
| [14089390](https://pubmed.ncbi.nlm.nih.gov/14089390/) | 1964 | 미분류 | Arch Ophthalmol | 원발성 결막결핵 증례 |
| [4233886](https://pubmed.ncbi.nlm.nih.gov/4233886/) | 1968 | 미분류 | Arch Ophtalmol | 안구결막 결핵 증례 |
| [12226788](https://pubmed.ncbi.nlm.nih.gov/12226788/) | 2002 | 미분류 | Dtsch Med Wochenschr | BCG 방광내 주입 후 결막염 동반 만성 반응성 관절염 증례 |

> 대부분 문헌은 결핵-결막 병변의 연관성 및 예방/치료 사례를 다룬 오래된 증례보고이며, 아직 관련성(relevance) 및 연구유형 분류가 완료되지 않았습니다("pending" 상태).

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 점수는 높으나(99.36%), 이를 뒷받침하는 근거는 결막염을 직접 평가한 현대적 임상시험이 아니라 대부분 1960~1990년대의 결핵성 결막 병변 증례보고에 그칩니다. 또한 작용기전(MOA), 한국 허가/시판 정보, 안전성 경고 데이터가 모두 확보되지 않아(DG001: Blocking) 안전성 초평가(S1) 단계 진입이 불가능한 상태입니다.

**진행하려면 필요한 것:**
- TFDA(식약처) 수준 허가사항 및 경고·금기 정보 확보 (DG001, Blocking)
- DrugBank 기반 작용기전(MOA) 데이터 확보 (DG002, High)
- 임상시험·문헌의 관련성(relevance) 및 연구유형 분류 완료 (현재 전량 "pending")
- 결핵성 결막염 vs 일반 결막염 적응증 범위 명확화
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

