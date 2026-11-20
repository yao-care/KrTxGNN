---
layout: default
title: Nizatidine
parent: 모델 예측만 (L5)
nav_order: 552
evidence_level: L5
indication_count: 2
monitor_inn: "NIZATIDINE"
predicted_indications: ["duodenal obstruction", "multiple endocrine neoplasia"]
last_modified_at: 2026-11-20
description: "Nizatidine: 예측 신규 적응증 십이지장 폐쇄 (duodenal obstruction) (근거 수준 L5). 기존 적응증: 1. 활동성 위ㆍ십이지장 궤양 치료 및 십이지장 궤양 재발방지 2. 내시경상으로 진단된 미란성 및 궤양성…"
---

# Nizatidine
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **2** 건
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

## Nizatidine: H2 수용체 길항제 → 십이지장 폐쇄 (duodenal obstruction)
{: .text-alpha }

## 한 문장 요약

Nizatidine은 위산 분비를 억제하는 H2 수용체 길항제 계열의 약물입니다. TxGNN 모델은 **십이지장 폐쇄(duodenal obstruction)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 직접 뒷받침하는 **임상시험은 0건, 문헌도 0편**이며 모델 예측만 있는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 1. 활동성 위ㆍ십이지장 궤양 치료 및 십이지장 궤양 재발방지 2. 내시경상으로 진단된 미란성 및 궤양성 식도염, 위식도 역류질환(GERD)에 기인한 가슴쓰림(heartburn) 증상의 치료 3. 다음 질환의 위점막병변(미란, 출혈, 발적, 부종)의 개선: 급성위염, 만성위염의 급성… ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201403769/EE)) |
| 예측 신규 적응증 | 십이지장 폐쇄 (duodenal obstruction) |
| TxGNN 예측 점수 | 0.9986 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 19건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Nizatidine 처방 정보(Prescribing Information)의 “Clinical Pharmacology” 항목에 따르면(비공식 번역): “니자티딘은 히스타민 H 2 -수용체, 특히 위 벽세포의 H 2 -수용체에서 히스타민의 경쟁적, 가역적 억제제이다. 위산 분비 억제 작용 위산 분비에 대한 효과 니자티딘은 최대 12시간 동안 야간 위산 분비를 유의하게 억제하였다.” 영어 원문: "Nizatidine is a competitive, reversible inhibitor of histamine at the histamine H 2 -receptors, particularly those in the gastric parietal cells. Antisecretory Activity Effects on Acid Secretion Nizatidine significantly inhibited nocturnal gastric acid secretion for up to 12 hours." ([DailyMed: nizatidine prescribing information, Epic Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e9957997-8b85-48a0-9bb3-b878cb223236), 버전 2025-01-02; 확인일 2026-11-19). 알려진 정보에 따르면 nizatidine은 H2 수용체 길항제 계열로, 위산 분비를 줄이는 방식으로 작용합니다.

다만 십이지장 폐쇄는 주로 궤양 흉터 등으로 생기는 기계적 문제이므로 산 억제만으로 직접 호전되기는 어렵습니다. 기저에 궤양이나 염증 요소가 있는 경우에 한해 보조적 도움이 될 가능성이 있는 정도입니다.

이 예측을 지지하는 임상시험이나 문헌이 없어, 현재 근거는 모델 예측에 한정됩니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201403769 | 니자딘엠캡슐 | 경질캡슐 | 허가사항 문서 참조 |
| 201600879 | 니자액스캡슐150mg | 경질캡슐 | 허가사항 문서 참조 |
| 200404671 | 빅시딘캡슐150밀리그램 | 경질캡슐 | 허가사항 문서 참조 |
| 201400450 | 틴자정150밀리그램 | 필름코팅정 | 허가사항 문서 참조 |
| 200200502 | 프로틴정 | 필름코팅정 | 이 약은 위산과다, 속쓰림, 신트림에 사용합니다. |

전체 20건 중 주요 5건만 나열했으며, 대부분의 허가 적응증은 문서 링크로만 제공되어 요약하지 못했습니다.

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 조회되었으며, 주요 등급 상호작용으로 atazanavir, dasatinib이 확인되었습니다. 중등도 상호작용에는 acalabrutinib, bosutinib, brigatinib, ceritinib, dabrafenib, dacomitinib 등이 있습니다. 일부 cephalosporin계(cefditoren, cefpodoxime, cefuroxime)와 chlorpropamide도 중등도입니다.

그 외 경고 및 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
십이지장 폐쇄는 기계적 질환이어서 산 억제제의 직접 효과를 기대하기 어렵고, 지지하는 임상시험과 문헌이 없어 근거 수준이 L5(모델 예측만 존재)입니다.

**진행하려면 필요한 것:**
- 십이지장 폐쇄에 대한 직접적인 임상시험 또는 문헌 근거
- 상세한 약물 작용 기전(MOA) 데이터
- 허가사항(경고·금기) 확인 및 안전성 검토
- 한국 시판 상태(취소 여부) 확인

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: nizatidine prescribing information, Epic Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e9957997-8b85-48a0-9bb3-b878cb223236) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

