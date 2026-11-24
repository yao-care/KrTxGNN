---
layout: default
title: Ritonavir
parent: 모델 예측만 (L5)
nav_order: 660
evidence_level: L5
indication_count: 3
monitor_inn: "RITONAVIR"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
last_modified_at: 2026-11-24
description: "Ritonavir: 예측 신규 적응증 고양이 후천성 면역결핍 증후군 (근거 수준 L5). 기존 적응증: HIV-1 감염 환자 치료를 위한 프로테아제 억제제와의 병용요법"
---

# Ritonavir
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

## Ritonavir: HIV 감염에서 고양이 후천성 면역결핍 증후군으로
{: .text-alpha }

## 한 문장 요약

Ritonavir는 HIV-1 단백분해효소 억제제로 알려진 약물이며, 한국에는 단일 성분 제제로 허가되어 있습니다. TxGNN 모델은 **고양이 후천성 면역결핍 증후군(feline acquired immunodeficiency syndrome)**에 효과가 있을 수 있다고 예측하지만, 이 질환에 대한 임상시험과 문헌은 **0건**입니다. 이 예측은 모델 예측 수준(L5)에 머무르며, 수의학 적응증이라 인체 약물 재창출 범위 밖입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | HIV-1 감염 환자 치료를 위한 프로테아제 억제제와의 병용요법 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201106064/EE)) |
| 예측 신규 적응증 | 고양이 후천성 면역결핍 증후군 |
| TxGNN 예측 점수 | 0.9992 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 2건 / 전체 3건) |
| 허가증 수 | 3건 (유효 2건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Ritonavir 처방 정보(Prescribing Information)의 “Mechanism of Action” 및 “Microbiology” 항목에 따르면(비공식 번역): “리토나비르는 항레트로바이러스제이다. […] 리토나비르는 HIV-1 프로테아제의 펩티드 모방 억제제이다. HIV 프로테아제가 억제되면 이 효소가 Gag-Pol 다단백질 전구체를 처리할 수 없게 되어 감염성이 없는 미성숙 HIV 입자가 생성된다.” 영어 원문: "Ritonavir is an antiretroviral drug. […] Ritonavir is a peptidomimetic inhibitor of the HIV-1 protease. Inhibition of HIV protease renders the enzyme incapable of processing the Gag-Pol polyprotein precursor which leads to production of non-infectious immature HIV particles." ([DailyMed: Norvir (ritonavir) prescribing information, AbbVie Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2849298e-de6e-47bb-8194-56e075b33fc3), 버전 2026-07-23; 확인일 2026-11-19). 다만 일반적으로 ritonavir는 HIV-1 단백분해효소 억제제로 알려져 있으며, 고양이 면역결핍 바이러스(FIV)도 구조적으로 관련된 단백분해효소를 가지고 있어 기전상 연관성을 생각해 볼 수 있습니다.

그러나 FIV 단백분해효소는 HIV-1과 기질 특이성 및 억제제 감수성이 다르며, HIV 단백분해효소 억제제에 대한 FIV의 감수성 저하가 보고된 바 있습니다. 0.9992의 TxGNN 점수는 모델 예측일 뿐 실제 연구로 뒷받침되지 않습니다. 또한 이 질환은 동물(수의학) 적응증입니다.

참고로 같은 점수대에서 다음 후보도 예측되었습니다.
- **시미안 면역결핍 바이러스 감염(SIV)**: 마카크 원숭이 전임상 연구와 시험관 감수성 연구 문헌이 있으나, SIV는 HIV의 동물 모델이어서 새로운 인체 적응증이라기보다 연구 도구로서의 가치가 큽니다. (예: PMID 12709355는 SIV가 ritonavir 등 단백분해효소 억제제에 의해 억제됨을 보고했습니다.)
- **운동실조 보행·언어 소실·피질 백질 감소를 동반한 신경발달장애**: 단백분해효소 억제와의 기전적 연관성이 확인되지 않아 모델 산물일 가능성이 높습니다.

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 201106064 | 노비르정(리토나비르) | 흰색의 장방형 필름코팅정 | 한국애브비(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201106064/EE) | 유효 |

위 표는 허가 3건 중 1건입니다.

<!-- licenses:end -->

허가 정보에는 단일 성분 제제(노비르정, 한국애브비) 외에 리토나비르 복합제(팍스로비드정, 칼레트라정)도 있습니다. 허가 건수와 상태는 빠른 개요와 위 표에 있습니다.

<!-- review:begin kr-lic-20261124-ritonavir-1 -->

> **검토 정정 (2026-11-24)**: 원래 문장: “허가 정보는 단일 성분 제제 1건(한국애브비)이며, 시판 여부(취소 상태)는 확인되지 않았습니다.” 식품의약품안전처 의약품안전나라(nedrug) 허가 자료(2026-11-23 데이터) 기준으로 수정했습니다: 이 약의 허가에는 단일제 노비르정 외에 복합제 팍스로비드정(니르마트렐비르, 리토나비르)과 칼레트라정이 있고, 허가 상태(취소/취하 여부)도 자료에 있습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261124-ritonavir-1 -->

## 안전성 고려사항

허가사항의 경고 및 금기 정보는 이번에 수집된 자료에 없으므로 허가사항을 참조하세요.

**지식그래프에 기록된 금기 관계** (허가 문서가 아닌 TxGNN 지식그래프 기반):
- 심장·전도계: QT 연장 증후군, 가족성 QT 연장 증후군, torsades de pointes, 급성 심정지, 심장 전도 질환, 방실 차단, 심근 허혈, 관상동맥 질환, 심근병증
- 간·담도·췌장: 췌장염, 간 질환, 간경변, 담낭 질환, 고빌리루빈혈증, 길버트 증후군, 만성 B형 간염
- 대사: 고혈당, 당뇨병, 당뇨병성 케톤산증, 고중성지방혈증, 고지혈증, 통풍, 칼륨 결핍
- 기타: 혈우병

**약물 상호작용** (DDInter 기준, 총 100건 중 일부):
- 주요(Major): Loperamide, Triamcinolone, Budesonide
- 중등도(Moderate): Acarbose, Hydrocortisone, Metformin, Alosetron, Bupropion, Aprepitant, Dexamethasone, Clarithromycin, Metronidazole 등

## 결론 및 다음 단계

**결정: Hold**

**사유:**
고양이 후천성 면역결핍 증후군에 대한 임상시험과 문헌이 전혀 없고 점수는 모델 예측에 불과합니다. 또한 수의학 적응증이어서 인체 약물 재창출 범위를 벗어나며, FIV 단백분해효소의 감수성 차이도 우려됩니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기·적응증) 확보: 식약처(MFDS) 허가 PDF를 내려받아 분석
- 작용 기전(MOA) 데이터 보충: DrugBank 조회
- FIV 단백분해효소에 대한 ritonavir의 시험관/동물 효능 자료
- 인체 재창출이 목적이라면 인체 질환 중심의 후보 재선정 검토

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다. 작용 기전 자료가 없다는 문장은 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Norvir (ritonavir) prescribing information, AbbVie Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2849298e-de6e-47bb-8194-56e075b33fc3) |
| 2026-11-24 | 허가 구성: “단일 성분 제제 1건, 시판 여부 미확인” → 단일제(노비르정)와 복합제(팍스로비드정, 칼레트라정) | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

