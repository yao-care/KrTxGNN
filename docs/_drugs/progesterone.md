---
layout: default
title: Progesterone
parent: 모델 예측만 (L5)
nav_order: 630
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Progesterone: 예측 신규 적응증 무월경 (Amenorrhea) (근거 수준 L5). 기존 적응증: 허가 적응증 본문은 허가증 링크로만 제공되어 이번 데이터에서 확인되지 않음 (제품별 허가사항 참조)"
monitor_inn: "Progesterone"
predicted_indications: ["amenorrhea (disease)", "breast fibrocystic disease", "benign mammary dysplasia", "renal hypoplasia, bilateral", "cervix endometriosis", "renal hypoplasia (disease)", "endometriosis in cutaneous scar", "endometriosis of rectovaginal septum and vagina", "blunt duct adenosis of breast"]
---

# Progesterone
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
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

# Progesterone: 한국 허가 적응증에서 무월경(Amenorrhea)으로

## 한 문장 요약

Progesterone은 천연 여성 호르몬으로, 한국에서 질좌제·겔·주사제 등 7건의 단일제 허가로 시판되고 있습니다. TxGNN 모델은 **무월경(Amenorrhea)**에 효과가 있을 수 있다고 예측하며, 이와 관련해 **4건의 임상시험**과 **19편의 문헌**이 수집되었습니다. 다만 임상시험은 대부분 progesterone이 직접 시험 대상이 아니어서 근거는 간접적입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문은 허가증 링크로만 제공되어 이번 데이터에서 확인되지 않음 (제품별 허가사항 참조) |
| 예측 신규 적응증 | 무월경 (Amenorrhea) |
| TxGNN 예측 점수 | 99.9996% |
| 근거 수준 | L2 (아래 설명 참조) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 7건 (모두 단일제, 유효) |
| 권장 결정 | Proceed with Guardrails |

> 근거 수준 참고: 완료된 Phase 2/3 시험(NCT00088153)이 1건 있어 L2 기준에 형식상 부합하지만, 이 시험은 estrogen 투여가 중심이며 progesterone은 주 시험약이 아닌 것으로 보입니다. 실제 직접 근거는 L2보다 낮게 해석해야 합니다.

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 progesterone은 내인성 여성 성호르몬으로, 자궁내막을 분비기로 전환시키고 시상하부-뇌하수체-난소 축의 조절에 관여합니다.

무월경에서는 progesterone(또는 progestin)이 두 가지 방식으로 사용됩니다. 첫째, 프로게스틴 위약출혈 검사로 내인성 에스트로겐 상태를 진단합니다. 둘째, 속발성 무월경에서 위약출혈을 유도하고, 에스트로겐으로 자극된 자궁내막을 보호합니다. 운동선수나 신경성 식욕부진증 등 저에스트로겐성 기능성 시상하부 무월경은 주로 에스트로겐 보충으로 관리하며, 자궁내막 보호를 위해 progesterone을 병용합니다. 경구 미분화 progesterone의 내분비 영역 진단·치료 활용은 2024년 리뷰(PMID 38652231)에 정리되어 있습니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00946192](https://clinicaltrials.gov/study/NCT00946192) | Phase 3 | 완료 | 121 | 월경이 멈춘 젊은 운동선수에서 경피·경구 에스트로겐의 골밀도 개선 효과 평가. progesterone의 역할은 불명확 |
| [NCT00088153](https://clinicaltrials.gov/study/NCT00088153) | Phase 2/3 | 완료 | 110 | 신경성 식욕부진증 청소년에서 에스트로겐 투여가 골 발달 유지에 도움이 되는지 평가. progesterone은 주기적 병용 성분으로 추정 |
| [NCT03740204](https://clinicaltrials.gov/study/NCT03740204) | Phase 2 | 활성, 모집 종료 | 120 | 저에스트로겐 섭식장애 여성에서 경피 estradiol + 주기적 progesterone vs 위약의 인지 유연성·보상 처리 평가 |
| [NCT03018366](https://clinicaltrials.gov/study/NCT03018366) | Phase 2 | 완료 | 29 | 기능성 시상하부 무월경 여성의 심혈관 위험 인자 평가. 무월경은 대상 집단이며 치료 목표가 아님 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [38652231](https://pubmed.ncbi.nlm.nih.gov/38652231/) | 2024 | Review | Rev Endocr Metab Disord | 내분비 영역에서 경구 미분화 progesterone의 진단·치료적 사용 |
| [34405378](https://pubmed.ncbi.nlm.nih.gov/34405378/) | 2022 | Review | Rev Endocr Metab Disord | 자궁내막증 호르몬 치료의 내분비학적 배경 |
| [33716979](https://pubmed.ncbi.nlm.nih.gov/33716979/) | 2021 | Review | Front Endocrinol | 조기난소부전(POI)의 병인, 증상, 치료 |
| [22283375](https://pubmed.ncbi.nlm.nih.gov/22283375/) | 2012 | 리뷰성 논문 | Gynecol Endocrinol | 배란의 신경내분비 조절과 시상하부성 무월경 |
| [28257537](https://pubmed.ncbi.nlm.nih.gov/28257537/) | 2017 | 리뷰성 논문 | South Med J | 원발성 난소부전 개념, 속발성 무월경과 호르몬 대체요법 |
| [8629565](https://pubmed.ncbi.nlm.nih.gov/8629565/) | 1996 | Review | Am Fam Physician | 무월경 평가 방법 |
| [32233689](https://pubmed.ncbi.nlm.nih.gov/32233689/) | 2020 | Review | Climacteric | 폐경 후 질출혈의 임상 관리 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200705309 | 예나트론 질좌제 | 질좌제 | 허가증 원문 참조 |
| 200711790 | 크리논겔 8% | 겔 | 허가증 원문 참조 |
| 202600485 | 유티프로주 25밀리그램 | 주사제 | 허가증 원문 참조 |
| 200706721 | 타이유프로게스테론주 | 주사제(유성액) | 허가증 원문 참조 |
| 202008202 | 사이클로제스트 질좌제 400밀리그램 | 질좌제 | 허가증 원문 참조 |

이 외에 프롤루텍스주 25밀리그램(201805378), 사이클로제스트 질좌제 200밀리그램(201108835)이 있어 총 7건입니다.

## 안전성 고려사항

- **약물 상호작용**: 당뇨병 치료제와의 중등도(Moderate) 상호작용이 다수 보고되었습니다(총 100건 중 일부 확인). 대표 항목은 다음과 같습니다.
  - 혈당강하제: acarbose, metformin, pioglitazone, glimepiride, repaglinide, chlorpropamide
  - DPP-4 억제제 및 SGLT2 억제제: alogliptin, saxagliptin, canagliflozin, dapagliflozin, empagliflozin
  - GLP-1 계열 및 인슐린: albiglutide, dulaglutide, liraglutide, semaglutide, insulin aspart, insulin degludec, insulin detemir
  - 기타: aprepitant, clarithromycin

경고 및 금기 사항은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
무월경에서 progesterone은 진단(위약출혈 검사)과 치료(자궁내막 보호, 출혈 유도)에 이미 임상적으로 쓰이고 있어 기전적 타당성이 높습니다. 다만 수집된 임상시험은 모두 에스트로겐 중심이거나 무월경 집단을 대상으로 한 연구여서 progesterone 단독 효과를 입증하는 직접 근거는 부족합니다.

**진행하려면 필요한 것:**
- 허가사항 PDF에서 경고·금기·허가 적응증 확인 (현재 안전성 검토 진행을 막는 핵심 공백)
- 작용 기전(MOA) 데이터 보완 (DrugBank 등)
- 무월경 유형(원발성/속발성, 저에스트로겐성 등)별 progesterone 사용 근거 정리
- 투여 경로 적합성 검토 (질좌제, 주사제, 겔 중 무월경에 적합한 제형)

**참고: 다른 예측 적응증**
유방 섬유낭성 질환(L4), 자궁내막증(L4), 양성 유방 이형성증(L4)은 근거가 오래되었거나 간접적이며 Hold 또는 연구 과제 수준입니다. 양측 신형성부전, 자궁경부 자궁내막증, 피부 흉터 자궁내막증, 직장질중격 자궁내막증, 유방 둔성관 선증은 L5로, 모델 예측만 있고 임상 근거가 없어 Hold를 권장합니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

