---
layout: default
title: Ascorbic Acid
parent: 僅模型預測 (L5)
nav_order: 91
evidence_level: L5
indication_count: 10
---

# Ascorbic Acid
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

# Ascorbic Acid: 비타민 C 결핍증에서 급성 손상 치료로

## 한 문장 요약

Ascorbic Acid(비타민 C)는 필수 수용성 비타민으로, 비타민 C 결핍증(괴혈병) 예방·치료와 항산화 영양 보충에 사용되어 왔습니다. TxGNN 모델이 예측한 10개 적응증 중 가장 강력한 임상 근거를 보유한 **급성 손상(Injury)**에 대해, 현재 **Phase 2/3를 포함한 10건의 핵심 임상시험**과 **10편의 문헌**이 보조 치료 가능성을 지지하고 있습니다. 화상·수혈 관련 급성 폐손상(TRALI)·패혈증 분야에서 직접적인 Phase 2/3 수준 근거가 존재하며 재창출 타당성이 인정됩니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 비타민 C 결핍증 (괴혈병) — 대만 TFDA 허가 미취득 |
| 예측 신규 적응증 | 급성 손상 (Injury) |
| TxGNN 예측 점수 | 99.60% |
| 근거 수준 | L2 |
| 대만 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 전체 예측 적응증 스크리닝 요약

본 Evidence Pack은 10개 적응증에 대한 다중 예측 결과를 포함합니다. 재창출 우선순위 요약:

| 순위 | 적응증 | TxGNN 점수 | 근거 수준 | 권고 |
|------|--------|-----------|---------|-----|
| 1 | 비증후군성 식도 기형 | 99.96% | L5 | Hold |
| 2 | 식도 질환 | 99.90% | L4 | Research Question |
| 3 | 선천성 프로트롬빈 결핍증 | 99.70% | L5 | Hold |
| **4** | **급성 손상** | **99.60%** | **L2** | **Proceed with Guardrails** |
| 5 | 생물소 대사 질환 | 99.52% | L4 | Research Question |
| 6 | 절편성 치악 이형성증 | 99.47% | L5 | Hold |
| **7** | **주산기 질환** | **99.47%** | **L2** | **Proceed with Guardrails** |
| 8 | 광범위 백악골성 이형성증 | 99.47% | L5 | Hold |
| 9 | 아세포 시스템 영향 질환 | 99.47% | L5 | Hold |
| **10** | **비타민 결핍 장애** | **99.47%** | **L1** | **Proceed with Guardrails** |

> ⚠️ **해석 주의**: 비타민 결핍 장애(rank 10, L1)는 Ascorbic Acid의 원래 적응증(괴혈병·비타민 C 결핍 치료)과 사실상 동일하여, TxGNN 모델이 기존 약물-질환 관계를 정확히 복원한 것으로 해석됩니다. 진정한 신규 재창출 후보는 **급성 손상(L2)** 및 **주산기 질환(L2)**입니다. Rank 1·3·6·8·9의 L5 예측은 지식 그래프 군집 효과에 의한 모델 과일반화 가능성이 높습니다.

---

## 이 예측이 타당한 이유는?

Ascorbic Acid는 다중 확인된 기전을 통해 급성 손상 보호 효과를 발휘합니다.

**항산화·허혈-재관류 보호:** 강력한 수용성 항산화제로서 반응성 산소종(ROS)을 직접 소거하여 허혈-재관류 손상에서 발생하는 산화 스트레스 급증을 억제합니다. 이 기전은 TRALI·패혈증·화상 소생·심정지 후 증후군 등 다양한 급성 손상 상황에서 공통적으로 적용되며, Phase 2 직접 시험(NCT04153487, TRALI)과 Phase 3 대규모 시험(LOVIT, n=872)에서 임상적으로 검증되었습니다.

**콜라겐 합성 촉진·조직 회복:** 프롤린·라이신 수산화효소의 필수 보조인자로서 콜라겐 합성을 촉진하여 피부·힘줄·인대 등 결합 조직의 손상 후 회복을 가속화합니다. RCT(PMID 27852613)에서 비타민 C 강화 젤라틴 섭취 후 간헐적 운동 시 혈중 콜라겐 합성 마커가 유의미하게 증가함이 확인되었으며, 힘줄 손상 동물 모델(PMID 30777116)에서도 회복 촉진 효과가 입증되었습니다.

**내피 장벽 유지·신경 재생:** 미세혈관 내피 장벽 기능을 유지하여 화상·창상 후 혈장 누출 및 수액 소생 요구량을 감소시킬 수 있습니다(VICToRY 시험 설계 근거). 척수손상에서는 TET 탈메틸화효소 활성화를 통한 표관유전학적 조절로 신경 재생 관련 유전자 발현을 증가시키는 독특한 기전이 동물 연구에서 보고되었습니다(PMID 32466098).

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT04153487](https://clinicaltrials.gov/study/NCT04153487) | Phase 2 | 완료 | 40 | TRALI 중환자에서 정맥 비타민 C 주입의 역할 직접 평가 — 급성 손상 분야 핵심 직접 시험 |
| [NCT03680274](https://clinicaltrials.gov/study/NCT03680274) | Phase 3 | 완료 | 872 | 패혈증 ICU에서 고용량 정맥 비타민 C vs. 위약, 28일 사망률·장기 기능 장애 평가 (LOVIT 시험) |
| [NCT04138394](https://clinicaltrials.gov/study/NCT04138394) | Phase 3 | 정지 | 666 | 화상 중환자에서 고용량 정맥 비타민 C의 장기 기능·생존·회복 개선 여부 평가 (VICToRY 시험) |
| [NCT02873026](https://clinicaltrials.gov/study/NCT02873026) | Phase 3 | 완료 | 300 | 안구 관통 외상 유리체망막 수술 시 보조 항염 치료 효과, 다기관 이중 맹검 RCT |
| [NCT04921189](https://clinicaltrials.gov/study/NCT04921189) | Phase 2 | 완료 | 160 | 원외 심정지 소생 후 스테로이드+비타민 C+티아민 병용 신경 보호 (STAR 시험) |
| [NCT02106975](https://clinicaltrials.gov/study/NCT02106975) | Phase 2 | 완료 | 170 | 패혈증 유발 급성 폐손상에서 비타민 C 주입이 SOFA 점수·산소화·염증 바이오마커에 미치는 영향 (CITRIS-ALI) |
| [NCT02735707](https://clinicaltrials.gov/study/NCT02735707) | Phase 3 | 모집 중 | 20,000 | 지역사회 획득 폐렴 ICU 환자 적응형 플랫폼 시험, 비타민 C 포함 복합 중재 비교 (REMAP-CAP) |
| [NCT03756220](https://clinicaltrials.gov/study/NCT03756220) | Phase 2 | 완료 | 116 | 패혈성 쇼크에서 비타민 C+티아민 병용의 장기 기능·생존 개선 다기관 이중 맹검 RCT |
| [NCT06050668](https://clinicaltrials.gov/study/NCT06050668) | Phase 2 | 모집 중 | 60 | 대퇴골 취약 골절 후 아미노산·비타민 C 기반 보충제의 근육 형태 및 손상 회복 영향 (MEND 시험) |
| [NCT03780933](https://clinicaltrials.gov/study/NCT03780933) | N/A | 완료 | 40 | 고용량 비타민 C의 ARDS 중환자 임상 결과(산화/항산화 불균형·재원 기간·사망률·기계 환기 이탈) 평가 |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [27852613](https://pubmed.ncbi.nlm.nih.gov/27852613/) | 2017 | RCT | Am J Clin Nutr | 비타민 C 강화 젤라틴이 간헐적 운동 전 섭취 시 콜라겐 합성 유의미 증가 — 근골격 손상 예방 가능성 직접 시사 |
| [33675075](https://pubmed.ncbi.nlm.nih.gov/33675075/) | 2021 | Clinical Review | JPEN Parenter Enteral Nutr | 급성 의료 환경(패혈증·화상·중환자)에서 비타민 C의 다양한 적응증 및 정맥 투여 필요성 체계적 검토 |
| [31631076](https://pubmed.ncbi.nlm.nih.gov/31631076/) | 2020 | Prospective Cohort | Ann Thorac Cardiovasc Surg | 식도 절제술 후 코르티코스테로이드+비타민 C+티아민 병용이 산화·염증 반응 억제 및 산소화 지표 개선 |
| [31440996](https://pubmed.ncbi.nlm.nih.gov/31440996/) | 2020 | Narrative Review | Neurocritical Care | 외상성 뇌손상(TBI)에서 고용량 정맥 비타민 C의 이차 손상 억제 기전(항산화·항염증) 및 임상 적용 가능성 검토 |
| [32466098](https://pubmed.ncbi.nlm.nih.gov/32466098/) | 2020 | Animal Study | Cells | 비타민 C가 TET 효소 매개 DNA 탈메틸화(표관유전학적 조절)를 통해 척수손상 후 신경 재생 관련 유전자 발현 촉진 |
| [37199082](https://pubmed.ncbi.nlm.nih.gov/37199082/) | 2023 | Animal Study | Clin Exp Pharmacol Physiol | 멜라토닌+비타민 C 병용이 패혈증 유발 폐손상 쥐 모델에서 산화 스트레스·염증 시너지 억제 및 조직병리 개선 |
| [32141505](https://pubmed.ncbi.nlm.nih.gov/32141505/) | 2020 | Retrospective Study | J Burn Care Res | 중증 화상 성인에서 고용량(66 mg/kg/h) vs. 저용량(3.5 g/일) 비타민 C 안전성·약력학 후향 비교 연구 |
| [30777116](https://pubmed.ncbi.nlm.nih.gov/30777116/) | 2019 | Animal Study | J Orthop Surg Res | 비타민 C+T3 병용이 쥐 아킬레스건 손상 모델에서 골수 줄기세포 단독보다 우수한 힘줄 치유 효과 확인 |
| [25977448](https://pubmed.ncbi.nlm.nih.gov/25977448/) | 2015 | Ex vivo/In vitro | J Appl Physiol | 비타민 C가 고압 노출 관련 혈관 손상 및 마이크로파티클 생성(혈소판·호중구 활성 마커)을 억제 |
| [23994218](https://pubmed.ncbi.nlm.nih.gov/23994218/) | 2013 | Animal Study | Brain Res | 비타민 C가 자가포식(autophagy) 억제를 통해 쥐 발작 모델에서 뇌손상을 경감 — 신경 손상 기전 연구 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
급성 손상(화상·TRALI·패혈증·척수손상) 분야에서 복수의 Phase 2/3 완료 임상시험이 Ascorbic Acid 보조 치료 효과를 직접 시험하였고, 항산화·콜라겐 합성 촉진·내피 장벽 보호·표관유전학적 신경 재생 촉진 등 다중 확인된 기전이 이를 뒷받침합니다. 다만 핵심 Phase 3 시험인 LOVIT(패혈증, n=872)에서 명확한 생존 이득이 확인되지 않아, 손상 유형별로 세분화된 접근과 최적 용량·투여 경로 프로토콜 확립이 선행되어야 합니다.

**진행하려면 필요한 것:**
- 손상 유형별(화상·TRALI·패혈증·척수손상·외상성 뇌손상) 세분화 근거 리뷰 및 최적 용량·투여 경로 결정
- 대만 TFDA 허가사항 및 안전성 데이터 확보 (Data Gap DG001: TFDA 경고·금기사항 PDF 파싱 필요)
- DrugBank 상세 MOA 데이터 보완 (Data Gap DG002)
- 고용량 투여 시 신결석 위험군(고수산뇨증·신부전) 및 혈색소침착증 환자 모니터링 계획 수립
- 경구 vs. 정맥 주사 투여 경로별 약동학 차이를 반영한 적응증별 프로토콜 확립
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

