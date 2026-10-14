---
layout: default
title: Sulfasalazine
parent: 모델 예측만 (L5)
nav_order: 707
evidence_level: L5
indication_count: 10
---

# Sulfasalazine
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

# Sulfasalazine: 염증성 질환에서 골관절염으로

## 한 문장 요약

Sulfasalazine은 한국에서 장용정 형태로 허가·시판 중인 단일 성분 약물입니다. TxGNN 모델은 상위 예측 10건을 제시했지만, 실제로 문헌 근거가 있는 것은 **골관절염(osteoarthritis)**과 **척추관절병증 감수성(spondyloarthropathy, susceptibility to)** 두 가지뿐입니다. 임상시험은 한 건도 없고, 골관절염 관련 문헌은 대부분 전임상 연구이거나 주제와 거리가 있습니다.

> 이 보고서는 예측 순위 1위(brachydactyly-syndactyly syndrome)가 아니라, 근거가 가장 풍부한 5위 예측인 **골관절염**을 중심으로 작성했습니다. 1위는 TxGNN 점수가 매우 높지만 기전적 연관성이 확인되지 않았고 근거도 전혀 없습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문이 링크로만 제공되어 확인할 수 없음 (허가사항 PDF 참조) |
| 예측 신규 적응증 | 골관절염 (Osteoarthritis) — 예측 순위 5위 |
| TxGNN 예측 점수 | 99.64% |
| 근거 수준 | L4 (전임상·기전 연구만 있음) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 5건 (모두 유효, 단일제) |
| 권장 결정 | Hold (추가 연구 질문으로 분류) |

**참고: 상위 10개 예측 요약**

| 순위 | 예측 질환 | 점수 | 근거 수준 |
|-----|---------|------|---------|
| 1 | Brachydactyly-syndactyly syndrome | 99.94% | L5 |
| 2 | Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99.94% | L5 |
| 3 | Osteoarthritis susceptibility | 99.88% | L5 |
| 4 | Congenital hypotrichosis with juvenile macular dystrophy | 99.66% | L5 |
| 5 | **Osteoarthritis** | 99.64% | L4 |
| 6 | WHIM syndrome | 99.62% | L5 |
| 7 | Acromesomelic dysplasia, Hunter-Thompson type | 99.61% | L5 |
| 8 | Spondyloarthropathy, susceptibility to | 99.53% | L4 |
| 9 | Brachyolmia-amelogenesis imperfecta syndrome | 99.49% | L5 |
| 10 | Myosclerosis | 99.43% | L5 |

희귀 유전 질환 위주인 L5 항목(1, 2, 4, 6, 7, 9, 10위)은 기전적 연관성이 없고 연구도 없어 모두 Hold입니다. 3위는 유전적 감수성 항목으로, 골관절염 항목과의 그래프상 근접성에서 나온 산물로 보입니다.

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 sulfasalazine은 항염증·면역조절 작용을 가진 약물로, NF-κB 억제와 xCT(SLC7A11) 시스템 억제가 제안되어 있습니다.

골관절염은 염증과 연골 분해가 병태에 관여하는 질환이어서 기전상 접근 가능성이 있습니다. 전임상 연구에서 sulfasalazine은 다음과 같은 효과를 보였습니다.
- 사이토카인으로 자극한 연골에서 프로테오글리칸·콜라겐 방출을 차단하고 금속단백분해효소를 하향 조절 (PMID 19690126)
- 쥐 골관절염 모델에서 염증과 연골 분해를 완화 (히알루론산 결합 제형, PMID 29548914)
- 전방십자인대 절단·반월상연골 절제 모델에서 cystine/glutamate 역수송체 억제를 통해 연골 파괴를 감소 (PMID 26466556)

다만 이는 모두 전임상 또는 간접 근거입니다. 사람 대상 임상시험 근거가 없어 효능을 확인할 수 없습니다.

한편 척추관절병증(8위)은 sulfasalazine이 말초 관절염과 IBD 연관 관절병증에 DMARD로 쓰여 온 질환군이어서 생물학적으로 타당한 연결이 있습니다. 다만 "감수성" 항목은 임상 질환이 아니므로 강직성 척추염, 반응성 관절염, 건선관절염 등 실제 임상 질환에 대응시켜 별도로 근거를 확인해야 합니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

골관절염 예측과 관련된 문헌 중 sulfasalazine과 직접 관련된 주요 연구입니다. 나머지 문헌은 주제와 거리가 있어 제외했습니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [29548914](https://pubmed.ncbi.nlm.nih.gov/29548914/) | 2018 | 전임상 (동물) | Int J Biol Macromol | Sulfasalazine 함유 히알루론산이 60일간 지속 방출되며 쥐 골관절염 모델에서 염증·연골 분해 완화 |
| [26466556](https://pubmed.ncbi.nlm.nih.gov/26466556/) | 2016 | 전임상 (동물) | J Orthop Res | Cystine/glutamate 역수송체 억제로 연골 파괴 감소 |
| [19690126](https://pubmed.ncbi.nlm.nih.gov/19690126/) | 2009 | 전임상 (in vitro) | Rheumatology (Oxford) | 사이토카인 자극 연골에서 프로테오글리칸·콜라겐 방출 차단, 금속단백분해효소 하향 조절 |
| [24329131](https://pubmed.ncbi.nlm.nih.gov/24329131/) | 2014 | 전임상 (in vitro) | Mod Rheumatol | Sulfasalazine과 tofacitinib이 관절 연골세포의 단백질 프로필에 미치는 영향 |
| [1673814](https://pubmed.ncbi.nlm.nih.gov/1673814/) | 1991 | 전임상 (in vitro) | Wien Klin Wochenschr | Sulfasalazine 및 대사체가 사람 활막 조직의 프로스타글란딘·류코트리엔 방출에 미치는 영향 |
| [35958605](https://pubmed.ncbi.nlm.nih.gov/35958605/) | 2022 | 리뷰 | Front Immunol | 염증성 관절염에서 ferroptosis의 역할 (일반 리뷰) |

**척추관절병증 관련 참고 문헌 (8위 예측)**

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [15922688](https://pubmed.ncbi.nlm.nih.gov/15922688/) | 2005 | 리뷰 | Am J Med | 척추관절염의 병인과 치료 최신 동향 |
| [18166219](https://pubmed.ncbi.nlm.nih.gov/18166219/) | 2008 | 리뷰 | Semin Arthritis Rheum | 척추관절염의 분류, 유전적 감수성, 병리, 치료 반응 |
| [19938189](https://pubmed.ncbi.nlm.nih.gov/19938189/) | 2009 | 리뷰 | World J Gastroenterol | 염증성 장질환의 류마티스 증상 |
| [25413361](https://pubmed.ncbi.nlm.nih.gov/25413361/) | 2014 | 유전적 연관성 연구 | BMC Pharmacol Toxicol | 중국 한족 강직성 척추염 환자의 NAT 다형성과 sulfasalazine 이상반응의 상관성 (효능 근거 아님) |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 199803482 | 조피린장용정(설파살라진) | 황색의 장용성 코팅정제 | 허가사항 PDF 참조 |
| 199806926 | 사피루진이엔정500(설파살라진)(수출용) | 백색의 타원형 장용성 필름코팅정제 | 허가사항 PDF 참조 |
| 200403301 | 아자설판장용정500밀리그램(수출용) | 황색~황갈색 타원형의 장용성 필름코팅정 | 허가사항 PDF 참조 |
| 201209552 | 사조핀정(설파살라진)(수출용) | 주황색 타원형의 장용성 코팅정 | 허가사항 PDF 참조 |
| 201110251 | 아자설판장용정250밀리그램(수출용) | 황색~황갈색 원형의 장용성 필름코팅정 | 허가사항 PDF 참조 |

5건 중 4건은 수출용 허가입니다.

## 안전성 고려사항

허가사항의 경고·금기 정보는 이 보고서에 반영되지 않았으므로 허가사항을 참조하세요.

**지식 그래프 기반 금기 질환 (허가 문서가 아닌 TxGNN 지식 그래프 기준)**
- 혈액 질환: 호중구감소증, 무과립구증, 재생불량성 빈혈, G6PD 결핍
- 대사 질환: 포르피린증(유전성 포함), 글리코겐 저장병, 시스틴뇨증, 갈락토오스혈증
- 장기 질환: 신장 질환, 간 질환, 담낭 질환, 요로 폐쇄, 요관 농양
- 호흡기 질환: 천식(내인성·알레르기성 포함)
- 기타: 느린 아세틸화 대사 유형(slow acetylation)

**약물 상호작용** (총 100건 조회, 일부 표시)
- **주요(Major)**: Prilocaine(국소), 사람 면역글로불린 G(정맥), Methenamine
- **중등도(Moderate)**: Ketorolac, Ibuprofen, Celecoxib 등 NSAID, Acyclovir, Ethinylestradiol, Estradiol, Alpelisib, Amphotericin B, Amikacin, Apalutamide, Azathioprine, Asparaginase, Bacitracin 등
- **경미(Minor)**: Folic acid

골관절염 환자는 NSAID를 병용하는 경우가 많으므로 NSAID와의 상호작용에 유의해야 합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
골관절염 예측은 TxGNN 점수(99.64%)가 높지만 근거는 전임상 연구뿐이며 임상시험이 없습니다(L4). 나머지 상위 예측은 대부분 희귀 유전 질환으로, 기전적 연결이나 근거가 전혀 없습니다. 안전성 데이터(허가사항 경고·금기)도 확보되지 않아 안전성 선별 단계로 진행할 수 없습니다.

**진행하려면 필요한 것:**
- MFDS 허가사항(경고·금기) 확보 및 분석: 안전성 선별의 필수 선행 조건
- DrugBank에서 작용 기전(MOA) 데이터 확보
- 골관절염에 대한 사람 대상 임상 근거 검색 및 평가(체계적 문헌고찰, 임상시험 등록 확인)
- 척추관절병증 "감수성" 항목을 강직성 척추염·반응성 관절염·건선관절염 등 임상 질환으로 매핑하고, 가이드라인 수준 근거를 별도 검증
- 제형(경구 장용정) 측면에서 골관절염 국소 치료 적합성 검토(히알루론산 결합 관절강 내 제형은 전임상 단계)
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

