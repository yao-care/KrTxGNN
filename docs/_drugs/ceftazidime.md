---
layout: default
title: Ceftazidime
parent: 모델 예측만 (L5)
nav_order: 196
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-15
description: "Ceftazidime: 예측 신규 적응증 고아밀라제혈증 (Hyperamylasemia) (근거 수준 L5). 기존 적응증: 허가 적응증 텍스트는 문서 링크로만 제공되어 구체적인 내용을 확인할 수 없음"
monitor_inn: "CEFTAZIDIME"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "urinary tract infection (disease)", "epiglottitis", "blood group incompatibility", "Peptostreptococcus infectious disease"]
---

# Ceftazidime
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **7** 건
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

## Ceftazidime: 세균 감염에서 고아밀라제혈증으로
{: .text-alpha }

## 한 문장 요약

Ceftazidime은 3세대 세ファロ스포린계 항생제로, 한국에서 수출용 주사제로 허가되어 시판 중입니다.
TxGNN 모델은 **고아밀라제혈증(hyperamylasemia)**에 효과가 있을 수 있다고 가장 높게 예측했으나, 이를 뒷받침하는 임상시험과 문헌은 **없습니다**.
다만 예측 순위 하위 항목 중 **요로감염**(임상시험 4건, 문헌 20편)은 상대적으로 근거가 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 텍스트는 문서 링크로만 제공되어 구체적인 내용을 확인할 수 없음 |
| 예측 신규 적응증 | 고아밀라제혈증 (Hyperamylasemia) |
| TxGNN 예측 점수 | 0.9951 |
| 근거 수준 | L5 (모델 예측만 존재) |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

> 참고: 1순위 예측은 근거가 없어 보류이며, 아래에서 근거가 있는 다른 예측 적응증도 함께 정리했습니다.

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Ceftazidime은 Pseudomonas aeruginosa를 포함한 그람음성균에 활성을 보이는 3세대 세팔로스포린으로, 세균 세포벽 합성을 억제합니다.

1순위인 고아밀라제혈증은 감염이 아니라 검사실 소견이며, 세포벽 합성 억제 기전과 연결되는 합리적인 설명이 없습니다. 2~3순위(다클론성 과점성 증후군, 선천성 무알부민혈증)도 마찬가지로 기전상 타당성이 낮으며, 이 점수는 TxGNN 모델(딥러닝)이 관련 질환 간에 학습한 유사성을 반영한 것일 수 있고 생물학적 근거는 아닙니다.

반면 요로감염과 Pseudomonas에 의한 만성 화농성 중이염은 항균 스펙트럼과 부합합니다. 다만 요로감염은 이미 허가 범위에 포함되었을 가능성이 높아 진정한 재창출이라기보다 기존 적응증에 가깝습니다.

## 임상시험 근거

1순위 예측(고아밀라제혈증)에 대한 임상시험은 없습니다. 현재 관련 임상시험 등록이 없습니다.

참고로 4순위 예측인 요로감염에는 아래 시험이 있습니다. 대부분 ceftazidime 단독이 아닌 avibactam 복합제 또는 비교약 시험입니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00921024](https://clinicaltrials.gov/study/NCT00921024) | Phase 2 | 완료 | 129 | 복잡성 요로감염(신우신염 포함)에서 CXA-101 vs Ceftazidime 정맥 투여의 안전성·유효성 비교 (이중맹검 무작위) |
| [NCT04882085](https://clinicaltrials.gov/study/NCT04882085) | Phase 4 | 완료 | 60 | 중국 성인의 카바페넴 내성 그람음성균 감염에서 Ceftazidime-avibactam vs 최선의 가용 치료 (공개 라벨) |
| [NCT01430910](https://clinicaltrials.gov/study/NCT01430910) | Phase 1 | 완료 | 43 | 건강인 대상 Ceftazidime-avibactam의 약동학 및 약물 상호작용 |
| [NCT04278404](https://clinicaltrials.gov/study/NCT04278404) | 해당 없음 | 모집 중 | 5000 | 소아에서 연구가 부족한 약물의 약동학·안전성 |

## 문헌 근거

1순위 예측에 대한 문헌은 없습니다. 현재 관련 문헌이 없습니다.

아래는 근거가 있는 예측 적응증의 주요 문헌입니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [39817442](https://pubmed.ncbi.nlm.nih.gov/39817442/) | 2025 | 체계적 문헌고찰/네트워크 메타분석 | J Comp Eff Res | 급성 신우신염을 포함한 복잡성 요로감염 치료 옵션의 효능 비교 (요로감염) |
| [35787918](https://pubmed.ncbi.nlm.nih.gov/35787918/) | 2022 | Review | Int J Antimicrob Agents | 다제내성 그람음성균 감염 신약 임상 자료, ceftazidime-avibactam 포함 (요로감염) |
| [32094128](https://pubmed.ncbi.nlm.nih.gov/32094128/) | 2020 | 후향적 코호트 | Antimicrob Agents Chemother | 카바페넴 내성 장내세균 감염에서 meropenem-vaborbactam vs ceftazidime-avibactam (요로감염) |
| [10826908](https://pubmed.ncbi.nlm.nih.gov/10826908/) | 2000 | 무작위 공개 시험 | Scand J Infect Dis | Pseudomonas성 만성 화농성 중이염 소아에서 ceftazidime(15명) vs aztreonam(15명) 비교 (중이염) |
| [10768520](https://pubmed.ncbi.nlm.nih.gov/10768520/) | 2000 | 코호트/증례 연속 | J Chemother | 소아 52명에서 ceftazidime 외래 정맥 항생제 치료(OPAT)의 유효성과 안전성 (중이염) |
| [8451104](https://pubmed.ncbi.nlm.nih.gov/8451104/) | 1993 | 코호트 | Pediatr Infect Dis J | 담지종 없는 소아 만성 화농성 중이염에서 ceftazidime 치료 (중이염) |
| [1528644](https://pubmed.ncbi.nlm.nih.gov/1528644/) | 1992 | 코호트 | Pediatr Infect Dis J | 소아 만성 화농성 중이염의 외래 치료 가능성 (중이염) |
| [39567876](https://pubmed.ncbi.nlm.nih.gov/39567876/) | 2025 | Case report | Ann Otol Rhinol Laryngol | 소아 Gradenigo 증후군에서 ceftazidime-cefazolin 경험적 치료 (중이염) |
| [8126192](https://pubmed.ncbi.nlm.nih.gov/8126192/) | 1994 | Case report | J Clin Microbiol | ceftazidime 투여 중 발생한 내성 폐렴구균 원내 후두개염 (후두개염) |
| [19802974](https://pubmed.ncbi.nlm.nih.gov/19802974/) | 1981 | In-vitro | J Antimicrob Chemother | 혐기성균에 대한 ceftazidime의 제한적 활성 (Peptostreptococcus 감염) |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201202147 | 딤제프주2그램(수출용) | 백색 또는 유백색의 가루가 든 주사제 | 허가 적응증 문서 링크로만 제공되어 요약 불가 |

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 조회되었으며, 주요 항목은 다음과 같습니다.
  - 중등도: Amphotericin B 계열(일반, cholesteryl sulfate, lipid complex, liposomal), Kanamycin, Neomycin, Streptomycin, Picosulfuric acid
  - 등급 미상: Calcitriol, Pantoprazole, Doxycycline, Morphine, Metformin, Omeprazole, Sucralfate, Lansoprazole, Vancomycin, Atropine, Lactulose, Triamcinolone 등
- **지식 그래프 기반 금기 관련 질환** (허가사항이 아닌 모델 지식 그래프 자료): 신장 질환, 요관 농양, 간 질환, 담낭 질환, 혈액응고 질환, Clostridium difficile 대장염, 신생아 괴사성 장염, 선천성 프로트롬빈 결핍

허가사항의 경고 및 금기는 허가증 자료가 확인되지 않았으므로 허가사항을 직접 참조하세요.

## 결론 및 다음 단계

**결정: Hold** (1순위 예측 고아밀라제혈증 기준)

**사유:**
고아밀라제혈증은 기전상 타당성이 없고 임상시험·문헌 근거가 전혀 없는 모델 예측일 뿐입니다. 요로감염은 근거 수준 L2(Proceed with Guardrails)로 평가되었으나 대부분 avibactam 복합제 시험이며 기존 적응증과 겹칠 가능성이 있습니다. 감염성 중이염(L3)은 소아 대상의 소규모·고연령 연구가 중심입니다.

**진행하려면 필요한 것:**
- 허가 적응증 및 경고·금기 정보 확보 (식약처 허가사항 PDF 내려받아 분석)
- 작용 기전(MOA) 데이터 보완 (DrugBank 조회)
- 요로감염: ceftazidime 단독 요법의 근거와 기존 허가 적응증 포함 여부 확인
- 감염성 중이염: Pseudomonas성 만성 화농성 중이염에서 국소 치료 대비 전신 투여의 필요성 검토, 국내 내성 양상과 항생제 적정사용 지침 반영
- 후두개염, 임질성 요도염, Peptostreptococcus 감염은 근거가 부족하고 더 적합한 대체 약제가 있어 연구 질문 수준에 머무름
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

