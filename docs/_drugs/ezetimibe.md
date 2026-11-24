---
layout: default
title: Ezetimibe
parent: 모델 예측만 (L5)
nav_order: 336
evidence_level: L5
indication_count: 1
monitor_inn: "EZETIMIBE"
predicted_indications: ["cholesterol-ester transfer protein deficiency"]
last_modified_at: 2026-11-24
description: "Ezetimibe: 예측 신규 적응증 콜레스테롤 에스테르 전달 단백질 결핍증 (근거 수준 L5). 기존 적응증: 원발성 고콜레스테롤혈증 원발성 고콜레스테롤혈증(이형접합 가족형 및 비가족형) 및 혼합형 고지혈증 환자의…"
---

# Ezetimibe
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

## Ezetimibe: 이상지질혈증에서 콜레스테롤 에스테르 전달 단백질 결핍증으로
{: .text-alpha }

## 한 문장 요약

Ezetimibe는 장에서 콜레스테롤 흡수를 억제하여 LDL 콜레스테롤을 낮추는 약물로, 한국에서 단일제 및 스타틴 복합제 형태로 허가되어 있습니다.
TxGNN 모델은 **콜레스테롤 에스테르 전달 단백질 결핍증(cholesterol-ester transfer protein deficiency)**에 효과가 있을 수 있다고 예측하지만, 이 질환을 직접 연구한 임상시험이나 문헌은 없습니다.
현재 이 예측을 직접 뒷받침하는 근거는 모델 예측뿐이며, 관련 문헌 2편은 지질 저하 치료 전반을 다룬 것입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 원발성 고콜레스테롤혈증 원발성 고콜레스테롤혈증(이형접합 가족형 및 비가족형) 및 혼합형 고지혈증 환자의 상승된 총 콜레스테롤 (total-C), LDL-콜레스테롤(LDL-C), 아포B단백(Apo B) 및 트리글리세라이드(TG)를 감소시키고, HDL-콜레스테롤(HDL-C)을 증가시키기… ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201601721/EE)) |
| 예측 신규 적응증 | 콜레스테롤 에스테르 전달 단백질 결핍증 |
| TxGNN 예측 점수 | 0.9909 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 20건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Ezetimibe 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “에제티미브는 소장에서의 콜레스테롤 흡수를 억제하여 혈중 콜레스테롤을 감소시킨다. 에제티미브의 분자 표적은 콜레스테롤 및 식물스테롤의 장내 흡수에 관여하는 스테롤 수송체인 Niemann-Pick C1-Like 1 (NPC1L1)인 것으로 밝혀졌다.” 영어 원문: "Ezetimibe reduces blood cholesterol by inhibiting the absorption of cholesterol by the small intestine. The molecular target of ezetimibe has been shown to be the sterol transporter, Niemann-Pick C1-Like 1 (NPC1L1), which is involved in the intestinal uptake of cholesterol and phytosterols." ([DailyMed: ezetimibe prescribing information, A-S Medication Solutions](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c37c695b-fb40-423c-9b73-d1aa58a34db9), 버전 2026-10-08; 확인일 2026-11-19). 일반적으로 알려진 바에 따르면, Ezetimibe는 NPC1L1 매개 장내 콜레스테롤 흡수를 억제하여 LDL 콜레스테롤을 낮춥니다.

CETP 결핍증은 HDL 콜레스테롤이 높고 지단백 대사가 변하는 유전적 상태로, 그 자체로 치료가 필요한 질환이 아닙니다. 0.9909라는 높은 점수는 TxGNN 모델(딥러닝)이 관련 질환 사이에서 학습한 유사성을 반영했을 가능성이 크며, 생물학적 근거나 실제 치료 관계를 의미한다고 보기 어렵습니다.

Ezetimibe가 이 질환 자체의 치료제라고 볼 기전적 근거는 없습니다. 다만 CETP 결핍증 환자가 이상지질혈증이나 심혈관 위험 상승을 동반하는 경우 지질 저하제로 쓰일 수 있다는 추정이 가능하나, 이는 추측 수준입니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [40911366](https://pubmed.ncbi.nlm.nih.gov/40911366/) | 2025 | Review | European Heart Journal | LDL-C, 중성지방, apoB, Lp(a) 등 지질 저하 표적 전반을 다룬 종설로, CETP 결핍증을 직접 다루지 않음 |
| [31779098](https://pubmed.ncbi.nlm.nih.gov/31779098/) | 2019 | 동물 모델 연구 (햄스터) | International Journal of Molecular Sciences | Ldlr 이형접합 결핍 햄스터에서 PCSK9 항체의 효능을 평가한 모델 연구로, Ezetimibe나 CETP 결핍증 치료를 직접 다루지 않음 |

## 한국 시판 정보

아래는 확인된 허가 중 일부이며, 전체 목록이 아닐 수 있습니다. 허가 적응증 원문은 링크로만 제공되어 요약하지 못했습니다. 이 목록의 제품 중 다수는 스타틴 등과의 복합제이므로, 단일 성분 Ezetimibe의 허가 현황으로 해석해서는 안 됩니다.

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 201701413 | 에제스롤정(에제티미브) | 흰색 내지 거의 흰색의 장방형 정제 | 환인제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201701413/EE) | 유효 |
| 201500366 | 아토젯정10/80밀리그램 | 백색 내지 미백색의 한 면에 357이 새겨진 양면이 볼록한 캡슐모양의 필… | 한국오가논(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201500366/EE) | 유효 |
| 201606048 | 슈바젯정10/20밀리그램(에제티미브, 로수바스타틴) | 분홍색의 장방형 필름코팅정 | 안국약품(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201606048/EE) | 유효 |
| 201007235 | 이지심바정10/10밀리그램(에제티미브, 심바스타틴) | 흰색 내지 연한 노란색의 양면이 볼록한 장방형의 정제 | (주)서흥 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201007235/EE) | 유효 |
| 202402807 | 암로젯정10/5/10밀리그램(암로디핀,로수바스타틴,에제티미브) | 분홍색의 양면이 볼록한 원형 필름코팅정 | (주)셀트리온제약 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202402807/EE) | 유효 |

위 표는 허가 최소 20건 중 5건입니다.

<!-- licenses:end -->

## 안전성 고려사항

- **지식그래프상 금기 관계**: 지식그래프(PrimeKG)에 기록된 관계로, 허가사항 문구가 아닙니다. 췌장염, 간 질환, 담낭 질환, 근병증, 근육 질환, 골격근 질환, 가족성 주기성 마비, 약물 남용/의존, 횡문근융해증, 결절성 근막염이 있습니다.
- **약물 상호작용**: 데이터베이스에 총 100건이 조회되었으며, 중등도로 분류된 주요 항목은 다음과 같습니다.
  - Chenodeoxycholic acid
  - Eluxadoline
  - Rosuvastatin
  - Simvastatin
- 그 밖에 Calcitriol, Pantoprazole, Glimepiride, Metformin, Omeprazole 등은 상호작용 등급이 불명입니다.

허가사항의 경고 및 금기 정보는 허가사항 원문을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
CETP 결핍증은 그 자체로 치료 대상이 아닌 유전적 상태이며, 이 질환을 직접 연구한 임상시험과 문헌이 없어 근거 수준은 L5입니다. 높은 TxGNN 점수는 네트워크 근접성을 반영한 것으로 보이며, 치료적 관련성을 뒷받침하지 않습니다.

**진행하려면 필요한 것:**
- 허가사항 원문(경고·금기·적응증) 확보 및 분석
- 상세한 작용 기전(MOA) 데이터 확보
- CETP 결핍증 환자 중 이상지질혈증 또는 심혈관 위험이 높은 집단에서 Ezetimibe 사용을 직접 평가한 연구 탐색
- 예측 대상 질환을 치료 필요 질환으로 볼 수 있는지에 대한 임상적 재검토

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: ezetimibe prescribing information, A-S Medication Solutions](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c37c695b-fb40-423c-9b73-d1aa58a34db9) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

