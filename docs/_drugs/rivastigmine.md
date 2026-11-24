---
layout: default
title: Rivastigmine
parent: 모델 예측만 (L5)
nav_order: 662
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Rivastigmine: 예측 신규 적응증 녹내장 (Glaucoma) (근거 수준 L5). 기존 적응증: 경도 내지 중등도의 알츠하이머형 치매 또는 파킨슨병과 관련된 치매의 대증적 치료 중증 알츠하이머형 치매의…"
monitor_inn: "RIVASTIGMINE"
predicted_indications: ["glaucoma"]
---

# Rivastigmine
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

## Rivastigmine: 알츠하이머형 치매에서 녹내장으로
{: .text-alpha }

## 한 문장 요약

Rivastigmine은 콜린에스테라제 억제제 계열 약물로, 한국에서 패취제 형태로 허가되어 시판되고 있습니다. TxGNN 모델은 **녹내장(Glaucoma)**에 효과가 있을 수 있다고 예측하며, 현재 등록된 임상시험은 없고 **3편의 문헌**(토끼 전임상 연구 1편 포함)이 이 방향을 간접적으로 지지합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 경도 내지 중등도의 알츠하이머형 치매 또는 파킨슨병과 관련된 치매의 대증적 치료 중증 알츠하이머형 치매의 대증적 치료 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201401412/EE)) |
| 예측 신규 적응증 | 녹내장 (Glaucoma) |
| TxGNN 예측 점수 | 0.9927 |
| 근거 수준 | L5 (전임상·기전 연구 수준) |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 20건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

Rivastigmine은 아세틸콜린에스테라제와 부티릴콜린에스테라제를 억제하는 콜린에스테라제 억제제입니다. 미국 FDA가 승인한 Rivastigmine 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “리바스티그민의 정확한 작용기전은 알려져 있지 않으나, 콜린성 기능을 증강시킴으로써 치료 효과를 나타내는 것으로 생각된다. 이는 콜린에스테라제에 의한 아세틸콜린의 가수분해를 가역적으로 억제하여 아세틸콜린의 농도를 증가시킴으로써 이루어진다.” 영어 원문: "Although the precise mechanism of action of rivastigmine is unknown, it is thought to exert its therapeutic effect by enhancing cholinergic function. This is accomplished by increasing the concentration of acetylcholine through reversible inhibition of its hydrolysis by cholinesterase." ([DailyMed: rivastigmine tartrate prescribing information, American Health Packaging](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=52781229-ee82-43f9-a113-4419a611978d), 버전 2025-11-11; 확인일 2026-11-19).

눈에서 콜린 작용이 강화되면 섬유주(trabecular meshwork)와 섬모체근 수축을 통해 방수 배출이 늘어날 수 있습니다. 이는 pilocarpine 같은 부교감신경 작용제가 안압을 낮추는 방식과 유사합니다. 토끼에서 rivastigmine을 점안했을 때 안압이 감소했다는 연구가 있어 생물학적 개연성을 뒷받침합니다. 2024년 콜린 작용제와 안압 감소에 관한 계통 유전학·분자 수준 리뷰도 간접적인 근거를 제공합니다.

다만 TxGNN 점수(0.9927)는 컴퓨터 예측값일 뿐이며, 사람 대상 데이터는 없습니다. 따라서 기전 연결은 검증된 것이 아니라 추정 단계입니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [10673128](https://pubmed.ncbi.nlm.nih.gov/10673128/) | 2000 | 전임상 (토끼, 점안) | J Ocul Pharmacol Ther | 선택적 아세틸콜린에스테라제 억제제인 rivastigmine 점안이 정상 안압 토끼에서 안압을 낮추는지 평가한 연구 |
| [39130374](https://pubmed.ncbi.nlm.nih.gov/39130374/) | 2024 | 리뷰 (계통 유전학·기전) | Front Mol Biosci | 콜린 작용제의 안압 감소 효과와 전안부 콜린계를 다룬 리뷰. M3 수용체 작용제의 전신 콜린성 부작용이 한계로 제시됨 |
| [27967267](https://pubmed.ncbi.nlm.nih.gov/27967267/) | 2017 | 리뷰 (특허 문헌) | Expert Opin Ther Pat | 아세틸콜린에스테라제 억제제와 재활성화제의 특허 동향. 경미한 억제가 알츠하이머병, 중증근무력증, 녹내장 등에서 치료적 의미가 있다고 언급 |

임상시험 등록은 현재 없습니다.

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 201401412 | 리바덤패취10(리바스티그민) | 점착층에 사각형 베이지색 보호 필름과 피복체가 부착된 10 ㎠ 크기의 패… | 아이큐어(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201401412/EE) | 유효 |
| 200712637 | 엑셀론패취5(리바스티그민) | 이중 점착층에 원형 베이지색 보호필름과 직사각형의 박리지가 부착된 5㎠… | 한국노바티스(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200712637/EE) | 유효 |
| 202502150 | 리셀톤멀티데이패취51.84밀리그램(리바스티그민) | RID-TDS 9.5mg/24h이 파란색 글씨로 인쇄되어 있는 가로x세로… | 명인제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202502150/EE) | 유효 |
| 201307729 | 디누보패취5(리바스티그민) | 약물을 함유한 점착층에 연한 노랑색의 보호필름과 투명한 박리지가 부착된… | 신일제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201307729/EE) | 유효 |
| 201803070 | 엑셀리바패취15(리바스티그민) | 이중 점착층에 흰색 반투명한 원형 보호필름과 엠보싱 처리된 사각형의 이형… | 대웅바이오(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201803070/EE) | 유효 |

위 표는 허가 최소 20건 중 5건입니다.

<!-- licenses:end -->

허가 건수와 상태는 빠른 개요와 위 표에 있습니다. 이 중 일부는 수출용입니다. 모든 제형이 경피 패취제이며, 안과용 제형은 없습니다.

<!-- review:begin kr-lic-20261124c-rivastigmine-1 -->

> **검토 정정 (2026-11-24)**: 원래 문장: “전체 20건 모두 단일제이며 유효 상태입니다.” 식품의약품안전처 의약품안전나라(nedrug) 허가 자료(2026-11-23 데이터) 기준으로 수정했습니다: 이 사이트 자료의 성분란에는 일치한 성분만 기록되어 허가 품목별 단일 성분·복합 성분 여부를 확인할 수 없으므로, 단일·복합 표기를 빼고 건수는 쓰지 않고 빠른 개요와 「한국 시판 정보」의 표를 가리키도록 고쳤습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261124c-rivastigmine-1 -->

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 조회되었으며, 그중 주요 항목은 다음과 같습니다.
  - **Major**: Bupropion
  - **Moderate**: Famotidine, Ranitidine, Cimetidine, Atropine, Hyoscyamine, Glycopyrronium, Dicyclomine, Trospium(항콜린제 다수), Loperamide, Metronidazole, Clarithromycin, Levofloxacin, Dolasetron, Palonosetron 등
  - 항콜린제와는 약리학적으로 작용이 상쇄될 수 있습니다.
- **지식 그래프 기반 금기 관련 질환** (허가사항이 아닌 모델의 지식 그래프에서 추출): 간질, 기저핵 질환, 천식, 만성폐쇄성폐질환, 활동성 소화성 궤양, 요로 폐쇄, 동기능부전증후군, 방실차단, 심장 전도 질환, 급성 심정지, 파킨슨병, 설사성 질환, 신경성 식욕부진증, 안검경련, 국소 손 근긴장이상 등
- 허가사항 기준의 경고 및 금기 정보는 이번 자료에 포함되어 있지 않으므로 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
녹내장에 대한 근거는 토끼 점안 연구와 기전 리뷰 등 전임상·간접 근거에 그치며, 사람 대상 임상시험은 없습니다. 또한 한국 허가 제형이 모두 경피 패취제여서 안과 국소 투여를 위한 별도 제형 개발이 필요하고, 허가사항 기반 안전성 정보도 확보되지 않았습니다.

**진행하려면 필요한 것:**
- 허가사항(첨부문서)에서 경고·금기 정보 확보 (안전성 선별의 필수 선행 조건)
- DrugBank 등에서 상세 작용 기전(MOA) 데이터 확보
- 녹내장 모델에서의 추가 전임상 연구 및 점안 제형의 안전성·안구 투과성 평가
- 사람 대상 임상시험 설계 가능성 검토
- 기존 허가 적응증의 구체적 내용 확인 (허가 문서 파싱)
- 서맥·방실차단 등 심혈관계 위험과 항콜린제 병용 등 약물 상호작용에 대한 고려

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다. 작용 기전 자료가 없다는 문장은 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: rivastigmine tartrate prescribing information, American Health Packaging](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=52781229-ee82-43f9-a113-4419a611978d) |
| 2026-11-24 | 단일·복합 표기: “전체 20건 모두 단일제이며 유효 상태입니다.” → 확인할 수 없는 단일·복합 표기와 건수 삭제(건수는 빠른 개요와 표) | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

