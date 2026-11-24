---
layout: default
title: Levetiracetam
parent: 모델 예측만 (L5)
nav_order: 471
evidence_level: L5
indication_count: 1
monitor_inn: "LEVETIRACETAM"
predicted_indications: ["beta-ketothiolase deficiency"]
last_modified_at: 2026-11-24
description: "Levetiracetam: 예측 신규 적응증 베타-케토티올라제 결핍증 (beta-ketothiolase deficiency) (근거 수준 L5). 기존 적응증: 1. 단독요법 : 처음 뇌전증으로 진단된 2차성 전신발작을 동반하거나 동반하지 않는 부분발작의 치료(12세…"
---

# Levetiracetam
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

## Levetiracetam: SV2A 결합 항경련제 → 베타-케토티올라제 결핍증 (beta-ketothiolase deficiency)
{: .text-alpha }

## 한 문장 요약

Levetiracetam은 SV2A(시냅스 소포 단백질 2A)에 작용하는 항경련제 계열의 약물입니다.
TxGNN 모델은 **베타-케토티올라제 결핍증(beta-ketothiolase deficiency)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 직접 뒷받침하는 **임상시험은 0건**, **문헌도 0편**입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 1. 단독요법 : 처음 뇌전증으로 진단된 2차성 전신발작을 동반하거나 동반하지 않는 부분발작의 치료(12세 이상) 2. 부가요법 : 기존 1차 뇌전증치료제 투여로 적절하게 조절이 되지 않는 2차성 전신발작을 동반하거나 동반하지 않는 부분발작의 치료(12세 이상) ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201805181/EE)) |
| 예측 신규 적응증 | 베타-케토티올라제 결핍증 (beta-ketothiolase deficiency) |
| TxGNN 예측 점수 | 0.9990 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 20건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Levetiracetam 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “레베티라세탐이 항뇌전증 효과를 나타내는 정확한 기전은 알려져 있지 않다. 랫드 뇌 조직에서 레베티라세탐에 대한 포화성 및 입체선택적 신경세포 결합 부위가 보고되었다. 실험 자료에 따르면 이 결합 부위는 소포 세포외유출의 조절에 관여하는 것으로 생각되는 시냅스 소포 단백질 SV2A이다.” 영어 원문: "The precise mechanism(s) by which levetiracetam exerts its antiepileptic effect is unknown. A saturable and stereoselective neuronal binding site in rat brain tissue has been described for levetiracetam. Experimental data indicate that this binding site is the synaptic vesicle protein SV2A, thought to be involved in the regulation of vesicle exocytosis." ([DailyMed: Keppra (levetiracetam) prescribing information, UCB, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c6d5784d-abf9-45fe-ac5a-d5c53bd50f7e), 버전 2026-11-11; 확인일 2026-11-19). 일반적으로 알려진 바로는 levetiracetam은 SV2A에 결합하여 신경 전달물질 방출을 조절하는 약물입니다.

베타-케토티올라제 결핍증은 케톤체 및 이소류신 대사 경로의 선천성 대사 질환입니다. Levetiracetam의 SV2A 기전과 이 대사 경로 사이에는 뚜렷한 연결 고리가 확인되지 않습니다.

따라서 이 예측은 계산 모델의 결과일 뿐이며, 기전상 타당성을 뒷받침하는 임상시험이나 문헌 근거는 현재 없습니다.

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 201805181 | 큐팜엑스알서방정500밀리그램(레비티라세탐) | 흰색의 장방형 서방성 필름코팅정 | 명인제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201805181/EE) | 유효 |
| 201301649 | 원프라정250밀리그램(레비티라세탐) | 파란색의 타원형 필름코팅정 | 코스맥스파마(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201301649/EE) | 유효 |
| 201908013 | 케파베아정250밀리그램(레비티라세탐) | 파란색의 타원형 필름코팅정 | 대웅바이오(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201908013/EE) | 유효 |
| 201605338 | 레비티람주500mg(레비티라세탐) | 무색의 투명한 용액이 무색 투명한 수액용 플라스틱 용기에 충전된 주사제 | 제이더블유생명과학(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201605338/EE) | 유효 |
| 201605863 | 케프라엑스알서방정750밀리그램(레비티라세탐) | 흰색의 장방형 서방성 필름코팅정제 | 한국유씨비제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201605863/EE) | 유효 |

위 표는 허가 최소 20건 중 5건입니다.

<!-- licenses:end -->

위 표는 전체 허가 중 일부이며, 목록이 부분적일 수 있습니다.

## 안전성 고려사항

**약물 상호작용** (총 100건 조회, 주요 항목):
- 중등도: Morphine, Dronabinol, Metoclopramide, Morphine(리포좀), Nabilone, Opium, Sibutramine
- 등급 미확인: Calcitriol, Pantoprazole, Glimepiride, Mesalazine, Doxycycline, Metformin, Omeprazole 등

그 외 경고 및 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 점수는 높지만 임상시험과 문헌이 모두 없고, SV2A 기전과 케톤체·이소류신 대사 질환 사이의 연결도 확인되지 않아 근거 수준이 L5에 머뭅니다.

**진행하려면 필요한 것:**
- 작용 기전(MOA) 데이터 보완 및 대사 경로와의 기전적 연관성 분석
- 베타-케토티올라제 결핍증 관련 전임상 연구 또는 문헌 검토
- 허가사항(경고·금기)의 확인 및 안전성 검토

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Keppra (levetiracetam) prescribing information, UCB, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c6d5784d-abf9-45fe-ac5a-d5c53bd50f7e) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

