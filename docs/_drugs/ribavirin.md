---
layout: default
title: Ribavirin
parent: 모델 예측만 (L5)
nav_order: 651
evidence_level: L5
indication_count: 10
---

# Ribavirin
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
{: .fs-6 .fw-300 }

---

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 약사 평가 보고서

</div>

# Ribavirin: 바이러스성 감염증에서 만성 B형 간염으로

## 한 문장 요약

Ribavirin은 구아노신 유사체 계열의 항바이러스제로, 한국에서 단일 성분 캡슐제로 허가·시판되고 있습니다.
TxGNN 모델은 **만성 B형 간염(chronic hepatitis B virus infection)**에 효과가 있을 수 있다고 예측하며, 이를 다룬 **임상시험 15건**과 **문헌 19편**이 검색되었습니다. 다만 상당수는 C형 간염 중심이어서 직접적인 근거는 제한적입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문은 허가증 PDF 링크로만 제공되어 확인하지 못했습니다 |
| 예측 신규 적응증 | 만성 B형 간염 (chronic hepatitis B virus infection) |
| TxGNN 예측 점수 | 99.86% |
| 근거 수준 | L2 (아래 설명 참조) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 20건 (모두 유효, 단일 성분) |
| 권장 결정 | Hold (연구 질문 단계) |

> 근거 수준 L2는 완료된 Phase 2/3 임상시험(NCT00275938)과 Phase 3 임상시험(NCT00114361)을 근거로 한 판정입니다. 다만 두 시험 모두 ribavirin 단독의 추가 효과를 분리해서 보여주는지 확인되지 않았고, 결과 데이터도 없습니다. 따라서 실제 근거 강도는 L2보다 낮게 보수적으로 해석해야 합니다.

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 입력되지 않았습니다. 일반적으로 알려진 바에 따르면 ribavirin은 구아노신 유사체로 바이러스 RNA 중합효소와 IMPDH를 억제하여 GTP 풀을 고갈시키고, 면역조절 효과도 가집니다.

다만 B형 간염 바이러스(HBV)는 역전사로 복제하는 DNA 바이러스이므로 ribavirin의 직접적인 항바이러스 효과는 제한적입니다. 이점이 있다면 peginterferon과 병용할 때 인터페론 매개 면역반응을 강화하는 간접 효과일 가능성이 큽니다.

HBV 치료의 표준은 핵산(뉴클레오시드/뉴클레오티드) 유사체와 peginterferon 단독요법입니다. 따라서 ribavirin 추가의 이득은 ribavirin 특이적 무작위 임상 근거로 확인되어야 합니다.

## 임상시험 근거

HBV와 직접 관련된 시험을 우선하여 정리했습니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00114361](https://clinicaltrials.gov/study/NCT00114361) | Phase 3 | 완료 | 138 | HBeAg 음성 만성 B형 간염에서 PEG-IFN + ribavirin 병용 vs PEG-IFN 단독 비교 (결과 미확인) |
| [NCT00275938](https://clinicaltrials.gov/study/NCT00275938) | Phase 2/3 | 완료 | 120 | 만성 B형 간염에서 인터페론 알파-2b + ribavirin 파일럿 연구 |
| [NCT03759782](https://clinicaltrials.gov/study/NCT03759782) | Phase 3 | 불명 | 24 | HBV 핵산유사체 치료에 ribavirin을 병용하는 면역조절 파일럿 |
| [NCT00154869](https://clinicaltrials.gov/study/NCT00154869) | Phase 3 | 불명 | 320 | HCV/HBV 동시감염 환자에서 PEG-IFN α-2a + ribavirin 비교 |
| [NCT00117533](https://clinicaltrials.gov/study/NCT00117533) | Phase 4 | 불명 | 20 | HBV/HDV 이중감염에서 PEG-IFN α-2b + ribavirin 파일럿 |
| [NCT02219477](https://clinicaltrials.gov/study/NCT02219477) | Phase 3 | 완료 | 36 | 대상성 간경변 HCV에서 DAA + ribavirin (HBV 근거 아님) |
| [NCT01447420](https://clinicaltrials.gov/study/NCT01447420) | Phase 4 | 완료 | 129 | HCV 유전자형 1에서 PEG-IFN + ribavirin과 IL-28B 발현 (간접적) |
| [NCT01425970](https://clinicaltrials.gov/study/NCT01425970) | Phase 2 | 조기 종료 | 210 | HCV 유전자형 2/3에서 INX-08189 병용 (간접적) |

나머지 시험(NCT01195181, NCT01795911, NCT01309932, NCT00911963, NCT03186313, NCT02483156, NCT01001754, NCT01830127)은 HCV 연구로, ribavirin은 배경 약물이므로 HBV 근거로 보기 어렵습니다.

## 문헌 근거

검색된 문헌은 대부분 HBV/HCV를 함께 다루는 리뷰이며, ribavirin의 HBV 효능을 직접 검증한 무작위 임상시험 논문은 없습니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [32664198](https://pubmed.ncbi.nlm.nih.gov/32664198/) | 2020 | Review | Viruses | HCV/HBV 동시감염 개관. HCV RNA 양성 시 PEG-IFN + ribavirin이 권고되었음 |
| [24659886](https://pubmed.ncbi.nlm.nih.gov/24659886/) | 2014 | Review | World J Gastroenterol | HCV/HBV 이중감염의 치료와 예후 |
| [25048716](https://pubmed.ncbi.nlm.nih.gov/25048716/) | 2015 | Review | Hepatology | 만성 HBV·HCV 항바이러스 치료의 면역학적 측면 |
| [25232239](https://pubmed.ncbi.nlm.nih.gov/25232239/) | 2014 | Review | World J Gastroenterol | IL28B 유전자 다형성과 HBV 감염의 관련성 |
| [26284971](https://pubmed.ncbi.nlm.nih.gov/26284971/) | 2015 | Review | Curr Opin Virol | IL28B 유전자형이 HBV·HCV 감염에 미치는 영향 |
| [24379612](https://pubmed.ncbi.nlm.nih.gov/24379612/) | 2013 | Review | World J Gastroenterol | 만성 B·C형 간염에서 간세포암 예방 |
| [17009938](https://pubmed.ncbi.nlm.nih.gov/17009938/) | 2006 | Review | Expert Rev Anti Infect Ther | 소아 만성 B·C형 간염 치료 옵션 |
| [11160766](https://pubmed.ncbi.nlm.nih.gov/11160766/) | 2001 | Review | Annu Rev Med | 만성 B·C형 간염의 치료 전략 |

## 한국 시판 정보

허가 적응증 본문은 허가증 PDF 링크로만 제공되어 요약하지 못했습니다. 아래는 주요 허가 5건이며, 20건 중 다수가 수출용입니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200703103 | 바이라미드캡슐200mg (일성아이에스) | 경질캡슐 | 허가증 원문 참조 |
| 198200958 | 바이라미드캡슐100mg (일성아이에스) | 젤라틴캡슐 | 허가증 원문 참조 |
| 201701378 | 중헌리바비린캡슐200밀리그램 (중헌제약) | 경질캡슐 | 허가증 원문 참조 |
| 200301870 | 바빌캅셀 (바스칸바이오제약, 수출용) | 경질캡슐 | 허가증 원문 참조 |
| 200410983 | 신풍리바비린캡슐200밀리그람 (신풍제약, 수출용) | 경질캡슐 | 허가증 원문 참조 |

## 안전성 고려사항

허가사항의 경고·금기 정보는 이번 자료에 포함되지 않았으므로 허가사항을 참조하세요.

- **지식그래프 기반 금기 질환(허가 문구 아님)**: 만성 폐쇄성 폐질환, 천식, 간경변, 유육종증, 겸상적혈구빈혈, 심근경색, 관상동맥질환, 용혈성 빈혈 및 기타 빈혈, 범혈구감소증, 간질성 폐질환, 신기능 장애, 췌장염, 자가면역간염 등이 연결되어 있습니다. 이 목록은 허가 문구가 아니므로 참고용으로만 사용해야 합니다.
- **약물 상호작용**: 상호작용 후보 100건이 조회되었으나(예: 칼시트리올, 판토프라졸, 글리메피리드, 메트포르민, 프레드니손, 암포테리신 B), 등급은 모두 확인되지 않았습니다.
- **참고**: 문헌에는 PEG-IFN/ribavirin 치료 중 포르피린증(PCT)이 유발·드러난 사례가 보고되어 있습니다. 또한 용혈성 빈혈 위험은 간질환 환자에서 특히 문제가 될 수 있습니다.

## 결론 및 다음 단계

**결정: Hold (연구 질문 단계)**

**사유:**
HBV를 직접 다룬 Phase 3 시험(NCT00114361)과 Phase 2/3 파일럿(NCT00275938)이 있지만, ribavirin 단독의 추가 효과를 보여주는 결과가 확인되지 않았습니다. 기전상 직접 항HBV 활성이 제한적이고, HBV에는 이미 핵산유사체와 peginterferon이라는 확립된 표준치료가 있으며, 나머지 근거는 대부분 HCV 관련입니다.

**진행하려면 필요한 것:**
- NCT00114361, NCT00275938의 투약군 구성과 결과 확인 (PEG-IFN 단독 대비 ribavirin 추가 이득)
- NCT03759782(핵산유사체 + ribavirin) 결과 확인
- 허가사항의 경고·금기 정보 확보 (현재 안전성 검토 진행 불가)
- 상세 작용 기전(MOA) 데이터 확보
- 한국 허가 적응증 원문 확인
- 용혈성 빈혈 등 간질환 환자에서의 위험·이익 평가

**참고(상위 예측 중 나머지 적응증):** 순위 2~10위 예측(특발성 구리 관련 간경변, 간문맥 고혈압, 간폐증후군 등)은 임상시험이나 의미 있는 문헌이 없고 기전적 연결도 불분명하여 모두 Hold입니다. 간성 포르피린증은 문헌상 ribavirin 병용요법이 치료가 아니라 유발 요인으로 보고된 안전성 신호입니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

