---
layout: default
title: Tinidazole
parent: 모델 예측만 (L5)
nav_order: 738
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Tinidazole: 예측 신규 적응증 폐경 후 위축성 질염 (postmenopausal atrophic vaginitis) (근거 수준 L5). 기존 적응증: 1. 트리코모나스증 2. 혐기성균 감염증 3. 아메바증 4. 람블편모충증 5. 비특이성 질염"
monitor_inn: "TINIDAZOLE"
predicted_indications: ["postmenopausal atrophic vaginitis", "ulceration of vulva", "vulvar neoplasm", "breast fibrocystic disease", "AIDS", "blunt duct adenosis of breast", "apocrine adenosis of breast", "AIDS related complex", "congenital human immunodeficiency virus", "benign mammary dysplasia"]
---

# Tinidazole
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

## Tinidazole: 원충·혐기성균 감염에서 폐경 후 위축성 질염으로
{: .text-alpha }

## 한 문장 요약

Tinidazole은 5-니트로이미다졸계 항원충·항균제로, 한국에서 단일제 정제 2건이 허가되어 시판 중입니다.
TxGNN 모델은 **폐경 후 위축성 질염(postmenopausal atrophic vaginitis)**에 효과가 있을 수 있다고 예측하지만, 이 적응증을 직접 지지하는 **임상시험은 0건, 문헌도 0편**입니다.
따라서 현재는 모델 예측만 있는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 1. 트리코모나스증 2. 혐기성균 감염증 3. 아메바증 4. 람블편모충증 5. 비특이성 질염 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/197800390/EE)) |
| 예측 신규 적응증 | 폐경 후 위축성 질염 (postmenopausal atrophic vaginitis) |
| TxGNN 예측 점수 | 0.9993 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 2건 / 전체 3건) |
| 허가증 수 | 3건 (유효 2건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Tinidazole 처방 정보(Prescribing Information)의 “Mechanism of Action” 및 “Microbiology” 항목에 따르면(비공식 번역): “티니다졸은 항원충제이자 항균제이다.. […] 티니다졸은 항원충제이자 항균제이다. 티니다졸의 니트로기는 트리코모나스(Trichomonas)의 세포 추출물에 의해 환원된다. 이 환원의 결과로 생성된 유리 니트로 라디칼이 항원충 활성의 원인일 수 있다.” 영어 원문: "Tinidazole is an antiprotozoal, antibacterial agent.. […] Tinidazole is an antiprotozoal, antibacterial agent. The nitro- group of tinidazole is reduced by cell extracts of Trichomonas. The free nitro radical generated as a result of this reduction may be responsible for the antiprotozoal activity." ([DailyMed: Tindazole (tinidazole) prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=45fa3ebd-52da-4987-82a1-4a64f99785a7), 버전 2026-08-18; 확인일 2026-11-19). 알려진 정보에 따르면 Tinidazole은 혐기성균과 질편모충(*Trichomonas vaginalis*)에 활성이 있는 5-니트로이미다졸계 약물입니다.

위축성 질염은 감염이 아니라 에스트로겐 결핍이 원인이므로, 직접적인 기전 연관성은 확립되어 있지 않습니다. 높은 예측 점수는 치료적 근거라기보다 질 감염 질환과의 네트워크상 근접성을 반영했을 가능성이 큽니다.

참고로 예측 순위 2~10위(외음부 궤양, 외음부 종양, 유방 섬유낭성 질환, AIDS 등)도 모두 근거가 매우 제한적입니다. 그중 AIDS는 HIV 자체가 아니라 동반 원충 감염 관리라는 간접적 연관만 확인됩니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 197800390 | 티니다진정500밀리그램(티니다졸) | 노란색의 타원형 필름코팅정 | 신일제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/197800390/EE) | 유효 |
| 197400345 | 티니다진정(티니다졸) | 노란색의 원형 필름코팅정 | 신일제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/197400345/EE) | 유효 |

위 표는 허가 3건 중 2건입니다.

<!-- licenses:end -->

## 안전성 고려사항

- **약물 상호작용**: 현재 100건의 상호작용이 조회되었으며, 표시된 항목은 모두 중등도(Moderate)입니다. 주요 항목은 다음과 같습니다.
  - 항암제: paclitaxel, capecitabine, bortezomib, cabazitaxel, brentuximab vedotin, trastuzumab emtansine
  - 호르몬제: ethinylestradiol, estradiol
  - 기타: ethanol, amiodarone, atorvastatin, levodopa, 바르비투르산계(amobarbital, butalbital)
- **지식그래프상 금기 관련 질환**(허가사항 기재가 아닌 모델 지식그래프 기준): 간질, 호중구감소증, 무과립구증, 말초신경계 질환, 말초신경병증

그 외 경고 및 금기는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 점수는 매우 높지만 임상시험과 문헌이 없고, 위축성 질염의 원인(에스트로겐 결핍)과 Tinidazole의 작용(항원충·항혐기성균)이 맞지 않아 기전적 근거도 약합니다. 허가사항의 경고·금기 정보도 확인되지 않았습니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기) 확보 및 안전성 검토
- 작용 기전 데이터 확보 (DrugBank)
- 위축성 질염에서 Tinidazole의 이점을 뒷받침하는 전임상 또는 임상 근거
- 에스트로겐 요법 등 기존 표준치료 대비 필요성 검토
- 예측 순위 하위 후보(외음부 궤양 등 감염 연관 질환)에 대한 별도 평가 고려

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Tindazole (tinidazole) prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=45fa3ebd-52da-4987-82a1-4a64f99785a7) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

