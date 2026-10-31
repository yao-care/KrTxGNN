---
layout: default
title: Diazepam
parent: 모델 예측만 (L5)
nav_order: 275
evidence_level: L5
indication_count: 10
monitor_inn: "Diazepam"
predicted_indications: ["insomnia (disease)", "cauda equina syndrome", "sleep disorder, initiating and maintaining sleep", "attention deficit hyperactivity disorder, inattentive type", "barbiturate abuse", "antidepressant type abuse", "hallucinogen abuse", "specific developmental disorder", "attention deficit-hyperactivity disorder", "obsolete neurogenic bladder (disease)"]
last_modified_at: 2026-10-31
description: "Diazepam: 예측 신규 적응증 불면증 (근거 수준 L5). 기존 적응증: 확인 불가 (허가 적응증 본문이 링크로만 제공되어 내용을 확인할 수 없음)"
---

# Diazepam
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

## Diazepam: 기존 허가 적응증에서 불면증으로
{: .text-alpha }

## 한 문장 요약

Diazepam은 한국에서 단일 성분제로 8건의 허가증이 등록된 벤조디아제핀계 약물입니다. 다만 허가 적응증 본문은 이번 데이터에 담겨 있지 않아 기존 적응증을 확인할 수 없습니다.
TxGNN 모델은 **불면증(insomnia)**에 효과가 있을 수 있다고 예측합니다. 불면증을 직접 다룬 임상시험 등록은 없고, 문헌은 간접 근거 위주이므로 **근거 수준은 L5**입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (허가 적응증 본문이 링크로만 제공되어 내용을 확인할 수 없음) |
| 예측 신규 적응증 | 불면증 |
| TxGNN 예측 점수 | 0.9999 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 8건 / 전체 8건) |
| 허가증 수 | 8건 (유효 8건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 다만 검토된 문헌에 따르면 diazepam은 GABA-A 수용체의 벤조디아제핀 결합 부위에 작용하는 양성 알로스테릭 조절제로, 억제성 신경전달을 강화해 진정·수면 유도 효과를 냅니다. 이는 수면 유도에 있어 기전적으로 그럴듯합니다.

다만 벤조디아제핀류는 이미 단기 불면증에 임상적으로 사용되고 있어, 진정한 의미의 재창출보다는 기존 사용에 가깝습니다. 그리고 이번에 정리된 자료에는 불면증에서 diazepam 자체의 효능을 입증하는 최신 직접 근거가 없습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

불면증과 diazepam을 직접 다룬 문헌은 1981년 이중맹검 비교 연구가 유일하며, 나머지는 리뷰, 기전·동물 연구, 처방 양상 연구 등 간접 근거입니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [6113175](https://pubmed.ncbi.nlm.nih.gov/6113175/) | 1981 | 이중맹검 비교 연구 | J Int Med Res | 불면증 외래환자 100명에서 lormetazepam 1mg이 diazepam 5mg보다 입면 시간 단축과 수면 지속 면에서 우수 |
| [39581171](https://pubmed.ncbi.nlm.nih.gov/39581171/) | 2024 | Review | Bioorg Chem | GABA-A 수용체 조절제(diazepam 포함)의 신경계 질환 임상 적용 고찰 |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | Review | Expert Opin Drug Metab Toxicol | 항불안제의 약동학 고찰 |
| [31770357](https://pubmed.ncbi.nlm.nih.gov/31770357/) | 2019 | Review | Med Lett Drugs Ther | 대마 및 카나비노이드 개요 |
| [36692463](https://pubmed.ncbi.nlm.nih.gov/36692463/) | 2023 | 메타분석 | Acta Pharm | 만성 비전염성 질환 노인의 진정제 사용 효과와 안전성 |
| [40583063](https://pubmed.ncbi.nlm.nih.gov/40583063/) | 2025 | 코호트 | Cell Mol Biol Lett | 벤조디아제핀·Z-drug 장기 사용이 유방암을 악화시킬 수 있다는 임상·분자 근거 |
| [32623439](https://pubmed.ncbi.nlm.nih.gov/32623439/) | 2020 | 동물 연구 | Med Sci Monit | 불면 쥐 모델에서 berberine 효과 평가 (diazepam은 대조약) |
| [37776625](https://pubmed.ncbi.nlm.nih.gov/37776625/) | 2023 | 동물 연구 | J Pharm Biomed Anal | 불면 쥐 모델에서 Naoling Pian 평가 (diazepam은 양성 대조약) |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 198501812 | 명인디아제팜정5밀리그램 | 정제 | 허가 적응증 본문 확인 불가 |
| 198501813 | 명인디아제팜정10밀리그램 | 정제 | 허가 적응증 본문 확인 불가 |
| 197900546 | 삼진디아제팜주 | 앰플 주사제 | 허가 적응증 본문 확인 불가 |
| 197700525 | 대원디아제팜정2밀리그램 | 정제 | 허가 적응증 본문 확인 불가 |
| 197700535 | 삼진디아제팜정2밀리그람 | 정제 | 허가 적응증 본문 확인 불가 |

허가증은 총 8건이며 모두 단일 성분제로 유효 상태입니다. 위 표에는 그중 5건만 실었습니다. 나머지는 명인디아제팜정2밀리그램(198501811), 삼진디아제팜정5밀리그람(197700536), 바리움정5밀리그람(200700501)입니다.

## 안전성 고려사항

- **약물 상호작용**: 이번 조회에서 총 100건이 확인되었습니다. 주요 항목은 다음과 같습니다.
  - 주의 필요(Major): Morphine
  - 중등도(Moderate): Bupropion, Aprepitant, Omeprazole, Cimetidine, Clarithromycin, Cisapride, Clotrimazole, Dronabinol, Esomeprazole, Metoclopramide, Miconazole
  - 경미(Minor): Dexamethasone, Betamethasone, 제산제(수산화마그네슘, 수산화알루미늄, 탄산칼슘 등)
- **문헌에서 확인된 일반 우려**: 벤조디아제핀 장기 사용 시 의존성, 인지 저하, 낙상 위험, 수면 구조 변화(서파수면·REM 수면 억제) 등이 보고됩니다. 이는 클래스 전반의 정보이며 허가사항 확인이 필요합니다.

경고 및 금기 사항은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 불면증은 TxGNN 점수가 매우 높지만, 임상시험 등록이 없고 diazepam을 직접 다룬 근거는 1981년 비교 연구 1건뿐입니다. 이 때문에 근거 수준은 L5입니다.
- 벤조디아제핀은 이미 단기 불면증에 쓰이고 있어 새로운 재창출 가치가 제한적이며, 의존성 등 안전성 부담도 있습니다.

**진행하려면 필요한 것:**
- 8건 허가증의 허가 적응증 본문 확보 (불면증이 이미 허가 범위에 포함되는지 확인)
- 허가사항의 경고·금기 정보 확보
- 작용 기전(MOA) 데이터 보완
- 불면증에서 diazepam 자체의 효능·안전성을 직접 평가한 최신 연구 확인
- 시판 현황(취소 여부) 확인

## 참고: 기타 예측 적응증

상위 10개 예측 중 불면증 외에는 근거가 더 약합니다. 수면 개시·유지 장애는 불면증과 겹치며 간접 문헌뿐입니다. 마비 관련 질환(마미 증후군), 주의력결핍 과잉행동장애(두 항목), 신경인성 방광은 문헌이 없거나 부정적 안전 신호만 있습니다. 약물 남용 관련 항목(바르비투르산염, 항우울제, 환각제)은 간접 문헌뿐이며 diazepam 자체의 남용 가능성이 문제입니다. 모두 Hold 권장입니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

