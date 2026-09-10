---
layout: default
title: Pretomanid
parent: 僅模型預測 (L5)
nav_order: 575
evidence_level: L5
indication_count: 10
---

# Pretomanid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Pretomanid: 결핵(다제내성/광범위약제내성)에서 칸디다증으로

## 한 문장 요약

Pretomanid는 니트로이미다졸계 전구약물로, 문헌상 BPaL/BPaLM 요법(bedaquiline+pretomanid+linezolid±moxifloxacin)의 일부로 다제내성(MDR)·광범위약제내성(XDR) 결핵 치료에 사용되는 것으로 확인됩니다(공식 MOA·적응증 필드는 데이터 부재).
TxGNN 모델은 **칸디다증(Candidiasis)**에 효과가 있을 수 있다고 예측했으나, 이를 뒷받침하는 **임상시험은 0건, 문헌은 0편**이며, 제공된 기전 분석 자체가 생물학적 연관성이 없다고 명시하고 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (문헌 기준 다제내성/광범위약제내성 결핵, BPaL·BPaLM 요법의 일부로 확인) |
| 예측 신규 적응증 | 칸디다증 (Candidiasis) |
| TxGNN 예측 점수 | 99.69% |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터는 확보되지 않았습니다(Data Gap, High severity). 다만 임상시험·문헌 데이터를 통해 확인되는 바로는, Pretomanid는 결핵균(M. tuberculosis) 특이적인 Ddn 탈질소황색소 의존형 질산환원효소 시스템을 통해 활성화되어 분枝균산(mycolic acid) 합성을 억제하는 항결핵 전구약물입니다.

칸디다증은 진균(Candida) 세포벽/세포막을 표적으로 하는 항진균제 기전이 필요한 질환으로, Pretomanid의 분枝균 특이적 활성화 경로와는 생물학적 접점이 없습니다. 제공된 기전 근거(repurposing_rationale)도 "Ddn 질산환원효소 시스템과 분枝균산 합성 억제는 칸디다(진균) 세포벽/막 표적과 생물학적 연관성이 없으며, 이를 뒷받침하는 증거가 전혀 없다"고 명시하고 있어, 이 예측은 지식그래프 임베딩 상의 통계적 유사성에 의한 결과일 가능성이 높습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. (주요 경고, 금기, 약물상호작용 자료는 현재 확보되지 않았으며, TFDA 수준 자료 확보가 Blocking 등급 데이터 갭으로 분류되어 있습니다.)

## 결론 및 다음 단계

**결정: Hold**

**사유:**
1위 예측 적응증인 칸디다증은 임상시험 0건, 문헌 0편으로 뒷받침되지 않으며, 제공된 기전 분석 자체가 생물학적 타당성을 명시적으로 부정하고 있어 지식그래프 임베딩의 통계적 인공물(artifact)로 판단됩니다. 참고로 2~10순위 예측(나병, 관상동맥질환, 심근허혈, HIV, 구강칸디다증, Bacteroidaceae 감염, 혈소판감소증, 간질증)도 모두 근거 수준 L4~L5이며, 그중 나병은 직접적인 반증 문헌(M. leprae의 PA-824 천연 내성)이 존재하고, HIV·혈소판감소증 관련 근거는 실제로는 기존 결핵 적응증의 병용요법·부작용 데이터가 지식그래프 공출현으로 오분류된 사례로 확인됩니다. 즉 이번 예측 세트 전체에서 진행 가능한 수준의 근거를 가진 후보가 없습니다.

**진행하려면 필요한 것:**
- TFDA(식약처 해당 기관) 허가사항 원문 확보 및 경고/금기 사항 파싱 (DG001, Blocking)
- DrugBank API를 통한 상세 작용 기전(MOA) 데이터 확보 (DG002, High)
- 칸디다증 관련 실제 전임상(in vitro/in vivo) 데이터 발생 시 재평가
- 현재 상태에서는 추가 임상 개발 자원 투입을 권장하지 않음
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

