---
layout: default
title: Nystatin
parent: 모델 예측만 (L5)
nav_order: 556
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
monitor_inn: "Nystatin"
predicted_indications: ["disease of orbital region", "disease of orbital part of eye adnexa", "cystic teratoma", "spinal cord dermoid cyst", "postmenopausal atrophic vaginitis", "biotin metabolic disease", "vulvitis", "commissural lip fistula", "osteoradionecrosis of the mandible"]
description: "Nystatin: 예측 신규 적응증 안와 부위 질환 (disease of orbital region) (근거 수준 L5). 기존 적응증: (시럽제) ○ 유효균종 니스타틴에 감수성인 칸디다 ○ 적응증 소화관칸디다증, 구강칸디다증"
---

# Nystatin
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **9** 건
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

## Nystatin: 안와 부위 질환 (disease of orbital region)
{: .text-alpha }

## 한 문장 요약

Nystatin은 폴리엔계 항진균제로, 한국에서 허가되어 시판 중입니다(허가 건수와 상태는 빠른 개요 참조).
TxGNN 모델은 **안와 부위 질환(disease of orbital region)**에 효과가 있을 수 있다고 예측하며, 예측 점수는 0.9990입니다.
그러나 이 질환을 직접 다룬 임상시험이나 문헌은 없습니다. 연결된 임상시험 1건은 Nystatin과 무관한 다른 질환 연구여서 실질적인 근거가 없습니다.

<!-- review:begin kr-lic-20261124c-nystatin-1 -->

> **검토 정정 (2026-11-24)**: 원래 문장: “Nystatin은 폴리엔계 항진균제로, 한국에서 단일제 2건이 허가되어 시판 중입니다.” 식품의약품안전처 의약품안전나라(nedrug) 허가 자료(2026-11-23 데이터) 기준으로 수정했습니다: 단일·복합 표기와 건수를 본문에 고정해 쓰지 않고, 매주 갱신되는 허가 자료를 반영하는 빠른 개요와 「한국 시판 정보」의 표를 가리키도록 고쳤습니다. 2026-11-25에 식품의약품안전처 품목허가 상세 자료(2026-03)의 주성분명으로 품목별로 다시 확인한 결과, 이 자료에 수록된 허가 품목에는 단일 성분 제제와 복합 성분 제제가 함께 있습니다. 이 자료에는 허가의 일부만 수록되어 있습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261124c-nystatin-1 -->

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | (시럽제) ○ 유효균종 니스타틴에 감수성인 칸디다 ○ 적응증 소화관칸디다증, 구강칸디다증 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202107502/EE)) |
| 예측 신규 적응증 | 안와 부위 질환 (disease of orbital region) |
| TxGNN 예측 점수 | 0.9990 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 20건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Nystatin 처방 정보(Prescribing Information)의 “Clinical Pharmacology” 항목에 따르면(비공식 번역): “니스타틴은 감수성 Candida 종의 세포막에 있는 스테롤에 결합하여 작용하며, 그 결과 막 투과성이 변화되어 세포 내 구성성분이 누출된다. 니스타틴은 세균, 원충 또는 바이러스에 대해 유의한 활성을 나타내지 않는다.” 영어 원문: "Nystatin acts by binding to sterols in the cell membrane of susceptible Candida species with a resultant change in membrane permeability allowing leakage of intracellular components. Nystatin exhibits no appreciable activity against bacteria, protozoa, or viruses." ([DailyMed: Nystatin Oral Suspension (nystatin) prescribing information, Xttrium Laboratories, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4a670371-d373-1ba6-e063-6394a90a13b6), 버전 2026-02-06; 확인일 2026-11-19). 일반적으로 Nystatin은 진균 세포막의 에르고스테롤에 결합해 항진균 작용을 나타내는 폴리엔계 약물로 알려져 있습니다.

안와 부위 질환과의 기전적 연결고리는 확인되지 않았습니다. 연결된 유일한 임상시험은 지도 위축(망막 질환)에 대한 다른 약물 연구입니다. 안와 질환과는 질환 부위도 다르고 Nystatin과도 관련이 없어, 우연한 연관으로 보입니다. 높은 예측 점수는 모델 예측일 뿐 임상적 뒷받침이 아닙니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT03178149](https://clinicaltrials.gov/study/NCT03178149) | Phase 1 | 모집 중 | 42 | 연령관련 황반변성에 따른 지도 위축에서 ASP7317의 안전성·내약성 평가. Nystatin 및 안와 질환과 무관 |

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 202107502 | 제이티니스타틴시럽(니스타틴) | 황색의 균질한 현탁시럽 | (주)중헌제약 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202107502/EE) | 유효 |
| 200501317 | 니스틴정(니스타틴)(수출용)(수출명:IntermedicNystatintablet) | 갈색의 원형 당의정 | 천우신약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200501317/EE) | 유효 |

위 표는 허가 최소 20건 중 2건입니다.

<!-- licenses:end -->

## 안전성 고려사항

- **약물 상호작용**: 총 100건의 상호작용 기록이 있으나 위험 등급은 분류되어 있지 않습니다. 주요 항목은 Cyclosporine, Fluconazole, Erythromycin, Azithromycin, Bortezomib, Tramadol, Lorazepam, Sildenafil, Pantoprazole 등입니다.

경고 및 금기 사항은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 안와 부위 질환을 직접 다룬 임상시험이나 문헌이 없고, 기전적 근거도 확인되지 않아 근거 수준은 L5입니다. 높은 예측 점수만으로는 개발을 진행하기 어렵습니다.

**진행하려면 필요한 것:**
- 안와 부위 질환과 Nystatin의 관련성을 직접 검증하는 전임상 또는 임상 연구
- 작용 기전 데이터 확보 및 안와 질환에서의 기전적 타당성 검토
- 허가사항(경고·금기) 확보 후 안전성 검토
- 안와 부위 투여 경로 및 제형의 적합성 검토

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다. 작용 기전 자료가 없다는 문장은 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Nystatin Oral Suspension (nystatin) prescribing information, Xttrium Laboratories, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4a670371-d373-1ba6-e063-6394a90a13b6) |
| 2026-11-24 | 단일·복합 표기: “Nystatin은 폴리엔계 항진균제로, 한국에서 단일제 2건이 허가되어 …” → 고정된 단일·복합 표기와 건수 삭제(건수는 빠른 개요와 표) | 정정 (2026-11-25 수정, 이전 판은 기록에 보존) | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

