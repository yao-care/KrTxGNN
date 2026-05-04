---
layout: default
title: Amikacin
parent: 僅模型預測 (L5)
nav_order: 53
evidence_level: L5
indication_count: 10
---

# Amikacin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Amikacin: 중증 그람음성균 감염증에서 부장티푸스열(Paratyphoid Fever)로

## 한 문장 요약

Amikacin은 세균의 30S 리보솜 소단위에 결합하여 단백질 합성을 억제하는 아미노글리코사이드계 항생제로, 중증 그람음성균 감염증 치료에 사용됩니다.
TxGNN 모델은 **부장티푸스열(Paratyphoid Fever)**에 효과가 있을 수 있다고 예측하며,
현재 **0건의 임상시험**과 **12편의 문헌**이 이 방향을 간접 지지합니다.
기전적 근거는 성립하나 부장티푸스열 특이적 RCT가 전무하여 현 단계에서는 연구 과제로 분류됩니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 중증 그람음성균 감염증 (패혈증·폐렴·복막염 등; 허가 데이터 미수집) |
| 예측 신규 적응증 | 부장티푸스열 (Paratyphoid Fever) |
| TxGNN 예측 점수 | 99.82% |
| 근거 수준 | L4 (기전 연구 + 관찰 데이터) |
| 시판 현황 | 미등록 (未上市) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

Amikacin은 아미노글리코사이드계 항생제로, 세균의 30S 리보솜 소단위에 결합하여 mRNA 번역을 왜곡시키고 단백질 합성을 억제합니다. 이 기전은 그람음성 막대균 전반에 살균 효과를 나타내며, 부장티푸스열의 원인균인 *Salmonella paratyphi* 역시 그람음성 막대균이므로 항균 활성의 기전적 타당성이 성립합니다. 다만 현재 Evidence Pack에 DrugBank MOA 데이터가 수집되지 않아 상세한 약력학적 분석은 별도 조회가 필요합니다.

부장티푸스열 치료에서 Amikacin이 주목받는 배경은 다제내성(MDR) 균주의 확산입니다. 클로람페니콜·암피실린·코-트리목사졸 내성 *S. paratyphi* B 감염에서 불응 사례가 증가함에 따라, PMID 2516600(1989)에서 아미노글리코사이드류를 대체 치료 선택지로 사용한 초기 임상 결과가 기록되었습니다. PMID 10505326에서는 면역저하 소아에서 cefepime + Amikacin 병용 요법으로 *S. Paratyphi* B 관련 무결석성 담낭염을 성공적으로 치료한 증례도 보고되어 있습니다.

그러나 현재 부장티푸스열을 일차 적응증으로 설계한 무작위 대조 임상시험(RCT)은 전무합니다. 이용 가능한 문헌의 대부분은 케이스 리포트·후향적 항균 감수성 조사로, 임상적 효능보다 항균 스펙트럼 확인에 집중되어 있습니다. MDR 장열의 일선 치료 자리는 이미 fluoroquinolone·3세대 세팔로스포린이 차지하고 있으므로, Amikacin의 독자적 역할 확립을 위해서는 체계적 임상 개발이 필요합니다.

---

## 임상시험 근거

현재 부장티푸스열 관련 Amikacin 임상시험 등록이 없습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [10505326](https://pubmed.ncbi.nlm.nih.gov/10505326/) | 1999 | Case Report | Pediatric Hematology Oncology | 급성 림프모구 백혈병 소아에서 *S. Paratyphi* B 무결석성 담낭염; cefepime + amikacin 병용으로 완치 |
| [9459410](https://pubmed.ncbi.nlm.nih.gov/9459410/) | 1997 | Case Report | The Journal of Infection | 신생아 퀴놀론 내성 *S. Paratyphi* B 뇌막염 증례; 대체 항생제 필요성 부각 |
| [2516600](https://pubmed.ncbi.nlm.nih.gov/2516600/) | 1989 | Case Series | Mikrobiyoloji Bulteni | MDR *Paratyphi* B 감염 48례 치료·항균 감수성 결과; 아미노글리코사이드류 대체 사용 초기 기록 |
| [18383953](https://pubmed.ncbi.nlm.nih.gov/18383953/) | 2007 | Prospective Cohort | J Indian Medical Association | 소아 장열 145례 전향적 임상·미생물 분석; *S. paratyphi* 포함 항생제 감수성 패턴 제시 |
| [17337835](https://pubmed.ncbi.nlm.nih.gov/17337835/) | 2007 | Case Report | Indian Journal of Pediatrics | 신생아 MDR *S. Paratyphi* A 패혈증 증례; 항균 감수성 범위 확인 |
| [27407999](https://pubmed.ncbi.nlm.nih.gov/27407999/) | 2007 | Retrospective Antibiogram | Medical Journal, Armed Forces India | 인도 북부 *S. typhi* 및 *S. paratyphi* A 45례 감수성 패턴; 클로람페니콜 감수성 재출현 관찰 |
| [30724049](https://pubmed.ncbi.nlm.nih.gov/30724049/) | 2018 | Cross-sectional | Pakistan J Biological Sciences | 퀘타 지역 병원 장열 환자 *S. paratyphi* 분리·동정 및 미생물학적 특성 |
| [26905550](https://pubmed.ncbi.nlm.nih.gov/26905550/) | 2014 | Retrospective Antibiogram | JNMA | 교육병원 혈액배양 분리주 빈도 및 항균 감수성 패턴 분석; Amikacin 감수성 포함 |
| [14596347](https://pubmed.ncbi.nlm.nih.gov/14596347/) | 2003 | Microbiological Survey | The New Microbiologica | 요르단 1988–2000 *S. typhi·S. paratyphi* 발생 역학 분석 |
| [16410091](https://pubmed.ncbi.nlm.nih.gov/16410091/) | 2006 | Case Series | Journal of Pediatric Surgery | 소아 비장 농양 4례 경피적 배농 + 항생제 병용 치료 성공 (살모넬라 관련 합병증 포함) |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
Amikacin은 *Salmonella paratyphi*에 대한 기전적 항균 활성이 성립하고 소규모 임상 사용 기록이 있으나, 부장티푸스열 특이 임상시험이 전무하며 현존 문헌 근거는 케이스 시리즈·후향적 항균 감수성 연구(L4)에 머물러 있습니다. 현 단계에서는 개발 우선순위를 정당화할 충분한 근거가 없으므로 추가 연구 질문 정립이 필요합니다.

**진행하려면 필요한 것:**
- DrugBank API를 통한 Amikacin MOA 공식 데이터 확보
- MFDS 허가사항 조회를 통한 국내 적응증 및 경고 사항 확인
- MDR *Salmonella paratyphi* 감염에서 Amikacin 임상 유효성을 평가하는 전향적 코호트 연구 또는 파일럿 RCT 설계
- 신독성(nephrotoxicity) 및 이독성(ototoxicity) 모니터링 프로토콜을 포함한 안전성 계획 수립
- 기존 1선 치료제(fluoroquinolone, 3세대 세팔로스포린) 실패 후 구제 요법으로서의 포지셔닝 전략 수립
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

