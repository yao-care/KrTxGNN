---
layout: default
title: Defibrotide
parent: 모델 예측만 (L5)
nav_order: 257
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Defibrotide: 예측 신규 적응증 가성 폰 빌레브란트병 (pseudo-von Willebrand disease) (근거 수준 L5). 기존 적응증: 허가 적응증 본문을 확인할 수 없음 (허가 문서 링크만 제공됨)"
monitor_inn: "DEFIBROTIDE"
predicted_indications: ["pseudo-von Willebrand disease", "primary release disorder of platelets", "Glanzmann thrombasthenia", "thrombotic thrombocytopenic purpura", "Scott syndrome", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "congenital factor V deficiency", "fetal and neonatal alloimmune thrombocytopenia", "thrombocytopenic purpura"]
---

# Defibrotide
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

## Defibrotide: 허가 적응증에서 가성 폰 빌레브란트병으로
{: .text-alpha }

## 한 문장 요약

Defibrotide는 한국에서 「데피텔리오주200밀리그램」으로 허가·시판 중인 주사제입니다. 다만 허가 적응증 본문은 문서 링크로만 제공되어 구체적인 내용을 확인할 수 없었습니다.
TxGNN 모델은 최상위 예측으로 **가성 폰 빌레브란트병(pseudo-von Willebrand disease)**을 제시했지만(예측 점수 0.9991), 이를 지지하는 임상시험과 문헌은 **0건**입니다. 기전상으로도 출혈 위험을 키울 수 있어 신중한 접근이 필요합니다.
참고로 예측 순위 4위의 **혈전성 혈소판감소성 자반증(TTP)**에는 소규모 증례 및 증례군, 종설, 시험관 연구 등 **문헌 8편**이 있어 가장 현실적인 연구 후보입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문을 확인할 수 없음 (허가 문서 링크만 제공됨) |
| 예측 신규 적응증 | 가성 폰 빌레브란트병 (pseudo-von Willebrand disease) |
| TxGNN 예측 점수 | 0.9991 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Defibrotide는 항혈전·섬유소 용해 촉진 작용과 혈관내피 보호 작용을 가진 약물로 분류됩니다.

그러나 1순위 예측인 가성 폰 빌레브란트병은 GP1BA 기능획득 변이로 생기는 혈소판형 출혈성 질환이며, Defibrotide와의 기전적 연관성은 확인되지 않습니다. 오히려 항혈전·섬유소 용해 촉진 작용이 출혈 위험을 악화시킬 가능성이 있습니다.

상위 예측 대부분(원발성 혈소판 분비 장애, 글란츠만 혈소판무력증, Scott 증후군, 콜라겐 수용체 결함에 의한 출혈소인, 선천성 응고인자 V 결핍 등)도 출혈성 질환이어서 같은 우려가 적용됩니다. 높은 점수는 계산상의 예측일 뿐이며 임상적 타당성을 뜻하지 않습니다.

반면 TTP와 이식 관련 혈전성 미세혈관병증(TMA)은 내피 손상이 병태생리의 핵심이어서 내피 보호 작용으로 설명할 수 있는 생물학적 개연성이 있습니다. 다만 고전적 TTP는 ADAMTS13 결핍이 원인이며, 표준 치료(혈장 교환, caplacizumab, 면역억제)와는 기전이 다릅니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

1순위 예측(가성 폰 빌레브란트병)에는 관련 문헌이 없습니다. 아래는 4순위 예측인 TTP 항목의 문헌입니다. 10순위(혈소판감소성 자반증)도 거의 같은 문헌 세트를 공유하므로 중복해서 기재하지 않았습니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [30305540](https://pubmed.ncbi.nlm.nih.gov/30305540/) | 2018 | Review | Rinsho Ketsueki | 이식 관련 혈전성 미세혈관병증(TA-TMA)의 관리 |
| [17603513](https://pubmed.ncbi.nlm.nih.gov/17603513/) | 2007 | Review | Bone Marrow Transplant | TA-TMA의 진단과 치료 현황, 합의된 정의 부재 |
| [19228075](https://pubmed.ncbi.nlm.nih.gov/19228075/) | 2009 | Review | Drugs | 조혈모세포이식 후 TMA의 진단과 치료 (사망률 60–90%) |
| [10775024](https://pubmed.ncbi.nlm.nih.gov/10775024/) | 2000 | Case report | Clin Appl Thromb Hemost | 재발성 TTP에서 Defibrotide 사용 |
| [11960280](https://pubmed.ncbi.nlm.nih.gov/11960280/) | 2002 | Case series | Bone Marrow Transplant | 골수이식 환자의 TTP에서 Defibrotide의 가능성 제시 |
| [3754836](https://pubmed.ncbi.nlm.nih.gov/3754836/) | 1986 | Clinical report | Haemostasis | TMA로 인한 급성 신부전에서 Defibrotide의 효과 |
| [37001283](https://pubmed.ncbi.nlm.nih.gov/37001283/) | 2023 | In vitro | Thrombosis Research | COVID-19 및 관련 혈관병증 환자 혈장에 의한 내피세포 손상을 완화 |
| [7896218](https://pubmed.ncbi.nlm.nih.gov/7896218/) | 1994 | Case report (이상반응) | Haematologica | **Defibrotide 치료 후 TTP가 발생**한 보고 (안전성 신호) |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201600952 | 데피텔리오주200밀리그램(데피브로타이드) ((주)한독) | 주사제 (투명한 미황색-갈색 용액이 무색투명한 바이알에 든 제형) | 허가 문서 링크로만 제공되어 본문 확인 불가 |

## 세포독성

해당 없음(항종양약이 아님)으로 판단하여 생략합니다.

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 조회되었으며, 이 중 20건의 상세 정보가 확인되었습니다. 출혈 위험과 관련된 항혈전·항혈소판·혈전용해 계열이 다수 포함됩니다.
  - **Major**: Acetylsalicylic acid, Deferasirox, Ibritumomab tiuxetan, Tositumomab 및 Tositumomab (I-131), Abciximab, Acalabrutinib, Fondaparinux, Alteplase, Anagrelide
  - **Moderate**: Dexfenfluramine, Fenfluramine, Sibutramine, Ketorolac(전신 및 점안), Ibuprofen, Fluvoxamine, Diclofenac(외용), Celecoxib, Omega-3 fatty acids
- **예측 적응증 관련 우려**: 상위 예측 대부분이 출혈성 질환이어서 출혈 위험이 악화될 수 있습니다. 또한 Defibrotide 투여 후 TTP가 발생한 증례 보고(PMID 7896218)가 있어 인과관계 해석에 주의가 필요합니다.

경고 및 금기 등 허가사항 기반 안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
1순위 예측인 가성 폰 빌레브란트병은 임상시험과 문헌이 전무하고(L5), 기전상 연관성이 없으며 출혈 위험을 키울 수 있습니다. 상위 10개 예측 중 TTP 및 혈소판감소성 자반증만 L4 수준의 간접 근거가 있으나, 모두 소규모 증례, 종설, 시험관 연구에 그치며 이상반응 보고도 포함되어 있습니다. 이 두 항목은 독립된 근거가 아니라 같은 문헌을 공유하므로 하나의 연구 질문으로 함께 평가해야 합니다.

**진행하려면 필요한 것:**
- 허가 문서(PDF)에서 허가 적응증, 경고, 금기를 확인·정리 (현재 안전성 심사를 진행할 수 없는 차단 수준의 데이터 공백)
- DrugBank 등에서 작용 기전(MOA) 데이터 확보
- TTP/이식 관련 TMA 중심의 후속 평가: 체계적 문헌고찰, ADAMTS13 결핍형과 이식 관련 TMA를 구분한 분석, 전향적 연구 설계 검토
- 출혈성 질환 적응증에 대한 안전성 평가 (항혈전 작용에 따른 출혈 위험 분석)
- 항혈전·항혈소판제 병용 시 출혈 위험을 포함한 약물 상호작용 관리 계획
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

