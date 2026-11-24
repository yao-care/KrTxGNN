---
layout: default
title: Tadalafil
parent: 모델 예측만 (L5)
nav_order: 714
evidence_level: L5
indication_count: 8
last_modified_at: 2026-11-24
description: "Tadalafil: 예측 신규 적응증 Ambras형 선천성 전신 다모증 (Ambras type hypertrichosis universalis congenita) (근거 수준 L5). 기존 적응증: 1. 발기부전 (erectile dysfunction)의 치료 이 약이 효과적이려면, 성적자극(sexual…"
monitor_inn: "TADALAFIL"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "familial isolated trichomegaly", "kyphoscoliotic heart disease", "migraine with brainstem aura"]
---

# Tadalafil
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

## Tadalafil: 한국 허가 적응증 정보 미확인에서 Ambras형 선천성 전신 다모증으로
{: .text-alpha }

## 한 문장 요약

Tadalafil은 PDE5 억제제로, 한국에서 허가되어 시판 중인 약물입니다(허가 건수와 상태는 빠른 개요 참조). 다만 이번 데이터에는 허가 적응증 본문이 확보되지 않아 기존 적응증을 텍스트로 확인할 수 없습니다.
TxGNN 모델은 **Ambras형 선천성 전신 다모증(Ambras type hypertrichosis universalis congenita)**에 효과가 있을 수 있다고 예측하지만, 이를 지지하는 **임상시험은 0건, 문헌도 0편**입니다.
이 예측 점수는 TxGNN 모델(딥러닝)에서 나온 것이며, 모델이 관련 질환 사이에서 학습한 유사성을 반영할 수 있을 뿐 생물학적 근거는 아닙니다. 현재로서는 보류(Hold)가 타당합니다.

<!-- review:begin kr-lic-20261124c-tadalafil-1 -->

> **검토 정정 (2026-11-24)**: 원래 문장: “Tadalafil은 PDE5 억제제로, 한국에서 20건의 단일제 허가증이 유효한 시판 약물입니다.” 식품의약품안전처 의약품안전나라(nedrug) 허가 자료(2026-11-23 데이터) 기준으로 수정했습니다: 이 사이트 자료의 성분란에는 일치한 성분만 기록되어 허가 품목별 단일 성분·복합 성분 여부를 확인할 수 없으므로, 단일·복합 표기를 빼고 건수는 쓰지 않고 빠른 개요와 「한국 시판 정보」의 표를 가리키도록 고쳤습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261124c-tadalafil-1 -->

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 1. 발기부전 (erectile dysfunction)의 치료 이 약이 효과적이려면, 성적자극(sexual stimulation)을 필요로 한다. 이 약은 여성에 의한 사용을 그 적응증 으로 하지 않는다. 2. 양성 전립선 비대증 양성 전립선 비대증의 징후 및 증상의 치료 3… ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201703977/EE)) |
| 예측 신규 적응증 | Ambras형 선천성 전신 다모증 (Ambras type hypertrichosis universalis congenita) |
| TxGNN 예측 점수 | 0.9998 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 19건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Tadalafil 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “성적 자극 시 음경 발기는 음경 동맥 및 음경해면체 평활근의 이완으로 인한 음경 혈류 증가에 의해 일어난다. 이 반응은 신경 말단 및 내피세포로부터의 산화질소(NO) 방출에 의해 매개되며, 이는 평활근 세포에서 cGMP의 합성을 자극한다. […] 타다라필은 PDE5를 억제한다.” 영어 원문: "Penile erection during sexual stimulation is caused by increased penile blood flow resulting from the relaxation of penile arteries and corpus cavernosal smooth muscle. This response is mediated by the release of nitric oxide (NO) from nerve terminals and endothelial cells, which stimulates the synthesis of cGMP in smooth muscle cells. […] Tadalafil inhibits PDE5." ([DailyMed: Cialis (tadalafil) prescribing information, Eli Lilly and Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=bcd8f8ab-81a2-4891-83db-24a0b0e25895), 버전 2026-06-03; 확인일 2026-11-19). 알려진 정보에 따르면 Tadalafil은 PDE5 억제제로, cGMP 경로를 통해 혈관을 확장시키는 약물입니다. 다만 이 정보는 데이터 수집 항목이 아니라 일반적인 약리학 지식에 근거한 것입니다.

Ambras형 선천성 전신 다모증은 TRPS1 조절에 영향을 주는 유전체 재배열로 발생하는 선천성 모발 성장 질환입니다. PDE5 억제가 이 질환과 연결된다는 그럴듯한 기전은 확립되어 있지 않습니다. 높은 점수는 다모증 관련 네트워크 이웃(예: minoxidil 유사 혈관확장제 연관성)을 반영했을 가능성이 크며, PDE5 특이적 기전을 반영한 것으로 보기 어렵습니다.

참고로 다모증은 minoxidil 같은 혈관확장제의 이상반응으로 알려져 있습니다. 이는 치료 효과가 아니라 부작용 계열의 연관성이므로, 이 방향의 재창출은 지지되지 않습니다.

## 한국 시판 정보

허가증 20건 중 주요 5건입니다. 허가 적응증은 PDF 링크로만 제공되어 본문을 확인하지 못했습니다.

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 201703977 | 발그나필정5밀리그램(타다라필) | 노란색의 모서리가 둥근 삼각형 모양의 필름코팅정제 | 제이더블유신약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201703977/EE) | 유효 |
| 202203569 | 홈런정5밀리그램(타다라필) | 노란색의 모서리가 둥근 삼각형 모양의 필름코팅정제 | 코스맥스파마(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202203569/EE) | 유효 |
| 201501479 | 자이리스정5mg(타다라필) | 노란색의 타원형 필름코팅정 | (주)동구바이오제약 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201501479/EE) | 유효 |
| 201603989 | 시알정20밀리그램(타다라필) | 노란색 리본모양의 필름코팅정제 | 유니메드제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201603989/EE) | 유효 |
| 201805151 | 시알롱기구강용해필름20mg(타다라필) | 흰색의 사각형 구강용해필름 | 대원제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201805151/EE) | 유효 |

위 표는 허가 최소 20건 중 5건입니다.

<!-- licenses:end -->

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 조회되었으며, 상위 항목은 대부분 중등도(Moderate)입니다. 주요 항목은 Aprepitant, Dexamethasone, Clarithromycin, Cimetidine, Miconazole, Clotrimazole, Lorcaserin 및 SGLT2 억제제(Canagliflozin, Dapagliflozin, Empagliflozin, Ertugliflozin) 등입니다. Papaverine은 경미(Minor)로 분류되었습니다.
- **지식그래프 기반 금기 관련 질환** (허가 문서가 아니라 TxGNN 지식그래프의 약물-질환 금기 연결 정보): 간부전, 간질, 대동맥 판막 협착 및 관련 질환, 저혈압, 혈액응고 질환, 급성 관상동맥 증후군, 심근경색, 뇌졸중 및 뇌경색, 겸상적혈구빈혈 및 혈색소병증, 다발골수종, 백혈병, 지속발기증, 페이로니병, 청력 손실, 비후성 심근병증 등이 포함됩니다.
- **편두통 관련 신호**: 8순위 예측 질환(뇌간 전조 편두통)과 관련해, tadalafil이 두통 없는 전형적 편두통 전조를 유발했다는 증례 보고(PMID 17059442, 2006)가 있습니다. 이는 편두통 전조 환자에서의 안전성 신호일 수 있습니다.

허가사항의 경고 및 금기 본문은 확보되지 않았으므로 허가사항을 직접 확인해야 합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
Ambras형 선천성 전신 다모증에 대한 임상시험과 문헌이 없고, 모델 점수 외에는 근거가 없습니다(L5). 기전상 타당성도 부족하며, 상위 예측 8건 모두 Hold입니다. 가장 기전적으로 개연성이 있는 항목은 후통 심장질환(kyphoscoliotic heart disease)이지만, 이 역시 직접 근거가 없는 외삽 수준입니다. 편두통은 오히려 부작용 방향의 증례만 있습니다.

**진행하려면 필요한 것:**
- 허가 적응증 및 경고·금기 본문 확보 (한국 식약처 허가사항 PDF 파싱). 안전성 스크리닝 진행의 차단 요소입니다.
- DrugBank 등에서 작용 기전(MOA) 데이터 확보
- Ambras형 다모증에서 PDE5/cGMP 경로의 관련성을 보여주는 전임상·기전 연구
- 다모증 계열 예측이 혈관확장제 부작용 연관성에 기인한 것인지 검증
- 대안 후보(예: kyphoscoliotic heart disease)에 대한 별도의 문헌 검색 및 평가

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다. 작용 기전 자료가 없다는 문장은 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Cialis (tadalafil) prescribing information, Eli Lilly and Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=bcd8f8ab-81a2-4891-83db-24a0b0e25895) |
| 2026-11-24 | 단일·복합 표기: “Tadalafil은 PDE5 억제제로, 한국에서 20건의 단일제 허가증이…” → 확인할 수 없는 단일·복합 표기와 건수 삭제(건수는 빠른 개요와 표) | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

