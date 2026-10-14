---
layout: default
title: Sulindac
parent: 모델 예측만 (L5)
nav_order: 708
evidence_level: L5
indication_count: 10
---

# Sulindac
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

# Sulindac: 관절염 계열 질환에서 골관절염 예측으로

## 한 문장 요약

Sulindac은 비스테로이드성 소염진통제(NSAID)로, 한국에서 단일제(크리돌정 100mg)로 허가·시판되고 있습니다. TxGNN 모델은 **골관절염 감수성(osteoarthritis susceptibility)**에 효과가 있을 것으로 가장 높게 예측했지만, 이 항목은 임상시험과 문헌이 모두 없는 예측 단독 결과입니다. 실제 문헌 근거가 있는 항목은 **골관절염**(문헌 20편, 임상시험 0건)과 **류마티스 관절염**(문헌 18편, 임상시험 0건)이며, 이 둘은 기존 적응증과 겹칠 가능성이 높아 진정한 재창출로 보기 어렵습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 원문이 링크 형태로만 제공되어 구체적인 내용을 확인할 수 없음 |
| 예측 신규 적응증 | 골관절염 감수성 (Osteoarthritis Susceptibility) |
| TxGNN 예측 점수 | 99.98% |
| 근거 수준 | L5 (참고: 골관절염 L3, 류마티스 관절염 L3) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

> 1순위 예측인 골관절염 감수성은 치료 가능한 임상 질환이라기보다 유전적 감수성 개념입니다. 따라서 임상적으로 의미 있는 후보는 2순위(골관절염)와 3순위(류마티스 관절염)이며, 아래 근거 섹션은 2순위 골관절염을 중심으로 정리했습니다.

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Sulindac은 NSAID 계열이며, 활성 대사체(sulfide)가 COX(사이클로옥시게나제)를 억제해 프로스타글란딘 매개 염증과 통증을 줄입니다. 이 기전은 골관절염의 증상 완화와 일치합니다.

1980년대의 무작위 비교 연구들에서 Sulindac은 ibuprofen, naproxen, flurbiprofen과 비슷한 효능을 보였습니다. 다만 골관절염과 류마티스 관절염은 이미 Sulindac의 허가 범위에 포함되어 있을 가능성이 높아, 새로운 적응증 발굴이라기보다 기존 사용을 재확인하는 성격입니다. 허가 적응증 원문을 확인하지 못했으므로 이 점은 검증이 필요합니다.

그 외 상위 예측(말단중간이형성증 Hunter-Thompson형, 단지증-법랑질형성부전 증후군, 단지증, 근경화증, 가성연골무형성증, 단지증-합지증 증후군)은 유전성 골격·근육 질환입니다. COX 억제가 이들의 근본 원인을 교정할 기전은 없으며, 점수는 지식그래프상 관절·뼈 용어와의 근접성을 반영한 것으로 보입니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

골관절염(2순위) 관련 문헌 중 Sulindac을 직접 다룬 주요 연구입니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [3515919](https://pubmed.ncbi.nlm.nih.gov/3515919/) | 1986 | RCT | Am J Med | 고관절·슬관절 골관절염 143명에서 flurbiprofen과 Sulindac 이중맹검 비교(6주) |
| [7261665](https://pubmed.ncbi.nlm.nih.gov/7261665/) | 1981 | RCT | Curr Med Res Opin | 고령 골관절염 32명에서 Sulindac 대 ibuprofen 12주 비교(공개 시험) |
| [7105794](https://pubmed.ncbi.nlm.nih.gov/7105794/) | 1982 | RCT | Curr Med Res Opin | 고령 증상성 골관절염에서 Sulindac과 ibuprofen 비교 |
| [7025178](https://pubmed.ncbi.nlm.nih.gov/7025178/) | 1981 | RCT | Rheumatol Rehabil | 고관절·슬관절 골관절염 30명 교차 시험에서 naproxen과 Sulindac 모두 개선, 유의한 차이 없음 |
| [10321419](https://pubmed.ncbi.nlm.nih.gov/10321419/) | 1999 | RCT | Clin Ther | 골관절염 여성 12명에서 nabumetone·Sulindac·위약의 신장 혈역학 효과 비교 |
| [7044801](https://pubmed.ncbi.nlm.nih.gov/7044801/) | 1982 | RCT | Eur J Rheumatol Inflamm | 류마티스 관절염·골관절염에서 benoxaprofen과 Sulindac 이중맹검 교차 비교 |
| [6839797](https://pubmed.ncbi.nlm.nih.gov/6839797/) | 1983 | 비교 연구 | Curr Med Res Opin | 고령 골관절염 30명에서 Sulindac 대 ibuprofen 비교 |
| [7105795](https://pubmed.ncbi.nlm.nih.gov/7105795/) | 1982 | 다기관 공개 연구 | Curr Med Res Opin | 고령 외래 환자 239명에서 Sulindac과 ibuprofen, naproxen, diclofenac 비교 |
| [35039952](https://pubmed.ncbi.nlm.nih.gov/35039952/) | 2022 | 임상 연구 | Breast Cancer Res Treat | 아로마타제 억제제 복용 유방암 환자의 근골격계 증상(경직)과 삶의 질 개선 (다른 모집단) |
| [3886353](https://pubmed.ncbi.nlm.nih.gov/3886353/) | 1985 | Review | Drugs | tiaprofenic acid 리뷰, 골관절염 치료에서 Sulindac 등과 효능 유사 |

류마티스 관절염(3순위)에서도 indomethacin, oxaprozin, flurbiprofen, mefenamic acid, ibuprofen 등과의 이중맹검 비교 시험(예: PMID 7013055, 6340971, 373989, 377154)이 있으며, 증상 개선 효능은 비슷하다고 보고되었습니다. 다만 모두 오래된 연구이고 표본이 작으며 질병 경과 조절 근거는 아닙니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 197900123 | 크리돌정100밀리그람(설린닥) | 진한 황색의 육각형 필름 코팅정 | 허가사항 원문(식약처 의약품안전나라) 참조 |

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 조회되었으며, 이 중 일부 주요 항목은 다음과 같습니다.
  - 중등도: acetylsalicylic acid, 코르티코스테로이드(hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), metformin, 설폰요소제(glimepiride, chlorpropamide), mesalazine, balsalazide, 칼륨 제제(potassium citrate, potassium bicarbonate), 장 세척·완하제(picosulfuric acid, polyethylene glycol, sodium sulfate)
  - 경미: famotidine, ranitidine, cimetidine, linaclotide
- **문헌에서 확인된 안전성 이슈**: Sulindac 유발 아나필락시스 증례, 무과립구증 보고, 교원성 대장염 증례, 신기능 저하 환자나 cyclosporine 병용 시 신장 기능에 미치는 영향.

허가사항상 경고·금기 정보는 확인되지 않았으므로 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
점수가 가장 높은 예측(골관절염 감수성)과 유전성 골격 질환 예측들은 임상시험과 문헌이 없고 기전도 맞지 않아 지식그래프 연관에 따른 결과로 보입니다. 골관절염과 류마티스 관절염은 문헌 근거(L3)가 있으나 대부분 1980년대 비교 연구이고, 이미 허가 범위일 가능성이 높아 신규 재창출 후보로 보기 어렵습니다.

**진행하려면 필요한 것:**
- 허가 적응증 및 경고·금기 원문 확보 (식약처 허가사항 PDF 내용 확인), 골관절염·류마티스 관절염이 기허가 적응증인지 확정
- 작용 기전(MOA) 데이터 보완
- 허가 범위 밖의 후보를 찾는다면 구체적인 질환 단위(예: 특정 관절병증 아형)로 재정의
- 신장 기능 저하 환자, 고령자, 병용 약물(특히 NSAID·코르티코스테로이드·cyclosporine)에 대한 안전성 평가
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

