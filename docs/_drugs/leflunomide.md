---
layout: default
title: Leflunomide
parent: 모델 예측만 (L5)
nav_order: 465
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
description: "Leflunomide: 예측 신규 적응증 단지증-합지증 증후군 (brachydactyly-syndactyly syndrome) (근거 수준 L5). 기존 적응증: 1. 성인에 대하여 아래와 같이 류마티스 관절염 치료에 사용된다. ● 류마티스 관절염의 징후 및 증상 완화…"
monitor_inn: "LEFLUNOMIDE"
predicted_indications: ["brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
---

# Leflunomide
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **2** 건
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

## Leflunomide: 류마티스 질환에서 합지증-단지증 증후군으로
{: .text-alpha }

## 한 문장 요약

Leflunomide는 한국에서 정제로 허가·시판 중인 면역조절 계열 약물입니다(허가 건수와 상태는 빠른 개요 참조). TxGNN 모델은 **단지증-합지증 증후군(brachydactyly-syndactyly syndrome)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 뒷받침하는 **임상시험은 0건**, **문헌도 0편**입니다. 모델 예측 점수만 있는 상태입니다.

<!-- review:begin kr-lic-20261124c-leflunomide-1 -->

> **검토 정정 (2026-11-24)**: 원래 문장: “Leflunomide는 한국에서 단일제 정제로 19건이 허가·시판 중인 면역조절 계열 약물입니다.” 식품의약품안전처 의약품안전나라(nedrug) 허가 자료(2026-11-23 데이터) 기준으로 수정했습니다: 이 사이트 자료의 성분란에는 일치한 성분만 기록되어 허가 품목별 단일 성분·복합 성분 여부를 확인할 수 없으므로, 단일·복합 표기를 빼고 건수는 쓰지 않고 빠른 개요와 「한국 시판 정보」의 표를 가리키도록 고쳤습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261124c-leflunomide-1 -->

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 1. 성인에 대하여 아래와 같이 류마티스 관절염 치료에 사용된다. ● 류마티스 관절염의 징후 및 증상 완화 ● 엑스선(X-ray) 촬영 소견상 관절공간의 감소 및 침식증과 같은 구조적 손상을 억제 ● 류마티스 관절염으로 인하여 저하된 신체기능의 개선 2. 활동성 건선성 관절염의 증상… ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200710887/EE)) |
| 예측 신규 적응증 | 단지증-합지증 증후군 (brachydactyly-syndactyly syndrome) |
| TxGNN 예측 점수 | 0.9993 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 19건 / 전체 19건) |
| 허가증 수 | 19건 (유효 19건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Leflunomide 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “레플루노미드는 디하이드로오로테이트 탈수소효소(de novo 피리미딘 합성에 관여하는 미토콘드리아 효소)를 억제하고 항증식 활성을 갖는 이속사졸계 면역조절제이다. 여러 in vivo 및 in vitro 실험 모델에서 항염 효과가 입증되었다.” 영어 원문: "Leflunomide is an isoxazole immunomodulatory agent that inhibits dihydroorotate dehydrogenase (a mitochondrial enzyme involved in de novo pyrimidine synthesis) and has antiproliferative activity. Several in vivo and in vitro experimental models have demonstrated an anti-inflammatory effect." ([DailyMed: Arava (leflunomide) prescribing information, sanofi-aventis U.S. LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=320f63f2-fac3-4aee-aff8-85724e00ef52), 버전 2025-06-04; 확인일 2026-11-19). 일반적으로 알려진 정보에 따르면 leflunomide는 활성 대사체(teriflunomide)를 통해 DHODH(dihydroorotate dehydrogenase)를 억제하고, 이로써 피리미딘 합성을 차단해 활발히 증식하는 면역세포의 활동을 억제합니다.

신규 적응증과의 연결고리는 약합니다. DHODH 관련 생물학이 Miller 증후군 같은 사지 기형 질환에서 알려져 있지만, 이는 DHODH **결핍**에 의한 질환이며 DHODH **억제**가 이점을 준다는 근거가 아닙니다. 따라서 이 예측 점수는 TxGNN 모델(딥러닝)이 산출한 것이며, 모델이 관련 질환 사이에서 학습한 유사성을 반영할 수 있을 뿐 생물학적 근거는 아닙니다.

또한 leflunomide는 최기형성이 있고 배아·태아 독성에 대한 경고가 있는 약물입니다. 선천성 사지 기형 질환에 사용하는 것은 특히 우려되는 방향입니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

주요 허가 5건입니다. 허가 적응증 본문은 데이터에 없어 허가증 링크로만 제공되었습니다.

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 200710887 | 루알바정20밀리그램(레플루노미드) | 황색 내지 미황색의 삼각형 필름코팅정 | (주)셀트리온제약 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200710887/EE) | 유효 |
| 200711110 | 키마라정20밀리그램(레플루노미드) | 미황색의 삼각형 필름코팅정 | (주)킴스제약 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200711110/EE) | 유효 |
| 200806846 | 아레이정10밀리그램(레플루노미드) | 백색의 원형 필름코팅정 | 한림제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200806846/EE) | 유효 |
| 200808310 | 듀로바정10밀리그램(레플루노미드) | 흰색의 원형 필름코팅정 | 진양제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200808310/EE) | 유효 |
| 200810760 | 류마이드정10밀리그램(레플루노미드) | 백색의 원형필름코팅정 | (주)종근당 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200810760/EE) | 유효 |

위 표는 허가 19건 중 5건입니다.

<!-- licenses:end -->

## 안전성 고려사항

- **약물 상호작용**: 데이터에서 총 100건의 상호작용이 조회되었으며, 주요 항목은 다음과 같습니다.
  - **Major**: Acarbose, Hydrocortisone, Pioglitazone, Bupropion, Triamcinolone, 아세틸살리실산(aspirin), Dexamethasone, Betamethasone, Budesonide, Chenodeoxycholic acid, Clarithromycin, Minocycline, Oxandrolone, Oxymetholone, Naltrexone
  - **Moderate**: Metronidazole, Chlorpropamide, Acetohexamide
  - **Minor**: Zinc sulfate, Zinc acetate
- **지식 그래프상 금기 관련 질환** (허가사항 문구가 아닌 모델 지식 그래프 기반): 간부전·간질환, 신장 질환, 담낭 질환, 만성 B형·C형 간염, 혈소판감소증, 호중구감소증, 무과립구증, 범혈구감소증, 빈혈, 말초신경병증, 간질성 폐질환, 폐포자충증, 아스페르길루스증 등
- **배아·태아 독성**: 최기형성이 있어 배아·태아 독성에 대한 경고가 있는 약물로 알려져 있으며, 선천성 기형 질환 대상 적용 시 특히 중요합니다.

허가사항의 경고 및 금기 항목은 이번 데이터에 포함되지 않았으므로 허가사항을 직접 확인해야 합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
지지 근거가 TxGNN 예측 점수(0.9993) 하나뿐이며 임상시험과 문헌이 전혀 없습니다. 또한 약물의 최기형성 위험이 선천성 사지 기형 질환과 상충하므로, 현 단계에서 재창출을 진행할 근거가 부족합니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기·적응증) 원문 확보 및 분석
- DrugBank 기반 작용 기전(MOA) 데이터 확보
- 단지증-합지증 증후군의 병태생리와 DHODH 억제 간 기전적 연관성에 대한 전임상 근거
- 배아·태아 독성 위험 대비 이익에 대한 평가
- 관련 임상시험 및 문헌 근거 탐색

---

*참고: 동일 약물의 2순위 예측(colobomatous microphthalmia-rhizomelic dysplasia syndrome, 점수 0.9993)도 임상시험·문헌 근거가 없는 L5 수준이며, 마찬가지로 Hold로 평가되었습니다.*

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다. 작용 기전 자료가 없다는 문장은 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Arava (leflunomide) prescribing information, sanofi-aventis U.S. LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=320f63f2-fac3-4aee-aff8-85724e00ef52) |
| 2026-11-24 | 단일·복합 표기: “Leflunomide는 한국에서 단일제 정제로 19건이 허가·시판 중인 …” → 확인할 수 없는 단일·복합 표기와 건수 삭제(건수는 빠른 개요와 표) | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

