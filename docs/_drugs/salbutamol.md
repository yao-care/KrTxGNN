---
layout: default
title: Salbutamol
parent: 모델 예측만 (L5)
nav_order: 680
evidence_level: L5
indication_count: 8
last_modified_at: 2026-11-24
description: "Salbutamol: 예측 신규 적응증 유두성 결막염 (Papillary Conjunctivitis) (근거 수준 L5)."
monitor_inn: "Salbutamol"
predicted_indications: ["papillary conjunctivitis", "nasal cavity disease", "pharyngitis", "acute laryngopharyngitis", "anaphylaxis", "common cold", "atopic conjunctivitis", "anorectal stricture"]
---

# Salbutamol
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

## Salbutamol: 기관지 확장제에서 유두성 결막염(Papillary Conjunctivitis)으로
{: .text-alpha }

## 한 문장 요약

Salbutamol은 베타-2 작용제 계열의 약물로, 한국에서는 정제와 흡입제 형태로 시판되고 있습니다. TxGNN 모델은 **유두성 결막염(Papillary Conjunctivitis)**에 효과가 있을 수 있다고 예측하지만(예측 점수 1.0000), 이 예측을 뒷받침하는 **임상시험은 0건, 문헌도 0편**입니다. 따라서 현재는 모델 예측만 있는 초기 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 예측 신규 적응증 | 유두성 결막염 (Papillary Conjunctivitis) |
| TxGNN 예측 점수 | 1.0000 |
| 근거 수준 | L5 (모델 예측만 있음) |
| 한국 시판 현황 | 시판 중 (유효 허가 5건 / 전체 6건) |
| 허가증 수 | 6건 (유효 5건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Salbutamol 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “알부테롤 황산염은 베타 2 -아드레날린 작용제이다. 알부테롤 황산염의 약리학적 효과는 기도 평활근의 베타 2 -아드레날린 수용체 활성화에 기인한다. 베타 2 -아드레날린 수용체의 활성화는 아데닐시클라제의 활성화 및 세포 내 고리형 3', 5’-아데노신 일인산(cyclic AMP) 농도의 증가로 이어진다.” 영어 원문: "Albuterol sulfate is a beta 2 -adrenergic agonist. The pharmacologic effects of albuterol sulfate are attributable to activation of beta 2 -adrenergic receptors on airway smooth muscle. Activation of beta 2 -adrenergic receptors leads to the activation of adenylcyclase and to an increase in the intracellular concentration of cyclic-3', 5’-adenosine monophosphate (cyclic AMP)." ([DailyMed: Albuterol Sulfate Inhalation (albuterol sulfate) prescribing information, Amneal Pharmaceuticals NY LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2e449282-ee58-4e36-b983-85c4e6f0864d), 버전 2024-12-20; 확인일 2026-11-19). 이 보고서에 정리된 자료로는 Salbutamol이 베타-2 아드레날린 작용제라는 점만 확인됩니다. 이 약은 기관지 평활근을 이완시키는 기관지 확장제로 알려져 있으며, 한국에서는 흡입제와 정제로 허가되어 있습니다.

결막염에 적용할 수 있다는 근거는 이론적 추정 단계입니다. 베타-2 작용제가 결막의 비만세포에서 매개물질 방출을 줄일 가능성은 있습니다. 그러나 이 가설을 직접 검증한 임상시험이나 문헌은 이번에 수집된 자료에 없습니다.

한국에서 허가된 제형은 정제, 흡입액, 정량분무흡입제 등이며 안구용 제형은 없습니다. 따라서 실제로 개발하려면 새로운 점안 제형이 필요합니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 198900576 | 대우살부타몰정(살부타몰황산염)(수출명:벤탈정)(수출용) | 황색의 원형 정제(수출용:적갈색의 원형정제) | 대우제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/198900576/EE) | 유효 |
| 200607690 | 살부톨흡입액(살부타몰황산염) | 무색의 투명~미황색의 액제 | 대한약품공업(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200607690/EE) | 유효 |
| 200209634 | 벤토린흡입액(살부타몰황산염) | 갈색 유리병에 든 무색~연한 노란색의 투명한 액제 | (주)글락소스미스클라인 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200209634/EE) | 유효 |
| 199906869 | 벤토린에보할러(살부타몰황산염) | 흰색~회백색의 현탁액이 흡입량조절밸브가 달린 내압 금속통에 든 정량분무흡… | (주)글락소스미스클라인 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199906869/EE) | 유효 |
| 199907319 | 벤토린네뷸2.5mg(살부타몰황산염) | 플라스틱 앰플에 든 무색~연한 노란색의 투명한 액제 | (주)글락소스미스클라인 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199907319/EE) | 유효 |

위 표는 허가 6건 중 5건입니다.

<!-- licenses:end -->

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 확인되었습니다. 주요 항목은 다음과 같습니다.
  - 중등도(Moderate): Acarbose, Isometheptene, Famotidine, Epinephrine, Albiglutide, Acetohexamide, Alogliptin, Bisacodyl, Canagliflozin, Castor oil, Chlorpropamide, Cisapride, Clarithromycin, Dapagliflozin, Diethylpropion
  - 경미(Minor): Hydrocortisone, Beclomethasone dipropionate, Betamethasone, Budesonide, Dexamethasone

  혈당강하제 병용 시 혈당 변동, 에피네프린 등 교감신경 작용제 병용 시 심혈관 영향에 유의해야 합니다.

경고, 금기 등 그 밖의 안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
유두성 결막염에 대해서는 TxGNN 예측 점수만 높을 뿐 임상시험과 문헌이 전혀 없고, 기전상의 근거도 가설 수준입니다. 또한 허가된 제형에 점안제가 없어 지금 단계에서 개발을 진행하기는 어렵습니다.

**진행하려면 필요한 것:**
- 결막염에서 베타-2 작용제의 효과를 다룬 전임상·임상 문헌 조사
- 허가사항(경고·금기·적응증 텍스트)과 작용 기전 데이터 확보
- 점안 등 안구용 제형의 필요성 및 실현 가능성 검토
- 약물 상호작용(100건)과 심혈관·저칼륨혈증 위험 검토

**참고:** 이번 자료에는 같은 약물에 대한 다른 예측 적응증도 포함되어 있습니다. 아나필락시스는 Phase 3 시험이 24명 등록 후 조기 종료되어 근거 수준이 L3에 머뭅니다. 이는 별도 평가가 필요합니다.

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Albuterol Sulfate Inhalation (albuterol sulfate) prescribing information, Amneal Pharmaceuticals NY LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2e449282-ee58-4e36-b983-85c4e6f0864d) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

