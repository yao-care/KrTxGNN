---
layout: default
title: Alprostadil
parent: 僅模型預測 (L5)
nav_order: 46
evidence_level: L5
indication_count: 10
---

# Alprostadil
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

# Alprostadil: 도관 의존성 선천성 심장병 안정화에서 대동맥 기형으로

---

## 한 문장 요약

Alprostadil은 합성 프로스타글란딘 E1(PGE1)으로, 전 세계적으로 신생아의 도관 의존성 선천성 심장병(ductus-dependent CHD)에서 동맥관 개존(PDA) 유지를 통한 수술 전 안정화 목적으로 사용되어 왔습니다.
TxGNN 모델은 **대동맥 기형(Aortic Malformation)**에 효과가 있을 수 있다고 예측하며,
현재 **2건의 임상시험**과 **20편의 문헌**이 이 방향을 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 한국 허가 없음 (전 세계적으로 도관 의존성 선천성 심장병 수술 전 안정화에 사용) |
| 예측 신규 적응증 | 대동맥 기형 (Aortic Malformation) |
| TxGNN 예측 점수 | 99.98% |
| 근거 수준 | L3 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

Alprostadil(PGE1)은 EP4 수용체를 통해 동맥관(ductus arteriosus) 평활근의 수축을 억제하고 cAMP를 상향 조절하여 동맥관 개존을 유지합니다. 동시에 전신 및 폐혈관 확장 작용을 통해 심박출량 분배를 조절합니다. 이 기전은 체순환 혈류가 PDA에 전적으로 의존하는 도관 의존성 병변에서 수술 전 생명 유지 브릿지(bridge-to-surgery) 치료의 약리적 근거입니다.

대동맥 기형—특히 대동맥궁 단절(Interrupted Aortic Arch, IAA), 대동맥 축착(Coarctation of the Aorta), 저좌심증후군(Hypoplastic Left Heart Syndrome, HLHS), 대동맥 폐쇄(Aortic Atresia) 등—은 좌심 박출 경로가 막혀 체순환이 PDA를 통해서만 유지되는 대표적인 도관 의존성 병변입니다. 이러한 신생아에서 동맥관이 자연 폐쇄되면 체순환이 급격히 붕괴되어 대사성 산증 및 사망에 이를 수 있으므로, Alprostadil 정맥 주입을 통한 동맥관 유지는 외과적 교정 전 필수적입니다.

1982년부터 축적된 임상 시리즈(PMID 6763200, 7201134)는 Alprostadil이 대동맥 발달 이상 병변에서 직접 사용되어 왔음을 기록하고 있으며, IAA 관리에서 PGE1 도입이 치료 패러다임 전체를 바꾸었다는 리뷰(PMID 26686446)도 이 연관성을 강력히 지지합니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT04054115](https://clinicaltrials.gov/study/NCT04054115) | Phase 1 | 조기 종료 | 10 | 양방향 Glenn 수술(BCPC) 후 Alprostadil이 뇌혈류 및 폐혈류에 미치는 급성 효과를 평가한 RCT. 단심실 선천성 심장병의 도관 의존성 맥락에서 직접적인 약효 평가로 설계됨. 조기 종료(n=10)로 수집 데이터 제한적이나 설계 타당성 높음. |
| [NCT02042092](https://clinicaltrials.gov/study/NCT02042092) | N/A | 완료 | 39 | 전신 대혈관 혈관염(sLVV)에서 CDUS 대 MRA 영상 비교 연구. Alprostadil 직접 치료 시험이 아니며 대동맥 기형과의 직접 관련성 낮음. |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [19080093](https://pubmed.ncbi.nlm.nih.gov/19080093/) | 2008 | RCT | Zhonghua Yi Xue Za Zhi | 소아 CHD 환자의 심폐우회술 후 Alprostadil + Ulinastatin 병용이 대조군 대비 염증 반응 및 폐 손상을 유의하게 감소시킴 |
| [6763200](https://pubmed.ncbi.nlm.nih.gov/6763200/) | 1982 | 전향적 임상 시리즈 | Pharmacotherapy | 우심 유출로 폐쇄 및 체순환 의존성 병변에서 Alprostadil 주입으로 PDA 확장 및 폐혈류·체순환 유지 효과 최초 체계 기술 |
| [26686446](https://pubmed.ncbi.nlm.nih.gov/26686446/) | 2015 | 리뷰 | Semin Thorac Cardiovasc Surg | 1970년대 후반 PGE1 도입이 대동맥궁 단절(IAA) 관리를 혁신함; 수술 전 수일간 PGE1 소생 후 직접 궁 문합술 및 VSD 폐쇄 권고 |
| [7201134](https://pubmed.ncbi.nlm.nih.gov/7201134/) | 1982 | 증례 시리즈 | Pediatric Cardiology | 저좌심증후군 및 대동맥 폐쇄 신생아 7례에서 PGE1 주입 후 일시적 대사·순환 개선 확인; 일부 비반응 사례에서 조기 혈역학 붕괴의 기전적 설명 제공 |
| [25647388](https://pubmed.ncbi.nlm.nih.gov/25647388/) | 2014 | 리뷰/임상 지침 | Cardiology in the Young | 신생아 중증 대동맥판 협착의 수술 전 관리; PGE1으로 좌심실 벽 스트레스 감소 및 관상동맥 관류 보호 전략 기술 |
| [32184038](https://pubmed.ncbi.nlm.nih.gov/32184038/) | 2020 | 후향적 코호트 | Asian J Surg | IAA 환자의 단계적 수술 결과 보고; PGE1을 초기 안정화 수단으로 사용하는 임상 경로 기술 |
| [6537955](https://pubmed.ncbi.nlm.nih.gov/6537955/) | 1984 | 임상 시리즈 | J Am Coll Cardiol | 신생아 17례에서 평균 39일간 장기 PGE1 정맥 주입; 대동맥 축착 포함 다양한 CHD에서 효과 및 장기 안전성 데이터 제공 |
| [10771966](https://pubmed.ncbi.nlm.nih.gov/10771966/) | 1998 | 임상 시리즈 | Indian J Pediatrics | 도관 의존성 CHD에서 PGE1 1단계 고식 치료 효과; 폐동맥 폐쇄, 대혈관 전위, 대동맥 축착 등 포함 |
| [1926911](https://pubmed.ncbi.nlm.nih.gov/1926911/) | 1991 | 임상 지침 | DICP Ann Pharmacother | 도관 의존성 심장 결함 의심 즉시 이송 전 PGE1 시작 권고; 지역 병원 투여 프로토콜 정립 |
| [30347623](https://pubmed.ncbi.nlm.nih.gov/30347623/) | 2019 | 리뷰 | J Neonatal Perinat Med | 도관 의존성 CHD 신생아의 PGE1 주입 중 장관 영양 전략 및 NEC 발생률 검토; 실제 임상 적용 현황 파악 |

---

## 한국 시판 정보

현재 한국 내 Alprostadil에 대한 허가 이력이 없습니다 (허가증 0건, 미시판). 전 세계적으로는 정맥 주사제(Prostin VR Pediatric® 등)로 신생아 도관 의존성 선천성 심장병 관리에 광범위하게 사용되고 있으며, 별도 제형은 발기부전 및 말초동맥 질환 치료에 허가된 국가들이 있습니다. 한국 도입 시 MFDS 신규 허가 절차가 필요합니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

> **참고**: PGE1 장기 주입 시 알려진 주요 부작용으로 무호흡(특히 미숙아), 저혈압, 발열, 피질 골 증식증(장기 투여 시), 비대성 유문 협착증 등이 문헌에 보고된 바 있습니다(PMID 25263728, 28508920). 규제 기관 허가사항을 통한 공식 확인이 필요합니다.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
1982년부터 축적된 다수의 임상 시리즈, 리뷰 문헌, 그리고 1건의 RCT가 대동맥 기형(IAA, 대동맥 축착, HLHS 등)에서 Alprostadil의 임상적 사용을 지지하며, EP4 수용체를 통한 동맥관 유지라는 명확한 기전적 근거(L3)가 존재합니다. 다만 한국 내 미시판 상태로 도입 전 규제적 검토 및 안전성 프로파일 확보가 선결 조건입니다.

**진행하려면 필요한 것:**
- TFDA/MFDS 공식 허가사항(경고, 금기, 용량) PDF 확보 및 파싱 (Data Gap DG001 해소)
- DrugBank API를 통한 상세 작용 기전(MOA) 및 약물 상호작용 데이터 보완 (Data Gap DG002 해소)
- 한국 내 신생아 도관 의존성 CHD 발생 현황 및 현행 치료 경로 분석
- 정맥 주사 제형 도입을 위한 MFDS 신규 허가 또는 희귀의약품 지정 경로 검토
- 특이 인구집단(미숙아, 장기 투여 필요 환자) 대상 안전성 모니터링 계획 수립

---

> **⚠️ 면책 조항**: 본 보고서는 연구 참고용으로만 제공되며 의료 조언을 구성하지 않습니다. 모든 약물 재창출 후보는 임상 검증을 거쳐야 적용 가능합니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

