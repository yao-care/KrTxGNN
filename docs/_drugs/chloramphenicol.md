---
layout: default
title: Chloramphenicol
parent: 모델 예측만 (L5)
nav_order: 205
evidence_level: L5
indication_count: 8
monitor_inn: "CHLORAMPHENICOL"
predicted_indications: ["diffuse scleroderma", "postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "infective urethral stricture", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome", "punctate epithelial keratoconjunctivitis"]
last_modified_at: 2026-10-31
description: "Chloramphenicol: 예측 신규 적응증 미만성 피부경화증 (diffuse scleroderma) (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201501443/EE"
---

# Chloramphenicol
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **8** 건
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

## Chloramphenicol: 항균제(단백질 합성 억제) → 미만성 피부경화증 (diffuse scleroderma)
{: .text-alpha }

## 한 문장 요약

Chloramphenicol은 광범위 항균제로, 한국에서는 점안액(수출용) 제품으로 허가되어 있습니다.
TxGNN 모델은 **미만성 피부경화증(diffuse scleroderma)**에 효과가 있을 수 있다고 예측하지만, 이 질환에 대한 임상시험은 없고 문헌 4편은 모두 피부경화증 섬유아세포를 다룬 기초 연구로 chloramphenicol을 직접 검증하지 않았습니다.
따라서 현재는 모델 예측 수준의 근거에 머물러 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201501443/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199301046/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201001531/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199403384/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199202903/EE |
| 예측 신규 적응증 | 미만성 피부경화증 (diffuse scleroderma) |
| TxGNN 예측 점수 | 0.9965 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 5건 / 전체 5건) |
| 허가증 수 | 5건 (유효 5건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 일반적으로 chloramphenicol은 세균의 단백질 합성을 억제하는 항균제로 알려져 있으나, 이 보고서에 정리된 자료에서는 확인되지 않았습니다.

검색된 문헌 4편(1996~2006년)은 피부경화증 섬유아세포에서의 콜라겐 유전자 조절(α1(I) 프로콜라겐 프로모터, Smad3/Sp1/p300, TGF-β 신호)을 다룹니다. 이 연구들은 chloramphenicol을 시험하지 않았습니다. 미토콘드리아 단백질 합성 억제가 섬유아세포 활동에 영향을 줄 수 있다는 추정은 가능하지만 이를 뒷받침하는 자료는 없는 가설 단계입니다.

## 문헌 근거

이 질환을 직접 연구한 임상시험은 없습니다. 아래 문헌은 모두 기초 연구(시험관 내)이며 chloramphenicol의 효능을 평가한 것이 아닙니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [11229480](https://pubmed.ncbi.nlm.nih.gov/11229480/) | 2001 | 기초 연구 | Arthritis Rheum | 내인성 TGF-β 신호 차단이 피부경화증 섬유아세포의 콜라겐 합성 증가를 억제 |
| [16319104](https://pubmed.ncbi.nlm.nih.gov/16319104/) | 2006 | 기초 연구 | Rheumatology (Oxford) | 인산화된 Smad3가 Sp1, p300과 상호작용하여 콜라겐 발현에 관여 |
| [9811061](https://pubmed.ncbi.nlm.nih.gov/9811061/) | 1998 | 기초 연구 | Arthritis Rheum | α1(I) 프로콜라겐 프로모터의 조절 요소와 전사인자 규명 |
| [8702443](https://pubmed.ncbi.nlm.nih.gov/8702443/) | 1996 | 기초 연구 | Arthritis Rheum | 미만성 전신 경화증 섬유아세포에서 COL1A1 전사 조절과 인트론 서열의 역할 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201501443 | 클리어에프점안액(수출용) | 점안액 | 적응증 텍스트 미기재 |
| 199301046 | 신폴점안액(수출용) | 점안액 | 적응증 텍스트 미기재 |
| 201001531 | 쿠이로점안액(수출용) | 점안액 | 적응증 텍스트 미기재 |
| 199403384 | 다클점안액(수출용) | 점안액 | 적응증 텍스트 미기재 |
| 199202903 | 참클로람페니콜점안액 | 점안액 | 적응증 텍스트 미기재 |

## 안전성 고려사항

- **약물 상호작용**: 중대(Major) 수준으로 cisapride, naloxegol이 확인되었습니다. 중등도(Moderate) 수준으로는 metronidazole, 설포닐우레아계 혈당강하제(glipizide, glimepiride, glyburide, chlorpropamide, acetohexamide), repaglinide, simvastatin, rosuvastatin, saxagliptin, budesonide, aprepitant, 철분 등이 있습니다. 조회된 상호작용은 총 100건이며 이 중 일부만 나열했습니다.
- **주의가 필요한 질환(참고)**: 신장 질환, 간 질환, 혈소판감소증, 빈혈, 무과립구증, 호중구감소증, 재생불량성 빈혈, 말초신경병증, 시신경염, 급성 간헐성 포르피린증, 발작성 야간 혈색소뇨증 등에서 주의가 필요한 것으로 확인되었으나, 이는 허가 문서의 기재 내용이 아닙니다.
- 특히 골수 독성(재생불량성 빈혈)은 만성 섬유성 질환에 사용하기에 큰 안전성 장벽입니다.

허가사항의 경고 및 금기 정보는 이번 자료에서 확보되지 않았으므로 허가사항을 직접 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
미만성 피부경화증을 직접 다룬 임상시험이나 chloramphenicol 투여 연구가 없고, 모델 점수(0.9965)만 근거로 남아 있습니다. 골수 독성이라는 안전성 문제도 만성 질환 적용에 큰 걸림돌입니다.

**진행하려면 필요한 것:**
- chloramphenicol의 작용 기전(MOA) 자료 확보 및 섬유화 관련 기전 연결 검증
- 섬유아세포 모델 등 전임상 연구를 통한 효과 확인
- 허가 문서의 경고·금기 사항 확보 및 골수 독성 위험-이익 평가
- 한국 허가 제품이 모두 점안액(수출용)이므로, 전신 투여가 필요한 경우 투여 경로 적합성 검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

