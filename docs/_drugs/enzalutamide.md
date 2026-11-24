---
layout: default
title: Enzalutamide
parent: 모델 예측만 (L5)
nav_order: 313
evidence_level: L5
indication_count: 5
monitor_inn: "ENZALUTAMIDE"
predicted_indications: ["prostate leiomyoma", "Brenner tumor", "fibroma of prostate", "benign reproductive system neoplasm", "benign prostate phyllodes tumor"]
last_modified_at: 2026-11-24
description: "Enzalutamide: 예측 신규 적응증 전립선 평활근종 (prostate leiomyoma) (근거 수준 L5). 기존 적응증: 1. 무증상 또는 경미한 증상의 전이성 거세저항성 전립선암 환자의 치료 2. 이전에 도세탁셀로 치료받았던…"
---

# Enzalutamide
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **5** 건
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

## Enzalutamide: 안드로겐 수용체 억제제 → 전립선 평활근종 (prostate leiomyoma)
{: .text-alpha }

## 한 문장 요약

Enzalutamide는 안드로겐 수용체를 표적으로 하는 약물로, 한국에서 단일제 허가를 받아 사용되고 있습니다.
TxGNN 모델은 **전립선 평활근종(prostate leiomyoma)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 직접 뒷받침하는 **임상시험은 0건, 문헌도 0편**입니다.
따라서 이 예측은 모델 계산에만 근거한 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 1. 무증상 또는 경미한 증상의 전이성 거세저항성 전립선암 환자의 치료 2. 이전에 도세탁셀로 치료받았던 전이성 거세저항성 전립선암 환자의 치료 3. 고위험 비전이성 거세저항성 전립선암 환자의 치료 4. 호르몬 반응성 전이성 전립선암(mHSPC) 환자의 치료에 안드로겐… ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202600225/EE)) |
| 예측 신규 적응증 | 전립선 평활근종 (prostate leiomyoma) |
| TxGNN 예측 점수 | 0.9957 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 7건 / 전체 7건) |
| 허가증 수 | 7건 (유효 7건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Enzalutamide 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “엔잘루타마이드는 안드로겐 수용체 신호전달 경로의 여러 단계에 작용하는 안드로겐 수용체 억제제이다. 엔잘루타마이드는 안드로겐 수용체에 대한 안드로겐 결합을 경쟁적으로 억제하고, 그 결과 안드로겐 수용체의 핵 내 이동 및 DNA와의 상호작용을 억제하는 것으로 나타났다.” 영어 원문: "Enzalutamide is an androgen receptor inhibitor that acts on different steps in the androgen receptor signaling pathway. Enzalutamide has been shown to competitively inhibit androgen binding to androgen receptors; and consequently, inhibits nuclear translocation of androgen receptors and their interaction with DNA." ([DailyMed: Xtandi (enzalutamide) prescribing information, Astellas Pharma US, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b129fdc9-1d8e-425c-a5a9-8a2ed36dfbdf), 버전 2026-07-28; 확인일 2026-11-19). 다만 enzalutamide는 안드로겐 수용체(AR) 신호를 억제하는 계열의 약물로 알려져 있습니다. 전립선 기질 조직에서 AR 신호가 어떤 역할을 할 수 있다는 가설이 가능합니다.

전립선 평활근종은 전립선의 양성 중간엽 종양입니다. AR 억제와의 연결은 어디까지나 추측 수준이며, 이 예측은 전립선암과의 근접성 때문에 높은 점수를 받았을 가능성이 큽니다. 이를 지지하는 임상시험이나 문헌은 확인되지 않았습니다.

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 202600225 | 엔잘엑스연질캡슐40밀리그램(엔잘루타미드) | 무색 내지 미황색의 투명한 액체가 든 흰색 내지 미백색의 불투명한 장방형… | 한국메나리니(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202600225/EE) | 유효 |
| 202500452 | 아나미드연질캡슐40밀리그램(엔잘루타미드) | 무색 내지 미황색의 투명한 액체가 든 흰색 내지 미백색의 불투명한 장방형… | 알보젠코리아(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202500452/EE) | 유효 |
| 202402841 | 엑스탄디정80밀리그램(엔잘루타마이드) | 노란색의 타원형 필름코팅정 | 한국아스텔라스제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202402841/EE) | 유효 |
| 202402842 | 엑스탄디정40밀리그램(엔잘루타마이드) | 노란색의 원형 필름코팅정 | 한국아스텔라스제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202402842/EE) | 유효 |
| 201307883 | 엑스탄디연질캡슐40mg(엔잘루타마이드) | 맑은 노란색의 액체가 든 흰색 내지 미백색의 장방형의 연질캡슐 | 한국아스텔라스제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201307883/EE) | 유효 |

위 표는 허가 7건 중 5건입니다.

<!-- licenses:end -->

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적치료제 (호르몬 계열, 안드로겐 수용체 억제) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 취급 방호 | 허가사항의 경고 및 주의사항을 참조하세요 |

## 안전성 고려사항

- **약물 상호작용**: 이번 조회에서 총 100건이 확인되었으며, 그중 일부 주요 항목은 다음과 같습니다.
  - 주요(Major) 등급: bupropion, dolasetron, eliglustat
  - 중등도(Moderate) 등급: famotidine, rabeprazole, omeprazole, hydrocortisone, dexamethasone, clarithromycin, aprepitant, loperamide, saxagliptin, linagliptin, empagliflozin 등

경고 및 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
전립선 평활근종에 대해 직접 연구한 임상시험이나 문헌이 없으며, 예측은 모델 계산에만 근거합니다. 기전적 연결도 추측 수준입니다.

**진행하려면 필요한 것:**
- 전립선 평활근종에서 안드로겐 수용체 발현과 의존성을 확인하는 전임상 또는 병리 연구
- 작용 기전(MOA) 상세 데이터 보완
- 허가사항(경고·금기) 확인 및 안전성 검토
- 질환의 희귀성을 고려한 임상 근거 확보 가능성 평가

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Xtandi (enzalutamide) prescribing information, Astellas Pharma US, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b129fdc9-1d8e-425c-a5a9-8a2ed36dfbdf) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

