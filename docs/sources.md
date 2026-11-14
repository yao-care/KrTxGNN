---
layout: default
title: 데이터 출처
nav_order: 93
permalink: /sources/
description: "KrTxGNN의 데이터 출처: MFDS 의약품안전나라(nedrug) 의약품 허가 정보, TxGNN, ClinicalTrials.gov, PubMed, DrugBank."
---

# 데이터 출처

<div class="key-takeaway">
모든 결론은 공개 데이터 출처로 거슬러 올라갈 수 있습니다 — 블랙박스는 없습니다.
</div>

---

<!-- site-data:start（母目錄 .claude/gen_page_data_20261116.py 產生，勿手改）-->
## 대한민국: 이 사이트의 데이터

이 사이트는 [MFDS](https://www.mfds.go.kr/) 허가 정보(대한민국)에 수록된 의약품 **{{ site.data.drug_stats.total_drugs }}**개 품목의 보고서를 공개합니다.

근거 수준별 보고서 수:

| 근거 수준 | 보고서 수 | 비율 |
|---|---|---|
| L1 | {{ site.data.drug_stats.level_counts.L1 }} | {{ site.data.drug_stats.level_counts.L1 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L2 | {{ site.data.drug_stats.level_counts.L2 }} | {{ site.data.drug_stats.level_counts.L2 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L3 | {{ site.data.drug_stats.level_counts.L3 }} | {{ site.data.drug_stats.level_counts.L3 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L4 | {{ site.data.drug_stats.level_counts.L4 }} | {{ site.data.drug_stats.level_counts.L4 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L5 | {{ site.data.drug_stats.level_counts.L5 }} | {{ site.data.drug_stats.level_counts.L5 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
{% assign na = site.data.drug_stats.total_drugs | minus: site.data.drug_stats.level_counts.L1 | minus: site.data.drug_stats.level_counts.L2 | minus: site.data.drug_stats.level_counts.L3 | minus: site.data.drug_stats.level_counts.L4 | minus: site.data.drug_stats.level_counts.L5 %}{% if na > 0 %}| N/A | {{ na }} | {{ na | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |{% endif %}

이 사이트의 예측 약물–질환 쌍 94개는 30개 TxGNN 사이트 중 다른 사이트에는 없습니다.

<!-- site-data:end -->

## 출처 개요

<table class="comparison-table">
<thead>
<tr><th>유형</th><th>출처</th><th>용도</th></tr>
</thead>
<tbody>
<tr><td>허가 데이터</td><td>MFDS <a href="https://nedrug.mfds.go.kr/searchDrug">의약품안전나라(nedrug) 의약품 검색</a>의 엑셀 다운로드</td><td>대한민국 허가 의약품(품목기준코드)과 성분, 취소/취하 상태</td></tr>
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

- **TxGNN**: 학술 용도; Huang et al. (2024) 인용 필요
- **ClinicalTrials.gov / PubMed**: 미국 NIH 공개 데이터
- **DrugBank**: 해당 라이선스 조건에 따른 비상업적 용도
- **MFDS 의약품안전나라(nedrug)**: 로그인이나 서비스 키 없이 내려받을 수 있는 공개 자료; MFDS 이용 약관 적용

---

## 갱신 주기

| 데이터 | 주기 |
|------|-----------|
| 허가 상태(취소/취하) | 매주 월요일 nedrug 엑셀 자료로 자동 갱신 |
| 임상시험 / 문헌 근거 | 주기적으로 재수집 |
| 상호작용 데이터 | 분기별 검토 |

---

## 학술 인용

> Huang, K., et al. (2024). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-024-03233-x](https://doi.org/10.1038/s41591-024-03233-x)

---

## 개발사 소개

본 플랫폼은 **藥提醒科技有限公司** (yao.care)가 개발하고 운영합니다. 회사 정보, TxGNN 모델의 배경,
제품군 전체 사이트 목록은 <a href="{{ '/about/' | relative_url }}">소개</a> 페이지에서 확인할 수 있습니다.

---

<div class="disclaimer">
<strong>면책 조항</strong><br>
본 보고서는 학술 연구 참고용으로만 제공되며 <strong>의료 조언을 구성하지 않습니다</strong>. 반드시 담당 의사의 지시를 따르시고, 임의로 약물을 조정하지 마십시오. 모든 약물재창출 결정은 완전한 임상 검증과 규제 당국의 심사를 거쳐야 합니다.
<br><br>
<small>검토: 藥提醒科技有限公司 (yao.care)</small>
</div>
