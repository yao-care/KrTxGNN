# KrTxGNN - 한국: 약물 재창출 예측

[![Website](https://img.shields.io/badge/Website-krtxgnn.yao.care-blue)](https://krtxgnn.yao.care)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

TxGNN 모델을 사용한 한국 의약품에 대한 약물 재창출(drug repurposing) 예측.

## 주의사항

- 본 프로젝트의 결과는 연구 목적으로만 사용되며 의료 조언을 구성하지 않습니다.
- 약물 재창출 후보는 적용 전에 임상 검증이 필요합니다.

## 프로젝트 개요

| 항목 | 수량 |
|------|------|
| **의약품 보고서** | 533 |
| **총 예측 수** | 38,275,274 |

## 예측 방법

### 지식 그래프 방법 (Knowledge Graph)
TxGNN 지식 그래프에서 약물-질병 관계를 직접 조회하여 생물의학 네트워크의 기존 연결을 기반으로 잠재적인 재창출 후보를 식별합니다.

### 딥러닝 방법 (Deep Learning)
TxGNN 사전 훈련된 신경망 모델을 사용하여 예측 점수를 계산하고, 승인된 약물의 새로운 치료 적응증 가능성을 평가합니다.

## 링크

- 웹사이트: https://krtxgnn.yao.care
- TxGNN 논문: https://doi.org/10.1038/s41591-023-02233-x
