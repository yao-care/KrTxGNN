---
layout: default
title: Methylene Blue
parent: 모델 예측만 (L5)
nav_order: 510
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-31
description: "Methylene Blue: 예측 신규 적응증 기관지염 (Bronchitis) (근거 수준 L5). 기존 적응증: 허가 적응증 본문이 확인되지 않음 (허가 정보가 문서 링크로만 제공됨)"
monitor_inn: "METHYLENE BLUE"
predicted_indications: ["bronchitis"]
---

# Methylene Blue
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

## Methylene Blue: 기존 적응증에서 기관지염으로
{: .text-alpha }

## 한 문장 요약

Methylene blue(메틸렌블루)는 국내에서 주사제(프로베블루주 0.5%)로 허가·시판 중인 약물입니다. TxGNN 모델은 **기관지염(bronchitis)**에 효과가 있을 수 있다고 예측하지만, 현재 임상시험은 **0건**이며 문헌 8편은 모두 치료 근거와 무관합니다. 따라서 이 예측은 모델 점수에만 의존하고 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문이 확인되지 않음 (허가 정보가 문서 링크로만 제공됨) |
| 예측 신규 적응증 | 기관지염 (Bronchitis) |
| TxGNN 예측 점수 | 0.9997 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 1건 / 전체 1건) |
| 허가증 수 | 1건 (유효 1건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 이론적으로 methylene blue는 일산화질소 합성효소와 구아닐산 고리화효소를 억제하는 것으로 알려져 있어 기도 염증과 평활근 긴장도에 영향을 줄 가능성이 있습니다. 다만 이는 추측 수준입니다.

검색된 문헌에서 methylene blue는 기관지 내시경 검사의 진단용 염색제로만 등장합니다. 기관지염 치료 효과를 시사하는 자료는 없습니다. 이 예측(점수 0.9997)은 치료 근거보다는 TxGNN 모델(딥러닝)이 관련 질환 사이에서 학습한 유사성을 반영했을 가능성이 크며, 생물학적 근거는 아닙니다.

참고로 같은 약물의 예측 목록에는 메트헤모글로빈혈증(알파형 및 메트헤모글로빈 환원효소 결핍형)도 있습니다. 이쪽은 기전적 타당성이 높지만, 기관지염과는 별개의 예측입니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

검색된 문헌은 모두 기관지염 치료와 직접 관련이 없습니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [9387672](https://pubmed.ncbi.nlm.nih.gov/9387672/) | 1996 | 진단 염색 연구 | Zhonghua Wai Ke Za Zhi | 기관지 내시경에서 methylene blue 염색으로 중심형 폐암 진단 (염색 양성률 97.14%, 기관지염 8.33%) |
| [7313968](https://pubmed.ncbi.nlm.nih.gov/7313968/) | 1981 | 진단 염색 연구 | Terapevticheskii Arkhiv | 위장관·기관지 종양의 양성/악성 감별을 위한 methylene blue 색소내시경 |
| [8420409](https://pubmed.ncbi.nlm.nih.gov/8420409/) | 1993 | 방법론 연구 | Am Rev Respir Dis | 기관지폐포세척액 내 폐포 체액량 정량을 위한 표지자 중 하나로 methylene blue 사용 |
| [6121761](https://pubmed.ncbi.nlm.nih.gov/6121761/) | 1982 | 전임상 약리 | Int J Clin Pharmacol Ther Toxicol | 새로운 베타차단제 연구에서 순환시간 측정에 methylene blue 사용 |
| [31419501](https://pubmed.ncbi.nlm.nih.gov/31419501/) | 2020 | 전임상 (동물 조직) | J Ethnopharmacol | Lippia alnifolia 정유의 기니피그 기관 이완 효과 (methylene blue와 무관) |
| [21767626](https://pubmed.ncbi.nlm.nih.gov/21767626/) | 2011 | 전임상 (동물) | J Ethnopharmacol | Aloysia gratissima의 항우울·신경보호 효과 (기관지염은 전통 용도로만 언급) |
| [29254574](https://pubmed.ncbi.nlm.nih.gov/29254574/) | 2018 | 분석/센서 방법 | Anal Chim Acta | 테오필린 검출용 전기화학 앱타센서 |
| [20084922](https://pubmed.ncbi.nlm.nih.gov/20084922/) | 2009 | 증례 보고 | Mikrobiyol Bul | 면역능이 정상인 환자의 Moraxella catarrhalis 심내막염 1례 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201708376 | 프로베블루주0.5%(메틸렌블루) | 짙은 청색의 액이 무색투명한 유리앰플에 든 주사제 | 허가 적응증 본문 확인 불가 (허가사항 참조) |

## 안전성 고려사항

- **금기 가능 질환 (지식 그래프 기반)**: 허가사항 본문이 아니라 TxGNN 지식 그래프의 약물-질환 금기 연결에서 추출한 정보입니다. 주요 항목은 다음과 같습니다.
  - G6PD 결핍 (용혈 위험)
  - 간질환·간부전, 신장질환
  - 울혈성 심부전, 관상동맥질환, 고혈압, 심장 전도장애, 심정지
  - 당뇨병, 당뇨병성 케톤산증
  - 혈액응고장애, 혈우병, 빈혈
  - 중증근무력증 등 신경근접합부 질환
- **약물 상호작용**: 총 100건이 확인되었고, 아래는 일부입니다. 세로토닌 증후군과 관련된 약물이 다수 포함됩니다.
  - **Major**: Bupropion, Morphine, Ondansetron, Granisetron, Palonosetron, Dolasetron, Phentermine, Fenfluramine, Dexfenfluramine, Lorcaserin, Mazindol, Diethylpropion, Ephedrine, Isometheptene, Opium
  - **Moderate**: Epinephrine (전신·안과·국소), Ephedrine (비강)

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 점수는 매우 높지만(0.9997) 임상시험이 없고, 검색된 문헌에도 기관지염 치료 효과를 뒷받침하는 자료가 없습니다. 근거 수준은 L5이며, 안전성 측면에서도 금기 가능 질환과 Major 상호작용이 많습니다.

**진행하려면 필요한 것:**
- 허가사항(MFDS 첨부문서)의 적응증, 경고, 금기 확인
- 작용 기전(MOA) 데이터 확보 및 기관지염과의 기전적 연관성 검토
- 기관지염에 대한 전임상 또는 임상 근거 확보 (기도 염증·평활근 모델 등)
- 투여 경로 적합성 검토 (현재 국내 제형은 주사제만 있음)
- 참고: 메트헤모글로빈혈증 관련 예측은 기전적 타당성이 높아 별도 검토할 가치가 있습니다. 다만 알파형(M-헤모글로빈 변이)은 반응이 불량할 수 있고, 환원효소 결핍형은 이미 표준 진료에서 다뤄지고 있어 재창출 가치는 제한적입니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

