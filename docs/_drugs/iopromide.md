---
layout: default
title: Iopromide
parent: 모델 예측만 (L5)
nav_order: 432
evidence_level: L5
indication_count: 9
monitor_inn: "Iopromide"
predicted_indications: ["osteoarthritis", "rheumatoid arthritis", "brachyolmia", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "alopecia", "myosclerosis", "hemoglobinopathy", "pseudoachondroplasia"]
last_modified_at: 2026-11-24
description: "Iopromide: 예측 신규 적응증 골관절염 (osteoarthritis) (근거 수준 L5). 기존 적응증: 1. 정맥요로조영(IVP) 2. CT 조영증강 : 두부, 체부 3. 혈관조영 4. 디지털감산혈관조영(DSA)"
---

# Iopromide
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

## Iopromide: 골관절염 (osteoarthritis)
{: .text-alpha }

## 한 문장 요약

Iopromide는 요오드화 비이온성 방사선 조영제로, 한국에서 주사제 형태로 허가되어 있습니다. TxGNN 모델은 **골관절염(osteoarthritis)**에 효과가 있을 수 있다고 예측하지만, 이 방향을 지지하는 **임상시험은 0건**, **문헌도 0편**입니다. 따라서 이 예측은 모델 점수에만 의존하며 근거 수준은 L5입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 1. 정맥요로조영(IVP) 2. CT 조영증강 : 두부, 체부 3. 혈관조영 4. 디지털감산혈관조영(DSA) ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201400622/EE)) |
| 예측 신규 적응증 | 골관절염 (osteoarthritis) |
| TxGNN 예측 점수 | 0.9953 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 5건 / 전체 5건) |
| 허가증 수 | 5건 (유효 5건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Iopromide 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “이오프로마이드의 혈관 내 주사는 조영제가 존재하는 혈관을 불투명하게 하여, 광자 감쇠를 통해 내부 구조의 방사선학적 시각화를 가능하게 한다. 신체 영상 촬영에서 요오드화 조영제는 혈관에서 혈관외 공간으로 확산된다.” 영어 원문: "Intravascular injection of iopromide opacifies those vessels where the contrast agent is present, permitting radiographic visualization of the internal structures through attenuation of photons. In imaging of the body, iodinated contrast agents diffuse from the vessels into the extravascular space." ([DailyMed: Ultravist (iopromide) prescribing information, Bayer HealthCare Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=df917c3a-59a2-4ed1-8470-8a5394c73325), 버전 2026-03-02; 확인일 2026-11-19). Iopromide는 요오드화 비이온성 방사선 조영제로, 항염증 작용이나 연골 보호 작용이 알려져 있지 않습니다. 관절 조영술에 쓰일 수 있으나 이는 진단 목적이며 치료 효과가 아닙니다.

TxGNN 점수(0.9953)는 TxGNN 모델(딥러닝)에서 나온 값이며, 관련 질환 간에 모델이 학습한 유사성을 반영할 수 있을 뿐 생물학적 근거는 아닙니다. 기전적 연결고리는 확인되지 않았으며, 이를 뒷받침하는 임상시험이나 문헌도 없습니다.

참고로 같은 약물에 대해 류마티스 관절염(0.9937), 알로페시아(탈모, 0.9911), 헤모글로빈병증(0.9908), 가성연골무형성증(0.9906) 등 여러 질환이 예측되었습니다. 이들 역시 모두 L5이며 Hold 판정입니다. 이 중 일부는 희귀 유전성 골격 이형성증으로, 조영제의 약리와 연결되지 않습니다. 헤모글로빈병증의 경우 일부 혈액 질환(예: 겸상적혈구병)에서 조영제의 삼투압 영향으로 오히려 안전성 우려가 있을 수 있어, 치료 사용에 불리합니다.

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 201400622 | 레이프로주370(이오프로마이드)(수출용) | 무색투명한 주사액이 충진되어 있는 무색투명한 병 또는 바이알 | 일성아이에스(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201400622/EE) | 유효 |
| 201802934 | 울트라비스트300주프리필드카트리지(이오프로마이드) | 아주 연한갈색~아주 연한노란색의 투명한 액이 무색의 플라스틱카트리지에 든… | 바이엘코리아(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201802934/EE) | 유효 |
| 201804420 | 울트라비스트듀300주사(이오프로마이드) | 아주 연한갈색 - 아주 연한노란색의 투명한 액이 무색의 유리병 또는 유리… | 바이엘코리아(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201804420/EE) | 유효 |
| 201804419 | 울트라비스트듀370주사(이오프로마이드) | 아주 연한갈색 - 아주 연한노란색의 투명한 액이 무색의 유리병 또는 유리… | 바이엘코리아(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201804419/EE) | 유효 |
| 201400621 | 레이프로주300(이오프로마이드)(수출용) | 무색투명한 주사액이 충진되어 있는 무색투명한 병 또는 바이알 | 일성아이에스(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201400621/EE) | 유효 |

<!-- licenses:end -->

허가 건수와 상태는 빠른 개요와 위 표에 있습니다.

<!-- review:begin kr-lic-20261124c-iopromide-1 -->

> **검토 정정 (2026-11-24)**: 원래 문장: “모두 단일 성분 제품이며 유효한 허가입니다.” 식품의약품안전처 의약품안전나라(nedrug) 허가 자료(2026-11-23 데이터) 기준으로 수정했습니다: 단일·복합 표기와 건수를 본문에 고정해 쓰지 않고, 매주 갱신되는 허가 자료를 반영하는 빠른 개요와 「한국 시판 정보」의 표를 가리키도록 고쳤습니다. 2026-11-25에 식품의약품안전처 품목허가 상세 자료(2026-03)의 주성분명으로 품목별로 다시 확인한 결과, 이 자료에 수록된 허가 품목은 모두 단일 성분 제제입니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261124c-iopromide-1 -->

## 안전성 고려사항

- **약물 상호작용**: 데이터에서 총 100건이 확인되었으며, 이 중 일부를 나열합니다.
  - 주요(Major) 등급: 메트포르민, 암포테리신 B(지질 복합체, 콜레스테릴 설페이트, 리포좀 제형 포함), 메살라진, 발살라자이드, 올살라진, 설파살라진, 반코마이신, 카나마이신, 네오마이신, 스트렙토마이신, 폴리믹신 B
  - 보통(Moderate) 등급: 만니톨
  - 등급 미상: 클로트리마졸, 아세틸살리실산, 부프로피온, 덱사메타손, 판토프라졸

허가사항의 경고 및 금기 정보는 이번 데이터에 포함되어 있지 않으므로, 상세 내용은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
골관절염에 대한 임상시험과 문헌이 전혀 없고, 약리학적 기전상으로도 연결고리가 없습니다. 높은 TxGNN 점수는 TxGNN 모델(딥러닝)이 관련 질환 간에 학습한 유사성을 반영할 수 있을 뿐 생물학적 근거는 아니며, 이것만으로 진행할 수 없습니다.

**진행하려면 필요한 것:**
- 허가사항의 경고 및 금기 정보 확보 (한국 MFDS 허가사항 PDF 분석)
- 작용 기전(MOA) 데이터 확보 (DrugBank 조회)
- 골관절염과 Iopromide의 연관성을 보여주는 전임상 또는 임상 연구
- 치료 목적의 투여 경로 및 용량 타당성 검토

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다. 작용 기전 자료가 없다는 문장은 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Ultravist (iopromide) prescribing information, Bayer HealthCare Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=df917c3a-59a2-4ed1-8470-8a5394c73325) |
| 2026-11-24 | 단일·복합 표기: “모두 단일 성분 제품이며 유효한 허가입니다.” → 고정된 단일·복합 표기와 건수 삭제(건수는 빠른 개요와 표) | 정정 (2026-11-25 수정, 이전 판은 기록에 보존) | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

