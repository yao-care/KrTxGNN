---
layout: default
title: Iohexol
parent: 모델 예측만 (L5)
nav_order: 431
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
description: "Iohexol: 예측 신규 적응증 불면증 (Insomnia) (근거 수준 L5). 기존 적응증: 1. 혈관조영 2. 정맥요로조영(IVP) 3. CT 조영증강 4. 체강조영 : 관절조영, 소화관조영 5…"
monitor_inn: "Iohexol"
predicted_indications: ["insomnia (disease)", "anxiety"]
---

# Iohexol
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

## Iohexol: 방사선 조영 진단에서 불면증으로
{: .text-alpha }

## 한 문장 요약

Iohexol은 비이온성 요오드 방사선 조영제로, 원래 영상 진단 목적으로 사용되어 왔습니다.
TxGNN 모델은 **불면증(Insomnia)**에 효과가 있을 수 있다고 예측하지만, 이를 지지하는 **임상시험은 0건**이고 **문헌도 0편**입니다.
이 점수는 TxGNN 모델(딥러닝)에서 나온 것이며, 모델이 관련 질병 간에 학습한 유사성을 반영했을 수 있을 뿐 생물학적 근거는 아닙니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 1. 혈관조영 2. 정맥요로조영(IVP) 3. CT 조영증강 4. 체강조영 : 관절조영, 소화관조영 5. 조영증강 유방촬영술(Contrast-Enhanced Mammography): 알려지거나 의심스러운 유방병변이 있는 환자 중 ᆞ유방촬영술(mammography)(초음파검사 실시… ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200606357/EE)) |
| 예측 신규 적응증 | 불면증 (Insomnia) |
| TxGNN 예측 점수 | 0.9987 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 20건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Iohexol 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “이오헥솔의 요오드 원자는 이오헥솔의 농도에 정비례하여 X선을 감쇠시킨다. 농도는 시간에 따라 변하므로, 이오헥솔은 시간 의존적 영상 대조를 제공하여 신체 구조의 시각화에 도움이 될 수 있다.” 영어 원문: "The iodine atoms in iohexol provide attenuation of X-rays in direct proportion to the concentration of iohexol. Since concentration changes over time, iohexol provides time-dependent image contrast which may assist in visualizing body structures." ([DailyMed: Omnipaque (iohexol) prescribing information, Medical Purchasing Solutions, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=508c42eb-f5e5-44f1-e063-6294a90a4d1f), 버전 2026-04-28; 확인일 2026-11-19). 알려진 정보에 따르면 Iohexol은 비이온성 요오드 조영제로, 약리학적으로 불활성이며 체내에서 대사되지 않고 신장을 통해 변하지 않은 형태로 배설됩니다.

수면 조절 경로(GABA, 오렉신, 멜라토닌 계통)에 대한 알려진 활성이 없어, 기존 용도(영상 진단)와 불면증 사이에 타당한 기전적 연관성을 찾기 어렵습니다. 높은 점수는 TxGNN 모델(딥러닝)에서 나온 것이며, 모델이 관련 질병 간에 학습한 유사성을 반영했을 수 있을 뿐 생물학적 근거는 아닙니다.

## 한국 시판 정보

허가 적응증 본문은 데이터에 포함되어 있지 않아 허가사항 원문을 참조해야 합니다.

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 200606357 | 보노렉스350주(이오헥솔) | 무색투명한 유리 또는 플라스틱(폴리프로필렌, 환형 올레핀 공중합체(COC… | 대한약품공업(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200606357/EE) | 유효 |
| 200102945 | 아이오브릭스주350(이오헥솔) | 무색의 바이알에 들어있는 무색내지 담황색의 맑은 액 | (주)태준제약 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200102945/EE) | 유효 |
| 202103715 | 메디레이350주(이오헥솔) | 무색 내지 미황색의 맑은 용액이 들어있는 무색 투명한 바이알 주사제 | 동국생명과학(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202103715/EE) | 유효 |
| 199202409 | 아이오브릭스주240(이오헥솔) | 무색투명한 바이알에 들어있는 무색에서 미황색의 약간 점조성 있는 액체이다 | (주)태준제약 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199202409/EE) | 유효 |
| 199806679 | 옴니파큐350주(이오헥솔) | 무색투명한 유리 또는 폴리프로필렌 용기에 든 무색 ~ 미황색의 액체 | 지이헬스케어에이에스한국지점 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199806679/EE) | 유효 |

위 표는 허가 최소 20건 중 5건입니다.

<!-- licenses:end -->

위 표는 주요 5건이며, 허가 건수와 상태는 빠른 개요에 있습니다.

<!-- review:begin kr-lic-20261124c-iohexol-1 -->

> **검토 정정 (2026-11-24)**: 원래 문장: “총 20건이 모두 단일제로 유효하며, 위 표는 그중 주요 5건입니다.” 식품의약품안전처 의약품안전나라(nedrug) 허가 자료(2026-11-23 데이터) 기준으로 수정했습니다: 이 사이트 자료의 성분란에는 일치한 성분만 기록되어 허가 품목별 단일 성분·복합 성분 여부를 확인할 수 없으므로, 단일·복합 표기를 빼고 건수는 쓰지 않고 빠른 개요와 「한국 시판 정보」의 표를 가리키도록 고쳤습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261124c-iohexol-1 -->

## 안전성 고려사항

- **약물 상호작용**: 총 100건의 상호작용이 조회되었습니다. 주요 항목 중 Major 등급은 다음과 같습니다.
  - 스테로이드: Hydrocortisone, Dexamethasone, Betamethasone, Triamcinolone
  - 신독성 가능 약물: Amphotericin B(일반 및 지질 복합체), Vancomycin, Kanamycin, Neomycin
  - 기타: Metformin, Bupropion, Mesalazine, Morphine, Levofloxacin, Metoclopamide 등
- 문헌에서 메토트렉세이트 복용 환자에게 반복 투여 후 치명적인 다장기 기능부전이 발생한 사례가 보고되었으며, 조영제 과민반응에 대한 탈감작 사례도 있습니다.

나머지 안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
임상시험과 문헌 근거가 전혀 없고(L5), 불활성 조영제로서 불면증과의 기전적 연관성이 없습니다. 검토 대상인 다른 예측(불safe 불안, 류마티스 관절염, 항트롬빈 결핍, 섬유근육통, 결막염, 건염 등)도 문헌에서 Iohexol이 진단·측정 도구로만 쓰이거나 이상반응 사례로 등장하여 치료 근거가 되지 못합니다.

**진행하려면 필요한 것:**
- 작용 기전(MOA) 데이터 확보
- 허가 적응증 및 경고·금기 등 허가사항 원문 확보
- 불면증에 대한 전임상 또는 임상 근거 (현재는 없음)
- 점수가 TxGNN 모델(딥러닝)이 관련 질병 간에 학습한 유사성을 반영한 것인지 확인하는 추가 검증

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다. 작용 기전 자료가 없다는 문장은 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Omnipaque (iohexol) prescribing information, Medical Purchasing Solutions, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=508c42eb-f5e5-44f1-e063-6294a90a4d1f) |
| 2026-11-24 | 단일·복합 표기: “총 20건이 모두 단일제로 유효하며, 위 표는 그중 주요 5건입니다.” → 확인할 수 없는 단일·복합 표기와 건수 삭제(건수는 빠른 개요와 표) | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

