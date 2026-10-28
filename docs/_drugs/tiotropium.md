---
layout: default
title: Tiotropium
parent: 모델 예측만 (L5)
nav_order: 739
evidence_level: L5
indication_count: 4
monitor_inn: "tiotropium"
predicted_indications: ["respiratory malformation", "Rienhoff syndrome", "hyperlucent lung", "tracheal stenosis"]
last_modified_at: 2026-10-28
description: "Tiotropium: 예측 신규 적응증 호흡기 기형 (근거 수준 L5). 기존 적응증: 확인 불가 (허가 적응증 본문 없이 허가문서 링크만 제공됨)"
---

# Tiotropium
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **4** 건
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

## Tiotropium: 허가 적응증 확인 불가에서 호흡기 기형(Respiratory Malformation)으로
{: .text-alpha }

## 한 문장 요약

Tiotropium은 장기 지속형 무스카린 길항제(LAMA)로 흡입제 형태로 한국에서 허가되어 있으나, 이번 자료에는 허가 적응증 본문이 담겨 있지 않고 허가문서 링크만 있습니다.
TxGNN 모델은 **호흡기 기형(Respiratory Malformation)**에 효과가 있을 수 있다고 예측하지만, 이 질환 자체를 직접 연구한 임상시험이나 문헌은 확인되지 않았습니다.
연결된 임상시험 3건은 모두 낭포성 섬유증 환자 대상이고, 문헌 5편은 COPD 등 다른 질환 관련이어서 근거 수준은 **L5(모델 예측 단계)**입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (허가 적응증 본문 없이 허가문서 링크만 제공됨) |
| 예측 신규 적응증 | 호흡기 기형 |
| TxGNN 예측 점수 | 0.9995 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 3건 (모두 단일제, 유효) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 없습니다. 일반적으로 알려진 바로는 tiotropium은 기관지 평활근의 M3 무스카린 수용체를 차단해 기관지를 확장시키는 LAMA 계열 약물입니다. 이 점에서 기도 폐쇄가 동반된 질환에서 증상 완화를 기대해 볼 수 있습니다.

다만 이는 간접적인 추정입니다. 호흡기 기형은 구조적 이상이며, 기관지 확장이 기형 자체에 도움이 된다는 근거는 없습니다. 0.9995라는 높은 TxGNN 점수는 모델의 계산 결과일 뿐 임상적 근거가 아닙니다. 연결된 시험과 문헌은 낭포성 섬유증이나 COPD 같은 폐쇄성 기도질환을 다루며, 선천성 호흡기 기형을 다룬 연구는 아닙니다.

## 임상시험 근거

아래 시험은 모두 낭포성 섬유증 환자 대상으로, 호흡기 기형을 직접 연구한 시험은 아닙니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01179347](https://clinicaltrials.gov/study/NCT01179347) | Phase 3 | 완료 | 464 | 낭포성 섬유증 환자에서 tiotropium 5 mcg(Respimat) 12주 효능·안전성 위약 대조 시험 |
| [NCT00737100](https://clinicaltrials.gov/study/NCT00737100) | Phase 2 | 완료 | 510 | 낭포성 섬유증 환자에서 tiotropium 2.5/5 mcg 12주 폐기능 효과 및 용량 선택 |
| [NCT02172534](https://clinicaltrials.gov/study/NCT02172534) | Phase 1 | 완료 | 113 | 소아·청소년·성인 낭포성 섬유증 환자에서 단회·반복 투여 안전성, 내약성, 약동학 |

## 문헌 근거

아래 문헌은 대부분 COPD 등 다른 질환을 다루며, 호흡기 기형에 대한 직접 근거로 보기 어렵습니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [31522031](https://pubmed.ncbi.nlm.nih.gov/31522031/) | 2019 | RCT (생리학적, COPD) | Respiratory Medicine | COPD에서 tiotropium/olodaterol에 의한 폐 과팽창 감소가 운동 시 심순환 반응에 미치는 영향 |
| [26229457](https://pubmed.ncbi.nlm.nih.gov/26229457/) | 2015 | Review | Int J Chron Obstruct Pulmon Dis | COPD에서 indacaterol-glycopyrronium 이중 기관지 확장 요법의 역할 |
| [22608352](https://pubmed.ncbi.nlm.nih.gov/22608352/) | 2012 | Cohort | Respiratory Medicine | COPD 환자의 비강 섬모 운동이 감소함 |
| [40850565](https://pubmed.ncbi.nlm.nih.gov/40850565/) | 2025 | 전임상/기전 | Chemico-biological Interactions | 유기인계 신경작용제에 노출된 마우스의 환기 기능 장애 기전 |
| [33787023](https://pubmed.ncbi.nlm.nih.gov/33787023/) | 2021 | Case report | Rev Fac Cienc Med (Córdoba) | 누두흉이 있는 젊은 환자의 COVID-19 감염 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201506154 | 바헬바레스피맷 | 흡입용 액제(카트리지, 레스피맷 흡입기) | 허가문서 링크만 제공되어 적응증 본문 확인 불가 |
| 200811444 | 스피리바레스피맷(티오트로퓸브롬화물수화물) | 흡입용 액제(카트리지, 레스피맷 흡입기) | 허가문서 링크만 제공되어 적응증 본문 확인 불가 |
| 200209849 | 스피리바흡입용캡슐(티오트로퓸브롬화물수화물) | 흡입용 캡슐(핸디핼러) | 허가문서 링크만 제공되어 적응증 본문 확인 불가 |

## 안전성 고려사항

- **지식그래프상 금기 관계**: 지식그래프에 기록된 금기 관계는 양성 전립선 비대증, 신기능 장애, 협우각 녹내장(폐쇄각 녹내장), 방광 경부 폐색입니다. 허가 문서 본문이 아니라 지식그래프 기록이므로 허가사항 확인이 필요합니다.
- **약물 상호작용**: 총 430건이 조회되었습니다. 주요 항목은 다음과 같습니다.
  - 중등도: 다른 항콜린제인 hyoscyamine, atropine, glycopyrronium, clidinium, dicyclomine, trospium, scopolamine, propantheline, methscopolamine, mepenzolate 등. 또한 eluxadoline, prucalopride, 흡입 인슐린.
  - 경미: cimetidine.
  - 등급 불명: calcitriol, pantoprazole, glimepiride, mesalazine, doxycycline.

허가사항의 경고 및 주의사항은 이번 자료에서 확인되지 않았으므로 허가문서를 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
호흡기 기형을 직접 연구한 임상시험이나 문헌이 없고, 근거는 TxGNN 모델 예측뿐이어서 L5입니다. 연결된 시험은 낭포성 섬유증, 문헌은 주로 COPD를 다루며 기전적 연결도 간접적입니다. 같은 모델이 제시한 Rienhoff 증후군, 과투과성 폐, 기관 협착 예측도 임상시험과 문헌이 없어 L5입니다.

**진행하려면 필요한 것:**
- 허가문서에서 허가 적응증, 경고, 금기 본문 확보 (허가사항 확인이 선행되어야 안전성 검토 가능)
- 작용 기전(MOA) 데이터 보완
- 호흡기 기형 환자를 대상으로 한 직접적인 임상 또는 관찰 연구 근거 확인
- 호흡기 기형 중 기도 반응성이 동반된 하위군이 있는지 정의하고 기관지 확장제 반응성 평가
- 한국 시판 현황(취소 여부 포함) 확인
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

