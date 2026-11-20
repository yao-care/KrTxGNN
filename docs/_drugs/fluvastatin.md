---
layout: default
title: Fluvastatin
parent: 모델 예측만 (L5)
nav_order: 363
evidence_level: L5
indication_count: 6
monitor_inn: "Fluvastatin"
predicted_indications: ["HIV infectious disease", "cholesterol-ester transfer protein deficiency", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "fibroma of prostate"]
last_modified_at: 2026-11-15
description: "Fluvastatin: 예측 신규 적응증 HIV 감염증 (근거 수준 L5). 기존 적응증: 1. 다음의 심장혈관 질환에 대한 위험성감소 1) 식이요법에 적절히 반응하지 않는 원발성 고콜레스테롤혈증과…"
---

# Fluvastatin
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

## Fluvastatin: 고지혈증 치료제에서 HIV 감염증으로
{: .text-alpha }

## 한 문장 요약

Fluvastatin은 HMG-CoA 환원효소를 억제하는 스타틴 계열 약물로, 한국에서는 서방정 제제(레스콜엑스엘서방정)로 허가되어 있습니다. TxGNN 모델은 **HIV 감염증(HIV infectious disease)**에 효과가 있을 수 있다고 예측하지만, 이를 직접 입증하는 임상시험은 없고 **문헌 13편**(대부분 HIV 환자의 지질 관리나 HCV 동반감염 연구)만 간접적으로 관련됩니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 1. 다음의 심장혈관 질환에 대한 위험성감소 1) 식이요법에 적절히 반응하지 않는 원발성 고콜레스테롤혈증과 관상동맥질환을 나타내는 성인 환자에 대 한 관상동맥경화증의 진행 지연 2) 관상동맥질환 성인 환자의 경피적 관상동맥 삽관술 후 심장사고(coronary events)의 재발… ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200108760/EE)) |
| 예측 신규 적응증 | HIV 감염증 |
| TxGNN 예측 점수 | 0.9988 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 1건 / 전체 1건) |
| 허가증 수 | 1건 (유효 1건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Fluvastatin 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “플루바스타틴은 HMG-CoA 환원효소의 경쟁적 억제제이며, 이 효소는 3-히드록시-3-메틸글루타릴-조효소 A (HMG-CoA)를 콜레스테롤의 전구체인 메발론산으로 전환하는 속도 제한 효소이다.” 영어 원문: "Fluvastatin is a competitive inhibitor of HMG-CoA reductase, the rate limiting enzyme that converts 3-hydroxy-3-methylglutaryl-coenzyme A (HMG-CoA) to mevalonate, a precursor of cholesterol." ([DailyMed: Fluvastatin Sodium Er (fluvastatin sodium) prescribing information, Sandoz Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5ab4296c-87c2-4c64-b218-d620eef51310), 버전 2024-01-31; 확인일 2026-11-19). 알려진 정보에 따르면 fluvastatin은 HMG-CoA 환원효소 억제제(스타틴)로, 콜레스테롤 합성을 줄이는 약물입니다.

HIV와의 연결 고리는 두 가지로 생각할 수 있습니다. 첫째, 항레트로바이러스 치료로 생기는 이상지질혈증 관리입니다. Fluvastatin은 주로 CYP2C9로 대사되어 CYP3A4를 많이 거치는 다른 스타틴보다 단백분해효소 억제제와의 상호작용이 적은 편입니다. 둘째, 스타틴의 항염증·면역조절 작용이 만성 면역 활성화를 줄일 가능성이 있고, 쥐 모델에서 HIV 연관 신병증의 족세포 손상을 막은 전임상 결과도 있습니다.

다만 제시된 문헌은 대부분 지질 저하 효과와 약물 상호작용에 관한 것이며, HIV 자체에 대한 항바이러스 효과나 치료 효과를 보여주지는 않습니다. HIV·HCV 동반감염 환자에서 보조요법으로 쓴 연구가 있으나, 그 효과는 확립되지 않았습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [20118492](https://pubmed.ncbi.nlm.nih.gov/20118492/) | 2010 | 공개라벨 RCT | J Antimicrob Chemother | HIV/HCV 유전자형 1 동반감염 환자에서 PegIFN·ribavirin 보조요법으로 fluvastatin 평가 |
| [15293079](https://pubmed.ncbi.nlm.nih.gov/15293079/) | 2004 | 임상연구 | Infection | 항레트로바이러스 치료 중인 HIV 환자에서 fluvastatin·pravastatin의 지질 저하 효과와 indinavir 상호작용 비교 |
| [12351967](https://pubmed.ncbi.nlm.nih.gov/12351967/) | 2002 | 임상연구 | AIDS | 단백분해효소 억제제 치료를 받는 고지혈증 HIV 환자에서 fluvastatin의 효능과 안전성 |
| [16868453](https://pubmed.ncbi.nlm.nih.gov/16868453/) | 2006 | 임상연구 | AIDS | HIV 환자 20명을 ezetimibe 또는 fluvastatin 80 mg에 무작위 배정. LDL-C는 ezetimibe 20%, fluvastatin 24% 감소 |
| [19215577](https://pubmed.ncbi.nlm.nih.gov/19215577/) | 2009 | 예비연구 | J Viral Hepat | HIV-HCV 동반감염 환자에서 fluvastatin이 HCV 복제에 미치는 영향 평가 |
| [33238713](https://pubmed.ncbi.nlm.nih.gov/33238713/) | 2021 | 코호트 | AIDS Res Hum Retroviruses | 효과적인 항레트로바이러스 치료 중인 HIV 감염자에서 스타틴 사용과 염증·면역활성화 지표의 관련성 (스타틴 전반, fluvastatin 특이적 아님) |
| [19188342](https://pubmed.ncbi.nlm.nih.gov/19188342/) | 2009 | 전임상 | Nephrol Dial Transplant | HIV 연관 신병증 마우스 모델에서 fluvastatin이 족세포 손상을 예방 |
| [23703578](https://pubmed.ncbi.nlm.nih.gov/23703578/) | 2013 | 리뷰 | Clin Pharmacokinet | 스타틴과 항바이러스 단백분해효소 억제제 간 약물 상호작용 |
| [12660532](https://pubmed.ncbi.nlm.nih.gov/12660532/) | 2003 | 리뷰 | AIDS | 항레트로바이러스 치료 중인 HIV 환자의 고지혈증에서 스타틴과 fibrate의 역할 |
| [19838098](https://pubmed.ncbi.nlm.nih.gov/19838098/) | 2010 | RCT | AIDS | 이상지질혈증 HIV 환자에서 rosuvastatin과 pravastatin 비교 (fluvastatin 아님, 간접 근거) |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200108760 | 레스콜엑스엘서방정(플루바스타틴나트륨) | 황색의 원형 필름 코팅 서방정 | 허가 적응증 본문은 링크로만 제공되어 요약할 수 없음 |

## 안전성 고려사항

- **약물 상호작용**: 데이터에 100건의 상호작용이 기록되어 있으며, 주요 항목은 다음과 같습니다.
  - 중등도: aprepitant, metronidazole, oxandrolone, naltrexone, nateglinide, nitisinone, rosuvastatin, simvastatin, tinidazole, glyburide, pectin
  - 등급 미상: calcitriol, doxycycline, cimetidine, epinephrine, mannitol, dicyclomine, famotidine, acetylsalicylic acid, pantoprazole
- HIV 환자는 항레트로바이러스제를 병용하므로 상호작용 확인이 필요합니다. 스타틴 계열 간 병용(rosuvastatin, simvastatin)도 중등도 상호작용으로 기록되어 있습니다.
- 경고 및 금기 사항은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
HIV 감염증을 직접 연구한 임상시험이나 문헌이 없습니다. 제시된 문헌은 HIV 환자의 지질 관리, 약물 상호작용, HCV 동반감염, 전임상 연구에 해당하며, 항바이러스 효과나 HIV 치료 효과를 입증하지 않습니다. 따라서 근거 수준은 L5로 판단합니다. 같은 후보 목록의 다른 예측(CETP 결핍증, 희귀 신경발달장애, 원숭이·고양이 면역결핍 감염, 전립선 섬유종)도 근거가 전혀 없습니다.

**진행하려면 필요한 것:**
- 한국 허가 적응증 본문과 경고·금기 사항 확보 (허가사항 PDF 분석)
- 작용 기전 데이터 보충
- HIV 감염 자체(바이러스 부하, 면역활성화 등)를 평가변수로 하는 임상시험 설계 또는 근거 확보
- 항레트로바이러스제와의 상호작용 평가
- 시판 현황(취소 여부) 확인

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Fluvastatin Sodium Er (fluvastatin sodium) prescribing information, Sandoz Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5ab4296c-87c2-4c64-b218-d620eef51310) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

