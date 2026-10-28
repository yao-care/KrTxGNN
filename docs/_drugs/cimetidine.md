---
layout: default
title: Cimetidine
parent: 모델 예측만 (L5)
nav_order: 214
evidence_level: L5
indication_count: 4
monitor_inn: "CIMETIDINE"
predicted_indications: ["peptic ulcer perforation", "duodenal obstruction", "acne (disease)", "abnormality of glucagon secretion"]
last_modified_at: 2026-10-27
description: "Cimetidine: 예측 신규 적응증 소화성 궤양 천공 (peptic ulcer perforation) (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200200521/EE"
---

# Cimetidine
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **4** 건
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

## Cimetidine: H2 수용체 길항제 → 소화성 궤양 천공 (peptic ulcer perforation)
{: .text-alpha }

## 한 문장 요약

Cimetidine은 위산 분비를 억제하는 H2 수용체 길항제 계열의 약물입니다.
TxGNN 모델은 **소화성 궤양 천공(peptic ulcer perforation)**에 효과가 있을 수 있다고 예측하지만, 현재 등록된 임상시험은 **0건**이며 문헌 20편은 대부분 간접적이거나 시메티딘 투여 중 천공이 발생한 증례 보고입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200200521/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/197800307/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200503802/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/197800165/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200501464/EE;  |
| 예측 신규 적응증 | 소화성 궤양 천공 (peptic ulcer perforation) |
| TxGNN 예측 점수 | 0.9977 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 20건 (일부 기록만 포함되었을 수 있음) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Cimetidine은 위산 분비를 줄이는 H2 수용체 길항제 계열 약물로, 위산 억제가 궤양 재발 예방에 도움이 될 수 있다는 점에서 소화성 궤양과 기전상 관련이 있습니다.

그러나 궤양 천공은 응급 수술이 필요한 합병증이며, Cimetidine이 천공 자체를 치료하는 약물이라는 근거는 없습니다. 검색된 문헌의 상당수는 Cimetidine 투여 중 또는 중단 후 천공이 발생한 증례(PMID 3967139, 6743974, 922364)로, 효능보다는 안전성 측면의 신호에 가깝습니다. 점막 보호나 지속 치료에 관한 논문은 간접적인 근거에 그칩니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

소화성 궤양 천공을 직접 대상으로 Cimetidine의 효능을 검증한 연구는 확인되지 않았습니다. 아래는 관련성이 높은 문헌입니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [7082957](https://pubmed.ncbi.nlm.nih.gov/7082957/) | 1982 | 증례 보고 | Br J Surg | Cimetidine 도입 후 择期 수술은 45% 감소했으나 천공 건수는 약 10% 감소에 그침 |
| [6743974](https://pubmed.ncbi.nlm.nih.gov/6743974/) | 1984 | 증례 보고 | Br J Surg | Cimetidine 투여 중 십이지장 궤양 천공 9건; 모두 미주신경절단술 및 배액술 필요 |
| [3967139](https://pubmed.ncbi.nlm.nih.gov/3967139/) | 1985 | 증례 보고 | Br J Surg | Cimetidine 투여 중 천공 발생 보고 |
| [8364140](https://pubmed.ncbi.nlm.nih.gov/8364140/) | 1993 | 리뷰 | Aliment Pharmacol Ther | H2 수용체 길항제 지속 치료가 궤양 재발률을 낮춤 (천공 직접 평가는 아님) |
| [2573146](https://pubmed.ncbi.nlm.nih.gov/2573146/) | 1989 | 리뷰 | Scand J Gastroenterol Suppl | H2 길항제의 NSAID 유발 점막 손상 보호 |
| [6649737](https://pubmed.ncbi.nlm.nih.gov/6649737/) | 1983 | 관찰 연구 | Z Gastroenterol | Cimetidine 도입 후 궤양 수술 35% 감소; 합병증 수술도 감소 |
| [922364](https://pubmed.ncbi.nlm.nih.gov/922364/) | 1977 | 보고 | Br Med J | Cimetidine 중단 후 소화성 궤양 천공 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 197800307 | 싸이메트정 | 필름코팅정 | 허가 문서 링크로만 기재됨 |
| 197800165 | 시그나틴정 | 필름코팅정 | 허가 문서 링크로만 기재됨 |
| 198401252 | 타가메트정400밀리그램 | 필름코팅정 | 허가 문서 링크로만 기재됨 |
| 197800134 | 타가메트주사 | 주사제(앰플) | 허가 문서 링크로만 기재됨 |
| 202005464 | 팜편안엠정 | 필름코팅정 | 위통, 속쓰림, 체함, 구역 |

※ 허가증은 총 20건이며, 위 표는 일부만 나열한 것입니다. 기록이 일부만 수집되었을 수 있습니다.

## 안전성 고려사항

- **약물 상호작용**: 데이터에 총 100건의 상호작용이 있으며, 주요 항목은 다음과 같습니다.
  - 중등도: Paclitaxel, Fentanyl, Acalabrutinib, Lidocaine, Acebutolol, Dihydrocodeine, Codeine, Tramadol, Nifedipine, Alfentanil
  - 경미: Dolutegravir, Zidovudine, Acetaminophen, Ketorolac, Ibuprofen, Ethinylestradiol, Albendazole, Ethanol, Alendronic acid, Cholecalciferol

주요 경고 및 금기는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
소화성 궤양 천공을 직접 연구한 임상시험이나 문헌이 없어 근거 수준은 L5입니다. 천공은 수술이 필요한 응급 합병증이며, 검색된 문헌은 Cimetidine 투여 중 천공이 발생한 증례가 중심이어서 진행을 뒷받침하지 않습니다.

**진행하려면 필요한 것:**
- 소화성 궤양 천공에 대한 Cimetidine의 직접적인 임상 또는 전임상 근거
- 허가사항의 경고·금기 정보 확보 (현재 누락)
- 상세한 약물 작용 기전(MOA) 데이터
- 한국 시판 상태(취하 여부) 확인
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

