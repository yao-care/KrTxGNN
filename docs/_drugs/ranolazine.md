---
layout: default
title: Ranolazine
parent: 모델 예측만 (L5)
nav_order: 644
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Ranolazine: 예측 신규 적응증 신성 항이뇨호르몬 부적절 분비 증후군 (Nephrogenic Syndrome of Inappropriate Antidiure… (근거 수준 L5). 기존 적응증: 허가 적응증 본문은 허가증 링크로만 제공되어 요약할 수 없음 (허가사항 참조)"
monitor_inn: "RANOLAZINE"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis"]
---

# Ranolazine
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **1** 건
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

# Ranolazine: 허가 적응증에서 신성 항이뇨호르몬 부적절 분비 증후군(NSIAD)으로

## 한 문장 요약

Ranolazine은 한국에서 허가된 단일 성분 서방정제로, 후기 나트륨 전류(late sodium current)를 억제하는 약물입니다.
TxGNN 모델은 **신성 항이뇨호르몬 부적절 분비 증후군(Nephrogenic Syndrome of Inappropriate Antidiuresis, NSIAD)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 뒷받침하는 **임상시험과 문헌은 각각 0건**으로 모델 예측만 존재하는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문은 허가증 링크로만 제공되어 요약할 수 없음 (허가사항 참조) |
| 예측 신규 적응증 | 신성 항이뇨호르몬 부적절 분비 증후군 (Nephrogenic Syndrome of Inappropriate Antidiuresis) |
| TxGNN 예측 점수 | 99.65% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 3건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 이번 보고서에 수집된 자료에 없습니다. 알려진 정보에 따르면 Ranolazine은 후기 나트륨 전류(INa-late) 억제제이며, hERG 전류와 지방산 산화에도 부분적인 영향을 미칩니다.

NSIAD는 바소프레신 V2 수용체(AVPR2)의 기능획득 돌연변이(R137C/R137L)로 인해 cAMP 경로가 지속적으로 활성화되고, 집합관의 아쿠아포린-2(AQP2)를 통해 수분이 과도하게 재흡수되는 질환입니다. Ranolazine의 나트륨 채널 억제가 V2 수용체 신호전달이나 AQP2 이동과 연결된다고 알려진 기전적 경로는 없습니다.

신세뇨관 이온 수송이나 cAMP 관련 조절을 통한 연관성은 추측 수준이며 전임상 검증이 필요합니다. 높은 예측 점수는 실제 생물학적 관련성보다 지식 그래프상의 네트워크 근접성을 반영했을 가능성이 있습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202001782 | 라넥사서방정500밀리그램(라놀라진) | 서방성 필름코팅정 (밝은 주황색, 타원형, 500 표기) | 허가사항 참조 |
| 202001784 | 라넥사서방정750밀리그램(라놀라진) | 서방성 필름코팅정 (연한 녹색, 타원형, 750 표기) | 허가사항 참조 |
| 202001783 | 라넥사서방정375밀리그램(라놀라진) | 필름코팅정 (연한 파랑색, 타원형, 375 표기) | 허가사항 참조 |

3건 모두 한국메나리니(주)의 유효한 단일 성분 허가입니다.

## 안전성 고려사항

- **지식 그래프상 금기 질환**: 긴QT증후군, 가족성 긴QT증후군, 토르사드 드 푸앵트, 신장질환, 농뇨관(pyoureter), 간경변. 이는 허가 문구가 아닌 TxGNN 지식 그래프(PrimeKG)의 약물-질환 금기 연결에서 얻은 정보입니다.
- **약물 상호작용**: 총 100건이 확인되었으며, 주요 항목은 다음과 같습니다.
  - **Major**: Aprepitant, Dexamethasone, Clarithromycin, Dolasetron, Eliglustat
  - **Moderate**: Famotidine, Metformin, Loperamide, Bisacodyl, Budesonide, Canagliflozin, Dapagliflozin, Empagliflozin 등
  - **Minor**: Bupropion, Lorcaserin, Cimetidine

NSIAD는 신장 질환과 수분·전해질 균형이 핵심인 질환이므로, 금기 목록에 신장질환과 QT 연장 관련 질환이 포함된 점은 신규 적응증 검토 시 특히 유의해야 합니다. 허가사항의 경고 및 금기 문구는 아직 확인되지 않았으므로 허가사항을 직접 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 점수는 매우 높지만(99.65%) 임상시험과 문헌 근거가 전혀 없고, 나트륨 채널 억제와 V2 수용체/AQP2 경로 사이의 기전적 연결도 확립되어 있지 않습니다. 또한 신장질환이 지식 그래프상 금기로 나타나 있어 현 단계에서는 진행을 보류합니다.

**진행하려면 필요한 것:**
- 허가 적응증 및 경고·금기 문구 확인 (MFDS 허가사항 PDF 내려받아 분석)
- 상세한 작용 기전(MOA) 데이터 확보 (DrugBank 조회)
- Ranolazine과 V2 수용체 신호전달/AQP2 이동 간의 연관성을 검증하는 전임상 연구
- 신장 기능 저하 환자 및 QT 연장 위험에 대한 안전성 평가
- 투여 경로 적합성 평가 (현재 미확인)
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

