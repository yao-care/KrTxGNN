---
layout: default
title: Capecitabine
parent: 모델 예측만 (L5)
nav_order: 177
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Capecitabine: 예측 신규 적응증 위 선암 및 위 근위부 용종증 (gastric adenocarcinoma and proximal polyposis of th… (근거 수준 L5). 기존 적응증: 허가증에 적응증 원문이 포함되어 있지 않아 확인할 수 없음 (허가 문서 링크만 제공됨)"
monitor_inn: "Capecitabine"
predicted_indications: ["gastric adenocarcinoma and proximal polyposis of the stomach", "gastric tubular adenocarcinoma", "signet ring cell gastric adenocarcinoma", "gastric cardia adenocarcinoma"]
---

# Capecitabine
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

# Capecitabine: 위암에서 위 선암(관상 선암)으로

## 한 문장 요약

Capecitabine은 5-FU로 전환되는 경구 플루오로피리미딘 전구약물로, 한국에서 허가받아 항암 치료에 사용되고 있습니다.
TxGNN 모델은 **위 선암 및 위 관련 하위 유형**에 효과가 있을 수 있다고 예측하며, 가장 근거가 풍부한 **위 관상 선암(Gastric tubular adenocarcinoma)**에는 **20편의 문헌**(대부분 3상 RCT)이 연결되어 있습니다.
다만 이 예측은 사실상 기존 위암 적응증의 연장선이며, 일부 희귀 하위 유형은 근거가 전혀 없습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가증에 적응증 원문이 포함되어 있지 않아 확인할 수 없음 (허가 문서 링크만 제공됨) |
| 예측 신규 적응증 | 위 선암 및 위 근위부 용종증 (gastric adenocarcinoma and proximal polyposis of the stomach) — 1순위 예측 |
| TxGNN 예측 점수 | 99.94% (1순위 기준) |
| 근거 수준 | L5 (1순위 기준). 관상 선암 L1, 분문부 선암 L2 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 7건 (모두 유효, 단일제) |
| 권장 결정 | Hold (1순위 기준). 관상 선암·위체부 암은 Proceed with Guardrails |

> 1순위 예측은 희귀 증후군(GAPPS)으로 임상시험과 문헌이 모두 없습니다. 이 때문에 아래 근거 표는 근거가 가장 풍부한 2순위(위 관상 선암)를 중심으로 정리하고, 다른 하위 유형은 요약으로 비교했습니다.

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Capecitabine은 체내에서 5-FU로 전환되는 플루오로피리미딘 전구약물이며, 5-FU는 티미딜레이트 합성효소(thymidylate synthase)를 억제해 DNA 합성을 막습니다. 이 기전은 위 선암에서 확립되어 있어, 위 선암의 하위 유형에도 적용 가능할 수 있습니다.

관상 선암은 위 선암에서 가장 흔한 조직형입니다. Capecitabine은 CAPOX(capecitabine + oxaliplatin) 요법의 핵심 성분으로 보조요법과 1차 요법에서 사용됩니다. 따라서 이 경우는 진정한 재창출이라기보다 기존 위암 적응증에 가까운 사용입니다.

반면 1순위인 GAPPS 증후군, 미세침윤성 위암, 악성 위 과립세포종은 직접 근거가 없습니다. 이들에 대한 예측은 위 선암에서의 효과를 외삽한 것입니다. 인상 세포(signet ring) 선암은 화학요법에 반응이 낮다고 보고되어, 하위 유형별 이점은 열린 질문입니다.

## 임상시험 근거

2순위(위 관상 선암)에는 등록된 임상시험이 없습니다. 아래는 다른 예측 질환에서 확인된 시험 중 관련성이 높은 것들입니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00040859](https://clinicaltrials.gov/study/NCT00040859) | Phase 2 | 완료 | 48 | 위 분문부·식도·위식도 접합부 전이성 선암에서 oxaliplatin + capecitabine 병용 평가 (분문부 선암) |
| [NCT00938470](https://clinicaltrials.gov/study/NCT00938470) | Phase 2 | 완료 | 73 | 국소 진행 식도·위식도 접합부 선암의 연장 선행요법, docetaxel·oxaliplatin·capecitabine 등 포함 (분문부 선암) |
| [NCT01295086](https://clinicaltrials.gov/study/NCT01295086) | NA | 완료 | 27 | HER2 양성 진행성 위식도암에서 docetaxel·oxaliplatin·capecitabine + trastuzumab의 최대 내약 용량 탐색 (분문부 선암) |
| [NCT02494583](https://clinicaltrials.gov/study/NCT02494583) | Phase 3 | 완료 | 763 | 진행성 위·위식도 접합부 선암 1차 치료, pembrolizumab ± 화학요법(cisplatin + 5-FU 또는 capecitabine) (위체부 암) |
| [NCT07091227](https://clinicaltrials.gov/study/NCT07091227) | Phase 2 | 모집 예정 | 66 | 인상세포 포함 위·위식도 접합부 선암의 선행요법으로 AK112 + 화학요법, capecitabine 포함 여부는 미확인 (인상세포 선암) |

> NCT02494583은 capecitabine이 선택 가능한 플루오로피리미딘 중 하나일 뿐이어서, capecitabine만의 기여는 분리할 수 없습니다. 나머지 시험은 초기 단계이거나 소규모입니다.

## 문헌 근거

2순위(위 관상 선암) 문헌 중 RCT를 우선하여 정리했습니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [22226517](https://pubmed.ncbi.nlm.nih.gov/22226517/) | 2012 | RCT (Phase 3) | Lancet | CLASSIC: D2 위절제술 후 capecitabine + oxaliplatin 보조요법의 무병생존 효과 평가 |
| [34252374](https://pubmed.ncbi.nlm.nih.gov/34252374/) | 2021 | RCT (Phase 3) | Lancet Oncol | RESOLVE: 주수술기·수술 후 SOX와 수술 후 CapOx 비교 |
| [39952264](https://pubmed.ncbi.nlm.nih.gov/39952264/) | 2025 | RCT (Phase 3) | Lancet Oncol | RESOLVE 최종 보고, 전체 생존 갱신 분석 |
| [34102137](https://pubmed.ncbi.nlm.nih.gov/34102137/) | 2021 | RCT (Phase 3) | Lancet | CheckMate 649: 진행성 위·식도 선암 1차 nivolumab + 화학요법 |
| [37875143](https://pubmed.ncbi.nlm.nih.gov/37875143/) | 2023 | RCT (Phase 3) | Lancet Oncol | KEYNOTE-859: HER2 음성 진행성 위암에서 pembrolizumab + 화학요법 |
| [37524953](https://pubmed.ncbi.nlm.nih.gov/37524953/) | 2023 | RCT (Phase 3) | Nat Med | GLOW: CLDN18.2 양성 위암에서 zolbetuximab + CAPOX |
| [38806195](https://pubmed.ncbi.nlm.nih.gov/38806195/) | 2024 | RCT (Phase 3) | BMJ | RATIONALE-305: 1차 tislelizumab + 화학요법 |
| [38051328](https://pubmed.ncbi.nlm.nih.gov/38051328/) | 2023 | RCT (Phase 3) | JAMA | ORIENT-16: 절제 불가 위·위식도 접합부암에서 sintilimab + 화학요법 |
| [39992668](https://pubmed.ncbi.nlm.nih.gov/39992668/) | 2025 | RCT (Phase 3) | JAMA | GEMSTONE-303: 진행성 위암 1차 sugemalimab + 화학요법 |
| [20728210](https://pubmed.ncbi.nlm.nih.gov/20728210/) | 2010 | RCT (Phase 3) | Lancet | ToGA: HER2 양성 진행성 위암에서 trastuzumab + 화학요법 |

> 이 중 CLASSIC과 RESOLVE의 CapOx군이 capecitabine을 직접 평가한 근거입니다. 나머지 3상 시험은 capecitabine이 화학요법 골격(backbone)의 일부이며, 이 약만의 효과를 입증한 것은 아닙니다. 관상 선암이라는 조직형 하위군 분석도 확인되지 않았습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200008797 | 젤로다정500밀리그램 (보령) | 미홍색의 타원형 필름코팅정 | 허가 문서 참조 (원문 텍스트 미제공) |
| 200008796 | 젤로다정150밀리그램 (보령) | 미홍색의 타원형 필름코팅정 | 허가 문서 참조 (원문 텍스트 미제공) |
| 201309043 | 젤로빅정500밀리그램 (일동제약) | 미홍색의 타원형 필름코팅정 | 허가 문서 참조 (원문 텍스트 미제공) |
| 201309978 | 젤로빅정150밀리그램 (일동제약) | 미홍색의 타원형 필름코팅정 | 허가 문서 참조 (원문 텍스트 미제공) |
| 201507291 | 잘보빈정500밀리그램 (알보젠코리아) | 분홍색의 장방형 필름코팅정 | 허가 문서 참조 (원문 텍스트 미제공) |

이 외에 젤타빈정(수출용, 한국유나이티드제약, 201200727)과 잘보빈정150밀리그램(알보젠코리아, 201602786)이 있어 총 7건이 모두 유효한 단일제입니다.

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 약물 (Fluoropyrimidine 계열, 5-FU 전구약물) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요. 질환-금기 관계 데이터에 호중구감소증, 혈소판감소증, 무과립구증, 빈혈이 포함되어 있어 혈액학적 독성에 유의해야 합니다. |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | CBC(분류 포함), 간기능, 신기능, 빌리루빈 |
| 취급 방호 | 세포독성 약물 취급 규정 준수 필요 |

## 안전성 고려사항

- **주요 경고·금기**: 허가사항의 경고 및 주의사항을 참조하세요.
- **질환 금기 관련 정보 (지식 그래프 기반, 허가 문서가 아님)**: 간질환, 담낭질환, 혈소판감소증, 감염성 질환, 호중구감소증, 무과립구증, 관상동맥질환, 빈혈, 고빌리루빈혈증, 길버트 증후군, 신기능 장애, 심정지, 심장 전도 질환, 괴사성 장염, 구내염, **디하이드로피리미딘 탈수소효소(DPD) 결핍**이 연관되어 있습니다.
- **약물 상호작용**: 총 100건이 조회되었으며, 아래는 확인된 주요 항목입니다.
  - 보통(Moderate): Metronidazole, Tinidazole
  - 경미(Minor): Levofloxacin 및 제산제(수산화알루미늄, Magaldrate, 탄산마그네슘, 수산화마그네슘, 산화마그네슘)
  - 등급 미상: Pantoprazole, Omeprazole, Lansoprazole, Metformin, Morphine 등
  - 일부 예측 근거에서 와파린 병용 시 주의가 언급되었으나, 이번 상호작용 목록에서는 확인되지 않아 별도 확인이 필요합니다.

## 결론 및 다음 단계

**결정: Hold (1순위 GAPPS 기준) / 관상 선암·위체부 암은 Proceed with Guardrails**

**사유:**
- 1순위인 GAPPS, 미세침윤성 위암, 악성 위 과립세포종은 임상시험과 문헌이 없는 모델 예측뿐이어서 보류가 적절합니다.
- 위 관상 선암과 위체부 암은 3상 근거(CLASSIC, RESOLVE 등)가 있어 가드레일 하에 진행할 수 있으나, 이는 사실상 기존 위암 사용의 범위입니다. 분문부 선암(L2)과 EBV 관련 위암(L3)은 추가 연구가 필요한 연구 질문 단계입니다.

**진행하려면 필요한 것:**
- 한국 허가 문서(PDF)에서 허가 적응증, 경고, 금기를 확인 (현재 필수 안전성 데이터가 없어 안전성 심사로 진행할 수 없음)
- 작용 기전(MOA) 데이터 보충 (DrugBank 조회)
- DPD 결핍 검사와 신기능에 따른 용량 조정, 와파린 등 상호작용 관리 계획
- 관상 선암 등 조직형별 하위군 효과 확인
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

