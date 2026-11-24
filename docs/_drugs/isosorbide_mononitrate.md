---
layout: default
title: Isosorbide Mononitrate
parent: 모델 예측만 (L5)
nav_order: 441
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Isosorbide Mononitrate: 예측 신규 적응증 다모증 (Hypertrichosis) (근거 수준 L5). 기존 적응증: 1. 관동맥심질환(협심증, 심근경색 등) 2. 울혈성심부전의 보조요법(강심배당체 또는 이뇨제와 병용)"
monitor_inn: "Isosorbide mononitrate"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "alopecia", "isolated genetic hair shaft abnormality", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "pulmonary arterial hypertension"]
---

# Isosorbide Mononitrate
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
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

## Isosorbide mononitrate: 협심증 치료제에서 다모증 (Hypertrichosis)으로
{: .text-alpha }

## 한 문장 요약

Isosorbide mononitrate는 일산화질소(NO) 공여체 계열의 혈관확장제로, 한국에서 단일제로 허가되어 시판되고 있습니다. TxGNN 모델은 **다모증(Hypertrichosis)**에 효과가 있을 수 있다고 예측하지만, 이 예측을 지지하는 **임상시험은 0건, 문헌도 0편**입니다. 따라서 현재로서는 모델 예측만 있는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 1. 관동맥심질환(협심증, 심근경색 등) 2. 울혈성심부전의 보조요법(강심배당체 또는 이뇨제와 병용) ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/198601383/EE)) |
| 예측 신규 적응증 | 다모증 (Hypertrichosis) |
| TxGNN 예측 점수 | 1.0000 (전체 순위 265위) |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 2건 / 전체 3건) |
| 허가증 수 | 3건 (유효 2건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Isosorbide Mononitrate 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “이소소르비드 일질산염 서방정은 이소소르비드 이질산염의 주요 활성 대사체인 ISMN의 경구용 서방형 제제이며, 이질산염의 임상적 활성의 대부분은 일질산염에 기인한다. ISMN 및 일반적으로 모든 유기 질산염의 주된 약리학적 작용은 혈관 평활근의 이완으로, 말초 동맥과 정맥, 특히 정맥의 확장을 일으킨다.” 영어 원문: "Isosorbide mononitrate extended-release tablet are an oral extended-release formulation of ISMN, the major active metabolite of isosorbide dinitrate; most of the clinical activity of the dinitrate is attributable to the mononitrate. The principal pharmacological action of ISMN and all organic nitrates in general is relaxation of vascular smooth muscle, producing dilatation of peripheral arteries and veins, especially the latter." ([DailyMed: isosorbide mononitrate prescribing information, Golden State Medical Supply, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=86be0e85-5337-bee4-e053-2a91aa0a8158), 버전 2026-11-10; 확인일 2026-11-19). 알려진 정보에 따르면 Isosorbide mononitrate는 NO 공여체로서 cGMP 경로를 통해 혈관을 확장합니다. 다만 이 내용은 데이터 수집 과정에서 확보된 공식 MOA가 아니라 일반적인 약리학적 설명입니다.

다모증과의 기전적 연관성은 **신뢰할 만한 수준으로 확인되지 않았습니다**. minoxidil 같은 혈관확장제가 다모증을 유발하는 것으로 알려져 있어 혈관확장과 털 성장 사이에 관련이 있을 수는 있습니다. 그러나 이는 치료 효과가 아니라 **이상반응 가능성**에 가깝습니다. 높은 TxGNN 점수는 TxGNN 모델(딥러닝)이 관련 질환 사이에서 학습한 유사성을 반영할 수 있을 뿐 생물학적 근거는 아니며, 임상 또는 문헌 근거가 뒷받침하지 않습니다.

참고로 상위 예측 10건은 대부분 모발·선천성 기형 관련 질환(Ambras형 선천성 전신 다모증, 탈모, 원형탈모 등)이며, 대부분 기전적 연관성이 없는 것으로 평가되었습니다. 이 중 **폐동맥 고혈압(10위)**은 NO-sGC-cGMP 경로가 검증된 표적이므로 생물학적으로 가장 그럴듯하며, 별도의 연구 질문으로 검토할 만합니다. 다만 만성 사용 시 내성, 전신 저혈압, 환기-관류 불일치 가능성이 있고, 현행 가이드라인은 PAH에 경구 질산염을 권고하지 않습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

다모증에 대한 관련 문헌이 없습니다. 참고로 10위 예측인 폐동맥 고혈압에서는 다음 2편이 확인되었으나, 직접적인 근거는 아닙니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [16422873](https://pubmed.ncbi.nlm.nih.gov/16422873/) | 2005 | 임상 혈역학 연구 | J Sex Med | 관상동맥질환 및 발기부전 남성에서 sildenafil과 isosorbide mononitrate의 혈역학적 효과 (PAH 환자 대상 아님) |
| [29705351](https://pubmed.ncbi.nlm.nih.gov/29705351/) | 2018 | 전임상 동물 연구 | Life Sci | monocrotaline 유발 폐고혈압 쥐에서 sGC 자극 효과 (isosorbide mononitrate를 직접 시험하지 않음) |

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 198601383 | 엘로톤정20밀리그램(이소소르비드일질산염) | 담황색의 원형 정제 | 현대약품(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/198601383/EE) | 유효 |
| 198902253 | 엘로톤정40밀리그램(이소소르비드일질산염) | 담황색의 원형 정제 | 현대약품(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/198902253/EE) | 유효 |

위 표는 허가 3건 중 2건입니다.

<!-- licenses:end -->

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 조회되었으며, 주요 항목은 다음과 같습니다.
  - 중등도: bupropion, morphine, canagliflozin, dapagliflozin, empagliflozin, ertugliflozin, dronabinol, nabilone, opium, sapropterin, rosiglitazone
  - 경미: omeprazole
- **지식 그래프 기반 금기 질환** (허가사항 문구가 아니라 TxGNN 지식 그래프의 약물-질환 금기 연결 정보): 저혈압, 비후성 심근병증, 심근경색, 관상동맥 혈전증, 혈색소병증, 빈혈(거대적혈구성 포함), 갑상선기능항진증, 그레이브스병, 갑상선중독증, 뇌내출혈
- 이 약의 허가사항상 경고 및 금기는 아직 확인되지 않았으므로 허가사항을 직접 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
다모증 예측에는 임상시험과 문헌 근거가 전혀 없고, 기전적으로도 치료보다 이상반응에 가까운 방향입니다. 근거 수준은 L5(모델 예측만 존재)입니다. 전신 투여 시 저혈압과 두통 위험도 있어 현 단계에서 진행할 근거가 부족합니다.

**진행하려면 필요한 것:**
- MFDS 허가사항(경고·금기·적응증)을 내려받아 확인 (현재 안전성 선별을 진행할 수 없는 차단 수준의 데이터 공백)
- DrugBank에서 작용 기전(MOA) 데이터 확보
- 모발 질환 예측은 중단하거나 후순위로 두고, 기전적 타당성이 상대적으로 높은 폐동맥 고혈압을 별도 연구 질문으로 검토 (PAH 환자 대상 문헌고찰, 내성·저혈압 문제 평가 포함)

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: isosorbide mononitrate prescribing information, Golden State Medical Supply, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=86be0e85-5337-bee4-e053-2a91aa0a8158) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

