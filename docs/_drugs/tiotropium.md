---
layout: default
title: Tiotropium
parent: 높은 근거 (L1-L2)
nav_order: 739
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-15
description: "Tiotropium: 예측 신규 적응증 폐쇄성 폐질환 (Obstructive Lung Disease) (근거 수준 L1). 기존 적응증: 허가증에 적응증 원문이 제공되지 않음 (식약처 허가정보 링크만 확인됨). 흡입용 기관지확장제로서 COPD 유지 치료로 알려져…"
monitor_inn: "tiotropium"
predicted_indications: ["obstructive lung disease", "respiratory malformation", "Rienhoff syndrome", "hyperlucent lung", "tracheal stenosis", "susceptibility to respiratory infections associated with CD8alpha chain mutation"]
---

# Tiotropium
{: .fs-9 }

근거 수준: **L1** | 예측 적응증: **10** 건
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

# Tiotropium: 만성 폐쇄성 폐질환에서 폐쇄성 폐질환으로

## 한 문장 요약

Tiotropium은 장시간 작용 항콜린제(LAMA)로, 원래 만성 폐쇄성 폐질환(COPD) 등 기도 폐쇄 질환의 유지 치료에 사용되었습니다.
TxGNN 모델은 **폐쇄성 폐질환(Obstructive Lung Disease)**에 효과가 있을 수 있다고 예측하며, 현재 **39건의 임상시험**과 **20편의 문헌**이 이 방향을 지지합니다.
다만 이 예측은 이미 승인된 COPD 용도와 사실상 같아서, 새로운 적응증 발굴이라기보다 모델 예측의 타당성을 확인하는 결과에 가깝습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가증에 적응증 원문이 제공되지 않음 (식약처 허가정보 링크만 확인됨). 흡입용 기관지확장제로서 COPD 유지 치료로 알려져 있음 |
| 예측 신규 적응증 | 폐쇄성 폐질환 (Obstructive Lung Disease) |
| TxGNN 예측 점수 | 99.99% |
| 근거 수준 | L1 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 3건 |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 이 보고서용으로 확보되지 않았습니다. 알려진 정보에 따르면 Tiotropium은 무스카린 수용체 길항제로, 기도 평활근의 M3 수용체를 차단하여 지속적인 기관지 확장을 일으키고 콜린성 긴장을 줄입니다. 해리 속도가 느려 하루 1회 투여가 가능합니다.

폐쇄성 폐질환은 COPD를 포함하는 상위 범주입니다. 따라서 이 예측은 이미 승인된 COPD 용도와 거의 일치하며, 진정한 의미의 약물 재창출 후보는 아닙니다. 높은 점수는 기전적 적합성과 일치합니다.

같은 순위표의 다른 예측들은 상황이 다릅니다. 호흡기 기형, Rienhoff 증후군, 기관 협착, 간질성 폐기종, 보상성 폐기종, CD8α 사슬 돌연변이 관련 호흡기 감염 감수성 등은 임상 근거가 없거나 이름 유사성에 기반한 것으로 보이며, 기전적 연결도 불분명합니다.

## 임상시험 근거

데이터에 수록된 시험이 많아, 관련성이 높은 대표 시험 10건만 정리했습니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00240435](https://clinicaltrials.gov/study/NCT00240435) | Phase 3 | 완료 | 491 | COPD에서 Respimat Tiotropium 5·10 mcg을 위약 및 ipratropium MDI와 비교한 12주 이중맹검 시험 |
| [NCT01431274](https://clinicaltrials.gov/study/NCT01431274) | Phase 3 | 완료 | 2,624 | COPD에서 Tiotropium+Olodaterol 복합제를 단일 성분과 비교한 52주 시험 (TOnado 1) |
| [NCT00877383](https://clinicaltrials.gov/study/NCT00877383) | Phase 3 | 완료 | 1,142 | 중등도~중증 COPD에서 Indacaterol+Tiotropium을 Tiotropium 단독과 비교한 12주 시험 |
| [NCT00900731](https://clinicaltrials.gov/study/NCT00900731) | Phase 3 | 완료 | 1,598 | 중등도~중증 COPD에서 Indacaterol과 Tiotropium(HandiHaler)을 비교한 12주 시험 |
| [NCT01854645](https://clinicaltrials.gov/study/NCT01854645) | Phase 3 | 완료 | 2,103 | 중등도~매우 중증 COPD에서 PT003·PT005·PT001을 위약 및 Tiotropium 공개 대조와 비교한 24주 시험 |
| [NCT00157235](https://clinicaltrials.gov/study/NCT00157235) | Phase 3 | 완료 | 234 | 폐 재활 중인 COPD 환자에서 Tiotropium이 운동 내성에 미치는 효과(위약 대조) |
| [NCT00144326](https://clinicaltrials.gov/study/NCT00144326) | Phase 3 | 완료 | 250 | COPD에서 Tiotropium이 가속도계로 측정한 일상 신체활동량에 미치는 효과(위약 대조) |
| [NCT02172807](https://clinicaltrials.gov/study/NCT02172807) | Phase 3 | 완료 | 201 | COPD에서 Tiotropium 18·36 mcg과 oxitropium MDI를 비교한 4주 시험 |
| [NCT04780984](https://clinicaltrials.gov/study/NCT04780984) | Phase 2 | 완료 | 116 | COPD에서 Tiotropium 흡입액 3개 용량의 약력학·상대 생체이용률·안전성 평가 |
| [NCT04999930](https://clinicaltrials.gov/study/NCT04999930) | 해당 없음 | 완료 | 100 | Respimat 투여 시 에어로챔버 사용 여부에 따른 효과와 환자 만족도 비교(효능 근거는 아님) |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [28877027](https://pubmed.ncbi.nlm.nih.gov/28877027/) | 2017 | RCT | N Engl J Med | 경증~중등도 COPD에서 Tiotropium 장기 사용이 폐기능을 개선하고 감소를 늦추는지 평가 |
| [29779416](https://pubmed.ncbi.nlm.nih.gov/29779416/) | 2018 | RCT | Am J Respir Crit Care Med | 장기 삼제요법 중인 COPD 환자에서 Indacaterol/Glycopyrronium으로 단계 축소하는 SUNSET 시험 |
| [16844726](https://pubmed.ncbi.nlm.nih.gov/16844726/) | 2006 | 메타분석 | Thorax | 안정형 COPD에서 Tiotropium의 임상 사건, 증상, 폐기능, 이상반응 평가 |
| [25046211](https://pubmed.ncbi.nlm.nih.gov/25046211/) | 2014 | 체계적 고찰 | Cochrane Database Syst Rev | Tiotropium과 위약 비교 |
| [23728670](https://pubmed.ncbi.nlm.nih.gov/23728670/) | 2013 | 체계적 고찰 | Cochrane Database Syst Rev | 흡입 스테로이드+LABA 복합제와 Tiotropium 비교 |
| [32727455](https://pubmed.ncbi.nlm.nih.gov/32727455/) | 2020 | Review | Respir Res | COPD에서 Tiotropium의 임상 개발 현황 |
| [19402836](https://pubmed.ncbi.nlm.nih.gov/19402836/) | 2009 | 메타분석 | Respirology | 중국인 안정형 COPD 환자에서 Tiotropium의 효능과 안전성 |
| [33095662](https://pubmed.ncbi.nlm.nih.gov/33095662/) | 2021 | Review | Curr Med Res Opin | Tiotropium+Olodaterol 복합제로 COPD 악화를 줄이고 관리하는 근거 정리 |
| [31119643](https://pubmed.ncbi.nlm.nih.gov/31119643/) | 2019 | Review | Drugs | COPD 장기 유지 치료에서 Tiotropium/Olodaterol 고정용량 복합제 |
| [10069510](https://pubmed.ncbi.nlm.nih.gov/10069510/) | 1999 | 기전 연구 | Life Sci | Tiotropium의 작용 기전과 폐쇄성 폐질환에서의 임상 프로파일 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201506154 | 바헬바레스피맷 | 레스피맷 흡입기용 액제(4.5mL 카트리지) | 허가 적응증 원문은 식약처 허가정보 참조 |
| 200811444 | 스피리바레스피맷(티오트로퓸브롬화물수화물) | 레스피맷 흡입기용 액제(4.5mL 카트리지) | 허가 적응증 원문은 식약처 허가정보 참조 |
| 200209849 | 스피리바흡입용캡슐(티오트로퓸브롬화물수화물) | 흡입용 캡슐(핸디핼러) | 허가 적응증 원문은 식약처 허가정보 참조 |

세 제품 모두 한국베링거인겔하임(주) 제품이며 유효한 단일제 허가입니다.

## 안전성 고려사항

허가사항의 경고 및 금기 정보는 이 보고서용으로 확보되지 않았으므로, 안전성 정보는 허가사항을 참조하세요.

참고로 지식 그래프상 금기 질환으로 연결된 항목은 다음과 같습니다. 허가 문서 기반이 아니므로 확인이 필요합니다.
- 양성 전립선 비대증
- 신기능 저하
- 폐쇄각 녹내장(협우각 녹내장)
- 방광 경부 폐색

**약물 상호작용**: 총 430건이 조회되었으며, 주요 항목은 다음과 같습니다.
- 중등도: 다른 항콜린제와의 병용(Hyoscyamine, Atropine, Glycopyrronium, Clidinium, Dicyclomine, Trospium, Scopolamine, Propantheline, Methscopolamine, Mepenzolate), 그리고 Eluxadoline, Prucalopride, 흡입 인슐린
- 경미: Cimetidine

항콜린 작용이 겹치므로 다른 항콜린제와 병용할 때는 주의가 필요합니다. 또한 Handhaler Tiotropium이 안구 전방 파라미터에 미치는 영향을 본 시험(NCT06525051)이 있어, 녹내장 위험 평가가 관련됩니다.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
완료된 Phase 3 RCT가 다수 있고 RCT와 메타분석 문헌이 뒷받침하여 근거 수준은 L1입니다. 다만 이 예측은 이미 승인된 COPD 용도와 같은 범주이므로 신규 재창출이 아니라 예측 모델의 타당성 검증으로 해석해야 합니다.

**진행하려면 필요한 것:**
- 식약처 허가사항(적응증, 경고, 금기)을 내려받아 확인하고 안전성 선별 진행
- 작용 기전(MOA) 데이터 보완 (DrugBank 조회)
- 항콜린제 병용, 녹내장·전립선 비대·신기능 저하 환자에 대한 안전성 모니터링 계획
- 호흡기 기형 등 하위 예측은 임상 근거가 없어 보류(Hold)하며, 진짜 신규 적응증 탐색은 별도 후보로 진행
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

