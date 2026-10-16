---
layout: default
title: Pertuzumab
parent: 모델 예측만 (L5)
nav_order: 595
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Pertuzumab: 예측 신규 적응증 프로게스테론 수용체 양성 유방암 (Progesterone-receptor positive breast cancer) (근거 수준 L5). 기존 적응증: 허가 문서 링크만 확인되며 적응증 본문은 이번 데이터에 포함되어 있지 않음 (HER2 과발현 유방암에 사용되는 것으로 알려져…"
monitor_inn: "Pertuzumab"
predicted_indications: ["normal breast-like subtype of breast carcinoma", "progesterone-receptor positive breast cancer", "progesterone-receptor negative breast cancer", "breast tumor luminal A or B", "ectomesenchymoma", "malignant cutaneous granular cell skin tumor", "human herpesvirus 8-related tumor", "middle ear neuroendocrine tumor", "prostatic urethra urothelial carcinoma", "kidney pelvis sarcomatoid transitional cell carcinoma"]
---

# Pertuzumab
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

# Pertuzumab: HER2 양성 유방암에서 프로게스테론 수용체 양성 유방암으로

## 한 문장 요약

Pertuzumab은 HER2 이량체화를 억제하는 단일클론항체로, 원래 HER2 과발현 유방암 치료에 사용되었습니다.
TxGNN 모델은 **프로게스테론 수용체 양성 유방암(Progesterone-receptor positive breast cancer)**에 효과가 있을 수 있다고 예측하며, 현재 **1건의 임상시험**과 **20편의 문헌**이 이 방향을 지지합니다.
다만 이 예측 대상은 사실상 이미 허가된 HER2 양성 유방암 집단과 대부분 겹치므로, 새로운 재창출 신호로 보기는 어렵습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 문서 링크만 확인되며 적응증 본문은 이번 데이터에 포함되어 있지 않음 (HER2 과발현 유방암에 사용되는 것으로 알려져 있음) |
| 예측 신규 적응증 | 프로게스테론 수용체 양성 유방암 (Progesterone-receptor positive breast cancer) |
| TxGNN 예측 점수 | 99.93% |
| 근거 수준 | L1 (완료된 Phase 3 RCT 근거가 있으나, 오리지널 약물이 아닌 바이오시밀러 동등성 시험임) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 3건 |
| 권장 결정 | Proceed with Guardrails |

> 참고: TxGNN 점수 순위 1위는 "정상 유방 유사 아형 유방암"(99.93%)이지만, 임상시험과 문헌이 없고 기전 연관성이 약해 Hold로 평가되었습니다. 이 보고서는 근거가 가장 충실한 2위 예측(프로게스테론 수용체 양성 유방암)을 중심으로 작성했습니다.

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Pertuzumab은 HER2 이량체화 억제 항체로, HER2가 HER3 등 다른 HER 계열 수용체와 짝을 이루는 것을 막아 PI3K/AKT 및 MAPK 신호전달을 억제합니다.

프로게스테론 수용체(PR) 양성이면서 HER2 양성인 유방암은 HER2 양성 유방암의 상당 부분을 차지합니다. 이 집단에서는 HER2 차단이 기전상 그대로 적용됩니다. 다만 PR 상태만으로는 치료 대상이 정해지지 않으며, **HER2 양성 확진이 전제**되어야 합니다.

따라서 이 예측은 새로운 질환으로의 확장이라기보다 이미 허가된 HER2 양성 유방암 집단의 하위 분류에 가깝습니다. TxGNN의 높은 점수는 지식그래프상 유방암 전반과의 연관성을 반영한 것으로 보입니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT04629846](https://clinicaltrials.gov/study/NCT04629846) | Phase 3 | 완료 | 517 | HER2 양성, ER/PR 음성 조기·국소 진행 유방암에서 Pertuzumab 바이오시밀러(QL1209) vs 기존 Pertuzumab을 trastuzumab+docetaxel과 병용한 무작위 이중맹검 동등성 시험 |

이 시험은 대상이 ER/PR 음성 환자이며 바이오시밀러 동등성 시험이므로, 오리지널 약물의 PR 양성 유방암 효능에 대한 간접 근거입니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [27179402](https://pubmed.ncbi.nlm.nih.gov/27179402/) | 2016 | RCT | Lancet Oncol | NeoSphere 5년 분석: 術前 pertuzumab+trastuzumab+docetaxel의 무진행생존기간·무질병생존기간 및 안전성 |
| [28945833](https://pubmed.ncbi.nlm.nih.gov/28945833/) | 2017 | RCT | Ann Oncol | WSG-ADAPT HER2+/HR-: 12주 이중차단 ± paclitaxel의 de-escalation 전략 |
| [38906970](https://pubmed.ncbi.nlm.nih.gov/38906970/) | 2024 | RCT | Br J Cancer | QL1209(바이오시밀러)와 기존 pertuzumab의 동등성 입증을 위한 Phase 3 시험 |
| [42150145](https://pubmed.ncbi.nlm.nih.gov/42150145/) | 2026 | RCT | J Clin Oncol | WSG TP-II 생존 분석: HR 양성/HER2 양성 조기 유방암에서 trastuzumab+pertuzumab+내분비요법 vs 화학요법 |
| [37166817](https://pubmed.ncbi.nlm.nih.gov/37166817/) | 2023 | RCT | JAMA Oncol | WSG-TP-II: HR 양성/HER2 양성에서 내분비요법+이중 HER2 차단 vs 감량 화학요법 |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | 가이드라인 | J Clin Oncol | 진행성 HER2 양성 유방암 전신치료 ASCO 가이드라인 개정 |
| [40076535](https://pubmed.ncbi.nlm.nih.gov/40076535/) | 2025 | 체계적 문헌고찰 | Int J Mol Sci | HER2 양성 유방암에서 pertuzumab+trastuzumab+docetaxel 보조 이중요법 |
| [27057657](https://pubmed.ncbi.nlm.nih.gov/27057657/) | 2016 | Review | Cancer Treat Rev | HR/HER2 양성 유방암의 현재와 미래 |
| [40983817](https://pubmed.ncbi.nlm.nih.gov/40983817/) | 2025 | Review | Breast Cancer | HR+/HER2+ 유방암의 신호전달 경로 상호작용과 임상 적용 |
| [41387082](https://pubmed.ncbi.nlm.nih.gov/41387082/) | 2026 | 후향 코호트 | Breast | 폐경 전 HR+/HER2+ 유방암에서 보조 난소기능억제 및 아로마타제 억제제의 효과 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202106366 | 페스코피하주사1200/600밀리그램(퍼투주맙/트라스투주맙) | 바이알 주사제 | 허가사항 문서 참조 |
| 201307522 | 퍼제타주(퍼투주맙) | 바이알 주사제 | 허가사항 문서 참조 |
| 202106365 | 페스코피하주사600/600밀리그램(퍼투주맙/트라스투주맙) | 바이알 주사제 | 허가사항 문서 참조 |

3건 모두 (주)한국로슈의 단일 성분 허가이며 유효 상태입니다.

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적치료제 (HER2 단일클론항체) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 (병용되는 docetaxel 등 화학요법에 의한 골수억제 가능) |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 심기능(좌심실 구혈률)은 문헌에서 핵심 안전성 지표로 다뤄지며(TRYPHAENA, BERENICE), 병용 화학요법에 따른 CBC 확인도 필요 |
| 취급 방호 | 허가사항의 경고 및 주의사항을 참조하세요 |

## 안전성 고려사항

- **약물 상호작용**: Idelalisib과 중등도(Moderate) 상호작용이 보고되어 있습니다.

그 외 경고·금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
HER2 양성/PR 양성 유방암은 Pertuzumab이 이미 사용되는 집단과 겹치며, 이중 HER2 차단을 뒷받침하는 RCT 문헌이 풍부합니다. 다만 Phase 3 시험은 바이오시밀러 동등성 시험이고 ER/PR 음성 환자 대상이어서, PR 양성 집단에 대한 직접 근거는 제한적입니다. 새로운 재창출이라기보다 기존 적응증의 하위 집단 확인에 가깝습니다.

**진행하려면 필요한 것:**
- 환자 선별 시 HER2 양성 확진 필수 (PR 상태만으로는 적격 판단 불가)
- 한국 허가 적응증 본문 및 경고·금기 사항 확인 (허가 문서 파싱 필요)
- 상세 작용 기전 데이터 보완
- 심기능 모니터링 계획 수립
- HR 양성/HER2 양성 하위집단에 대한 직접 근거 정리 (WSG TP-II, PERTAIN 등)

**참고: 다른 예측 질환**
- "정상 유방 유사 아형 유방암"은 TxGNN 점수 99.93%로 1위이나 임상시험·문헌이 없고 HER2 기전 연관성이 약해 **Hold**입니다.
- "프로게스테론 수용체 음성 유방암"은 완료된 Phase 3 바이오시밀러 시험(NCT04629846)과 DECRESCENDO(Phase 2, 중단) 근거가 있어 **Proceed with Guardrails**이나, 마찬가지로 이미 허가된 HER2 양성 집단과 대부분 겹칩니다.
- "유방 종양 루미널 A/B"는 HER2 양성 하위집단에서만 기전이 성립하며, 근거 수준 L2의 **연구 과제**로 분류됩니다.
- 외골수종 등 희귀 종양 및 요로상피암 등 나머지 예측은 임상 근거가 없는 모델 예측 단계(L5)로 **Hold**입니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

