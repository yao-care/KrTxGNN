---
layout: default
title: Letrozole
parent: 높은 근거 (L1-L2)
nav_order: 470
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-15
description: "Letrozole: 예측 신규 적응증 여성 유방암 (Female Breast Carcinoma) (근거 수준 L1). 기존 적응증: 허가 문서 링크만 확인됨 (본문 미확인). 알려진 용도는 호르몬 수용체 양성 유방암"
---

# Letrozole
{: .fs-9 }

근거 수준: **L1** | 예측 적응증: **10** 건
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

# Letrozole: 유방암(허가 적응증)에서 여성 유방암으로 — 기존 적응증과 거의 일치하는 예측

## 한 문장 요약

Letrozole은 비스테로이드성 아로마타제 억제제로, 한국에서 단일제로 허가·시판 중입니다. TxGNN 모델은 **여성 유방암(female breast carcinoma)**에 효과가 있을 것으로 예측하며, 이 예측은 임상시험 40건 이상과 문헌 20편이 지지합니다. 다만 이 예측은 이미 알려진 호르몬 수용체 양성 유방암 치료와 사실상 같은 영역이어서, 엄밀한 의미의 새로운 재창출 발견은 아닙니다.

> 참고: 한국 허가증에 연결된 적응증 정보는 문서 링크 형태로만 확인되며, 본문 텍스트는 이번 데이터에 포함되어 있지 않습니다. 따라서 아래 기존 적응증은 약물의 알려진 용도(호르몬 수용체 양성 유방암 치료)에 근거해 정리했습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 문서 링크만 확인됨 (본문 미확인). 알려진 용도는 호르몬 수용체 양성 유방암 |
| 예측 신규 적응증 | 여성 유방암 (Female Breast Carcinoma) |
| TxGNN 예측 점수 | 99.98% |
| 근거 수준 | L1 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 6건 (모두 유효, 단일제) |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 이번 데이터에 포함되어 있지 않습니다. 다만 수집된 문헌과 근거 평가에 따르면, letrozole은 안드로겐이 에스트로겐으로 전환되는 과정을 막는 비스테로이드성 아로마타제 억제제입니다. 에스트로겐 의존성 종양의 성장을 낮추는 방식으로 작용합니다.

호르몬 수용체 양성 유방암은 에스트로겐이 종양 성장을 이끄는 질환이므로, 에스트로겐 생성을 줄이는 이 기전이 그대로 적용됩니다. 따라서 이 예측은 새로운 용도 발견이라기보다 **이미 확립된 적응증을 모델이 재확인한 것**으로 보는 것이 적절합니다.

같은 맥락에서 상위 예측 10건 중 다수가 유방암의 하위 유형입니다. 이 중 호르몬 수용체 양성 질환(여성 유방암, 에스트로겐 수용체 양성 유방암)은 근거가 풍부합니다. 반면 에스트로겐 수용체 음성 유방암은 기전상 효과를 기대하기 어렵고, 임상 근거도 대부분 수용체 양성 환자 대상이라 온톨로지 용어 중복에 따른 연관으로 보입니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT02941926](https://clinicaltrials.gov/study/NCT02941926) | Phase 3 | 완료 | 3,246 | HR+/HER2- 진행성 유방암에서 ribociclib + letrozole의 안전성·효능 (COMPLEEMENT-1) |
| [NCT02600923](https://clinicaltrials.gov/study/NCT02600923) | Phase 3 | 완료 | 131 | 폐경 후 HR+ 진행성 유방암에서 palbociclib + letrozole 접근 연구 |
| [NCT01740427](https://clinicaltrials.gov/study/NCT01740427) | Phase 3 | 완료 | 666 | 1차 치료로 palbociclib + letrozole vs 위약 + letrozole (PALOMA-2) |
| [NCT00382070](https://clinicaltrials.gov/study/NCT00382070) | Phase 3 | 불명 | 3,966 | 5년 호르몬 치료 완료 후 letrozole 5년 vs 위약, 무병생존 기간 비교 |
| [NCT00908531](https://clinicaltrials.gov/study/NCT00908531) | Phase 3 | 조기 종료 | 123 | 수술 전 letrozole 4개월 vs 수술 우선 (DBCG) |
| [NCT03425838](https://clinicaltrials.gov/study/NCT03425838) | Phase 3 | 진행 중(모집 종료) | 1,050 | 아로마타제 억제제 + CDK4/6 억제제의 1차 vs 2차 투여 순서 (SONIA) |
| [NCT04272801](https://clinicaltrials.gov/study/NCT04272801) | Phase 2 | 진행 중(모집 종료) | 84 | 고령 여성 조기 유방암에서 수술 전 내분비 치료 |
| [NCT00728949](https://clinicaltrials.gov/study/NCT00728949) | Phase 2 | 완료 | 93 | 항에스트로겐 치료 후 진행한 환자에서 IMC-A12 단독 또는 병용 |
| [NCT01439711](https://clinicaltrials.gov/study/NCT01439711) | Phase 2 | 완료 | 108 | 에스트로겐 수용체 양성 DCIS에서 수술 전 letrozole |
| [NCT02344550](https://clinicaltrials.gov/study/NCT02344550) | Phase 2 | 완료 | 137 | 폐경 전 전이성 유방암에서 난소 억제 + letrozole + everolimus |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [35263519](https://pubmed.ncbi.nlm.nih.gov/35263519/) | 2022 | RCT | N Engl J Med | 진행성 유방암에서 ribociclib + letrozole의 전체 생존율 개선 여부 보고 |
| [29718092](https://pubmed.ncbi.nlm.nih.gov/29718092/) | 2018 | RCT | Ann Oncol | MONALEESA-2: 1차 ribociclib + letrozole의 무진행 생존 연장 및 관리 가능한 독성 |
| [30632023](https://pubmed.ncbi.nlm.nih.gov/30632023/) | 2019 | 코호트 | Breast Cancer Res Treat | PALOMA-2 장기 추적: palbociclib + letrozole의 무진행 생존 연장 (HR 0.58) |
| [36243120](https://pubmed.ncbi.nlm.nih.gov/36243120/) | 2022 | 리뷰 | Life Sci | Letrozole의 약리, 독성 및 잠재적 치료 효과 정리 |
| [20095792](https://pubmed.ncbi.nlm.nih.gov/20095792/) | 2010 | 리뷰 | Expert Opin Drug Metab Toxicol | 3세대 아로마타제 억제제 letrozole의 약력학·약동학·효능·안전성 |
| [17912633](https://pubmed.ncbi.nlm.nih.gov/17912633/) | 2007 | 기타 | Breast Cancer Res Treat | Letrozole의 발견 과정과 작용 기전 |
| [12113048](https://pubmed.ncbi.nlm.nih.gov/12113048/) | 2002 | 리뷰 | Expert Rev Anticancer Ther | 전이성 폐경 후 유방암 1차 치료에서 tamoxifen 대비 우월성 |
| [17544670](https://pubmed.ncbi.nlm.nih.gov/17544670/) | 2007 | 기타 | Breast | MA-17 시험에 근거한 연장 보조 letrozole 처방 |
| [35464999](https://pubmed.ncbi.nlm.nih.gov/35464999/) | 2022 | 기타 | Comput Math Methods Med | Tamoxifen-letrozole 순차 요법 vs letrozole 단독의 효능·안전성·예후 비교 |
| [38492847](https://pubmed.ncbi.nlm.nih.gov/38492847/) | 2024 | 전임상 | J Pharm Sci | Letrozole 전달용 금속-유기 골격체 나노입자 개발 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201500168 | 파누엘정2.5밀리그램 | 어두운 황색의 원형 필름코팅정 | 허가 문서 참조 |
| 202402459 | 레트로보정2.5밀리그램 | 어두운 황색의 원형 필름코팅정 | 허가 문서 참조 |
| 200108765 | 페마라정 | 어두운 황색의 원형 필름코팅정 | 허가 문서 참조 |
| 202403042 | 페트라정 | 어두운 황색의 원형 필름코팅정 | 허가 문서 참조 |
| 201500998 | 테바레트로졸정2.5밀리그램 | 어두운 노란색의 볼록한 원형 필름코팅정 | 허가 문서 참조 |

그 외 신풍제약의 브레트라정(200710810)을 포함해 총 6건이 유효합니다.

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 호르몬 요법 (아로마타제 억제제). 기존 세포독성 화학요법제는 아님 |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 허가사항의 경고 및 주의사항을 참조하세요. 데이터상 금기 연관 질환으로 간·골 관련 항목이 확인되어 간기능과 골밀도 확인을 고려할 수 있습니다 |
| 취급 방호 | 허가사항의 경고 및 주의사항을 참조하세요 |

## 안전성 고려사항

- **지식그래프상 금기 연관 질환** (허가 문서가 아닌 TxGNN 지식그래프의 약물-질환 금기 연결 기준): 간부전, 간경변, 골다공증, 폐경 후 골다공증, 고빌리루빈혈증, 유전성 고빌리루빈혈증, 길버트 증후군, 뇌혈관 질환
- **약물 상호작용**: 총 100건이 조회되었습니다. 이 중 중증도가 확인된 항목은 **aprepitant(중등도)** 입니다. 나머지 항목(calcitriol, glimepiride, lansoprazole, dolasetron, granisetron, famotidine, acetylsalicylic acid, pantoprazole, morphine, metformin 등)은 등급이 명시되지 않았습니다.
- 임상시험 보조 연구에서 아로마타제 억제제 관련 근골격계 증상, 뼈 소실, 내피 기능 변화가 다루어졌고, 증례 보고로 황반병증(황반부종)이 있었습니다.

허가사항상의 공식 경고·금기 정보는 이번 데이터에 포함되어 있지 않으므로, 허가 문서를 반드시 확인해야 합니다.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
여성 유방암(및 에스트로겐 수용체 양성 유방암)에 대해 완료된 Phase 3 임상시험이 여러 건 있고 RCT 문헌도 풍부해 근거 수준은 L1입니다. 다만 이는 이미 확립된 용도에 해당하여 새로운 재창출 가치는 제한적이며, 안전성 관련 허가사항 데이터가 비어 있어 안전성 검토 전에는 최종 결정이 어렵습니다.

**진행하려면 필요한 것:**
- 한국 허가 문서(MFDS) 원문에서 경고·금기·적응증 확인 (현재 차단 수준의 데이터 공백)
- 작용 기전(MOA) 데이터 보완 (DrugBank 조회)
- 간·골 관련 금기 연관 질환 보유 환자에 대한 모니터링 계획
- 새로운 가치를 찾는다면 하위 예측 중 근거가 있는 후보 검토: 호르몬 저항성 유방암(Phase 2 병용 시험 중심, 연구 질문 단계), 양측성 유방암(간접 근거, Proceed with Guardrails)
- 근거가 부족한 후보(유두암, 에를리히 종양, 유방 섬유낭성 질환, 양성 유선 이형성증)는 보류(Hold) 권장
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

