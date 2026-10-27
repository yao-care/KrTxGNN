---
layout: default
title: Clofazimine
parent: 모델 예측만 (L5)
nav_order: 226
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Clofazimine: 예측 신규 적응증 폐포자충증 (Pneumocystosis) (근거 수준 L5). 기존 적응증: 허가 적응증 원문이 문서 링크 형태로만 제공되어 구체적인 질환명을 확인할 수 없음 (허가사항 참조 필요)"
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
| 기존 적응증 | 허가 적응증 원문이 문서 링크 형태로만 제공되어 구체적인 질환명을 확인할 수 없음 (허가사항 참조 필요) |
| 예측 신규 적응증 | 폐포자충증 (Pneumocystosis) |
| TxGNN 예측 점수 | 99.90% |
| 근거 수준 | L5 (모델 예측 중심, 직접적인 연구 없음) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 3건 |
| 권장 결정 | Hold |

> 참고: 데이터상 근거 수준은 L4로 제시되어 있으나, 판정 규칙에 따르면 폐포자충증에 대한 전임상·기전 연구가 없으므로 L5가 더 적절합니다.

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. Clofazimine은 리미노페나진 계열 항마이코박테리아제로 알려져 있으며, 결핵 및 한센병 치료 요법에 사용됩니다. 그러나 폐포자충증의 원인균인 *Pneumocystis jirovecii*는 세균이 아니라 진균이며, clofazimine이 이 병원체에 활성이 있다는 근거는 확인되지 않았습니다.

TxGNN 점수(99.9%)는 네트워크 기반 예측일 뿐입니다. 연결된 문헌은 AIDS 환자에서의 *Mycobacterium avium* complex(MAC) 예방 연구와, *M. kansasii* 감염에 폐포자충 폐렴이 동반된 증례입니다. 즉, 이 연관성은 HIV/AIDS 환자에서 기회감염이 함께 나타나는 현상을 반영한 것이며, 항폐포자충 효능을 보여주는 것은 아닙니다. 따라서 기전상 연결고리는 확립되지 않았습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [8501340](https://pubmed.ncbi.nlm.nih.gov/8501340/) | 1993 | 무작위 공개label 임상시험 (MAC 예방) | J Infect Dis | HIV 환자 110명 대상으로 clofazimine의 파종성 MAC 감염 예방 효과와 안전성을 평가함. 폐포자충증에 대한 연구는 아님 |
| [2714863](https://pubmed.ncbi.nlm.nih.gov/2714863/) | 1989 | Case report | Infection | AIDS 환자의 *M. kansasii* 폐질환에 폐포자충 폐렴이 합병된 사례. clofazimine은 병용 항균요법에 포함되었으며, 회복은 TMP-SMX 투여 후 관찰됨 |
| [11363899](https://pubmed.ncbi.nlm.nih.gov/11363899/) | 1996 | Review | PI Perspective | 기회감염 최신 동향 개괄 (초록 없음) |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201706794 | 람프레민연질캡슐100밀리그램(클로파지민) | 연질캡슐 | 허가사항 문서 참조 |
| 201105516 | 코러스클로파지민연질캡슐(수출용) | 연질캡슐 | 허가사항 문서 참조 |
| 198601341 | 라프렌연질캡슐50밀리그램(클로파지민) | 연질캡슐 | 허가사항 문서 참조 |

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
| 2 | 말라리아 (Malaria) | 99.60% | 임상시험 없음. clofazimine 유사체의 항플라스모디움 활성에 대한 시험관 연구 1편([29026393](https://pubmed.ncbi.nlm.nih.gov/29026393/))이 있으나, 나머지 문헌은 대부분 내성 결핵·한센병 관련으로 말라리아 효능 근거가 아님 | Hold |
| 3 | 가스트린 분비 이상 | 99.57% | 임상시험 및 문헌 없음. 모델 예측만 존재 | Hold |
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

