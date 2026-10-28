---
layout: default
title: Pirfenidone
parent: 모델 예측만 (L5)
nav_order: 605
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Pirfenidone: 예측 신규 적응증 외피 외 비만세포종 (extracutaneous mastocytoma) (근거 수준 L5). 기존 적응증: 허가 적응증 본문 확인 불가 (허가증 문서 링크만 제공됨)"
monitor_inn: "Pirfenidone"
predicted_indications: ["extracutaneous mastocytoma", "dermatofibrosarcoma protuberans", "aggressive systemic mastocytosis", "heart fibrosarcoma", "conventional fibrosarcoma", "autosomal recessive familial Mediterranean fever", "kidney fibrosarcoma", "hepatic infarction", "fibroblastic neoplasm", "low grade fibromyxoid sarcoma"]
---

# Pirfenidone
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

## Pirfenidone: 허가 적응증 정보 미확인에서 외피 외 비만세포종으로
{: .text-alpha }

## 한 문장 요약

Pirfenidone은 한국에서 단일제로 9건이 허가되어 시판 중인 항섬유화 약물입니다. 다만 이번 보고서에 사용된 데이터에는 허가 적응증 본문이 없고 허가증 문서 링크만 있어 기존 적응증을 확인할 수 없었습니다.
TxGNN 모델은 **외피 외 비만세포종(extracutaneous mastocytoma)**에 효과가 있을 수 있다고 예측하지만, 이를 지지하는 **임상시험은 0건, 문헌도 0건**으로 모델 예측 단계(L5)에 머물러 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문 확인 불가 (허가증 문서 링크만 제공됨) |
| 예측 신규 적응증 | 외피 외 비만세포종 (extracutaneous mastocytoma) |
| TxGNN 예측 점수 | 0.9971 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 9건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Pirfenidone은 항섬유화·항염증 작용을 가진 약물로, TGF-β와 TNF-α 신호를 조절하는 것으로 알려져 있습니다. 다만 이번 데이터만으로는 이 기전이 비만세포종에 적용된다는 근거를 확인할 수 없습니다.

골외 비만세포종과의 직접적인 기전 연결은 데이터로 뒷받침되지 않습니다. 이 점수는 TxGNN 모델(딥러닝)에서 나온 것이며, 모델이 관련 질환 사이에서 학습한 유사성을 반영할 수 있을 뿐 생물학적 근거는 아닙니다.

참고로 상위 10개 예측에는 섬유육종, 피부섬유육종(DFSP), 침습성 전신 비만세포증, 섬유모세포성 신생물 등이 포함되어 있습니다. 이들 대부분은 섬유모세포 증식 억제라는 일반적 논리에 기댄 추정입니다. 침습성 전신 비만세포증은 KIT 변이가 원인인데 Pirfenidone에는 알려진 KIT 억제 활성이 없어 기전적 근거가 약합니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

1순위 예측 질환(외피 외 비만세포종)에 대한 문헌은 없습니다. 아래는 참고용으로, 9순위 예측인 섬유모세포성 신생물에서 확인된 문헌입니다. 모두 간접 근거입니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [12907346](https://pubmed.ncbi.nlm.nih.gov/12907346/) | 2003 | 파일럿 임상 | Am J Gastroenterol | 가족성 선종성 용종증의 desmoid 종양에 대한 효능 평가 파일럿 (제목이 잘려 있어 시험 약물은 확인 불가) |
| [27835939](https://pubmed.ncbi.nlm.nih.gov/27835939/) | 2016 | 시험관 연구 | BMC Musculoskelet Disord | Dupuytren병 유래 섬유모세포에서 TGF-β1 매개 작용 억제 |
| [30927912](https://pubmed.ncbi.nlm.nih.gov/30927912/) | 2019 | 시험관 연구 | BMC Musculoskelet Disord | Dupuytren병 섬유모세포에서 TGF-β1 자극 non-SMAD 신호 경로에 대한 효과 |
| [35129055](https://pubmed.ncbi.nlm.nih.gov/35129055/) | 2022 | 전임상/리뷰 | Pharm Dev Technol | Dupuytren병에 대한 주사형 항섬유화제 가능성 |
| [29702057](https://pubmed.ncbi.nlm.nih.gov/29702057/) | 2018 | 증례 보고 | Perm J | Pirfenidone 사용 후 미분화 다형성 육종 발생 (안전성 신호 가능) |
| [32572469](https://pubmed.ncbi.nlm.nih.gov/32572469/) | 2020 | 증례 보고 | Rheumatology (Oxford) | 전신 경화증 환자에서 mycophenolate mofetil과 pirfenidone 사용 중 다발성 피부섬유종 악화 (안전성 신호 가능) |

## 한국 시판 정보

허가 적응증 본문은 제공되지 않았고 허가증 문서 링크만 확인되었습니다. 적응증은 해당 허가증을 참조하세요.

| 허가번호 | 제품명 | 제형 | 제조사 |
|---------|------|------|--------|
| 202200358 | 유니페니돈정200밀리그램 | 필름코팅정 | 한국유니온제약 |
| 201804024 | 피레스코정600밀리그램 | 필름코팅정 | 코오롱제약 |
| 201703971 | 파이브로정200밀리그램 | 필름코팅정 | 영진약품 |
| 202200359 | 유니페니돈정400밀리그램 | 필름코팅정 | 한국유니온제약 |
| 201803148 | 파이브로정600밀리그램 | 필름코팅정 | 영진약품 |

이 밖에 4건(피레스코정200·400밀리그램, 파이브로정400밀리그램, 피레스파정200밀리그램)이 더 허가되어 있어 총 9건이며, 모두 유효한 단일제입니다.

## 안전성 고려사항

- **약물 상호작용**: 데이터에서 총 100건이 확인되었으며, 이 중 상위 20건은 모두 중등도(Moderate)입니다. 주요 항목은 다음과 같습니다.
  - 위산 억제제: Omeprazole, Lansoprazole, Esomeprazole, Cimetidine
  - 항우울·중독 치료제: Bupropion, Naltrexone, Disulfiram
  - 항진균·항말라리아·구충제: Miconazole, Lumefantrine, Primaquine, Thiabendazole
  - 기타: Eliglustat, Obeticholic acid, Oxandrolone, Nitisinone, Glycerol phenylbutyrate, Rolapitant, Deferasirox, Ticlopidine, Ivacaftor
- **문헌상 안전성 신호**: 미분화 다형성 육종 증례와 피부섬유종 악화 증례가 보고되어 있습니다. 모두 증례 수준이며 인과관계는 확립되지 않았습니다.
- **간독성**: 10순위 내 간경색 예측 항목의 근거 설명에 Pirfenidone의 간독성 경고가 언급되어 있습니다.

허가사항의 경고 및 금기 정보는 이번 데이터에 포함되지 않았으므로 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
외피 외 비만세포종에 대한 임상시험과 문헌이 없고 근거는 모델 예측뿐(L5)입니다. 작용 기전 데이터와 허가 경고·금기 정보도 확보되지 않아, 현재 데이터로는 재창출 타당성을 판단할 수 없습니다.

**진행하려면 필요한 것:**
- MFDS 허가증(첨부문서)에서 허가 적응증, 경고, 금기 정보 확보 (현재 안전성 검토 진행을 막는 항목)
- DrugBank 등에서 작용 기전(MOA) 데이터 확보
- 비만세포 및 비만세포종과 Pirfenidone의 관련성을 다루는 전임상·임상 문헌 탐색
- 섬유모세포성 종양 계열 예측에서 확인된 육종 및 피부섬유종 관련 안전성 신호 검토
- 예측 순위 전반에서 기전적 근거와 안전성 측면이 더 유리한 후보 질환 재검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

