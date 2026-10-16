---
layout: default
title: Pemetrexed
parent: 모델 예측만 (L5)
nav_order: 586
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Pemetrexed: 예측 신규 적응증 악성 복막 중피종 (Malignant Peritoneal Mesothelioma) (근거 수준 L5). 기존 적응증: MFDS 허가증 원문 참조 (본 보고서에 허가 적응증 본문 없음)"
monitor_inn: "pemetrexed"
predicted_indications: ["malignant peritoneal mesothelioma", "pleural adenomatoid tumor", "pleural mesothelioma", "pleural epithelioid mesothelioma", "pleural sarcomatoid mesothelioma", "pleural biphasic mesothelioma", "pericardium cancer", "well differentiated papillary mesothelioma", "lymphohistiocytoid mesothelioma", "iminoglycinuria"]
---

# Pemetrexed
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
{: .fs-6 .fw-300 }

---

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 약사 평가 보고서

</div>

# Pemetrexed: 기존 항암 적응증에서 악성 복막 중피종으로

## 한 문장 요약

Pemetrexed는 엽산 대사를 차단하는 항종양제로, 국내에서 20건의 단일제 허가증으로 시판되고 있습니다.
TxGNN 모델은 **악성 복막 중피종(Malignant Peritoneal Mesothelioma)**에 효과가 있을 수 있다고 예측하며, 현재 **7건의 임상시험**과 **20편의 문헌**이 이 방향을 지지합니다.
다만 복막 부위에 한정된 3상 무작위 시험은 없고, 근거의 상당 부분은 흉막 중피종 연구와 2상 시험에서 나옵니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | MFDS 허가증 원문 참조 (본 보고서에 허가 적응증 본문 없음) |
| 예측 신규 적응증 | 악성 복막 중피종 (Malignant Peritoneal Mesothelioma) |
| TxGNN 예측 점수 | 99.99% |
| 근거 수준 | L3 (후향 관찰 연구 및 문헌고찰 중심, 완료된 무작위 시험 없음) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 20건 (모두 유효, 단일제) |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

Pemetrexed는 티미딜레이트 합성효소(TS), DHFR, GARFT를 억제합니다. 이를 통해 퓨린과 피리미딘 합성을 막아 빠르게 분열하는 종양세포의 증식을 억제합니다. 중피종은 항엽산제에 비교적 민감하며, TS 발현이 치료 반응과 연관된다는 보고가 있습니다.

복막 중피종은 흉막 중피종과 조직학적, 생물학적 특성이 유사합니다. 흉막 중피종에서는 pemetrexed와 platinum 병용이 표준 화학요법입니다. 핵심 3상 시험(PMID 12860938)에서 cisplatin 단독 대비 pemetrexed 병용의 생존 이점이 확인되었습니다. 따라서 이 기전은 복막 부위에도 적용될 수 있습니다.

복막 부위의 직접 근거는 2상 시험과 후향 연구에서 나옵니다. 여기에는 흉막 또는 복막 중피종을 대상으로 한 완료된 2상 시험(NCT00061477)이 포함됩니다. 최신 문헌(PMID 39413826)도 복막 중피종의 전신 치료 권고가 흉막 중피종 시험에서 외삽된 것이라고 설명합니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00061477](https://clinicaltrials.gov/study/NCT00061477) | Phase 2 | 완료 | 48 | 흉막/복막 중피종 1차 치료로 pemetrexed + gemcitabine 평가. 복막 환자를 직접 포함하나 단일군 설계 |
| [NCT05001880](https://clinicaltrials.gov/study/NCT05001880) | Phase 2 | 모집 중 | 66 | 복막 중피종에서 carboplatin + pemetrexed + bevacizumab에 atezolizumab 추가 여부를 무작위 비교. 결과 미발표 |
| [NCT06543069](https://clinicaltrials.gov/study/NCT06543069) | Phase 2 | 모집 중 | 28 | 절제 불가 복막 중피종에서 sintilimab + bevacizumab + pemetrexed + cisplatin 단일군 시험 |
| [NCT03875144](https://clinicaltrials.gov/study/NCT03875144) | Phase 2 | 중단(보류) | 66 | PIPAC + 전신 화학요법(cisplatin + pemetrexed) vs 전신 화학요법 단독 비교. pemetrexed의 기여는 분리되지 않음 |
| [NCT02535312](https://clinicaltrials.gov/study/NCT02535312) | Phase 1/2 | 진행 중(모집 종료) | 30 | TRC102 + cisplatin + pemetrexed. 혼합 고형암 대상 안전성 중심이며 복막 중피종은 소수 |
| [NCT06057935](https://clinicaltrials.gov/study/NCT06057935) | Phase 2 | 모집 중 | 64 | 세포감축술과 HIPEC 후 복강내 vs 정맥 화학요법 비교. 복강내 약제가 초점이라 pemetrexed와는 간접적 관련 |
| [NCT00402766](https://clinicaltrials.gov/study/NCT00402766) | Phase 1 | 완료 | 19 | 악성 중피종에서 cisplatin + pemetrexed + imatinib의 최대내약용량 탐색. 소규모 안전성 시험 |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [28594258](https://pubmed.ncbi.nlm.nih.gov/28594258/) | 2017 | 후향 연구 | Expert Rev Anticancer Ther | 복막 중피종에서 1차 pemetrexed + cisplatin 전신 화학요법의 효능을 후향적으로 평가 |
| [21528659](https://pubmed.ncbi.nlm.nih.gov/21528659/) | 2011 | 단일기관 후향 연구 | Tumori | 항암 치료 경험이 없는 복막 중피종 환자에서 pemetrexed + cisplatin의 효능과 안전성 평가 |
| [41133016](https://pubmed.ncbi.nlm.nih.gov/41133016/) | 2025 | 비교 연구 | Clin Med Insights Oncol | 복막 중피종 1차 치료에서 pemetrexed-platinum과 gemcitabine-platinum 비교. pemetrexed-platinum이 1차 전신 치료의 주류 |
| [38806763](https://pubmed.ncbi.nlm.nih.gov/38806763/) | 2024 | 다기관 연구 | Ann Surg Oncol | 복막 중피종의 임상병리 특성, 예후, 치료 전략을 다기관에서 분석 |
| [39413826](https://pubmed.ncbi.nlm.nih.gov/39413826/) | 2024 | Review | J Natl Compr Canc Netw | 복막 중피종 전용 임상시험이 드물어 전신 치료 권고는 흉막 중피종 시험에서 외삽. 1차 옵션에 nivolumab + ipilimumab 또는 pemetrexed 기반 화학요법 포함 |
| [36765620](https://pubmed.ncbi.nlm.nih.gov/36765620/) | 2023 | Review | Cancers | 미만성 복막 중피종의 진단 및 치료 경로. 세포감축술 + HIPEC 적합 환자에서 생존 최적(중앙 OS 34–92개월) |
| [35407498](https://pubmed.ncbi.nlm.nih.gov/35407498/) | 2022 | Review | J Clin Med | 선택된 환자에서는 세포감축술과 HIPEC이 우선 치료로 자리 잡음 |
| [30450291](https://pubmed.ncbi.nlm.nih.gov/30450291/) | 2018 | Review | Transl Lung Cancer Res | 복막 중피종은 매우 드물고 예후가 불량한 종양이며, 석면 노출과의 연관성은 흉막보다 약함 |
| [26941986](https://pubmed.ncbi.nlm.nih.gov/26941986/) | 2016 | Review | J Gastrointest Oncol | 복막 중피종의 진단과 관리. 미국에서 연간 약 800건 발생 |
| [33257382](https://pubmed.ncbi.nlm.nih.gov/33257382/) | 2020 | 증례 보고 | BMJ Case Rep | 초기 전신 화학요법 후 nivolumab을 투여한 복막 중피종 1례 |

---

## 한국 시판 정보

총 20건의 허가증 중 주요 5건입니다. 허가 적응증은 MFDS 허가증 원문 링크로만 제공되어 요약하지 못했습니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201204635 | 페림타주500밀리그램 (광동제약) | 주사용 동결건조 분말 바이알 | [허가증 원문](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201204635/EE) 참조 |
| 201800591 | 메인타주사액100밀리그램 (동아에스티) | 주사액 바이알 | [허가증 원문](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201800591/EE) 참조 |
| 201501028 | 펨타주25밀리그램/밀리리터 (에이치케이이노엔) | 주사액 바이알 | [허가증 원문](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201501028/EE) 참조 |
| 201505185 | 알림시드주800밀리그램 (보령바이오파마) | 주사용 동결건조 분말 바이알 | [허가증 원문](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201505185/EE) 참조 |
| 201207342 | 메인타주300밀리그램 (동아에스티) | 주사용 동결건조 분말 바이알 | [허가증 원문](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201207342/EE) 참조 |

---

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 약물 (항엽산 대사길항제) |
| 골수억제 위험 | 높음. 호중구감소증, 혈소판감소증, 빈혈은 지식그래프에서 확인된 금기·주의 질환 항목에 해당 |
| 구토 유발성 등급 | 저~중등도 (cisplatin 병용 시 병용약에 따라 상승) |
| 모니터링 항목 | CBC(분류 포함), 신기능, 간기능. 엽산·비타민 B12 보충 병행(임상시험 프로토콜에서 비타민 B12 보충을 사용) |
| 취급 방호 | 세포독성 약물 취급 규정 준수 필요 |

위 분류는 일반적인 약물 분류에 따른 것입니다. 상세 수치는 허가사항의 경고 및 주의사항을 참조하세요.

---

## 안전성 고려사항

- **지식그래프상 금기 관련 질환**: 신장 질환, 신기능 장애, 농뇨관(pyoureter), 혈소판감소증, 호중구감소증, 무과립구증, 빈혈, 거대적아구성 빈혈. 이는 허가 문서가 아니라 지식그래프에서 도출한 정보이므로 허가사항과 대조가 필요합니다.
- **약물 상호작용**: 총 367건이 확인되었습니다. 목록에 제시된 항목은 모두 중등도(Moderate)입니다. 주요 항목은 다음과 같습니다.
  - 위산억제제: famotidine, ranitidine, cimetidine
  - 당뇨병 치료제: metformin
  - 항진균제: amphotericin B(지질 제형 포함)
  - 항생제: amoxicillin, vancomycin, kanamycin, neomycin, levofloxacin, polymyxin B
  - 소염제: aspirin, mesalazine, balsalazide, olsalazine
  - 기타: sapropterin

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
pemetrexed + platinum은 흉막 중피종에서 3상으로 입증된 표준 요법이고, 복막 중피종에서는 후향 연구와 완료된 2상 시험이 이를 뒷받침합니다. 여러 2상 시험이 진행 중이지만, 복막 부위에 한정된 3상 무작위 시험이 없어 근거 수준은 L3로 평가했습니다. 이 평가는 단일군 시험은 판정 기준의 무작위 시험으로 인정하지 않았고, 후향 관찰 연구와 문헌고찰을 근거로 삼았기 때문입니다. 따라서 조건부로 진행할 수 있습니다.

**진행하려면 필요한 것:**
- 허가증 원문에서 허가 적응증, 경고, 금기 확인(허가 적응증에 중피종이 포함되는지 포함)
- 복막 중피종 전용 전향 시험(NCT05001880, NCT06543069 등)의 결과 확인
- 세포감축술 + HIPEC 적합 환자와 부적합 환자를 구분한 치료 위치 설정, 면역항암제 병용(nivolumab + ipilimumab 등)과의 비교 검토
- 골수억제, 신기능, 엽산·B12 보충을 포함한 안전성 모니터링 계획
- 상호작용 약물(NSAID, 항생제, 위산억제제 등) 병용 시 신기능 및 약물 농도 관리 방안

**참고:** 같은 예측 목록의 흉막 중피종은 이미 확립된 표준 치료이므로 새로운 재창출 발견이 아니라 기존 적응증의 확인으로 봐야 합니다. 흉막 선종양양 종양, 고분화 유두상 중피종, 림프조직구양 중피종, 이미노글리신뇨증은 임상 근거가 없고 세포독성 약물이 부적절할 수 있어 보류를 권고합니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

