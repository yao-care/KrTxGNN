---
layout: default
title: Bedaquiline
parent: 모델 예측만 (L5)
nav_order: 130
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Bedaquiline: 예측 신규 적응증 비활동성 결핵 (Inactive Tuberculosis) (근거 수준 L5). 기존 적응증: 허가증 원문 확인 불가 (허가 적응증 텍스트가 링크로만 제공됨)"
monitor_inn: "Bedaquiline"
predicted_indications: ["vulvovaginal candidiasis", "fascioliasis", "urea cycle disorder", "esophageal candidiasis"]
---

# Bedaquiline
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

## Bedaquiline: 다제내성 결핵에서 잠복 결핵(비활동성 결핵)으로
{: .text-alpha }

## 한 문장 요약

Bedaquiline은 한국에서 서튜러정(Sirturo)으로 허가된 항결핵제입니다. 허가증에 연결된 적응증 정보는 링크 형태로만 제공되어 구체적인 문구는 확인할 수 없었습니다.
TxGNN 모델은 **비활동성 결핵(Inactive Tuberculosis)**에 효과가 있을 수 있다고 예측하며, 현재 **3건의 임상시험**과 **20편의 문헌**이 이 방향과 관련되어 있습니다. 다만 완료된 임상시험 결과는 없습니다.

> 참고: 이 보고서는 예측 순위 1위(소 결핵)가 아니라, 근거가 가장 충실한 4위 예측(비활동성 결핵)을 중심으로 작성했습니다. 1위는 근거가 체외 시험 논문 1편뿐이어서 평가 보류 상태입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가증 원문 확인 불가 (허가 적응증 텍스트가 링크로만 제공됨) |
| 예측 신규 적응증 | 비활동성 결핵 (Inactive Tuberculosis) |
| TxGNN 예측 점수 | 99.96% |
| 근거 수준 | L5 (완료된 Phase 2/3 RCT 없음, 모델 예측과 진행 중인 시험만 존재) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | Proceed with Guardrails (조건부 진행) |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 없습니다. 다만 수집된 문헌에 따르면 bedaquiline은 결핵균의 F-ATP 합성효소(c 소단위, AtpE)를 억제하는 항결핵제입니다. 이 효소는 세균의 에너지 생성에 필수적입니다.

비활동성(잠복) 결핵은 증식하지 않고 휴면 상태인 결핵균이 몸속에 남아 있는 상태입니다. Bedaquiline은 에너지 대사에 의존하는 비증식 균에도 작용할 수 있어 예방 치료에 적용될 가능성이 있습니다. 특히 표준 예방 요법이 듣지 않는 다제내성·리팜핀 내성 결핵 접촉자에게 의미가 있을 수 있습니다.

다만 수집된 문헌 대부분은 일반 결핵 총설이며, bedaquiline의 예방 효과를 직접 입증한 완료된 시험은 아직 없습니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT06568484](https://clinicaltrials.gov/study/NCT06568484) | Phase 2/3 | 모집 중 | 2,530 | HIV 감염자 및 고위험 접촉자에서 4주 bedaquiline과 표준 요법의 결핵 예방 효과 비열등성 비교 (결과 미발표) |
| [NCT05766267](https://clinicaltrials.gov/study/NCT05766267) | Phase 2/3 | 활성, 모집 종료 | 288 | 폐결핵에서 17주 단기 요법(bedaquiline+moxifloxacin+pyrazinamide 기반)과 표준 6개월 요법 비교. 활동성 결핵 대상이라 간접 근거 |
| [NCT07069582](https://clinicaltrials.gov/study/NCT07069582) | Phase 1 | 모집 예정 | 60 | 수유부에서 bedaquiline 등 항결핵제의 혈장 및 모유 약동학. 효능이 아닌 노출 정보 |

## 문헌 근거

대부분 총설이며 bedaquiline의 예방 효과를 직접 검증한 연구는 없습니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [28625141](https://pubmed.ncbi.nlm.nih.gov/28625141/) | 2018 | Review | Recent Pat Antiinfect Drug Discov | Bedaquiline이 더 짧고 나은 항결핵 요법으로 기대됨 |
| [39766559](https://pubmed.ncbi.nlm.nih.gov/39766559/) | 2024 | Review | Antibiotics (Basel) | 결핵균 F-ATP 합성효소 억제제와 표적 정리 |
| [36915977](https://pubmed.ncbi.nlm.nih.gov/36915977/) | 2022 | 총설 | Zhejiang Da Xue Xue Bao Yi Xue Ban | 잠복 결핵 감염의 진단 및 치료 진展 |
| [39887565](https://pubmed.ncbi.nlm.nih.gov/39887565/) | 2025 | Review | Respirology | 결핵은 잠복·활동성의 이분법이 아닌 질환 스펙트럼이며 무증상 결핵도 전파에 기여 |
| [33837535](https://pubmed.ncbi.nlm.nih.gov/33837535/) | 2021 | Review | Clin Pharmacol Ther | 잠복 결핵과 활동성 결핵의 치료 및 항결핵제 특성 |
| [36982277](https://pubmed.ncbi.nlm.nih.gov/36982277/) | 2023 | Review | Int J Mol Sci | 결핵의 병인, 현행 치료 요법, 신약 표적 |
| [38003836](https://pubmed.ncbi.nlm.nih.gov/38003836/) | 2023 | 총설 | Pathogens | 소아 약제내성 결핵의 관리와 예방 전망, bedaquiline·delamanid 포함 |
| [39301910](https://pubmed.ncbi.nlm.nih.gov/39301910/) | 2025 | 총설 | Infect Disord Drug Targets | Bedaquiline 기반 전달 시스템, 휴면 균에 대한 표적 가능성 |
| [28776518](https://pubmed.ncbi.nlm.nih.gov/28776518/) | 2017 | 총설 | Int J Mycobacteriol | 비증식 결핵균을 표적으로 하는 약물 |
| [29580819](https://pubmed.ncbi.nlm.nih.gov/29580819/) | 2018 | 총설 | Lancet Infect Dis | 결핵 신약, 치료 요법, 숙주 표적 치료의 발전 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201401310 | 서튜러정100밀리그램 (베다퀼린푸마르산염), (주)한국얀센 | 흰색 내지 거의 흰색의 양면이 볼록한 원형 정제 | 허가사항 문서 참조 (텍스트 미확인) |

## 세포독성

해당 없음 (항종양약이 아님).

## 안전성 고려사항

- **약물 상호작용**: 데이터에 100건의 상호작용이 있으며, 주요(Major) 등급은 다음과 같습니다.
  - Dexamethasone
  - Clarithromycin
  - Picosulfuric acid
  - Polyethylene glycol (3350, 전해질 포함)
  - Dolasetron
  - Palonosetron
  - Sodium sulfate
  - 그 외 중등도(Moderate) 상호작용은 Acarbose, Famotidine, Doxycycline, Pioglitazone, Loperamide, Bupropion 등이 있습니다.
- **주의 사항(재창출 평가 시 고려)**: QT 연장 위험, CYP3A4 유도제·억제제 및 다른 QT 연장 약물과의 병용, 간독성 모니터링이 필요합니다. 무증상 대상인 예방 치료에서는 안전 여유가 더 좁습니다.

허가사항의 경고 및 금기 정보는 데이터를 확보하지 못했으므로 허가사항 원문을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
비활동성 결핵은 bedaquiline의 기전과 가장 잘 부합하며, 예방 효과를 직접 검증하는 대규모 Phase 2/3 시험(BREACH-TB, 2,530명)이 진행 중입니다. 그러나 완료된 시험 결과가 없고 안전성 정보(허가사항)도 확인되지 않아, 근거 수준은 L5입니다. QT 연장, 약물 상호작용, 간독성을 관리하는 조건하에서만 진행해야 합니다.

**진행하려면 필요한 것:**
- 허가사항 원문(경고, 금기, 적응증) 확보 및 분석
- 작용 기전 데이터 보완 (DrugBank 조회)
- BREACH-TB(NCT06568484) 결과 확인
- 무증상 대상 예방 치료에서의 QT 연장·간독성 모니터링 계획 수립
- 주요 상호작용 약물(clarithromycin, dexamethasone 등) 병용 관리 방안

**기타 예측 신규 적응증 (참고)**

| 순위 | 질환 | 근거 수준 | 비고 |
|-----|------|----------|------|
| 1 | 소 결핵 | L4 | 체외 MIC 시험 논문 1편뿐, 임상 자료 없음 (Hold) |
| 2 | 결핵종 | L4 | 약제내성 결핵에서의 증례 보고 중심. CNS 침투가 한계 (연구 질문 단계) |
| 3 | 결핵성 복수 | L4 | 항결핵제 간손상 증례만 있어 간접 근거 (Hold) |
| 5 | 조류 결핵 | L5 | 예측 점수만 있음 (Hold) |
| 6, 10 | 외음질 칸디다증, 식도 칸디다증 | L5 | 기전 연결 없음, 모델 인공물 가능성 (Hold) |
| 7 | 간질증 | L5 | 기전 연결 없음, 기존 치료제 있음 (Hold) |
| 8 | 요소회로 장애 | L5 | 기전 연결 없음, 간독성 우려 (Hold) |
| 9 | 피부 결핵 | L4 | 검색된 문헌은 항결핵제 피부 부작용 보고로 효능과 무관 (Hold) |
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

