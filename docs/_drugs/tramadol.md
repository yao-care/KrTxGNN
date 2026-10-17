---
layout: default
title: Tramadol
parent: 모델 예측만 (L5)
nav_order: 751
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Tramadol: 예측 신규 적응증 골관절염 (Osteoarthritis) (근거 수준 L5). 기존 적응증: 허가증 자료에는 허가 적응증 본문이 아닌 허가사항 문서 링크만 포함되어 있어 구체적 문구를 확인할 수 없음 (중등도 이상의…"
monitor_inn: "Tramadol"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "juvenile idiopathic arthritis"]
---

# Tramadol
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

# Tramadol: 골관절염 통증 치료제에서 골관절염(Osteoarthritis)으로

## 한 문장 요약

Tramadol은 중추성 진통제로, 국내에서 중등도 이상의 통증 치료에 사용되는 약물입니다.
TxGNN 모델은 **골관절염(Osteoarthritis)**에 효과가 있을 수 있다고 예측하며, 현재 **21건의 임상시험**(Phase 3 완료 시험 다수 포함)과 **20편의 문헌**이 이 방향을 지지합니다.
다만 이는 질병을 변화시키는 치료가 아니라 기존의 증상 완화 진통 용도에 가깝습니다.

> 참고: 예측 점수 1위는 "골관절염 감수성(osteoarthritis susceptibility)"이나, 이는 치료 가능한 임상 상태가 아닌 유전적 감수성 개념이어서 근거가 간접적입니다. 따라서 이 보고서는 임상적으로 의미 있고 근거가 가장 충실한 2위 예측인 **골관절염**을 중심으로 평가합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가증 자료에는 허가 적응증 본문이 아닌 허가사항 문서 링크만 포함되어 있어 구체적 문구를 확인할 수 없음 (중등도 이상의 통증 치료제) |
| 예측 신규 적응증 | 골관절염 (Osteoarthritis) |
| TxGNN 예측 점수 | 99.99% (골관절염 기준, 1위 골관절염 감수성도 99.99%) |
| 근거 수준 | L1 (완료된 Phase 3 RCT 다수) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 20건 (모두 단일제, 유효) |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Tramadol은 약한 mu-오피오이드 수용체 작용제이면서 세로토닌·노르에피네프린 재흡수를 억제하는 이중 작용 진통제입니다. 이 중추성 진통 작용이 만성 골관절염 통증에 적용될 수 있습니다.

기존 적응증인 통증 치료와 골관절염의 통증 관리는 직접적으로 연결됩니다. 실제로 ACR/관절염재단 2019 가이드라인은 Tramadol을 조건부로 권고하며, 특히 NSAIDs를 사용할 수 없거나 효과가 부족한 환자에서 고려할 수 있습니다.

다만 Tramadol은 이미 증상 완화용 진통제로 쓰이고 있어 엄밀한 의미의 재창출 후보라기보다 기존 용도의 재확인에 가깝습니다. 질병 진행을 늦추는 효과(질병 수정)는 없습니다.

## 임상시험 근거

골관절염 관련 시험 21건 중 관련성이 높은 상위 10건입니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00348452](https://clinicaltrials.gov/study/NCT00348452) | Phase 3 | 완료 | 1000 | 무릎·고관절 골관절염에서 Tramadol ER 100/200/300 mg vs 위약·셀레콕시브 이중맹검 용량 탐색 |
| [NCT00325858](https://clinicaltrials.gov/study/NCT00325858) | Phase 3 | 완료 | 1000 | Tramadol ER 100~400 mg vs 위약, 중등도~중증 골관절염 통증 |
| [NCT00833794](https://clinicaltrials.gov/study/NCT00833794) | Phase 3 | 완료 | 1028 | 1일 1회 Tramadol vs 위약, 골관절염 통증 진통 효과·안전성 |
| [NCT00852917](https://clinicaltrials.gov/study/NCT00852917) | Phase 3 | 완료 | 552 | 1일 1회 Tramadol 100/200/300 mg vs 위약, 무릎 골관절염 통증 |
| [NCT00348010](https://clinicaltrials.gov/study/NCT00348010) | Phase 3 | 완료 | 245 | Tramadol ER vs 위약, 무릎 골관절염 이중맹검 용량 적정 |
| [NCT00950651](https://clinicaltrials.gov/study/NCT00950651) | Phase 3 | 완료 | 431 | 1일 1회 Contramid 제형 vs 1일 2회 SR 제형, 무릎 골관절염 |
| [NCT00736853](https://clinicaltrials.gov/study/NCT00736853) | Phase 3 | 완료 | 321 | Tramadol/아세트아미노펜(JNS013), NSAIDs로 조절되지 않는 만성 통증(골관절염 또는 요통) |
| [NCT05362851](https://clinicaltrials.gov/study/NCT05362851) | Phase 3 | 불명 | 692 | YYC301의 무릎 골관절염 대상 활성대조 이중맹검 시험 |
| [NCT01063842](https://clinicaltrials.gov/study/NCT01063842) | Phase 4 | 완료 | 250 | 한국인 골관절염 환자에서 Tramadol/아세트아미노펜 용량 적정을 통한 내약성 개선 |
| [NCT01728246](https://clinicaltrials.gov/study/NCT01728246) | Phase 4 | 완료 | 473 | 만성 골관절염에서 Tramadol/파라세타몰 추가요법의 효능·안전성·삶의 질 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [31132298](https://pubmed.ncbi.nlm.nih.gov/31132298/) | 2019 | 체계적 문헌고찰 (Cochrane) | Cochrane Database Syst Rev | 골관절염에서 Tramadol의 효과와 이상반응 평가 (NSAIDs 대비 위장관·신장 부작용 가능성 낮음) |
| [34251756](https://pubmed.ncbi.nlm.nih.gov/34251756/) | 2023 | 체계적 문헌고찰·네트워크 메타분석 | Arthritis Care Res | 무릎·고관절 골관절염 RCT에서 Tramadol의 효능과 안전성 평가 |
| [31908149](https://pubmed.ncbi.nlm.nih.gov/31908149/) | 2020 | 가이드라인 | Arthritis Care Res | ACR/관절염재단 2019 손·고관절·무릎 골관절염 관리 가이드라인 |
| [31908163](https://pubmed.ncbi.nlm.nih.gov/31908163/) | 2020 | 가이드라인 | Arthritis Rheumatol | 위 ACR/관절염재단 가이드라인의 동일 게재본 |
| [16856101](https://pubmed.ncbi.nlm.nih.gov/16856101/) | 2006 | 체계적 문헌고찰 (Cochrane) | Cochrane Database Syst Rev | 골관절염에서 Tramadol 사용 근거 (위장관 출혈·신장 문제 없음) |
| [17343302](https://pubmed.ncbi.nlm.nih.gov/17343302/) | 2007 | 체계적 문헌고찰·메타분석 | J Rheumatol | 경구 Tramadol의 진통 효과, 신체 기능, 효과 지속 기간, 안전성 평가 |
| [30860559](https://pubmed.ncbi.nlm.nih.gov/30860559/) | 2019 | 코호트 | JAMA | 골관절염 환자에서 Tramadol과 전체 사망률의 연관성 |
| [35410440](https://pubmed.ncbi.nlm.nih.gov/35410440/) | 2022 | 인구 기반 연구 | Arthritis Res Ther | 골관절염 환자에서 Tramadol과 사망, 심혈관질환, 정맥혈전색전증, 고관절 골절 위험 |
| [38937394](https://pubmed.ncbi.nlm.nih.gov/38937394/) | 2024 | 체계적 문헌고찰·메타분석 | Drugs | 요통·골관절염에서 파라세타몰 병용요법의 효과 (효과 불분명) |
| [40095377](https://pubmed.ncbi.nlm.nih.gov/40095377/) | 2025 | 체계적 문헌고찰 | Drugs | 항골관절염 약물의 시판 후 안전성 감시 연구 검토 |

## 한국 시판 정보

허가증 20건 중 주요 5건입니다. 허가 적응증 본문은 허가사항 문서 링크로만 제공되어 있어 요약하지 않았습니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200713092 | 트라칸정 | 필름코팅정 | 허가사항 문서 참조 |
| 202201142 | 울트라셋세미정 | 필름코팅정 | 허가사항 문서 참조 |
| 200805389 | 울트라맥세미정 | 필름코팅정 | 허가사항 문서 참조 |
| 198300327 | 트리돌캡슐50mg | 경질캡슐 | 허가사항 문서 참조 |
| 198600090 | 타마돌주사 | 주사제(앰플) | 허가사항 문서 참조 |

## 안전성 고려사항

- **약물 상호작용**: 데이터상 상호작용 100건이 확인되었습니다. 주요(Major) 등급 예시는 Alvimopan, Bupropion, Cisapride, Dexfenfluramine, Diethylpropion, Dolasetron, Dronabinol, Ephedrine, Fenfluramine 등입니다. 중등도(Moderate) 등급 예시는 Atropine, Bisacodyl, Cimetidine, Clarithromycin, Famotidine 등입니다.
- **문헌상 안전성 신호**: 골관절염 환자에서 전체 사망률 증가 신호, 낙상, 의존성 위험이 보고되었습니다. 세로토닌 증후군과 경련 발작에 대한 모니터링도 필요합니다.
- **소아 사용**: 소아에서는 호흡억제와 CYP2D6 초고속 대사 위험으로 사용에 제한이 큽니다.

허가사항상의 경고·금기 정보는 이번 데이터에 포함되지 않았으므로 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
골관절염 통증에 대해 완료된 대규모 Phase 3 RCT가 다수 있고 Cochrane 리뷰와 ACR 가이드라인이 뒷받침합니다. 다만 사망률 신호, 낙상, 의존성, 약물 상호작용 위험이 있고 질병 수정 효과가 없어 안전 장치를 전제로 한 증상 완화 용도로 제한해야 합니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기) 확보: 한국 MFDS 허가사항 PDF 내용 확인 (현재 안전성 심사를 막는 핵심 공백)
- 상세한 작용 기전 데이터 (DrugBank 등)
- NSAIDs 사용 불가 또는 효과 부족 환자로 대상 제한, 최저 유효 용량·최단 기간 사용
- 세로토닌 증후군, 경련, 낙상, 의존성, 약물 상호작용에 대한 모니터링 계획

**기타 예측 신규 적응증에 대한 참고:**
- 관절병증(Arthropathy): 근거는 사실상 골관절염 시험과 중복되며, 골관절염형 통증으로 한정할 때 같은 안전 장치로 Proceed with Guardrails가 가능합니다.
- 골관절염 감수성, 척추관절병증 감수성: 유전적 감수성 개념이어서 치료 대상이 아니며 Hold입니다.
- 말단중간이형성증(Hunter-Thompson형), 단지증-법랑질형성부전 증후군, 근경화증, 단지증, 가성무연골형성증, 소아특발성관절염: 기전적 연관성과 임상 근거가 없거나 부적절하여 Hold입니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

