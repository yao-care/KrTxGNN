---
layout: default
title: Sodium Fluoride
parent: 모델 예측만 (L5)
nav_order: 697
evidence_level: L5
indication_count: 7
last_modified_at: 2026-11-24
description: "Sodium Fluoride: 예측 신규 적응증 후두개염 (Epiglottitis) (근거 수준 L5). 기존 적응증: 다음 경우의 양전자방출 단층촬영(Positronemissiontomography, PET)에 사용한다…"
monitor_inn: "SODIUM FLUORIDE"
predicted_indications: ["epiglottitis", "urinary tract infection (disease)", "Ureaplasma urethritis", "gonococcal urethritis", "uterine inflammatory disease", "xanthogranulomatous pyelonephritis", "laryngitis"]
---

# Sodium Fluoride
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **7** 건
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

## Sodium Fluoride: 방사성의약품 진단 및 치아 미백에서 후두개염(Epiglottitis)으로
{: .text-alpha }

## 한 문장 요약

Sodium Fluoride는 한국에서 F-18 표지 PET 진단용 주사제와 치아 미백용 겔로 허가되어 사용되고 있습니다.
TxGNN 모델은 **후두염(Laryngitis)**을 포함한 여러 감염·염증성 질환에 효과가 있을 수 있다고 예측하지만, 이를 지지하는 **임상시험은 0건**이며 **문헌 4편**도 치료 효과와는 무관한 간접 자료입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 다음 경우의 양전자방출 단층촬영(Positronemissiontomography, PET)에 사용한다. 1) 변화된 골형성 활성 영역을 확인하기 위한 뼈의 촬영 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202105308/EE)) |
| 예측 신규 적응증 | 후두개염 (Epiglottitis) |
| TxGNN 예측 점수 | 0.9992 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 13건 / 전체 15건) |
| 허가증 수 | 15건 (유효 13건) |
| 권장 결정 | Hold |

참고: 예측 순위 1위는 후두개염이며, 7위인 후두염은 문헌이 검색된 유일한 예측입니다. 다만 두 항목 모두 근거 수준은 L5입니다.

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Sodium Fluoride 처방 정보(Prescribing Information)의 “Clinical Pharmacology” 항목에 따르면(비공식 번역): “Clinpro 5000에서 전달되는 불소는 건전한 치아의 탈회를 억제하고 탈회된 치아의 재광화(즉, 복구)를 촉진한다. 칫솔질하는 동안 불소는 치아와 치태에 흡수된다.” 영어 원문: "Fluoride delivered from Clinpro 5000 inhibits the demineralization of sound teeth and enhances the remineralization (i.e., repair) of demineralized teeth. During tooth brushing, fluoride is taken up by teeth and dental plaque." ([DailyMed: Clinpro 5000 (sodium fluoride) prescribing information, Solventum US LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a20d3cf0-2e1f-4191-971e-9e47936b4580), 버전 2024-08-01; 확인일 2026-11-19). Sodium fluoride는 F-18 표지 PET 골 영상 진단제와 치아 관련 제품으로 허가되어 있으며, 두 용도 모두 전신 항균·항염 효과를 목적으로 하지 않습니다.

후두개염의 주요 원인균(Hib, 연쇄구균 등)에 대해 임상적으로 의미 있는 용량에서 항균 활성이 있다는 근거는 없습니다. 요로감염에 대해서도 fluoride의 시험관 내 정균 효과가 고농도에서만 관찰될 뿐, 임상적 유용성이나 안전역은 확인되지 않았습니다. 상위 예측 중 Ureaplasma 요도염과 임균성 요도염이 같은 점수(0.9990)인 것은 약물 고유의 생물학 때문이 아니라, 점수가 TxGNN 모델(딥러닝)에서 나온 것이며 모델이 관련 질환 사이에서 학습한 유사성을 반영할 수 있고 생물학적 근거는 아니라는 점을 시사합니다.

따라서 이 예측은 현재 기전적으로 뒷받침되지 않는 계산상의 연관성으로 보는 것이 타당합니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

후두염 예측에 대해 검색된 문헌은 다음과 같으며, 모두 치료 효과를 입증하지 않습니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [29245332](https://pubmed.ncbi.nlm.nih.gov/29245332/) | 2017 | 증례 보고 | Medicine | 후두암 환자에서 윤상연골의 18F-NaF 섭취 증가 (진단 영상 용도) |
| [42721223](https://pubmed.ncbi.nlm.nih.gov/42721223/) | 2026 | 영상/리뷰 | Cartilage | [18F]NaF 및 [18F]FDG PET/CT로 갑상연골의 연령별 생리적 석회화·포도당 대사 평가 |
| [24178785](https://pubmed.ncbi.nlm.nih.gov/24178785/) | 2013 | 동물 독성 연구 | Biol Trace Elem Res | 고불소 사료가 육계의 장 발달을 억제함 |
| [235491](https://pubmed.ncbi.nlm.nih.gov/235491/) | 1975 | 시험관/전임상 | Infect Immun | 배양 세포에서 디프테리아 독소 작용의 화학적 조절 (염화암모늄 중심, 간접 관련) |

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 202105308 | 전남대학교병원플루오르화나트륨주사액(플루오르화나트륨 F-18액) | 무색투명한 액이 무색투명한 바이알에 든 주사제 | 전남대학교병원 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202105308/EE) | 유효 |
| 202500192 | 뉴큐어엠소듐플루오라이드F-18주사액 | 무색투명한 액이 무색투명한 유리바이알에 든 주사제 | 주식회사뉴큐어엠 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202500192/EE) | 유효 |
| 201500482 | 메타스캔주사액(플루오르화나트륨(18F)액) | 무색투명한 액이 무색투명한 유리바이알에 든 주사제 | (주)듀켐바이오 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201500482/EE) | 유효 |
| 200511435 | 더존오팔레센스에프15%(메론향) | 거품이 있는 무색의 점조성 겔 | (주)더존월드 | — | 유효 |
| 201402837 | 에이치디엑스 소듐플루오라이드F18주사액 | 무색 투명한 유리 바이알에 든 무색의 맑은 액 | 에이치디엑스(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201402837/EE) | 유효 |

위 표는 허가 15건 중 5건입니다.

<!-- licenses:end -->

## 안전성 고려사항

허가사항의 경고·금기 본문은 확보되지 않았으므로 허가사항을 참조하세요.

참고로 지식그래프 기반 금기 연관 질환(허가 문서 내용이 아닌 모델 데이터)은 다음과 같습니다.
- **신장·요로 계통**: 신장 질환, 신석증, 신석회증, 요산 신병증, 농뇨관(pyoureter)
- **칼슘·인 대사**: 고칼슘혈증, 부갑상선기능항진증, 섬유성 골염, 인 대사 질환
- **기타**: 사르코이드증, 변비, 용해성 전이성 골병변, 치아 불소증

약물 상호작용은 조회되지 않았습니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
모든 예측 적응증이 L5(모델 예측만 존재)이며, 임상시험이 없고 문헌도 진단 영상 또는 독성 연구로 치료 근거가 되지 않습니다. 감염성 질환에 대한 기전적 타당성도 확인되지 않았고, 금기 연관 질환에 신장·칼슘 대사 질환이 다수 포함되어 있습니다.

**진행하려면 필요한 것:**
- 작용 기전(MOA) 데이터 확보 (DrugBank 조회)
- 허가사항(첨부문서)의 경고·금기 본문 확보 및 안전성 검토
- 대상 감염 병원체에 대한 전임상 항균 활성 및 안전역 근거
- 투여 경로 적합성 평가 (현재 허가 제형은 주사제(PET 진단용 등), 치아용 겔, 껌정(수출용)임)
- 신규 적응증을 지지하는 임상시험 또는 의미 있는 문헌 근거

<!-- review:begin kr-lic-20261124b-sodium_fluoride-1 -->

> **검토 정정 (2026-11-24)**: 원래 문장: “(현재 허가 제형은 PET 진단용 주사제와 치아용 겔뿐임)” 식품의약품안전처 의약품안전나라(nedrug) 허가 자료(2026-11-23 데이터) 기준으로 수정했습니다: 허가 제형에 대한 설명이 자료와 맞지 않아 자료에 있는 제형으로 고쳤습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261124b-sodium_fluoride-1 -->

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다. 작용 기전 자료가 없다는 문장은 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Clinpro 5000 (sodium fluoride) prescribing information, Solventum US LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a20d3cf0-2e1f-4191-971e-9e47936b4580) |
| 2026-11-24 | 허가 제형: “(현재 허가 제형은 PET 진단용 주사제와 치아용 겔뿐임)” → 자료 기준으로 수정 | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

