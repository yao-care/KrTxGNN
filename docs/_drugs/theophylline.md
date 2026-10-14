---
layout: default
title: Theophylline
parent: 모델 예측만 (L5)
nav_order: 732
evidence_level: L5
indication_count: 7
---

# Theophylline
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **7** 건
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

# Theophylline: 기도질환 치료제에서 혈전성 질환으로

## 한 문장 요약

Theophylline은 기관지확장 작용을 하는 크산틴계 약물로, 일반적으로 천식과 만성 폐쇄성 폐질환 같은 기도질환 치료에 사용됩니다. TxGNN 모델은 **혈전성 질환(thrombotic disease)**에 효과가 있을 수 있다고 예측합니다(점수 99.62%). 그러나 이 적응증을 직접 검증한 **임상시험은 0건**이고, 검색된 **문헌 18편**도 혈전 치료에 대한 theophylline의 효과를 시험한 연구가 아닙니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 기도질환(천식·COPD 등, 일반적 용도). 한국 허가 적응증 원문은 링크로만 제공되어 본문을 확인하지 못했습니다. |
| 예측 신규 적응증 | 혈전성 질환 (Thrombotic Disease) |
| TxGNN 예측 점수 | 99.62% |
| 근거 수준 | L5 (모델 예측만 있음) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 2건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 이 보고서용으로 수집된 자료에 없습니다. 알려진 정보에 따르면 theophylline은 비선택적 포스포디에스테라제(PDE) 억제제이자 아데노신 수용체 길항제입니다.

PDE를 억제하면 혈소판 내 cAMP가 올라갑니다. 이론상 혈소판 응집이 줄 수 있어 혈전성 질환과 기전상 연결될 수 있습니다. 다만 이 연결은 약하고 간접적입니다. 기도질환과 혈전성 질환은 임상적 연관성이 크지 않아, 높은 예측 점수는 지식 그래프 기반의 계산적 추정으로 보는 것이 적절합니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

검색된 문헌은 대부분 혈소판 바이오마커, 검체 처리, 분석법에 관한 것입니다. theophylline을 혈전성 질환 치료에 시험한 연구는 없습니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [8055680](https://pubmed.ncbi.nlm.nih.gov/8055680/) | 1994 | Review | Clin Pharmacokinet | 항혈소판제 ticlopidine의 약동학 고찰(theophylline 직접 연구 아님) |
| [6771102](https://pubmed.ncbi.nlm.nih.gov/6771102/) | 1980 | Review | CRC Crit Rev Biochem | 프로스타글란딘, 혈소판, 죽상경화의 관계. 프로스타사이클린이 혈소판 아데닐산 고리화효소를 자극해 응집을 억제함 |
| [8981060](https://pubmed.ncbi.nlm.nih.gov/8981060/) | 1996 | 미분류 | Gen Pharmacol | milrinone과 아데노신이 cAMP를 높여 인체 혈소판 반응을 억제함(기전적 참고, theophylline 아님) |
| [4776567](https://pubmed.ncbi.nlm.nih.gov/4776567/) | 1973 | 미분류 | Minerva Cardioangiol | theophylline 유도체(nicotinate)의 만성 폐쇄성 말초동맥질환 치료 관련 보고(초록 없음) |
| [5136470](https://pubmed.ncbi.nlm.nih.gov/5136470/) | 1971 | 미분류 | Cardiologia Pratica | theophylline 유도체의 뇌·말초 혈관병증 환자 심혈관 효과(초록 없음) |
| [5605983](https://pubmed.ncbi.nlm.nih.gov/5605983/) | 1967 | 미분류 | Ann Ottalmol Clin Ocul | theophylline nicotinate의 망막 혈관질환 효과를 망막전위도로 평가(초록 없음) |
| [6241135](https://pubmed.ncbi.nlm.nih.gov/6241135/) | 1984 | 미분류 | Cor Vasa | 심근경색·혈전정맥염 환자에서 theophylline 저항성 T세포 증가 |
| [19897460](https://pubmed.ncbi.nlm.nih.gov/19897460/) | 2010 | 미분류 | Heart | 관상동맥질환 환자에서 허혈이 운동 시 혈소판 반응성 증가를 완화함 |
| [749930](https://pubmed.ncbi.nlm.nih.gov/749930/) | 1978 | 미분류 | Br J Haematol | 혈소판 인자 4 측정법. theophylline은 채혈 항응고 용액의 성분일 뿐 치료 목적이 아님 |
| [29254574](https://pubmed.ncbi.nlm.nih.gov/29254574/) | 2018 | 분석법 | Anal Chim Acta | theophylline 검출용 전기화학 앱타센서 개발 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200704931 | 데올론건조시럽20%(수출용) (코오롱제약) | 건조시럽제 | [허가 원문 링크](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200704931/EE) 참조 |
| 200302202 | 데오크레건조시럽20% (알보젠코리아) | 건조시럽제 | [허가 원문 링크](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200302202/EE) 참조 |

두 제품 모두 단일제이며 현재 유효한 허가입니다.

## 안전성 고려사항

- **약물 상호작용**: 이번에 조회된 상호작용은 총 100건이며, 그중 일부만 상세 목록으로 제공되었습니다.
  - **Major**: Bupropion
  - **Moderate**: Famotidine, Ranitidine, Cimetidine, Omeprazole, Rabeprazole, Clarithromycin, Doxycycline, Tetracycline, Minocycline, Hydrocortisone, Dexamethasone, Betamethasone, Triamcinolone, Budesonide, Picosulfuric acid, Polyethylene glycol (전해질 포함), Activated charcoal
  - **Minor**: Ephedrine (경구·비강)
- **지식 그래프상 금기 관련 질환**(허가 문구가 아닌 모델 지식 그래프 기준): 고혈압, 간부전·간질환, 간질(뇌전증), 불안장애, 정신병적 장애, 포르피린증, 신장질환, 담낭질환, 혈소판감소증, 호중구감소증·무과립구증, 갑상선기능저하증, 소화성 궤양, 개방각 녹내장, 당뇨병·당뇨병성 케톤산증, 양성 전립선 비대증 등.
- Theophylline은 치료역이 좁고 CYP1A2 관련 상호작용이 많습니다. 비중증 질환이나 혈전 예방 목적으로 사용하려면 이 위험을 고려해야 합니다. 허가사항의 경고·금기는 허가 원문에서 별도로 확인해야 합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
혈전성 질환에 대해 임상시험이 없고 문헌도 이 용도를 직접 검증하지 않아 근거는 모델 예측에 그칩니다(L5). 혈소판 cAMP 상승이라는 기전적 연결은 약하며, 좁은 치료역과 높은 상호작용 부담이 이 가설의 부담을 키웁니다.

**진행하려면 필요한 것:**
- theophylline의 혈소판 응집·혈전 형성에 대한 전임상 및 소규모 임상 근거
- 한국 허가 원문에서 적응증, 경고, 금기 확인
- 상세 작용 기전 데이터 확보 및 기존 항혈전제 대비 이점 평가
- 참고: 같은 모델이 예측한 **폐쇄성 폐질환**은 근거 수준이 L1이지만 이미 확립된 기존 용도에 가까워 신규 재창출 후보로 보기는 어렵습니다. 알레르기성 비염(비강 질환)은 Phase 2 시험 1건과 소규모 연구가 있어 별도 검토 대상입니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

