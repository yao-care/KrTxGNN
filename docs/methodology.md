---
layout: default
title: 방법론
nav_order: 91
permalink: /methodology/
description: "KrTxGNN이 예측을 생성하고 검증하는 방법: TxGNN 지식 그래프 예측, 근거 수집, L1-L5 등급화, 의사결정 권고."
---

# 방법론

<div class="key-takeaway">
AI 예측에서 근거 등급화까지 — 모든 후보는 등급 판정의 근거를 추적할 수 있습니다.
</div>

---

## 전체 파이프라인

<p class="key-answer" data-question="KrTxGNN은 어떻게 예측을 생성합니까?">
본 플랫폼은 4단계 파이프라인을 사용합니다. TxGNN 지식 그래프 모델이 잠재적인 약물&ndash;질병
연관성을 예측하고, 예측된 각 쌍에 대해 근거를 자동으로 수집하며, 그 근거를 L1부터 L5까지
등급화한 뒤, 최종적으로 의사결정 권고를 제시합니다.
</p>

<ol class="actionable-steps">
<li><strong>TxGNN 예측</strong>: 지식 그래프와 그래프 신경망을 결합하여 약물&ndash;질병 관계를 예측합니다.</li>
<li><strong>근거 수집</strong>: 예측된 각 쌍에 대해 ClinicalTrials.gov, PubMed, DrugBank, MFDS에서 근거를 수집합니다.</li>
<li><strong>근거 등급화</strong>: L1부터 L5까지 등급을 부여하며, L1이 가장 강력하고(다수의 3상 RCT) L5는 모델 예측만 있는 경우입니다.</li>
<li><strong>의사결정 권고</strong>: 근거 수준에 따라 Go, Proceed, Consider, Explore, Hold 중 하나를 제시합니다.</li>
</ol>

---

## 근거 등급 기준

<table class="comparison-table">
<thead>
<tr><th>등급</th><th>정의</th><th>임상적 의미</th></tr>
</thead>
<tbody>
<tr><td><strong>L1</strong></td><td>다수의 3상 RCT / 체계적 문헌고찰</td><td>강력한 근거; 임상 적용을 고려할 수 있음</td></tr>
<tr><td><strong>L2</strong></td><td>단일 RCT 또는 다수의 2상 시험</td><td>중등도 근거; 검증 시험을 설계할 수 있음</td></tr>
<tr><td><strong>L3</strong></td><td>관찰 연구 / 대규모 증례 시리즈</td><td>예비적 근거; 추가 검증이 필요함</td></tr>
<tr><td><strong>L4</strong></td><td>전임상 / 기전 연구</td><td>이론적 근거; 임상 적용과는 거리가 있음</td></tr>
<tr><td><strong>L5</strong></td><td>모델 예측만 존재</td><td>가설 단계; 사람 대상 근거 없음</td></tr>
</tbody>
</table>

---

## 이중 엔진 예측

두 가지 방법을 병렬로 실행하고, 두 결과의 일치 여부를 신뢰도 라벨로 기록합니다:

| 방법 | 속도 | 정밀도 | 설명 |
|--------|-------|-----------|-------------|
| 지식 그래프 (KG) | 빠름 | 낮음 | DrugBank 관계와 그래프 구조에 기반한 추론 |
| 딥러닝 (DL) | 느림 | 높음 | TxGNN 그래프 신경망 모델 |

| 신뢰도 | 출처 | 의미 |
|------------|--------|---------|
| very_high | KG + DL | 두 방법의 결과가 일치 |
| high | DL만 | 딥러닝의 높은 점수로 뒷받침됨 |
| medium | KG만 | 지식 그래프로 뒷받침됨 |

---

## 규제 데이터 통합

대한민국 의약품 허가 데이터는 MFDS에서 가져옵니다. 성분명은 DrugBank 어휘집에 매핑되며,
생약 추출물, 백신, 첨가제 등 DrugBank에 등재되지 않아 매핑할 수 없는 성분은 예측 대상에서
제외됩니다.

---

## 한계

<ol class="actionable-steps">
<li>예측 결과는 통계적 연관성이며 <strong>인과관계나 임상적 유효성을 의미하지 않습니다</strong>.</li>
<li>L5 등급은 모델 예측만 존재하며 사람 대상의 뒷받침 근거가 없다는 뜻입니다.</li>
<li>근거 수집은 공개 데이터베이스에 의존하므로, 미발표되었거나 색인되지 않은 연구는 포착되지 않습니다.</li>
<li>성분 매핑은 명칭 차이로 인해 일부 항목이 누락될 수 있습니다.</li>
</ol>

---

## 개발사 소개

본 플랫폼은 **藥提醒科技有限公司** (yao.care, 사업자등록번호 83620786, 12F, No. 220, Sec. 2,
Taiwan Blvd., West Dist., Taichung City, Taiwan)가 개발하고 운영합니다.

KrTxGNN은 이 회사의 "TxGNN 약물재창출" 제품군 중 대한민국 사이트입니다.
동일한 시스템이 30개 국가 및 지역에 배포되어 있으며, 각각 `{CC}TxGNN`
(JpTxGNN, UsTxGNN, DETxGNN 등)으로 명명되어 `{cc}txgnn.yao.care`에서 운영됩니다.
제품 개요: <https://www.yao.care/medical/txgnn/>.

TxGNN 모델 자체는 Harvard Medical School의 Zitnik Lab이 개발하여 *Nature Medicine*에
발표했습니다. 본 플랫폼은 藥提醒科技有限公司가 해당 모델을 기반으로 구축한 운영 시스템으로,
국가별 의약품 허가 데이터 통합, 지식 그래프와 딥러닝의 이중 예측, PubMed / ClinicalTrials
근거 등급화, SMART on FHIR 전자의무기록 연동을 포함합니다.

---

<div class="disclaimer">
<strong>면책 조항</strong><br>
본 보고서는 학술 연구 참고용으로만 제공되며 <strong>의료 조언을 구성하지 않습니다</strong>. 반드시 담당 의사의 지시를 따르시고, 임의로 약물을 조정하지 마십시오. 모든 약물재창출 결정은 완전한 임상 검증과 규제 당국의 심사를 거쳐야 합니다.
<br><br>
<small>검토: 藥提醒科技有限公司 (yao.care)</small>
</div>
