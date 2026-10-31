---
layout: default
title: Dipyridamole
parent: 모델 예측만 (L5)
nav_order: 283
evidence_level: L5
indication_count: 8
monitor_inn: "DIPYRIDAMOLE"
predicted_indications: ["thrombotic disease", "sick sinus syndrome 2, autosomal dominant", "transient ischemic attack (disease)", "sarcoglycanopathy", "Wildervanck syndrome", "macrocephaly, dysmorphic facies, and psychomotor retardation", "lateral sinus thrombosis", "cavernous sinus thrombosis"]
last_modified_at: 2026-10-31
description: "Dipyridamole: 예측 신규 적응증 혈전성 질환 (근거 수준 L5). 기존 적응증: 확인 불가 (허가증 문서 링크만 있고 적응증 본문이 없음)"
---

# Dipyridamole
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **8** 건
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

## Dipyridamole: 허가 적응증 문서 미확인 상태에서 혈전성 질환으로
{: .text-alpha }

## 한 문장 요약

Dipyridamole은 혈소판 응집을 억제하는 항혈소판 계열 약물로, 한국에서 5건의 허가증이 확인됩니다. 다만 허가 적응증 본문은 이번 데이터에 포함되지 않았습니다. TxGNN 모델은 **혈전성 질환(thrombotic disease)** 에 효과가 있을 수 있다고 예측합니다. 이 질환을 직접 다룬 임상시험은 없고, 문헌도 대부분 항혈소판제 전반을 다룬 오래된 종설이어서 근거는 **모델 예측 수준(L5)** 입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (허가증 문서 링크만 있고 적응증 본문이 없음) |
| 예측 신규 적응증 | 혈전성 질환 |
| TxGNN 예측 점수 | 0.9994 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 4건 / 전체 5건) |
| 허가증 수 | 5건 (유효 4건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

Dipyridamole은 아데노신 재흡수(ENT1)와 포스포디에스테라제(PDE3/PDE5/PDE10)를 억제합니다. 그 결과 혈소판 내 cAMP와 cGMP가 증가하고 혈소판 응집이 억제됩니다. 이는 항혈전 효과로 이어지는 잘 알려진 기전이며, 이 약은 심장판막 치환술 후 혈전색전 합병증의 보조요법으로도 쓰입니다. 혈소판이 관여하는 혈전성 질환에 적용될 가능성은 기전상 충분히 설명됩니다.

다만 "혈전성 질환"은 범위가 매우 넓은 용어입니다. 제시된 문헌은 특정 질환이나 환자군을 겨냥하지 않은 항혈소판제 일반 종설이 중심입니다. 동맥 혈전과 정맥 혈전은 치료 원칙이 다르기 때문에, 이 예측을 바로 임상 적응증으로 해석하기는 어렵습니다.

## 임상시험 근거

현재 이 질환과 관련해 등록된 임상시험이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [18174451](https://pubmed.ncbi.nlm.nih.gov/18174451/) | 2008 | Review | Arterioscler Thromb Vasc Biol | Dipyridamole이 PDE 억제로 cAMP/cGMP를 높여 혈소판 응집과 혈소판 매개 혈전성 질환을 억제한다고 정리 |
| [12765506](https://pubmed.ncbi.nlm.nih.gov/12765506/) | 2003 | Review | Med J Aust | 항혈소판제가 심근경색, 뇌졸중 등 심각한 혈관 사건을 줄인다고 정리 (아스피린이 1차 약제) |
| [382146](https://pubmed.ncbi.nlm.nih.gov/382146/) | 1979 | Review | Postgrad Med | 아스피린, dipyridamole, sulfinpyrazone이 사람에서 항혈전 효과를 보인다는 근거 검토 |
| [2182246](https://pubmed.ncbi.nlm.nih.gov/2182246/) | 1990 | Review | Clin Cardiol | 관상동맥 혈전에서 아스피린과 dipyridamole 병용의 효과와 한계 검토 |
| [25697566](https://pubmed.ncbi.nlm.nih.gov/25697566/) | 2015 | 미분류 | Curr Top Med Chem | Dipyridamole의 PDE 억제, 아데노신 재흡수 억제 기전과 항산화 활성 |
| [11945125](https://pubmed.ncbi.nlm.nih.gov/11945125/) | 2002 | 미분류 | Curr Med Chem | 혈전색전성 질환에서 항혈소판제의 최신 동향 |
| [15494585](https://pubmed.ncbi.nlm.nih.gov/15494585/) | 2004 | 미분류 | JAMA | 뇌혈관, 관상동맥, 말초동맥 질환에서 경구 항혈소판제의 재발 예방 효과 |
| [2096418](https://pubmed.ncbi.nlm.nih.gov/2096418/) | 1990 | 미분류 | Rev Med Interne | 동맥 혈전 예방에서 항응집제 사용 (프랑스어 문헌) |
| [2440111](https://pubmed.ncbi.nlm.nih.gov/2440111/) | 1987 | 미분류 | Semin Hematol | 혈전성 혈소판감소성 자반증(TTP)에서 항혈소판 치료 (다른 질환) |
| [559478](https://pubmed.ncbi.nlm.nih.gov/559478/) | 1977 | 증례 | Arch Intern Med | TTP 환자 2명 중 1명에서 aspirin, dipyridamole 등 투여 후 혈소판 회복과 관해. dipyridamole 감량 시 재발 (다른 질환) |

검색 결과에는 이 질환과 무관한 항목(예: 중피종에 대한 bevacizumab 3상 시험)도 섞여 있어 표에서 제외했습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200302190 | 디피라몰정12.5밀리그람 (수출용) | 등적색 원형 당의정 | 적응증 본문 없음 (허가 문서 링크만 확인) |
| 200403295 | 디피라몰정25밀리그람 (수출용) | 등적색 원형 당의정 | 적응증 본문 없음 (허가 문서 링크만 확인) |
| 201600889 | 아디녹스캡슐 | 아스피린 당의정과 dipyridamole 펠렛을 담은 캡슐 | 적응증 본문 없음 (허가 문서 링크만 확인) |
| 201702431 | 스트록스타서방캡슐 | 아스피린 당의정과 dipyridamole 펠렛을 담은 캡슐 | 적응증 본문 없음 (허가 문서 링크만 확인) |
| 201702432 | 디피아녹스서방캡슐 | 아스피린 당의정과 dipyridamole 펠렛을 담은 캡슐 | 적응증 본문 없음 (허가 문서 링크만 확인) |

- 5건 모두 단일 성분으로 분류되어 있으나, 아디녹스, 스트록스타, 디피아녹스는 제형 설명상 아스피린과 dipyridamole이 함께 들어 있는 복합 제형으로 보입니다. 이 제품들의 허가 사항을 dipyridamole 단일 성분의 허가 현황으로 해석해서는 안 됩니다.
- 디피라몰정 2건은 수출용 허가입니다.

## 안전성 고려사항

허가사항(경고, 금기)의 상세 내용은 이번 데이터에 포함되지 않았습니다. 허가 문서를 직접 확인해야 합니다.

- **지식그래프상 금기 관계(허가 문서 기반 아님)**: TxGNN 지식그래프에 신장 질환, 간 질환, 혈소판감소증, 소화성 궤양, 저혈압, 통풍, 혈우병, 급성 관상동맥 증후군, 심근경색, 빈혈, 위염, Reye 증후군 등 다수 질환이 금기 관계로 기록되어 있습니다. 허가 문서로 검증되지 않았으므로 참고용입니다.
- **약물 상호작용**: 총 100건이 기록되어 있고, 이 중 확인된 20건 가운데 중등도로 분류된 것은 dexfenfluramine, sibutramine, fenfluramine입니다. 나머지 17건은 등급이 미분류입니다. 여기에는 acetylsalicylic acid, cimetidine, omeprazole, pantoprazole, lansoprazole, metformin, glimepiride, morphine, simvastatin 등이 포함됩니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
항혈전 기전은 타당하지만, "혈전성 질환"이라는 광범위한 용어에 대해 직접 연구한 임상시험이나 문헌이 없습니다. 제시된 문헌은 간접적이고 오래된 종설이 대부분이며, 안전성 판단에 필요한 허가사항도 확인되지 않았습니다.

**진행하려면 필요한 것:**
- 허가 문서에서 경고, 금기, 적응증 본문을 확인하고, 아스피린 복합제와 단일 성분 제품을 구분
- 대상 질환을 구체화 (예: 동맥 혈전, 정맥 혈전, 특정 혈전성 질환별로 나누어 평가)
- 구체화한 질환에 대한 직접 임상시험 및 문헌 검색
- 출혈 위험과 항응고제, 다른 항혈소판제와의 상호작용 검토

**참고:** 이번 데이터에는 "일과성 뇌허혈 발작(TIA)"이라는 다른 예측 질환에 대해 대규모 임상시험(ESPRIT, 4,500명)과 메타분석이 정리되어 있습니다. 평가 대상을 TIA로 구체화하면 이 보고서보다 훨씬 강한 근거를 바탕으로 별도 평가를 진행할 수 있습니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

