---
layout: default
title: Dupilumab
parent: 모델 예측만 (L5)
nav_order: 294
evidence_level: L5
indication_count: 9
monitor_inn: "DUPILUMAB"
predicted_indications: ["bronchitis", "acne keloid", "exanthem (disease)", "neonatal dermatomyositis", "acrodermatitis chronica atrophicans", "amyopathic dermatomyositis", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "hydroa vacciniforme, familial", "severe nonproliferative diabetic retinopathy"]
last_modified_at: 2026-10-31
description: "Dupilumab: 예측 신규 적응증 기관지염 (bronchitis) (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202202110/EE"
---

# Dupilumab
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

## Dupilumab: 항IL-4Rα 단클론항체 → 기관지염 (bronchitis)
{: .text-alpha }

## 한 문장 요약

Dupilumab은 IL-4 수용체 알파(IL-4Rα)를 차단하는 단클론항체입니다.
TxGNN 모델은 **기관지염(bronchitis)**에 효과가 있을 수 있다고 예측하지만, 이 질환 자체를 직접 연구한 임상시험이나 문헌은 확인되지 않았습니다. 현재 관련 질환(만성 비용종 없는 부비동염, 천식, COPD)을 다룬 **1건의 임상시험**과 **11편의 문헌**이 간접적으로 참고됩니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202202110/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202003302/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202202109/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201801406/EE |
| 예측 신규 적응증 | 기관지염 (bronchitis) |
| TxGNN 예측 점수 | 0.9992 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 4건 / 전체 4건) |
| 허가증 수 | 4건 (유효 4건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 수집되지 않았습니다. 다만 Dupilumab은 IL-4Rα를 차단하여 IL-4/IL-13 신호를 억제하는 약물로 알려져 있으며, 이는 2형 기도 염증(호산구 증가, 점액 과분비, 기도 재형성)과 관련이 있습니다.

따라서 2형 염증이 주도하는 기도 질환, 예를 들어 만성 기관지염 표현형의 2형 COPD나 호산구성 플라스틱 기관지염에는 기전상 적용 가능성이 있습니다. 그러나 "기관지염"이라는 명칭은 범위가 넓고, 현재 근거는 2형 염증 하위군에만 해당합니다. 감염성 또는 급성 기관지염에 대한 근거는 없습니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT04362501](https://clinicaltrials.gov/study/NCT04362501) | Phase 2 | 완료 | 33 | 비용종 없는 만성 부비동염에서 Dupilumab 효능을 평가한 무작위 이중맹검 위약대조 시험. 기관지염이 아닌 관련 2형 상기도 질환이므로 간접 근거에 그침 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [34597534](https://pubmed.ncbi.nlm.nih.gov/34597534/) | 2022 | RCT (장기 연장) | Lancet Respir Med | 중등도~중증 천식에서 Dupilumab의 장기 안전성 및 효능 평가 (TRAVERSE) |
| [30273510](https://pubmed.ncbi.nlm.nih.gov/30273510/) | 2019 | 메타분석 | J Asthma | 조절되지 않는 천식에서 Dupilumab의 안전성과 효능을 RCT 메타분석으로 평가 |
| [39904363](https://pubmed.ncbi.nlm.nih.gov/39904363/) | 2025 | 체계적 문헌고찰 | Tuberc Respir Dis | COPD 악화 예방을 위한 약물 치료 종합 검토 |
| [42617837](https://pubmed.ncbi.nlm.nih.gov/42617837/) | 2026 | 비교 분석 | Chest | 호산구성 COPD에서 Mepolizumab과 Dupilumab의 악화 감소 효과에 유의한 차이 없음 |
| [42839285](https://pubmed.ncbi.nlm.nih.gov/42839285/) | 2026 | 실제 임상 코호트 | Respir Res | 독일 다기관 분석으로 COPD에서 Dupilumab의 실제 임상 효과 평가 |
| [42511891](https://pubmed.ncbi.nlm.nih.gov/42511891/) | 2026 | 실제 임상 증례군 | Biomedicines | 만성 기관지염 표현형이 두드러진 2형 COPD 12명에서 Dupilumab 사용 경험 |
| [42773542](https://pubmed.ncbi.nlm.nih.gov/42773542/) | 2026 | 리뷰 | Eur J Clin Invest | COPD 관리의 염증 경로 기반 표적 치료 최신 동향 |
| [38488768](https://pubmed.ncbi.nlm.nih.gov/38488768/) | 2024 | 리뷰 | Pediatr Pulmonol | 호산구성 소아 플라스틱 기관지염의 새로운 치료법 |
| [41672525](https://pubmed.ncbi.nlm.nih.gov/41672525/) | 2026 | 증례 보고 | Intern Med | 호산구성 세기관지염 2례에서 생물학적 제제(Dupilumab 포함) 치료 성공 |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | 리뷰 | Expert Opin Pharmacother | 흡연 유발 기도 질환을 동반한 천식 관리의 어려움 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202202110 | 듀피젠트프리필드펜300밀리그램 | 프리필드 펜 주사제 | 허가 문서 링크만 제공되어 적응증 텍스트 확인 불가 |
| 202003302 | 듀피젠트프리필드주200밀리그램 | 프리필드시린지 주사제 | 허가 문서 링크만 제공되어 적응증 텍스트 확인 불가 |
| 202202109 | 듀피젠트프리필드펜200밀리그램 | 프리필드 펜 주사제 | 허가 문서 링크만 제공되어 적응증 텍스트 확인 불가 |
| 201801406 | 듀피젠트프리필드주300밀리그램 | 프리필드시린지 주사제 | 허가 문서 링크만 제공되어 적응증 텍스트 확인 불가 |

## 안전성 고려사항

- **약물 상호작용**: 수집된 데이터에서 53건의 상호작용이 확인되었습니다. 주요(Major) 등급은 Adalimumab, Baricitinib, Certolizumab pegol, Cladribine 등이며, 중등도(Moderate) 등급은 Warfarin, Roflumilast, Cyclosporine, Azathioprine, Denosumab 등입니다. 아연 제제(아세트산아연, 글루콘산아연, 황산아연, 염화아연)는 경미한(Minor) 등급입니다.

경고 및 금기 등 그 밖의 안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
기관지염 자체를 직접 연구한 임상시험이나 문헌이 없고, 현재 근거는 천식, COPD, 상기도 질환 등 관련 질환에 한정되어 근거 수준은 L5입니다. 근거는 2형 염증 하위군에만 해당하며, 감염성 또는 급성 기관지염에는 적용할 수 없습니다.

**진행하려면 필요한 것:**
- 2형 염증 표현형(호산구 증가 등)을 가진 만성 기관지염 환자를 직접 대상으로 한 임상 근거
- 대상 환자군(기관지염의 하위 유형)의 명확한 정의
- 허가사항의 경고·금기 정보 확보 및 안전성 검토
- 작용 기전 데이터의 보완
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

