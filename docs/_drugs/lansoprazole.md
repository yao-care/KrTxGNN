---
layout: default
title: Lansoprazole
parent: 모델 예측만 (L5)
nav_order: 459
evidence_level: L5
indication_count: 1
monitor_inn: "LANSOPRAZOLE"
predicted_indications: ["duodenal obstruction"]
last_modified_at: 2026-11-24
description: "Lansoprazole: 예측 신규 적응증 십이지장 폐쇄 (duodenal obstruction) (근거 수준 L5). 기존 적응증: 1. 활동성 십이지장궤양의 단기치료 2. 활동성 양성 위궤양의 단기치료 3. 십이지장궤양 재발방지를 위한…"
---

# Lansoprazole
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

## Lansoprazole: 프로톤 펌프 억제제 → 십이지장 폐쇄 (duodenal obstruction)
{: .text-alpha }

## 한 문장 요약

Lansoprazole은 위산 분비를 억제하는 프로톤 펌프 억제제 계열의 약물입니다.
TxGNN 모델은 **십이지장 폐쇄(duodenal obstruction)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 직접 뒷받침하는 **임상시험은 0건, 문헌도 0편**으로 모델 예측 단계에 머물러 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 1. 활동성 십이지장궤양의 단기치료 2. 활동성 양성 위궤양의 단기치료 3. 십이지장궤양 재발방지를 위한 Helicobacter pylori의 박멸 4. 십이지장궤양의 치료후 유지요법 5. 비스테로이드성 소염진통제 유발성 위궤양의 치료 6. 비스테로이드성 소염진통제 유발성 위궤양의… ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200401591/EE)) |
| 예측 신규 적응증 | 십이지장 폐쇄 (duodenal obstruction) |
| TxGNN 예측 점수 | 0.9968 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 20건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Lansoprazole 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “란소프라졸은 위 벽세포의 분비 표면에서 (H +, K + )-ATPase 효소계를 특이적으로 억제하여 위산 분비를 억제하는 항분비 화합물 계열인 치환 벤즈이미다졸에 속한다. 이 효소계는 벽세포 내의 산(양성자) 펌프로 간주되므로, 란소프라졸은 산 생성의 마지막 단계를 차단한다는 점에서 위산 펌프 억제제로 규정되어 왔다.” 영어 원문: "Lansoprazole belongs to a class of antisecretory compounds, the substituted benzimidazoles, that suppress gastric acid secretion by specific inhibition of the (H +, K + )-ATPase enzyme system at the secretory surface of the gastric parietal cell. Because this enzyme system is regarded as the acid (proton) pump within the parietal cell, lansoprazole has been characterized as a gastric acid-pump inhibitor, in that it blocks the final step of acid production." ([DailyMed: Prevacid (lansoprazole) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=71ba78cb-7e46-43eb-9425-fa130f537f84), 버전 2025-07-08; 확인일 2026-11-19). 일반적으로 lansoprazole은 위산 분비를 줄이는 약물로 알려져 있으며, 이 점이 소화성 궤양 질환 관리와 연결됩니다.

그러나 십이지장 폐쇄는 협착, 윤상 췌장, 악성 종양, 궤양 후 흉터 등 구조적·기계적 원인으로 생기는 경우가 많아 내시경 또는 수술적 치료가 필요합니다. 산 억제가 궤양 같은 기저 원인을 관리하는 데 도움이 될 수는 있어도, 폐쇄 자체를 치료한다고 보기는 어렵습니다. 따라서 명확한 기전적 연결고리는 확인되지 않았습니다.

0.9968이라는 높은 예측 점수는 모델 내부의 예측값일 뿐이며, 십이지장 궤양 관련 적응증과의 근접성을 반영했을 가능성이 있습니다. 실제 임상적 근거를 의미하지는 않습니다.

## 한국 시판 정보

이 자료에 수록된 허가증에는 란소프라졸 단일제 외에 침강탄산칼슘 복합제(란소앤정, 란스타정, 뉴란소엑스정)도 있으며, 아래는 그중 주요 단일제입니다. 목록은 일부일 수 있습니다.

<!-- review:begin kr-lic-20261124-lansoprazole-1 -->

> **검토 정정 (2026-11-24)**: 원래 문장: “허가증 20건이 모두 유효 단일 성분 기록으로 확인되며, 아래는 그중 주요 5건입니다.” 식품의약품안전처 의약품안전나라(nedrug) 허가 자료(2026-11-23 데이터) 기준으로 수정했습니다: 이 자료에 수록된 허가 중 란소앤정·란스타정·뉴란소엑스정 15/600밀리그램은 란소프라졸과 침강탄산칼슘의 복합제입니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261124-lansoprazole-1 -->

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 200401591 | 뉴란소정(란소프라졸)(수출용) | 적갈색의 원형 장용 코팅정 | 한국유니온제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200401591/EE) | 유효 |
| 201208079 | 란가톤캡슐15밀리그램(란소프라졸) | 백색 내지 엷은 갈색의 과립이 든 상,하부 백색의 경질캡슐제 | 광동제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201208079/EE) | 유효 |
| 201501764 | 모노리툼플라스정15밀리그램(란소프라졸) | 회색반점이 있는 흰색의 원형정제 | (주)태준제약 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201501764/EE) | 유효 |
| 201110631 | 란프톤캡슐30밀리그램(란소프라졸) | 흰색 내지 엷은 갈색의 과립이 들어있는 상・하부 흰색의 경질캡슐제 | 삼천당제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201110631/EE) | 유효 |
| 200402541 | 란소롤정(란소프라졸)(수출용) | 적갈색의 원형 장용코팅정 | 미래바이오제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200402541/EE) | 유효 |

위 표는 허가 최소 20건 중 5건입니다.

<!-- licenses:end -->

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

참고로, 약물 상호작용 조회에서 100건이 확인되었으며 이 중 일부는 다음과 같습니다.
- **주요(Major) 등급**: Acalabrutinib, Atazanavir
- **중등도(Moderate) 등급**: Hydrochlorothiazide, Amphotericin B, Atorvastatin, Aprepitant 등
- **경미(Minor) 등급**: Acetylsalicylic acid, Cyanocobalamin 등

## 결론 및 다음 단계

**결정: Hold**

**사유:**
십이지장 폐쇄에 대한 임상시험과 문헌이 전혀 없고, 질환의 기계적 특성상 산 억제제의 직접적인 기전적 연결고리도 불분명합니다. 모델 예측만 있는 L5 단계입니다.

**진행하려면 필요한 것:**
- 십이지장 폐쇄 자체를 직접 다룬 임상시험 또는 문헌 근거
- 상세한 작용 기전(MOA) 데이터
- 허가사항(경고·금기) 확인 및 안전성 검토
- 한국 시판 현황의 정확한 확인 (허가 취소 여부 등)

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다. 작용 기전 자료가 없다는 문장은 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Prevacid (lansoprazole) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=71ba78cb-7e46-43eb-9425-fa130f537f84) |
| 2026-11-24 | 허가 구성: “모두 단일 성분” → 침강탄산칼슘 복합제 포함 | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

