---
layout: default
title: Ketoprofen
parent: 모델 예측만 (L5)
nav_order: 417
evidence_level: L5
indication_count: 10
---

# Ketoprofen
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

# Ketoprofen: 관절염 진통소염제(NSAID)의 골관절염(Osteoarthritis) 근거 확인

## 한 문장 요약

Ketoprofen은 propionic acid 계열 비스테로이드성 소염진통제(NSAID)로, 전 세계적으로 관절 통증·염증 완화에 널리 사용되어 온 약물입니다.
TxGNN 모델은 이 약물에 대해 10개 적응증을 예측했으며, 그중 **골관절염(Osteoarthritis)**이 **임상시험 20건, 문헌 20편(L1 등급)**으로 가장 강력한 실증 근거를 갖추고 있고, **류마티스 관절염(L2)**·**관절병증(Arthropathy, L1)**이 그 뒤를 잇습니다. 반면 상위 스코어 예측 중 절반 이상(희귀 유전성 골격/안면 질환군)은 문헌·임상시험이 전무해 지식그래프상 유전자 노드 인접성에 의한 예측 인공물(artifact)로 판단됩니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터셋에 기재 없음 (문헌상 전 세계적으로 골관절염·류마티스 관절염 등 통증/염증 질환에 사용되는 NSAID) |
| 예측 신규 적응증 | 골관절염 (Osteoarthritis) — 예측 목록 중 근거 가장 풍부 |
| TxGNN 예측 점수 | 99.98% (osteoarthritis, rank 849) |
| 근거 수준 | L1 (osteoarthritis) / L2 (rheumatoid arthritis) / L1 (arthropathy) / L5 (희귀 유전질환 6건) |
| 한국 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails (관절염 계열 3개 적응증) / Hold (희귀 유전질환 6건) |

---

## 이 예측이 타당한 이유는?

현재 DrugBank 등에서 확인 가능한 상세 작용 기전(MOA) 데이터는 확보되지 않았습니다(High severity 데이터 갭, DG002). 다만 확보된 문헌들을 종합하면, Ketoprofen은 **비선택적 COX-1/COX-2 억제제**로 프로스타글란딘 합성을 차단해 소염·진통·해열 작용을 나타내는 전형적인 propionic acid계 NSAID입니다.

이 기전은 골관절염·류마티스 관절염 등 관절 활막의 염증 매개물질 과다 생성을 억제하는 표준적 증상 완화 기전과 직접 연결되며, 실제로 문헌(PMID 1947892, 3526298 등)은 이미 1970~90년대부터 ketoprofen이 두 질환 모두에 사용되어 왔음을 보여줍니다. 즉 TxGNN이 상위권으로 예측한 "osteoarthritis", "rheumatoid arthritis", "arthropathy"는 **새로운 재창출 가설이 아니라 기존 임상 용도를 모델이 재발견한 것**에 가깝습니다.

반면 순위 3, 4, 6, 7, 8, 9위의 희귀 유전성 골격/안면 발달이상 증후군(예: acromesomelic dysplasia, brachyolmia 등)은 GDF5/CHST3 등 골격 관련 유전자 노드가 osteoarthritis와 지식그래프상 인접해 있어 높은 점수를 받았을 가능성이 높으며, 실제 약리학적 연관성이나 문헌·임상시험 근거가 전혀 없어 **모델 인공물(artifact)**로 판단합니다. 특히 rank 1 "osteoarthritis susceptibility"도 표준 osteoarthritis 노드와 중복 계산되었을 가능성이 있어 별도 신규 신호로 보기 어렵습니다.

---

## 임상시험 근거

*(골관절염 기준, 관련성 grade A 및 Phase 2/3 완료 시험 우선 선정)*

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT07319728](https://clinicaltrials.gov/study/NCT07319728) | Phase 1 | 진행 중 | 40 | Ketoprofen 경피 겔 제형의 무릎 골관절염 치료 평가 |
| [NCT06202989](https://clinicaltrials.gov/study/NCT06202989) | Phase 3 | 모집 중 | 288 | Multiprofen-CC(ketoprofen 계열)로 슬관절 전치환술 후 통증 감소 |
| [NCT00647231](https://clinicaltrials.gov/study/NCT00647231) | Phase 2 | 완료 | 300 | HKT-500(ketoprofen 패치) 단회 투여 진통 효과, 경증~중등도 무릎 OA |
| [NCT00365586](https://clinicaltrials.gov/study/NCT00365586) | Phase 3 | 완료 | 300 | Ketoprofen 20% 국소 패치, 무릎 OA 급성 악화 통증에 효과 확인 |
| [NCT00722852](https://clinicaltrials.gov/study/NCT00722852) | Phase 3 | 완료 | 555 | Diractin(ketoprofen 100mg, Transfersome겔), 무릎 OA에서 안전성·유효성 재현 확인 |
| [NCT00792727](https://clinicaltrials.gov/study/NCT00792727) | Phase 3 | 완료 | 380 | HKT-500 패치, 경증~중등도 무릎 OA 통증에 유효 |
| [NCT04421911](https://clinicaltrials.gov/study/NCT04421911) | Phase 3 | 완료 | 236 | Ketoprofen vs Diclofenac, 보행 시 관절통 개선 비교 |
| [NCT00488267](https://clinicaltrials.gov/study/NCT00488267) | Phase 3 | 완료 | 679 | ThermoProfen(온열보조 ketoprofen 패치), 12주간 무릎 OA 통증 개선 |
| [NCT00716547](https://clinicaltrials.gov/study/NCT00716547) | Phase 3 | 완료 | 1,399 | Diractin 50mg/100mg 용량별 무릎 OA 안전성·유효성 재현 |
| [NCT00317733](https://clinicaltrials.gov/study/NCT00317733) | Phase 2 | 완료 | 360 | IDEA-033(Transfersome ketoprofen) vs 경구 celecoxib, 무릎 OA에서 효과 확인 |

**참고**: 류마티스 관절염(RA) 단독 적응증으로 등록된 임상시험은 이 데이터셋에서 확인되지 않았습니다(문헌 근거만 존재). Arthropathy 적응증은 위 목록과 상당 부분 중복됩니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [27103611](https://pubmed.ncbi.nlm.nih.gov/27103611/) | 2016 | Cochrane Review | Cochrane Database Syst Rev | 만성 근골격계 통증에서 국소 NSAID의 효과와 안전성 |
| [27778435](https://pubmed.ncbi.nlm.nih.gov/27778435/) | 2017 | 체계적 문헌고찰 | Musculoskeletal Care | Transfersome겔 국소 ketoprofen의 무릎 OA 안전성·유효성 확인 |
| [40333622](https://pubmed.ncbi.nlm.nih.gov/40333622/) | 2025 | 네트워크 메타분석 | PLoS ONE | 다양한 NSAID의 OA 치료 효과·안전성 비교 |
| [33554694](https://pubmed.ncbi.nlm.nih.gov/33554694/) | 2021 | 체계적 문헌고찰 | Physician Sportsmed | 국소 NSAID의 무릎 OA 통증·기능 개선 효과 |
| [34479761](https://pubmed.ncbi.nlm.nih.gov/34479761/) | 2021 | RCT (Phase III) | Clinical Therapeutics | Ketoprofen 플라스터 vs Diclofenac 플라스터, 무릎 OA 통증에서 비열등 효과 |
| [33674957](https://pubmed.ncbi.nlm.nih.gov/33674957/) | 2021 | 메타분석(RCT) | Pain and Therapy | Ketoprofen vs Ibuprofen, RA 통증 관리 효능 비교 |
| [28497473](https://pubmed.ncbi.nlm.nih.gov/28497473/) | 2017 | Cochrane Overview | Cochrane Database Syst Rev | 급/만성 통증(OA 포함)에서 국소 진통제 개관 |
| [20133510](https://pubmed.ncbi.nlm.nih.gov/20133510/) | 2010 | RCT (위약대조) | J Clin Pharmacol | Ketoprofen 패치, RA 손목 통증에서 위약 대비 유효성·안전성 확인 (n=676) |
| [364615](https://pubmed.ncbi.nlm.nih.gov/364615/) | 1978 | RCT | Rheumatol Rehabil | Ketoprofen vs Naproxen, RA에서 유사한 효과 |
| [796938](https://pubmed.ncbi.nlm.nih.gov/796938/) | 1976 | RCT | Rheumatol Rehabil | Ketoprofen이 위약 대비 RA 통증·조조강직 개선에 유의하게 우수 |

---

## 한국 시판 정보

이 약물은 현재 한국에 허가된 제품이 없습니다 (미출시, 허가증 0건). 국내 시판 시 필요한 허가 절차 및 국내 임상자료 확보가 선행되어야 합니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. (경고·금기·약물상호작용 자료 미확보 — DG001, Blocking 등급 데이터 갭)

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails (골관절염·류마티스 관절염·관절병증) / Hold (희귀 유전질환 6건)**

**사유:**
- 골관절염은 다수의 완료된 Phase 2/3 RCT(L1)와 20편의 문헌으로 뒷받침되나, 이는 신규 재창출이 아니라 기존 NSAID 용도의 실증 재확인입니다.
- 류마티스 관절염(L2)·관절병증(L1)도 다수의 인체 대조 연구로 지지되나 마찬가지로 기존 용도의 연장선입니다.
- 희귀 유전성 골격질환 6건은 문헌·임상시험이 전무하고 기전적 연관성도 없어, 지식그래프의 유전자 노드 인접성에 의한 예측 인공물로 판단하여 추가 검토 없이 Hold합니다.

**진행하려면 필요한 것:**
- 허가사항 경고/금기/약물상호작용 정보 확보 (DG001, Blocking — 제조사 원 허가국 라벨 또는 DrugBank 조회 필요)
- 상세 작용 기전(MOA) 데이터 확보 (DG002, High)
- 국내 시판을 전제로 할 경우 국내 임상자료 및 허가 신청 경로 확인
- "osteoarthritis susceptibility"와 "osteoarthritis" 노드의 중복 계산 여부를 모델 팀에 확인하여 향후 스코어링 왜곡 방지
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

