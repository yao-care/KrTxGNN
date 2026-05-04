---
layout: default
title: Azathioprine
parent: 僅模型預測 (L5)
nav_order: 110
evidence_level: L5
indication_count: 10
---

# Azathioprine
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

# Azathioprine: 자가면역질환 치료에서 염증성 장질환으로

## 한 문장 요약

Azathioprine은 퓨린 유사체 계열의 면역억제제로, 전 세계적으로 장기이식 거부반응 예방 및 류마티스 관절염 등 자가면역질환 치료에 사용되어 왔습니다.
TxGNN 모델은 **염증성 장질환(Inflammatory Bowel Disease, IBD)**에 효과가 있을 것으로 예측하며, 이는 약물의 T 림프구 억제 기전과 IBD의 핵심 병태생리가 직접 부합하기 때문입니다.
현재 **50건 이상의 임상시험**과 **20편의 문헌**(코크란 체계적 문헌고찰 및 Phase 3 RCT 다수 포함)이 이 방향을 강력히 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 한국 미허가 (글로벌: 장기이식 거부반응 예방, 자가면역질환) |
| 예측 신규 적응증 | 염증성 장질환 (Inflammatory Bowel Disease) |
| TxGNN 예측 점수 | 99.52% |
| 근거 수준 | L1 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

Azathioprine은 체내에서 활성 대사체인 6-티오구아닌 뉴클레오타이드(6-TGN)로 전환됩니다. 6-TGN은 DNA에 삽입되어 Rac1/Vav 신호경로를 차단함으로써 T 림프구의 세포자멸사(apoptosis)를 유도하고, 장점막의 과도한 면역 반응을 억제합니다. TPMT 및 NUDT15 약물유전체학적 표현형이 대사 속도를 결정하여 치료 효과와 독성에 영향을 미칩니다.

IBD(크론병 및 궤양성 대장염)는 T 세포 매개 장점막 면역 과활성이 핵심 병태생리로, azathioprine의 작용 기전이 질환의 근본 원인에 직접 작용합니다. 특히 궤양성 대장염에서는 Th2/Th9 매개 결장 점막 과활성화에 대응하여 IL-13, IL-9 등 염증성 사이토카인을 감소시키고 점막 관해를 유지합니다. 실제로 전 세계 주요 IBD 치료 가이드라인에서 azathioprine은 스테로이드 의존성 또는 저항성 IBD의 1차 면역조절제로 확고히 자리 잡고 있으며, 다수의 Phase 3 RCT와 코크란 체계적 문헌고찰이 그 효과를 뒷받침합니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00094458](https://clinicaltrials.gov/study/NCT00094458) | Phase 3 | 완료 | 508 | 면역조절제·생물학적 제제 미치료 크론병 환자에서 infliximab, azathioprine, 병용 요법의 안전성 및 효과 비교 (SONIC 연구 배경); azathioprine 대조군으로서 높은 직접 증거 |
| [NCT01536535](https://clinicaltrials.gov/study/NCT01536535) | Phase 4 | 완료 | 431 | 새로 진단된 소아·청소년 궤양성 대장염에서 mesalamine 및 코르티코스테로이드 포함 표준 초기 요법의 안전성·유효성 평가; azathioprine 포함 표준 요법 근거 확인 |
| [NCT00946946](https://clinicaltrials.gov/study/NCT00946946) | Phase 3 | 완료 | 78 | 수술 후 중등도~중증 내시경 재발 크론병에서 azathioprine 대 mesalazine의 임상 재발 예방 효과 비교 (이중맹검 이중위약 RCT) |
| [NCT00976690](https://clinicaltrials.gov/study/NCT00976690) | Phase 3 | 완료 | 83 | 크론병 수술 후 재발 예방에서 azathioprine의 mesalazine 대비 우월성 평가 (다기관 무작위 공개 연구) |
| [NCT00098111](https://clinicaltrials.gov/study/NCT00098111) | Phase 3 | 조기종료 | 31 | 코르티코스테로이드 치료가 필요한 활성 크론병에서 azathioprine의 최적 체중 기반 용량 탐색 (ACORDIS); azathioprine 직접 연구로 설계 적합성 높음 |
| [NCT03101800](https://clinicaltrials.gov/study/NCT03101800) | Phase 3 | 상태 불명 | 84 | 궤양성 대장염에서 저용량 azathioprine + allopurinol 대 azathioprine 단독 요법의 유효성·안전성 비교; 치료 최적화 전략 근거 |
| [NCT02852694](https://clinicaltrials.gov/study/NCT02852694) | Phase 4 | 완료 | 192 | 위험도 층화 소아 크론병에서 azathioprine 대 메토트렉세이트(저위험군) 또는 adalimumab(고위험군) 비교 RCT; azathioprine 유지 요법 소아 적용 근거 |
| [NCT02425852](https://clinicaltrials.gov/study/NCT02425852) | Phase 4 | 완료 | 65 | 급성 중증 궤양성 대장염에서 infliximab + azathioprine 조기 병용 대 스테로이드 + azathioprine의 효과 비교 |
| [NCT05535946](https://clinicaltrials.gov/study/NCT05535946) | Phase 3 | 진행 중 (모집 완료) | 1,116 | 중등도~중증 활성 궤양성 대장염에서 ABX464 유지 요법 장기 평가; azathioprine 기존 치료 실패 환자 포함, 장기 안전성 비교 데이터 제공 |
| [NCT01802593](https://clinicaltrials.gov/study/NCT01802593) | Phase 4 | 조기종료 | 20 | 면역조절제 치료 실패 소아 크론병에서 infliximab 단독 전환 시 azathioprine 중단 시기 평가; 유지 치료 내 azathioprine 역할 간접 확인 |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [40013523](https://pubmed.ncbi.nlm.nih.gov/40013523/) | 2025 | 코크란 체계적 문헌고찰 | Cochrane Database Syst Rev | 궤양성 대장염에서 azathioprine 및 6-MP의 관해 유지 효과 최신 업데이트; 최고 수준 근거 |
| [39586616](https://pubmed.ncbi.nlm.nih.gov/39586616/) | 2025 | RCT | Gut | 정맥 스테로이드 반응성 급성 중증 궤양성 대장염에서 infliximab + azathioprine 병용 대 azathioprine 단독 유지 요법 비교 (ACTIVE trial) |
| [27192092](https://pubmed.ncbi.nlm.nih.gov/27192092/) | 2016 | 코크란 체계적 문헌고찰 | Cochrane Database Syst Rev | 궤양성 대장염에서 azathioprine 및 6-MP의 관해 유지 효과 종합 분석 |
| [22972046](https://pubmed.ncbi.nlm.nih.gov/22972046/) | 2012 | 코크란 체계적 문헌고찰 | Cochrane Database Syst Rev | 궤양성 대장염에서 azathioprine 관해 유지 효과 코크란 리뷰 (2012년판) |
| [19392869](https://pubmed.ncbi.nlm.nih.gov/19392869/) | 2009 | 메타분석 | Aliment Pharmacol Ther | 궤양성 대장염에서 azathioprine 및 mercaptopurine 유효성 메타분석; 크론병 대비 UC에서의 효과 비교 |
| [29293971](https://pubmed.ncbi.nlm.nih.gov/29293971/) | 2018 | 리뷰 | J Crohn's Colitis | IBD에서 thiopurine 치료 최신 동향 및 임상적 시사점 종합; 전문가 합의 기반 실무 지침 |
| [37586320](https://pubmed.ncbi.nlm.nih.gov/37586320/) | 2023 | 실험연구 | Cell Reports Medicine | IBD에서 장내 세균 Blautia wexlerae가 6-MP 생체이용률 감소를 통해 azathioprine 치료 실패를 유발하는 기전 규명; 치료 최적화에 중요한 임상적 함의 |
| [19072367](https://pubmed.ncbi.nlm.nih.gov/19072367/) | 2008 | 기전 리뷰 | Expert Rev Gastroenterol Hepatol | Azathioprine의 분자 기전 최신 분석 및 IBD 임상 치료에서의 시사점; 45년 임상 경험 기반 근거 종합 |
| [22072847](https://pubmed.ncbi.nlm.nih.gov/22072847/) | 2011 | 임상 리뷰 | World J Gastroenterol | IBD 치료에서 6-MP 및 azathioprine 최적화 전략; 6-TGN 농도 모니터링 및 대사 경로 실무 지침 |
| [16048561](https://pubmed.ncbi.nlm.nih.gov/16048561/) | 2005 | 약물유전체 리뷰 | J Gastroenterol Hepatol | Azathioprine 및 6-MP의 약물유전체학과 IBD에서의 대사체 모니터링; TPMT 다형성과 치료 반응 및 독성의 연관성 |

---

## 한국 시판 정보

현재 Azathioprine은 한국 내 허가된 의약품이 없습니다 (허가증 0건, 미시판 상태).

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
IBD 적응증에 대해 다수의 완료된 Phase 3 RCT, 코크란 체계적 문헌고찰, 메타분석이 azathioprine의 유효성을 직접 뒷받침하며 근거 수준 L1로 평가됩니다. 그러나 한국 내 미허가 상태이고 허가사항의 경고·금기 정보가 아직 확인되지 않아 안전성 검토 체계 구축이 선행되어야 합니다.

**진행하려면 필요한 것:**
- 한국 식품의약품안전처(MFDS) 허가 전략 수립 (해외 허가 데이터 기반 직접 허가 신청 검토)
- DrugBank MOA 데이터 확인을 통한 상세 작용 기전 문서화
- MFDS/TFDA 허가사항 기반 경고, 금기, 주요 약물 상호작용 정보 수집
- TPMT 및 NUDT15 약물유전체 검사 프로토콜 수립 (특히 한국인 집단의 NUDT15 R139C 변이 빈도가 서양인 대비 높아 용량 조절 필요)
- 한국인 IBD 환자에서의 골수억제, 감염 위험 등 이상반응 모니터링 계획 수립
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

