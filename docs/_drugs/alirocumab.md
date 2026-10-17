---
layout: default
title: Alirocumab
parent: 모델 예측만 (L5)
nav_order: 39
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Alirocumab: 예측 신규 적응증 X-연관 어린선, 스테로이드 설파타아제 결핍 없음 (ichthyosis, X-linked… (근거 수준 L5). 기존 적응증: 허가 적응증 본문이 데이터에 포함되어 있지 않음(허가증 문서 링크만 제공). 약리 분류상 고콜레스테롤혈증 및 죽상경화성 심혈…"
monitor_inn: "Alirocumab"
predicted_indications: ["ichthyosis, X-linked, without steroid sulfatase deficiency", "disorder of other vitamins and cofactors metabolism and transport", "xanthomatosis (disease)", "46,XY disorder of sexual development due to dihydrotestosterone backdoor pathway biosynthesis defect", "cholesterol catabolic process disease", "46,XY disorder of sex development due to a cholesterol synthesis defect", "dappled diaphyseal dysplasia", "neutral lipid storage disease", "3-hydroxyacyl-CoA dehydrogenase deficiency", "spastic paraplegia-optic atrophy-neuropathy and spastic paraplegia-optic atrophy-neuropathy-related disorder"]
---

# Alirocumab
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

# Alirocumab: 고콜레스테롤혈증에서 X-연관 어린선(ichthyosis)으로

## 한 문장 요약

Alirocumab은 PCSK9를 표적으로 하는 단클론항체로, 원래 LDL 콜레스테롤을 낮추는 지질강하 치료에 사용되었습니다.
TxGNN 모델은 **X-연관 어린선(스테로이드 설파타아제 결핍 없음)**에 효과가 있을 수 있다고 예측하지만(예측 점수 99.43%), 이 질환을 직접 뒷받침하는 **임상시험은 0건, 문헌도 0건**입니다.
이 예측은 지식 그래프의 인위적 결과일 가능성이 높아 현 단계에서는 보류가 타당합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문이 데이터에 포함되어 있지 않음(허가증 문서 링크만 제공). 약리 분류상 고콜레스테롤혈증 및 죽상경화성 심혈관질환에서의 LDL-C 저하 |
| 예측 신규 적응증 | X-연관 어린선, 스테로이드 설파타아제 결핍 없음 (ichthyosis, X-linked, without steroid sulfatase deficiency) |
| TxGNN 예측 점수 | 99.43% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 5건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 이번 보고서용으로 수집된 자료에 없습니다. 다만 약리 정보에 따르면 Alirocumab은 PCSK9(proprotein convertase subtilisin/kexin type 9)에 결합하는 항체입니다. PCSK9를 억제하면 LDL 수용체 재순환이 늘어 혈중 LDL-C가 감소합니다. 미국 FDA는 2015년 7월 이형접합 가족성 고콜레스테롤혈증과 임상적 죽상경화성 심혈관질환 환자에게 이 약을 승인했습니다.

X-연관 어린선은 스테로이드 설파타아제와 콜레스테롤 황산염 축적과 연관된 피부 질환입니다. PCSK9 억제 및 LDL-C 저하와 직접 이어지는 기전적 연결 고리는 확인되지 않았습니다. 높은 TxGNN 점수는 콜레스테롤 관련 키워드에서 비롯된 지식 그래프상의 인위적 결과일 가능성이 큽니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202300530 | 프랄런트펜주300mg | 프리필드 주사기(주입기 장착) 주사액 | 허가 적응증 본문 미확인(허가증 문서 참조) |
| 201700394 | 프랄런트주75mg | 프리필드 주사기 주사액 | 허가 적응증 본문 미확인(허가증 문서 참조) |
| 201700395 | 프랄런트펜주150mg | 프리필드 주사기(주입기 장착) 주사액 | 허가 적응증 본문 미확인(허가증 문서 참조) |
| 201700396 | 프랄런트펜주75mg | 프리필드 주사기(주입기 장착) 주사액 | 허가 적응증 본문 미확인(허가증 문서 참조) |
| 201700393 | 프랄런트주150mg | 프리필드 주사기 주사액 | 허가 적응증 본문 미확인(허가증 문서 참조) |

제조사는 모두 (주)사노피-아벤티스코리아이며, 5건 모두 단일제로 유효 상태입니다.

## 안전성 고려사항

- **약물 상호작용**: 약리 데이터베이스에서 확인된 항목은 표적인 PCSK9(상호작용 대상: proprotein convertase subtilisin/kexin type 9)뿐이며, 병용 약물과의 임상적 상호작용 등급은 제시되지 않았습니다.

그 외 안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
X-연관 어린선에 대한 임상시험과 문헌이 전혀 없고(근거 수준 L5), PCSK9 억제와 이 질환 사이의 타당한 기전적 연결도 확인되지 않았습니다. 높은 모델 점수만으로는 개발을 진행할 근거가 부족합니다.

**진행하려면 필요한 것:**
- X-연관 어린선의 병태생리(콜레스테롤 황산염 대사)와 PCSK9 경로의 연관성을 입증하는 전임상 또는 기전 연구
- 허가사항(경고, 금기, 허가 적응증)의 확보 및 분석: 현재 안전성 선별을 진행할 수 없는 상태
- 상세한 작용 기전(MOA) 데이터 보완

**참고: 다른 예측 후보**
같은 모델의 상위 예측 중 다음 두 가지는 상대적으로 의미 있는 검토 대상입니다.
- **황색종증(xanthomatosis, 점수 99.37%, L4)**: 심한 고콜레스테롤혈증에서 지질이 침착되어 생기는 질환이므로, LDL-C 저하가 병변 소실을 도울 수 있다는 간접적이나 생물학적으로 일관된 근거가 있습니다. 다만 확인된 문헌 2편은 증례 보고 수준이어서 Alirocumab의 효과를 확증하지 못합니다(sitosterolemia는 ABCG5/ABCG8 이상이라 효과가 불확실). 연구 질문(Research Question) 단계입니다.
- **콜레스테롤 이화과정 질환(cholesterol catabolic process disease, 점수 99.36%, L4)**: 가족성 고콜레스테롤혈증 등 이미 승인된 적응증과 겹치는 범주입니다. 검색된 문헌 19편은 주로 PCSK9 치료제 리뷰와 안전성 분석(47,296 환자-년 관찰 포함)이며, 새로운 재창출이라기보다 기존 용도의 재발견에 가깝습니다.

나머지 상위 예측(비타민·보조인자 대사 장애, 46,XY 성분화 장애, 반점 골간 이형성증, 중성지질 저장병, 3-하이드록시아실-CoA 탈수소효소 결핍증, 경직성 하지마비-시신경위축-신경병증)은 기전적 연결과 임상 근거가 모두 없어 Hold가 적절합니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

