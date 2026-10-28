---
layout: default
title: Thiopental
parent: 모델 예측만 (L5)
nav_order: 734
evidence_level: L5
indication_count: 8
monitor_inn: "Thiopental"
predicted_indications: ["trichotillomania", "Prinzmetal angina", "migraine disorder", "Tourette syndrome", "migraine with brainstem aura", "obsolete bundle branch block", "substance abuse/dependence", "nephrogenic syndrome of inappropriate antidiuresis"]
last_modified_at: 2026-10-23
description: "Thiopental: 예측 신규 적응증 Trichotillomania (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200308471/EE"
---

# Thiopental
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **8** 건
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

## Thiopental: Trichotillomania
{: .text-alpha }

## 한 문장 요약

Thiopental(치오펜탈)은 한국에서 주사용 분말 제제(펜토탈소디움)로 허가된 바르비투르산계 약물입니다. TxGNN 모델은 **트리코틸로마니아(발모벽, trichotillomania)**에 효과가 있을 수 있다고 예측하지만, 이 질환을 직접 다룬 임상시험과 문헌은 **0건**으로 모델 예측 단계(L5)에 머물러 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200308471/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200109981/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/198601870/EE |
| 예측 신규 적응증 | Trichotillomania |
| TxGNN 예측 점수 | 0.9995 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가 건수 | 3건 (단일 성분 3건, 모두 유효) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 일반적으로 thiopental은 GABA-A 수용체 신호를 강화하는 바르비투르산계 약물로 알려져 있으나, 이 보고서를 위해 수집된 자료에서는 반복 행동을 보이는 트리코틸로마니아의 신경회로와 연결할 근거가 확인되지 않습니다.

기존 적응증과 신규 적응증 사이의 유사성 분석도 아직 이루어지지 않았습니다. 따라서 기전상 타당성은 현재 입증되지 않았습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200308471 | 펜토탈소디움주사0.25그램(치오펜탈나트륨) | 황백색 분말 충진 갈색 바이알 | 허가 문서 링크만 제공되어 본문 확인 불가 |
| 200109981 | 펜토탈소디움0.5그램주(치오펜탈나트륨) | 황백색 분말 충진 갈색 바이알 | 허가 문서 링크만 제공되어 본문 확인 불가 |
| 198601870 | 펜토탈소디움0.5그램주(치오펜탈나트륨) | 황백색 분말 충진 갈색 바이알 | 허가 문서 링크만 제공되어 본문 확인 불가 |

세 건 모두 제이더블유중외제약(주) 제품입니다.

## 안전성 고려사항

허가사항의 경고·금기 정보는 이번 자료에 포함되지 않았습니다. 상세 내용은 허가사항을 참조하세요.

**약물 상호작용** (총 45건 확인, 아래는 일부)
- **중대(Major)**: Ethanol(에탄올), Warfarin(와파린)
- **중등도(Moderate)**: Morphine, Codeine, Hydrocodone, Dextromethorphan, Doxycycline, Dronabinol, Nabilone, Cetirizine, Carbinoxamine, Clemastine, Methylene blue, Nitisinone, Iodide I-131, Iodide I-123
- **경미(Minor)**: Pyridoxine, Cimetidine, Sulfasalazine, Promethazine

## 결론 및 다음 단계

**결정: Hold**

**사유:**
허가 적응증, 작용 기전, 경고·금기 정보도 확보되지 않아 안전성 1차 검토를 진행할 수 없습니다.

**진행하려면 필요한 것:**
- 식약처 허가사항(적응증, 경고, 금기) 문서 확보 및 분석
- 작용 기전(MOA) 데이터 보완 (DrugBank 조회)
- 트리코틸로마니아와 GABA 계열 약물의 연관성에 대한 직접 근거 탐색
- 기존 적응증과 신규 적응증 간 유사성 분석 및 투여 경로 적합성 평가

### 참고: 기타 예측 질환

모든 예측 질환의 근거 수준과 권장 결정은 아래와 같습니다.

| 순위 | 예측 질환 | 점수 | 근거 수준 | 비고 |
|-----|---------|------|---------|------|
| 2 | Prinzmetal 협심증 | 0.9994 | L5 | 임상시험·문헌 없음. 혈역학 부작용 우려 |
| 3 | 편두통 | 0.9994 | L5 | 문헌 1건은 식물 추출물 연구로 thiopental과 무관 |
| 4 | 투렛 증후군 | 0.9990 | L5 | 임상시험·문헌 없음 |
| 5 | 뇌간 조짐 편두통 | 0.9990 | L5 | 문헌 1건은 metoprolol 연구로 thiopental과 무관 |
| 6 | 각차단(obsolete 용어) | 0.9990 | L5 | 폐기된 질환 용어로 예측 가치 낮음 |
| 7 | 물질 남용/의존 | 0.9989 | L5 | 문헌 8건은 바르비투르산계 약물의 내성·의존 위험을 다룬 것으로, 치료 근거가 아닌 안전성 신호임 |
| 8 | 신인성 항이뇨호르몬 부적절 분비 증후군 | 0.9985 | L5 | 임상시험·문헌 없음 |

위 질환 모두 권장 결정은 **Hold**입니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

