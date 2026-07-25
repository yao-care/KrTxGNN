---
layout: default
title: 사용 안내
nav_order: 92
permalink: /guide/
description: "KrTxGNN 사용 안내: 의약품 검색 방법, 근거 등급 읽는 법, 권고 해석 방법."
---

# 사용 안내

<div class="key-takeaway">
근거 등급을 먼저 확인하고, 그다음 권고를 보고, 마지막으로 원문 문헌을 읽으십시오.
</div>

---

## 의약품 검색하기

<ol class="actionable-steps">
<li>페이지 상단의 검색창을 이용하십시오(제품명보다 성분명으로 검색하면 더 잘 찾을 수 있습니다).</li>
<li>또는 <a href="{{ '/drugs/' | relative_url }}">전체 의약품</a>에서 전체 목록을 살펴보십시오.</li>
<li>근거 등급별로 살펴볼 수도 있습니다: <a href="{{ '/evidence-high/' | relative_url }}">높음</a>, <a href="{{ '/evidence-medium/' | relative_url }}">중등도</a>, <a href="{{ '/evidence-low/' | relative_url }}">모델 예측만</a>.</li>
</ol>

---

## 보고서 읽는 법

<p class="key-answer" data-question="근거 등급 L1부터 L5까지는 무엇을 의미합니까?">
각 의약품 보고서에는 예측된 새로운 적응증이 나열되며, 각 적응증에는 L1&ndash;L5의 근거 등급이
부여됩니다. <strong>L1은 다수의 3상 무작위 대조 시험이 이미 뒷받침하고 있다는 뜻이고, L5는
모델 예측만 있을 뿐 사람 대상 근거가 없다는 뜻입니다.</strong> 전체 기준은
<a href="{{ '/methodology/' | relative_url }}">방법론</a> 페이지에 있습니다.
</p>

| 표시된 등급 | 의미 | 권장 조치 |
|-----------|----------|------------------|
| L1 / L2 | 임상시험 근거가 존재함 | 원문 NCT 및 PMID 기록을 확인 |
| L3 / L4 | 관찰 연구 또는 전임상 근거 | 연구 단서로 활용 |
| L5 | 모델 예측만 존재 | 가설 도출 용도로만 사용; 임상 참고 불가 |

---

## 인용과 추적 가능성

보고서에 실린 모든 근거에는 추적 가능한 식별자가 붙어 있습니다:

- **NCT 번호**: ClinicalTrials.gov 등록 정보로 연결
- **PMID**: PubMed 문헌 기록으로 연결
- **DrugBank ID**: 약물 및 표적 데이터로 연결

본 플랫폼의 결론을 인용하기 전에 반드시 원문 문헌을 읽고 맥락을 확인하십시오.

---

## 자주 묻는 질문

<p class="key-answer" data-question="예측 결과를 임상에 사용할 수 있습니까?">
<strong>사용할 수 없습니다.</strong> 본 플랫폼의 예측은 연구 단서일 뿐 임상 조언이 아닙니다.
약물재창출을 임상에 적용하려면 반드시 완전한 임상시험 검증과 규제 당국의 심사를 거쳐야
합니다.
</p>

<p class="key-answer" data-question="특정 의약품을 찾을 수 없는 이유는 무엇입니까?">
성분이 DrugBank 어휘집에 매핑되어야만 예측 대상에 포함됩니다. 생약 추출물, 백신, 첨가제 등
DrugBank에 등재되지 않은 항목은 본 플랫폼에 표시되지 않습니다.
</p>

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
