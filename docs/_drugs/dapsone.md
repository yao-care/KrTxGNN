---
layout: default
title: Dapsone
parent: 모델 예측만 (L5)
nav_order: 250
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Dapsone: 예측 신규 적응증 주폐포자충증 (Pneumocystosis) (근거 수준 L5). 기존 적응증: 확인 불가 (허가 적응증 텍스트가 문서 링크로만 제공됨)"
monitor_inn: "DAPSONE"
predicted_indications: ["pneumocystosis"]
---

# Dapsone
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **1** 건
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

## Dapsone: 허가 적응증 미확인에서 주폐포자충증(Pneumocystosis)으로
{: .text-alpha }

## 한 문장 요약

Dapsone은 국내에서 단일제 정제(태극답손정 100mg)로 시판 중인 설폰계 약물이며, 이번 보고서에 정리된 데이터에서는 허가 적응증 본문을 확인할 수 없었습니다.
TxGNN 모델은 **주폐포자충증(Pneumocystosis)**에 효과가 있을 수 있다고 예측하며, 현재 **10건의 임상시험**과 **20편의 문헌**이 이 방향과 관련되어 있습니다. 이 중 완료된 Phase 3 임상시험은 4건입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (허가 적응증 텍스트가 문서 링크로만 제공됨) |
| 예측 신규 적응증 | 주폐포자충증 (Pneumocystosis) |
| TxGNN 예측 점수 | 99.73% |
| 근거 수준 | L1 (완료된 Phase 3 RCT 4건) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

현재 이 약의 상세한 작용 기전 데이터는 수집되지 않았습니다. 다만 일반적으로 알려진 바에 따르면, dapsone은 엽산 합성 경로의 디하이드로프테로에이트 합성효소(dihydropteroate synthase)를 억제하는 설폰계 약물이며, sulfamethoxazole 같은 설폰아미드계 약물과 같은 표적을 공유합니다.

*Pneumocystis jirovecii*는 이 엽산 경로에 의존하므로, 기전상 주폐포자충증에 적용 가능성이 있습니다. 실제로 dapsone은 trimethoprim-sulfamethoxazole(TMP-SMX)을 견디지 못하는 환자에서 폐포자충 폐렴(PCP)의 예방 및 치료 대안으로 연구되어 왔습니다. 이는 TxGNN의 높은 예측 점수와 부합합니다.

다만 이 제품의 허가 적응증과 기전 정보는 이번 데이터에서 확인되지 않았으므로, 허가사항에 근거한 검증이 별도로 필요합니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00000802](https://clinicaltrials.gov/study/NCT00000802) | Phase 3 | 완료 | 700 | TMP/설폰아미드 불내성 HIV 환자에서 PCP 예방: 매일 dapsone vs atovaquone |
| [NCT00000991](https://clinicaltrials.gov/study/NCT00000991) | Phase 3 | 완료 | 600 | 진행성 HIV 감염에서 3가지 항폐포자충제 + zidovudine 1차 예방 비교 |
| [NCT00001028](https://clinicaltrials.gov/study/NCT00001028) | Phase 3 | 완료 | 400 | TMP/설폰아미드 불내성 HIV 환자에서 흡입 pentamidine(월 1회) vs dapsone(주 3회) 예방 비교 |
| [NCT00000640](https://clinicaltrials.gov/study/NCT00000640) | Phase 3 | 완료 | 290 | AIDS 환자의 경증~중등도 PCP 치료: dapsone/trimethoprim 및 clindamycin/primaquine vs TMP/SMX |
| [NCT00002283](https://clinicaltrials.gov/study/NCT00002283) | 해당 없음 | 완료 | 미보고 | AIDS 환자의 첫 PCP 발병에서 dapsone vs TMP-SMX 치료의 효과 및 이상반응 비교 |
| [NCT00002043](https://clinicaltrials.gov/study/NCT00002043) | 해당 없음 | 완료 | 미보고 | AIDS 관련 복합증(ARC) 환자에서 PCP 1차 예방 dapsone 100mg vs 50mg 용량 비교 |
| [NCT00000739](https://clinicaltrials.gov/study/NCT00000739) | Phase 1 | 완료 | 96 | HIV 감염 소아에서 dapsone 매일 vs 주 1회 투여의 독성 및 약동학 비교 |
| [NCT00002120](https://clinicaltrials.gov/study/NCT00002120) | Phase 1 | 완료 | 20 | 중등도 PCP에서 trimetrexate + leucovorin + dapsone vs TMP/SMX의 안전성 평가 |
| [NCT02550080](https://clinicaltrials.gov/study/NCT02550080) | Phase 4 | 불명 | 3130 | dapsone 과민반응증후군 예방을 위한 HLA-B*1301 유전자 선별검사의 임상적 유용성 (PCP 환자 포함, 관련성 낮음) |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [38583518](https://pubmed.ncbi.nlm.nih.gov/38583518/) | 2024 | 메타분석 | Clin Microbiol Infect | HIV 환자 PCP 예방 요법(TMP-SMX, dapsone 기반, 흡입 pentamidine, atovaquone)의 효능·안전성 네트워크 메타분석 |
| [39732393](https://pubmed.ncbi.nlm.nih.gov/39732393/) | 2025 | 메타분석 | Clin Microbiol Infect | HIV 환자 PCP 치료 요법의 효능·안전성 네트워크 메타분석 |
| [27550992](https://pubmed.ncbi.nlm.nih.gov/27550992/) | 2016 | 가이드라인 | J Antimicrob Chemother | 혈액암·조혈모세포이식 환자의 PCP 예방 ECIL 가이드라인 (TMP-SMX가 1차 선택) |
| [33870843](https://pubmed.ncbi.nlm.nih.gov/33870843/) | 2021 | 리뷰 | Expert Opin Pharmacother | *P. jirovecii*의 예방 및 치료 중심 리뷰 |
| [11155588](https://pubmed.ncbi.nlm.nih.gov/11155588/) | 2001 | 리뷰 | Dermatol Clin | Dapsone이 HIV 환자의 PCP 예방에 유용함을 포함한 dapsone/sulfapyridine 개요 |
| [18971152](https://pubmed.ncbi.nlm.nih.gov/18971152/) | 2008 | 리뷰 | J Formos Med Assoc | 폐포자충 폐렴 전반 리뷰 |
| [1727534](https://pubmed.ncbi.nlm.nih.gov/1727534/) | 1992 | 리뷰 | Med Clin North Am | 주폐포자충증은 예방 및 치료가 가능한 질환임을 설명 |
| [7937279](https://pubmed.ncbi.nlm.nih.gov/7937279/) | 1994 | 리뷰 | Pharmacotherapy | 임신 중 PCP 예방 약물(TMP-SMX, pentamidine, dapsone 등) 검토 |
| [33280223](https://pubmed.ncbi.nlm.nih.gov/33280223/) | 2021 | 후향 연구 | Pediatr Transplant | 소아 신장이식 후 PJP 예방용 dapsone의 methemoglobinemia 부담 |
| [9606476](https://pubmed.ncbi.nlm.nih.gov/9606476/) | 1998 | 증례 보고 | Ann Pharmacother | PCP 예방 중 dapsone 유발 methemoglobinemia 증례 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 198300470 | 태극답손정100밀리그램 | 흰색의 타원형 정제 | 허가 적응증 본문 미확인 (허가사항 참조) |

## 안전성 고려사항

- **금기 관련 지식그래프 정보**(허가 문서가 아닌 TxGNN 지식그래프 기반): 간질환, 담낭질환, 빈혈, 대적혈구성 빈혈, G6PD 결핍증, 글리코겐 축적질환, 시스틴뇨증, 갈락토오스혈증, 피루브산 탈수소효소 E3 결핍, 메트헤모글로빈 환원효소 결핍에 의한 메트헤모글로빈혈증
- **약물 상호작용**: 총 100건이 조회되었습니다. 이 중 중등도로 분류된 주요 항목은 aprepitant, metronidazole, picosulfuric acid, nateglinide, nitisinone, rosuvastatin, simvastatin, tinidazole, 활성탄, troglitazone입니다.
- **문헌상 보고된 이상반응**: methemoglobinemia 및 저산소증, 간 합併증, 급성 췌장염 증례가 보고되어 있습니다.

허가사항의 경고 및 금기 본문은 이번 데이터에서 확인되지 않았으므로 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
완료된 Phase 3 RCT 4건이 PCP 예방 및 치료에서 dapsone을 직접 평가했고, 최근 메타분석도 있어 근거가 충분합니다. 다만 허가 적응증과 안전성 본문을 확인하지 못했고, 중대한 이상반응 위험이 있어 안전 조치가 필요합니다.

**진행하려면 필요한 것:**
- 허가사항(첨부문서) 확보 및 분석: 허가 적응증, 경고, 금기 확인
- 상세한 작용 기전(MOA) 데이터 보완
- 투여 전 G6PD 결핍 선별검사
- methemoglobinemia 및 용혈 모니터링 계획 (CBC, 간기능 포함)
- 병용약물 상호작용 검토
- 임상시험 대부분이 1990년대 HIV 환자 대상이므로, 현재 진료 환경에서의 적용성 평가
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

