---
layout: default
title: 데이터 출처
nav_order: 93
permalink: /sources/
description: "KrTxGNN의 데이터 출처: MFDS 허가 데이터, TxGNN, ClinicalTrials.gov, PubMed, DrugBank."
---

# 데이터 출처

<div class="key-takeaway">
모든 결론은 공개 데이터 출처로 거슬러 올라갈 수 있습니다 — 블랙박스는 없습니다.
</div>

---

## 출처 개요

<table class="comparison-table">
<thead>
<tr><th>유형</th><th>출처</th><th>용도</th></tr>
</thead>
<tbody>
<tr><td>허가 데이터</td><td><a href="https://www.mfds.go.kr/">MFDS</a></td><td>대한민국 허가 의약품 목록 및 성분</td></tr>
<tr><td>예측 모델</td><td><a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/">TxGNN</a></td><td>약물&ndash;질병 연관성 예측</td></tr>
<tr><td>임상시험</td><td><a href="https://clinicaltrials.gov/">ClinicalTrials.gov</a></td><td>근거 등급화 (NCT)</td></tr>
<tr><td>문헌</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a></td><td>근거 등급화 (PMID)</td></tr>
<tr><td>의약품 정보</td><td><a href="https://go.drugbank.com/">DrugBank</a></td><td>성분 매핑 및 표적 데이터</td></tr>
<tr><td>상호작용</td><td><a href="https://ddinter2.scbdd.com/">DDInter</a></td><td>약물&ndash;약물 상호작용 데이터</td></tr>
</tbody>
</table>

---

## 라이선스

각 출처에는 고유한 라이선스가 있으므로 인용 전에 반드시 확인하십시오:

- **TxGNN**: 학술 용도; Huang et al. (2023) 인용 필요
- **ClinicalTrials.gov / PubMed**: 미국 NIH 공개 데이터
- **DrugBank**: 해당 라이선스 조건에 따른 비상업적 용도
- **MFDS**: 대한민국 규제 기관의 공공데이터 이용 약관 적용

---

## 갱신 주기

| 데이터 | 주기 |
|------|-----------|
| 허가 데이터 | 규제 기관 공개 시점에 따름 |
| 임상시험 / 문헌 근거 | 주기적으로 재수집 |
| 상호작용 데이터 | 분기별 검토 |

---

## 학술 인용

> Huang, K., et al. (2023). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-023-02233-x](https://doi.org/10.1038/s41591-023-02233-x)

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
