---
layout: default
title: Levothyroxine
parent: 모델 예측만 (L5)
nav_order: 475
evidence_level: L5
indication_count: 4
monitor_inn: "levothyroxine"
predicted_indications: ["renal hypodysplasia/aplasia", "bilateral renal agenesis", "Potter sequence", "Carney complex"]
last_modified_at: 2026-11-15
description: "Levothyroxine: 예측 신규 적응증 신장 저형성/무형성증 (근거 수준 L5). 기존 적응증: 갑상선기능저하증, 점액부종, 크레틴병"
---

# Levothyroxine
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **4** 건
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

## Levothyroxine: 갑상선 질환 치료제에서 신장 저형성/무형성증으로
{: .text-alpha }

## 한 문장 요약

Levothyroxine은 한국에서 19건의 단일제 허가증이 확인된 갑상선호르몬 제제입니다. TxGNN 모델은 **신장 저형성/무형성증(renal hypodysplasia/aplasia)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 직접 뒷받침하는 **임상시험은 0건, 문헌도 0편**입니다. 따라서 이 예측은 모델 예측 수준에 머물러 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 갑상선기능저하증, 점액부종, 크레틴병 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201903264/EE)) |
| 예측 신규 적응증 | 신장 저형성/무형성증 |
| TxGNN 예측 점수 | 0.9967 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 19건 / 전체 19건) |
| 허가증 수 | 19건 (유효 19건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Levothyroxine 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “갑상선 호르몬은 DNA 전사 및 단백질 합성의 조절을 통해 생리적 작용을 나타낸다. Triiodothyronine(T3) 및 L-thyroxine(T4)은 세포핵 내로 확산되어 DNA에 부착된 갑상선 수용체 단백질에 결합한다.” 영어 원문: "Thyroid hormones exert their physiologic actions through control of DNA transcription and protein synthesis. Triiodothyronine (T3) and L-thyroxine (T4) diffuse into the cell nucleus and bind to thyroid receptor proteins attached to DNA." ([DailyMed: Levoxyl (levothyroxine sodium) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=758588c3-c63e-491b-0aa2-4f50d80cb174), 버전 2026-11-06; 확인일 2026-11-19). 일반적으로 levothyroxine은 갑상선호르몬 수용체를 통해 대사와 발달을 조절하며, 갑상선호르몬은 태아 장기 형성에도 전반적인 역할을 합니다.

그러나 신장 저형성/무형성증은 주로 PAX2, HNF1B, RET 등 발달 유전자의 변이로 생기는 구조적 선천 기형입니다. 갑상선호르몬을 보충해도 형성이 잘못되었거나 없는 신장 조직을 되돌리기는 어렵습니다. 따라서 확립된 기전적 연결은 없으며, 높은 점수는 TxGNN 모델(딥러닝)이 관련 질환 사이에서 학습한 유사성을 반영한 것일 수 있고 생물학적 근거는 아닙니다.

같은 순위권의 다른 예측(양측 신장 무형성, Potter 연속체, Carney 복합체)도 모두 L5이며 근거가 없습니다. 그중 Carney 복합체는 갑상선 병변 관리 차원에서 간접적 연관성만 추정됩니다.

## 한국 시판 정보

허가 19건은 모두 단일제이며 유효 상태입니다. 허가 적응증 본문은 문서 링크로만 제공되어 내용을 요약하지 못했습니다. 아래는 주요 5건입니다.

| 허가번호 | 제품명 | 제형 | 제조사 |
|---------|------|------|------|
| 201903264 | 씬지로이드정0.025밀리그램 | 연보라색의 원형 정제 | 부광약품(주) |
| 201700462 | 엘지로이드정 (수출용) | 황색의 원형 정제 | 삼남제약(주) |
| 201804237 | 씬지로이드정0.2밀리그램 | 연두색의 타원형 정제 | 부광약품(주) |
| 200301116 | 씬지록신정100마이크로그램 | 황색의 타원형 정제 | (주)다림바이오텍 |
| 201706645 | 씬지록신정125마이크로그램 | 청색의 타원형 정제 | (주)다림바이오텍 |

## 안전성 고려사항

허가사항의 경고·금기 정보는 확보하지 못했으며, 안전성 정보는 허가사항을 참조하세요.

참고로 지식 그래프에는 고혈압, 뇌하수체 기능저하증, 골다공증, 당뇨병, 당뇨병성 케톤산증, 관상동맥질환, 심근경색 등과 금기 관계가 기록되어 있습니다. 이는 허가 문서의 금기가 아니라 지식 그래프상의 관계이므로 참고용으로만 보아야 합니다.

**약물 상호작용:** 총 666건이 확인되었습니다. 조회된 주요 항목은 다음과 같습니다.
- 중등도: 혈당강하제(acarbose, metformin, pioglitazone, alogliptin, canagliflozin, dapagliflozin, empagliflozin, chlorpropamide), GLP-1 계열(albiglutide, dulaglutide), 위산억제제(omeprazole, rabeprazole, dexlansoprazole), 칼슘·마그네슘 제제(calcium acetate, calcium phosphate, magnesium oxide), epinephrine, isometheptene, diethylpropion
- 경미: cimetidine

## 결론 및 다음 단계

**결정: Hold**

**사유:**
신장 저형성/무형성증에 대한 임상시험과 문헌이 전혀 없고, 기전상으로도 갑상선호르몬 보충이 선천적 신장 구조 이상을 개선할 가능성이 낮습니다. 근거 수준은 L5이며, 점수는 TxGNN 모델(딥러닝)이 관련 질환 사이에서 학습한 유사성을 반영한 것일 수 있을 뿐 생물학적 근거는 아닙니다.

**진행하려면 필요한 것:**
- 약물 작용 기전(MOA) 데이터 확보
- 허가사항 문서에서 적응증, 경고, 금기 확인
- 신장 발달과 갑상선호르몬의 관련성을 다룬 전임상 또는 임상 문헌 확인
- 시판 현황(취소 여부) 확인

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Levoxyl (levothyroxine sodium) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=758588c3-c63e-491b-0aa2-4f50d80cb174) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

