---
layout: default
title: Molsidomine
parent: 높은 근거 (L1-L2)
nav_order: 527
evidence_level: L2
indication_count: 10
last_modified_at: 2026-10-15
description: "Molsidomine: 예측 신규 적응증 혈관 질환 (Vascular disease) (근거 수준 L2). 기존 적응증: 허가증에 적응증 원문이 없고 문서 링크만 제공되어 확인할 수 없습니다 (문헌상 관상동맥질환·협심증 치료제)"
monitor_inn: "Molsidomine"
predicted_indications: ["vascular disease", "alopecia", "hypotrichosis simplex of the scalp", "venous thoracic outlet syndrome", "idiopathic spontaneous coronary artery dissection", "arterial thoracic outlet syndrome", "visceral calciphylaxis", "neurogenic thoracic outlet syndrome", "congenital hypotrichosis milia", "hemangioendothelioma"]
---

# Molsidomine
{: .fs-9 }

근거 수준: **L2** | 예측 적응증: **10** 건
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

## Molsidomine: 협심증 등 허혈성 심질환에서 혈관 질환으로
{: .text-alpha }

## 한 문장 요약

Molsidomine은 산화질소(NO)를 방출하는 전구약물로, 한국에서 몰시톤정(2mg, 4mg)으로 허가되어 시판 중입니다. TxGNN 모델은 **혈관 질환(vascular disease)**에 효과가 있을 수 있다고 예측하며, 현재 **2건의 임상시험**과 **20편의 문헌**이 이 방향을 지지합니다. 다만 대부분의 문헌은 리뷰나 소규모 연구입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가증에 적응증 원문이 없고 문서 링크만 제공되어 확인할 수 없습니다 (문헌상 관상동맥질환·협심증 치료제) |
| 예측 신규 적응증 | 혈관 질환 (Vascular disease) |
| TxGNN 예측 점수 | 99.99995% |
| 근거 수준 | L2 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 2건 |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터(DrugBank)는 없습니다. 다만 문헌에 따르면 Molsidomine은 linsidomine(SIN-1)으로 전환되는 전구약물이며, NO를 방출해 가용성 구아닐산 고리화효소를 활성화하고 cGMP를 높입니다. 그 결과 혈관 확장, 혈소판 응집 억제, 내피 기능 개선 효과가 나타납니다(PMID 7620515, 8767924).

이러한 기전은 관상동맥질환, 말초동맥질환, 내피 기능 이상 등 혈관 질환 전반과 부합합니다. 실제로 말초동맥질환 환자에서 프로스타시클린과 병용 시 항혈소판 및 섬유소 용해 작용이 보고되었고, 안정형 협심증 환자의 내피 기능을 평가한 Phase 4 시험도 완료되었습니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01363661](https://clinicaltrials.gov/study/NCT01363661) | Phase 4 | 완료 | 165 | 경피적 관상동맥 중재술을 받는 안정형 협심증 환자에서 Molsidomine 추가 투여가 12개월 후 내피 기능(RH-PAT)을 개선하는지 평가한 이중맹검 위약대조 시험. 결과 데이터는 확인 필요 |
| [NCT00382421](https://clinicaltrials.gov/study/NCT00382421) | 해당 없음 | 완료 | 정보 없음 | SWISSI 1: 무증상 허혈 환자에서 항협심증 약물 치료와 위험인자 관리의 효과를 비교. Molsidomine 단독 위약대조 시험은 아님 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [2242448](https://pubmed.ncbi.nlm.nih.gov/2242448/) | 1990 | Review | Blood Vessels | Molsidomine은 SIN-1을 통해 NO를 방출하는 관상동맥질환 치료제 |
| [7914627](https://pubmed.ncbi.nlm.nih.gov/7914627/) | 1994 | Review | Lancet | Molsidomine 개요 (초록 없음) |
| [7620515](https://pubmed.ncbi.nlm.nih.gov/7620515/) | 1994 | Review | Pol J Pharmacol | 심장질환에서 NO 공여체의 역할과 내성 |
| [1790782](https://pubmed.ncbi.nlm.nih.gov/1790782/) | 1991 | Review | Eur Heart J | 유기질산염과 sydnonimine의 약력학적 작용이 유사함 |
| [8743336](https://pubmed.ncbi.nlm.nih.gov/8743336/) | 1996 | 약동학 리뷰 | Clin Pharmacokinet | 경구 생체이용률 44~59%, 최고 농도 도달 1~2시간 |
| [2651251](https://pubmed.ncbi.nlm.nih.gov/2651251/) | 1989 | 비교 임상시험 | Fortschr Med | 무작위 교차시험(20명)에서 운동 유발 협심증의 ST 하강을 감소시킴 (0.16 → 0.09 mV) |
| [8438599](https://pubmed.ncbi.nlm.nih.gov/8438599/) | 1993 | 임상연구 | Wien Klin Wochenschr | 말초동맥질환 환자 20명에서 프로스타시클린과 병용 시 섬유소 용해 및 항혈소판 작용이 상승 |
| [2598982](https://pubmed.ncbi.nlm.nih.gov/2598982/) | 1989 | 임상연구 | Eur J Clin Pharmacol | 관상동맥질환 환자 24명에서 nifedipine과 달리 폐동맥압과 좌심실 확장기말압을 유의하게 낮춤 |
| [3919549](https://pubmed.ncbi.nlm.nih.gov/3919549/) | 1985 | 전임상 | Am Heart J | 동물 허혈 모델에서 ST 상승 정상화 및 심장 보호·항혈전 작용 |
| [39316777](https://pubmed.ncbi.nlm.nih.gov/39316777/) | 2024 | 전임상 | ACS Appl Bio Mater | Molsidomine 탑재 액정 나노입자의 니아신 유도 하지정맥류 동물모델 치료 가능성 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 199802244 | 몰시톤정4밀리그램 (몰시도민) | 연분홍색 원형 정제 | 허가 문서 링크로만 제공되어 적응증 원문 확인 불가 |
| 199501832 | 몰시톤정2밀리그램 (몰시도민) | 주황색 원형 정제 | 허가 문서 링크로만 제공되어 적응증 원문 확인 불가 |

두 제품 모두 에리슨제약(주)이 제조하며 단일제로 유효 상태입니다.

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
혈관 질환 방향으로는 완료된 Phase 4 위약대조 시험 1건(165명)이 있고, NO 공여체 기전도 문헌에서 잘 확립되어 있습니다. 다만 Phase 3 RCT가 없고 결과 데이터가 확인되지 않았으며, 허가사항 기반 안전성 검토도 이루어지지 않아 조건부 진행을 권장합니다. 혈관 질환은 범위가 넓은 분류이므로, 관상동맥질환·말초동맥질환 등 구체적 적응증으로 좁혀야 합니다.

**진행하려면 필요한 것:**
- 허가증 PDF에서 허가 적응증, 경고, 금기 확인 (필수, 현재 안전성 선별 불가)
- NCT01363661의 주요 결과(내피 기능 개선 여부)와 안전성 결과 확인
- DrugBank에서 상세 작용 기전 데이터 확보
- 목표 혈관 질환의 세부 정의 및 대상 환자군 설정
- PDE5 억제제 등 병용 금기 약물, 저혈압 위험, 질산염 내성에 대한 모니터링 계획

**참고:** 2위 이하 예측 질환(탈모증, 흉곽출구증후군, 특발성 관상동맥 박리 등)은 모두 TxGNN 예측만 있고 임상시험이나 문헌 근거가 없어(L5) 보류(Hold)를 권장합니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

