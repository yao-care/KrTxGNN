---
layout: default
title: Gemcitabine
parent: 모델 예측만 (L5)
nav_order: 372
evidence_level: L5
indication_count: 8
monitor_inn: "Gemcitabine"
predicted_indications: ["rectum mucinous adenocarcinoma", "colon mucinous adenocarcinoma", "villoglandular endometrial endometrioid adenocarcinoma", "endometrial mixed adenocarcinoma", "endometrial mucinous adenocarcinoma", "cervical mucinous adenocarcinoma", "gallbladder mucinous adenocarcinoma", "secretory uterine corpus endometrioid adenocarcinoma"]
last_modified_at: 2026-11-24
description: "Gemcitabine: 예측 신규 적응증 직장 점액성 선암 (근거 수준 L5). 기존 적응증: ○비소세포폐암 - 시스플라틴과병용하여국소진행성또는전이성비소세포폐암의1차치료 -…"
---

# Gemcitabine
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **8** 건
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

## Gemcitabine: 허가 적응증에서 직장 점액성 선암으로
{: .text-alpha }

## 한 문장 요약

Gemcitabine은 한국에서 주사제로 다수 허가된 항종양 약물입니다. 다만 이번 데이터에는 허가 적응증의 구체적인 본문 텍스트가 포함되어 있지 않습니다.
TxGNN 모델은 **직장 점액성 선암(rectum mucinous adenocarcinoma)**에 효과가 있을 수 있다고 예측하지만(점수 0.9977), 이 질환을 직접 다룬 임상시험과 문헌은 **0건**입니다. 따라서 근거 수준은 L5(모델 예측만 존재)입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | ○비소세포폐암 - 시스플라틴과병용하여국소진행성또는전이성비소세포폐암의1차치료 - 단독투여하여국소진행성또는전이성비소세포폐암의고식적치료 ○췌장암 - 국소진행성또는전이성췌장암의1차치료(first‐linetreatment) ○방광암 - 방광암(BladderCancer) ○유방암 - 임상적으로… ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201506534/EE)) |
| 예측 신규 적응증 | 직장 점액성 선암 |
| TxGNN 예측 점수 | 0.9977 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 20건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Gemcitabine 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “젬시타빈은 DNA 합성 중인 세포를 사멸시키고 G1/S기 경계를 통한 세포의 진행을 차단한다. 젬시타빈은 뉴클레오시드 키나아제에 의해 이인산(dFdCDP) 및 삼인산(dFdCTP) 뉴클레오시드로 대사된다.” 영어 원문: "Gemcitabine kills cells undergoing DNA synthesis and blocks the progression of cells through the G1/S-phase boundary. Gemcitabine is metabolized by nucleoside kinases to diphosphate (dFdCDP) and triphosphate (dFdCTP) nucleosides." ([DailyMed: Avgemsi (gemcitabine) prescribing information, Avyxa Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e11eeff7-bcaf-4bf1-8da8-88138e01af84), 버전 2026-07-27; 확인일 2026-11-19). 일반적으로 알려진 바에 따르면 gemcitabine은 뉴클레오시드 유사체 계열 항대사제로, DNA 합성과 리보뉴클레오티드 환원효소를 억제합니다. 이 세포독성 기전은 소화관 선암에서도 이론적으로 가능성이 있습니다.

다만 이번 데이터에서 예측을 뒷받침하는 것은 TxGNN 점수뿐입니다. 직장 점액성 선암과 관련된 임상시험이나 문헌은 확인되지 않았고, 기존 적응증과의 유사성 분석도 완료되지 않았습니다. 따라서 이 예측은 가설 단계로 보아야 합니다.

## 한국 시판 정보

한국 식품의약품안전처(MFDS)에 등록된 단일 성분 허가가 20건 확인되었으며, 전체 목록의 일부일 수 있습니다. 허가 적응증은 링크로만 제공되어 본문을 확인하지 못했습니다. 대표 5건은 다음과 같습니다.

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 201506534 | 젬탄액상주(젬시타빈염산염) | 무색 투명 또는 담황색의 액이 무색 투명한 바이알에 든 주사제 | (주)종근당 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201506534/EE) | 유효 |
| 201402859 | 화이자젬시타빈액상주(젬시타빈염산염) | 무색투명 또는 담황색의 액이 무색투명한 바이알에 든 주사제 | 한국화이자제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201402859/EE) | 유효 |
| 200600254 | 젬자주200밀리그램(젬시타빈염산염) | 동결건조된 흰색 ~ 회백색의 덩어리 또는 분말이 무색 투명한 바이알에 충… | (주)보령 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200600254/EE) | 유효 |
| 202401967 | 인퓨젬주10밀리그램/밀리리터(젬시타빈염산염) | 눈에 보이는 미립자가 없는 무색투명한 액이 무색투명한 수액용 플라스틱 용… | 리퓨어헬스케어(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202401967/EE) | 유효 |
| 200709600 | 젬타빈주2그램(젬시타빈염산염) | 동결건조된 흰색 내지 회백색의 덩어리 또는 분말상이며 녹였을때 맑고 무색… | 한국유나이티드제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200709600/EE) | 유효 |

위 표는 허가 최소 20건 중 5건입니다.

<!-- licenses:end -->

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 약물 (뉴클레오시드 유사체 항대사제) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요. (지식 그래프상 혈소판감소증, 백혈구감소증, 빈혈과 금기 관계가 기록되어 있음) |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요. |
| 모니터링 항목 | 혈구검사(CBC), 간기능, 신기능 |
| 취급 방호 | 세포독성 약물 취급 규정 준수 필요 |

## 안전성 고려사항

허가 문서의 경고 및 금기 정보는 확보되지 않았습니다. 허가사항을 참조하세요.

- **지식 그래프상 금기 관계(허가 문서 근거 아님)**: 신장 질환, 간 질환, 담낭 질환, 혈소판감소증, 감염성 질환, 빈혈, 대적혈구성 빈혈, 간질성 폐질환, 백혈구감소증, 용혈성 요독 증후군
- **약물 상호작용**: 총 100건이 조회되었습니다. 중등도로 분류된 항목은 naltrexone이고, 경미한 항목은 levofloxacin입니다. 나머지 대부분은 등급이 불명확합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
직장 점액성 선암에 대한 임상시험과 문헌이 없고, 근거는 모델 예측뿐(L5)입니다. 허가 적응증 본문과 안전성 정보도 확보되지 않아 안전성 선별 단계로 진행할 수 없습니다.

**진행하려면 필요한 것:**
- MFDS 허가 문서(PDF)를 내려받아 적응증, 경고, 금기 정보 확보
- DrugBank에서 작용 기전(MOA) 확보
- 직장 및 대장 점액성 선암에 대한 gemcitabine 임상시험 및 문헌 조사
- 참고: 같은 예측 목록의 자궁내막 혼합 선암은 후향 연구와 Phase II 시험 등 관련 근거가 있어(L3) 우선 검토 후보가 될 수 있으나, 질환 자체를 직접 다룬 연구는 아니므로 추가 확인이 필요합니다.

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Avgemsi (gemcitabine) prescribing information, Avyxa Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e11eeff7-bcaf-4bf1-8da8-88138e01af84) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

