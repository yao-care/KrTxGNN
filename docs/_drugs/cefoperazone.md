---
layout: default
title: Cefoperazone
parent: 모델 예측만 (L5)
nav_order: 190
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Cefoperazone: 예측 신규 적응증 경화성 담관염 (Sclerosing Cholangitis) (근거 수준 L5). 기존 적응증: 세균 감염증 (허가 문서 본문이 확인되지 않아 항생제 계열 기준으로 기재)"
monitor_inn: "Cefoperazone"
predicted_indications: ["sclerosing cholangitis", "rheumatoid arthritis", "pneumonia", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "gout", "bronchitis", "meningococcal infection", "infectious otitis media", "IgG4-related sclerosing cholangitis"]
---

# Cefoperazone
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
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

# Cefoperazone: 세균 감염증에서 경화성 담관염으로

## 한 문장 요약

Cefoperazone은 3세대 세팔로스포린계 주사용 항생제로, 원래 세균 감염증 치료에 사용되어 왔습니다.
TxGNN 모델은 **경화성 담관염(Sclerosing Cholangitis)**에 효과가 있을 수 있다고 예측하지만, 현재 이 방향을 지지하는 **임상시험은 0건, 문헌도 0편**입니다.
모델 점수만 높을 뿐 실제 근거가 없어, 이 예측은 보류(Hold)를 권장합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 세균 감염증 (허가 문서 본문이 확인되지 않아 항생제 계열 기준으로 기재) |
| 예측 신규 적응증 | 경화성 담관염 (Sclerosing Cholangitis) |
| TxGNN 예측 점수 | 99.98% (전체 순위 743위) |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 19건 (모두 유효) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 없습니다. 알려진 정보에 따르면 Cefoperazone은 베타락탐계 항생제로, 세균 세포벽 합성을 억제하여 그람음성균(녹농균 포함)을 포함한 넓은 범위의 세균에 작용합니다. 설박탐과의 복합제로도 허가되어 있습니다.

경화성 담관염과 연결될 수 있는 점은 Cefoperazone이 담즙으로 상당량 배설된다는 것입니다. 또 항생제는 담관염 급성 악화 시 감염 관리에 쓰일 수 있습니다. 그러나 이는 질환 자체를 치료하는 효과가 아니라 합병 감염을 관리하는 것입니다. 이 배설 특성이 경화성 담관염의 경과를 개선한다는 근거도 제시된 자료에 없습니다. 따라서 기전상 타당성은 뒷받침되지 않으며, 그래프 기반 예측의 한계를 반영한 결과일 가능성이 있습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

허가 적응증 본문은 확인되지 않았고 허가 문서 링크만 확인되었습니다. 상당수가 수출용 허가입니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 199700538 | 페라탐주 (설박탐나트륨·세포페라존나트륨) | 바이알제 (결정성 분말) | [허가 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199700538/EE) 참조 |
| 199701650 | 세포라탐주사 (설박탐나트륨·세포페라존나트륨) | 바이알 주사제 | [허가 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199701650/EE) 참조 |
| 201600616 | 페라탐주2그램 (설박탐나트륨·세포페라존나트륨) | 용시 용해 주사제 | [허가 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201600616/EE) 참조 |
| 200202759 | 세포페론주1그람 (수출용) | 바이알 | [허가 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200202759/EE) 참조 |
| 200400461 | 대웅세포페라존주1g (수출용) | 바이알제 | [허가 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200400461/EE) 참조 |

## 안전성 고려사항

**약물 상호작용**: 14건이 확인되었으며 모두 중등도(Moderate)입니다.
- **아미노글리코사이드계**: Kanamycin, Neomycin, Streptomycin, Amikacin(리포솜 제형 포함), Gentamicin
- **항응고제**: Warfarin, Heparin
- **기타**: Ethanol, Chloramphenicol, Ethinylestradiol, Mycophenolic acid, Pemetrexed, Picosulfuric acid

Ethanol과는 disulfiram 유사 반응 위험이 있고, 항응고제와는 응고 이상 위험이 있어 주의가 필요합니다.

경고 및 금기 사항은 허가사항을 참조하세요.

## 다른 예측 적응증 참고

TxGNN 상위 10개 예측 중 근거가 있는 항목은 대부분 이미 확립된 감염증 영역입니다. 진정한 의미의 재창출이라기보다 기존 사용의 연장입니다.

| 예측 적응증 | 근거 수준 | 평가 | 비고 |
|-----------|---------|------|------|
| 폐렴 | L1 | Proceed with Guardrails | 임상시험 2건, 문헌 20편. Cefoperazone-sulbactam vs cefepime 비열등성 RCT(2019) 등이 있으나 대체로 기존 사용에 가까움. 내성 양상, 항생제 적정 사용, DDI 주의 필요 |
| 기관지염 | L2 | Research Question | 1980년대 다기관 임상 연구 중심. 비세균성 가능성 고려 필요 |
| 수막구균 감염 | L3 | Research Question | 소규모 예비 보고 1건. CNS 투과성이 ceftriaxone/cefotaxime보다 낮음 |
| 감염성 중이염 | L4 | Research Question | 간접 근거만 있음 |
| 류마티스 관절염, 통풍, IgG4 관련 경화성 담관염 등 | L5 | Hold | 기전 근거 없음 |

## 결론 및 다음 단계

**결정: Hold**

**사유:**
1순위 예측인 경화성 담관염은 모델 점수(99.98%)만 높고 임상시험과 문헌이 전혀 없으며, 기전상 연결고리도 질환 치료와 무관한 담즙 배설 특성뿐입니다. 근거 수준이 L5이므로 현 단계에서는 개발을 진행하기 어렵습니다.

**진행하려면 필요한 것:**
- 경화성 담관염에서 Cefoperazone의 효과를 뒷받침하는 전임상 또는 임상 근거
- 상세한 약물 작용 기전(MOA) 데이터 확보
- 허가사항(경고·금기)의 확인 및 안전성 검토
- 근거가 상대적으로 충분한 폐렴(감염증) 쪽을 우선 검토하는 방안(내성 양상 및 DDI 가드레일 전제)
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

