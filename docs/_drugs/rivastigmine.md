---
layout: default
title: Rivastigmine
parent: 僅模型預測 (L5)
nav_order: 284
evidence_level: L5
indication_count: 1
---

# Rivastigmine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Rivastigmine: 알츠하이머 치매에서 녹내장으로

---

## 한 문장 요약

Rivastigmine은 선택적 아세틸콜린에스테라제(AChE) 억제제로, 알츠하이머 치매 및 파킨슨병 치매 치료에 사용되는 콜린성 약물입니다.
TxGNN 모델은 **녹내장(Glaucoma)**에 효과가 있을 수 있다고 예측하며,
현재 **임상시험 0건**과 **문헌 3편**이 이 방향의 기전적 가능성을 시사합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 알츠하이머 치매 / 파킨슨병 치매 (AChE 억제제) |
| 예측 신규 적응증 | 녹내장 (Glaucoma) |
| TxGNN 예측 점수 | 99.27% |
| 근거 수준 | L4 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

Rivastigmine은 선택적 카바메이트계 AChE 억제제로, 뇌에서 아세틸콜린(ACh)의 가수분해를 억제하여 콜린성 시냅스 전달을 강화합니다. 이 기전은 알츠하이머 치매의 인지 증상 완화에 적용되어 왔으나, 안압(IOP) 조절과 관련한 안과 적용 가능성도 존재합니다.

녹내장의 핵심 위험 요인은 안압 상승이며, 기존 치료제 pilocarpine은 M3 무스카린 수용체(M3R)를 **직접** 자극해 섬모체 수축과 소주망(trabecular meshwork)을 통한 방수 유출을 촉진하여 안압을 낮춥니다. Rivastigmine이 국소(점안) 방식으로 적용될 경우, 전안부의 AChE를 억제해 국소 ACh 농도를 높이고 M3R을 **간접** 활성화함으로써 pilocarpine과 유사한 안압 강하 효과를 유도할 수 있습니다.

전임상 토끼 실험(PMID 10673128)에서 국소 점안 Rivastigmine이 정상안압 토끼의 IOP를 유의하게 낮추는 것이 확인되었고, 2024년 발표된 시스템 유전학 연구(PMID 39130374)는 전안부 콜린성 시스템이 소주망을 통한 IOP 조절에 핵심적 역할을 한다는 기전적 근거를 추가로 뒷받침합니다. TxGNN 지식 그래프 점수 0.9927은 콜린성 경로 노드와 녹내장 노드 간의 강한 연관성을 반영합니다.

---

## 임상시험 근거

현재 Rivastigmine과 녹내장에 관련된 등록된 임상시험이 없습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|------|------|------|---------|
| [10673128](https://pubmed.ncbi.nlm.nih.gov/10673128/) | 2000 | 전임상 동물 연구 | J Ocul Pharmacol Ther | 국소 Rivastigmine 점안이 정상안압 토끼에서 투여 후 8시간까지 IOP를 유의하게 낮춤 — 직접 안압 강하 가능성 최초 입증 |
| [39130374](https://pubmed.ncbi.nlm.nih.gov/39130374/) | 2024 | 시스템 유전학 / 분자 연구 | Front Mol Biosci | 전안부 콜린성 시스템(M3R 경유)이 소주망을 통한 IOP 조절에 중요함을 확인; 기존 M3R 직접 작용제의 전신 부작용 한계를 지적하며 간접 콜린성 접근의 필요성 제시 |
| [27967267](https://pubmed.ncbi.nlm.nih.gov/27967267/) | 2017 | 특허 문헌 리뷰 | Expert Opin Ther Pat | 2012–2015년 AChE 억제제 특허 동향 분석; 알츠하이머병·중증근무력증과 함께 녹내장이 AChE 억제의 치료 관련 분야로 명시 |

---

## 한국 시판 정보

현재 한국에 Rivastigmine으로 허가된 의약품이 없습니다. 기존 안전성 모니터링 기반 자료를 독자적으로 확보해야 합니다.

> 참고: Rivastigmine은 미국(FDA), 유럽(EMA) 등 주요 국가에서 알츠하이머 치매 치료제로 허가되어 있으며, 경피 패치 및 경구 제형이 존재합니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
녹내장에 대한 Rivastigmine의 인체 임상 근거가 전무하며, 현재 가용 데이터는 전임상 동물 실험과 기전 연구에 한정됩니다. 한국 시판 실적이 없어 국내 안전성 기반 자료가 부재하고, MOA 및 경고·금기 사항 데이터도 미확보 상태입니다.

**진행하려면 필요한 것:**
- 국소 점안 제형으로의 약물 재처방 가능성 타당성 평가 (안구 투과율, 국소 AChE 선택성 검토)
- 인체 대상 개념 증명(PoC) 임상시험 설계 — 1상/2상 IOP 강하 효능 및 안전성 평가
- MOA 상세 자료 확보 (DrugBank API 조회)
- MFDS 허가 안전성 자료 또는 해외 허가 자료(FDA Label) 준용을 통한 경고·금기 사항 보완
- 기존 녹내장 치료제(prostaglandin 유사체, β-차단제, pilocarpine)와의 병용 가능성 및 DDI 검토
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

