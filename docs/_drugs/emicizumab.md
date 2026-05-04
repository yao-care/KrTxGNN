---
layout: default
title: Emicizumab
parent: 僅模型預測 (L5)
nav_order: 242
evidence_level: L5
indication_count: 10
---

# Emicizumab
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

# Emicizumab: 선천성 혈우병 A에서 후천성 응고인자 결핍증으로

> **다중 적응증 분석 보고서** | 10개 예측 적응증 평가 | 최우선 권장 결정: Proceed with Guardrails

---

## 한 문장 요약

Emicizumab은 FIXa와 FX를 동시에 결합하는 이중특이성 항체로, 활성화 FVIII의 보조인자 기능을 모방하여 선천성 혈우병 A(항체 유무 불문) 환자의 출혈 예방에 사용됩니다.
TxGNN 모델은 **후천성 응고인자 결핍증(Acquired Coagulation Factor Deficiency)**, 특히 후천성 혈우병 A(AHA)에서도 강력한 효과를 예측하며,
현재 **1건의 관찰 임상시험**과 **Phase 3 전향적 연구 3편을 포함한 20편의 문헌**이 이를 강력히 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 선천성 혈우병 A (항체 유무 불문) 출혈 예방 |
| 예측 신규 적응증 (최우선) | 후천성 응고인자 결핍증 (Acquired Coagulation Factor Deficiency / AHA) |
| TxGNN 예측 점수 | 99.90% |
| 근거 수준 | L1 |
| 한국 시판 현황 | 미허가 (허가증 없음) |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 전체 예측 적응증 요약

| 순위 | 적응증 | TxGNN 점수 | 근거 수준 | 권장 결정 | 비고 |
|------|--------|-----------|---------|---------|------|
| 1 | Pseudo-von Willebrand disease | 99.99% | L5 | Hold | 기전 비중첩 (초기 vs 이차 지혈) |
| 2 | 혈소판 일차 방출 장애 | 99.99% | L5 | Hold | 간접 기전, 임상 근거 없음 |
| 3 | Glanzmann 혈소판무력증 | 99.98% | L4 | Research Question | 우회 치료 기전 유사성, 개별 증례 존재 |
| 4 | Scott 증후군 | 99.92% | L5 | Hold | 극희귀 (전 세계 <30례), 근거 없음 |
| **5** | **후천성 응고인자 결핍증 (AHA)** | **99.90%** | **L1** | **Proceed with Guardrails** | **Phase 3 다수, 유럽 일부 허가** |
| 6 | 콜라겐 수용체 결함 출혈 소인 | 99.86% | L5 | Hold | 초기 지혈 기전, emicizumab 무관 |
| 7 | 선천성 혈소판감소 출혈 장애 | 99.85% | L5 | Hold | 혈소판 수에 무영향 |
| 8 | ⚠️ 혈전성 혈소판감소성 자반증 (TTP) | 99.61% | L5 | Hold | **기전 역방향 — 혈전 악화 위험** |
| 9 | 태아/신생아 동종면역 혈소판감소증 | 99.52% | L5 | Hold | 혈소판 수에 무영향, 신생아 안전성 미확립 |
| 10 | Flood factor deficiency (용어 미확인) | 99.40% | L5 | Hold | 질환 정의 불명확, 평가 불가 |

> ⚠️ **TTP 경고**: TTP는 과도한 혈전 형성이 핵심 병리입니다. 응고촉진제인 emicizumab 투여 시 미세혈관 혈전 부담을 가중시킬 가능성이 있어 **이 적응증은 강력히 비권장합니다.**

---

## 이 예측이 타당한 이유는?

Emicizumab은 FIXa(활성화 응고인자 IX)와 FX(응고인자 X)를 동시에 결합하는 이중특이성 단클론 항체입니다. 활성화 FVIII(FVIIIa)의 보조인자 기능을 모방하여 내인성 응고 경로의 텐나제(intrinsic tenase) 복합체를 우회적으로 재구성하고, FX를 FXa로 활성화시켜 응고 효소 연쇄 반응을 증폭합니다.

후천성 혈우병 A(AHA)는 FVIII에 대한 자가항체(억제제)가 내인성 FVIII를 중화하여 발생하는 희귀 출혈 질환입니다. Emicizumab의 FIXa-FX 교각 기전은 FVIII를 완전히 우회하므로, FVIII 억제제의 영향을 전혀 받지 않습니다. 이는 선천성 혈우병 A에서의 FVIII 결핍과 AHA에서의 FVIII 기능 상실이 동일한 응고 경로 차단을 공유한다는 점에서 기전적 논리가 직결됩니다.

GTH-AHA-EMI(Phase 2/3, *Lancet Haematology* 2023)와 AGEHA(Phase 3, *JTH* 2023; 최종 분석 2025)를 포함한 고질의 전향적 연구들이 AHA 환자에서 emicizumab 예방 투여의 출혈 감소 효과를 입증했습니다. 특히 기존 면역억제 요법(IST)의 부작용 위험이 높은 고령·허약 환자에서 emicizumab이 IST를 연기하면서도 출혈을 효과적으로 예방하는 전략이 확립되고 있으며, 유럽 일부 국가에서는 이미 AHA 적응증으로 허가 또는 확장 승인이 이루어진 상태입니다.

---

## 임상시험 근거 (후천성 응고인자 결핍증)

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT04398628](https://clinicaltrials.gov/study/NCT04398628) | N/A (관찰) | 모집 중 | 3,000 | ATHN Transcends: 비신생물성 혈액 질환(후천성 응고인자 결핍 포함)의 대규모 자연사 코호트. FDA 승인 신치료제의 장기 안전성·유효성 추적 및 실사용 치료 패턴 수집 목적. |

> 비개입 관찰 설계로 emicizumab의 직접적 효능 평가에는 한계가 있으나, 실사용 배경 데이터 및 AHA 자연사 파악에 기여합니다.

---

## 문헌 근거 (후천성 응고인자 결핍증)

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [36696195](https://pubmed.ncbi.nlm.nih.gov/36696195/) | 2023 | Phase 3 전향적 오픈라벨 | J Thromb Haemost | AGEHA 1차 분석: AHA 환자에서 emicizumab 예방 투여의 긍정적 유익-위험 프로파일 확인 |
| [37858328](https://pubmed.ncbi.nlm.nih.gov/37858328/) | 2023 | Phase 2/3 오픈라벨 단일군 | Lancet Haematology | GTH-AHA-EMI: emicizumab이 AHA 출혈 예방 및 초기 12주간 면역억제 연기 가능케 함 |
| [39134043](https://pubmed.ncbi.nlm.nih.gov/39134043/) | 2025 | Phase 3 최종 분석 | Thromb Haemost | AGEHA 최종 분석: IST 불가 환자(Cohort 2) 포함, emicizumab 장기 예방의 지속적 안전성·유효성 확인 |
| [40795229](https://pubmed.ncbi.nlm.nih.gov/40795229/) | 2025 | 종단 코호트 | Blood Advances | GTH-AHA-EMI 2년 추적: emicizumab과 IST 연기 전략이 AHA 생존 이점 지속적으로 제공 |
| [38049124](https://pubmed.ncbi.nlm.nih.gov/38049124/) | 2024 | 전문가 합의/임상 가이드라인 | Hamostaseologie | GTH-AHA 워킹그룹: AHA 환자에서 emicizumab 예방 사용을 위한 실무 합의 권고안 제시 |
| [39361769](https://pubmed.ncbi.nlm.nih.gov/39361769/) | 2024 | 실사용 다기관 코호트 | Blood Advances | 미국 12개 혈우병 치료센터 62명 AHA 환자: emicizumab 오프라벨 사용의 실사용 임상 이점 확인 |
| [39536818](https://pubmed.ncbi.nlm.nih.gov/39536818/) | 2025 | 서술 리뷰 | J Thromb Haemost | Emicizumab 시대의 AHA 포괄 관리 검토: 역학, 병태생리, 진단, 치료 전략 업데이트 |
| [38562115](https://pubmed.ncbi.nlm.nih.gov/38562115/) | 2024 | 리뷰 | Haemophilia | AHA·후천성 vW 증후군·만성 간질환 응고 이상 관리의 최신 진전 종합 |
| [36795341](https://pubmed.ncbi.nlm.nih.gov/36795341/) | 2023 | 비판적 논평/리뷰 | Blood Transfusion | AHA에서 emicizumab 적용의 장단점 비판적 검토: 현행 허가 현황과 확장 가능성 |
| [38936699](https://pubmed.ncbi.nlm.nih.gov/38936699/) | 2024 | 비교 분석 | J Thromb Haemost | Emicizumab vs 면역억제 요법: AHA 관리에서 각각의 역할 및 조합 전략 비교 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

> **문헌 기반 주요 안전성 고려사항:**
> - **aPCC 병용 금기**: Emicizumab과 활성 프로트롬빈 복합체 농축제(aPCC, FEIBA®) 병용 시 **혈전성 미세혈관병증(TMA) 및 혈전색전증** 발생 위험이 유의하게 증가합니다. AHA 환자 치료 시 aPCC 사용을 회피해야 합니다.
> - **rFVIIa 병용**: rFVIIa(NovoSeven®) 병용 시에도 주의가 필요하며, 투여 간격 및 용량 조절을 고려해야 합니다.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
후천성 혈우병 A에 대한 emicizumab의 효능을 지지하는 Phase 3 전향적 연구 3편(AGEHA, GTH-AHA-EMI)과 전문가 합의 권고안, 다기관 실사용 코호트 데이터가 일관되게 긍정적인 결과를 보입니다. FVIII 완전 우회 기전의 직접적 논리가 확립되어 있고, 유럽 일부 국가에서는 이미 AHA 적응증이 허가된 선례가 있어 근거 수준 L1을 충족합니다.

**진행하려면 필요한 것:**
- 국내 MFDS 규제 전략 수립 (현재 미허가 — 희귀의약품 지정 또는 허가 신청 경로 검토 필요)
- 작용 기전(MOA) 정식 데이터 확보 (DrugBank API 조회, data gap DG002 해소)
- 허가 안전성 정보 원문 확보 (경고 및 금기사항, data gap DG001 해소)
- aPCC 및 rFVIIa 병용 금기를 포함한 안전성 모니터링 프로토콜 수립
- 국내 후천성 혈우병 A 환자 규모 및 현행 치료 실태 역학 조사
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

