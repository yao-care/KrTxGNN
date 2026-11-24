---
layout: default
title: Frovatriptan
parent: 모델 예측만 (L5)
nav_order: 366
evidence_level: L5
indication_count: 2
monitor_inn: "frovatriptan"
predicted_indications: ["atrophoderma vermiculata", "ulerythema ophryogenesis"]
last_modified_at: 2026-11-24
description: "Frovatriptan: 예측 신규 적응증 위축피부증 벌레모양 (atrophoderma vermiculata) (근거 수준 L5). 기존 적응증: 전조증상을 수반하거나 수반하지 않는 편두통의 급성치료"
---

# Frovatriptan
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **2** 건
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

## Frovatriptan: 5-HT1B/1D 수용체 작용제 → 위축피부증 벌레모양 (atrophoderma vermiculata)
{: .text-alpha }

## 한 문장 요약

Frovatriptan은 5-HT1B/1D 수용체 작용제 계열의 약물입니다.
TxGNN 모델은 **위축피부증 벌레모양(atrophoderma vermiculata)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 직접 뒷받침하는 **임상시험은 0건**, **문헌도 0편**입니다.
따라서 이 예측은 컴퓨터 모델 단계의 가설에 머물러 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 전조증상을 수반하거나 수반하지 않는 편두통의 급성치료 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200903830/EE)) |
| 예측 신규 적응증 | 위축피부증 벌레모양 (atrophoderma vermiculata) |
| TxGNN 예측 점수 | 0.9973 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 2건 / 전체 2건) |
| 허가증 수 | 2건 (유효 2건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Frovatriptan 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “프로바트립탄은 5-HT 1B/1D 수용체에 높은 친화도로 결합한다. 프로바트립탄 숙시네이트의 치료 활성은 두개내 혈관(동정맥 문합 포함) 및 삼차신경계 감각신경의 5-HT 1B/1D 수용체에 대한 작용제 효과에 기인하는 것으로 생각되며, 이로 인해 두개 혈관 수축 및 전염증성 신경펩티드 방출 억제가 일어난다.” 영어 원문: "Frovatriptan binds with high affinity to 5-HT 1B/1D receptors. The therapeutic activity of frovatriptan succinate is thought to be due to the agonist effects at the 5-HT 1B/1D receptors on intracranial blood vessels (including the arterio-venous anastomoses) and sensory nerves of the trigeminal system which result in cranial vessel constriction and inhibition of pro-inflammatory neuropeptide release." ([DailyMed: frovatriptan succinate prescribing information, Leading Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d303af88-e0c1-4fb2-ba8e-83b7e6d163cd), 버전 2026-06-27; 확인일 2026-11-19). Frovatriptan은 단일 성분 제제이며, 5-HT1B/1D 수용체 작용제로 분류되는 약물입니다.

위축피부증 벌레모양은 볼에 나타나는 모낭 위축성 피부 질환입니다. 5-HT1B/1D 수용체 작용과 이 질환 사이에 설득력 있는 연결 고리는 아직 확립되지 않았습니다. 높은 점수는 계산 모델의 출력일 뿐이며, 현 단계에서는 추가 평가를 뒷받침할 근거가 부족합니다.

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 200903830 | 미가드정2.5밀리그램(프로바트립탄숙신산염일수화물) | 양면이 볼록한 흰색 원형 필름코팅정 | 에스케이케미칼(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200903830/EE) | 유효 |
| 202501584 | 프로트립탄정2.5밀리그램(프로바트립탄숙신산염일수화물) | 양면이 볼록한 흰색 원형 필름코팅정 | 명인제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202501584/EE) | 유효 |

<!-- licenses:end -->

## 안전성 고려사항

- **약물 상호작용**: 데이터에 31건의 상호작용이 기록되어 있습니다. 주요(Major) 등급으로는 dolasetron, lorcaserin, palonosetron, ondansetron, fenfluramine, dexfenfluramine, granisetron, sibutramine, methylene blue가 있습니다. 세로토닌 관련 약물과의 병용에 주의가 필요합니다. 중등도(Moderate) 등급으로는 morphine, codeine, hydrocodone, deferasirox 등이 있습니다.

허가사항의 경고 및 금기 정보는 이번 데이터에 포함되지 않았으므로 허가사항을 직접 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 질환에 대한 임상시험과 문헌이 전혀 없고, 기전상 연결 고리도 확립되지 않았습니다. TxGNN 점수가 높더라도 모델 예측만으로는 진행 근거가 되지 않습니다.

**진행하려면 필요한 것:**
- 5-HT1B/1D 수용체 작용과 모낭 위축성 피부 질환 사이의 기전 연구 또는 전임상 근거
- 위축피부증 벌레모양을 직접 다룬 임상 또는 문헌 근거
- 상세한 작용 기전(MOA) 데이터
- 허가사항(경고 및 금기) 확보 후 안전성 검토

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: frovatriptan succinate prescribing information, Leading Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d303af88-e0c1-4fb2-ba8e-83b7e6d163cd) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

