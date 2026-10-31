---
layout: default
title: Baclofen
parent: 모델 예측만 (L5)
nav_order: 121
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-31
description: "Baclofen: 예측 신규 적응증 주의력결핍 과잉행동장애 (Attention Deficit-Hyperactivity Disorder) (근거 수준 L5). 기존 적응증: 근육 경직(spasticity). 허가 문서는 링크로만 확인되었고, 적응증은 문헌의 설명을 따랐습니다"
monitor_inn: "BACLOFEN"
predicted_indications: ["attention deficit-hyperactivity disorder", "nicotine dependence"]
---

# Baclofen
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **2** 건
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

## Baclofen: 근육 경직에서 주의력결핍 과잉행동장애(ADHD)로
{: .text-alpha }

## 한 문장 요약

Baclofen은 GABA-B 수용체 작용제로, 원래 근육 경직(spasticity) 치료에 사용되어 온 약입니다.
TxGNN 모델은 **주의력결핍 과잉행동장애(ADHD)**에 효과가 있을 수 있다고 예측하지만, 임상시험은 **0건**입니다. 문헌 **9편**도 대부분 투렛증후군 총설이거나 동물 실험이어서, 이 약의 ADHD 효능을 직접 평가한 연구는 없습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 근육 경직(spasticity). 허가 문서는 링크로만 확인되었고, 적응증은 문헌의 설명을 따랐습니다. |
| 예측 신규 적응증 | 주의력결핍 과잉행동장애 (Attention Deficit-Hyperactivity Disorder) |
| TxGNN 예측 점수 | 0.9932 |
| 근거 수준 | L5 (모델 예측만 있고 직접적인 임상 연구 없음) |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 20건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 충분하지 않습니다. 다만 이번 보고서용으로 정리된 분석에 따르면 Baclofen은 GABA-B 수용체를 활성화하는 약물입니다. GABA-B 수용체는 뇌의 도파민·글루타메이트 회로를 조절합니다. 이 회로는 충동성과 주의력 조절에 관여하므로, GABA 신경계 조절이 ADHD 증상에 영향을 줄 수 있다는 가설이 가능합니다.

다만 이 연관성은 이론적 추정에 가깝습니다. 제공된 문헌은 ADHD가 흔히 동반되는 투렛증후군·틱 장애를 다루거나, 노르아드레날린 α2A 수용체, 해마, 해바라기핵(habenula), 대상피질·편도체 등을 다룬 설치류 연구입니다. 이 중 Baclofen을 ADHD에 직접 평가한 연구는 없습니다. 예측 점수 0.9932는 TxGNN 모델(딥러닝)의 계산상 예측값이며, 이를 뒷받침하는 임상 자료는 현재 확인되지 않았습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [24295630](https://pubmed.ncbi.nlm.nih.gov/24295630/) | 2013 | Review | Int Rev Neurobiol | 투렛증후군의 신규 치료 전략 개관. ADHD는 흔한 동반 질환으로만 언급됩니다. |
| [11393328](https://pubmed.ncbi.nlm.nih.gov/11393328/) | 2001 | Review | Paediatr Drugs | 투렛증후군의 임상 특징과 치료 전략. 동반 정신질환이 있을 때의 약물 치료를 다룹니다. |
| [35345730](https://pubmed.ncbi.nlm.nih.gov/35345730/) | 2022 | Review | Cureus | 투렛증후군 틱에 대한 행동 중재, 항정신병약, 알파 작용제의 효과 고찰 |
| [10342599](https://pubmed.ncbi.nlm.nih.gov/10342599/) | 1999 | Review | J Child Neurol | 틱/투렛증후군 환자 450명에게 baclofen/보툴리눔 독소를 사용한 경험. 틱 증상이 대상이며 ADHD는 직접 평가하지 않았습니다. |
| [21300040](https://pubmed.ncbi.nlm.nih.gov/21300040/) | 2011 | 전임상(동물 EEG) | Brain Res | ADHD 모델 쥐(SHR)와 카이닌산 처리 쥐에서 신경전달물질 작용제의 뇌파 반응 비교 |
| [24062084](https://pubmed.ncbi.nlm.nih.gov/24062084/) | 2014 | 전임상(동물) | Psychopharmacology | 해마 α2A 수용체 자극이 충동적 의사결정을 줄임 (guanfacine 사용) |
| [24496320](https://pubmed.ncbi.nlm.nih.gov/24496320/) | 2014 | 전임상(동물) | Neuropsychopharmacology | 인지적 노력 기반 의사결정에서 전방 대상피질과 기저외측 편도체의 역할 |
| [24103016](https://pubmed.ncbi.nlm.nih.gov/24103016/) | 2013 | 전임상(동물) | Eur J Neurosci | 해바라기핵 기능이 쥐의 사회적 놀이 행동에 필요함 |
| [30122296](https://pubmed.ncbi.nlm.nih.gov/30122296/) | 2019 | 기타 | L'Encephale | 성인 ADHD에서 methylphenidate의 적응증 외 처방 고찰. Baclofen 특이적 연구가 아닙니다. |

## 한국 시판 정보

한국에서는 단일제 20건이 유효하게 허가되어 있으며, 수출용 허가도 일부 포함됩니다. 허가 적응증은 문서 링크로만 제공되어 있습니다. 아래는 주요 5건입니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 198501456 | 바클란정10밀리그램 (유영제약) | 정제 | [허가 문서 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/198501456/EE) |
| 199101450 | 프렉스정5밀리그램 (한국유나이티드제약) | 정제 | [허가 문서 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199101450/EE) |
| 200000452 | 삼성바클로펜정 (삼성제약) | 정제 | [허가 문서 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200000452/EE) |
| 199602834 | 풍림바클로펜정 (풍림무약) | 정제 | [허가 문서 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199602834/EE) |
| 199001340 | 프렉스정 (한국유나이티드제약) | 정제 | [허가 문서 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199001340/EE) |

## 안전성 고려사항

허가사항의 경고·금기 정보는 이번 보고서에 포함되지 않았습니다. 상세 내용은 허가사항을 참조하세요.

- **지식그래프 기반 금기 관련 질환** (허가 문구가 아니라 TxGNN 지식그래프의 약물-질환 관계에서 도출됨): 간질, 신장 질환, 정신병적 장애(조현병, 조현정동장애 등 포함), 뇌졸중·뇌혈관 질환, 자율신경계 질환(자율신경 반사부전 등), 방광경부 질환
  - ADHD 환자는 신경·정신과적 동반 질환이 많으므로 특히 주의가 필요합니다.
- **약물 상호작용**: 총 100건이 조회되었습니다.
  - **Major**: Morphine, Morphine (liposomal)
  - **Moderate**: Dronabinol, Nabilone, Metoclopramide, Opium, Sibutramine, Difenoxin, Diphenoxylate
  - 중추신경 억제 작용이 겹치는 약물과의 병용에 유의해야 합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
ADHD에 대한 임상시험이 없고 문헌도 간접적이거나 전임상 수준이어서, 근거 수준이 L5(모델 예측만 있음)에 머물러 있습니다. 지식그래프상 금기 질환이 많다는 점도 신중한 접근이 필요한 이유입니다.

**진행하려면 필요한 것:**
- Baclofen의 ADHD 효능을 직접 평가한 전임상·임상 연구 (소규모 탐색적 시험부터)
- 허가사항(PDF)의 경고·금기·적응증 확인
- 상세한 작용 기전 데이터 보완 (DrugBank 등)
- 신경·정신과적 동반 질환이 있는 ADHD 환자에 대한 안전성 평가 계획
- 참고로, 같은 약물의 2순위 예측인 **니코틴 의존성**에는 Phase 2 임상시험 3건(완료 1건, 조기 종료 2건)과 전임상 근거가 있어 상대적으로 근거가 많습니다. 우선순위 재검토 시 함께 고려할 수 있습니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

