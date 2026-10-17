---
layout: default
title: Agomelatine
parent: 모델 예측만 (L5)
nav_order: 30
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Agomelatine: 예측 신규 적응증 불안장애 (Anxiety Disorder) (근거 수준 L5). 기존 적응증: 허가증에는 적응증 본문 대신 문서 링크만 등록되어 있어 확인할 수 없음 (문헌상 주요우울장애)"
monitor_inn: "Agomelatine"
predicted_indications: ["benign paroxysmal torticollis of infancy", "agoraphobia", "Ohdo syndrome and variants"]
---

# Agomelatine
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

# Agomelatine: 우울증에서 불안장애로

## 한 문장 요약

Agomelatine은 멜라토닌 MT1/MT2 수용체 작용제이자 5-HT2C 수용체 길항제로, 원래 주요우울장애 치료에 사용되는 항우울제입니다.
TxGNN 모델은 **불안장애(Anxiety Disorder)**에 효과가 있을 수 있다고 예측하며, 현재 **2건의 임상시험**과 **20편의 문헌**이 이 방향과 관련되어 있습니다. 다만 임상시험 중 직접 효능을 평가한 것은 1건(강박장애 Phase 2)뿐입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가증에는 적응증 본문 대신 문서 링크만 등록되어 있어 확인할 수 없음 (문헌상 주요우울장애) |
| 예측 신규 적응증 | 불안장애 (Anxiety Disorder) |
| TxGNN 예측 점수 | 99.98% |
| 근거 수준 | L3 (완료된 불안장애 Phase 3 RCT 없음, 체계적 문헌고찰·메타분석 존재) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터(DrugBank)는 확보되지 않았습니다. 다만 문헌에 따르면 agomelatine은 멜라토닌 MT1/MT2 수용체 작용제이자 5-HT2C 수용체 길항제입니다. 수집된 약리 정보에서도 5-HT2A, 5-HT2B, 5-HT2C, MT1, MT2 수용체와의 상호작용이 확인됩니다.

이 기전은 일주기 리듬과 수면을 조절하고 전전두엽의 도파민·노르에피네프린 방출을 높여 기분과 불안에 긍정적 영향을 줄 수 있습니다. 우울증과 불안은 자주 동반되므로 기전상 불안장애에도 적용될 가능성이 있습니다.

범불안장애(GAD)에 대해서는 agomelatine 전용 리뷰와 메타분석, 네트워크 메타분석이 여러 편 있고, 위약 및 활성 대조 시험(PMID 24569045)도 보고되었습니다. 다만 이번 자료만으로는 개별 시험의 결과를 검증하지 못했으므로, 효능은 원문 확인이 필요합니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01108393](https://clinicaltrials.gov/study/NCT01108393) | Phase 2 | 완료 | 74 | 강박장애에서 agomelatine 25~50 mg/일 vs 위약(16주, 이중맹검). 결과 미공개 |
| [NCT02374567](https://clinicaltrials.gov/study/NCT02375567) | Phase 3 | 종료 | 407 | 노인정신과 입원환자의 약물 안전성·약물이상반응 조사. 불안장애 효능시험 아님 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [24569045](https://pubmed.ncbi.nlm.nih.gov/24569045/) | 2014 | 위약·활성대조 시험 | J Clin Psychiatry | GAD에서 agomelatine의 단기 효능 확인을 위한 추가 위약대조 시험 |
| [32702221](https://pubmed.ncbi.nlm.nih.gov/32702221/) | 2020 | 메타분석 | Clin Psychopharmacol Neurosci | GAD에서 agomelatine의 효능과 안전성 평가 |
| [38804215](https://pubmed.ncbi.nlm.nih.gov/38804215/) | 2025 | 체계적 문헌고찰·네트워크 메타분석 | Int Clin Psychopharmacol | 성인 GAD에서 agomelatine과 승인된 약물의 관해 및 이상반응 중단 비교 |
| [33343351](https://pubmed.ncbi.nlm.nih.gov/33343351/) | 2020 | 네트워크 메타분석 | Front Pharmacol | GAD 약물들의 관해율과 내약성 비교 |
| [30712879](https://pubmed.ncbi.nlm.nih.gov/30712879/) | 2019 | 네트워크 메타분석 | Lancet | GAD 약물치료 간 비교 |
| [40788541](https://pubmed.ncbi.nlm.nih.gov/40788541/) | 2026 | 네트워크 메타분석 | Eur Arch Psychiatry Clin Neurosci | 항불안제의 효능과 수용성 비교 |
| [34417992](https://pubmed.ncbi.nlm.nih.gov/34417992/) | 2021 | 리뷰 | Adv Ther | GAD 근거 기반 약물치료, agomelatine 중심 |
| [35795687](https://pubmed.ncbi.nlm.nih.gov/35795687/) | 2022 | 리뷰 | Ther Adv Psychopharmacol | GAD에서 agomelatine의 독특한 작용 기전 |
| [28730851](https://pubmed.ncbi.nlm.nih.gov/28730851/) | 2017 | 리뷰 | Expert Opin Pharmacother | GAD의 단기·유지 치료에서 유망함 |
| [24766542](https://pubmed.ncbi.nlm.nih.gov/24766542/) | 2014 | 리뷰 | Expert Opin Investig Drugs | GAD 치료제로서 agomelatine 검토 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202403080 | 아고틴정25밀리그램(아고멜라틴) | 장방형 필름코팅정 (진노랑색) | 적응증 본문 없이 허가 문서 링크만 등록되어 있음 (제조사: 환인제약) |

## 안전성 고려사항

- **약리학적 표적**: 5-HT2A, 5-HT2B, 5-HT2C, MT1, MT2 수용체와 상호작용합니다. 이는 표적 정보이며 임상적 약물 상호작용 등급은 아닙니다.

그 외 경고·금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
GAD에서 agomelatine을 다룬 위약대조 시험, 메타분석, 네트워크 메타분석이 있어 불안장애 방향의 근거가 어느 정도 쌓여 있습니다. 그러나 등록된 임상시험 중 불안장애 효능을 직접 입증한 완료 Phase 3 시험은 없고, 허가사항상의 경고·금기도 확인하지 못했습니다.

**진행하려면 필요한 것:**
- 허가사항(첨부문서) 확인: 경고, 금기, 특히 간기능 관련 주의사항 (현재 확보되지 않음)
- 상세한 약물 작용 기전 데이터 (DrugBank 등)
- GAD 위약대조 시험(PMID 24569045)과 메타분석(PMID 32702221, 38804215)의 원문 결과 검토
- 한국 허가 적응증 본문 확인 및 불안장애 적응증 확대를 위한 국내 근거 검토

**참고:** 같은 예측 목록의 주요우울장애·단극성 우울증은 기존 적응증과 동일하거나 거의 같은 질환이므로 재창출 대상이 아닙니다. 멜랑콜리아, 신경증적 우울증, 내인성 우울증은 우울증 근거를 이어받은 항목으로, 해당 아형에 대한 직접 시험은 없습니다. 소아 양성 발작성 사경, 광장공포증, 오도 증후군은 근거가 없거나 기전상 연결이 불분명하여 보류(Hold)가 적절합니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

