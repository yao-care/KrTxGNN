---
layout: default
title: Allopurinol
parent: 모델 예측만 (L5)
nav_order: 42
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-20
description: "Allopurinol: 예측 신규 적응증 간성 포르피린증 (Hepatic Porphyria) (근거 수준 L5). 기존 적응증: (정제) 통풍, 고뇨산혈증, 요산신장병증"
monitor_inn: "Allopurinol"
predicted_indications: ["hepatic porphyria", "hepatoportal sclerosis", "primitive portal vein thrombosis", "idiopathic copper-associated cirrhosis", "hepatopulmonary syndrome", "early-onset familial noncirrhotic portal hypertension", "disorder of phenylalanine metabolism", "immune-mediated necrotizing myopathy", "antisynthetase syndrome", "idiopathic eosinophilic myositis"]
---

# Allopurinol
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

## Allopurinol: 통풍·고요산혈증에서 간성 포르피린증으로
{: .text-alpha }

## 한 문장 요약

Allopurinol은 잔틴 산화효소 억제제로, 한국에서 자이로릭정 등으로 시판 중입니다. TxGNN 모델은 **간성 포르피린증(Hepatic Porphyria)**에 효과가 있을 수 있다고 예측하지만, 현재 임상시험은 **0건**이고 직접 관련된 문헌은 **가설 수준의 2편**뿐입니다. 따라서 임상적 근거가 아닌 연구 질문 단계의 예측입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | (정제) 통풍, 고뇨산혈증, 요산신장병증 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/197000050/EE)) |
| 예측 신규 적응증 | 간성 포르피린증 (Hepatic Porphyria) |
| TxGNN 예측 점수 | 0.9995 |
| 근거 수준 | L5 (전임상·기전 수준) |
| 한국 시판 현황 | 시판 중 (유효 허가 2건 / 전체 2건) |
| 허가증 수 | 2건 (유효 2건) |
| 권장 결정 | Hold (연구 질문 단계) |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Allopurinol 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “알로푸리놀은 천연 퓨린 염기인 하이포잔틴의 구조 유사체이다. 알로푸리놀과 그 대사체인 옥시푸리놀은 하이포잔틴을 잔틴으로, 잔틴을 사람에서 퓨린 대사의 최종 산물인 요산으로 전환시키는 효소인 잔틴 산화효소를 저해한다.” 영어 원문: "Allopurinol is a structural analogue of the natural purine base, hypoxanthine. Allopurinol and its oxypurinol metabolite inhibitor xanthine oxidase, the enzyme responsible for the conversion of hypoxanthine to xanthine and of xanthine to uric acid, the end product of purine metabolism in humans." ([DailyMed: Aloprim (allopurinol) prescribing information, Mylan Institutional LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=10cc918f-aa44-415b-932d-2404695ac449), 버전 2022-02-18; 확인일 2026-11-19). 일반적으로 알려진 바에 따르면 allopurinol은 잔틴 산화효소를 억제하여 퓨린 대사와 요산 생성을 줄이는 약물입니다. 다만 이 정보는 이번에 수집된 데이터에 포함되어 있지 않아 보조적인 참고로만 제시합니다.

간성 포르피린증과의 연관성은 간접적이고 가설 수준입니다. 2019년 논문은 헴 생합성의 속도조절 효소인 5-아미노레불린산 합성효소(ALAS1)를 대사적으로 표적화하는 가설을 제시했고, 1992년 쥐 연구는 약물이 간 헴 대사에 미치는 영향을 다루었습니다. 오래된 문헌에서 allopurinol이 간 헴 산화효소와 헴 합성에 영향을 줄 수 있다고 보고되었지만, 사람에서 포르피린증 발작이나 포르피린 전구체(ALA/PBG) 수치를 평가한 자료는 없습니다.

특히 일부 약물은 포르피린증을 악화시킬 수 있으므로, 임상적 고려 전에 급성 포르피린증에서의 안전성을 반드시 먼저 검토해야 합니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [31443750](https://pubmed.ncbi.nlm.nih.gov/31443750/) | 2019 | 리뷰/가설 | Medical Hypotheses | 트립토판 및 트립토판 2,3-디옥시게나제의 헴 이용 억제를 통해 ALAS1을 조절하는 급성 간성 포르피린증 치료 가설 |
| [1567472](https://pubmed.ncbi.nlm.nih.gov/1567472/) | 1992 | 전임상 (동물) | Biochemical Pharmacology | 카르바마제핀이 쥐 간 헴 대사에 미치는 영향과 포르피린증 악화 기전 |

두 문헌 모두 allopurinol 자체를 직접 평가한 연구가 아니므로, 간접적인 배경 근거로만 볼 수 있습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 197000050 | 자이로릭정(알로푸리놀) | 흰색의 원형 정제 | 허가사항 원문 참조 (삼일제약) |
| 197900066 | 유유알로푸리놀정 | 백색 원형 정제 | 허가사항 원문 참조 ((주)유유제약) |

## 안전성 고려사항

- **지식그래프 기반 금기 관련 질환** (허가사항이 아닌 TxGNN 지식그래프의 약물-질환 금기 연결): 간 질환, 담낭 질환, 신기능 장애, 과민성 혈관염, 피부 백혈구파괴성 혈관염, 알레르기성 피부 혈관염, 항사구체기저막 질환
- **약물 상호작용**: 총 100건이 조회되었으며, 주요 항목은 다음과 같습니다.
  - 중등도: 수산화알루미늄(Aluminum hydroxide), 아타풀자이트(Attapulgite), 카올린(Kaolin), 마갈드레이트(Magaldrate), 수크랄페이트(Sucralfate)
  - 경미: 아목시실린(Amoxicillin), 클로르프로파미드(Chlorpropamide)
  - 등급 미상: 칼시트리올, 비타민 A, 판토프라졸, 글리메피리드, 메살라진, 독시사이클린, 메트포르민, 오메프라졸, 모르핀 등
- 허가사항상의 경고·금기 정보는 이번 데이터에 포함되어 있지 않으므로 허가사항을 참조하세요.
- 간 질환이 지식그래프상 금기 연결로 나타나므로, 간성 질환을 대상으로 한 재창출에서는 특별한 주의가 필요합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
간성 포르피린증 예측은 TxGNN 점수가 높지만(0.9995) 임상시험이 없고, 문헌도 allopurinol을 직접 평가하지 않은 가설·동물 연구에 한정됩니다. 약물이 포르피린증을 악화시킬 수 있다는 점과, 지식그래프상 간 질환 금기 연결도 고려해야 합니다.

**진행하려면 필요한 것:**
- 허가사항 원문(경고·금기·적응증)의 확보 및 분석
- DrugBank 등에서 작용 기전(MOA) 데이터 확보
- 헴 생합성 및 ALAS1에 대한 allopurinol의 영향을 확인하는 전임상 연구
- 급성 포르피린증에서의 안전성(발작 유발 가능성)에 대한 명시적 검토
- 사람 대상 데이터(ALA/PBG 수치 등) 확보 여부 확인

**참고:** 2위 이하의 예측 질환(간문맥경화증, 특발성 구리 연관 간경변, 간폐증후군, 면역매개 괴사성 근병증 등)은 모두 근거 수준 L5로 임상시험과 직접 관련 문헌이 없으며, 일부는 allopurinol의 과민반응·호산구증가 위험과 상충할 수 있어 Hold로 판단됩니다.

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Aloprim (allopurinol) prescribing information, Mylan Institutional LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=10cc918f-aa44-415b-932d-2404695ac449) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

