---
layout: default
title: Apremilast
parent: 모델 예측만 (L5)
nav_order: 80
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Apremilast: 예측 신규 적응증 류마티스 관절염 (Rheumatoid Arthritis) — 예측 순위 3위, 근거가 있는 가장 유망한 후보 (근거 수준 L5). 기존 적응증: 한국 허가 문서 링크만 확인되며, 허가 적응증 본문은 이번 데이터에 포함되어 있지 않습니다"
monitor_inn: "Apremilast"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "rheumatoid arthritis", "pulmonary hypertension", "migraine with or without aura, susceptibility to", "kyphoscoliotic heart disease", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "atrophoderma vermiculata", "ulerythema ophryogenesis"]
---

# Apremilast
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

# Apremilast: 건선성 관절염에서 류마티스 관절염으로

## 한 문장 요약

Apremilast는 PDE4(포스포디에스테라제-4) 억제제로, 원래 건선성 관절염 등 염증성 질환 치료에 사용되는 약물입니다.
TxGNN 모델의 최상위 예측은 **편두통(Migraine disorder)**이지만 이를 뒷받침하는 임상시험과 문헌은 없습니다. 반면 근거가 가장 풍부한 예측은 **류마티스 관절염(Rheumatoid Arthritis)**으로, **3건의 임상시험**(Phase 2)과 **20편의 문헌**이 있으며 이 보고서는 이 적응증을 중심으로 평가합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 한국 허가 문서 링크만 확인되며, 허가 적응증 본문은 이번 데이터에 포함되어 있지 않습니다 |
| 예측 신규 적응증 | 류마티스 관절염 (Rheumatoid Arthritis) — 예측 순위 3위, 근거가 있는 가장 유망한 후보 |
| TxGNN 예측 점수 | 98.09% (참고: 1위 편두통 98.66%, 근거 없음) |
| 근거 수준 | L2 (류마티스 관절염 기준) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 5건 |
| 권장 결정 | Hold (추가 연구 질문 단계, 연구 질문으로 분류) |

> 참고: 예측 1위(편두통)와 2위(뇌간 조짐 편두통)는 임상시험과 문헌이 전혀 없어 L5 / Hold입니다. 이 보고서에서는 근거가 실제로 존재하는 류마티스 관절염을 상세히 다룹니다.

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 다만 데이터에 포함된 문헌에 따르면 apremilast는 경구용 PDE4 억제제입니다. PDE4를 억제하면 세포 내 cAMP가 증가하고, TNF-α, IL-17, IL-23 등 염증 매개 물질이 감소합니다.

이러한 기전은 류마티스 관절염의 활막 염증과 관련이 있습니다. 또한 apremilast가 건선성 관절염(관련 염증성 관절병증)에 승인되어 있다는 점도 생물학적 타당성을 높입니다. 전임상 연구에서는 사람 류마티스 활막 세포의 TNF-α 자발적 생성 억제(PMID 20525198)와 마우스 관절염 모델 개선(PMID 30072998)이 보고되었습니다.

다만 Phase 2 무작위 대조시험(PMID 25779750)이 있음에도 류마티스 관절염 허가나 Phase 3 개발로 이어지지 않았습니다. 편두통 예측은 cAMP 신호와 신경염증 관련 가능성은 있으나 모델 예측에 그칩니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01285310](https://clinicaltrials.gov/study/NCT01285310) | Phase 2 | 조기 종료 | 237 | 메토트렉세이트 반응이 불충분한 활동성 RA에서 apremilast 두 용량의 이중맹검 위약대조 비교. 가장 정보량이 많으나 조기 종료로 해석에 한계 |
| [NCT01250548](https://clinicaltrials.gov/study/NCT01250548) | Phase 2 | 완료 | 34 | RA에서 apremilast와 위약 비교(안전성, 반응 시간, 효과 지속). 소규모로 검정력 부족 |
| [NCT01204138](https://clinicaltrials.gov/study/NCT01204138) | Phase 2 | 철회 | 0 | TNF 억제제 병용 활동성 RA 대상 교차 시험. 등록 0명으로 자료 없음 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [25779750](https://pubmed.ncbi.nlm.nih.gov/25779750/) | 2015 | RCT (Phase II) | Arthritis & Rheumatology | 메토트렉세이트 반응이 불충분한 활동성 RA에서 apremilast의 효능·안전성을 위약과 비교 |
| [24797159](https://pubmed.ncbi.nlm.nih.gov/24797159/) | 2014 | Review | Drugs | PDE4 억제제 apremilast의 첫 글로벌 승인(건선성 관절염)과 RA 등 개발 현황 |
| [20525198](https://pubmed.ncbi.nlm.nih.gov/20525198/) | 2010 | 전임상 | Arthritis Res Ther | 사람 RA 활막 세포의 TNF-α 자발적 생성 억제, 실험적 관절염 개선 |
| [30072998](https://pubmed.ncbi.nlm.nih.gov/30072998/) | 2018 | 전임상 | Front Immunol | 마우스 관절염 모델에서 Th1·Th17 세포 억제, 조절 T세포 분화 증진 |
| [26097790](https://pubmed.ncbi.nlm.nih.gov/26097790/) | 2014 | 약동학 연구 | Clin Pharmacol Drug Dev | RA·건선성 관절염 환자에서 apremilast와 메토트렉세이트 병용 시 약동학적 영향 평가 |
| [35956914](https://pubmed.ncbi.nlm.nih.gov/35956914/) | 2022 | Review | Molecules | 2010~2022년 초 PDE4 억제제 임상시험 개관 |
| [40283434](https://pubmed.ncbi.nlm.nih.gov/40283434/) | 2025 | Review | J Clin Med | 리툭시맙·apremilast·upadacitinib의 관절염 치료 현황 |
| [28891341](https://pubmed.ncbi.nlm.nih.gov/28891341/) | 2017 | Review | Expert Opin Pharmacother | 중등도~중증 건선성 관절염 소분자 치료 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202400868 | 오테리아정 (동아에스티) | 필름코팅정 10/20/30mg | 허가사항 문서 참조 |
| 202400867 | 압솔라정 (대웅제약) | 필름코팅정 10/20/30mg | 허가사항 문서 참조 |
| 202400869 | 오테벨정 (종근당) | 필름코팅정 10/20/30mg | 허가사항 문서 참조 |
| 202400870 | 오테밀라정 (동구바이오제약) | 필름코팅정 10/20/30mg | 허가사항 문서 참조 |
| 202400906 | 소프레정 (한림제약) | 필름코팅정 10/20/30mg | 허가사항 문서 참조 |

## 안전성 고려사항

- **약물 상호작용**: 총 75건이 확인되었으며, 이 중 주요(Major) 등급은 다음과 같습니다.
  - Lumacaftor
  - Fosphenytoin
  - Apalutamide
- 그 외 Dexamethasone, Deferasirox, Bosentan, Griseofulvin 등 다수가 중등도(Moderate) 상호작용으로 확인되었습니다. 주요 상호작용 약물은 CYP 효소 유도 가능성이 있어 병용 시 효과 감소 여부를 확인해야 합니다.

경고 및 금기 사항은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
류마티스 관절염에 대해 Phase 2 RCT 1건(PMID 25779750)이 있어 L2 수준이지만, 관련 임상시험 중 하나는 조기 종료되었고 다른 하나는 소규모이며, Phase 3 개발이나 허가로 이어지지 않았습니다. 예측 1위인 편두통을 포함한 나머지 예측(편두통 계열, 폐고혈압, 희귀 증후군 등)은 모델 예측만 있는 L5로, 폐고혈압 관련 문헌은 건선 등 무관한 내용이어서 키워드 우연 일치로 보입니다.

**진행하려면 필요한 것:**
- 한국 허가 적응증 및 경고·금기 정보 확보(허가사항 PDF 분석)
- 상세한 작용 기전(MOA) 데이터 확보
- 류마티스 관절염 Phase 2 RCT(PMID 25779750)와 NCT01285310의 대응 여부 확인 및 조기 종료 사유 검토
- 편두통 등 상위 예측에 대한 전임상·임상 근거 탐색
- 경로 적합성(투여 경로) 및 기존 적응증과의 유사성 평가 완료
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

