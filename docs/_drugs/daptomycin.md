---
layout: default
title: Daptomycin
parent: 모델 예측만 (L5)
nav_order: 251
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-15
description: "Daptomycin: 예측 신규 적응증 골관절염 (osteoarthritis) (근거 수준 L5). 기존 적응증: 허가증에 적응증 원문이 아닌 링크만 기재되어 있어 확인할 수 없음 (허가사항 참조 필요)"
monitor_inn: "Daptomycin"
predicted_indications: ["osteoarthritis", "rheumatoid arthritis", "gout", "pseudoachondroplasia", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachyolmia-amelogenesis imperfecta syndrome"]
---

# Daptomycin
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

## Daptomycin: 그람양성균 감염에서 골관절염으로
{: .text-alpha }

## 한 문장 요약

Daptomycin은 그람양성균 감염 치료에 쓰이는 고리형 지질펩타이드 항생제입니다.
TxGNN 모델은 **골관절염(osteoarthritis)**에 효과가 있을 수 있다고 예측하지만, 뒷받침하는 문헌은 대부분 관절 *감염*에 관한 것이며 퇴행성 골관절염 치료와는 무관합니다.
현재 이 예측을 직접 지지하는 **임상시험은 0건**이고, 연관 문헌 **10편**은 감염 치료 연구입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가증에 적응증 원문이 아닌 링크만 기재되어 있어 확인할 수 없음 (허가사항 참조 필요) |
| 예측 신규 적응증 | 골관절염 (osteoarthritis) |
| TxGNN 예측 점수 | 0.9986 |
| 근거 수준 | L5 (모델 예측 중심. 관련 문헌은 감염 관련 코호트 연구로 골관절염 자체에 대한 근거가 아님) |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 6건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 일반적으로 daptomycin은 그람양성균의 세포막에 작용하는 항생제로 알려져 있으며, 한국에서는 주사제로 시판되고 있습니다.

TxGNN 모델(딥러닝)의 높은 점수는 모델이 '관절염'과 '관절 감염'처럼 관련된 질환 사이에서 학습한 유사성을 반영한 것일 수 있으며, 생물학적 근거는 아닙니다. 검색된 문헌은 인공관절 감염, 화농성 관절염, 골·관절 감염에서 daptomycin을 사용한 경험으로, 퇴행성 골관절염에 대한 질환 조절 효과를 보여주지 않습니다. 따라서 이것은 진정한 의미의 약물 재창출이라고 보기 어렵습니다.

참고로 같은 예측 목록의 2순위인 류마티스 관절염에서는 마우스 콜라겐 유발 관절염 모델에서 염증성 사이토카인과 NF-κB 경로를 억제했다는 전임상 연구(PMID 39571268)가 있어, 후속 검토 가치가 상대적으로 더 있습니다. 다만 사람 대상 자료는 없습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [23519823](https://pubmed.ncbi.nlm.nih.gov/23519823/) | 2013 | 코호트 | Int Orthop | 그람양성균 골관절 감염에서 고용량 daptomycin + rifampicin 병용의 안전성·효능 평가 |
| [17999973](https://pubmed.ncbi.nlm.nih.gov/17999973/) | 2008 | 코호트 | J Antimicrob Chemother | S. aureus 균혈증 동반 골관절 감염에서 daptomycin과 표준요법 비교 |
| [22511636](https://pubmed.ncbi.nlm.nih.gov/22511636/) | 2012 | 코호트 | J Antimicrob Chemother | 무릎·고관절 인공관절 감염에서 daptomycin 임상 경험 |
| [26235888](https://pubmed.ncbi.nlm.nih.gov/26235888/) | 2015 | 코호트 | Int J Antimicrob Agents | 복잡성 골·관절 및 임플란트 관련 감염에서 고용량 daptomycin(>6 mg/kg)의 효능과 안전성 |
| [21477701](https://pubmed.ncbi.nlm.nih.gov/21477701/) | 2010 | 코호트 | Med Clin (Barc) | 스페인 EU-CORE 데이터베이스의 daptomycin 사용 경험 |
| [23312602](https://pubmed.ncbi.nlm.nih.gov/23312602/) | 2013 | 설문 | Int J Antimicrob Agents | 성인 인공관절 감염 관리 현황 설문 |
| [22854340](https://pubmed.ncbi.nlm.nih.gov/22854340/) | 2012 | 시험관 연구 | J Antibiot | 인공관절 감염 유래 포도상구균의 항생제 감수성 |
| [25650692](https://pubmed.ncbi.nlm.nih.gov/25650692/) | 2015 | 코호트 | Surg Infect | 골관절 감염 유래 포도상구균의 10년간 미생물 프로파일 변화 |
| [32206362](https://pubmed.ncbi.nlm.nih.gov/32206362/) | 2020 | 증례 보고 | Case Rep Orthop | 골관절염으로 알려진 환자에서 발견된 만성 Corynebacterium striatum 화농성 관절염 |
| [41853106](https://pubmed.ncbi.nlm.nih.gov/41853106/) | 2026 | 증례 보고 | ASM Case Rep | 자연 관절에서 Corynebacterium propinquum에 의한 화농성 관절염 |

위 문헌은 모두 감염 상황에 관한 것으로, 골관절염 자체에 대한 치료 효과를 입증하지 않습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202007028 | 답토주350밀리그램 (영진약품) | 동결건조분말 주사제 | 허가사항 참조 |
| 202007027 | 답토주500밀리그램 (영진약품) | 동결건조분말 주사제 | 허가사항 참조 |
| 202005952 | 펜토신주350밀리그램 (건일제약) | 동결건조분말 주사제 | 허가사항 참조 |
| 202005951 | 펜토신주500밀리그램 (건일제약) | 동결건조분말 주사제 | 허가사항 참조 |
| 201900706 | 답토신주500밀리그램 (펜믹스) | 동결건조분말 주사제 | 허가사항 참조 |

## 안전성 고려사항

- **약물 상호작용**: 총 12건이 확인되었습니다.
  - 중등도(Moderate): Picosulfuric acid, Rosuvastatin, Simvastatin, Iobenguane (I-131), Ibuprofen, Diclofenac, Ethinylestradiol, Celecoxib, Cyclosporine, Mycophenolic acid
  - 경미(Minor): Dicoumarol, Warfarin
  - 스타틴 계열과의 병용은 근병증 위험과 관련해 특히 주의가 필요합니다.
- **기타 참고 사항**: 증례 보고(PMID 36693494)에서 daptomycin 유발 횡문근융해증 이후 급성 통풍성 관절염이 발생했습니다. 장기·전신 투여 시 근병증과 CPK 상승 위험을 고려해야 하며, 정맥 투여만 가능하다는 점도 만성 질환 적용의 현실적 장벽입니다.

그 밖의 경고 및 금기 사항은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
골관절염에 대한 임상시험이 없고, 연관 문헌은 모두 관절 감염에서의 항균 효과에 관한 것이어서 퇴행성 골관절염에 대한 근거가 되지 못합니다. 또한 정맥 투여와 근병증 위험은 만성 비감염성 질환에 적용하기에 큰 부담입니다.

**진행하려면 필요한 것:**
- 허가증별 적응증 원문 및 경고·금기 사항 (식약처 허가사항 PDF 확인)
- 상세한 작용 기전(MOA) 데이터
- 비감염성 관절염에서의 항염증 효과를 뒷받침하는 추가 전임상 연구 (예: 류마티스 관절염 모델 결과 재현)
- 골관절염에서 항염증 작용이 성립하는지에 대한 기전 검증

**참고 (다른 예측 질환):**
- 류마티스 관절염: 전임상 근거(L4)만 있으며, 연구 질문(Research Question) 수준입니다.
- 골관절염 감수성, 통풍, 가성연골무형성증 등 나머지 예측은 근거가 없거나 부작용 신호만 있어 보류(Hold)를 권장합니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

