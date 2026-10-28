---
layout: default
title: Filgrastim
parent: 모델 예측만 (L5)
nav_order: 347
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Filgrastim: 예측 신규 적응증 혈소판 방출 장애 (primary release disorder of platelets) (근거 수준 L5). 기존 적응증: 허가 적응증 본문이 데이터에 포함되어 있지 않아 확인할 수 없음 (허가증별 PDF 링크만 제공됨)"
monitor_inn: "Filgrastim"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "Scott syndrome", "hemorrhagic disorder due to a constitutional thrombocytopenia", "bleeding diathesis due to a collagen receptor defect", "C1 inhibitor deficiency", "serpinopathy with toxic serpin polymerization", "fetal and neonatal alloimmune thrombocytopenia", "platelet-type bleeding disorder"]
---

# Filgrastim
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

## Filgrastim: 호중구감소증에서 혈소판 분비 장애로
{: .text-alpha }

## 한 문장 요약

Filgrastim은 G-CSF(과립구 집락자극인자) 유사체로, 호중구 계열에 작용하는 약물입니다. TxGNN 모델은 **혈소판 방출 장애(primary release disorder of platelets)**에 효과가 있을 수 있다고 예측하지만, 이를 직접 지지하는 **임상시험과 문헌은 없습니다**. 기전상 연관성도 확인되지 않아 모델 예측 단계의 가설로 보아야 합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문이 데이터에 포함되어 있지 않아 확인할 수 없음 (허가증별 PDF 링크만 제공됨) |
| 예측 신규 적응증 | 혈소판 방출 장애 (primary release disorder of platelets) |
| TxGNN 예측 점수 | 1.0000 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 8건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Filgrastim은 G-CSF 수용체를 통해 골수 호중구 전구세포의 증식과 분화를 촉진하는 단일 성분 제제입니다.

그러나 혈소판 방출 장애는 혈소판 과립 방출 또는 기능의 결함으로 생기는 질환입니다. Filgrastim이 혈소판 기능에 영향을 준다는 확립된 근거는 없습니다. 높은 TxGNN 점수는 TxGNN 모델(딥러닝)이 계산한 예측일 뿐이며, 관련 질환 사이에서 모델이 학습한 유사성을 반영할 수 있지만 생물학적 근거는 아닙니다. 기존 적응증과 신규 적응증 사이의 기전적 연관성은 현재 뒷받침되지 않습니다.

상위 예측 질환들(가성 폰빌레브란트병, Glanzmann 혈소판무력증, Scott 증후군 등)도 모두 혈소판 기능 이상이며, 같은 이유로 기전적 근거가 없습니다.

## 임상시험 근거

1순위 예측 질환(혈소판 방출 장애)에 대해 현재 관련 임상시험 등록이 없습니다.

참고로 10순위 예측 질환인 "혈소판형 출혈 질환"에는 7건의 시험이 연결되어 있습니다. 모두 조혈모세포이식 시험으로, Filgrastim은 줄기세포 동원이나 이식 후 호중구 회복에 보조적으로 쓰였을 가능성이 높고 시험의 평가 대상은 아닙니다. 따라서 혈소판 질환에 대한 직접 근거로 볼 수 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202007433 | 리콤비맥스주(필그라스팀)(수출용) | 주사제 (바이알) | 허가증 PDF 참조 |
| 201306361 | 류코스팀주사액프리필드시린지(필그라스팀(유전자재조합)) | 주사제 (프리필드시린지) | 허가증 PDF 참조 |
| 200209633 | 그라신300프리필드시린지주(필그라스팀) | 주사제 (프리필드시린지) | 허가증 PDF 참조 |
| 199500176 | 류코스팀주사액150마이크로그램(필그라스팀(유전자재조합)) | 주사제 (바이알) | 허가증 PDF 참조 |
| 201306360 | 류코스팀주사액프리필드시린지480마이크로그램(필그라스팀(유전자재조합))(수출용) | 주사제 (프리필드시린지) | 허가증 PDF 참조 |

위 표는 전체 8건 중 5건을 나열한 것입니다. 8건 모두 단일 성분 제제로 유효합니다.

## 안전성 고려사항

- **약물 상호작용**: 총 100건의 상호작용이 조회되었으며, 아래 항목이 모두 "중등도(Moderate)" 수준입니다.
  - 방사성의약품: Iobenguane (I-131), Fludeoxyglucose (18F), Ibritumomab tiuxetan, Tositumomab (I-131), Tositumomab
  - 항종양제 및 면역조절제: Levamisole, Trimetrexate, Mercaptopurine, Abemaciclib, Paclitaxel, Acalabrutinib, Aldesleukin, Alemtuzumab, Altretamine, Arsenic trioxide, Asparaginase Escherichia coli, Avapritinib, Azacitidine, Belantamab mafodotin, Bendamustine

경고 및 금기 사항은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
혈소판 방출 장애에 대한 임상시험과 문헌이 없고, Filgrastim의 작용 기전(호중구 계열)과 혈소판 기능 결함 사이에 알려진 연관성이 없습니다. 근거는 TxGNN 점수뿐(L5)이므로 현 단계에서 진행하기 어렵습니다.

**진행하려면 필요한 것:**
- 작용 기전(MOA) 데이터 확보 (예: DrugBank 조회)
- 한국 허가사항(경고, 금기, 적응증) 확인을 위한 허가증 PDF 분석
- 혈소판 기능과 G-CSF 신호 전달의 연관성을 보여주는 전임상 또는 기전 연구
- 상위 예측 질환에 대한 체계적 문헌 검색 및 임상시험 탐색
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

