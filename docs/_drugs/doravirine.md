---
layout: default
title: Doravirine
parent: 僅模型預測 (L5)
nav_order: 229
evidence_level: L5
indication_count: 3
---

# Doravirine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Doravirine: HIV-1 감염에서 유인원 면역결핍 바이러스 감염으로

## 한 문장 요약

Doravirine은 비뉴클레오시드 역전사효소 억제제(NNRTI) 계열의 항바이러스제로, HIV-1 감염 치료에 사용됩니다.
TxGNN 모델은 **유인원 면역결핍 바이러스 감염(Simian Immunodeficiency Virus Infection)**에 효과가 있을 수 있다고 예측하나, 현재 **임상시험 0건**, 직접 관련 **문헌 0편** (간접 연관 문헌 1편)으로 근거가 매우 제한적입니다.
이 예측은 바이러스 계통발생학적 유사성에 근거한 것으로, 기전적 타당성에 중요한 한계가 있어 신중한 평가가 필요합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | HIV-1 감염 치료 (NNRTI 계열; 국내 허가 데이터 미등록) |
| 예측 신규 적응증 | 유인원 면역결핍 바이러스 감염 (Simian Immunodeficiency Virus Infection) |
| TxGNN 예측 점수 | 99.93% |
| 근거 수준 | L4 |
| 한국 시판 현황 | 미판매 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

Doravirine은 3세대 NNRTI로, HIV-1 역전사효소(RT) p66 아단위의 비뉴클레오시드 결합 주머니(NNIBP)에 결합하여 바이러스 복제를 억제합니다. HIV-1과 SIV는 동일한 렌티바이러스과(Lentivirus family)에 속하며 계통발생학적으로 가깝습니다. TxGNN 모델은 이 계통발생학적 근접성을 근거로 높은 예측 점수(99.93%)를 부여한 것으로 판단됩니다.

그러나 기전적 측면에서 결정적인 한계가 존재합니다. SIV의 역전사효소는 NNIBP 내 핵심 방향족 잔기 배열(특히 Y181, Y188 위치)이 HIV-1 RT와 구조적으로 다릅니다. 이로 인해 1세대(nevirapine), 2세대(efavirenz, etravirine)에 이어 3세대 NNRTI를 포함한 대부분의 NNRTI가 SIV에 대한 활성을 갖지 않는다는 사실이 문헌으로 확인되어 있습니다. TxGNN의 고점수는 확인된 약리 활성이 아닌 계통발생학적 근접성을 반영할 가능성이 높으며, 이는 모델의 잠재적 가양성(false positive) 사례입니다.

임상적 적용 가능성도 극히 제한됩니다. SIV 감염은 주로 비인간 영장류(NHP)에서 발생하는 동물 질환으로, HIV/AIDS 연구의 동물 모델로 활용됩니다. 인간에게 직접 적용되는 임상 시나리오는 극히 드물어 약물 재창출의 실질적 의의가 매우 낮습니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [31658118](https://pubmed.ncbi.nlm.nih.gov/31658118/) | 2020 | Review/전임상 | Current Opinion in HIV and AIDS | Islatravir(역전사효소 전위 억제제, NRTTI)의 HIV-1 치료·예방 가능성 검토. Doravirine과는 별개 약물로, SIV에 대한 Doravirine 활성을 직접 지지하는 근거로 활용하기 어려움 |

> ⚠️ **주의**: 위 문헌은 Doravirine이 아닌 Islatravir를 다루고 있습니다. 검색 결과가 반환된 것은 두 약물이 모두 HIV-1 RT 억제제이기 때문으로 보이며, 이 예측에 대한 직접 근거로 보기 어렵습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
Doravirine의 NNRTI 기전은 SIV RT의 NNIBP 구조적 차이로 인해 활성을 기대하기 어렵고, SIV 감염은 인간 임상 적용 가능성이 극히 낮은 동물 질환입니다. 직접 관련 임상시험 및 문헌 근거가 전무하며, 유일하게 검색된 문헌도 별개 약물(Islatravir)에 관한 것입니다. 3개의 예측 적응증 모두(SIV 감염 L4, 고양이 면역결핍증후군 L5, 신경발달장애 L5) 현 시점에서 Hold 권고에 해당합니다.

**진행하려면 필요한 것:**
- Doravirine 상세 MOA 데이터 확보 (DrugBank API 조회, 현재 데이터 갭)
- 안전성 데이터 확보 (허가기관 허가사항 PDF 파싱, 현재 차단 수준 데이터 갭)
- SIV RT에 대한 in vitro 결합 활성 데이터 (전임상 근거 부재 확인 필요)
- 보다 임상적으로 의미 있는 적응증 재탐색 권고 (예: HIV-1의 다른 합병증, 내성 변이주 대응 등)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

