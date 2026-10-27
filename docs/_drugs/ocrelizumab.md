---
layout: default
title: Ocrelizumab
parent: 모델 예측만 (L5)
nav_order: 558
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Ocrelizumab: 예측 신규 적응증 HER2 양성 유방암 (HER2 positive breast carcinoma) (근거 수준 L5). 기존 적응증: 다발성 경화증 (허가 적응증 텍스트는 링크로만 제공되어 문헌 기준으로 판단)"
monitor_inn: "OCRELIZUMAB"
predicted_indications: ["HER2 positive breast carcinoma", "progesterone-receptor positive breast cancer", "normal breast-like subtype of breast carcinoma", "breast tumor luminal A or B", "progesterone-receptor negative breast cancer"]
---

# Ocrelizumab
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

## Ocrelizumab: 다발성 경화증에서 HER2 양성 유방암으로
{: .text-alpha }

## 한 문장 요약

Ocrelizumab은 항CD20 단클론항체로, 한국에서 허가된 제품(오크레부스주, 오크레부스피하주사)이 시판 중입니다. 다만 허가 적응증 원문은 데이터에 텍스트로 수록되어 있지 않으며, 제공된 문헌은 모두 다발성 경화증을 다루고 있어 이를 기존 적응증으로 보았습니다.
TxGNN 모델은 **HER2 양성 유방암(HER2 positive breast carcinoma)**에 효과가 있을 수 있다고 예측하지만, 이를 뒷받침하는 **임상시험은 0건**, **직접 관련 문헌도 0편**입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 다발성 경화증 (허가 적응증 텍스트는 링크로만 제공되어 문헌 기준으로 판단) |
| 예측 신규 적응증 | HER2 양성 유방암 (HER2 positive breast carcinoma) |
| TxGNN 예측 점수 | 99.89% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 2건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Ocrelizumab은 CD20을 발현하는 B세포를 선택적으로 제거하는 인간화 단클론항체이며, 다발성 경화증 치료에 사용됩니다.

HER2 기반 종양 생물학과 CD20 표적 B세포 제거 사이에 직접적인 기전적 연관성은 확인되지 않습니다. 0.999라는 매우 높은 점수는 모델 예측일 뿐이며, 임상시험이나 문헌으로 뒷받침되지 않습니다.

같은 유방암 계열의 다른 예측(프로게스테론 수용체 양성/음성, 정상 유방 유사형, 루미널 A/B)도 점수가 0.998 수준으로 거의 같습니다. 이는 모델이 약물 고유의 신호가 아니라 유방암 질환군이 공유하는 그래프 구조를 반영했을 가능성을 시사합니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

HER2 양성 유방암에 대해 직접 관련된 문헌은 없습니다. 참고로, 다른 유방암 하위 유형(루미널 A/B) 예측 항목에 연결된 문헌 18편 중 10편이 제시되었으나, 모두 다발성 경화증, 전신 홍반성 루푸스, 이차성 저감마글로불린혈증 등을 다루며 유방암과는 무관합니다. 대표적인 문헌은 다음과 같습니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [28002688](https://pubmed.ncbi.nlm.nih.gov/28002688/) | 2017 | RCT | N Engl J Med | 원발진행형 다발성 경화증에서 ocrelizumab과 위약 비교 |
| [28002679](https://pubmed.ncbi.nlm.nih.gov/28002679/) | 2017 | RCT | N Engl J Med | 재발형 다발성 경화증에서 ocrelizumab과 interferon beta-1a 비교 |
| [40245351](https://pubmed.ncbi.nlm.nih.gov/40245351/) | 2025 | RCT | Neurology | 피하 투여 ocrelizumab의 약물 노출 비열등성 평가(OCARINA II) |
| [35192158](https://pubmed.ncbi.nlm.nih.gov/35192158/) | 2022 | Review | Drugs | 다발성 경화증에서의 ocrelizumab 종합 고찰 |
| [37033984](https://pubmed.ncbi.nlm.nih.gov/37033984/) | 2023 | Review | Front Immunol | 다발성 경화증의 항CD20 치료: 병리에서 임상까지 |

이 문헌들은 이미 허가된 다발성 경화증 사용만을 뒷받침하며, 유방암 적응증의 근거가 되지 않습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202401165 | 오크레부스주(오크렐리주맙) | 바이알 주사제 | 허가 문서 링크로만 제공되어 요약 불가 |
| 202503294 | 오크레부스피하주사(오크렐리주맙) | 바이알 주사제 | 허가 문서 링크로만 제공되어 요약 불가 |

두 제품 모두 (주)한국로슈가 보유한 단일 성분 제제이며 현재 유효합니다.

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 면역치료 (항CD20 단클론항체, 전통적 세포독성 화학요법제 아님) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 취급 방호 | 허가사항의 경고 및 주의사항을 참조하세요 |

## 안전성 고려사항

- **약물 상호작용**: 데이터에서 100건이 확인되었으며, 일부를 제시합니다.
  - 중등도: 코르티코스테로이드 계열(hydrocortisone, prednisolone, prednisone, dexamethasone, triamcinolone, betamethasone, budesonide), 방사성의약품(ibritumomab tiuxetan, iobenguane I-131, tositumomab, samarium lexidronam), albendazole, pentamidine, levamisole
  - 경미: 아연 제제(zinc sulfate, acetate, gluconate, chloride)
- 참고로 문헌에서는 항CD20 치료 후 이차성 저감마글로불린혈증과 감염 위험이 논의되고 있습니다.

주요 경고와 금기는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 점수는 매우 높지만 임상시험과 직접 관련 문헌이 없고 기전적 연결 고리도 확인되지 않아 모델 예측만 존재하는 L5 단계입니다. 안전성 검토에 필요한 허가사항의 경고·금기 정보도 확보되지 않았습니다.

**진행하려면 필요한 것:**
- 한국 식약처(MFDS) 허가사항 PDF에서 경고·금기 및 허가 적응증 확보 (안전성 선별의 필수 선행 조건)
- DrugBank에서 작용 기전(MOA) 데이터 확보
- HER2 양성 유방암에서 CD20 B세포 표적 가능성을 뒷받침하는 전임상·기전 연구 탐색
- 유방암과 직접 관련된 문헌 및 임상시험 재검색 (현재 문헌은 약물명 기반으로 수집된 것으로 보임)
- 유방암 하위 유형 간 점수가 거의 같은 현상이 모델 아티팩트인지 검증
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

