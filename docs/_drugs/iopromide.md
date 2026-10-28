---
layout: default
title: Iopromide
parent: 모델 예측만 (L5)
nav_order: 432
evidence_level: L5
indication_count: 9
monitor_inn: "Iopromide"
predicted_indications: ["osteoarthritis", "rheumatoid arthritis", "brachyolmia", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "alopecia", "myosclerosis", "hemoglobinopathy", "pseudoachondroplasia"]
last_modified_at: 2026-10-28
description: "Iopromide: 예측 신규 적응증 골관절염 (osteoarthritis) (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201400622/EE"
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
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201400622/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201802934/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201804420/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201804419/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201400621/EE |
| 예측 신규 적응증 | 골관절염 (osteoarthritis) |
| TxGNN 예측 점수 | 0.9953 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 5건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. Iopromide는 요오드화 비이온성 방사선 조영제로, 항염증 작용이나 연골 보호 작용이 알려져 있지 않습니다. 관절 조영술에 쓰일 수 있으나 이는 진단 목적이며 치료 효과가 아닙니다.

TxGNN 점수(0.9953)는 TxGNN 모델(딥러닝)에서 나온 값이며, 관련 질환 간에 모델이 학습한 유사성을 반영할 수 있을 뿐 생물학적 근거는 아닙니다. 기전적 연결고리는 확인되지 않았으며, 이를 뒷받침하는 임상시험이나 문헌도 없습니다.

참고로 같은 약물에 대해 류마티스 관절염(0.9937), 알로페시아(탈모, 0.9911), 헤모글로빈병증(0.9908), 가성연골무형성증(0.9906) 등 여러 질환이 예측되었습니다. 이들 역시 모두 L5이며 Hold 판정입니다. 이 중 일부는 희귀 유전성 골격 이형성증으로, 조영제의 약리와 연결되지 않습니다. 헤모글로빈병증의 경우 일부 혈액 질환(예: 겸상적혈구병)에서 조영제의 삼투압 영향으로 오히려 안전성 우려가 있을 수 있어, 치료 사용에 불리합니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201400622 | 레이프로주370 (수출용) | 무색투명한 주사액 (병 또는 바이알) | 허가 적응증 텍스트는 외부 링크로만 제공됨 |
| 201802934 | 울트라비스트300주 프리필드카트리지 | 투명한 액이 든 플라스틱 카트리지 주사제 | 허가 적응증 텍스트는 외부 링크로만 제공됨 |
| 201804420 | 울트라비스트듀300주사 | 투명한 액이 든 유리병/바이알 주사제 | 허가 적응증 텍스트는 외부 링크로만 제공됨 |
| 201804419 | 울트라비스트듀370주사 | 투명한 액이 든 유리병/바이알 주사제 | 허가 적응증 텍스트는 외부 링크로만 제공됨 |
| 201400621 | 레이프로주300 (수출용) | 무색투명한 주사액 (병 또는 바이알) | 허가 적응증 텍스트는 외부 링크로만 제공됨 |

모두 단일 성분 제품이며 유효한 허가입니다.

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
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

