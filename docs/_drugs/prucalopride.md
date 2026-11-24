---
layout: default
title: Prucalopride
parent: 모델 예측만 (L5)
nav_order: 638
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Prucalopride: 예측 신규 적응증 저알파지단백혈증 (Hypoalphalipoproteinemia) (근거 수준 L5). 기존 적응증: 허가 적응증 본문은 이번 데이터에 포함되어 있지 않습니다. 장 운동 촉진제(5-HT4 작용제)로 알려져 있습니다"
monitor_inn: "Prucalopride"
predicted_indications: ["hypoalphalipoproteinemia", "homozygous familial hypercholesterolemia", "duodenal ulcer (disease)", "oral candidiasis", "obsolete familial combined hyperlipidemia", "amyloidosis (disease)", "strongyloidiasis", "HIV infectious disease", "primary amyloidosis", "acquired amyloid peripheral neuropathy"]
---

# Prucalopride
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

## Prucalopride: 만성 변비에서 저알파지단백혈증으로
{: .text-alpha }

## 한 문장 요약

Prucalopride는 선택적 5-HT4 수용체 작용제로, 장 운동을 촉진하는 약물입니다.
TxGNN 모델은 **저알파지단백혈증(Hypoalphalipoproteinemia)**에 효과가 있을 수 있다고 예측하지만, 이를 지지하는 **임상시험은 0건, 문헌도 0편**입니다.
기전상 뚜렷한 연관성이 확인되지 않아 모델 예측만 존재하는 상태입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문은 이번 데이터에 포함되어 있지 않습니다. 장 운동 촉진제(5-HT4 작용제)로 알려져 있습니다. |
| 예측 신규 적응증 | 저알파지단백혈증 (Hypoalphalipoproteinemia) |
| TxGNN 예측 점수 | 0.9982 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 18건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Prucalopride 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “선택적 세로토닌 4형(5-HT 4 ) 수용체 작용제인 프루칼로프라이드는 결장 연동운동(고진폭 전파성 수축[HAPCs])을 자극하여 장 운동성을 증가시키는 위장관(GI) 운동촉진제이다. 프루칼로프라이드는 in vitro에서 5-HT 4 수용체 친화도를 150배 이상 초과하는 농도에서도 5-HT 2A, 5-HT 2B, 5-HT 3, 모틸린 또는 CCK-A 수용체를 매개로 한 효과를 나타내지 않았다.” 영어 원문: "Prucalopride, a selective serotonin type 4 (5-HT 4 ) receptor agonist, is a gastrointestinal (GI) prokinetic agent that stimulates colonic peristalsis (high-amplitude propagating contractions [HAPCs]), which increases bowel motility. Prucalopride was devoid of effects mediated via 5-HT 2A, 5-HT 2B, 5-HT 3, motilin or CCK-A receptors in vitro at concentrations exceeding 5-HT 4 receptor affinity by 150-fold or greater." ([DailyMed: Motegrity (prucalopride) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=bca1e4c6-4b2b-4876-8ab3-654629c4ff1b), 버전 2025-07-17; 확인일 2026-11-19). 다만 알려진 정보에 따르면 Prucalopride는 선택적 5-HT4 수용체 작용제로서 소화관 운동을 촉진합니다.

저알파지단백혈증은 HDL 콜레스테롤이 낮은 지질대사 이상입니다. 5-HT4 작용과 HDL 대사 또는 지단백 조절 사이에 알려진 연관성은 없습니다. 따라서 높은 TxGNN 점수는 TxGNN 모델(딥러닝)이 관련 질환 사이에서 학습한 유사성을 반영한 것일 뿐, 생물학적 근거는 아니며 임상적·문헌적 뒷받침도 없습니다.

참고로 다른 상위 예측 중 **아밀로이드증(amyloidosis)**과 **일차성 아밀로이드증**은 아밀로이드 침착 자체가 아니라 동반되는 위장관 운동장애(만성 가성장폐색, 변비)에 대한 증상 완화 가설로서 간접적 타당성이 있습니다. 이들은 근거 수준 L4(연구 질문 단계)로 평가되었으나, Prucalopride 효능을 직접 검증한 연구는 아닙니다.

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 201900673 | 루칼로정1밀리그램(프루칼로프라이드숙신산염) | 흰색의 원형 필름코팅정 | (주)유영제약 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201900673/EE) | 유효 |
| 201902573 | 모티움정1밀리그램(프루칼로프라이드숙신산염) | 흰색의 원형 필름코팅정 | (주)유유제약 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201902573/EE) | 유효 |
| 201900756 | 프롤로정2밀리그램(프루칼로프라이드숙신산염) | 분홍색의 원형 필름코팅정 | 하나제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201900756/EE) | 유효 |
| 201207465 | 레졸로정2밀리그램(프루칼로프라이드숙신산염) | 분홍색의 원형 필름코팅정제 | 한국메나리니(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201207465/EE) | 유효 |
| 201207464 | 레졸로정1밀리그램(프루칼로프라이드숙신산염) | 흰색 내지 미백색의 원형 필름코팅정제 | 한국메나리니(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201207464/EE) | 유효 |

위 표는 허가 최소 20건 중 5건입니다.

<!-- licenses:end -->

총 18건의 유효 단일제 허가가 있으며 위에는 5건만 나열했습니다.

## 안전성 고려사항

- **약물 상호작용**: 총 98건이 확인되었습니다. 이 중 주요 항목은 다음과 같습니다.
  - 중등도: 항콜린제 계열(Aclidinium, Atropine, Benzatropine, Biperiden, Clidinium, Glycopyrronium, Hyoscyamine), 호르몬제(Levonorgestrel, Norethisterone, Ethinylestradiol)
  - 경미: Nifedipine, Afatinib, Alpelisib, Amiodarone, Cobicistat, Captopril, Diltiazem, Spironolactone, Carvedilol, Conivaptan
- **지식 그래프상 금기 관련 질환**: 궤양성 대장염, 염증성 장질환, 장천공 (허가 문서 기반이 아닌 지식 그래프 정보이므로 허가사항 확인이 필요합니다.)

주요 경고와 금기 등 그 밖의 안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
저알파지단백혈증 예측은 임상시험과 문헌이 전혀 없고 기전상 연관성도 확인되지 않아 모델 예측에 그칩니다. 차순위 예측(가족성 고콜레스테롤혈증, 십이지장궤양, 구강 칸디다증 등)도 마찬가지로 근거가 없습니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기) 확보 및 분석 (안전성 선별의 선행 조건)
- 상세한 작용 기전(MOA) 데이터 확보
- 지질대사와 5-HT4 경로의 연관성을 뒷받침하는 전임상 또는 기전 연구
- 대안으로, 아밀로이드증 동반 위장관 운동장애에 대한 증상 완화 가설을 별도 연구 질문으로 검토

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Motegrity (prucalopride) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=bca1e4c6-4b2b-4876-8ab3-654629c4ff1b) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

