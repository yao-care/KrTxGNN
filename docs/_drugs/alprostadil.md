---
layout: default
title: Alprostadil
parent: 모델 예측만 (L5)
nav_order: 48
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
monitor_inn: "Alprostadil"
predicted_indications: ["aortic malformation", "congenital tricuspid stenosis", "congenital valvular dysplasia", "straddling or overriding tricuspid valve", "tricuspid valve prolapse (disease)", "anomaly of the tricuspid subvalvular apparatus", "double outlet right ventricle with atrioventricular septal defect, pulmonary stenosis, heterotaxy", "heart septal defect", "endemic goiter"]
description: "Alprostadil: 예측 신규 적응증 대동맥 기형 (aortic malformation) (근거 수준 L5). 기존 적응증: 1. 만성동맥폐색증(버거씨병, 폐색성동맥경화증)에 있어서 사지궤양, 안정시 통증의 개선 2. 다음 질환에…"
---

# Alprostadil
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

## Alprostadil: 대동맥 기형 (aortic malformation)
{: .text-alpha }

## 한 문장 요약

Alprostadil은 프로스타글란딘 E1(PGE1) 계열의 혈관확장제로, 한국에서 허가되어 있습니다(허가 건수와 상태는 빠른 개요 참조).
TxGNN 모델은 **대동맥 기형(aortic malformation)**에 효과가 있을 수 있다고 예측하며, 현재 이 방향을 지지하는 **문헌 8편**이 있으나 등록된 임상시험은 없습니다.

<!-- review:begin kr-lic-20261124c-alprostadil-1 -->

> **검토 정정 (2026-11-24)**: 원래 문장: “Alprostadil은 프로스타글란딘 E1(PGE1) 계열의 혈관확장제로, 한국에서 단일 성분 제제 4건이 허가되어 있습니다.” 식품의약품안전처 의약품안전나라(nedrug) 허가 자료(2026-11-23 데이터) 기준으로 수정했습니다: 단일·복합 표기와 건수를 본문에 고정해 쓰지 않고, 매주 갱신되는 허가 자료를 반영하는 빠른 개요와 「한국 시판 정보」의 표를 가리키도록 고쳤습니다. 2026-11-25에 식품의약품안전처 품목허가 상세 자료(2026-03)의 주성분명으로 품목별로 다시 확인한 결과, 이 자료에 수록된 허가 품목은 모두 단일 성분 제제입니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261124c-alprostadil-1 -->

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 1. 만성동맥폐색증(버거씨병, 폐색성동맥경화증)에 있어서 사지궤양, 안정시 통증의 개선 2. 다음 질환에 있어서 피부궤양의 개선 : 진행성전신성경화증, 전신성홍반성낭창 3. 진동병에 있어서 말초혈행장해에 수반하는 자각증상의 개선 및 말초순환, 신경, 운동기능장해의 회복 4. 동맥관… ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199802243/EE)) |
| 예측 신규 적응증 | 대동맥 기형 (aortic malformation) |
| TxGNN 예측 점수 | 0.9998 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 4건 / 전체 5건) |
| 허가증 수 | 5건 (유효 4건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 수집되지 않았습니다. 다만 알려진 약리 특성상 Alprostadil(PGE1)은 동맥관(ductus arteriosus)의 평활근을 이완시켜 개존을 유지합니다.

인터럽티드 대동맥궁, 중증 대동맥 협착, 대혈관 전위처럼 동맥관 의존성 병변에서는 수술 전까지 전신 또는 폐 혈류를 유지하는 데 쓰이며, 이는 신생아 진료에서 확립된 방식입니다. 이 점이 대동맥 기형 예측의 기전적 근거가 됩니다.

다만 현재 확보된 근거는 증례 보고, 증례 연구, 종설이 중심이며, 대동맥 기형을 직접 대상으로 한 임상시험은 없습니다. 2008년 울리나스타틴 병용 연구는 체외순환 후 염증 반응을 다룬 것으로 간접적인 기전입니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [6763200](https://pubmed.ncbi.nlm.nih.gov/6763200/) | 1982 | 임상 평가/증례 시리즈 | Pharmacotherapy | 영아 선천성 심질환에서 PGE1이 동맥관을 확장하여 폐혈류를 증가시킴 |
| [19068708](https://pubmed.ncbi.nlm.nih.gov/19068708/) | 2008 | 증례 보고 | Kyobu Geka | B형 대동맥궁 단절 신생아에서 동맥관 유지에 사용 후 일차 교정술과 지속적 혈액투석여과로 생존 |
| [15362549](https://pubmed.ncbi.nlm.nih.gov/15362549/) | 2004 | 종설 | Kyobu Geka | 대혈관 전위증에서 동맥관 개존 유지를 위한 PGE1 사용 |
| [30184041](https://pubmed.ncbi.nlm.nih.gov/30184041/) | 2018 | 증례 보고 | Braz J Cardiovasc Surg | 복합 대동맥폐동맥창 수술 전 밀리논과 함께 폐동맥압 저하 목적으로 사용 |
| [19080093](https://pubmed.ncbi.nlm.nih.gov/19080093/) | 2008 | 임상 연구 | Zhonghua Yi Xue Za Zhi | 선천성 심질환 소아의 체외순환 후 염증 반응 및 폐 손상에 대한 효과 |
| [20029353](https://pubmed.ncbi.nlm.nih.gov/20029353/) | 2009 | 전임상(쥐) | Minerva Chir | 쥐 골격근 허혈-재관류 손상 완화 |
| [41167776](https://pubmed.ncbi.nlm.nih.gov/41167776/) | 2025 | 후향적 연구 | Zhonghua Fu Chan Ke Za Zhi | 복합 태아 선천성 심질환의 분만 방식·시기 탐색 (Alprostadil은 주제 아님) |
| [42469655](https://pubmed.ncbi.nlm.nih.gov/42469655/) | 2026 | 후향적 연구 | BMC Pregnancy Childbirth | 복합 태아 선천성 심질환의 임신·주산기 관리 (Alprostadil은 주제 아님) |

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 199802243 | 에글란딘주(알프로스타딜) | 무색투명한 앰플에 들어있는 백색의 유탁액으로 약간 점성이 있으며 특이한… | 타나베파마코리아주식회사 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199802243/EE) | 유효 |
| 200908752 | 알로스틴주사(알프로스타딜)(프리필드) | 흰색의 전질균등한 유탁액이 들어 있는, 위아래가고무마개로막힌 무색투명한… | 동국제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200908752/EE) | 유효 |
| 200705481 | 카버젝트주사20마이크로그람(알프로스타딜) | 무색투명한 바이알에 든 백색의 동결건조분말 주사제(첨부용제 : 위아래가… | 한국화이자제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200705481/EE) | 유효 |
| 200705483 | 카버젝트주사10마이크로그람(알프로스타딜) | 무색투명한 바이알에 든 백색의 동결건조분말 주사제(첨부용제 : 위아래가… | 한국화이자제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200705483/EE) | 유효 |

위 표는 허가 5건 중 4건입니다.

<!-- licenses:end -->

## 안전성 고려사항

- **약물 상호작용**: 총 59건이 보고되어 있으며, 중등도 수준으로는 카나글리플로진, 다파글리플로진, 엠파글리플로진, 에르투글리플로진, 로카세린, 사프로프테린이 있습니다. 그 외 판토프라졸, 모르핀, 메트포르민, 오메프라졸, 반코마이신, 프레드니손, 심바스타틴 등은 등급 미상으로 보고되었습니다.
- **사용 시 유의할 이상반응(문헌 보고)**: 장기간 PGE1 투여 신생아에서 유문 협착과 위 출구 폐색, 가성 바터 증후군이 보고되었습니다.

허가사항의 경고 및 금기는 허가 문서를 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
동맥관 의존성 대동맥 병변에서 PGE1을 쓰는 것은 기전적으로 타당하고 임상 관행과도 부합합니다. 그러나 근거가 소수의 증례와 종설에 한정되고, 대동맥 기형을 직접 검증한 임상시험이 없어 현 단계에서는 추가 근거 확보가 우선입니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기·적응증) 원문의 확보 및 분석
- 작용 기전(MOA) 데이터 보완
- 대동맥 기형을 직접 대상으로 한 임상 연구 또는 체계적 문헌고찰
- 장기 투여 시 이상반응(위 출구 폐색, 전해질 이상 등)에 대한 모니터링 계획

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-24 | 단일·복합 표기: “Alprostadil은 프로스타글란딘 E1(PGE1) 계열의 혈관확장제로…” → 고정된 단일·복합 표기와 건수 삭제(건수는 빠른 개요와 표) | 정정 (2026-11-25 수정, 이전 판은 기록에 보존) | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

