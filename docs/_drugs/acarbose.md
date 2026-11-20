---
layout: default
title: Acarbose
parent: 모델 예측만 (L5)
nav_order: 16
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-20
description: "Acarbose: 예측 신규 적응증 classic stiff person syndrome (전형적 강직인간증후군) (근거 수준 L5). 기존 적응증: 당뇨병의 식후 고혈당개선(단, 식사요법, 운동요법을 행하고 있는 환자에서 충분한 효과를 얻을 수 없는…"
monitor_inn: "ACARBOSE"
predicted_indications: ["classic stiff person syndrome", "focal stiff limb syndrome", "thiamine-responsive dysfunction syndrome", "opsismodysplasia", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis"]
---

# Acarbose
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

## Acarbose: 제2형 당뇨병에서 classic stiff person syndrome으로
{: .text-alpha }

## 한 문장 요약

Acarbose는 알파-글루코시다제 억제제로, 한국에서 혈당 조절(당뇨병 치료) 목적으로 허가되어 시판 중인 약입니다. TxGNN 모델은 **classic stiff person syndrome(전형적 강직인간증후군)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 직접 지지하는 **임상시험은 0건, 문헌도 0편**입니다. 이 예측은 모델 계산 결과일 뿐이며 실제 근거는 없습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 당뇨병의 식후 고혈당개선(단, 식사요법, 운동요법을 행하고 있는 환자에서 충분한 효과를 얻을 수 없는 경우, 또는 식사요법, 운동요법에 추가하여 경구혈당강하제 또는 인슐린 제제를 사용하고 있는 환자에서 충분한 효과를 얻을 수 없는 경우에 한함.) ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199900925/EE)) |
| 예측 신규 적응증 | classic stiff person syndrome (전형적 강직인간증후군) |
| TxGNN 예측 점수 | 0.9965 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 2건 / 전체 2건) |
| 허가증 수 | 2건 (유효 2건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Acarbose 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “설포닐우레아와 달리, Acarbose Tablets는 인슐린 분비를 증가시키지 않는다. 아카르보스의 항고혈당 작용은 췌장 알파-아밀라아제 및 막결합 장 알파-글루코시드 가수분해효소의 경쟁적·가역적 저해에 의한 것이다.” 영어 원문: "In contrast to sulfonylureas, Acarbose Tablets do not enhance insulin secretion. The antihyperglycemic action of acarbose results from a competitive, reversible inhibition of pancreatic alpha-amylase and membrane-bound intestinal alpha-glucoside hydrolase enzymes." ([DailyMed: acarbose prescribing information, Bryant Ranch Prepack](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1ba7a072-03b0-41f2-be7a-101145bdef3a), 버전 2026-08-11; 확인일 2026-11-19). 알려진 정보에 따르면 Acarbose는 장에서 탄수화물 소화·흡수를 늦춰 식후 혈당 상승을 완화하는 알파-글루코시다제 억제제입니다.

반면 강직인간증후군은 항-GAD65 항체 등과 관련된 자가면역성 질환으로, GABA 신경전달 이상이 핵심입니다. 두 질환 사이에 뚜렷한 기전적 연결고리는 확인되지 않습니다. 유일하게 생각해 볼 수 있는 접점은 자가면역성 당뇨병이 흔히 동반된다는 점인데, 이는 Acarbose의 치료적 역할을 뒷받침하지 않습니다.

따라서 높은 예측 점수는 TxGNN 모델(딥러닝)에서 나온 것으로, 모델이 관련 질환 간에 학습한 유사성을 반영할 수 있으며, 생물학적 근거나 임상적 타당성을 입증하는 것은 아닙니다.

같은 맥락에서 다른 상위 예측들도 근거가 없습니다.

| 순위 | 예측 질환 | TxGNN 점수 | 근거 수준 | 비고 |
|-----|---------|-----------|---------|------|
| 2 | focal stiff limb syndrome | 0.9965 | L5 | 기전적 연결 없음 |
| 3 | thiamine-responsive dysfunction syndrome | 0.9962 | L5 | 동반 당뇨병 표현형에 의한 간접 연관 가능성 |
| 4 | opsismodysplasia | 0.9962 | L5 | 기전적 연결 없음 |
| 5 | drug-induced localized lipodystrophy | 0.9924 | L5 | 약한 간접 대사 연관 |
| 9 | pancreatic agenesis | 0.9916 | L5 | 문헌 11편이 있으나 해당 질환을 직접 다루지 않음 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 199900925 | 글루코바이정50밀리그람(아카보즈) | 흰색 또는 연한 노란색의 원형정제 | 허가사항 링크 참조 ([MFDS](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199900925/EE)) |
| 199900924 | 글루코바이정100밀리그람(아카보즈) | 흰색 또는 연한 노란색의 원형정제 | 허가사항 링크 참조 ([MFDS](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199900924/EE)) |

두 제품 모두 (주)한독이 제조하는 단일제이며 유효 상태입니다.

## 안전성 고려사항

- **지식그래프 기반 금기 관련 질환** (허가사항이 아닌 TxGNN 지식그래프의 약물-질환 금기 연결 기준): 신장 질환, 화농성 요관(pyoureter), 간 질환, 담낭 질환, 간경변, 염증성 장질환, 저혈당, 손상
- **약물 상호작용**: 조회된 상호작용은 총 100건이며, 이 중 일부를 예시로 들면 다음과 같습니다.
  - 중등도: Acetazolamide, Salbutamol, Aloe Vera Leaf, Alpelisib, Amprenavir, Aripiprazole, Asenapine, Atazanavir, Bedaquiline, Bendroflumethiazide, Betamethasone 등
  - 경미: Albiglutide, Alclometasone(국소), Lipoic acid, Amcinonide, Anisindione 등

허가사항의 경고·금기 문구는 이번 자료에서 확인되지 않았으므로 허가사항을 직접 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 점수는 매우 높지만(0.9965) 임상시험과 문헌이 전혀 없고 기전적 연결도 확인되지 않아 근거 수준이 L5입니다. 현재로서는 재창출 후보로 진행할 근거가 부족합니다.

**진행하려면 필요한 것:**
- 작용 기전(MOA) 데이터 확보 및 강직인간증후군과의 기전적 연관성 재검토
- 허가사항(MFDS 첨부문서)의 경고·금기·적응증 문구 확보
- 강직인간증후군 관련 전임상 또는 임상 문헌 탐색
- 다른 상위 예측(예: 당뇨 관련 표현형 질환)에 대한 별도 타당성 검토

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: acarbose prescribing information, Bryant Ranch Prepack](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1ba7a072-03b0-41f2-be7a-101145bdef3a) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

