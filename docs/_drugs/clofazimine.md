---
layout: default
title: Clofazimine
parent: 僅模型預測 (L5)
nav_order: 178
evidence_level: L5
indication_count: 3
---

# Clofazimine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Clofazimine: 나병(한센병)/항마이코박테리아 감염 치료에서 주폐포자충증으로

## 한 문장 요약

Clofazimine은 나병(한센병)과 내성 결핵(MDR-TB) 치료에 사용되어 온 항마이코박테리아 약물로, 한국에는 현재 허가된 제품이 없습니다.
TxGNN 모델은 **주폐포자충증(Pneumocystosis)**에 효과가 있을 수 있다고 예측하며,
현재 **1건의 임상시험**과 **4편의 문헌**이 간접적으로 이 방향을 언급하고 있습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 나병(한센병), 항마이코박테리아 감염 (한국 미허가) |
| 예측 신규 적응증 | 주폐포자충증 (Pneumocystosis) |
| TxGNN 예측 점수 | 99.90% |
| 근거 수준 | L4 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터(MOA)가 없습니다. 알려진 정보에 따르면, Clofazimine은 항마이코박테리아 약물로서 병원체 내 활성산소(ROS) 생성을 통해 산화환원 항상성을 교란하는 기전이 제안되어 있으며, 나병 및 내성 결핵(MDR-TB) 치료에서 효능이 입증되어 있습니다.

주폐포자충증(Pneumocystosis)은 *Pneumocystis jirovecii*에 의해 발생하는 기회감염으로, HIV/AIDS 환자 등 면역저하자에서 주로 발생합니다. Clofazimine이 주로 표적으로 하는 분지균(Mycobacteria)과 *P. jirovecii*는 생물학적으로 본질적으로 다른 병원체(세균 vs. 진균유사 원생생물)이므로, 기전상 직접적인 연관성은 제한적입니다.

현재 수집된 문헌과 임상시험은 주로 AIDS 환자에서 MAC(Mycobacterium avium complex) 예방·치료 도중 PCP(Pneumocystis carinii pneumonia)가 동반 발생한 사례들을 기술한 것으로, Clofazimine이 *P. jirovecii*에 직접 작용한다는 기전적 또는 임상적 증거라기보다는 동일한 면역저하 환경에서의 공존 감염을 반영한 간접 신호로 보는 것이 적절합니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00002058](https://clinicaltrials.gov/study/NCT00002058) | NA | 완료 | N/A | HIV 감염 환자에서 MAC 예방을 위한 Clofazimine 무작위 대조 연구. 1차 목표는 MAC 예방이며, 연구 등록 기준에 PCP 과거력 또는 CD4 ≤100/mm³이 포함되어 환자군이 PCP 고위험군과 겹치나, 연구 설계 및 종료점이 pneumocystosis와 직접적 관련이 없음 (관련성 등급: C) |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [8501340](https://pubmed.ncbi.nlm.nih.gov/8501340/) | 1993 | 임상 연구 (MAC) | J Infect Dis | HIV 환자 110명 대상 Clofazimine 50mg의 MAC 예방 효과를 평가한 무작위 공개라벨 시험. 등록 기준에 PCP 과거력(2~4개월 전) 또는 CD4 ≤100/mm³ 포함. MAC을 1차 연구 목적으로 하며 pneumocystosis는 부수적으로 언급됨 |
| [2714863](https://pubmed.ncbi.nlm.nih.gov/2714863/) | 1989 | Case Report | Infection | AIDS 환자에서 *M. kansasii* 폐질환과 PCP 동반 사례. Clofazimine + 시프로플록사신 + TMP-SMX 복합요법으로 빠른 임상 호전 보고. Clofazimine의 항PCP 직접 기여 여부는 불명확 |
| [6299154](https://pubmed.ncbi.nlm.nih.gov/6299154/) | 1983 | Case Report | Ann Intern Med | 혈우병 남성에서 PCP 발생 후 MAC 동반 감염 진행 사례 보고. Clofazimine 사용 없이 PCP 진단·경과만 기술 |
| [11363899](https://pubmed.ncbi.nlm.nih.gov/11363899/) | 1996 | Review | PI perspective | 기회감염 전반에 대한 업데이트 리뷰 (초록 없음, 직접 관련 내용 확인 불가) |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
현재 근거는 AIDS 환자에서 MAC과 PCP가 동시에 관찰된 간접적인 사례 보고와 MAC 예방 임상시험에 국한되며, Clofazimine이 *Pneumocystis jirovecii*에 직접 효과적이라는 기전적·임상적 증거가 없습니다. TxGNN의 높은 예측 점수(99.90%)는 공유 환자군(AIDS/면역저하)에서의 간접 공존 신호를 반영한 것으로 해석될 가능성이 높아, 신규 적응증으로 개발을 추진하기에는 근거가 불충분합니다.

**진행하려면 필요한 것:**
- Clofazimine의 *Pneumocystis jirovecii*에 대한 체외(in vitro) 활성 실험 데이터 확보
- 작용 기전(MOA) 데이터 보완 (DrugBank API 조회)
- MFDS·WHO·FDA 처방 정보에서 경고/금기 등 안전성 데이터 확보 (현재 Blocking 데이터 갭)
- 한국 내 미시판 약물로, 임상 적용 이전 국내 도입 가능성 및 특례수입 검토 필요
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

