---
layout: default
title: Moxifloxacin
parent: 모델 예측만 (L5)
nav_order: 530
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-15
description: "Moxifloxacin: 예측 신규 적응증 폴리클로날 과점성 증후군 (Polyclonal Hyperviscosity Syndrome) (근거 수준 L5). 기존 적응증: 다음의 감수성 균종에 의한 세균성 결막염, 검판선염, 각막염(각막궤양포함)의 치료, 안과수술전후의…"
monitor_inn: "MOXIFLOXACIN"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "congenital hematological disorder", "hematopoietic and lymphoid system neoplasm"]
---

# Moxifloxacin
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

## Moxifloxacin: 세균 감염증에서 폴리클로날 과점성 증후군으로
{: .text-alpha }

## 한 문장 요약

Moxifloxacin은 플루오로퀴놀론계 항균제로, 한국에서 정제, 주사제, 점안액 형태로 시판되고 있습니다.
TxGNN 모델은 **폴리클로날 과점성 증후군(Polyclonal Hyperviscosity Syndrome)**에 효과가 있을 수 있다고 예측하지만, 이 질환에 대한 **임상시험과 문헌은 한 건도 없어** 근거는 모델 예측에 그칩니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 다음의 감수성 균종에 의한 세균성 결막염, 검판선염, 각막염(각막궤양포함)의 치료, 안과수술전후의 무균화요법 : 포도구균속, 연쇄상구균속, 폐렴구균, 장구균속, 마이크로코카스속, 모라셀라속,코리네박테리움속, 시트로박터속, 클렙시엘라속, 엔테로박터속, 세라치아속, 프로테우스속, 몰가네라… ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202003650/EE)) |
| 예측 신규 적응증 | 폴리클로날 과점성 증후군 (Polyclonal Hyperviscosity Syndrome) |
| TxGNN 예측 점수 | 0.9998 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 20건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Moxifloxacin 처방 정보(Prescribing Information)의 “Mechanism of Action” 및 “Microbiology” 항목에 따르면(비공식 번역): “목시플록사신 정제는 플루오로퀴놀론계 항균제에 속한다. […] 목시플록사신의 살균 작용은 세균의 DNA 복제, 전사, 복구 및 재조합에 필요한 토포이소머라제 II(DNA 자이레이스) 및 토포이소머라제 IV의 억제에 기인한다.” 영어 원문: "Moxifloxacin Tablet is a member of the fluoroquinolone class of antibacterial agents. […] The bactericidal action of moxifloxacin results from inhibition of the topoisomerase II (DNA gyrase) and topoisomerase IV required for bacterial DNA replication, transcription, repair, and recombination." ([DailyMed: Moxifloxacin (moxifloxacin hydrochloride) prescribing information, Kesin Pharma Corportation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5a6d3ff1-e853-a3d8-e063-6394a90a18f5), 버전 2026-11-06; 확인일 2026-11-19). 알려진 정보에 따르면 Moxifloxacin은 세균의 DNA gyrase와 topoisomerase IV를 억제하는 플루오로퀴놀론계 항균제입니다.

그러나 이 기전은 혈청 점도나 다클론성 감마글로불린혈증과 연결되지 않습니다. 기존 적응증(세균 감염)과 예측 질환 사이에 기전상 타당한 연관성을 찾기 어렵습니다. 높은 TxGNN 점수는 TxGNN 모델(딥러닝)이 산출한 값으로, 모델이 관련 질환 사이에서 학습한 유사성을 반영할 수 있을 뿐 생물학적 근거는 아니며, 임상적·문헌적 뒷받침도 없습니다.

참고로 다른 상위 예측들도 같은 양상입니다. 고아밀라아제혈증, 선천성 무알부민혈증, 혈액형 부적합 등은 근거가 없거나 간접적입니다. 상위 10개 예측 중 기전상 가장 설득력 있는 것은 **선페스트(bubonic plague)**로, 항균 활성에 기반한 전임상 근거가 있으나 이는 기존 항균제 용도의 연장선입니다.

## 임상시험 근거

폴리클로날 과점성 증후군에 대한 관련 임상시험 등록이 현재 없습니다.

## 문헌 근거

폴리클로날 과점성 증후군에 대한 관련 문헌이 현재 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202003650 | 리목신점안액 | 점안액 | 허가사항 문서 참조 |
| 201904236 | 플로나신점안액 | 점안액 | 허가사항 문서 참조 |
| 201310000 | 모벨록신정400밀리그램 | 필름코팅정 | 허가사항 문서 참조 |
| 201506838 | 퀴녹스주400밀리그램 | 주사제 | 허가사항 문서 참조 |
| 200209450 | 아벨록스주400밀리그람 | 주사제 | 허가사항 문서 참조 |

전체 20건(모두 단일제, 유효)이며, 점안액·정제·주사제가 포함됩니다.

## 안전성 고려사항

- **질환 금기(지식 그래프 기반, 허가사항 아님)**: QT 연장 증후군, 다형성 심실빈맥(torsades de pointes), 간질, 간경변, 저칼륨혈증, 건염, 말초신경병증, *Clostridium difficile* 대장염, 중증 근무력증, 약물유발 간손상, 심근허혈, 관상동맥질환, 심정지, 심장 전도 질환 등
- **약물 상호작용**: 총 100건 확인(상위 20건 조회). 주요(Major) 등급은 hydrocortisone, dexamethasone, betamethasone, triamcinolone(코르티코스테로이드), bupropion, chlorpropamide 등입니다. 중등도(Moderate)에는 metformin, pioglitazone 등 혈당강하제와 칼슘·칼륨 제제 등이 있습니다.
- 예측 순위 7위(후천성 말초신경병증 동반 혈액질환)는 플루오로퀴놀론의 말초신경병증 경고와 상충할 수 있습니다.

허가사항의 경고·금기 정보는 별도로 확인하시기 바랍니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
폴리클로날 과점성 증후군에 대한 임상시험과 문헌이 없고 기전상 연관성도 없어 모델 예측만 존재합니다(L5). 다른 상위 예측들 역시 근거가 없거나 간접적입니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기·적응증) 원문 확보 및 분석
- 작용 기전 데이터 보완
- 예측 질환과의 생물학적 연관성에 대한 가설 및 전임상 근거

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Moxifloxacin (moxifloxacin hydrochloride) prescribing information, Kesin Pharma Corportation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5a6d3ff1-e853-a3d8-e063-6394a90a18f5) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

