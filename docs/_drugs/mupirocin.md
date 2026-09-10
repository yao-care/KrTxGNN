---
layout: default
title: Mupirocin
parent: 僅模型預測 (L5)
nav_order: 491
evidence_level: L5
indication_count: 10
---

# Mupirocin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Mupirocin: 포도상구균 피부감염(국소 항생제)에서 포도상구균성 열상피부증후군(SSSS)으로

## 한 문장 요약

Mupirocin은 그람양성균, 특히 황색포도상구균(S. aureus)에 작용하는 국소 항생제로, 문헌상 농가진 등 포도상구균성 피부감염 치료에 사용되어 온 약물입니다(약물 자체의 공식 적응증 데이터는 현재 확보되지 않음). TxGNN 모델은 여러 적응증을 예측했으며, 이 중 실제 근거 수준이 가장 높은 것은 **포도상구균성 열상피부증후군(Staphylococcal Scalded Skin Syndrome, SSSS)**으로, 예측 점수 95.57%에 **14편의 문헌**(코호트 연구 포함)이 이를 뒷받침합니다. 단, TxGNN 최고 점수 예측인 늑막농흉(99.49%)은 임상시험·문헌 근거가 전무해 실제로는 반대로 근거 수준이 가장 낮았습니다 — 점수만으로 우선순위를 판단하면 안 되는 사례입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 공식 데이터 없음 (문헌상 포도상구균성 피부감염症 국소 치료로 파악, 예: 농가진) |
| 예측 신규 적응증 | 포도상구균성 열상피부증후군 (Staphylococcal Scalded Skin Syndrome, SSSS) |
| TxGNN 예측 점수 | 95.57% |
| 근거 수준 | L3 |
| 시판 현황 | ✗ 미상장 (허가증 0건) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 Mupirocin의 상세한 작용 기전(MOA) 공식 데이터는 확보되지 않았습니다(데이터 갭). 다만 근거팩 내 문헌(PMID 8222720)에 따르면 Mupirocin은 메티실린 감수성/내성 황색포도상구균(MSSA/MRSA)을 포함한 그람양성 구균에 대해 강한 항균 활성(낮은 MIC90)을 보이는 국소 항생제입니다.

SSSS는 표피박리독소(exfoliative toxin A/B)를 생성하는 황색포도상구균 감염이 근본 원인인 질환입니다. 따라서 원인균인 S. aureus를 표적으로 하는 Mupirocin을 국소 제균(decolonization) 또는 병변 부위 도포 목적으로 전신 항생제와 병용하는 것은 기전상 합리적입니다. 실제로 근거팩의 코호트 연구(PMID 37404367)는 정맥 항생제와 2% Mupirocin 연고를 병용한 소아 SSSS 치료 결과를 직접 다루고 있어, 이미 임상 현장에서 통용되는 병용요법임을 시사합니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [37404367](https://pubmed.ncbi.nlm.nih.gov/37404367/) | 2023 | 코호트 | Clin Cosmet Investig Dermatol | 정맥 항생제 + 2% Mupirocin 연고 병용 시 소아 SSSS 치료기간·비용에 미치는 영향 분석 |
| [8435912](https://pubmed.ncbi.nlm.nih.gov/8435912/) | 1993 | Review | Dermatologic Clinics | 포도상구균성 피부질환 관리에서 국소 Mupirocin이 유용한 최신 치료 옵션으로 언급 |
| [28592549](https://pubmed.ncbi.nlm.nih.gov/28592549/) | 2017 | 증례/분자역학 | J Clin Microbiol | Mupirocin·푸시드산 내성 S. aureus 클론이 피부연조직감염 주요 원인균으로 출현 |
| [30418106](https://pubmed.ncbi.nlm.nih.gov/30418106/) | 2019 | 증례보고 | J Med Microbiol | Mupirocin·푸시드산 내성 신규 독소생성 MSSA 클론에 의한 SSSS 발생 증가 |
| [15482208](https://pubmed.ncbi.nlm.nih.gov/15482208/) | 2004 | Review/증례군 | Expert Rev Anti Infect Ther | 영아 수포성 농가진 및 SSSS 치료 개관 |
| [16218885](https://pubmed.ncbi.nlm.nih.gov/16218885/) | 2005 | Review(추정) | Expert Opin Pharmacother | 소아 농가진 치료 옵션 개관 |
| [19000857](https://pubmed.ncbi.nlm.nih.gov/19000857/) | 2008 | Review(추정) | Arch Pediatr | 소아 피부·연조직 감염 관리 |
| [35901469](https://pubmed.ncbi.nlm.nih.gov/35901469/) | 2022 | 증례군 | Adv Neonatal Care | 신생아 MSSA 감염(SSSS 포함) 증례 및 상처관리 |
| [16009455](https://pubmed.ncbi.nlm.nih.gov/16009455/) | 2005 | 코호트(집단발생 조사) | J Hosp Infect | 신생아 병동 내 SSSS 원내 집단발생 역학조사 및 관리 |
| [9576389](https://pubmed.ncbi.nlm.nih.gov/9576389/) | 1998 | 코호트 | Pediatr Infect Dis J | 미숙아 SSSS 분자역학 및 감염관리 전략 |

*(전체 14편 중 관련성 높은 10편을 표시했습니다.)*

## 시판 정보

현재 등록된 시판 허가가 없습니다 (미상장, 허가증 0건).

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. (현재 주요 경고, 금기, 약물상호작용 데이터가 확보되지 않았습니다 — TFDA 첨부문서 확보가 Blocking 데이터 갭으로 지정되어 있습니다.)

## 결론 및 다음 단계

**결정: Hold**

**사유:**
SSSS 적응증은 기전상 타당하고 코호트 연구를 포함한 L3 수준 문헌 근거가 있어 조사 가치가 있으나, (1) 안전성 라벨 정보 부재가 "Blocking" 등급 데이터 갭으로 지정되어 S1 안전성 초기평가 자체를 진행할 수 없고, (2) 해당 시장에 허가증이 전혀 없어(미상장) 즉시 재창출을 추진할 기반이 없습니다.

**진행하려면 필요한 것:**
- TFDA 공식 첨부문서(경고/금기/DDI) 확보 — S1 안전성 초기평가 진입을 위한 선결 조건
- DrugBank 등에서 상세 작용기전(MOA) 데이터 확보
- SSSS 적응증에 특화된 대조군 임상연구(코호트 이상) 추가 확인
- 국내 시판/허가 경로(신규 허가 또는 병행수입) 검토
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

