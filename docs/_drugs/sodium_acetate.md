---
layout: default
title: Sodium Acetate
parent: 모델 예측만 (L5)
nav_order: 695
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Sodium Acetate: 예측 신규 적응증 선천성 프로트롬빈 결핍증 (congenital prothrombin deficiency) (근거 수준 L5). 기존 적응증: 허가증에 적응증 원문 텍스트가 아닌 허가사항 문서 링크만 확인되어 구체적인 적응증을 기재할 수 없음 (제품 구성상 복막투석액…"
monitor_inn: "SODIUM ACETATE"
predicted_indications: ["congenital prothrombin deficiency", "epiglottitis", "urinary tract infection (disease)", "sclerosing cholangitis", "Ureaplasma urethritis", "gonococcal urethritis", "dyspepsia", "uterine inflammatory disease", "gastroparesis (disease)", "xanthogranulomatous pyelonephritis"]
---

# Sodium Acetate
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

## Sodium Acetate: 전해질 보충·복막투석에서 선천성 프로트롬빈 결핍증으로
{: .text-alpha }

## 한 문장 요약

Sodium acetate(아세트산나트륨)는 나트륨과 중탄산염 전구체를 공급하는 전해질·알칼리화 성분으로, 한국에서는 복막투석액 성분과 주사제로 허가되어 있습니다.
TxGNN 모델은 **선천성 프로트롬빈 결핍증(congenital prothrombin deficiency)**에 효과가 있을 수 있다고 예측하지만, 이를 지지하는 **임상시험은 0건, 문헌도 0편**입니다.
모델 점수만 높을 뿐 기전적 근거가 없어 현 단계에서는 보류(Hold)를 권장합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가증에 적응증 원문 텍스트가 아닌 허가사항 문서 링크만 확인되어 구체적인 적응증을 기재할 수 없음 (제품 구성상 복막투석액 및 아세트산나트륨 주사제) |
| 예측 신규 적응증 | 선천성 프로트롬빈 결핍증 (congenital prothrombin deficiency) |
| TxGNN 예측 점수 | 99.98% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 4건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Sodium acetate는 전해질·알칼리화 제제로, 체내에서 대사되어 중탄산염을 생성하는 나트륨 공급원입니다.

선천성 프로트롬빈 결핍증은 응고인자 II의 유전적 결핍으로 생기는 출혈성 질환입니다. 이 약은 프로트롬빈 합성이나 응고인자 보충과 관련된 알려진 역할이 없으므로 기전상 연결고리를 찾을 수 없습니다. 높은 TxGNN 점수는 지식 그래프에서 생긴 인공적 결과일 가능성이 큽니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

예측 1순위 적응증(선천성 프로트롬빈 결핍증)에 관한 문헌은 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 199403160 | 다이아닐저칼슘피디액4.25% (밴티브코리아) | 복막투석액 (PVC 백) | 허가사항 문서 참조 |
| 199403159 | 다이아닐저칼슘피디액2.5% (밴티브코리아) | 복막투석액 (PVC 백) | 허가사항 문서 참조 |
| 199403158 | 다이아닐저칼슘피디액1.5% (밴티브코리아) | 복막투석액 (PVC 백) | 허가사항 문서 참조 |
| 202503115 | 네오나트륨주(아세트산나트륨) (한국팜비오) | 주사제 (바이알) | 허가사항 문서 참조 |

## 안전성 고려사항

- **약물 상호작용**: 총 30건이 확인되었으며, 주요 항목은 다음과 같습니다.
  - 중등도: Doxycycline, Tetracycline, Minocycline, Acetylsalicylic acid, Choline salicylate, Ephedrine, Pseudoephedrine, Amphetamine, Dextroamphetamine, Benzphetamine, Methenamine
  - 경미: Chlorpropamide, Tolazamide, Glipizide, Glyburide, Acetohexamide, Tolbutamide, Memantine, Methotrexate
- **지식그래프 기반 금기 질환 (허가사항 문구가 아닌 모델 데이터)**: 신장질환(만성 신부전, 말기 신부전, 무뇨 포함), 고칼슘혈증, 신석회화증, 신결석증, 심장질환·심혈관질환, 방실차단, 심실세동, 디기탈리스 중독, 고칼륨혈성 주기성 마비, 저알도스테론증, 페닐케톤뇨증, 사르코이드증 등.

허가사항상의 경고 및 금기는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
선천성 프로트롬빈 결핍증에 대한 임상시험과 문헌이 전혀 없고, 기전적 연결도 확인되지 않아 근거 수준은 L5(모델 예측만 존재)입니다. 상위 10개 예측 적응증 전체가 같은 평가(Hold)이며, 문헌이 있는 소화불량과 위마비도 이 약을 치료제로 평가한 연구가 아니라 아세트산나트륨을 위배출 호흡검사의 추적자로 사용한 연구로 보입니다.

**진행하려면 필요한 것:**
- 허가사항(허가증 PDF)에서 적응증, 경고, 금기 확인
- 작용 기전(MOA) 데이터 보완
- 예측 적응증에 대한 전임상 또는 기전 연구 근거 확보
- 신장 및 심장 질환 환자에 대한 안전성 검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

