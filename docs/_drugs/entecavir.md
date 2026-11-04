---
layout: default
title: Entecavir
parent: 모델 예측만 (L5)
nav_order: 311
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-04
monitor_inn: "ENTECAVIR"
predicted_indications: ["chronic hepatitis C virus infection", "HIV infectious disease", "hepatitis C virus infection", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "hepatitis, viral, animal", "hepatitis E virus infection", "hepatitis A virus infection"]
description: "Entecavir: 예측 신규 적응증 만성 C형 간염 바이러스 감염 (chronic hepatitis C virus infection) (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201404379/EE"
---

# Entecavir
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

## Entecavir: 만성 C형 간염 바이러스 감염 (chronic hepatitis C virus infection)
{: .text-alpha }

## 한 문장 요약

Entecavir는 구아노신 뉴클레오시드 유사체로, B형 간염 바이러스(HBV) 중합효소를 억제하는 약물입니다.
TxGNN 모델은 **만성 C형 간염 바이러스 감염(chronic hepatitis C virus infection)**에 효과가 있을 수 있다고 예측했습니다(예측 점수 0.9998).
다만 수집된 **2건의 임상시험**과 **20편의 문헌**은 모두 HCV 치료 중 HBV 재활성화 예방 등 HBV 관리를 다루며, C형 간염 자체의 치료 효과를 직접 검증한 연구는 없어 근거 수준은 **L5**입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201404379/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201501535/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201403512/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201206904/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201405425/EE;  |
| 예측 신규 적응증 | 만성 C형 간염 바이러스 감염 (chronic hepatitis C virus infection) |
| TxGNN 예측 점수 | 0.9998 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 20건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 수집된 자료에는 상세한 작용 기전(MOA) 데이터가 없습니다. 알려진 정보에 따르면 entecavir는 구아노신 뉴클레오시드 유사체로, HBV 중합효소를 억제합니다.

HCV는 NS5B 중합효소로 복제하는 RNA 바이러스입니다. Entecavir는 이 효소에 직접적인 항바이러스 활성이 없어, C형 간염 자체를 치료할 기전적 근거는 약합니다.

유일하게 생각할 수 있는 연결고리는 간접적입니다. HCV/HBV 공동감염 환자가 직접작용 항바이러스제(DAA)로 HCV를 제거하면 HBV가 재활성화될 수 있고, entecavir는 이때 HBV를 억제합니다. 이는 공동감염 환자의 HBV 관리이지 C형 간염 치료가 아닙니다. 모델의 높은 점수는 간염이라는 질환 용어의 중복과 약물 계열 유사성을 반영했을 가능성이 큽니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | 완료 | 23 | HCV/HBV 공동감염 환자에서 항HCV 직접작용 항바이러스제 투여 중 HBV 재활성화의 발생률과 위험인자를 평가. HBV 위험 관리에 관한 연구이며 entecavir의 HCV 효과를 보는 시험은 아님 |
| [NCT04405011](https://clinicaltrials.gov/study/NCT04405011) | 해당 없음 | 불명 | 60 | DAA 치료를 받는 HCV/HBV 공동감염 환자에서 뉴클레오시드(티드) 유사체 예방 투여가 HBV 재활성화를 막는지, 12주와 24주 투여를 비교. 평가변수는 HBV 재활성화 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [34864158](https://pubmed.ncbi.nlm.nih.gov/34864158/) | 2022 | 무작위 시험 | Clin Gastroenterol Hepatol | HCV/HBV 이중감염에서 DAA 치료 중 entecavir가 HBV 재활성화를 예방하는지 평가. HBV 재활성화 예방이 목적 |
| [24773464](https://pubmed.ncbi.nlm.nih.gov/24773464/) | 2014 | Review | Expert Opin Pharmacother | HBV/HCV 공동감염의 치료 발전을 정리. 공동감염은 간경변·간세포암 위험이 높아 효과적 치료가 필요 |
| [35327336](https://pubmed.ncbi.nlm.nih.gov/35327336/) | 2022 | Review | Biomedicines | 만성 바이러스성 간염(B·C·D형)의 치료를 개관. B형은 뉴클레오시드/뉴클레오티드 유사체 장기 억제 치료가 질병 경과를 크게 바꿈 |
| [36146665](https://pubmed.ncbi.nlm.nih.gov/36146665/) | 2022 | 코호트 | Viruses | 항HCV 항체 양성 만성 B형 간염 환자 66명에서 항HBV 뉴클레오시드 유사체 치료 후 HCV 재활성화 여부를 추적 |
| [35108715](https://pubmed.ncbi.nlm.nih.gov/35108715/) | 2022 | 관찰 연구 | Dig Dis | HCV 치료용 DAA를 받은 환자에서 HBV 재활성화의 발생률과 임상 경과를 평가 |
| [28230928](https://pubmed.ncbi.nlm.nih.gov/28230928/) | 2017 | 관찰 연구 | J Gastroenterol Hepatol | DAA로 치료한 HCV 환자에서 HBV 재활성화 위험을 조사 |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | 문헌 개관 | Minerva Gastroenterol Dietol | B형·C형 간염 항바이러스제의 신장 기능 영향을 개관 |
| [24868325](https://pubmed.ncbi.nlm.nih.gov/24868325/) | 2014 | 문헌 개관 | World J Hepatol | 간·신장 이식 전후 B형·C형 간염 환자 관리를 다룸. entecavir는 HBV 재발 예방에 쓰이며 신기능에 따라 용량 조절이 필요 |
| [32173307](https://pubmed.ncbi.nlm.nih.gov/32173307/) | 2020 | 문헌 개관 | Clin Res Hepatol Gastroenterol | 소아 B형·C형 간염의 현재와 향후 관리를 다룸 |
| [18221137](https://pubmed.ncbi.nlm.nih.gov/18221137/) | 2006 | Review | Recent Pat Anti-Infect Drug Discov | 만성 B형 간염에서 페그인터페론과 다른 항바이러스제를 비교 |

## 한국 시판 정보

한국에는 entecavir 단일제 허가증이 **20건**(유효 20건, 취소 0건) 있습니다. 허가 적응증은 각 허가증 원문 링크에서 확인할 수 있습니다. 아래는 주요 5건입니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200605263 | 바라크루드정1.0밀리그램 (한국비엠에스제약) | 필름코팅정 | 허가 문서 링크로만 제공됨 |
| 201206804 | 카비어정1밀리그램 (한미약품) | 필름코팅정 | 허가 문서 링크로만 제공됨 |
| 201208629 | 엔테카벨정1밀리그램 (종근당) | 필름코팅정 | 허가 문서 링크로만 제공됨 |
| 201501657 | 엔테카벨구강붕해정1밀리그램 (종근당) | 구강붕해정 | 허가 문서 링크로만 제공됨 |
| 201403953 | 바카비정0.5밀리그램 (삼진제약) | 필름코팅정 | 허가 문서 링크로만 제공됨 |

## 안전성 고려사항

경고·금기 정보는 이번 자료에 확보되지 않았으므로 허가사항을 참조하세요.

**약물 상호작용**: 총 44건이 확인되었고, 아래는 모두 중등도 수준입니다(일부만 표시).
- 신독성 가능성이 있는 약물: Amphotericin B(지질복합체·리포좀·콜레스테릴황산염 제형 포함), Vancomycin, Kanamycin, Neomycin, Polymyxin B
- 위산 억제제: Famotidine, Ranitidine, Cimetidine
- 기타: Metformin, Amoxicillin, Levofloxacin, Orlistat, Mesalazine, Balsalazide, Olsalazine, Sulfasalazine

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- Entecavir는 HCV에 직접적인 항바이러스 기전이 없고, 수집된 시험과 문헌은 모두 공동감염 환자의 HBV 재활성화 예방을 다룹니다. C형 간염 치료 효과를 직접 검증한 연구가 없어 근거 수준은 L5이며, 모델의 높은 점수만으로 진행하기는 어렵습니다.

**진행하려면 필요한 것:**
- HCV 자체에 대한 entecavir의 항바이러스 활성을 보여주는 전임상 또는 임상 자료
- 상세한 작용 기전(MOA) 데이터 확보
- 허가사항의 경고·금기 정보 확인
- 공동감염 환자의 HBV 재활성화 예방은 C형 간염 치료와 별개의 질문으로, 필요하면 따로 평가

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

