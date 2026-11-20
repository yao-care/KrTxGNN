---
layout: default
title: Imiglucerase
parent: 모델 예측만 (L5)
nav_order: 417
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-20
description: "Imiglucerase: 예측 신규 적응증 헐러 증후군 (Hurler syndrome, MPS I) (근거 수준 L5). 기존 적응증: 다음의 적응증 중 한가지 이상의 증상을 나타내는 타입 I 고셔병으로 확진된 환자에서 장기간 효소…"
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
| 기존 적응증 | 다음의 적응증 중 한가지 이상의 증상을 나타내는 타입 I 고셔병으로 확진된 환자에서 장기간 효소 대체요법으로 사용한다. * 철결핍 이외의 원인으로 인한 빈혈 * 혈소판 감소 * 비타민 D결핍 이외의 원인으로 인한 골질환 * 간비대증 또는 비장비대증 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201207109/EE)) |
| 예측 신규 적응증 | 헐러 증후군 (Hurler syndrome, MPS I) |
| TxGNN 예측 점수 | 0.9952 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 3건 / 전체 3건) |
| 허가증 수 | 3건 (유효 3건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Imiglucerase 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “고셔병은 β-글루코세레브로시다제 활성의 결핍을 특징으로 하며, 이로 인해 간, 비장 및 골수를 포함한 여러 조직에 글루코세레브로시드가 축적된다. 이미글루세라제의 만노스 당은 대식세포를 포함한 세포에 대한 결합 및 세포 내 흡수를 매개한다.” 영어 원문: "Gaucher disease is characterized by a deficiency of β-glucocerebrosidase activity, which results in accumulation of glucocerebroside in various tissues including liver, spleen, and bone marrow. The mannose sugars on imiglucerase mediate binding to and internalization by cells including macrophages." ([DailyMed: Cerezyme (imiglucerase) prescribing information, Genzyme Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=df60f030-866b-4374-a31f-8ae3f6b45c38), 버전 2026-08-27; 확인일 2026-11-19). 알려진 정보에 따르면 Imiglucerase는 고셰병에서 글루코실세라마이드의 축적을 줄이는 재조합 글루코세레브로시다제입니다.

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

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Cerezyme (imiglucerase) prescribing information, Genzyme Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=df60f030-866b-4374-a31f-8ae3f6b45c38) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

