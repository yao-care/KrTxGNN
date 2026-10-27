---
layout: default
title: Telbivudine
parent: 모델 예측만 (L5)
nav_order: 720
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Telbivudine: 예측 신규 적응증 만성 C형 간염 바이러스 감염 (chronic hepatitis C virus infection) (근거 수준 L5). 기존 적응증: 만성 B형 간염 (허가증의 적응증 원문은 링크로만 제공되어 문헌에 기재된 허가 용도를 기준으로 함)"
monitor_inn: "TELBIVUDINE"
predicted_indications: ["chronic hepatitis C virus infection", "HIV infectious disease", "hepatitis C virus infection", "disorder of phenylalanine metabolism", "disorder of tyrosine metabolism", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "tetrahydrobiopterin-responsive hyperphenylalaninemia/phenylketonuria"]
---

# Telbivudine
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

## 텔비부딘(Telbivudine): 만성 B형 간염에서 만성 C형 간염으로
{: .text-alpha }

## 한 문장 요약

텔비부딘은 B형 간염 바이러스(HBV)의 DNA 중합효소를 억제하는 뉴클레오시드 유사체로, 원래 만성 B형 간염 치료에 사용되었습니다.
TxGNN 모델은 **만성 C형 간염 바이러스 감염(chronic hepatitis C virus infection)**에 효과가 있을 수 있다고 예측합니다. 그러나 **임상시험은 0건**이고, 문헌 6편은 B형·C형 간염을 함께 다룬 총설이 대부분이어서 텔비부딘의 항HCV 효과를 직접 뒷받침하는 근거는 없습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 만성 B형 간염 (허가증의 적응증 원문은 링크로만 제공되어 문헌에 기재된 허가 용도를 기준으로 함) |
| 예측 신규 적응증 | 만성 C형 간염 바이러스 감염 (chronic hepatitis C virus infection) |
| TxGNN 예측 점수 | 99.96% |
| 근거 수준 | L5 (모델 예측만 있고 텔비부딘의 HCV 효과를 직접 다룬 연구 없음) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

텔비부딘은 천연 티미딘의 L-거울상 이성질체인 합성 뉴클레오시드 유사체입니다. 체내에서 활성형인 삼인산 형태로 인산화된 뒤 HBV DNA 중합효소(역전사효소)를 경쟁적으로 억제하여 DNA 사슬 연장을 중단시킵니다. 현재 상세한 작용 기전 데이터는 별도로 확보되지 않았으며, 위 설명은 문헌에 기재된 일반적인 기전입니다.

모델이 B형 간염과 C형 간염을 연결한 것은 둘 다 간을 침범하는 바이러스 감염이고, 문헌에서 함께 언급되는 경우가 많기 때문으로 보입니다. 그러나 HCV는 RNA 바이러스이며 치료 표적은 NS5B RNA 의존성 RNA 중합효소입니다. 텔비부딘은 HBV DNA 중합효소에 특이적이어서 이 표적에 작용한다는 근거가 없습니다. 따라서 높은 점수는 두 질환이 지식 그래프에서 함께 나타난 데서 비롯된 결과로 해석하는 것이 합리적이며, 기전상 타당성은 낮습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [25233195](https://pubmed.ncbi.nlm.nih.gov/25233195/) | 2014 | Review | Journal of Perinatology | 임신 중 B형·C형 간염의 영향과 모자 감염 감소 전략 고찰 (텔비부딘 직접 언급 없음) |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterologica e Dietologica | B형·C형 간염 항바이러스제(텔비부딘 포함)와 신기능에 미치는 영향 |
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | Review | Wiener Medizinische Wochenschrift | 만성 B형·C형 간염의 현재 치료와 향후 전망 |
| [18340426](https://pubmed.ncbi.nlm.nih.gov/18340426/) | 2008 | Review | Der Internist | 독일 지침에 따른 B형·C형 간염 항바이러스 치료 권고 (B형 간염에서 텔비부딘은 대체 단독요법 후보로 언급) |
| [21999649](https://pubmed.ncbi.nlm.nih.gov/21999649/) | 2011 | Review | Paediatric Drugs | 소아 만성 간질환의 내과적 관리 |
| [23697556](https://pubmed.ncbi.nlm.nih.gov/23697556/) | 2013 | Cohort | Journal of Interferon & Cytokine Research | 텔비부딘 치료 중인 만성 B형 간염 환자의 혈청 IL-37 농도와 HBeAg 혈청전환 관련성 (HCV 아님) |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200611515 | 세비보정(텔비부딘) (부광약품) | 미황색 타원형 필름코팅정 (한쪽 면에 'LDT' 각인) | 허가증 원문 참조 (https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200611515/EE) |

## 안전성 고려사항

- **약물 상호작용**: 총 96건이 확인되었습니다. 이 중 보고서에 수집된 20건은 모두 중등도(Moderate)입니다.
  - 코르티코스테로이드: 하이드로코르티손, 트리암시놀론, 덱사메타손, 베타메타손, 부데소니드, 프레드니손
  - 항진균제·항생제: 암포테리신 B(지질 복합체, 콜레스테릴 황산염 제형 포함), 반코마이신, 카나마이신, 네오마이신, 메트로니다졸
  - 아미노살리실산 계열: 메살라진, 발살라자이드, 올살라진, 설파살라진
  - 지질 관련 약물: 로수바스타틴, 심바스타틴, 오르리스타트
- **지식 그래프 기반 금기 질환**(허가사항 원문이 아닌 모델 지식 그래프 기준): 신장 질환, 근병증·근육 질환, 가족성 주기성 마비, 말초신경병증, 지방간 질환, 비알코올성 지방간염, 젖산산증, 피부근염·근염 등이 포함됩니다.
- **임상적 주의**: HBV 치료 맥락에서는 근병증, 말초신경병증, CK 상승 위험이 알려져 있습니다. 페그인터페론 알파-2a와의 병용은 말초신경병증 위험 때문에 금기입니다.

그 밖의 경고 및 금기 사항은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
C형 간염에 대한 임상시험이 없고, 문헌도 텔비부딘의 항HCV 활성을 보여주지 못합니다. 약물 표적(HBV DNA 중합효소)이 HCV의 표적(NS5B)과 달라 기전상 근거도 약합니다. 높은 예측 점수는 지식 그래프의 B형·C형 간염 동시 출현에서 비롯된 결과로 판단됩니다. 참고로 B형 간염은 이미 허가된 용도이므로 재창출 대상이 아닙니다.

**진행하려면 필요한 것:**
- HCV 복제 모델(레플리콘 등)에서 텔비부딘의 항바이러스 활성을 확인하는 전임상 데이터
- 상세한 약물 작용 기전(MOA) 데이터 확보
- 허가증 원문(PDF)에서 허가 적응증, 경고, 금기 사항을 추출하여 안전성 검토
- HCV에는 이미 직접작용 항바이러스제(DAA)가 확립되어 있으므로, 이들과 비교한 임상적 필요성 평가
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

