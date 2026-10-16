---
layout: default
title: Mefenamic Acid
parent: 모델 예측만 (L5)
nav_order: 497
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-15
description: "Mefenamic Acid: 예측 신규 적응증 류마티스 관절염 (Rheumatoid Arthritis) (근거 수준 L5). 기존 적응증: 허가 문서 링크만 확인되며, 적응증 본문 텍스트는 확인되지 않음"
monitor_inn: "MEFENAMIC ACID"
predicted_indications: ["rheumatoid arthritis", "osteoarthritis susceptibility", "headache disorder", "trigeminal autonomic cephalalgia", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "migraine disorder", "migraine with brainstem aura"]
---

# Mefenamic Acid
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **8** 건
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

# Mefenamic Acid: 비스테로이드 소염진통제에서 류마티스 관절염으로

## 한 문장 요약

Mefenamic acid(메페남산)는 비스테로이드성 소염진통제(NSAID)로, 한국에서 8건의 허가(모두 수출용)가 유효한 약물입니다.
TxGNN 모델은 **류마티스 관절염(Rheumatoid Arthritis)**에 효과가 있을 수 있다고 예측하며, 현재 **20편의 문헌**이 이 방향을 다루지만 등록된 임상시험은 없습니다.
다만 같은 데이터에서 근거가 가장 탄탄한 후보는 **편두통(Migraine disorder)**과 **두통 질환(Headache disorder)**이며, 각각 이중맹검 RCT 문헌이 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 문서 링크만 확인되며, 적응증 본문 텍스트는 확인되지 않음 |
| 예측 신규 적응증 | 류마티스 관절염 (Rheumatoid Arthritis) |
| TxGNN 예측 점수 | 99.73% |
| 근거 수준 | L3 (소규모 이중맹검 교차시험 등 문헌 위주, 임상시험 등록 없음) |
| 한국 시판 현황 | ✓ 시판 중 (전 품목 수출용) |
| 허가증 수 | 8건 |
| 권장 결정 | Hold (연구 질문 단계) |

> 참고: 같은 약물의 다른 예측 중 **편두통(점수 99.23%, 근거 L2)**과 **두통 질환(점수 99.64%, 근거 L2)**은 Proceed with Guardrails 수준입니다. 아래 "결론"에서 함께 정리했습니다.

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 mefenamic acid는 COX-1/COX-2를 억제해 프로스타글란딘 합성을 줄이는 NSAID입니다. 프로스타글란딘은 류마티스 관절염의 염증과 통증에 관여하므로, 증상 완화 목적의 적용은 기전상 타당합니다.

1960~70년대 임상 비교 연구에서 mefenamic acid는 ibuprofen, sulindac, flurbiprofen, indomethacin과 비슷한 통증·조조강직 개선 효과를 보였습니다. 다만 이는 증상 완화 치료일 뿐 질병 경과를 바꾸는 약이 아니며, 현재는 다른 NSAID와 DMARD·생물학적제제가 이를 대체했습니다. 재창출 후보로서의 새로움은 제한적입니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [373989](https://pubmed.ncbi.nlm.nih.gov/373989/) | 1979 | RCT (이중맹검 교차) | Curr Med Res Opin | 24명 대상. mefenamic acid, sulindac, flurbiprofen 모두 위약보다 통증·관절압통·조조강직에서 우수 |
| [330287](https://pubmed.ncbi.nlm.nih.gov/330287/) | 1977 | 비교 임상시험 | J Int Med Res | 40명 대상. ibuprofen과 진통·항염 효과 차이 없음 |
| [796645](https://pubmed.ncbi.nlm.nih.gov/796645/) | 1976 | 비교 임상시험 | Med J Aust | ibuprofen과 비교해 대등한 효과, 부작용은 대부분 경미한 위장관 증상 |
| [326491](https://pubmed.ncbi.nlm.nih.gov/326491/) | 1977 | 이중맹검 교차시험 | Curr Med Res Opin | 18명 대상. mefenamic acid와 indomethacin 모두 위약보다 우수 |
| [4294443](https://pubmed.ncbi.nlm.nih.gov/4294443/) | 1967 | 임상 연구 | Ann Rheum Dis | 류마티스 관절염에서의 초기 소규모 임상 경험 |
| [5920657](https://pubmed.ncbi.nlm.nih.gov/5920657/) | 1966 | 비교 연구 | Br Med J | aspirin, phenylbutazone과의 비교 (초록 없음) |
| [1455792](https://pubmed.ncbi.nlm.nih.gov/1455792/) | 1992 | 임상 연구 | Vopr Kurortol Fizioter Lech Fiz Kult | 전기영동 투여 시 125명 중 75%에서 완전/부분 반응 |
| [5676955](https://pubmed.ncbi.nlm.nih.gov/5676955/) | 1968 | 증례 보고 | Br Med J | 장기 복용 중 자가면역 용혈성 빈혈 3례 (안전성 신호) |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201908188 | 폰스텔캡슐(수출용) | 경질캡슐 | 적응증 본문 미확인 (허가 문서 링크만 있음) |
| 199100581 | 유한메페남산캅셀250밀리그람(수출용) | 캡슐 | 적응증 본문 미확인 |
| 199903201 | 휴온스메페남산정(수출용) | 정제 | 적응증 본문 미확인 |
| 201507851 | 코러스메페남산캡슐250밀리그램(수출용) | 경질캡슐 | 적응증 본문 미확인 |
| 201507854 | 코러스메페남산정250밀리그램(수출용) | 필름코팅정 | 적응증 본문 미확인 |

## 안전성 고려사항

- **금기 (지식 그래프 기반, 허가 문구 아님)**: 고혈압, 신장 질환, 간 질환, 담낭 질환, 소화성 궤양(활동성 포함), 혈액 응고 질환, 심근경색, 관상동맥 혈전증, 헤모글로빈병증, 심혈관 질환, 심장 질환 등
- **약물 상호작용**: 총 100건이 조회되었으며, 확인된 항목은 다음과 같습니다.
  - 중등도: Acetylsalicylic acid, Metformin, Chlorpropamide, Hydrocortisone, Dexamethasone, Betamethasone, Triamcinolone, Budesonide, Mesalazine, Balsalazide, Aprepitant, Potassium citrate, Potassium bicarbonate 등
  - 경미: Famotidine, Ranitidine, Cimetidine, Dapagliflozin, Linaclotide
- **문헌상 안전성 신호**: 장기 복용 시 소장병증(융모 위축 동반), 자가면역 용혈성 빈혈, 약물과용 두통, 진통제 연관 신장 손상 보고가 있습니다.

허가사항의 경고 및 주의사항(MFDS 첨부문서)은 아직 확인되지 않았으므로 반드시 별도로 검토해야 합니다.

## 결론 및 다음 단계

**결정: Hold (류마티스 관절염)**

**사유:**
- 류마티스 관절염에 대한 근거는 1960~70년대 소규모 증상 완화 시험에 한정되며, 등록된 임상시험이 없습니다. 질병 조절 효과가 없고 현재 표준치료로 대체되어 재창출 가치가 낮습니다.
- 반면 **편두통(L2)**과 **두통 질환(L2)**은 이중맹검 RCT(월경성 편두통 위약 대조, 아세트아미노펜 비교, propranolol/위약 대비 예방 시험)가 있어 **Proceed with Guardrails**가 적절합니다. 다만 시험이 작고 오래되었으며, 단기·월경 주기 중심 사용과 위장관·신장 모니터링이 필요합니다.
- 골관절염 감수성, 삼차신경 자율신경성 두통, 편두통(뇌간 조짐형)은 근거가 부족하거나 간접적이며, 소안구증-근위지 이형성 증후군과 합지증-단지증 증후군은 기전적 연관성이 없어 보류합니다.

**진행하려면 필요한 것:**
- MFDS 허가사항(경고·금기 등) 확보 (현재 차단 수준의 데이터 공백)
- 작용 기전(MOA) 데이터 보완 (DrugBank 조회)
- 허가 적응증 본문 확인 (현재 문서 링크만 확인됨)
- 두통·편두통 후보에 대해 최신 가이드라인 기준의 근거 재평가와 안전성 모니터링 계획 수립 (위장관, 신장, 약물과용 두통)
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

