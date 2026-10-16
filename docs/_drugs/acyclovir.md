---
layout: default
title: Acyclovir
parent: 모델 예측만 (L5)
nav_order: 23
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Acyclovir: 예측 신규 적응증 보통 사마귀 (Common Wart) (근거 수준 L5). 기존 적응증: 단순포진(물집) 바이러스 감염증(초기 및 재발성 생식기 포진과 구순포진 포함)"
monitor_inn: "Acyclovir"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "common wart", "post-infectious neuralgia", "hepatitis C induced liver cirrhosis", "eosinophilic pustular folliculitis", "sequela of COVID-19", "vulvovaginal candidiasis", "papular urticaria", "disease of orbital region", "epidemic keratoconjunctivitis"]
---

# Acyclovir
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

# Acyclovir: 단순포진 감염증에서 보통 사마귀(Common Wart)로

## 한 문장 요약

Acyclovir는 단순포진 바이러스 감염증(생식기 포진, 구순포진 포함) 치료에 사용되어 온 항바이러스제입니다.
TxGNN 모델은 여러 후보 중 **보통 사마귀(Common Wart)**를 근거가 가장 많은 신규 적응증으로 예측하며, 이 질환에 대해 **4건의 임상시험**과 **20편의 문헌**이 확인되었습니다. 다만 대부분 소규모 연구로, 근거 수준은 L2입니다.

> 참고: 모델의 최상위 예측은 점format 점수 순으로 "점상 상피성 각결막염(punctate epithelial keratoconjunctivitis)"입니다. 그러나 이 예측은 임상시험이 없고 확인된 문헌도 기전과 무관하여(L5), 근거가 가장 풍부한 보통 사마귀를 중심으로 평가했습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 단순포진(물집) 바이러스 감염증(초기 및 재발성 생식기 포진과 구순포진 포함) |
| 예측 신규 적응증 | 보통 사마귀 (Common Wart) |
| TxGNN 예측 점수 | 99.46% |
| 근거 수준 | L2 (Phase 2/3 임상시험 1건이 있으나 상태가 "불명"이며, 완료가 확인된 시험은 아님. 문헌에 RCT 보고 있음) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 20건 |
| 권장 결정 | Proceed with Guardrails |

> 최상위 예측(점상 상피성 각결막염, 99.67%)의 권장 결정은 Hold입니다.

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Acyclovir는 헤르페스 바이러스가 가진 티미딘 키나제에 의해 활성화된 뒤 바이러스 DNA 중합효소를 억제하는 뉴클레오시드 유사체이며, 단순포진에서의 효능이 입증되어 있습니다.

사마귀는 인유두종바이러스(HPV)라는 DNA 바이러스가 일으킵니다. 다만 HPV는 티미딘 키나제를 갖고 있지 않아 Acyclovir의 통상적인 활성화 경로가 없습니다. 제안된 기전은 바이러스 및 숙주 DNA 합성의 비특이적 억제, 병변 내 주사 후 면역조절 효과 등이며, 아직 입증되지 않았습니다.

그럼에도 병변 내 Acyclovir 주사를 냉동요법, 비타민 D3, Candida 항원, 5-FU 등과 비교한 소규모 시험들이 임상 활성을 시사합니다. 시험의 질은 아직 불확실합니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT06261684](https://clinicaltrials.gov/study/NCT06261684) | Phase 2/3 | 불명 | 92 | 족저 사마귀에서 병변 내 Acyclovir vs 냉동요법 무작위 비교(결과는 문헌으로 발표된 것으로 보임) |
| [NCT05429151](https://clinicaltrials.gov/study/NCT05429151) | Phase 4 | 불명 | 40 | 족저 사마귀에서 병변 내 Acyclovir vs Candida 항원 비교 |
| [NCT07448844](https://clinicaltrials.gov/study/NCT07448844) | Phase 4 | 모집 중 | 40 | 피부 바이러스성 사마귀에서 병변 내 비타민 D3 vs Acyclovir 비교(8주 완전 소실 평가), 결과 없음 |
| [NCT05324904](https://clinicaltrials.gov/study/NCT05324904) | 해당 없음 | 불명 | 44 | 족저 사마귀에서 병변 내 비타민 D3 vs Acyclovir 효능·안전성 비교 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [40889709](https://pubmed.ncbi.nlm.nih.gov/40889709/) | 2026 | RCT | J Am Acad Dermatol | 족저 사마귀에서 병변 내 Acyclovir vs 냉동요법 비교 |
| [38822848](https://pubmed.ncbi.nlm.nih.gov/38822848/) | 2024 | RCT | Arch Dermatol Res | 난치성 족저 사마귀에서 병변 내 Acyclovir vs B형 간염 백신 비교(48명 완료) |
| [41686619](https://pubmed.ncbi.nlm.nih.gov/41686619/) | 2026 | 체계적 문헌고찰·네트워크 메타분석 | Medicine | 피부 사마귀 치료법 비교, 병변 내 Acyclovir를 새로운 치료로 검토 |
| [40488756](https://pubmed.ncbi.nlm.nih.gov/40488756/) | 2025 | 비교 연구 | Arch Dermatol Res | 난치성 사마귀에서 병변 내 Acyclovir vs 5-FU 비교 |
| [40056255](https://pubmed.ncbi.nlm.nih.gov/40056255/) | 2025 | 임상시험 | Arch Dermatol Res | 난치성 피부 사마귀에서 병변 내 Acyclovir vs 4가 HPV 백신 비교(60명) |
| [37303436](https://pubmed.ncbi.nlm.nih.gov/37303436/) | 2023 | 비교 연구 | Cureus | 바이러스성 사마귀에서 병변 내 Acyclovir vs PPD 면역요법 비교 |
| [34412535](https://pubmed.ncbi.nlm.nih.gov/34412535/) | 2022 | 임상 연구 | J Cutan Med Surg | 병변 내 Acyclovir가 피부 사마귀의 잠재적 치료 옵션임을 제시 |
| [38793636](https://pubmed.ncbi.nlm.nih.gov/38793636/) | 2024 | 증례·문헌고찰 | Viruses | Acyclovir/발라시클로버로 HPV 관련 질환이 관해된 사례 |
| [26885794](https://pubmed.ncbi.nlm.nih.gov/26885794/) | 2016 | 임상 연구(증례) | J Drugs Dermatol | 대상포진용 경구 Acyclovir 10일 투여 후 지속성 족저 사마귀가 소실된 사례 |
| [6467981](https://pubmed.ncbi.nlm.nih.gov/6467981/) | 1984 | 보고 | Cutis | 보통 사마귀(Verrucae vulgares)에 대한 Acyclovir 연고 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202002583 | 헤르페진크림 | 크림 | 재발성 구순포진의 초기 치료 |
| 199201022 | 씨크로크림(아시클로버) | 크림 | 단순포진(물집) 바이러스 감염증(초기 및 재발성 생식기 포진(물집)과 구순포진(물집) 포함) |
| 200301629 | 에이버크림(아시클로버) | 크림 | 단순포진(물집) 바이러스 감염증(초기 및 재발성 생식기 포진(물집)과 구순포진(물집) 포함) |
| 202007060 | 아시클로크림(아시클로버) | 크림 | 단순포진 바이러스 감염증(초기 및 재발성 생식기 포진과 구순포진 포함) |
| 199201976 | 팜젠아시클로버연고 | 연고 | 단순포진 바이러스 감염증(초기 및 재발성 생식기 포진과 구순포진 포함) |

전체 20건은 모두 유효 허가이며, 정제·건조시럽·크림·연고·주사제 등 다양한 제형이 있습니다. 주사제(클로바주, 바크락스주250밀리그램)가 시판되고 있다는 점은 병변 내 투여 연구와 관련해 참고할 만합니다. 다만 사마귀는 현재 허가 적응증이 아닙니다.

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 조회되었으며, 중등도 수준으로 분류된 약물은 Balsalazide, Mesalazine, Olsalazine, Sulfasalazine, Trospium입니다. 그 외 Metformin, Glimepiride, Morphine, Amphotericin B 등은 위험도 등급이 미상입니다.
- **지식그래프 기반 금기 신호**(허가 문구가 아닌 모델 지식그래프 기준): 신장 질환/신기능 저하, 고혈압, 고혈당·당뇨병, 부신피질 기능부전, 뇌졸중·심근경색, 용혈성 요독 증후군, 혈소판감소성 자반증 등이 연결되어 있습니다. 허가사항 확인이 필요합니다.

허가사항의 경고 및 금기 문구는 이번 자료에 포함되지 않았으므로 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
보통 사마귀에서는 병변 내 Acyclovir를 평가한 무작위 비교 연구(Phase 2/3 시험 및 RCT 보고)가 여러 건 있어 다른 예측보다 근거가 확실합니다. 그러나 시험 규모가 작고 상태가 불명인 경우가 많으며, HPV에 대한 기전도 입증되지 않았습니다. 병변 내 투여는 기존 허가 용법과도 다르므로 연구 맥락으로 제한해 진행하는 것이 적절합니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기) 확보: MFDS 첨부문서 확인
- 작용 기전(MOA) 데이터 보완: DrugBank 조회
- 대규모 다기관 RCT 또는 메타분석으로 효능 재확인(소실률, 재발률, 비교군 대비 우월성)
- 병변 내 투여(주사제 전용) 용량·투여 간격·안전성 확인
- 신기능 저하 환자 등 지식그래프 금기 신호 관련 환자군에 대한 모니터링 계획

**기타 예측 신규 적응증 요약:**
- 점상 상피성 각결막염(점수 99.67%, L5): Hold. 확인된 문헌이 기전과 무관합니다.
- 헤르페스 관련 안과 질환("안와 부위 질환", L3): 이미 HSV/VZV 적응증에 포함되는 영역이라 새로운 재창출 기회로 보기 어렵습니다.
- 대상포진 후 신경통, C형 간염 유발 간경변, 호산구성 농포성 모낭염, 구진성 두드러기, 칸디다성 외음질염, 유행성 각결막염: Hold. 기전적 근거가 없거나 문헌이 연관성을 뒷받침하지 않습니다.
- COVID-19 후유증(L4): Hold. 문헌은 대부분 헤르페스 바이러스 재활성화 치료에 관한 것이며 COVID-19 후유증 자체의 치료 근거가 아닙니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

