---
layout: default
title: Tamoxifen
parent: 모델 예측만 (L5)
nav_order: 717
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
monitor_inn: "Tamoxifen"
predicted_indications: ["mammary Paget disease", "Ehrlich tumor carcinoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina"]
description: "Tamoxifen: 예측 신규 적응증 유방 파제트병 (mammary Paget disease) (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199403106/EE"
---

# Tamoxifen
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

## Tamoxifen: 유방 파제트병 (mammary Paget disease)
{: .text-alpha }

## 한 문장 요약

Tamoxifen은 에스트로겐 수용체(ER)를 차단하는 항에스트로겐제로, 원래 호르몬 수용체 양성 유방암 치료에 사용되었습니다. TxGNN 모델은 **유방 파제트병(Mammary Paget Disease)**에 효과가 있을 수 있다고 예측합니다. 다만 이를 직접 뒷받침하는 임상시험은 없고(등록된 1건은 간접 관련), **증례 보고와 외과·재발 분석 위주의 문헌 10편**만 확인되어 근거는 약합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199403106/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199302443/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200402432/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199904114/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199203344/EE;  |
| 예측 신규 적응증 | 유방 파제트병 (mammary Paget disease) |
| TxGNN 예측 점수 | 0.9969 |
| 근거 수준 | L5 (기전적 타당성과 증례 수준의 간접 근거) |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 11건 (모두 유효, 단일제) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 이 보고서용으로 수집된 자료에 없습니다. 알려진 정보에 따르면 Tamoxifen은 선택적 에스트로겐 수용체 조절제(SERM)로, 유방 조직에서 ER 신호를 경쟁적으로 차단합니다. ER 양성 유방암에서 효능이 확립되어 있어, ER 양성 병변에는 기전상 적용 가능할 수 있습니다.

유방 파제트병은 대개 기저의 상피내암(DCIS)이나 침윤성 유방암과 동반되며, 이 종양 중 상당수가 호르몬 수용체 양성입니다. 따라서 ER 차단이라는 기전이 타당할 수 있습니다. 문헌에는 Tamoxifen에 반응한 증례도 있습니다. 광범위한 유두 파제트병에서 Tamoxifen 반응이 보고되었고, 호르몬 수용체 양성 전이성 유방외 파제트병 1례에서도 효과가 보고되었습니다.

다만 근거는 간접적입니다. 유방외 파제트병은 별개의 질환이며, 파제트병의 표준 치료는 여전히 수술(유방절제술 등)입니다. 유방 파제트병에서 Tamoxifen의 효능을 검증한 시험은 현재 없습니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00002920](https://clinicaltrials.gov/study/NCT00002920) | Phase 3 | 완료 | 313 | Tamoxifen을 복용하는 폐경 후 유방암 환자(유두 파제트병 포함)에서 Medroxyprogesterone과 관찰군을 비교해 자궁내막 병변 예방 효과를 평가했습니다. Tamoxifen의 부작용 관리 연구이며, Tamoxifen의 파제트병 치료 효과를 평가한 시험은 아닙니다. |

## 문헌 근거

문헌 중 RCT는 없고, 증례 보고, 코호트·증례집, 리뷰뿐입니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [34463889](https://pubmed.ncbi.nlm.nih.gov/34463889/) | 2022 | 증례 보고 | Investigational New Drugs | 호르몬 수용체 양성 전이성 유방외 파제트병에서 Tamoxifen 치료 성공 사례 (유방 파제트병과는 다른 질환) |
| [14965622](https://pubmed.ncbi.nlm.nih.gov/14965622/) | 2001 | 증례 보고 | Breast | 10년 이상 방치된 광범위한 유두 파제트병에서 Tamoxifen 반응이 있었고, 방사선 치료로 초기 완전 반응을 얻음 |
| [1648987](https://pubmed.ncbi.nlm.nih.gov/1648987/) | 1991 | 리뷰(증례 분석) | British Journal of Surgery | 유두 파제트병 48명 분석. 대부분 단순 유방절제술 등 수술을 받았고, Tamoxifen 치료는 1례 |
| [25759627](https://pubmed.ncbi.nlm.nih.gov/25759627/) | 2014 | 메타분석(코호트) | Breast Care | 파제트병에서 유방절제술 대비 유방보존술 후 국소 재발 비교. 전체 재발률은 20~40% |
| [16277886](https://pubmed.ncbi.nlm.nih.gov/16277886/) | 2005 | 코호트 | Clinical Breast Cancer | 유방보존치료 후 국소 재발로 나타난 유두 파제트병 보고 |
| [8955252](https://pubmed.ncbi.nlm.nih.gov/8955252/) | 1996 | 증례 보고 | The American Surgeon | 남성 유방 파제트병 1례와 문헌 32례 고찰 |
| [17319355](https://pubmed.ncbi.nlm.nih.gov/17319355/) | 2006 | 증례집 | Nigerian Journal of Clinical Practice | 유방암 환자 240명 중 8명(3.3%)이 유두-유륜 파제트병 |
| [19112575](https://pubmed.ncbi.nlm.nih.gov/19112575/) | 2009 | 코호트(증례) | Archives of Gynecology and Obstetrics | 외음부와 유방 파제트병이 동반된 드문 사례 |
| [12924421](https://pubmed.ncbi.nlm.nih.gov/12924421/) | 2003 | 증례 보고 | Surgery Today | 파제트병과 침윤성 유관암이 동시에 있는 양측성 유방암 1례 |
| [18288984](https://pubmed.ncbi.nlm.nih.gov/18288984/) | 2008 | 리뷰 | Current Medicinal Chemistry | 골소실 질환의 약물치료 리뷰 (파제트병과의 직접 관련성은 낮음) |

## 한국 시판 정보

한국에는 총 11건의 단일제 허가증이 유효하며, 이 중 4건은 수출용입니다. 허가 적응증은 본문이 아니라 허가 문서 링크로만 제공되어, 아래 표에는 내수용 주요 허가 5건과 문서 링크를 기재했습니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 199403106 | 타모프렉스정20밀리그램 (한독테바) | 정제 | [허가 문서 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199403106/EE) |
| 199302443 | 광동타목시펜정10밀리그램 (광동제약) | 필름코팅정 | [허가 문서 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199302443/EE) |
| 199907055 | 놀바덱스정 (한국아스트라제네카) | 필름코팅정 | [허가 문서 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199907055/EE) |
| 198801218 | 타목센정20밀리그램 (한국유나이티드제약) | 필름코팅정 | [허가 문서 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/198801218/EE) |
| 199203344 | 타모프렉스정10밀리그램 (한독테바) | 정제 | [허가 문서 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199203344/EE) |

## 세포독성

Tamoxifen은 일반적인 세포독성 화학요법제가 아니라 내분비 치료제입니다. 이 약의 세포독성 관련 상세 데이터는 이 보고서용으로 수집된 자료에 없으며, 아래는 약물 분류에 근거한 일반 정보입니다. 구체적인 경고와 주의사항은 허가사항을 참조하세요.

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 내분비 치료제 (SERM, 비세포독성) |
| 구토 유발성 등급 | 저 |
| 모니터링 항목 | CBC, 간기능, 자궁내막 이상 증상, 혈전 증상 |
| 취급 방호 | 허가사항의 경고 및 주의사항을 참조하세요 |

## 안전성 고려사항

- **금기 관련 질환(지식그래프 기반, 허가 본문이 아님)**: 혈소판감소증, 고칼슘혈증, 신석회화증, 인 대사 질환, 뇌졸중 및 뇌혈관 질환, 허혈성 뇌졸중 감수성, 뇌경색, 폐색전증, 백혈구감소증, 시각 장애, 실명
- **약물 상호작용**: 총 100건이 확인되었고, 아래는 그중 일부입니다.
  - **Major**: Bupropion, Cimetidine, Lorcaserin, Dolasetron, Eliglustat, Cisapride, Dexfenfluramine, Fenfluramine
  - **Moderate**: Famotidine, Loperamide, Aprepitant, Dexamethasone, Clarithromycin, Granisetron, Levofloxacin 등
  - **Minor**: Fidaxomicin

허가사항상의 주요 경고와 금기는 이 보고서용 자료에서 확인되지 않아, 안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
유방 파제트병에 대한 직접적인 임상시험이 없고, 근거는 증례 보고와 외과·재발 분석뿐입니다. 등록된 Phase 3 시험도 Tamoxifen 부작용(자궁내막 병변) 예방을 다룰 뿐 효능을 검증하지 않았습니다. ER 차단이라는 기전은 타당하지만, 표준 치료가 수술이므로 근거가 더 쌓일 때까지 보류합니다.

참고로 같은 예측 목록의 유방 상피내암(DCIS)과 ER 양성 유방암은 Phase 3 RCT 근거가 있는 기존 확립 적응증이라 신규 재창출 후보로 보기 어렵습니다.

**진행하려면 필요한 것:**
- 파제트병 환자(특히 기저 DCIS·유방암이 ER 양성인 경우)에서 Tamoxifen의 보조요법 효과를 평가한 코호트 연구나 임상시험
- 수술 후 보조 내분비 치료로서의 재발 감소 효과 분석
- ER/HER2 상태별 반응성 데이터
- 허가사항의 경고·금기(혈전, 자궁내막암 위험 등)와 약물 상호작용(CYP2D6 관련 포함) 확인
- 작용 기전 상세 데이터
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

