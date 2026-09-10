---
layout: default
title: Felbinac
parent: 僅模型預測 (L5)
nav_order: 316
evidence_level: L5
indication_count: 10
---

# Felbinac
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

# Felbinac: 근골격계 연조직 손상에서 관절병증(Arthropathy)으로

## 한 문장 요약

Felbinac(biphenylacetic acid)은 fenbufen의 활성 대사체로, 문헌상 근골격계 연조직 손상 및 경증~중등도 골관절염에 국소(외용) 진통소염제로 사용되어 온 성분입니다.
이번 Evidence Pack의 TxGNN 예측 상위 항목 대부분(골관절염 이환 감수성, 희귀 골격이형성증 등)은 모델 스스로 "유전적 감수성 개념/기전상 무관"으로 판정한 통계적 잡음이라, 실질적으로 근거가 뒷받침되는 항목은 **관절병증(Arthropathy)**입니다.
현재 **등록된 임상시험은 없지만 문헌 11편**(RCT 2건 포함)이 이 방향(관절 염증성 질환에서의 NSAID 효능)을 지지하며, 이는 신규 적응증 발굴이라기보다 **기존 NSAID 용도의 재확인**에 가깝습니다.

> **참고**: TxGNN 최고 점수 항목(osteoarthritis susceptibility, 99.997%)은 GWAS 감수성 유전자좌 개념 노드로, 치료 가능한 질병 실체가 아니며 임상시험·문헌 근거가 전무하여 본 보고서에서 제외했습니다. 마찬가지로 희귀 골격/연골 이형성증 항목들(brachyolmia, acromesomelic dysplasia 등)도 기전적 연관성과 근거가 없어 제외했습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정보 없음 (대만 허가 자료 없음; 문헌상 근골격계 연조직 손상·경중등도 골관절염 국소 치료 이력 확인) |
| 예측 신규 적응증 | 관절병증 (Arthropathy) |
| TxGNN 예측 점수 | 99.97% (rank 1,059 / 전체) |
| 근거 수준 | L2 |
| 대만 시판 현황 | 미상장 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

Felbinac(biphenylacetic acid, BPAA)은 fenbufen의 치료 활성 대사체로, 비선택적 COX-1/COX-2 억제제입니다. 경피 흡수 후 국소 관절 조직에서 치료 농도에 도달해 프로스타글란딘 합성을 억제함으로써 소염·진통 효과를 냅니다. 이는 NSAID가 관절병증(골관절염·류마티스 관절염 포함)을 치료하는 표준 약리 기전과 동일합니다.

문헌 근거(아래 참고)를 보면 Felbinac(BPAA 겔) 자체가 이미 골관절염 환자와 류마티스 관절염 환자를 대상으로 한 RCT에서 평가된 바 있어, TxGNN의 이번 예측은 새로운 기전 가설이라기보다 **기존에 확인된 용도를 지식그래프가 재확인한 결과**로 해석하는 것이 타당합니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [1490436](https://pubmed.ncbi.nlm.nih.gov/1490436/) | 1992 | RCT | Drugs Exp Clin Res | 고령 골관절염 환자 대상 BPAA(Felbinac) 겔 vs diclofenac emulgel — 우수한 효과·부작용 없음, 두 군간 유의차 없음 |
| [8496885](https://pubmed.ncbi.nlm.nih.gov/8496885/) | 1993 | RCT | J Rheumatol | 류마티스 관절염 환자에서 biphenylacetic acid 3% 겔(Felbinac)의 유효성 평가 |
| [7601178](https://pubmed.ncbi.nlm.nih.gov/7601178/) | 1994 | Review | Eur J Rheumatol Inflamm | 외용 Felbinac이 연조직 손상·경중등도 골관절염에서 경구 ibuprofen/fenbufen과 동등한 효능을 보임 |
| [2530026](https://pubmed.ncbi.nlm.nih.gov/2530026/) | 1989 | Cohort | La Clinica Terapeutica | 골관절염(52명)·관절외 류마티스 질환(48명) 환자 대상 BPAA 겔 개방연구, 유효성·내약성 양호 |
| [27241582](https://pubmed.ncbi.nlm.nih.gov/27241582/) | 2016 | RCT(전임상) | Drug Dev Res | 랫드 항원유발 관절염 모델에서 외용 NSAID 패치의 항염·진통 효과 비교 |
| [2696292](https://pubmed.ncbi.nlm.nih.gov/2696292/) | 1989 | PK Study | Z Rheumatol | 무릎관절 수술 전 경구 fenbufen vs 국소 Felbinac 겔 투여 시 혈장·조직 내 BPAA 농도 비교 |
| [2085060](https://pubmed.ncbi.nlm.nih.gov/2085060/) | 1990 | PK Study | Z Rheumatol | 골관절증 환자에서 2~4주간 Felbinac 겔 투여 후 활액 내 BPAA 농도 측정 |
| [6356910](https://pubmed.ncbi.nlm.nih.gov/6356910/) | 1983 | Review | Am J Med | fenbufen의 약리학적 특성 — 활성대사체 BPAA의 강력한 COX 억제 작용 |
| [4050149](https://pubmed.ncbi.nlm.nih.gov/4050149/) | 1985 | 동물실험 | Z Rheumatol | 장기 관절강내 fenbufen 투여가 관절연골에 퇴행성 변화를 유발하지 않음 |
| [24178955](https://pubmed.ncbi.nlm.nih.gov/24178955/) | 2014 | 전임상 | Inflammopharmacology | 위장보호 대체제로서 biphenylacetic acid 결합 프로드럭 설계 및 약리평가 |

---

## 대만 시판 정보

대만에 등록된 허가 제품이 없습니다 (미상장, 허가 0건).

---

## 안전성 고려사항

TFDA 허가사항(경고·금기)과 약물상호작용 자료가 아직 확보되지 않았습니다 (Blocking 등급 데이터 갭). 안전성 정보는 향후 허가사항 확보 후 참조하시기 바랍니다.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
관절병증(OA/RA 포함) 치료에 대한 Felbinac(BPAA)의 NSAID 표준 기전과 이를 뒷받침하는 문헌 근거(RCT 2건 포함 총 11편, L2)는 존재하지만, 대만 미상장 상태이며 TFDA 허가사항(경고/금기) 자료 부재로 안전성 초기평가(S1)를 아직 통과할 수 없습니다.

**진행하려면 필요한 것:**
- TFDA 공식 허가사항(경고·금기) 자료 확보 (DG001, Blocking)
- DrugBank 작용기전(MOA) 상세 자료 재확인 — query_log상 DrugBank 조회는 성공(1건)으로 기록되어 있으나 MOA 필드가 비어 있어 데이터 정합성 재검토 필요 (DG002)
- 대만 내 허가 신청/유통 현황 실사 (현재 등록 0건)
- 등록 임상시험 부재 상태이므로, 관절병증 적응증 확장 시 자체 임상 데이터 확보 계획 수립
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

