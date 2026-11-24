---
layout: default
title: Etodolac
parent: 모델 예측만 (L5)
nav_order: 327
evidence_level: L5
indication_count: 6
monitor_inn: "Etodolac"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "hypermobility of coccyx"]
last_modified_at: 2026-11-24
description: "Etodolac: 예측 신규 적응증 말단중간이형성증 Hunter-Thompson형 (근거 수준 L5). 기존 적응증: 1. 다음 질환에 사용할 수 있다. 류마티양 관절염, 골관절염(퇴행성 관절질환), 강직성 척추염…"
---

# Etodolac
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **6** 건
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

## Etodolac: 기존 적응증 정보 부재에서 말단중간이형성증 헌터-톰슨형으로
{: .text-alpha }

## 한 문장 요약

Etodolac은 COX-2 선호성 비스테로이드 소염진통제(NSAID)이며, 한국에서 단일 성분 제제로 허가되어 있습니다. 다만 이 보고서에 사용된 데이터에는 허가 적응증의 본문이 없습니다.
TxGNN 모델은 **말단중간이형성증 Hunter-Thompson형(acromesomelic dysplasia, Hunter-Thompson type)**에 효과가 있을 수 있다고 예측합니다. 그러나 이를 직접 뒷받침하는 **임상시험은 0건, 문헌도 0편**이어서 모델 예측만 있는 상태입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 1. 다음 질환에 사용할 수 있다. 류마티양 관절염, 골관절염(퇴행성 관절질환), 강직성 척추염, . . 수술후 외상후 발치후 동통 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199002184/EE)) |
| 예측 신규 적응증 | 말단중간이형성증 Hunter-Thompson형 |
| TxGNN 예측 점수 | 0.9997 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 10건 / 전체 10건) |
| 허가증 수 | 10건 (유효 10건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Etodolac 처방 정보(Prescribing Information)의 “Clinical Pharmacology” 항목에 따르면(비공식 번역): “에토돌락 서방정의 작용기전은 다른 NSAID와 마찬가지로 완전히 규명되지 않았으나, 프로스타글란딘 합성효소 억제와 관련이 있을 수 있다.” 영어 원문: "The mechanism of action of etodolac extended-release tablets, like that of other NSAIDs, is not completely understood, but may be related to prostaglandin synthetase inhibition." ([DailyMed: Etodolac Er (etodolac) prescribing information, Advanced Rx Pharmacy of Tennessee, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=baebdfb2-17f6-9081-e053-2a95a90ab331), 버전 2024-12-31; 확인일 2026-11-19). 일반적으로 Etodolac은 COX-2 선호성 NSAID로 프로스타글란딘 합성을 줄여 염증과 통증을 완화하는 약물로 알려져 있습니다.

Hunter-Thompson형 말단중간이형성증은 GDF5(BMP 신호전달) 기능상실 변이로 생기는 희귀 골격 이형성증입니다. Etodolac은 GDF5/BMP 경로에 작용하는 것으로 알려져 있지 않아, 확립된 기전적 연결고리가 없습니다.

TxGNN 점수는 TxGNN 모델(딥러닝)이 산출한 값으로, 모델이 관련 질환 사이에서 학습한 유사성을 반영했을 가능성이 있으며 생물학적 근거는 아닙니다. NSAID가 이차적인 관절 통증을 완화할 수는 있지만, 이는 증상 완화일 뿐 질병 경과를 바꾸는 효과는 아닙니다.

같은 분석에서 예측된 다른 후보(점수순)는 다음과 같으며, 모두 L5이고 Hold입니다.

| 순위 | 질환 | TxGNN 점수 | 비고 |
|------|------|-----------|------|
| 2 | 단신증-법랑질형성부전 증후군 (brachyolmia-amelogenesis imperfecta syndrome) | 0.9997 | 확립된 기전 없음 |
| 3 | 근경화증 (myosclerosis) | 0.9997 | 기전 연결이 약하고 추측에 가까움 |
| 4 | 단신증 (brachyolmia) | 0.9996 | 확립된 기전 없음 |
| 5 | 가성연골무형성증 (pseudoachondroplasia) | 0.9993 | 증상 완화 수준의 간접 연결만 가능 |
| 6 | 미골 과운동성 (hypermobility of coccyx) | 0.9987 | 통증 완화 목적으로만 임상적 개연성이 있음 |

## 한국 시판 정보

허가 적응증 본문은 확인되지 않았고 허가 문서 링크만 있어, 적응증 열은 생략했습니다. 허가 건수와 상태는 빠른 개요와 아래 표에 있습니다.

<!-- review:begin kr-lic-20261124c-etodolac-1 -->

> **검토 정정 (2026-11-24)**: 원래 문장: “아래 10건은 모두 단일 성분 제제이며 상태는 유효입니다.” 식품의약품안전처 의약품안전나라(nedrug) 허가 자료(2026-11-23 데이터) 기준으로 수정했습니다: 이 사이트 자료의 성분란에는 일치한 성분만 기록되어 허가 품목별 단일 성분·복합 성분 여부를 확인할 수 없으므로, 단일·복합 표기를 빼고 건수는 쓰지 않고 빠른 개요와 「한국 시판 정보」의 표를 가리키도록 고쳤습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261124c-etodolac-1 -->

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 199002184 | 아신돌캡슐200밀리그램(에토돌락)(수출용) | 백색 내지 유백색의 분말이 충진된 상,하부 청색의 경질캡슐제 | 케이엠에스제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199002184/EE) | 유효 |
| 201401037 | 엔터락캡슐(에토돌락 )(수출용)(수출명 : Enterlac cap.) | 흰색 내지 유백색의 분말이 충진된 상하부 청색의 경질캡슐 | (주)마더스제약 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201401037/EE) | 유효 |
| 199400681 | 마카나캡슐(에토돌락)(수출용)(수출명:SEODOECapsules) | 백색-미황색의 내용물이 든 상 엷은 회색, 하 짙은 회색의 경질캅셀제 | (주)일화 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199400681/EE) | 유효 |
| 201405864 | 엘토스캡슐(에토돌락)(수출용) | 백색 내지 유백색의 분말이 충진된 상부 자색, 하부 담황색의 경질캡슐제 | 한국프라임제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201405864/EE) | 유효 |
| 199302406 | 파비스에토돌락캅셀(수출용)(수출명 : SOTOLAC , M-PRO ) | 백색-미황색의 내용물이 든 상 엷은 회색, 하 짙은 회색의 경질캅셀제 | (주)한국파비스제약 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199302406/EE) | 유효 |

위 표는 허가 10건 중 5건입니다.

<!-- licenses:end -->

위 표는 주요 5건만 나열한 것이며, 나머지 5건(코즈민캡슐, 에토락캡슐, 에토딘캡슐, 페노딘캡슐, 대우에토돌락캅셀)도 유효 허가입니다. 이 중 에토딘캡슐과 대우에토돌락캅셀은 제품명상 수출용 표기가 없습니다. 모든 제품의 제형은 경질캡슐입니다.

## 안전성 고려사항

허가사항의 경고 및 금기 정보는 이번 데이터에 없으므로 허가사항을 참조하세요.

**약물 상호작용** (DDInter 기준, 조회된 100건 중 일부):
- **중등도**: Acetylsalicylic acid, Hydrocortisone, Dexamethasone, Betamethasone, Budesonide, Triamcinolone, Metformin, Glimepiride, Repaglinide, Chlorpropamide, Mesalazine, Balsalazide, Potassium citrate, Potassium bicarbonate, Picosulfuric acid, Polyethylene glycol (전해질 함유 3350)
- **경미**: Famotidine, Ranitidine, Cimetidine, Linaclotide

## 결론 및 다음 단계

**결정: Hold**

**사유:**
6개 예측 후보 모두 직접 뒷받침하는 임상시험과 문헌이 없고, Etodolac의 기전과 연결되는 근거도 없습니다. 높은 점수는 TxGNN 모델(딥러닝)이 산출한 값일 뿐이며, 모델이 관련 질환 사이에서 학습한 유사성을 반영했을 가능성이 있고 생물학적 근거는 아닙니다. 허가 적응증과 안전성 정보도 확인되지 않았습니다.

**진행하려면 필요한 것:**
- 식약처 허가 문서에서 적응증, 경고, 금기 정보 확보 (현재 차단 수준의 데이터 공백)
- DrugBank 등에서 작용 기전(MOA) 확보
- 예측 질환별 임상시험 및 문헌 재검색
- 증상 완화 목적의 활용 가능성이 상대적으로 높은 미골 과운동성부터 우선 검토

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다. 작용 기전 자료가 없다는 문장은 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Etodolac Er (etodolac) prescribing information, Advanced Rx Pharmacy of Tennessee, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=baebdfb2-17f6-9081-e053-2a95a90ab331) |
| 2026-11-24 | 단일·복합 표기: “아래 10건은 모두 단일 성분 제제이며 상태는 유효입니다.” → 확인할 수 없는 단일·복합 표기와 건수 삭제(건수는 빠른 개요와 표) | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

