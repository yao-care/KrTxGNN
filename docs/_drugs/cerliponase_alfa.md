---
layout: default
title: Cerliponase Alfa
parent: 모델 예측만 (L5)
nav_order: 202
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Cerliponase Alfa: 예측 신규 적응증 Scheie 증후군 (Scheie syndrome, MPS I 완화형) (근거 수준 L5). 기존 적응증: 허가 적응증 본문은 링크로만 제공되어 구체적 내용을 확인할 수 없습니다 (허가 문서 참조)"
monitor_inn: "Cerliponase alfa"
predicted_indications: ["Scheie syndrome", "Hurler syndrome", "lysosomal storage disease with skeletal involvement", "cholesteryl ester storage disease", "Gaucher disease", "familial encephalopathy with neuroserpin inclusion bodies", "Wolman disease with hypolipoproteinemia and acanthocytosis", "myoclonic epilepsy, juvenile, susceptibility to", "proximal myopathy with extrapyramidal signs", "autosomal ichthyosis syndrome with fatal disease course"]
---

# Cerliponase Alfa
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

## Cerliponase alfa: 기존 적응증 미확인에서 Scheie 증후군으로
{: .text-alpha }

## 한 문장 요약

Cerliponase alfa는 재조합 인간 TPP1(tripeptidyl peptidase 1) 효소를 뇌실 내로 투여하는 효소대체요법제로, 한국에서 허가되어 시판 중입니다. TxGNN 모델은 **Scheie 증후군(Scheie syndrome)**에 효과가 있을 수 있다고 예측하지만, 이 예측을 직접 뒷받침하는 **임상시험은 0건, 문헌도 0편**입니다. 모델 예측만 있는 L5 수준이므로 현 단계에서는 보류(Hold)를 권장합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문은 링크로만 제공되어 구체적 내용을 확인할 수 없습니다 (허가 문서 참조) |
| 예측 신규 적응증 | Scheie 증후군 (Scheie syndrome, MPS I 완화형) |
| TxGNN 예측 점수 | 99.98% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 수집되지 않았습니다. 다만 이 약은 CLN2 질환(TPP1 결핍)에 대해 뇌실 내 투여하는 재조합 TPP1 효소대체요법제로 알려져 있습니다.

Scheie 증후군은 알파-L-이두로니다제(alpha-L-iduronidase) 결핍으로 생기는 MPS I의 완화형입니다. 두 질환 모두 리소좀 저장 질환이라는 점에서 지식 그래프상 가까이 위치하여 점수가 높게 나온 것으로 보입니다. 그러나 TPP1은 글리코사미노글리칸을 분해하지 않으므로 **직접적인 기전상 근거는 없습니다.** 또한 MPS I의 전신 증상은 뇌실 내 투여로는 해결되기 어렵습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202006239 | 브리뉴라주150mg(세르리포나제알파) | 2종 바이알 구성 (약제 바이알: 투명~약간 유백색, 무색~옅은 노란색 용액 / 관류세척용액 바이알: 투명 무색 용액) | 허가 문서 링크로만 제공되어 요약 불가 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
Scheie 증후군에 대한 임상시험과 문헌 근거가 전혀 없고, TPP1이 MPS I의 원인 효소(알파-L-이두로니다제)와 다르기 때문에 기전상 근거도 없습니다. 높은 TxGNN 점수는 리소좀 질환군 내 그래프 근접성을 반영한 것으로 보입니다. 이 질환에는 이미 라로니다제(laronidase)와 조혈모세포이식 같은 대안도 있습니다.

**진행하려면 필요한 것:**
- 허가사항 원문(적응증, 경고, 금기)을 확보하여 안전성 검토
- 상세한 약물 작용 기전(MOA) 데이터 확보
- TPP1이 MPS I 병태에 영향을 줄 수 있다는 전임상·기전 근거
- 뇌실 내 투여 경로와 MPS I의 전신 증상 사이의 투여 경로 적합성 평가

## 참고: 기타 예측 적응증

상위 10개 예측(Hurler 증후군, 골격 침범 리소좀 저장 질환, 콜레스테롤에스테르 저장병, Gaucher병 등)도 모두 L5 수준이며 Hold입니다. 대부분 효소와 기질이 달라 기전상 연결이 없고, 지지하는 임상시험도 없습니다. Gaucher병에서 검색된 문헌 1편(PMID 41527340, 2026)은 리소좀 질환의 자연경과를 다룬 리뷰로, 이 약의 사용을 뒷받침하지 않습니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

