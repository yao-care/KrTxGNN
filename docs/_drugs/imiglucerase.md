---
layout: default
title: Imiglucerase
parent: 모델 예측만 (L5)
nav_order: 417
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Imiglucerase: 예측 신규 적응증 헐러 증후군 (Hurler syndrome, MPS I) (근거 수준 L4). 기존 적응증: 허가 적응증 원문은 허가증 문서 링크로만 제공되어 구체적인 문구를 확인할 수 없음(고셰병 효소대체요법으로 사용)"
monitor_inn: "Imiglucerase"
predicted_indications: ["Hurler syndrome", "Scheie syndrome", "benign neoplasm of adrenal gland", "autosomal ichthyosis syndrome with fatal disease course", "cholesteryl ester storage disease"]
---

# Imiglucerase
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **5** 건
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

## Imiglucerase: 고셰병에서 헐러 증후군으로
{: .text-alpha }

## 한 문장 요약

Imiglucerase는 재조합 베타-글루코세레브로시다제 효소로, 원래 고셰병(Gaucher disease)의 효소대체요법에 사용되어 왔습니다.
TxGNN 모델은 **헐러 증후군(Hurler syndrome)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 직접 뒷받침하는 **임상시험은 0건**이고 **문헌은 1편**(리소좀 축적질환 효소대체요법 일반 리뷰)뿐입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 원문은 허가증 문서 링크로만 제공되어 구체적인 문구를 확인할 수 없음(고셰병 효소대체요법으로 사용) |
| 예측 신규 적응증 | 헐러 증후군 (Hurler syndrome, MPS I) |
| TxGNN 예측 점수 | 0.9952 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 3건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Imiglucerase는 고셰병에서 글루코실세라마이드의 축적을 줄이는 재조합 글루코세레브로시다제입니다.

헐러 증후군(MPS I)은 알파-L-이두로니다제 결핍으로 글리코사미노글리칸이 축적되는 질환입니다. 효소와 기질이 모두 달라 Imiglucerase가 직접 작용할 기전적 근거는 없습니다. 두 질환의 유일한 연결고리는 "리소좀 축적질환에 대한 효소대체요법"이라는 일반 개념입니다.

따라서 높은 TxGNN 점수는 특정한 생물학적 관계라기보다 리소좀 축적질환 간 네트워크 근접성을 반영한 것으로 보입니다. 같은 맥락에서 2위 예측인 샤이에 증후군(Scheie syndrome, MPS I의 경증형)도 동일한 한계를 가집니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [21211680](https://pubmed.ncbi.nlm.nih.gov/21211680/) | 2010 | Review | La Revue de médecine interne | 고셰병 효소대체요법(alglucerase, 이후 imiglucerase)을 시작으로 파브리병 등 리소좀 축적질환 효소대체요법이 발전해 온 과정을 개괄한 리뷰. 헐러 증후군에 대한 imiglucerase의 직접 근거는 아니며 계열 수준의 간접 맥락만 제공 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201207109 | 애브서틴주200단위 | 동결건조 주사제(재구성용) | 허가사항 문서 참조 |
| 201502789 | 애브서틴주400단위 | 동결건조 주사제(재구성용) | 허가사항 문서 참조 |
| 201210160 | 세레자임주400단위 | 동결건조 주사제(재구성용) | 허가사항 문서 참조 |

제조사: 애브서틴주 (주)이수앱지스, 세레자임주 (주)사노피-아벤티스코리아

## 안전성 고려사항

- **약물 상호작용**: Miglustat과 병용 시 중등도(Moderate) 상호작용이 보고되어 있습니다.

그 외 경고 및 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
Imiglucerase와 헐러 증후군 사이에는 효소·기질 측면에서 직접적인 기전 연결이 없으며, 임상시험도 없고 문헌도 일반 리뷰 1편뿐입니다. 높은 예측 점수는 네트워크 근접성에 따른 결과일 가능성이 큽니다.

**진행하려면 필요한 것:**
- 상세한 약물 작용 기전(MOA) 데이터 확보
- 헐러 증후군 기질(글리코사미노글리칸)에 대한 imiglucerase의 활성 여부를 확인하는 전임상 연구
- 한국 허가 적응증 및 경고·금기 정보 확인(허가증 원문 확보)
- 참고: 헐러 증후군에는 알파-L-이두로니다제 대체 효소(laronidase 등)가 이미 표적 치료제로 존재하므로, 이와 비교한 재창출 필요성 검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

