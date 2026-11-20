---
layout: default
title: Atracurium Besylate
parent: 모델 예측만 (L5)
nav_order: 102
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-15
description: "Atracurium Besylate: 예측 신규 적응증 자간전증 (Preeclampsia) (근거 수준 L5). 기존 적응증: 1.마취시 근이완 2.기관내 삽관시 근이완 유지 3.기계적 조절호흡 용이 4.수술시 근이완"
monitor_inn: "Atracurium besylate"
predicted_indications: ["preeclampsia", "cauda equina syndrome", "blepharospasm", "migraine disorder", "obsolete neurogenic bladder (disease)", "thrombotic disease", "migraine with brainstem aura", "severe pre-eclampsia", "mild pre-eclampsia", "irritable bowel syndrome"]
---

# Atracurium Besylate
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

## Atracurium besylate: 근이완(신경근 차단)에서 자간전증으로
{: .text-alpha }

## 한 문장 요약

Atracurium besylate는 비탈분극성 신경근 차단제로, 한국에서는 주사제로 허가되어 있습니다.
TxGNN 모델은 **자간전증(preeclampsia)**에 효과가 있을 수 있다고 예측하지만,
현재 이를 뒷받침하는 **임상시험은 0건**, **문헌도 0편**이어서 모델 예측만 있는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 1.마취시 근이완 2.기관내 삽관시 근이완 유지 3.기계적 조절호흡 용이 4.수술시 근이완 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200703106/EE)) |
| 예측 신규 적응증 | 자간전증 (Preeclampsia) |
| TxGNN 예측 점수 | 0.9997 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 3건 / 전체 4건) |
| 허가증 수 | 4건 (유효 3건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Atracurium Besylate 처방 정보(Prescribing Information)의 “Clinical Pharmacology” 항목에 따르면(비공식 번역): “아트라쿠리움 베실산염은 비탈분극성 골격근 이완제이다. 비탈분극성 제제는 운동종판의 콜린성 수용체 부위에 경쟁적으로 결합하여 신경전달물질인 아세틸콜린의 작용을 길항한다.” 영어 원문: "Atracurium besylate is a nondepolarizing skeletal muscle relaxant. Nondepolarizing agents antagonize the neurotransmitter action of acetylcholine by binding competitively with cholinergic receptor sites on the motor end-plate." ([DailyMed: atracurium besylate prescribing information, Meitheal Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=efe90ee2-fe9e-421f-9e54-2961085d3b12), 버전 2024-12-04; 확인일 2026-11-19). 알려진 정보에 따르면 Atracurium은 신경근접합부의 니코틴성 아세틸콜린 수용체를 길항하는 비탈분극성 신경근 차단제이며, 호프만 소거(Hofmann elimination)로 분해됩니다.

자간전증의 병태생리는 태반 기능 이상, 혈관내피 손상, 고혈압이 핵심이며, 신경근 차단과의 직접적인 기전적 연관성은 확립되어 있지 않습니다. 자간전증의 경련 예방에는 Atracurium이 아닌 황산마그네슘이 사용됩니다. 임신부에서 Atracurium은 마취 상황에 한정되어 사용됩니다.

따라서 이번 예측은 TxGNN 모델(딥러닝)이 관련 질환 사이에서 학습한 유사성을 반영한 것일 수 있으며, 생물학적 근거로 뒷받침되지는 않습니다. 같은 질환군의 하위 유형(중증 자간전증, 경증 자간전증)도 높은 점수를 받았으나 독립적인 근거로 볼 수 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200703106 | 트라리움주(베실산아트라쿠륨)(수출용) [수출명: Newtrium Inj.] | 주사제 (갈색 앰플, 무색~미황색 투명액) | 허가 문서 링크만 등재 (본문 확인 필요) |
| 201802514 | 비씨아트라쿠륨베실산염주사25밀리그램/2.5밀리리터(수출용) | 주사제 (갈색 앰플, 무색~미황색 투명액) | 허가 문서 링크만 등재 (본문 확인 필요) |
| 200103035 | 아크리움주사(아트라쿠륨베실산염) | 주사제 (내수용 갈색 앰플 / 수출용 무색투명 또는 갈색 앰플) | 허가 문서 링크만 등재 (본문 확인 필요) |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
자간전증 예측은 TxGNN 점수(0.9997)만 높을 뿐, 임상시험과 문헌이 전혀 없고(L5) 기전적 연관성도 확립되어 있지 않습니다. 자간전증의 표준 경련 예방 약물은 황산마그네슘이며, Atracurium은 치료 목적이 아닌 제왕절개 마취 시의 보조 용도로만 쓰입니다.

**진행하려면 필요한 것:**
- 허가 문서에서 허가 적응증 및 경고·금기 정보 확보 (안전성 검토의 선행 조건)
- 상세한 약물 작용 기전(MOA) 데이터 보강
- 자간전증 병태생리와의 기전적 연관성을 뒷받침하는 전임상 또는 문헌 근거
- 기존 적응증과의 유사성 및 투여 경로 적합성 평가

참고로, 같은 약물의 다른 예측 질환(뇌척수신경근 증후군인 마미증후군, 안검경련, 편두통, 과민성 대장 증후군 등)도 모두 근거 수준 L5로 임상시험·문헌이 없습니다. 특히 안검경련과 편두통은 TxGNN 모델(딥러닝)이 보툴리눔 독소 관련 질환 사이에서 학습한 유사성이 점수를 높였을 가능성이 있으나, 이는 생물학적 근거가 아니며 Atracurium은 작용 부위와 지속 시간이 달라 실현 가능성이 낮습니다. 혈전성 질환은 기전적 연관성이 확인되지 않았고, "obsolete neurogenic bladder"는 폐기된 온톨로지 용어여서 현행 용어로 재매핑이 필요합니다.

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: atracurium besylate prescribing information, Meitheal Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=efe90ee2-fe9e-421f-9e54-2961085d3b12) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

