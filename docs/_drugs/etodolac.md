---
layout: default
title: Etodolac
parent: 모델 예측만 (L5)
nav_order: 327
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Etodolac: 예측 신규 적응증 골관절염 감수성 (Osteoarthritis susceptibility) (근거 수준 L5). 기존 적응증: 허가증에는 적응증 본문 대신 허가사항 PDF 링크만 수록되어 있어 구체적 문구를 확인할 수 없음 (NSAID 계열로 관절염·…"
monitor_inn: "Etodolac"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia"]
---

# Etodolac
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

# Etodolac: 골관절염 관련 질환으로의 재창출 평가

## 한 문장 요약

Etodolac은 COX-2 선호성 비스테로이드 소염진통제(NSAID)로, 한국에서 관절염 등의 통증·염증 치료에 사용되어 왔습니다.
TxGNN 모델은 **골관절염 감수성(osteoarthritis susceptibility)**을 최상위 신규 적응증으로 예측했지만, 이에 대한 임상시험과 문헌은 한 건도 없습니다.
다만 예측 3순위인 **골관절염**에는 3건의 임상시험과 20편의 문헌이 있으나, 이는 이미 알려진 기존 적응증에 가깝습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가증에는 적응증 본문 대신 허가사항 PDF 링크만 수록되어 있어 구체적 문구를 확인할 수 없음 (NSAID 계열로 관절염·통증 치료에 사용) |
| 예측 신규 적응증 | 골관절염 감수성 (Osteoarthritis susceptibility) |
| TxGNN 예측 점수 | 99.995% |
| 근거 수준 | L5 (1순위 예측 기준) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 10건 |
| 권장 결정 | Hold |

> 참고: 골관절염 감수성은 유전적 감수성 표현형으로 직접 치료할 수 있는 임상 질환이 아닙니다. 상위 10개 예측 중 근거가 있는 항목은 골관절염(L2), 관절병증(L2), 강직성 척추염(L4)이며, 나머지는 L5입니다.

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면, Etodolac은 COX-2 선호성 NSAID로 프로스타글란딘 합성을 억제해 염증과 통증을 줄이며, 단일 성분 제제로 시판되고 있습니다.

1순위 예측인 골관절염 감수성은 유전적 소인을 나타내는 표현형이어서 약물이 직접 표적으로 삼기 어렵습니다. 골관절염 자체에서의 소염·진통 작용을 통한 간접적 연관성만 생각할 수 있습니다. 2·4·7·10순위의 희귀 골격 이형성증(Hunter-Thompson형 말단중간이형성증, brachyolmia 등)은 기전상 근거가 확인되지 않았고, 점수가 높은 것은 그래프상 골·관절 표현형과의 근접성을 반영한 것으로 보입니다.

반면 골관절염, 관절병증, 강직성 척추염은 NSAID가 증상 완화에 널리 쓰이는 질환이라 기전상 타당합니다. 다만 골관절염과 관절병증은 이미 기존 적응증 범위에 해당할 가능성이 높아 진정한 재창출 후보로 보기 어렵습니다.

## 임상시험 근거

1순위 예측(골관절염 감수성)에는 관련 임상시험이 없습니다. 아래는 근거가 가장 많은 3순위 예측 **골관절염**의 시험입니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT07308470](https://clinicaltrials.gov/study/NCT07308470) | Phase 2 | 모집 예정 | 30 | 무릎 골관절염에서 물리치료 보조요법으로 Etodolac 함유 고체지질나노입자 겔 평가 (신규 국소 제형, 결과 없음) |
| [NCT01638962](https://clinicaltrials.gov/study/NCT01638962) | N/A | 완료 | 93 | 무릎 골관절염에서 진통제 사용 지도와 신경근 운동의 관절 부하 비교 (Etodolac 직접 시험 아님) |
| [NCT02180516](https://clinicaltrials.gov/study/NCT02180516) | N/A | 완료 | 9,984 | Meloxicam과 다른 NSAID의 위장관 이상반응 비교 관찰 연구 (Etodolac은 간접 관련) |

## 문헌 근거

3순위 예측 **골관절염** 관련 문헌 중 RCT 및 주요 리뷰 위주로 정리했습니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [2150187](https://pubmed.ncbi.nlm.nih.gov/2150187/) | 1990 | RCT | Curr Med Res Opin | 무릎 골관절염 65명에서 Etodolac 300 mg 1일 2회와 piroxicam 비교 (8주) |
| [1286486](https://pubmed.ncbi.nlm.nih.gov/1286486/) | 1992 | RCT | Clin Ther | 무릎 골관절염 172명에서 Etodolac 600 mg/일과 diclofenac 150 mg/일 비교 (8주), 두 군 모두 통증 유의하게 감소 |
| [8565029](https://pubmed.ncbi.nlm.nih.gov/8565029/) | 1995 | 이중맹검 위약대조 | Clin Ther | 무릎 골관절염 254명에서 Etodolac, naproxen, 위약 비교 (4주) |
| [1828415](https://pubmed.ncbi.nlm.nih.gov/1828415/) | 1991 | 이중맹검 비교 | Curr Med Res Opin | 무릎 골관절염 220명에서 Etodolac이 piroxicam 대비 효능·내약성 평가, 기저치 대비 유의한 개선 |
| [20639739](https://pubmed.ncbi.nlm.nih.gov/20639739/) | 2010 | 무작위 이중맹검 | Clin J Pain | 무릎 골관절염 악화 시 Etodolac-paracetamol 복합제와 Etodolac 단독 비교 |
| [24194981](https://pubmed.ncbi.nlm.nih.gov/24194981/) | 2013 | RCT (공개) | Pain Res Treat | 무릎 골관절염 60명에서 Etodolac 단독과 eperisone 병용 비교 (8주) |
| [18405470](https://pubmed.ncbi.nlm.nih.gov/18405470/) | 2008 | 체계적 문헌고찰 | Health Technol Assess | Etodolac 등 COX-2 선택성 NSAID의 골관절염·류마티스관절염 효과 및 비용효과 평가 |
| [1717225](https://pubmed.ncbi.nlm.nih.gov/1717225/) | 1991 | Review | Drugs | 류마티스관절염, 골관절염, 강직성 척추염, 수술 후 통증에서 다른 NSAID와 최소 동등한 효능 |
| [2150570](https://pubmed.ncbi.nlm.nih.gov/2150570/) | 1990 | 임상 연구 | Rheumatol Int | 골관절염에서 위약보다 효과적이며 연골세포 기능 영향 검토 |
| [39345034](https://pubmed.ncbi.nlm.nih.gov/39345034/) | 2024 | Review | Ther Deliv | 골관절염에서 Etodolac의 약물 전달 과제와 국소 나노 치료 전략 |

> 강직성 척추염(9순위)에는 임상시험이 없고 Review, 공개 임상, 시판 후 안전성 연구 등 7편의 문헌만 있습니다. Etodolac 특이적 RCT는 확인되지 않았습니다.

## 한국 시판 정보

허가증에는 적응증 본문이 아닌 허가사항 PDF 링크만 수록되어 있어, 적응증은 해당 링크의 허가사항을 참조해야 합니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 199002184 | 아신돌캡슐200밀리그램 (수출용) | 경질캡슐 | 허가사항 PDF 참조 |
| 201401037 | 엔터락캡슐 (수출용) | 경질캡슐 | 허가사항 PDF 참조 |
| 199400681 | 마카나캡슐 (수출용) | 경질캡슐 | 허가사항 PDF 참조 |
| 201405864 | 엘토스캡슐 (수출용) | 경질캡슐 | 허가사항 PDF 참조 |
| 199102606 | 에토딘캡슐 | 경질캡슐 | 허가사항 PDF 참조 |

전체 10건 중 에토딘캡슐을 제외한 9건은 수출용입니다.

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 확인되었으며, 주요 항목은 다음과 같습니다.
  - 중등도: 코르티코스테로이드(hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), 아세틸살리실산, 메살라진, balsalazide, metformin, 설포닐우레아(glimepiride, chlorpropamide), repaglinide, 칼륨 제제(potassium citrate, potassium bicarbonate), 장 세척제(picosulfuric acid, polyethylene glycol)
  - 경미: famotidine, ranitidine, cimetidine, linaclotide
- **재창출 시 유의점**: NSAID 계열의 위장관, 심혈관, 신장 위험과 고령 환자에서의 주의가 필요합니다.

경고 및 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
1순위 예측인 골관절염 감수성은 직접 치료 가능한 질환이 아니며 임상시험과 문헌이 없어 L5 수준에 머뭅니다. 근거가 있는 골관절염(L2)과 관절병증(L2)은 이미 기존 적응증과 겹쳐 신규 재창출 후보로 보기 어렵고, 강직성 척추염(L4)은 Etodolac 특이적 근거가 부족합니다.

**진행하려면 필요한 것:**
- 허가사항 PDF에서 기존 적응증, 경고, 금기 확인 (안전성 선별의 선행 조건)
- 작용 기전(MOA) 데이터 보완
- 골관절염이 허가 적응증에 포함되는지 확인하여 진정한 재창출 여부 판단
- 강직성 척추염에서 기존 NSAID와 Etodolac을 비교한 임상시험 근거 확보 (현재는 추가 연구 질문 단계)
- 희귀 골격 이형성증 등 L5 예측은 기전 근거 확보 전까지 추가 진행 비권장
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

