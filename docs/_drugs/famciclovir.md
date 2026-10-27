---
layout: default
title: Famciclovir
parent: 모델 예측만 (L5)
nav_order: 337
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-15
description: "Famciclovir: 예측 신규 적응증 수두 (Chickenpox) (근거 수준 L5). 기존 적응증: 허가 적응증 원문이 링크 형태로만 제공되어 구체적 문구를 확인할 수 없음 (대상포진·헤르페스 감염 계열로 추정)"
monitor_inn: "FAMCICLOVIR"
predicted_indications: ["post-infectious neuralgia", "sequela of COVID-19", "hepatitis C induced liver cirrhosis", "malignant pleural mesothelioma", "AIDS-related disorder", "malignant epithelioid mesothelioma", "chickenpox", "sarcomatoid mesothelioma", "malignant visceral pleura tumor"]
---

# Famciclovir
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **9** 건
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

## Famciclovir: 헤르페스 바이러스 감염에서 수두(Chickenpox)로
{: .text-alpha }

## 한 문장 요약

Famciclovir는 penciclovir의 전구약물로, 원래 헤르페스 바이러스 감염(대상포진 등) 치료에 사용되었습니다.
TxGNN 모델은 **수두(Chickenpox)**에 효과가 있을 수 있다고 예측하며, 현재 **5건의 관련 임상시험**과 **20편의 문헌**이 이 방향을 지지합니다. 다만 수두 자체에 대한 직접 근거는 소아 약동학·안전성 시험 1건에 그치며, 대부분은 대상포진(VZV 재활성화) 근거입니다.

> 참고: 이 보고서는 TxGNN 예측 순위 1위(대상포진 후 신경통)가 아니라, 근거가 가장 풍부한 7위 예측(수두)을 중심으로 작성했습니다. 1위 및 기타 예측은 결론 부분에서 간략히 정리합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 원문이 링크 형태로만 제공되어 구체적 문구를 확인할 수 없음 (대상포진·헤르페스 감염 계열로 추정) |
| 예측 신규 적응증 | 수두 (Chickenpox) |
| TxGNN 예측 점수 | 99.11% (수두 기준; 전체 1위 예측인 대상포진 후 신경통은 99.75%) |
| 근거 수준 | L1 (완료된 Phase 3 시험 2건 존재, 단 수두 직접 근거는 제한적) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 20건 (모두 단일제, 유효) |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

현재 이 약물의 상세한 작용 기전(MOA) 데이터는 데이터베이스에 없습니다. 다만 알려진 정보에 따르면 famciclovir는 체내에서 penciclovir로 전환되는 전구약물이며, penciclovir 삼인산이 바이러스 DNA 중합효소를 억제하여 VZV(수두-대상포진 바이러스)와 HSV의 복제를 막습니다.

수두와 대상포진은 같은 바이러스(VZV)가 일으키는 질환입니다. 수두는 초감염, 대상포진은 잠복 바이러스의 재활성화입니다. 따라서 VZV DNA 중합효소를 억제하는 기전은 수두에도 이론적으로 적용될 수 있습니다.

다만 기존 적응증의 연장선에 가까워 엄밀한 의미의 재창출이라고 보기는 어렵습니다. 또한 대상포진 근거를 일차 수두에 자동으로 외삽해서는 안 됩니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00098046](https://clinicaltrials.gov/study/NCT00098046) | Phase 3 | 완료 | 76 | 1~12세 VZV 감염 소아에서 famciclovir 경구 소아용 제형의 약동학 및 안전성 평가 |
| [NCT01327144](https://clinicaltrials.gov/study/NCT01327144) | Phase 3 | 완료 | 177 | 대상포진 환자에서 famciclovir 500 mg과 aciclovir 400 mg의 효능·안전성을 비교한 무작위 다기관 시험 |
| [NCT07099157](https://clinicaltrials.gov/study/NCT07099157) | Phase 4 | 모집 중 | 140 | 급성 대상포진에서 brivudine과 famciclovir 비교 (통증, 대상포진 후 신경통 발생률 등) |
| [NCT03120962](https://clinicaltrials.gov/study/NCT03120962) | 해당 없음 | 불명 | 140 | 대상포진 급성기 oxycodone 조기 사용이 대상포진 후 신경통을 예방하는지 평가 (famciclovir 미투여) |
| [NCT06798662](https://clinicaltrials.gov/study/NCT06798662) | 해당 없음 | 모집 전 | 120 | 급성 대상포진 통증에 대한 신경차단술과 고주파 치료 (famciclovir 시험 아님) |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [29431387](https://pubmed.ncbi.nlm.nih.gov/29431387/) | 2017 | Review | Am Fam Physician | 대상포진 및 대상포진 후 신경통의 예방과 관리 |
| [33672709](https://pubmed.ncbi.nlm.nih.gov/33672709/) | 2021 | Review | Molecules | VZV 감염 관리의 최신 동향과 전망 |
| [36851652](https://pubmed.ncbi.nlm.nih.gov/36851652/) | 2023 | Review | Viruses | 암 환자의 HSV·VZV 감염 |
| [42693145](https://pubmed.ncbi.nlm.nih.gov/42693145/) | 2026 | Review | Nat Rev Dis Primers | VZV 감염 전반(수두, 대상포진, 합병증) 개관 |
| [21486500](https://pubmed.ncbi.nlm.nih.gov/21486500/) | 2011 | Review | BMJ Clin Evid | 수두의 역학 및 치료 |
| [9675639](https://pubmed.ncbi.nlm.nih.gov/9675639/) | 1997 | 문헌고찰 | Intervirology | valaciclovir와 famciclovir가 대형 임상시험에서 대상포진 및 성기 헤르페스 치료와 zoster 관련 통증에 효과적임을 기술 |
| [12182687](https://pubmed.ncbi.nlm.nih.gov/12182687/) | 2002 | 문헌고찰 | Drugs Aging | 고령자 바이러스성 피부 감염의 진단과 관리 (famciclovir, valaciclovir는 투여 횟수가 적은 신규 항바이러스제) |
| [11487454](https://pubmed.ncbi.nlm.nih.gov/11487454/) | 2001 | 문헌고찰 | Curr Treat Options Neurol | 발진 후 3일 이내 시작 시 famciclovir, valacyclovir, 고용량 acyclovir가 유익함 |
| [10375341](https://pubmed.ncbi.nlm.nih.gov/10375341/) | 1999 | Review | Ann Intern Med | VZV 감염의 최신 지견 (AIDS 환자의 새로운 임상 증후군 포함) |
| [11904784](https://pubmed.ncbi.nlm.nih.gov/11904784/) | 2002 | 문헌고찰 | Support Care Cancer | 줄기세포 이식 후 바이러스 감염 관리 (acyclovir, valaciclovir, famciclovir 사용) |

> 위 문헌은 대부분 리뷰이며 수두에서 famciclovir의 효능을 직접 입증한 무작위 대조시험은 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201306322 | 팜시정250밀리그램 | 흰색의 원형 필름코팅정 | 허가사항 문서 참조 (원문 링크만 제공됨) |
| 201403232 | 팜시날정 | 흰색의 원형 필름코팅정 | 허가사항 문서 참조 |
| 202200268 | 팜시론정750밀리그램 | 흰색의 장방형 필름코팅 정제 | 허가사항 문서 참조 |
| 200600500 | 팜시르정250밀리그램 | 흰색 원형의 필름코팅정 | 허가사항 문서 참조 |
| 200500714 | 클로비어정 | 흰색원형의 필름코팅정제 | 허가사항 문서 참조 |

위 5건은 전체 20건 중 일부이며, 모두 famciclovir 단일제 경구 정제입니다.

## 안전성 고려사항

- **금기(지식 그래프 기반)**: TxGNN 지식 그래프에는 신장 질환(kidney disease), 농뇨(pyoureter)가 금기 질환으로 연결되어 있습니다. 허가사항 문구가 아니므로 참고용입니다.
- **약물 상호작용**: 총 84건이 확인되었으며 위험도 등급은 모두 미분류입니다. 예시로 calcitriol, doxycycline, metformin, omeprazole, morphine, prednisone, simvastatin, vancomycin 등이 있습니다.

주요 경고와 금기 등 허가사항 기반 안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
famciclovir는 VZV에 직접 작용하는 항바이러스제이며, 대상포진 Phase 3 시험(NCT01327144)과 소아 VZV 감염 Phase 3 약동학·안전성 시험(NCT00098046)이 완료되어 있습니다. 다만 일차 수두에 대한 효능 근거는 소아 약동학·안전성 시험 1건뿐이므로 조건부로 진행합니다.

**진행하려면 필요한 것:**
- 소아 용량 확인 및 수두 적응증 범위 검증 (대상포진 데이터를 수두로 자동 외삽하지 않음)
- 한국 허가사항 원문(경고, 금기, 적응증)의 확보 및 분석
- 신기능 저하 환자에 대한 용량 조절 및 안전성 계획
- 작용 기전(MOA) 데이터 보강

**다른 예측 적응증 요약:**

| 순위 | 예측 적응증 | 점수 | 근거 수준 | 권장 |
|------|-----------|------|---------|------|
| 1 | 감염 후 신경통 | 99.75% | L4 | Hold (연결된 시험은 oxycodone 연구로, famciclovir 근거는 간접적) |
| 2 | 코로나19 후유증 | 99.73% | L5 | Hold (타당한 기전 연결 없음, 그래프상 인공물 가능성) |
| 3 | C형 간염 유발 간경변 | 99.73% | L5 | Hold (HCV는 RNA 바이러스이며 famciclovir 활성 근거 없음) |
| 4 | 악성 흉막 중피종 | 99.46% | L5 | Hold (모델 예측만 존재) |
| 5 | AIDS 관련 질환 | 99.30% | L4 | Research Question (헤르페스 바이러스 합병증에 한정된 간접 근거) |
| 6 | 악성 상피양 중피종 | 99.14% | L5 | Hold (모델 예측만 존재) |
| 8 | 육종양 중피종 | 99.09% | L5 | Hold (모델 예측만 존재) |
| 9 | 악성 내장 흉막 종양 | 99.04% | L5 | Hold (모델 예측만 존재) |
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

