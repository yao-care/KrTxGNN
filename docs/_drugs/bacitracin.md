---
layout: default
title: Bacitracin
parent: 모델 예측만 (L5)
nav_order: 120
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Bacitracin: 예측 신규 적응증 점상 상피성 각결막염 (punctate epithelial keratoconjunctivitis) (근거 수준 L5). 기존 적응증: 경미한 베인 상처, 긁힌 상처, 화상의 감염 방지"
monitor_inn: "Bacitracin"
predicted_indications: ["otitis externa", "postinfectious vasculitis", "post-bacterial disorder", "infective urethral stricture", "post-infectious syndrome", "infection-related hemolytic uremic syndrome", "Chagas cardiomyopathy"]
---

# Bacitracin
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

# Bacitracin: 경미한 상처·화상의 감염 방지에서 점상 상피성 각결막염으로

## 한 문장 요약

Bacitracin은 폴리펩타이드 계열의 국소 항생제로, 원래 경미한 베인 상처, 긁힌 상처, 화상의 감염 방지에 사용되었습니다.
TxGNN 모델은 **점상 상피성 각결막염(punctate epithelial keratoconjunctivitis)**에 효과가 있을 수 있다고 예측하지만, 현재 이 방향을 지지하는 **임상시험은 0건, 문헌도 0편**입니다. 모델 예측 단계의 가설입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 경미한 베인 상처, 긁힌 상처, 화상의 감염 방지 |
| 예측 신규 적응증 | 점상 상피성 각결막염 (punctate epithelial keratoconjunctivitis) |
| TxGNN 예측 점수 | 99.999% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 8건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Bacitracin은 그람 양성균에 활성을 보이는 국소 폴리펩타이드 항생제이며, 경미한 상처와 화상의 감염을 방지하는 데 쓰이고 있습니다. 안과용 제형도 존재합니다.

다만 점상 상피성 각결막염은 바이러스성이거나 독성·염증성인 경우가 많아, 직접적인 항균 기전과의 연관성은 약합니다. 각막 상피 손상 부위에서 2차 세균 감염을 예방하는 용도는 이론상 가능하지만 이를 뒷받침하는 자료가 없습니다. 99.999%의 높은 점수는 계산에 의한 예측일 뿐입니다.

참고로 같은 분석에서 두 번째로 예측된 노출성 각막염(exposure keratitis)도 건조로 인한 각막 상피 손상 후 2차 감염 위험이라는 간접적 논리에 그치며, 근거 수준은 L5입니다. 상위 10개 예측 중 문헌이 확인된 것은 외이도염(otitis externa)뿐입니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 198200799 | 바스포연고 | 연고제 (백색~담갈색) | 경미한 베인 상처, 긁힌 상처, 화상의 감염 방지 |
| 198200102 | 바네포연고 | 연고제 (백색~미황색) | 경미한 베인 상처, 긁힌 상처, 화상의 감염 방지 |
| 201400018 | 폴리스포린연고(수출용) | 연고제 (반투명) | 수출용 제품 |
| 200300821 | 태극바시트라신연고(수출용) | 연고 (백색) | 수출용 제품 |
| 202202465 | 바르덤연고 | 연고제 (흰색~담갈색) | 허가 적응증 텍스트 확인 필요 |

## 안전성 고려사항

- **약물 상호작용**: 총 84건의 상호작용이 확인되었습니다. 주요(Major) 등급은 다음과 같습니다.
  - 아미노글리코사이드 계열: Kanamycin, Neomycin, Streptomycin
  - Deferasirox
  - 요오드 조영제: Diatrizoate, Iodipamide, Iodixanol, Iohexol
- 중등도(Moderate) 등급에는 Mesalazine, Balsalazide, Sulfasalazine, Olsalazine, Vancomycin, Exenatide, Picosulfuric acid 등이 있습니다.
- 참고로 전신 투여 Bacitracin은 신독성이 있어 비경구 사용이 중단되었습니다. 이는 위 상호작용 중 신독성 약물과의 병용 우려와도 관련됩니다.

경고 및 금기 사항은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
점상 상피성 각결막염에 대한 임상시험과 문헌이 전혀 없고, 항균 기전과 질환의 병인(바이러스성·독성·염증성)이 잘 맞지 않습니다. 높은 TxGNN 점수만으로는 진행 근거가 부족합니다.

**진행하려면 필요한 것:**
- 점상 상피성 각결막염에서 Bacitracin의 효과를 평가한 임상시험 또는 문헌
- 작용 기전(MOA) 데이터 (DrugBank 조회)
- 허가사항의 경고·금기 사항 (MFDS 첨부문서 확인)
- 안과용 제형 및 투여 경로의 적합성 검토. 한국 허가 제품은 모두 연고제이며, 안과용 허가는 확인되지 않았습니다.
- 대안 검토: 외이도염은 4편의 문헌(복합제 연고 대상 이중맹검 비교연구 1건 포함)이 있어 우선 검토할 만합니다. 다만 대부분 오래되었거나 간접적인 자료이고 근거 수준은 L4입니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

