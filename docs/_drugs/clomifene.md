---
layout: default
title: Clomifene
parent: 僅模型預測 (L5)
nav_order: 179
evidence_level: L5
indication_count: 10
---

# Clomifene
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Clomifene: 배란 유도에서 여성 불임으로

## 한 문장 요약

Clomifene(클로미펜)은 선택적 에스트로겐 수용체 조절제(SERM)로, 전 세계적으로 배란 유도의 1차 선택약으로 사용되어 왔습니다. TxGNN 모델은 **여성 불임(Female Infertility)**에 효과가 있을 것으로 예측하며, 현재 **50건의 임상시험**과 **20편의 문헌**이 이 방향을 강하게 지지합니다. 한국에서는 현재 시판 허가가 없어 별도 허가 취득 절차가 필요합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 배란 유도 (국제 기준; 한국 미허가) |
| 예측 신규 적응증 | 여성 불임 (Female Infertility) |
| TxGNN 예측 점수 | 99.81% |
| 근거 수준 | L1 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

현재 Evidence Pack에 Clomifene의 공식 작용 기전(MOA) 데이터가 포함되어 있지 않습니다. 그러나 확립된 약리학적 지식에 따르면, Clomifene은 SERM(선택적 에스트로겐 수용체 조절제)으로 시상하부의 에스트로겐 수용체에 경쟁적으로 결합하여 음성 되먹임(negative feedback)을 차단합니다. 그 결과 GnRH 분비가 증가하고, 뇌하수체에서 FSH 및 LH 분비가 촉진되어 난포 발달과 배란이 유도됩니다.

여성 불임의 주요 원인은 무배란 또는 희발배란이며, 다낭성 난소 증후군(PCOS)이 가장 흔한 원인 질환입니다. Clomifene의 HPG axis 자극 기전은 이 병태생리에 직접 대응하여 PCOS 환자의 60~85%에서 배란 유도에 성공하는 것으로 보고되어 있습니다. 불명원인 불임에서도 배란 유도를 통한 임신율 개선 효과가 RCT로 입증되어 있습니다.

TxGNN이 여성 불임을 99.81%의 고득점으로 예측한 것은 이미 임상적으로 확립된 근거와 완전히 일치하는 결과입니다. 이는 모델이 기존 의학 지식을 올바르게 포착하고 있음을 보여주는 검증 신호이기도 하며, 배란 유도제로서의 Clomifene의 임상적 역할을 지식 그래프 관점에서 재확인합니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT02644304](https://clinicaltrials.gov/study/NCT02644304) | Phase 2 | 불명 | 88 | PCOS 불임에서 Clomiphene Citrate + Cabergoline 병용 vs. CC 단독 효과 직접 비교 RCT |
| [NCT02493933](https://clinicaltrials.gov/study/NCT02493933) | Phase 1 | 불명 | 240 | PCOS 불임에서 CC 기반에 식물성 에스트로겐·NO 공여체·NAC 보조요법 추가 시 배란·임신 결과 비교 (3군 공개 RCT) |
| [NCT02304107](https://clinicaltrials.gov/study/NCT02304107) | Phase 3 | 완료 | 140 | CC 저항성 PCOS에서 FSH vs. Letrozole 비교; CC 저항성을 코호트 진입 기준으로 정의 |
| [NCT00413179](https://clinicaltrials.gov/study/NCT00413179) | Phase 3 | 완료 | 56 | 고안드로겐 만성 희발배란 불임 여성에서 Metformin + CC vs. CC + 위약 임신율 비교 이중맹검 RCT |
| [NCT03778099](https://clinicaltrials.gov/study/NCT03778099) | Phase 3 | 완료 | 33 | PCOS에서 시나몬 보충 vs. 위약 배란 유도 효과 비교; CC를 표준 치료 대조군으로 설정 |
| [NCT03009838](https://clinicaltrials.gov/study/NCT03009838) | Phase 3 | 불명 | 150 | CC 저항성 PCOS에서 Letrozole vs. 복강경 난소 천공술 효능 비교 |
| [NCT01923194](https://clinicaltrials.gov/study/NCT01923194) | Phase 3 | 완료 | 215 | CC 실패 WHO Group II 중국 무배란 여성에서 고순도 Urofollitropin vs. rFSH 배란 유도 비교 |
| [NCT05206448](https://clinicaltrials.gov/study/NCT05206448) | Phase 4 | 모집 완료 | 190 | 무배란 PCOS에서 Letrozole + CC 병용 vs. Letrozole 단독 계단식 2주기 용량 비교 |
| [NCT03309436](https://clinicaltrials.gov/study/NCT03309436) | Phase 4 | 불명 | 360 | CC 배란 유도가 자궁내막 수용성 및 동결 배아 이식 임신 결과에 미치는 영향 평가 |
| [NCT01910766](https://clinicaltrials.gov/study/NCT01910766) | NA | 완료 | 110 | CC 저항성 PCOS에서 CoQ10 + CC 병용 vs. CC 단독 배란 유도 전향적 RCT |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [32920843](https://pubmed.ncbi.nlm.nih.gov/32920843/) | 2021 | RCT | Int J Gynecol Obstet | PCOS 무배란 여성에서 Letrozole vs. CC 배란 유도 효능 직접 비교; 두 약물 모두 유효 |
| [30712904](https://pubmed.ncbi.nlm.nih.gov/30712904/) | 2019 | Meta-analysis | JOGC | 불명원인 불임에서 CC vs. Letrozole 최신 메타분석; 두 약물의 임신율 동등성 확인 |
| [29273245](https://pubmed.ncbi.nlm.nih.gov/29273245/) | 2018 | RCT | Lancet | 정상 성선자극호르몬 무배란에서 CC 실패 후 성선자극호르몬 전환 및 IUI 추가 효과 평가 (2×2 요인설계 RCT) |
| [33451262](https://pubmed.ncbi.nlm.nih.gov/33451262/) | 2022 | Systematic Review | Hum Fertil | WHO Group II 배란 장애에서 단독 CC 치료 시 다태 임신률 체계적 문헌고찰; 최신 가이드라인 범위 내 실제 다태율 재평가 |
| [18687718](https://pubmed.ncbi.nlm.nih.gov/18687718/) | 2008 | RCT | BMJ | 불명원인 불임에서 CC vs. 비자극 IUI vs. 기대 요법 비교 실용적 RCT |
| [26613820](https://pubmed.ncbi.nlm.nih.gov/26613820/) | 2016 | RCT | Int J Gynecol Obstet | CC 저항성 PCOS에서 CC+Metformin+Pioglitazone vs. Letrozole+Metformin+Pioglitazone 배란율·임신율 비교 |
| [19809318](https://pubmed.ncbi.nlm.nih.gov/19809318/) | 2009 | Review | Curr Opin Obstet Gynecol | CC 저항성 PCOS 관리 전략 체계적 검토; CC를 PCOS 1차 치료제로, 저항성 시 대안 전략 기술 |
| [34338572](https://pubmed.ncbi.nlm.nih.gov/34338572/) | 2021 | Review | Gynecol Endocrinol | PCOS 불임 치료 개요; CC의 적응증·효능·한계 및 Letrozole과의 비교 기술 |
| [25660647](https://pubmed.ncbi.nlm.nih.gov/25660647/) | 2015 | Review | Fertil Steril | 여성 불임 치료에서 허가/비허가 약물 사용 검토; CC의 기전·부작용·금기 종합 분석 |
| [23182557](https://pubmed.ncbi.nlm.nih.gov/23182557/) | 2012 | Review | Obstet Gynecol Clin North Am | 무배란·불명원인 불임 평가 및 치료 검토; CC를 생활습관 교정 이후 1차 약물로 권고 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
Clomifene의 여성 불임(배란 유도) 효과는 미국 FDA 허가 적응증으로 전 세계적으로 확립되어 있으며, Phase 3 RCT를 포함한 50건의 임상시험과 20편의 문헌이 이를 강력히 뒷받침합니다. TxGNN L1 예측은 기존 임상 근거와 완전히 일치하는 검증 결과이나, 한국에서는 현재 시판 허가가 없고 안전성 초평가용 핵심 데이터(허가사항 경고·금기)가 미확보 상태입니다.

**진행하려면 필요한 것:**
- MFDS(식약처) 허가 신청을 위한 임상 데이터 패키지 준비 (한국인 대상 약동학·약력학 데이터 포함 여부 검토)
- DrugBank를 통한 작용 기전(MOA) 및 안전성 데이터 확보 (DG002 해소)
- 허가사항 PDF 파싱을 통한 경고·금기 정보 수집 및 안전성 초평가(S1) 완료 (DG001 해소)
- 다태 임신, 난소 과자극 증후군(OHSS), 시각 장애 등 주요 부작용에 대한 리스크 모니터링 계획 수립
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

