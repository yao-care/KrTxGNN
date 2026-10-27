---
layout: default
title: Imipenem
parent: 모델 예측만 (L5)
nav_order: 418
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Imipenem: 예측 신규 적응증 전신 피부경화증 (Diffuse scleroderma) (근거 수준 L5). 기존 적응증: 허가 적응증 텍스트가 문서 링크 형태로만 제공되어 구체적 내용을 확인할 수 없음 (허가사항 PDF 참조)"
monitor_inn: "Imipenem"
predicted_indications: ["diffuse scleroderma", "paratyphoid fever", "salmonellosis", "sinusitis", "chronic rhinosinusitis", "typhoid fever", "chronic ethmoidal sinusitis", "paranasal sinus neoplasm (disease)", "staphylococcus aureus infection", "eosinophilia-myalgia syndrome"]
---

# Imipenem
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

## Imipenem: 세균 감염증에서 미분류 신규 적응증으로 — 황색포도알균 감염(MRSA) 병용요법 중심 평가
{: .text-alpha }

## 한 문장 요약

Imipenem은 카바페넴계 광범위 베타락탐 항생제로, 한국에서 주사제(수출용 허가)로 허가되어 있습니다. TxGNN 모델은 여러 신규 적응증을 예측했으며, 그중 **황색포도알균 감염(Staphylococcus aureus infection)**이 임상시험 2건과 문헌이 있어 가장 근거가 두텁습니다. 다만 TxGNN 점수 1순위인 **전신 피부경화증(diffuse scleroderma)**은 임상시험과 문헌이 모두 없습니다.

> 참고: 이 보고서는 예측 순위 1위(전신 피부경화증)를 기준으로 개요를 작성하되, 근거가 실제로 존재하는 후보를 함께 비교합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 텍스트가 문서 링크 형태로만 제공되어 구체적 내용을 확인할 수 없음 (허가사항 PDF 참조) |
| 예측 신규 적응증 (1순위) | 전신 피부경화증 (Diffuse scleroderma) |
| TxGNN 예측 점수 (1순위) | 99.99% |
| 근거 수준 (1순위) | L5 (모델 예측만 있음) |
| 근거가 가장 풍부한 후보 | 황색포도알균 감염 (TxGNN 99.95%, 임상시험 2건, 근거 수준 L2 판정) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | 1순위(전신 피부경화증): Hold / 황색포도알균 감염: Proceed with Guardrails |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Imipenem은 카바페넴계 베타락탐 항생제로, 세균 세포벽 합성을 억제하는 항균 기전을 가집니다. 따라서 세균 감염 질환으로의 확장은 기전상 설명이 됩니다.

**전신 피부경화증(1순위)**은 자가면역성 섬유화 질환이어서 항균 기전과 연결되지 않습니다. 높은 점수는 지식 그래프 기반 예측일 뿐, 뒷받침하는 임상시험이나 문헌이 없습니다. 같은 이유로 부비동 신생물, 호산구증가-근육통 증후군도 기전적 근거가 없습니다.

반면 **감염성 질환 후보**는 기전상 타당성이 있습니다.
- **황색포도알균 감염**: 메티실린 감수성 균주에는 활성이 있습니다. MRSA에는 단독으로는 약하지만 fosfomycin, gentamicin, telavancin 등과의 병용 시너지가 보고되어 있습니다.
- **장티푸스·파라티푸스·살모넬라증**: Salmonella에 대한 항균 활성이 있고, 광범위내성(XDR) 장티푸스에서 카바페넴이 최후 치료 수단으로 거론됩니다. 다만 문헌은 대부분 내성 감시 연구이며, meropenem이 imipenem보다 더 자주 언급됩니다.
- **부비동염·만성 비부비동염·만성 사골동염**: 원인균에 대한 활성은 있으나, 비경구 광범위 항생제를 일상적 부비동염에 쓰는 것은 항생제 적정사용 측면에서 부적절합니다. 내성균·원내 감염에 한정될 수 있습니다.

## 임상시험 근거

1순위 예측(전신 피부경화증)에는 관련 임상시험 등록이 없습니다. 아래는 근거가 있는 후보인 황색포도알균 감염의 시험입니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00871104](https://clinicaltrials.gov/study/NCT00871104) | Phase 4 | 완료 | 50 | MRSA 감염성 심내막염에서 fosfomycin + imipenem을 표준치료인 vancomycin과 비교. 결과 데이터는 제공되지 않음 |
| [NCT01356472](https://clinicaltrials.gov/study/NCT01356472) | Phase 4 | 불명 | 60 | 인공호흡기 관련 폐렴 환자의 MRSA에서 linezolid 단독 또는 카바페넴 병용 효과 평가. 카바페넴이 imipenem이 아닐 수 있음 |

두 시험 모두 규모가 작고 결과가 제공되지 않아 결론을 내리기 어렵습니다. 다른 후보(장티푸스, 살모넬라증, 부비동염 등)에는 등록된 임상시험이 없습니다.

## 문헌 근거

**황색포도알균 감염** (주요 문헌)

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [3460521](https://pubmed.ncbi.nlm.nih.gov/3460521/) | 1986 | 임상 연구 | Antimicrob Agents Chemother | MSSA·MRSA 감염 환자 23명에서 imipenem-cilastatin의 효능과 독성 평가 |
| [33020155](https://pubmed.ncbi.nlm.nih.gov/33020155/) | 2020 | Case report | Antimicrob Agents Chemother | 난치성 MRSA 감염에서 imipenem/cilastatin + fosfomycin 병용 사례 |
| [10588305](https://pubmed.ncbi.nlm.nih.gov/10588305/) | 1999 | 전임상 | J Antimicrob Chemother | MRSA에 대한 vancomycin + imipenem의 시험관 및 마우스 모델 상승 효과 |
| [6421794](https://pubmed.ncbi.nlm.nih.gov/6421794/) | 1983 | 동물 연구 | J Antimicrob Chemother | 토끼 심내막염 모델에서 imipenem의 효과 |
| [22196394](https://pubmed.ncbi.nlm.nih.gov/22196394/) | 2012 | Review | Int J Antimicrob Agents | MRSA의 병태생리, 치료, 내성에 대한 리뷰 |

**장티푸스** (주요 문헌)

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [39991360](https://pubmed.ncbi.nlm.nih.gov/39991360/) | 2025 | 코호트 | Cureus | MDR/XDR 장티푸스에서 카바페넴 효과 평가 |
| [15707075](https://pubmed.ncbi.nlm.nih.gov/15707075/) | 2003 | Case report | J Med Liban | 장티푸스 합병 횡문근융해증·신부전을 imipenem/cilastatin으로 치료한 사례 |
| [19208884](https://pubmed.ncbi.nlm.nih.gov/19208884/) | 2009 | 시험관 연구 | J Med Microbiol | Salmonella 210주에 대한 카바페넴 및 tigecycline의 최소억제농도 |

**파라티푸스 및 살모넬라증**: 문헌 대부분이 내성 감시 연구이며 imipenem의 임상 효능 자료는 없습니다. 예외로 [22204180](https://pubmed.ncbi.nlm.nih.gov/22204180/)(2011, JPMA)은 imipenem을 포함한 신규 항균제의 시험관 감수성을 평가했고, [3469191](https://pubmed.ncbi.nlm.nih.gov/3469191/)(1986, 임상 평가)은 원내 감염·다제내성균에서 imipenem/cilastatin을 평가했으나 Salmonella 특이적이지 않습니다.

**부비동염·만성 비부비동염**: 다른 항생제 리뷰와 세균학적 조사가 대부분으로, imipenem 특이 임상 근거는 없습니다.

**전신 피부경화증, 부비동 신생물, 호산구증가-근육통 증후군**: 현재 관련 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200703652 | 자니심주사(수출용) | 백색~미황색 가루가 든 무색 투명 바이알 (주사제) | 허가사항 PDF 참조 |

제조사는 천우신약(주)이며, 수출용 허가입니다.

## 안전성 고려사항

**약물 상호작용** (총 15건, 주요 항목)
- **Major**: Bupropion, Iohexol, Iopamidol
- **Moderate**: Warfarin, Dicoumarol, Theophylline 계열(Aminophylline, Dyphylline, Oxtriphylline), Cyclosporine, Mycophenolic acid, Pemetrexed, Ethinylestradiol, Lindane, Polyethylene glycol (전해질 포함)

**지식 그래프 기반 금기 관련 질환** (허가 문구가 아닌 모델 지식 그래프 기준): 간질, 신장 질환, 요관 농양, *Clostridium difficile* 대장염, 신생아 괴사성 장염

경고 및 금기의 공식 내용은 허가사항을 확인해야 합니다.

## 결론 및 다음 단계

**결정: 1순위 예측(전신 피부경화증)은 Hold, 황색포도알균 감염은 Proceed with Guardrails**

**사유:**
- 전신 피부경화증은 기전적 연결이 없고 임상시험·문헌이 전무하여 모델 예측에 그칩니다. 부비동 신생물과 호산구증가-근육통 증후군도 마찬가지입니다.
- 황색포도알균 감염은 Phase 4 시험 2건(1건 완료)과 병용요법 문헌이 있으나 규모가 작고 결과가 제공되지 않았습니다. 난치성 MRSA에서 감수성 검사와 항생제 적정사용 관리 하에 병용요법으로만 고려해야 합니다.
- 장티푸스·파라티푸스·살모넬라증은 근거 수준 L4로, 연구 질문 단계입니다. 부비동염 계열은 적정사용 측면에서 Hold입니다.

**진행하려면 필요한 것:**
- 한국 허가사항(경고·금기·적응증) 확보. 현재 안전성 심사를 진행할 수 없는 차단 수준의 데이터 공백이 있습니다.
- 상세한 작용 기전(MOA) 데이터 보충
- NCT00871104의 결과 데이터 확보 및 imipenem 특이 효능 확인
- XDR 장티푸스에서 imipenem과 meropenem의 비교 근거 확인
- 간질·신기능 저하 환자 및 약물 상호작용(특히 항경련제·theophylline 계열)에 대한 안전성 모니터링 계획
- 수출용 허가임을 고려한 국내 사용 가능성 검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

