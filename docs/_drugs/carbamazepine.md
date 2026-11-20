---
layout: default
title: Carbamazepine
parent: 모델 예측만 (L5)
nav_order: 180
evidence_level: L5
indication_count: 3
monitor_inn: "Carbamazepine"
predicted_indications: ["trigeminal nerve neoplasm", "beta-ketothiolase deficiency", "Rett syndrome, congenital variant"]
last_modified_at: 2026-11-20
description: "Carbamazepine: 예측 신규 적응증 삼차신경 신생물 (근거 수준 L5). 기존 적응증: 1. 간질 : 정신운동발작, 간질성격 및 간질에 수반하는 정신장애, 간질의 경련발작…"
---

# Carbamazepine
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **3** 건
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

## Carbamazepine: 기존 허가 적응증에서 삼차신경 신생물(trigeminal nerve neoplasm)로
{: .text-alpha }

## 한 문장 요약

Carbamazepine은 한국에서 단일 성분 제제로 허가된 항경련제입니다. 다만 이번 데이터에는 허가 적응증 본문이 담겨 있지 않고 허가 문서 링크만 있어 구체적인 적응증을 확인할 수 없습니다.
TxGNN 모델은 **삼차신경 신생물**에 효과가 있을 수 있다고 예측하지만, 이 질환을 직접 연구한 임상시험은 없고 문헌도 대부분 삼차신경통의 증상 조절이나 종양 관련 증례 보고입니다.
따라서 근거는 모델 예측 수준(L5)에 머뭅니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 1. 간질 : 정신운동발작, 간질성격 및 간질에 수반하는 정신장애, 간질의 경련발작 [강직간대발작(대발작)] 2. 삼차신경통 3. 조병, 조울병의 조상태, 정신분열증의 흥분상태 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199802257/EE)) |
| 예측 신규 적응증 | 삼차신경 신생물 |
| TxGNN 예측 점수 | 1.0000 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 13건 / 전체 14건) |
| 허가증 수 | 14건 (유효 13건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Carbamazepine 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “Tegretol은 전기적 및 화학적으로 유발된 발작이 있는 랫드와 마우스에서 항경련 특성을 나타냈다. 이 약은 다시냅스 반응을 감소시키고 강직 후 증강을 차단함으로써 작용하는 것으로 보인다. […] Tegretol의 주요 대사체인 카르바마제핀-10,11-에폭사이드는 여러 생체 내 동물 발작 모델에서 입증된 바와 같이 항경련 활성을 가진다.” 영어 원문: "Tegretol has demonstrated anticonvulsant properties in rats and mice with electrically and chemically induced seizures. It appears to act by reducing polysynaptic responses and blocking the post-tetanic potentiation. […] The principal metabolite of Tegretol, carbamazepine-10,11-epoxide, has anticonvulsant activity as demonstrated in several in vivo animal models of seizures." ([DailyMed: Tegretol (carbamazepine) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8d409411-aa9f-4f3a-a52c-fbcb0c3ec053), 버전 2026-08-20; 확인일 2026-11-19). 일반적으로 알려진 정보에 따르면 carbamazepine은 나트륨 채널 차단제이며, 삼차신경통의 1차 치료제로 확립되어 있습니다.

삼차신경 주변의 종양(신경초종, 수막종, 유피낭종, 지방종, 정맥 혈관종 등)은 이차성 삼차신경통을 일으킬 수 있습니다. 이 경우 carbamazepine이 통증 증상을 완화할 수 있습니다. 그러나 종양 자체의 성장 억제, 조절, 퇴축에 작용한다는 근거는 없습니다.

높은 TxGNN 점수는 종양에 대한 항종양 효과보다는, TxGNN 모델(딥러닝)이 관련 질환 사이에서 학습한 유사성을 반영했을 가능성이 큽니다. 이는 생물학적 근거가 아니며, 이 약의 실제 적응증은 신생물이 아니라 신경통입니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

제공된 문헌은 모두 삼차신경통 또는 삼차신경 주변 병변에 관한 것으로, carbamazepine이 신생물 자체에 효과가 있음을 직접 연구한 문헌은 없습니다. 아래는 비교적 관련성이 높은 문헌입니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [36824641](https://pubmed.ncbi.nlm.nih.gov/36824641/) | 2022 | Review | Acta Clin Croat | 삼차신경통의 치료 옵션 개관. 혈관 압박이나 종양이 원인이 될 수 있음 |
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Review | Expert Rev Neurother | 삼차신경통의 내과적·외과적 치료 개관 |
| [30741017](https://pubmed.ncbi.nlm.nih.gov/30741017/) | 2023 | 증례 보고 | Br J Neurosurg | 삼차신경 원발성 림프종 환자에서 carbamazepine으로 증상이 호전되지 않음 |
| [25142539](https://pubmed.ncbi.nlm.nih.gov/25142539/) | 2014 | 증례 보고 | Rinsho Shinkeigaku | 삼차신경을 따라 퍼진 악성 림프종. 초기에는 carbamazepine에 반응했으나 이후 무효 |
| [15235745](https://pubmed.ncbi.nlm.nih.gov/15235745/) | 2004 | 증례 보고 | Arq Neuropsiquiatr | Meckel강 원발성 흑색종. carbamazepine으로 통증이 완화되지 않음 |
| [25433061](https://pubmed.ncbi.nlm.nih.gov/25433061/) | 2014 | 증례 보고 | No Shinkei Geka | 소뇌교각 지방종에 의한 삼차신경통. carbamazepine은 부작용으로 통증 조절이 불충분 |
| [33989821](https://pubmed.ncbi.nlm.nih.gov/33989821/) | 2021 | 증례 보고 | World Neurosurg | 추체사대 수막종에 의한 삼차신경통을 수술로 치료 |
| [3181365](https://pubmed.ncbi.nlm.nih.gov/3181365/) | 1988 | 동물 연구 | Exp Neurol | 실험적 신경종에서 carbamazepine이 자발적 신경 활동을 억제 (종양 치료 효과가 아님) |

## 한국 시판 정보

허가 적응증 본문은 데이터에 없고 허가 문서 링크만 제공되어, 적응증 열은 생략했습니다. 13건 모두 단일 성분 제제입니다. 아래는 주요 5건입니다.

| 허가번호 | 제품명 | 제형 | 제조사 |
|---------|------|------|-------|
| 200307816 | 테그레톨정200밀리그램 | 백색의 원형 정제 | 한국노바티스(주) |
| 200307818 | 테그레톨시럽2% | 백색의 점조성 시럽제 | 한국노바티스(주) |
| 200307819 | 테그레톨씨알정200밀리그램 | 서방성 필름코팅정 | 한국노바티스(주) |
| 199801575 | 부광티모닐서방정300밀리그램 | 백색의 원형 정제 | 부광약품(주) |
| 199101166 | 에필렙톨씨알정 | 필름코팅정 | 환인제약(주) |

이 밖에 수출용 제품(카바민씨알정, 대화카르바마제핀정, 카르마인정)을 포함한 8건이 더 있습니다.

## 안전성 고려사항

허가사항의 경고 및 금기 정보는 데이터에 포함되어 있지 않으므로, 안전성 정보는 허가사항을 참조하세요.

**약물 상호작용** (총 100건 중 일부 조회 결과)
- **주요(Major) 등급**: Clarithromycin, Eliglustat
- **중등도(Moderate) 등급**: Doxycycline, Hydrocortisone, Dexamethasone, Pioglitazone, Bupropion, Aprepitant, Morphine, Metronidazole, Cimetidine 등

종양 환자는 스테roid, 항구토제, 항생제 등을 병용하는 경우가 많아 상호작용 검토가 특히 중요합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
삼차신경 신생물 자체에 대한 임상시험이 없고, 문헌도 신경통 증상 조절이나 증례 보고에 한정됩니다. carbamazepine이 종양 자체에 작용한다는 근거가 없어 높은 예측 점수만으로는 진행하기 어렵습니다.

**진행하려면 필요한 것:**
- 허가사항(경고, 금기, 적응증) 원문 확보 (현재 안전성 검토를 진행할 수 없는 상태)
- 작용 기전 데이터 확보
- 신생물 자체에 대한 효과인지, 이차성 삼차신경통의 증상 완화인지 구분하는 연구 설계 또는 근거
- 신생물 환자에서 carbamazepine의 효과와 안전성을 평가한 임상 자료

---

*참고: 같은 약물에 대한 다른 예측(베타-케토티올라제 결핍증, Rett 증후군 선천성 변이형)은 임상시험과 문헌이 모두 없는 모델 예측뿐(L5)이며, 기전적 연관성도 확인되지 않아 보류가 적절합니다.*

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Tegretol (carbamazepine) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8d409411-aa9f-4f3a-a52c-fbcb0c3ec053) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

