---
layout: default
title: Glatiramer Acetate
parent: 모델 예측만 (L5)
nav_order: 378
evidence_level: L5
indication_count: 1
drugbank_id: DB05259
monitor_inn: "Glatiramer"
predicted_indications: ["hemoglobinopathy"]
last_modified_at: 2026-11-20
description: "Glatiramer Acetate: 예측 신규 적응증 혈색소병증 (hemoglobinopathy) (근거 수준 L5). 기존 적응증: MFDS 허가사항(PDF) 참조"
---

# Glatiramer Acetate
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **1** 건
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

## Glatiramer Acetate: 혈색소병증 (hemoglobinopathy)
{: .text-alpha }

## 한 문장 요약

Glatiramer acetate는 4가지 아미노산으로 이루어진 무작위 중합체 형태의 면역조절제입니다.
TxGNN 모델은 **혈색소병증(hemoglobinopathy)**에 효과가 있을 수 있다고 예측했지만, 이 질환을 직접 연구한 임상시험은 **0건**, 문헌은 **1편**(간접 관련)뿐입니다.
현재로서는 모델 예측 단계에 머물러 있어 실제 근거는 매우 제한적입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | [MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201404988/EE) |
| 예측 신규 적응증 | 혈색소병증 (hemoglobinopathy) |
| TxGNN 예측 점수 | 0.9903 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 1건 / 전체 1건) |
| 허가증 수 | 1건 (유효 1건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Glatiramer Acetate 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “글라티라머 아세테이트가 MS 환자에서 효과를 나타내는 기전은 완전히 밝혀지지 않았다. 그러나 글라티라머 아세테이트는 MS의 발병에 관여하는 것으로 여겨지는 면역 과정을 변화시킴으로써 작용하는 것으로 생각된다.” 영어 원문: "The mechanism(s) by which glatiramer acetate exerts its effects in patients with MS are not fully understood. However, glatiramer acetate is thought to act by modifying immune processes that are believed to be responsible for the pathogenesis of MS." ([DailyMed: Glatopa (glatiramer acetate) prescribing information, Bryant Ranch Prepack](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0679689e-8930-4d6a-b922-5125082b2716), 버전 2026-10-26; 확인일 2026-11-19). 일반적으로 알려진 바에 따르면 glatiramer acetate는 T세포 반응을 Th2/조절 T세포 표현형 쪽으로 전환시키고, 미엘린 염기성 단백질의 미끼(decoy)로 작용하는 면역조절제입니다.

혈색소병증(겸상적혈구병, 지중해빈혈 등)은 헤모글로빈의 구조나 합성에 이상이 생기는 유전성 질환입니다. 따라서 면역조절제와의 연결고리는 염증이나 면역 조절 이상을 통한 간접 경로 정도로만 추정할 수 있고, 현재 확인된 기전적 연관성은 없습니다. 0.9903이라는 높은 예측 점수도 모델 출력일 뿐 임상적 근거로 해석해서는 안 됩니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [28372806](https://pubmed.ncbi.nlm.nih.gov/28372806/) | 2017 | Review (분류 기준) | Revue neurologique | 다발성 경화증 환자가 natalizumab 중단 후 여러 면역 질환을 겪은 사례입니다. 환자의 과거력에 베타 지중해빈혈이 있었을 뿐, 혈색소병증에 대한 치료 효과를 다룬 연구는 아닙니다. |

이 문헌은 혈색소병증에 대한 glatiramer acetate의 효과를 직접 평가하지 않았으므로 지지 근거로 보기 어렵습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 제조사 |
|---------|------|------|------|
| 201404988 | 코팍손프리필드주40mg/1ml(글라티라머아세트산염) | 프리필드시린지 주사제 (무색~미황색 투명 액) | (주)한독테바 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 점수는 높지만 혈색소병증을 직접 연구한 임상시험이나 문헌이 없어 근거 수준이 L5에 머뭅니다. 기전적 연관성도 확인되지 않았고, 안전성 정보도 확보되지 않았습니다.

**진행하려면 필요한 것:**
- 작용 기전(MOA) 데이터 확보와 혈색소병증 병태생리와의 기전적 연결 분석
- 혈색소병증을 직접 대상으로 한 전임상 또는 임상 연구 근거
- 식약처 허가사항(경고, 금기 등)을 확인하고 안전성을 검토
- 혈색소병증 환자군에서의 면역조절 접근이 타당한지 전문가 검토

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다. 작용 기전 자료가 없다는 문장은 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-12 | 허가 건수: 0건 → 유효 1건 | 보고서가 다시 생성되어 이 문장이 없음(2026-11-16: 2026년 11월 16일 보고서가 새 예측(DrugBank ID로 찾은 TxGNN 예측)으로 다시 생성되어 이 문장이 더 이상 없음; 원래: 정정) | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Glatopa (glatiramer acetate) prescribing information, Bryant Ranch Prepack](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0679689e-8930-4d6a-b922-5125082b2716) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

