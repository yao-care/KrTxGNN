---
layout: default
title: Remdesivir
parent: 모델 예측만 (L5)
nav_order: 649
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Remdesivir: 예측 신규 적응증 다중 내분비 종양증 (Multiple Endocrine Neoplasia) (근거 수준 L5). 기존 적응증: 허가 적응증 본문은 확인되지 않았습니다(허가 문서 링크만 제공됨)"
monitor_inn: "Remdesivir"
predicted_indications: ["multiple endocrine neoplasia", "HIV infectious disease", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "homozygous familial hypercholesterolemia", "Prinzmetal angina", "leprosy", "antithrombin deficiency type 2", "cytomegalovirus infection"]
---

# Remdesivir
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

# Remdesivir: 바이러스 감염증에서 다중 내분비 종양증으로

## 한 문장 요약

Remdesivir는 바이러스 RNA 중합효소를 억제하는 뉴클레오티드 유사체 항바이러스제로, 한국에서는 베클루리주(정맥주사제)로 허가되어 있습니다.
TxGNN 모델은 **다중 내분비 종양증(Multiple Endocrine Neoplasia)**에 효과가 있을 수 있다고 예측하지만, 이를 지지하는 **임상시험은 0건, 문헌도 0편**입니다.
따라서 이 예측은 모델 계산 결과일 뿐이며 생물학적 근거가 확인되지 않습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문은 확인되지 않았습니다(허가 문서 링크만 제공됨). |
| 예측 신규 적응증 | 다중 내분비 종양증 (Multiple Endocrine Neoplasia) |
| TxGNN 예측 점수 | 99.50% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면, Remdesivir는 바이러스 RNA 의존성 RNA 중합효소(RdRp)를 억제하는 뉴클레오티드 유사체 전구약물입니다.

다중 내분비 종양증은 MEN1, RET 변이 등으로 발생하는 유전성 종양 증후군입니다. 항바이러스 기전은 이 질환의 병태생리와 연결되는 고리가 없으며, 높은 예측 점수는 계산상의 결과일 뿐 생물학적 타당성이 뒷받침되지 않습니다.

### 참고: 다른 예측 적응증

| 순위 | 예측 질환 | 점수 | 근거 수준 | 평가 |
|------|---------|------|---------|------|
| 2 | HIV 감염증 | 99.32% | L4 | 관련 시험(NCT04385719)은 약동학 연구로, HIV에서의 효능 근거는 없습니다. 문헌은 대부분 COVID-19 관련입니다. |
| 3 | 원숭이 면역결핍 바이러스 감염 | 99.07% | L5 | 시험·문헌 근거 없음 |
| 4 | 고양이 후천성 면역결핍 증후군 | 99.07% | L5 | 수의학 질환으로 인체 적용과 무관 |
| 8 | 나병 | 97.37% | L5 | 세균 감염으로 항균 활성이 알려져 있지 않음 |
| 10 | 거대세포바이러스 감염 | 97.08% | L4 | CMV는 DNA 바이러스로 직접 효능을 기대하기 어렵고, 문헌은 COVID-19 환자의 CMV 재활성화 관련입니다. |

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202005381 | 베클루리주정맥주사용동결건조분말(렘데시비르) | 동결건조분말 주사제 (길리어드사이언스코리아) | 허가 적응증 본문 확인 불가 |

## 안전성 고려사항

- **약물 상호작용**: 이 보고서용으로 수집된 데이터에서 100건의 상호작용이 확인되었으며, 목록에 제시된 20건은 모두 '중등도'입니다. 주요 항목은 다음과 같습니다.
  - 항생제: Doxycycline, Minocycline, Tetracycline, Clarithromycin, Levofloxacin, Vancomycin, Kanamycin, Neomycin
  - 항진균제: Amphotericin B (일반 및 지질 복합체)
  - 당뇨병 치료제: Acarbose, Pioglitazone
  - 기타: Bupropion, Mesalazine, Balsalazide, Olsalazine, Chenodeoxycholic acid, Oxandrolone, Oxymetholone, Naltrexone

허가사항의 경고 및 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
다중 내분비 종양증에 대해 임상시험과 문헌 근거가 전혀 없고(L5), 항바이러스 기전과의 생물학적 연결고리도 없습니다. 높은 TxGNN 점수만으로는 개발을 진행할 근거가 되지 않습니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기·적응증 본문) 확보 및 분석 (현재 안전성 선별 진행 불가)
- 상세한 약물 작용 기전(MOA) 데이터
- 다중 내분비 종양증과 관련된 전임상 또는 기전 연구 근거
- 추후 검토 대상으로는 HIV 감염증 및 CMV 감염이 있으나, 현재까지 직접적인 효능 근거는 없습니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

