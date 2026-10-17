---
layout: default
title: Alprostadil
parent: 모델 예측만 (L5)
nav_order: 48
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Alprostadil: 예측 신규 적응증 대동맥 기형 (Aortic Malformation) (근거 수준 L5). 기존 적응증: 허가증 원문이 링크 형태로만 제공되어 구체적인 적응증 문구를 확인할 수 없습니다"
monitor_inn: "Alprostadil"
predicted_indications: ["congenital tricuspid stenosis", "congenital valvular dysplasia", "straddling or overriding tricuspid valve", "tricuspid valve agenesis", "tricuspid valve prolapse (disease)", "anomaly of the tricuspid subvalvular apparatus", "double outlet right ventricle with atrioventricular septal defect, pulmonary stenosis, heterotaxy", "heart septal defect", "endemic goiter"]
---

# Alprostadil
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

# Alprostadil: 허가 적응증에서 대동맥 기형으로

## 한 문장 요약

Alprostadil(프로스타글란딘 E1)은 한국에서 주사제로 허가되어 시판 중인 약물입니다. TxGNN 모델은 **대동맥 기형(Aortic Malformation)**에 효과가 있을 수 있다고 예측합니다. 현재 등록된 임상시험은 없고, 증례 보고와 임상 연구 중심의 **문헌 8편**이 이 방향을 지지합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가증 원문이 링크 형태로만 제공되어 구체적인 적응증 문구를 확인할 수 없습니다 |
| 예측 신규 적응증 | 대동맥 기형 (Aortic Malformation) |
| TxGNN 예측 점수 | 99.98% |
| 근거 수준 | L4 (임상시험 없음, 증례 보고 및 소규모 임상 연구 수준) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 4건 |
| 권장 결정 | Hold (추가 근거 확보 전까지 연구 질문 단계로 유지) |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 다만 문헌에 따르면 Alprostadil(PGE1)은 동맥관(ductus arteriosus)의 평활근을 이완시켜 관을 열어 둡니다. 신생아의 동맥관 의존성 선천성 심장 기형에서 수술 전까지 전신 또는 폐 혈류를 유지하는 데 쓰입니다.

대동맥궁 단절, 중증 대동맥 축착, 대血管 전위 같은 동맥관 의존성 대동맥 병변에서는 이 작용이 혈류 유지에 직접 도움이 됩니다. 이는 이미 확립된 신생아 치료 방식이며, 기존 허가 적응증과도 겹칩니다. 따라서 예측은 기전상 타당성이 있습니다.

다만 2008년 울리나스타틴/알프로스타딜 연구는 체외순환 후 염증 반응과 폐 손상을 다룬 것으로, 동맥관 유지와는 별개의 간접적 기전입니다. 또한 대동맥 기형 자체를 치료하는 것이 아니라 수술 전 가교 역할이라는 점을 구분해야 합니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [19080093](https://pubmed.ncbi.nlm.nih.gov/19080093/) | 2008 | 임상 연구 | Zhonghua Yi Xue Za Zhi | 선천성 심장병 소아의 체외순환 후 염증 반응과 폐 손상에 대한 Alprostadil·ulinastatin 효과 평가 |
| [6763200](https://pubmed.ncbi.nlm.nih.gov/6763200/) | 1982 | 임상 평가/증례 시리즈 | Pharmacotherapy | 우심실 유출로 폐쇄 영아에서 Alprostadil이 동맥관을 확장해 폐혈류를 증가시킴 |
| [15362549](https://pubmed.ncbi.nlm.nih.gov/15362549/) | 2004 | Review | Kyobu Geka | 대血管 전위 신생아에서 동맥관 개존 유지를 위해 Alprostadil alfadex 사용 |
| [19068708](https://pubmed.ncbi.nlm.nih.gov/19068708/) | 2008 | 증례 보고 | Kyobu Geka | 대동맥궁 단절 B형 신생아에서 동맥관 유지에 사용 후 일단계 수술 및 지속적 혈액투석여과로 생존 |
| [30184041](https://pubmed.ncbi.nlm.nih.gov/30184041/) | 2018 | 증례 보고 | Braz J Cardiovasc Surg | 복합 대동맥폐동맥 중격 결손 환아에서 수술 전 폐동맥압 감소 목적으로 milrinone과 병용 |
| [41167776](https://pubmed.ncbi.nlm.nih.gov/41167776/) | 2025 | 예비 임상 연구 | Zhonghua Fu Chan Ke Za Zhi | 복합 태아 선천성 심장병의 분만 방식·시기 탐색 (Alprostadil이 주제는 아님) |
| [42469655](https://pubmed.ncbi.nlm.nih.gov/42469655/) | 2026 | 후향적 예비 연구 | BMC Pregnancy Childbirth | 복합 태아 선천성 심장병의 임신·주산기 통합 관리 (Alprostadil이 주제는 아님) |
| [20029353](https://pubmed.ncbi.nlm.nih.gov/20029353/) | 2009 | 전임상(동물) | Minerva Chir | 흰쥐 골격근 허혈-재관류 손상 완화 (대동맥 기형과는 간접적 관련) |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 199802243 | 에글란딘주 (타나베파마코리아) | 유탁액 앰플 주사제 | 허가증 원문 링크로만 제공됨 |
| 200908752 | 알로스틴주사 프리필드 (동국제약) | 프리필드 주사제 (유탁액) | 허가증 원문 링크로만 제공됨 |
| 200705481 | 카버젝트주사 20마이크로그램 (한국화이자제약) | 동결건조분말 주사제 | 허가증 원문 링크로만 제공됨 |
| 200705483 | 카버젝트주사 10마이크로그램 (한국화이자제약) | 동결건조분말 주사제 | 허가증 원문 링크로만 제공됨 |

## 안전성 고려사항

- **금기 관련 지식 그래프 신호**: 라벨 문구가 아니라 지식 그래프의 약물-질환 금기 연결에서 확인된 항목입니다. 신생아 호흡곤란증후군, 급성 호흡곤란증후군, 저혈압, 혈액응고 질환, 겸상적혈구빈혈 및 헤모글로빈병증, 폐질환, 다발골수종, 백혈병(림프성·골수성), 혈소판증가증, 적혈구증가증, 유문협착, 지속발기증, 요도협착, 페이로니병, 귀두염 등이 포함됩니다.
- **문헌상 이상반응**: 장기 PGE1 투여 신생아에서 항(antral) 융모세포 증식 및 비후성 유문협착이 보고되었고, 의인성 슈도바터 증후군 증례도 있습니다.
- **약물 상호작용**: 총 59건이 확인되었습니다. 중등도로 분류된 약물은 canagliflozin, dapagliflozin, empagliflozin, ertugliflozin, lorcaserin, sapropterin입니다. 그 밖에 pantoprazole, morphine, metformin, omeprazole 등은 등급이 미분류입니다.

허가사항상의 경고·금기 문구는 확인되지 않았으므로 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
동맥관 의존성 대동맥 병변에서 Alprostadil을 쓰는 것은 이미 확립된 신생아 임상 관행으로 기전상 타당합니다. 그러나 현재 근거는 등록된 임상시험 없이 증례 보고와 소규모 연구에 한정되며(L4), 대동맥 기형 자체를 치료하는 것이 아니라 수술 전 가교 역할이라는 한계가 있습니다. 허가 적응증 및 안전성 문구도 확인되지 않아 현 단계에서는 연구 질문으로 유지하는 것이 적절합니다.

**진행하려면 필요한 것:**
- 허가증 PDF에서 허가 적응증, 경고, 금기 문구를 확인하여 기존 적응증과 신규 적응증의 중복 범위 정리
- DrugBank 등에서 상세 작용 기전(MOA) 데이터 확보
- 동맥관 의존성 대동맥 병변에 대한 체계적 문헌고찰 또는 코호트 근거 수집
- 신생아에서의 장기 투여 안전성(무호흡, 유문협착, 전해질 이상 등) 모니터링 계획 수립
- 낮은 순위 예측(선천성 삼첨판 협착, 판막 이형성증 등)은 근거가 TxGNN 점수뿐(L5)이므로 별도 근거 확보 전까지 보류
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

