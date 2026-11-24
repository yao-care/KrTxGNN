---
layout: default
title: Esomeprazole
parent: 모델 예측만 (L5)
nav_order: 318
evidence_level: L5
indication_count: 1
monitor_inn: "ESOMEPRAZOLE"
predicted_indications: ["duodenal obstruction"]
last_modified_at: 2026-11-24
description: "Esomeprazole: 예측 신규 적응증 십이지장 폐쇄 (duodenal obstruction) (근거 수준 L5). 기존 적응증: 비스테로이드성 소염진통제(나프록센 등)와 관련한 위궤양 및/또는 십이지장궤양의 발생 위험이 있으면서 저용량…"
---

# Esomeprazole
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

## Esomeprazole: 양성자 펌프 억제제 → 십이지장 폐쇄 (duodenal obstruction)
{: .text-alpha }

## 한 문장 요약

Esomeprazole은 위산 분비를 억제하는 양성자 펌프 억제제 계열의 약물입니다.
TxGNN 모델은 **십이지장 폐쇄(duodenal obstruction)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 뒷받침하는 **임상시험은 0건**, **문헌은 0편**입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 비스테로이드성 소염진통제(나프록센 등)와 관련한 위궤양 및/또는 십이지장궤양의 발생 위험이 있으면서 저용량 나프록센 또는 다른 비스테로이드성 소염진통제에 의해 충분하지 않은 환자에서의 골관절염, 류마티스성 관절염, 강직성척추염의 증상 치료 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201403894/EE)) |
| 예측 신규 적응증 | 십이지장 폐쇄 (duodenal obstruction) |
| TxGNN 예측 점수 | 0.9945 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 20건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Esomeprazole 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “에스오메프라졸은 치환 벤즈이미다졸계에 속하는 항분비 화합물로, 위 벽세포의 분비 표면에 있는 H+/K+ ATPase 효소계를 특이적으로 억제하여 위산 분비를 억제한다. 에스오메프라졸은 벽세포의 산성 구획에서 양성자화되고 전환되어 활성 억제제인 비키랄성 설펜아미드를 형성한다.” 영어 원문: "Esomeprazole belongs to a class of antisecretory compounds, the substituted benzimidazoles, that suppress gastric acid secretion by specific inhibition of the H+/K+ ATPase enzyme system at the secretory surface of the gastric parietal cell. Esomeprazole is protonated and converted in the acidic compartment of the parietal cell forming the active inhibitor, the achiral sulphenamide." ([DailyMed: Nexium (esomeprazole magnesium) prescribing information, AstraZeneca Pharmaceuticals LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f4853677-1622-4037-688b-fdf533a11d96), 버전 2025-12-19; 확인일 2026-11-19). 알려진 정보에 따르면 esomeprazole은 위산 분비를 줄이는 계열의 약물이며, 산 관련 상부 위장관 질환에서 사용됩니다.

다만 십이지장 폐쇄는 종양, 협착, 윤상 췌장 등 기계적 원인으로 생기는 경우가 많아, 위산 억제만으로 치료되기 어렵습니다. 궤양과 연관된 협착처럼 이차적인 소화성 합병증에서만 보조적 도움이 될 가능성이 있습니다. 따라서 뚜렷한 기전적 연결고리는 확인되지 않으며, 높은 모델 점수는 어디까지나 예측값일 뿐입니다.

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 201403894 | 나프라졸정 | 세 개의 층으로 이루어진 노란색의 장방형 필름코팅정 | 알보젠코리아(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201403894/EE) | 유효 |
| 201403728 | 에소록센정(나프록센, 에스오메프라졸) | 세 개의 층으로 이루어진 노란색의 장방형 필름코팅정 | 고려제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201403728/EE) | 유효 |
| 201403085 | 나프메드정500/20밀리그램 | 세 개의 층으로 이루어진 노란색의 장방형 필름코팅정 | 에스케이케미칼(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201403085/EE) | 유효 |
| 201606894 | 오엠피에스주40밀리그램(에스오메프라졸나트륨) | 무색의 유리 바이알에 들어있는 흰색 혹은 거의 흰색의 동결 건조물 | (주)종근당 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201606894/EE) | 유효 |
| 200009026 | 넥시움정40밀리그램(에스오메프라졸마그네슘) | 분홍색 장방형 필름코팅정 | 한국아스트라제네카(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200009026/EE) | 유효 |

위 표는 허가 최소 20건 중 5건입니다.

<!-- licenses:end -->

위 표는 주요 5건만 나열한 것이며, 전체 허가 건수는 빠른 개요에 있습니다.

<!-- review:begin kr-lic-20261124b-esomeprazole-1 -->

> **검토 정정 (2026-11-24)**: 원래 문장: “전체 허가증은 8건입니다.” 식품의약품안전처 의약품안전나라(nedrug) 허가 자료(2026-11-23 데이터) 기준으로 수정했습니다: 허가 건수가 자료와 맞지 않아, 건수를 쓰지 않고 빠른 개요와 「한국 시판 정보」의 표를 가리키도록 고쳤습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261124b-esomeprazole-1 -->

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 조회되었으며, 그중 주요(Major) 등급으로는 acalabrutinib, atazanavir 등이 있습니다. 중등도(Moderate) 등급으로는 hydrochlorothiazide, amphotericin B, amikacin, amphetamine, fenofibrate, apalutamide, armodafinil, atorvastatin, bendamustine, bosutinib, bumetanide 등이 있습니다. 경미(Minor) 등급으로는 acetylsalicylic acid, axitinib, bortezomib, brivaracetam, cyanocobalamin 등이 있습니다.

허가사항상의 경고 및 금기는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
십이지장 폐쇄에 대한 임상시험과 문헌이 전혀 없고, 기전상으로도 연결고리가 불분명하여 근거 수준은 L5(모델 예측만 있음)입니다.

**진행하려면 필요한 것:**
- 십이지장 폐쇄(특히 궤양성 협착 등 산 관련 원인)에 대한 임상 또는 관찰 연구 근거
- 상세한 작용 기전(MOA) 데이터
- 허가사항(경고·금기)의 확인 및 정리
- 적용 가능한 투여 경로(주사/경구)에 대한 검토

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다. 작용 기전 자료가 없다는 문장은 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Nexium (esomeprazole magnesium) prescribing information, AstraZeneca Pharmaceuticals LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f4853677-1622-4037-688b-fdf533a11d96) |
| 2026-11-24 | 허가 건수: “전체 허가증은 8건입니다.” → 자료 기준으로 수정(건수는 빠른 개요와 표) | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

