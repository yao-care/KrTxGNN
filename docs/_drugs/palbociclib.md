---
layout: default
title: Palbociclib
parent: 모델 예측만 (L5)
nav_order: 574
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-15
description: "Palbociclib: 예측 신규 적응증 갑상선기능항진증 (Hyperthyroidism) (근거 수준 L5). 기존 적응증: 이 약은 호르몬 수용체(HR)-양성 및 사람상피세포성장인자수용체2(HER2)-음성인 진행성 또는 전이성…"
monitor_inn: "Palbociclib"
predicted_indications: ["hyperthyroidism", "rheumatoid arthritis", "thrombotic disease", "resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta"]
---

# Palbociclib
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **4** 건
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

## Palbociclib: 유방암에서 갑상선기능항진증으로
{: .text-alpha }

## 한 문장 요약

Palbociclib은 CDK4/6 억제제로, 일반적으로 호르몬수용체 양성/HER2 음성 진행성·전이성 유방암 치료에 사용되는 약물입니다.
TxGNN 모델은 **갑상선기능항진증(Hyperthyroidism)**에 효과가 있을 수 있다고 예측하지만, 이 예측을 뒷받침하는 **임상시험은 0건, 문헌도 0편**이어서 현재는 모델 예측 단계에 머물러 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 이 약은 호르몬 수용체(HR)-양성 및 사람상피세포성장인자수용체2(HER2)-음성인 진행성 또는 전이성 유방암 치료에 아래와 같이 병용한다: · 여성에서 일차 내분비 요법으로서 아로마타제 억제제와 병용 또는 · 내분비요법 후 질환이 진행된 여성에서 풀베스트란트와 병용 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202300993/EE)) |
| 예측 신규 적응증 | 갑상선기능항진증 (Hyperthyroidism) |
| TxGNN 예측 점수 | 0.9944 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 12건 / 전체 12건) |
| 허가증 수 | 12건 (유효 12건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Palbociclib 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “팔보시클립은 사이클린 의존성 키나아제(CDK) 4 및 6의 억제제이다. 사이클린 D1 및 CDK4/6은 세포 증식을 유도하는 신호전달 경로의 하류에 위치한다. 시험관 내에서 팔보시클립은 세포가 세포주기의 G1기에서 S기로 진행하는 것을 차단함으로써 에스트로겐 수용체(ER) 양성 유방암 세포주의 세포 증식을 감소시켰다.” 영어 원문: "Palbociclib is an inhibitor of cyclin-dependent kinases (CDK) 4 and 6. Cyclin D1 and CDK4/6 are downstream of signaling pathways which lead to cellular proliferation. In vitro, palbociclib reduced cellular proliferation of estrogen receptor (ER)-positive breast cancer cell lines by blocking progression of the cell from G1 into S phase of the cell cycle." ([DailyMed: Ibrance (palbociclib) prescribing information, U.S. Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=89a142d5-7e61-48bf-9e77-e2cd124c4792), 버전 2026-07-06; 확인일 2026-11-19). 알려진 정보에 따르면 Palbociclib은 CDK4/6(사이클린 의존성 키나제 4/6)을 억제하는 세포주기 조절 약물이며, 유방암에서 효능이 입증되어 있습니다.

다만 이번에 정리한 자료에서는 CDK4/6 억제와 갑상선 호르몬 과잉 사이의 기전적 연결고리를 확인하지 못했습니다. 0.9944라는 높은 점수는 TxGNN 모델(딥러닝)이 산출한 것으로, 모델이 관련 질환 간에 학습한 유사성을 반영할 수 있으며 생물학적 근거를 의미하지는 않습니다. 갑상선기능항진증은 호르몬 과잉 분비를 조절해야 하는 질환이어서, 세포 증식을 억제하는 항종양 기전과는 치료 논리가 다릅니다. 따라서 이 예측은 현재로서는 타당성을 설명하기 어렵습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

한국에는 단일 성분 제품 12건이 유효 허가 상태입니다(취소 0건). 주요 허가 5건은 다음과 같습니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202200687 | 입랜스정125밀리그램 (한국화이자제약) | 필름코팅정 | 허가증 PDF 참조 |
| 202200688 | 입랜스정100밀리그램 (한국화이자제약) | 필름코팅정 | 허가증 PDF 참조 |
| 201605163 | 입랜스캡슐100mg (한국화이자제약) | 캡슐 | 허가증 PDF 참조 |
| 202300993 | 알렌시캡슐75밀리그램 (광동제약) | 캡슐 | 허가증 PDF 참조 |
| 202402383 | 랜클립정125밀리그램 (대웅제약) | 필름코팅정 | 허가증 PDF 참조 |

허가 적응증은 텍스트가 아닌 허가증 PDF 링크로만 제공되어 요약하지 못했습니다.

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적치료제 (CDK4/6 억제제) |
| 골수억제 위험 | 중등도 (CDK4/6 억제제의 흔한 이상반응으로 골수억제가 알려져 있음) |
| 구토 유발성 등급 | 저 |
| 모니터링 항목 | CBC (호중구 수 포함), 간기능 |
| 취급 방호 | 항종양약 취급 규정 준수 권장. 자세한 내용은 허가사항의 경고 및 주의사항을 참조하세요. |

## 안전성 고려사항

- **약물 상호작용**: 조회된 상호작용은 총 100건입니다. 이 중 확인된 주요 **Major** 등급 약물은 다음과 같습니다.
  - Clarithromycin
  - Cobicistat
  - Deferiprone
  - Samarium (153Sm) lexidronam
- **Moderate 등급 예시**: Aprepitant, Dexamethasone, Cimetidine, Simvastatin, Cilostazol 등
- 경고 및 금기 사항은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
갑상선기능항진증에 대한 임상시험과 문헌이 없고, 기전적 연결고리도 확인되지 않아 근거는 모델 예측뿐(L5)입니다. 이 질환에서 Palbociclib을 진행할 근거는 현재 없습니다.

**진행하려면 필요한 것:**
- CDK4/6 억제와 갑상선 호르몬 조절 사이의 기전적 근거 (전임상 연구 등)
- 허가사항(경고·금기) 원문 확인 및 안전성 검토
- 상세한 작용 기전 데이터 확보
- 참고: 같은 약물의 다른 예측 중 류마티스 관절염(전임상 및 증례 보고, L4)과 골수성 백혈병(Phase 1/2 임상시험 진행, L3)은 근거가 상대적으로 더 있어, 우선 검토 대상으로 고려할 수 있습니다.

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Ibrance (palbociclib) prescribing information, U.S. Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=89a142d5-7e61-48bf-9e77-e2cd124c4792) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

