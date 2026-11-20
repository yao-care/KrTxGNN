---
layout: default
title: Haloperidol
parent: 모델 예측만 (L5)
nav_order: 398
evidence_level: L5
indication_count: 9
monitor_inn: "Haloperidol"
predicted_indications: ["congenital disorder of glycosylation with defective fucosylation", "retinal dystrophy with or without extraocular anomalies", "hydranencephaly (disease)", "myopia X-linked", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "myopia 26, X-linked, female-limited", "syndromic myopia", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "atypical glycine encephalopathy"]
last_modified_at: 2026-11-15
description: "Haloperidol: 예측 신규 적응증 푸코실화 결함을 동반한 선천성 당화 이상증 (congenital disorder of glycosylation with defective fucosylation) (근거 수준 L5). 기존 적응증: 정신분열증(조현병), 제1형 양극성 장애와 관련된 조증삽화, 정신병적 장애의 증상, 투렛증후군(Gilles…"
---

# Haloperidol
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

## Haloperidol: 푸코실화 결함을 동반한 선천성 당화 이상증 (congenital disorder of glycosylation with defective fucosylation)
{: .text-alpha }

## 한 문장 요약

Haloperidol은 도파민 D2 수용체를 차단하는 약물로, 한국에서 단일 성분제 12건이 허가되어 있습니다. TxGNN 모델은 **푸코실화 결함을 동반한 선천성 당화 이상증(congenital disorder of glycosylation with defective fucosylation)**에 효과가 있을 수 있다고 예측합니다(점수 0.9991). 그러나 이를 뒷받침하는 **임상시험은 0건, 문헌도 0편**이어서 모델 예측만 있는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정신분열증(조현병), 제1형 양극성 장애와 관련된 조증삽화, 정신병적 장애의 증상, 투렛증후군(Gilles de laTourette's syndrome) ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/198500618/EE)) |
| 예측 신규 적응증 | 푸코실화 결함을 동반한 선천성 당화 이상증 (congenital disorder of glycosylation with defective fucosylation) |
| TxGNN 예측 점수 | 0.9991 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 12건 / 전체 12건) |
| 허가증 수 | 12건 (유효 12건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Haloperidol 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “성인 조현병 치료에 있어 할로페리돌데카노에이트의 작용기전은 명확하지 않다. 그러나 조현병에서의 효과는 중추 도파민 2형 수용체에서 길항제로 작용하는 활성을 통해 매개될 수 있다.” 영어 원문: "The mechanism of action of haloperidol decanoate for the treatment of schizophrenia in adults is unclear. However, its effect in schizophrenia could be mediated through its activity as an antagonist at central dopamine type 2 receptors." ([DailyMed: haloperidol decanoate prescribing information, BluePoint Laboratories](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3d011250-a517-4c27-8ce3-d59d441ea61c), 버전 2026-11-03; 확인일 2026-11-19). 이번 데이터에서 확인되는 것은 Haloperidol이 도파민 D2 수용체 길항제라는 점뿐입니다.

D2 차단과 푸코실화 경로를 잇는 기전적 연결 고리는 확인되지 않았습니다. 이 질환에 대한 임상시험이나 문헌도 없습니다. 따라서 높은 예측 점수는 모델 출력일 뿐이며, 기전이나 임상 근거로 확인된 것이 아닙니다.

## 한국 시판 정보

12건 모두 단일 성분제입니다. 허가 적응증 본문은 제공되지 않았고 허가사항 문서 링크만 있어, 아래에는 주요 5건을 제시했습니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 198500618 | 명인할로페리돌정1.5밀리그램 | 백색의 원형정제 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/198500618/EE) 참조 |
| 198500715 | 페리돌정3밀리그램(할로페리돌) | 황색의 원형정제 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/198500715/EE) 참조 |
| 198400475 | 페리돌정10밀리그램(할로페리돌) | 청색 원형정제 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/198400475/EE) 참조 |
| 198301325 | 페리돌주(할로페리돌) | 무색투명한 액체가 든 갈색 앰플제 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/198301325/EE) 참조 |
| 198200323 | 페리돌정5밀리그램(할로페리돌) | 연두색의 원형정제 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/198200323/EE) 참조 |

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 기록되어 있습니다. 이 중 위험도가 높은 **Major** 등급으로 확인된 약물은 Bupropion, Morphine, Clarithromycin, Dolasetron입니다. Famotidine, Epinephrine, Hydrocortisone, Atropine 등 다수는 중등도(Moderate)입니다.
- 경고 및 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 이 적응증을 직접 다룬 임상시험과 문헌이 없고, 기전적 연결 고리도 확인되지 않았습니다. 근거는 TxGNN 예측뿐이므로 L5이며, 현 단계에서 진행하기는 어렵습니다.
- 다만 이는 기존에 알려진 항정신병약 용도에 가까워 신규 재창출로 보기 어렵습니다.

**진행하려면 필요한 것:**
- 허가사항 본문(적응증, 경고, 금기) 확보
- 작용 기전 데이터 확보
- D2 차단과 푸코실화 결함 질환을 잇는 기전 또는 전임상 근거
- 이 질환 환자를 대상으로 한 연구 근거

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: haloperidol decanoate prescribing information, BluePoint Laboratories](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3d011250-a517-4c27-8ce3-d59d441ea61c) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

