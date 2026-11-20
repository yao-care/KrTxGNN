---
layout: default
title: Temozolomide
parent: 모델 예측만 (L5)
nav_order: 722
evidence_level: L5
indication_count: 1
monitor_inn: "TEMOZOLOMIDE"
predicted_indications: ["cauda equina neoplasm"]
last_modified_at: 2026-11-15
description: "Temozolomide: 예측 신규 적응증 마미총 종양 (근거 수준 L5). 기존 적응증: 1) 새로이 진단된 다형성 교아종(Glioblastoma multiforme)의 치료 ; 초기에는 방사선…"
---

# Temozolomide
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

## Temozolomide: 기존 허가 적응증에서 마미총 종양(Cauda Equina Neoplasm)으로
{: .text-alpha }

## 한 문장 요약

Temozolomide는 한국에서 단일성분 제제로 9건의 허가증이 있는 경구 알킬화제입니다. 다만 이번 보고서에 정리된 데이터에는 허가 적응증의 본문이 포함되어 있지 않습니다.
TxGNN 모델은 **마미총 종양(Cauda Equina Neoplasm)**에 효과가 있을 수 있다고 예측하지만, 이 질환을 직접 다룬 임상시험은 없고 **증례 보고 1건**만 확인됩니다.
따라서 현재 근거는 모델 예측 수준(L5)입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 1) 새로이 진단된 다형성 교아종(Glioblastoma multiforme)의 치료 ; 초기에는 방사선 치료와 병용 하며,이후 단독으로 투여한다. 2) 표준요법에 실패한 재발성, 진행성 다형성 교아종(Glioblastoma multiforme) 및 미분화성상세포종… ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201503273/EE)) |
| 예측 신규 적응증 | 마미총 종양 |
| TxGNN 예측 점수 | 0.9930 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 9건 / 전체 11건) |
| 허가증 수 | 11건 (유효 9건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Temozolomide 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “Temozolomide는 직접적인 활성은 없으나 생리적 pH에서 빠른 비효소적 전환을 거쳐 반응성 화합물인 5-(3-methyltriazen-1-yl)-imidazole-4-carboxamide(MTIC)로 변환된다. MTIC의 세포독성은 주로 DNA 알킬화, 특히 구아닌의 O 6 및 N 7 위치에서의 알킬화에 기인하는 것으로 생각되며, 이는 DNA 이중가닥 절단을 일으켜 세포예정사(programmed cell death)를 초래한다.” 영어 원문: "Temozolomide is not directly active but undergoes rapid nonenzymatic conversion at physiologic pH to the reactive compound 5-(3-methyltriazen-1-yl)-imidazole-4-carboxamide (MTIC). The cytotoxicity of MTIC is thought to be primarily due to DNA alkylation, mainly at the O 6 and N 7 positions of guanine, which causes DNA double strand breaks and results in programmed cell death." ([DailyMed: Temodar (temozolomide) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=046a9011-3911-4d3f-a15f-fbb56d5aad56), 버전 2026-02-20; 확인일 2026-11-19). 일반적으로 알려진 정보에 따르면 Temozolomide는 DNA를 메틸화(특히 O6-구아닌)하여 종양 세포에 세포독성 손상과 세포자멸사를 일으키는 경구 알킬화제입니다. 효과는 MGMT 발현이 낮거나 MGMT 프로모터가 메틸화된 경우에 크게 좌우됩니다.

마미총 종양은 대부분 점액유두상 상의세포종(myxopapillary ependymoma)이며, 그 밖의 상의세포·신경교 종양도 있습니다. Temozolomide는 혈액뇌장벽을 통과하고 교모세포종 같은 중추신경계 악성 종양에서 이미 사용되고 있어, 생물학적으로 그럴듯한 근거가 됩니다.

다만 마미총 종양의 MGMT 상태는 다양하고 충분히 규명되지 않아 기전적 연관성은 간접적입니다. 높은 TxGNN 점수는 계산상의 예측일 뿐 임상 근거를 대체하지 못합니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [29270703](https://pubmed.ncbi.nlm.nih.gov/29270703/) | 2018 | 증례 보고 | European Spine Journal | 여러 차례 재발하고 뇌척수액으로 파종된 척수 점액유두상 상의세포종에서 Temozolomide가 뚜렷한 효과를 보인 1례와 문헌 고찰 |
| [42760727](https://pubmed.ncbi.nlm.nih.gov/42760727/) | 2026 | 증례 보고 | Medicine | 비강 NUT 암종의 방사선 포함 다학제 치료 증례. 마미총 종양과는 직접 관련이 없음 |
| [18706663](https://pubmed.ncbi.nlm.nih.gov/18706663/) | 2009 | 증례 보고 | Neuro-Chirurgie | 뇌교 신경교종 소아의 신경수막 크립토코쿠스증 증례. 마미총 종양과는 직접 관련이 없음 |

마미총 종양과 직접 관련된 문헌은 첫 번째 증례 보고(척수 점액유두상 상의세포종) 1건뿐이며, 이는 마미총 부위 종양에 대한 간접적 단일 증례 근거입니다. 나머지 두 편은 이 질환과 관련성이 낮습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201503273 | 테모람캡슐20밀리그램 (일동제약) | 경질캡슐제 | 허가 문서 링크만 수록되어 본문 확인 불가 |
| 201503271 | 테모람캡슐250밀리그램 (일동제약) | 경질캡슐제 | 허가 문서 링크만 수록되어 본문 확인 불가 |
| 201502604 | 테몰드캡슐100밀리그램 (신풍제약) | 경질캡슐제 | 허가 문서 링크만 수록되어 본문 확인 불가 |
| 200511107 | 테모달캡슐100밀리그램 (한국엠에스디) | 캡슐제 | 허가 문서 링크만 수록되어 본문 확인 불가 |
| 201502602 | 테몰드캡슐250밀리그램 (신풍제약) | 경질캡슐제 | 허가 문서 링크만 수록되어 본문 확인 불가 |

허가증은 모두 9건이며, 위 표에는 주요 5건만 나열했습니다.

<!-- review:begin kr-lic-20261105-temozolomide-1 -->

> **검토 정정 (2026-11-05)**: 원래 문장: “허가증은 모두 9건이며, 위 표에는 주요 5건만 나열했습니다. 9건 모두 유효한 단일성분 제제입니다.” 삭제: 허가 건수나 상태가 성분 기준으로 다시 맞춘 2026-11-05 기준 식품의약품안전처(nedrug) 허가 자료와 맞지 않습니다. 이 약의 허가는 11건(유효 9건)이며, 현재 수치는 빠른 개요와 「한국 시판 정보」의 표에 있습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261105-temozolomide-1 -->

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 약물 (알킬화제) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요. 지식그래프에는 혈소판감소증, 호중구감소증, 범혈구감소증, 재생불량성 빈혈 등 혈액학적 금기 관계가 기록되어 있습니다. |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요. |
| 모니터링 항목 | 혈구 검사(CBC, 분류 포함), 간기능 |
| 취급 방호 | 세포독성 약물 취급 규정 준수 필요 |

## 안전성 고려사항

허가사항의 경고 및 금기 정보는 이번 데이터에 포함되어 있지 않으므로 허가사항을 참조하세요.

- **지식그래프 금기 관계(허가 문서 근거 아님)**: 간부전, 혈소판감소증, 호중구감소증, 무과립구증, 빈혈, 거대적아구성 빈혈, 뉴모시스티스증, 범혈구감소증, 림프구감소증, 골수이형성증후군, 특발성 재생불량성 빈혈, 재생불량성 빈혈
- **약물 상호작용**: 총 100건이 조회되었으며, 그중 주요 항목은 다음과 같습니다.
  - 중등도: Naltrexone
  - 경미: Levofloxacin
  - 등급 미상: Calcitriol, Pantoprazole, Doxycycline, Clotrimazole, Morphine, Metformin, Omeprazole, Lansoprazole, Prednisone 등

## 결론 및 다음 단계

**결정: Hold**

**사유:**
마미총 종양을 직접 연구한 임상시험은 없고 증례 보고 1건뿐이어서, 근거 수준은 모델 예측 단계(L5)입니다. 허가사항 기반의 안전성 정보도 확보되지 않아 현재로서는 진행을 보류하는 것이 적절합니다.

**진행하려면 필요한 것:**
- 식약처 허가사항(적응증, 경고, 금기) 원문 확보 및 분석
- DrugBank 등에서 작용 기전(MOA) 데이터 보완
- 마미총 종양(점액유두상 상의세포종 등)에서의 MGMT 상태 및 반응 자료 조사
- 해당 질환에 대한 추가 증례 시리즈, 관찰 연구 또는 임상시험 근거 탐색

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다. 작용 기전 자료가 없다는 문장은 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-05 | 삭제: “9건 모두 유효한 단일성분 제제입니다” | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Temodar (temozolomide) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=046a9011-3911-4d3f-a15f-fbb56d5aad56) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

