---
layout: default
title: Cilastatin
parent: 모델 예측만 (L5)
nav_order: 212
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Cilastatin: 예측 신규 적응증 세균성 관절염 (bacterial arthritis) (근거 수준 L5). 기존 적응증: 허가 적응증 본문이 확인되지 않음 (허가 정보에 문서 링크만 등록되어 있음)"
monitor_inn: "Cilastatin"
predicted_indications: ["staphylococcus aureus infection", "chronic rhinosinusitis", "chronic ethmoidal sinusitis", "sinusitis", "paranasal sinus neoplasm (disease)", "paratyphoid fever", "bronchitis"]
---

# Cilastatin
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

# Cilastatin: 세균성 관절염으로의 재창출 평가 (기존 적응증 정보 확인 필요)

## 한 문장 요약

Cilastatin은 신장 디하이드로펩티다제-I(DHP-1)을 억제하여 imipenem의 분해를 막는 약물이며, 항균 활성은 없습니다. TxGNN 모델은 **세균성 관절염(bacterial arthritis)**을 1순위 신규 적응증으로 예측했고, 이 예측에는 임상시험 0건과 **문헌 17편**이 연결되어 있습니다. 다만 이 근거는 대부분 imipenem/cilastatin 복합제에 대한 것이어서, cilastatin 단독의 효과를 뜻하지는 않습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문이 확인되지 않음 (허가 정보에 문서 링크만 등록되어 있음) |
| 예측 신규 적응증 | 세균성 관절염 (bacterial arthritis) |
| TxGNN 예측 점수 | 99.98% |
| 근거 수준 | L3 (소규모 임상 연구와 증례 보고 중심, 대조 임상시험 없음) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | Hold (추가 근거 확보 시까지 연구 질문 단계 유지) |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 수집되지 않았습니다. 다만 약리학 데이터에 따르면 cilastatin은 DHP-1 억제제로, imipenem과 고정 용량 복합제로 투여되어 imipenem의 효과를 높입니다. Cilastatin 자체에는 항균 작용이 없습니다.

따라서 예측된 세균성 관절염에 대한 효능은 imipenem/cilastatin 복합제에서 비롯된 것입니다. Imipenem은 광범위 항균제이며 뼈와 관절 활막 조직으로 침투하므로, 화농성 관절염과 골수염에 적용할 수 있다고 볼 수 있습니다. 이 신호는 cilastatin 단독이 아니라 복합제에 귀속됩니다.

## 임상시험 근거

세균성 관절염에 대해 등록된 관련 임상시험은 현재 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [3544811](https://pubmed.ncbi.nlm.nih.gov/3544811/) | 1987 | 임상 연구 (소아, 비대조) | Am J Dis Child | 급성 골수염·화농성 관절염 소아 25명에서 imipenem/cilastatin 치료 |
| [3464787](https://pubmed.ncbi.nlm.nih.gov/3464787/) | 1986 | 임상 연구 | Jpn J Antibiot | 골·관절 감염 30례에서 imipenem/cilastatin의 전체 치유율 87% (급성 96%, 만성 50%) |
| [3904406](https://pubmed.ncbi.nlm.nih.gov/3904406/) | 1985 | 임상 연구 (소아 감염) | Am J Dis Child | 입원 소아 40명의 세균 감염에서 imipenem/cilastatin의 효능과 독성 평가 |
| [7843815](https://pubmed.ncbi.nlm.nih.gov/7843815/) | 1994 | 증례 보고 | Infection | Bacteroides fragilis에 의한 고관절 화농성 관절염을 imipenem/cilastatin과 metronidazole 등으로 치료 |
| [26020393](https://pubmed.ncbi.nlm.nih.gov/26020393/) | 2015 | 증례 보고 | Medicine | 화농성 관절염 후 파종성 Mycobacterium abscessus 감염 |
| [37718611](https://pubmed.ncbi.nlm.nih.gov/37718611/) | 2023 | 증례 보고 | Mod Rheumatol Case Rep | 골관절 증상을 보인 파종성 M. abscessus 감염 |
| [36550469](https://pubmed.ncbi.nlm.nih.gov/36550469/) | 2022 | 증례 보고 | BMC Infect Dis | Ureaplasma parvum 화농성 관절염 환자의 고암모니아혈증 |
| [11869242](https://pubmed.ncbi.nlm.nih.gov/11869242/) | 1997 | 리뷰 | Clin Microbiol Infect | 패혈증 치료 개관 |
| [36804370](https://pubmed.ncbi.nlm.nih.gov/36804370/) | 2023 | 리뷰 | Int J Antimicrob Agents | 다제내성균 감염에 대한 항생제의 허가 외 사용과 공식 권고 비교 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200201807 | 실라신주사500밀리그램 | 흰색 또는 연한 노란색 가루가 바이알에 든 주사제 | 허가 적응증 본문 미확인 (문서 링크만 등록) |

## 안전성 고려사항

- **약물 상호작용**: 약리학 데이터상 cilastatin은 Dipeptidase 1(DHP-1)을 표적으로 하는 억제제이며, imipenem과 복합제로 사용됩니다. 별도의 약물 간 상호작용 등급은 제공되지 않았습니다.

그 밖의 경고와 금기는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
세균성 관절염에 대한 근거는 1980~90년대의 소규모 비대조 연구와 증례 보고가 중심이며, 효과는 cilastatin이 아니라 imipenem에서 나옵니다. 또한 허가 적응증과 안전성 정보가 확인되지 않아 평가를 진행하기 어렵습니다.

**참고: 다른 예측 적응증**
- **폐렴**: 3상 RCT가 다수 있어 근거 수준은 L1입니다. 다만 이는 imipenem/cilastatin 복합제의 근거이며, 이미 허가된 용도에 가까워 엄밀한 의미의 재창출은 아닐 가능성이 높습니다. 일부 시험은 제목이 잘려 있어, 해당 약이 시험약인지 대조약인지 배경 요법인지 확인이 필요합니다.
- **황색포도알균 감염, 기관지염, 폐렴구균 폐렴**: 오래된 임상 연구가 중심(L3)입니다. 카바페넴은 내성균이나 중증 감염에 아껴 써야 하므로, 일상적 사용은 항생제 관리 원칙과 맞지 않습니다.
- **만성 비부비동염, 만성 사골동염, 부비동 종양, 파라티푸스**: TxGNN 점수 외에 근거가 없어 보류합니다. 부비동 종양은 생물학적 근거도 없습니다.

**진행하려면 필요한 것:**
- 허가 적응증 본문과 경고·금기 사항 확보 (MFDS 허가사항 PDF 확인)
- 작용 기전 데이터 보완 (DrugBank 조회)
- 세균성 관절염에서 imipenem/cilastatin 복합제의 효능을 평가한 대조 연구 확인
- 폐렴 관련 시험에서 imipenem/cilastatin의 역할(시험약, 대조약, 배경 요법) 확인 및 기존 허가 적응증 포함 여부 검증
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

