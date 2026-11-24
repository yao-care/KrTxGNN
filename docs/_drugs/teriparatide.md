---
layout: default
title: Teriparatide
parent: 모델 예측만 (L5)
nav_order: 729
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
description: "Teriparatide: 예측 신규 적응증 십이지장궤양 (Duodenal Ulcer) (근거 수준 L5). 기존 적응증: 골다공증 (골절 고위험 환자)"
monitor_inn: "TERIPARATIDE"
predicted_indications: ["duodenal ulcer (disease)", "non-syndromic esophageal malformation", "duodenal obstruction", "duodenogastric reflux", "esophageal disease", "Worth syndrome", "autosomal dominant neovascular inflammatory vitreoretinopathy", "succinyl-CoA:3-ketoacid CoA transferase deficiency", "amenorrhea (disease)"]
---

# Teriparatide
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **9** 건
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

## Teriparatide: 골다공증에서 십이지장궤양 (Duodenal Ulcer)으로
{: .text-alpha }

## 한 문장 요약

Teriparatide는 부갑상선호르몬(PTH) 1-34 부분 펩타이드 제제로, 원래 골절 위험이 높은 골다공증 환자의 치료에 사용되었습니다.
TxGNN 모델은 **십이지장궤양(Duodenal Ulcer)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 지지하는 **임상시험은 0건, 문헌도 0편**입니다. 모델 예측만 있는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 골다공증 (골절 고위험 환자) |
| 예측 신규 적응증 | 십이지장궤양 (Duodenal Ulcer) |
| TxGNN 예측 점수 | 0.9986 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 5건 / 전체 6건) |
| 허가증 수 | 6건 (유효 5건) |
| 권장 결정 | Hold |

> 기존 적응증은 허가 문서 본문이 아니라 약리 데이터의 임상 용도 설명을 기준으로 기재했습니다. 허가증에는 적응증 본문 대신 문서 링크만 확인됩니다.

## 이 예측이 타당한 이유는?

Teriparatide는 PTH1 수용체(PTH1R)와 PTH2 수용체(PTH2R)에 결합하는 펩타이드입니다. 간헐적으로 투여하면 골형성을 촉진하는 것으로 알려져 있습니다. 위 내용은 수용체 표적 정보에 근거한 것입니다. 미국 FDA가 승인한 Teriparatide 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “내인성 84-아미노산 부갑상선호르몬(PTH)은 뼈와 신장에서 칼슘 및 인산 대사를 조절하는 주된 조절인자이다. PTH의 생리학적 작용에는 뼈 대사의 조절, 칼슘 및 인산의 신세뇨관 재흡수, 그리고 장관 칼슘 흡수가 포함된다. […] PTH와 테리파라타이드의 생물학적 작용은 특이적인 고친화성 세포 표면 수용체에 대한 결합을 통해 매개된다.” 영어 원문: "Endogenous 84-amino acid parathyroid hormone (PTH) is the primary regulator of calcium and phosphate metabolism in bone and kidney. Physiological actions of PTH include regulation of bone metabolism, renal tubular reabsorption of calcium and phosphate, and intestinal calcium absorption. […] The biological actions of PTH and teriparatide are mediated through binding to specific high-affinity cell-surface receptors." ([DailyMed: Bonsity (teriparatide) prescribing information, Alvogen Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2d0c89a2-3849-adf6-007d-aeca21cf417c), 버전 2026-08-31; 확인일 2026-11-19).

십이지장궤양은 소화관 점막 손상 질환입니다. 골형성 촉진이라는 teriparatide의 기전과 궤양 치유 사이에서 타당한 연결 고리는 현재 데이터에서 확인되지 않습니다. 0.9986이라는 높은 점수는 TxGNN 모델(딥러닝)이 산출한 값이며, 관련 질환 사이에서 모델이 학습한 유사성을 반영할 수 있을 뿐 생물학적 근거는 아닙니다. 임상적 또는 기전적 검증을 거치지 않았으므로 이 예측은 가설 수준으로 보아야 합니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 201907542 | 테로사카트리지주(테리파라타이드) | 무색투명한 액이 무색투명한 유리 카트리지에 든 주사제 | 대원제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201907542/EE) | 유효 |
| 202401682 | 테로사프리필드펜(테리파라타이드) | 무색투명한 액이 담긴 무색투명한 유리 카트리지가 장착된 프리필드펜 | 대원제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202401682/EE) | 유효 |
| 201507697 | 테리본피하주사56.5마이크로그램(테리파라타이드아세트산염) | 흰색의 고체 또는 분말이 무색투명한 바이알에 든 주사제 | 동아에스티(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201507697/EE) | 유효 |
| 202501822 | 테리멘트주(테리파라타이드) | 무색투명한 액이 무색투명한 유리 카트리지에 충전되어 주사침이 없는 프리필… | (주)파마리서치 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202501822/EE) | 유효 |
| 200209623 | 포스테오주(테리파라타이드) | 무색투명한 액이 충진된 주사침이 없는 프리필드펜 주입기 | 한국릴리(유) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200209623/EE) | 유효 |

위 표는 허가 6건 중 5건입니다.

<!-- licenses:end -->

## 안전성 고려사항

허가사항의 경고 및 금기 정보는 이번 데이터에 포함되어 있지 않으므로 허가사항을 직접 확인해야 합니다.

- **지식 그래프상 금기 질환** (허가 문구가 아닌 TxGNN 지식 그래프 기반): 고칼슘혈증, 부갑상선기능항진증, 골육종, 파제트병(소아 파제트병 포함), 신석회증, 요로결석, 인 대사 질환, 골연화증, 구루병, 신성 골이영양증, 섬유성 골염, 저혈압성 질환
- **약물 상호작용** (총 8건 중 약물 상호작용으로 확인된 6건):
  - 중등도: Calcitriol(외용), Calcipotriol(외용), Digoxin, Digitoxin
  - 경미: Hydrochlorothiazide, Furosemide

## 결론 및 다음 단계

**결정: Hold**

**사유:**
십이지장궤양 예측은 점수가 높지만 임상시험과 문헌이 전혀 없는 L5 단계입니다. 기전적 연결 고리도 확인되지 않아 현 시점에서 추가 진행할 근거가 부족합니다.

**진행하려면 필요한 것:**
- 십이지장궤양과 PTH 신호전달 사이의 기전적 연관성을 보여주는 전임상 또는 기전 연구
- 허가사항(경고, 금기)의 확인과 상세 작용 기전 데이터 보완
- 고칼슘혈증 및 디곡신 병용 위험 등 안전성 검토

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-20 | "다만 허가 정보에 기재된 상세 작용 기전은 이번 데이터에 없습니다. 위 내용은 수용체 표적 정보에 근거한 것입니다" replaced with a sourced mechanism-of-action statement | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 (2026-11-20 수정, 이전 판은 기록에 보존) | [DailyMed: Bonsity (teriparatide) prescribing information, Alvogen Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2d0c89a2-3849-adf6-007d-aeca21cf417c) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

