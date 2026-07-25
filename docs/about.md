---
layout: default
title: 소개
nav_order: 90
permalink: /about/
description: "KrTxGNN은 藥提醒科技有限公司 (yao.care)가 Harvard TxGNN 모델을 기반으로 개발한 약물재창출 예측 플랫폼으로, 대한민국 MFDS 허가 의약품을 대상으로 합니다."
---

# 소개

<div class="key-takeaway">
AI로 약물재창출 근거 검증을 가속화합니다 — 예측부터 근거까지 한눈에.
</div>

---

## 배경

<p class="key-answer" data-question="KrTxGNN이란 무엇입니까?">
<strong>KrTxGNN</strong>은 Harvard 대학교 Zitnik Lab이 <em>Nature Medicine</em>에 발표한 TxGNN
모델을 기반으로 구축한 약물재창출 연구 지원 플랫폼입니다. 대한민국 MFDS가 허가한 의약품의
적응증 확대를 예측합니다. AI 예측 점수뿐만 아니라 ClinicalTrials.gov와 PubMed의 임상 근거를
통합하여, 연구자가 각 예측의 신뢰도를 신속하게 평가할 수 있도록 합니다.
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

## 약물재창출이란?

<p class="key-answer" data-question="약물재창출이란 무엇입니까?">
<strong>약물재창출</strong>이란 기존 의약품에서 새로운 치료 용도를 찾는 것을 말합니다.
신약을 처음부터 개발하는 경우 10~15년과 10억&ndash;20억 미국 달러가 소요되는 데 비해,
약물재창출은 3~5년과 1억&ndash;3억 미국 달러가 소요되며 사람에 대한 안전성 데이터가 이미
존재하므로 실패 위험이 낮습니다.
</p>

<table class="comparison-table">
<thead>
<tr><th>항목</th><th>신약 개발</th><th>약물재창출</th></tr>
</thead>
<tbody>
<tr><td>기간</td><td>10&ndash;15년</td><td>3&ndash;5년</td></tr>
<tr><td>비용</td><td>10억&ndash;20억 미국 달러</td><td>1억&ndash;3억 미국 달러</td></tr>
<tr><td>안전성 데이터</td><td>새로 확보해야 함</td><td>사람 데이터가 이미 존재</td></tr>
<tr><td>실패 위험</td><td>매우 높음 (&gt;90%)</td><td>비교적 낮음</td></tr>
</tbody>
</table>

---

## TxGNN이란?

<p class="key-answer" data-question="TxGNN이란 무엇입니까?">
<a href="https://www.nature.com/articles/s41591-023-02233-x">TxGNN</a>은 Harvard Medical School의
Zitnik Lab이 개발하여 <em>Nature Medicine</em>에 발표한 딥러닝 모델입니다.
새로운 약물&ndash;질병 연관성을 예측하며, 임상의를 위해 특별히 설계된 최초의 약물재창출
파운데이션 모델입니다.
</p>

<blockquote class="expert-quote">
"TxGNN은 17,080개 생의학 개체로 이루어진 지식 그래프를 통합하고 그래프 신경망을 사용하여
노드 간의 복잡한 관계를 학습함으로써, 희귀질환에 대한 약물의 잠재적 효능을 예측합니다."
<cite>&mdash; Huang et al., Nature Medicine (2023)</cite>
</blockquote>

---

## 데이터 출처

<table class="comparison-table">
<thead>
<tr><th>유형</th><th>출처</th><th>설명</th></tr>
</thead>
<tbody>
<tr><td>AI 예측</td><td><a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/">TxGNN</a></td><td>Harvard 지식 그래프 예측 모델</td></tr>
<tr><td>임상시험</td><td><a href="https://clinicaltrials.gov/">ClinicalTrials.gov</a></td><td>글로벌 임상시험 등록 정보</td></tr>
<tr><td>문헌</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a></td><td>생의학 문헌 데이터베이스</td></tr>
<tr><td>의약품 정보</td><td><a href="https://go.drugbank.com/">DrugBank</a></td><td>약물 및 표적 데이터베이스</td></tr>
<tr><td>허가 데이터</td><td><a href="https://www.mfds.go.kr/">MFDS</a></td><td>대한민국 의약품 허가 데이터</td></tr>
</tbody>
</table>

---

## 학술적 근거

> Huang, K., et al. (2023). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-023-02233-x](https://doi.org/10.1038/s41591-023-02233-x)

---

## 규모

| 항목 | 값 |
|------|-------|
| 의약품 보고서 | {{ site.drugs.size }} |
| 규제 기관 | MFDS |
| 배포 사이트 | 30개 국가 / 지역 |

---

## 연락처

- **GitHub Issues**: <https://github.com/yao-care/KrTxGNN/issues>
- **개발사**: 藥提醒科技有限公司 (<https://www.yao.care>, service@yao.care)
- **제품 개요**: <https://www.yao.care/medical/txgnn/>

---

<div class="disclaimer">
<strong>면책 조항</strong><br>
본 보고서는 학술 연구 참고용으로만 제공되며 <strong>의료 조언을 구성하지 않습니다</strong>. 반드시 담당 의사의 지시를 따르시고, 임의로 약물을 조정하지 마십시오. 모든 약물재창출 결정은 완전한 임상 검증과 규제 당국의 심사를 거쳐야 합니다.
<br><br>
<small>검토: 藥提醒科技有限公司 (yao.care)</small>
</div>
