---
layout: default
title: Prednisolone Acetate
parent: 모델 예측만 (L5)
nav_order: 625
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Prednisolone Acetate: 예측 신규 적응증 기생충성 결막염 (Parasitic Conjunctivitis) (근거 수준 L5). 기존 적응증: 치열·치핵의 아픔, 가려움, 부종(부기), 출혈의 일시적 완화"
monitor_inn: "PREDNISOLONE ACETATE"
predicted_indications: ["parasitic conjunctivitis", "chronic follicular conjunctivitis", "serous conjunctivitis except viral", "conjunctival folliculosis", "papillary conjunctivitis", "Angelucci syndrome", "pseudomembranous conjunctivitis", "acute hemorrhagic conjunctivitis", "vernal conjunctivitis", "postinfectious vasculitis"]
---

# Prednisolone Acetate
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

# Prednisolone Acetate: 치열·치핵 및 안과 염증에서 기생충성 결막염으로

## 한 문장 요약

Prednisolone Acetate는 합성 부신피질호르몬(글루코코르티코이드)으로, 한국에서 점안액과 치열·치핵 완화용 크림 등으로 허가되어 사용되고 있습니다.
TxGNN 모델은 **기생충성 결막염(Parasitic Conjunctivitis)**에 효과가 있을 수 있다고 예측하지만, 이 예측을 직접 지지하는 임상시험과 문헌은 **0건**입니다.
다만 순위가 낮은 다른 결막염 계열 예측 중 일부(유두성 결막염, 봄철 결막염 등)는 간접 근거가 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 치열·치핵의 아픔, 가려움, 부종(부기), 출혈의 일시적 완화 |
| 예측 신규 적응증 | 기생충성 결막염 (Parasitic Conjunctivitis) |
| TxGNN 예측 점수 | 99.74% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 16건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Prednisolone Acetate는 글루코코르티코이드 계열로 염증 반응을 억제하는 약물이며, 한국에서는 점안액, 주사제, 크림 등 여러 제형으로 허가되어 있습니다. 따라서 결막의 염증성 질환에도 기전상 적용 가능할 수 있습니다.

다만 기생충성 결막염은 감염이 원인이므로, 스테로이드는 기껏해야 보조 요법입니다. 항기생충 치료 없이 사용하면 감염을 악화시킬 수 있습니다. 즉 모델 점수는 매우 높지만, 임상적 타당성은 제한적입니다.

TxGNN 상위 10개 예측은 대부분 결막염 계열입니다. 이 중 **유두성 결막염**과 **봄철 결막염(vernal conjunctivitis)**은 알레르기·면역 매개 염증이라 스테로이드의 기전적 연관성이 상대적으로 강합니다. 반면 급성 출혈성 결막염(바이러스성)이나 결막 여포증(대개 양성, 자연 소실)은 이득이 불분명합니다.

## 임상시험 근거

1순위 예측인 기생충성 결막염과 관련된 임상시험 등록은 현재 없습니다.

참고로, 같은 결막염 계열의 다른 예측 질환에 대해 확인된 시험은 다음과 같습니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT04705584](https://clinicaltrials.gov/study/NCT04705584) | 해당 없음(NA) | 불명 | 180 | 봄철 결막염에서 Cyclosporine A 2% vs Tacrolimus 0.3% 비교. 스테로이드 대체 요법 평가이며, Prednisolone Acetate가 비교군인지는 불분명 |
| [NCT01437982](https://clinicaltrials.gov/study/NCT01437982) | Phase 4 | 완료 | 140 | 유두성 결막염 예측과 연관. Loteprednol(다른 스테로이드) 시판 후 안전성 조사로, Prednisolone Acetate 직접 근거 아님 |

## 문헌 근거

1순위 예측(기생충성 결막염)에 대한 문헌은 없습니다. 아래는 다른 결막염 예측에 대한 문헌 중 Prednisolone Acetate와 관련성이 높은 것들입니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [24055903](https://pubmed.ncbi.nlm.nih.gov/24055903/) | 2013 | 비교 임상연구 | Cornea | 실험적 알레르기 결막염 모델에서 Cyclosporine A, Epinastine, Prednisolone Acetate 1%의 효과 비교 (봄철 결막염) |
| [12931748](https://pubmed.ncbi.nlm.nih.gov/12931748/) | 2003 | 코호트 | Asian Pac J Allergy Immunol | 태국 봄철 각결막염 환자에서 중증 시 국소 스테로이드 사용 및 치료 결과 |
| [26984315](https://pubmed.ncbi.nlm.nih.gov/26984315/) | 2016 | Review | Advances in Therapy | 국소 안과용 스테로이드(Loteprednol)의 안압 영향 |
| [32621983](https://pubmed.ncbi.nlm.nih.gov/32621983/) | 2020 | 증례 보고 | J AAPOS | 마이코플라스마 연관 점막염·위막성 결막염에서 Prednisolone Acetate 점안 병용 치료 |
| [21434554](https://pubmed.ncbi.nlm.nih.gov/21434554/) | 2011 | 증례 보고 | Indian J Tuberc | 알레르기 결막염으로 오진된 결막 결핵. Prednisolone Acetate 1% 투여에도 호전 없음 |
| [15523196](https://pubmed.ncbi.nlm.nih.gov/15523196/) | 2004 | Review | Curr Opin Ophthalmol | 이식편대숙주병의 안구 증상과 치료 (위막성 결막염 예측 관련) |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 199504099 | 프레드포르테점안액 | 백색의 현탁성 점안액 | 허가사항 참조 |
| 201905235 | 포르텐점안액 | 흰색의 현탁성 점안액 | 허가사항 참조 |
| 201802749 | 프레드벨1%점안액 (1회용) | 흰색의 현탁성 점안액 | 허가사항 참조 |
| 201901128 | 치치엔더블유크림 | 크림제 | 치열·치핵의 아픔, 가려움, 부종(부기), 출혈의 일시적 완화 |
| 201904220 | 한미치쏙크림 | 크림제 | 치열·치핵의 아픔·가려움·부종(부기)·출혈의 일시적 완화 |

이 외에 점안액 다수(프레드니론, 프레드에프, 프레드루체, 옵티프레디 등), 수출용 점안액·주사제, 주입크림(래반포르테) 등이 허가되어 있습니다.

## 안전성 고려사항

- **금기 질환(지식 그래프 기반, 허가 문구 아님)**: 헤르페스 단순 바이러스 각막염, 개방각 녹내장, 고안압증, 안구 감염(바이러스성·진균성·결핵성), 결막염, 당뇨병, 당뇨병성 케톤산증, 포르피린증, G6PD 결핍 등이 보고되어 있습니다.
- **예측 적응증 관련 우려**: 국소 스테로이드는 안압 상승, 백내장, 이차 감염 위험이 있습니다. 감염성 결막염(기생충성, 바이러스성)에서는 감염 악화 가능성이 있습니다.

그 외 상세 안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
1순위 예측인 기생충성 결막염은 TxGNN 점수(99.74%)만 있고 임상시험과 문헌이 전혀 없는 L5 단계입니다. 또한 감염성 질환이므로 스테로이드 단독 사용 시 오히려 악화 위험이 있습니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기) 확보 및 작용 기전 데이터 보완
- 기생충성 결막염에서 항기생충 치료와 병용한 스테로이드 사용 근거 조사
- 대안 검토: 알레르기·면역 매개 질환인 **봄철 결막염**(L4, 연구 질문 단계)과 **유두성 결막염**(L4)은 기전적 연관성이 더 강하므로, Prednisolone Acetate 직접 비교 근거를 수집해 우선 평가할 가치가 있음
- 안압 상승, 백내장, 이차 감염에 대한 안전성 모니터링 계획
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

