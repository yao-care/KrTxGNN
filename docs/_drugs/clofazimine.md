---
layout: default
title: Clofazimine
parent: 모델 예측만 (L5)
nav_order: 226
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
description: "Clofazimine: 예측 신규 적응증 폐포자충증 (Pneumocystosis) (근거 수준 L5). 기존 적응증: 1. 한센병 1) 나병종나병과 중간나병 2) 답손에 내성이 있는 나병종나병과 중간나병 3) 나병결절홍반과…"
monitor_inn: "CLOFAZIMINE"
predicted_indications: ["pneumocystosis", "malaria", "gastrin secretion abnormality"]
---

# Clofazimine
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

## Clofazimine: 한센병·결핵 치료제에서 폐포자충증으로
{: .text-alpha }

## 한 문장 요약

Clofazimine은 리미노페나진(riminophenazine) 계열 항마이코박테리아제로, 한국에서 허가된 단일제 연질캡슐 제품으로 시판되고 있습니다. TxGNN 모델은 **폐포자충증(pneumocystosis)**에 효과가 있을 수 있다고 예측하지만, 이 예측을 직접 뒷받침하는 임상시험은 **0건**이며 연결된 문헌 3편도 폐포자충증에 대한 효능 근거가 아닙니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 1. 한센병 1) 나병종나병과 중간나병 2) 답손에 내성이 있는 나병종나병과 중간나병 3) 나병결절홍반과 같은 나병반응 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201706794/EE)) |
| 예측 신규 적응증 | 폐포자충증 (Pneumocystosis) |
| TxGNN 예측 점수 | 0.9990 |
| 근거 수준 | L5 (모델 예측 중심, 직접적인 연구 없음) |
| 한국 시판 현황 | 시판 중 (유효 허가 3건 / 전체 3건) |
| 허가증 수 | 3건 (유효 3건) |
| 권장 결정 | Hold |

> 참고: 데이터상 근거 수준은 L4로 제시되어 있으나, 판정 규칙에 따르면 폐포자충증에 대한 전임상·기전 연구가 없으므로 L5가 더 적절합니다.

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Clofazimine 처방 정보(Prescribing Information)의 “Mechanism of Action” 및 “Microbiology” 항목에 따르면(비공식 번역): “LAMPRENE은 항마이코박테리아 약물이다. […] 클로파지민은 Mycobacterium leprae(한센균)에 대해 느린 살균 효과를 나타낸다. 클로파지민은 마이코박테리아의 증식을 억제하며 마이코박테리아 DNA에 우선적으로 결합한다. 클로파지민은 또한 나성 결절성 홍반 반응의 치료에 있어 항염증 작용을 나타낸다.” 영어 원문: "LAMPRENE is an anti-mycobacterial drug. […] Clofazimine exerts a slow bactericidal effect on Mycobacterium leprae (Hansen’s bacillus). Clofazimine inhibits mycobacterial growth and binds preferentially to mycobacterial DNA. Clofazimine also exerts anti-inflammatory properties in treating erythema nodosum leprosum reactions." ([DailyMed: Lamprene (clofazimine) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2e07448f-f888-4747-80ab-570c1b621250), 버전 2026-08-17; 확인일 2026-11-19). Clofazimine은 리미노페나진 계열 항마이코박테리아제로 알려져 있으며, 결핵 및 한센병 치료 요법에 사용됩니다. 그러나 폐포자충증의 원인균인 *Pneumocystis jirovecii*는 세균이 아니라 진균이며, clofazimine이 이 병원체에 활성이 있다는 근거는 확인되지 않았습니다.

TxGNN 점수(0.9990)는 네트워크 기반 예측일 뿐입니다. 연결된 문헌은 AIDS 환자에서의 *Mycobacterium avium* complex(MAC) 예방 연구와, *M. kansasii* 감염에 폐포자충 폐렴이 동반된 증례입니다. 즉, 이 연관성은 HIV/AIDS 환자에서 기회감염이 함께 나타나는 현상을 반영한 것이며, 항폐포자충 효능을 보여주는 것은 아닙니다. 따라서 기전상 연결고리는 확립되지 않았습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [8501340](https://pubmed.ncbi.nlm.nih.gov/8501340/) | 1993 | 무작위 공개label 임상시험 (MAC 예방) | J Infect Dis | HIV 환자 110명 대상으로 clofazimine의 파종성 MAC 감염 예방 효과와 안전성을 평가함. 폐포자충증에 대한 연구는 아님 |
| [2714863](https://pubmed.ncbi.nlm.nih.gov/2714863/) | 1989 | Case report | Infection | AIDS 환자의 *M. kansasii* 폐질환에 폐포자충 폐렴이 합병된 사례. clofazimine은 병용 항균요법에 포함되었으며, 회복은 TMP-SMX 투여 후 관찰됨 |
| [11363899](https://pubmed.ncbi.nlm.nih.gov/11363899/) | 1996 | Review | PI Perspective | 기회감염 최신 동향 개괄 (초록 없음) |

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 201706794 | 람프레민연질캡슐100밀리그램(클로파지민) | 진한 적갈색~갈색의 내용물을 함유하는 갈색의 타원형 연질캡슐제 | 동아에스티(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201706794/EE) | 유효 |
| 201105516 | 코러스클로파지민연질캡슐(수출용) | 적갈색의 유상 내용물을 함유한 적갈색의 원형 연질캡슐 | 한국코러스(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201105516/EE) | 유효 |
| 198601341 | 라프렌연질캡슐50밀리그램(클로파지민) | 적갈색의 원형 연질캅셀 | (주)태준제약 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/198601341/EE) | 유효 |

<!-- licenses:end -->

## 안전성 고려사항

- **약물 상호작용**: 데이터상 총 100건이 확인되었으며, 주요 항목은 다음과 같습니다.
  - **Major**: Cisapride, Dolasetron
  - **Moderate**: Famotidine, Loperamide, Bisacodyl, Clarithromycin, Levofloxacin, Ondansetron, Granisetron, Palonosetron 및 여러 설사제·완하제(Lactulose, Magnesium citrate, Magnesium hydroxide, Castor oil, Mineral oil 등)
  - **Minor**: Metronidazole
- **지식 그래프상 금기 관련 질환** (허가사항이 아닌 TxGNN 지식 그래프 기반): 간질환, 담낭질환, 설사성 질환, 활동성 소화성 궤양, 소화기계 질환, 장질환, 비장 경색, 비장 질환, 비기능항진증

그 외 경고 및 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
폐포자충증에 대한 임상시험이 없고, 연결된 문헌은 MAC 예방 연구와 동시 감염 증례일 뿐 항폐포자충 효능을 보여주지 않습니다. 높은 TxGNN 점수 외에는 기전상 근거가 없어 현 단계에서 진행하기 어렵습니다.

**진행하려면 필요한 것:**
- 작용 기전(MOA) 데이터 확보
- *Pneumocystis*에 대한 in vitro/in vivo 전임상 활성 검증
- 한국 허가 적응증 및 허가사항(경고·금기)의 확인과 분석
- 약물 상호작용(특히 QT 연장 관련 Major 상호작용) 위험 평가

---

### 참고: 기타 예측 적응증

| 순위 | 예측 질환 | TxGNN 점수 | 근거 | 권장 |
|------|---------|-----------|------|------|
| 2 | 말라리아 (Malaria) | 0.9960 | 임상시험 없음. clofazimine 유사체의 항플라스모디움 활성에 대한 시험관 연구 1편([29026393](https://pubmed.ncbi.nlm.nih.gov/29026393/))이 있으나, 나머지 문헌은 대부분 내성 결핵·한센병 관련으로 말라리아 효능 근거가 아님 | Hold |
| 3 | 가스트린 분비 이상 | 0.9957 | 임상시험 및 문헌 없음. 모델 예측만 존재 | Hold |

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Lamprene (clofazimine) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2e07448f-f888-4747-80ab-570c1b621250) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

