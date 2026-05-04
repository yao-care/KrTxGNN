---
layout: default
title: Rozanolixizumab
parent: 僅模型預測 (L5)
nav_order: 296
evidence_level: L5
indication_count: 10
---

# Rozanolixizumab
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

# Rozanolixizumab: IgG 자가면역질환(해외 허가)에서 기관지염으로

## 한 문장 요약

Rozanolixizumab은 FcRn(신생아 Fc 수용체)을 차단하여 병인성 IgG 자가항체를 감소시키는 단클론항체로, 해외에서 중증 근무력증(gMG) 등 IgG 매개 자가면역질환 치료제로 허가되어 있습니다.
TxGNN 모델은 **기관지염(Bronchitis)**을 최우선 예측 적응증으로 제시하나, 이를 지지하는 **임상시험 및 문헌이 전혀 없으며** 기전 연관성도 낮습니다.
상위 10개 예측 적응증 모두 근거 수준 L5 · Hold 판정이며, 한국에는 아직 미허가 약물입니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 한국 미허가 (해외: 중증 근무력증, 원발면역혈소판감소증) |
| 예측 신규 적응증 | 기관지염 (Bronchitis) |
| TxGNN 예측 점수 | 95.28% |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미상시 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터(MOA)가 수집되지 않았습니다. 그러나 Evidence Pack의 기전 분석 메모에 따르면, Rozanolixizumab은 **FcRn(neonatal Fc receptor)을 차단하는 단클론항체**입니다. FcRn은 세포 내로 흡수된 IgG를 분해로부터 보호해 혈중으로 되돌려 보내는 역할을 합니다. Rozanolixizumab이 FcRn을 차단하면 IgG 반감기가 단축되어 병인성 자가항체(anti-AChR, anti-MuSK 등) 농도가 낮아지며, 이것이 중증 근무력증(gMG)이나 원발면역혈소판감소증(ITP) 같은 IgG 매개 자가면역질환에서의 치료 원리입니다.

기관지염은 주로 바이러스 감염 또는 공기 오염으로 발생하며, 급성기는 선천면역·호중구 반응, 만성기는 기도 재형성이 핵심 병리입니다. **IgG 자가항체가 기관지염의 주된 병인이 아니므로**, anti-FcRn 기전을 기관지염 치료에 적용할 논리적 근거가 부족합니다. 오히려 IgG 전반이 감소하면 호흡기 감염에 대한 방어력이 저하될 위험이 있습니다.

상위 10개 예측 적응증(골수종·지중해빈혈·위암·효소 결핍증·염색체 이상 등)을 종합하면, FcRn 차단 기전과 직접 연결되는 IgG 자가면역질환이 단 하나도 포함되어 있지 않습니다. 이는 TxGNN 모델이 Rozanolixizumab의 실제 허가 적응증(자가면역) 학습 데이터가 충분하지 않아, 기전과 무관한 방향으로 예측이 집중된 사례로 판단됩니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 관련 문헌이 없습니다.

---

## 한국 시판 정보

Rozanolixizumab은 현재 한국에서 허가된 제품이 없습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN이 기관지염을 최우선 예측 적응증으로 제시했으나, anti-FcRn 기전과 기관지염의 병인 사이에 직접적 연결고리가 없고, 이를 지지하는 임상시험·문헌이 전혀 존재하지 않습니다. 상위 10개 예측 적응증 전체가 동일하게 기전 연관성 낮음(L5) · Hold 판정으로, 현재 시점에서 Rozanolixizumab의 재창출 가능성을 평가하기 위한 기초 데이터가 부족합니다.

**진행하려면 필요한 것:**
- DrugBank MOA 및 TFDA/MFDS 허가사항 데이터 수집 (현재 Blocking 데이터 갭)
- 실제 허가 적응증(중증 근무력증, ITP 등 IgG 자가면역질환)을 기준으로 TxGNN 예측 결과 재평가
- CIDP(만성 염증성 탈수초 다발신경병증), 수포성 유천포창, WAIHA(온난항체자가면역용혈빈혈) 등 IgG 매개 질환 대상 별도 재창출 탐색 권장
- 한국 MFDS 허가 추진 시 해외 허가 근거(FDA/EMA) 및 임상 데이터 패키지 확보
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

