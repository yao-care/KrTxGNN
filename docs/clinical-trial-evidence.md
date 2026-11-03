---
layout: default
title: "새 적응증에 임상시험 근거가 있는 국내 의약품"
nav_order: 25
permalink: /clinical-trial-evidence/
description: "MFDS 허가 의약품 중 TxGNN이 예측한 신규 적응증에 임상시험 근거(L1–L2)가 있는 의약품: 예측 적응증, 근거 수준, 등록 임상시험 수."
last_modified_at: 2026-11-03
---
{%- comment -%}
2026-11-03：回答 AI 搜尋常問的「本國藥物中，哪些新適應症有臨床試驗證據」。全表由 Liquid 從藥物頁產生，不寫死藥名或數字。
收錄＝公開藥物頁（排除 id_redirect 與 noindex）中 evidence_level 為 L1 或 L2（本站 evidence-high 標準：L1 多個 Phase 3 RCT／系統性回顧，
L2 單一 RCT 或多個 Phase 2 試驗）。預測新適應症與等級註記取自各藥物頁快速總覽表；下列欄名是本站藥物頁實際用到的寫法（建頁時逐頁核對），
新寫法抓不到時顯示「보고서 참조」、等級仍取 front matter。試驗數＝該藥物頁引用的不重複 NCT 編號數。
{%- endcomment -%}
{%- assign ind_labels = "예측 신규 적응증" | split: "|" -%}
{%- assign lev_labels = "근거 수준" | split: "|" -%}
{%- assign listed = site.drugs | where_exp: "d", "d.layout != 'id_redirect'" | where_exp: "d", "d.noindex != true" -%}
{%- assign l1 = listed | where: "evidence_level", "L1" | sort: "title" -%}
{%- assign l2 = listed | where: "evidence_level", "L2" | sort: "title" -%}
{%- assign trial_drugs = l1 | concat: l2 -%}
{%- assign latest = trial_drugs | sort: "last_modified_at" | last -%}
{%- assign latest_date = latest.last_modified_at | date: "%Y-%m-%d" -%}

# 새 적응증에 임상시험 근거가 있는 국내 의약품

<p class="key-answer" data-question="국내 의약품 중 새 적응증에 대한 임상시험 근거가 있는 것은 무엇입니까?">
KrTxGNN 보고서가 있는 의약품 {{ listed.size }}개 중 <strong>{{ trial_drugs.size }}</strong>개는 TxGNN이 예측한 신규 적응증의 근거 수준이 <strong>L1 또는 L2</strong>(L1 {{ l1.size }}개, L2 {{ l2.size }}개)로, 임상시험 근거(무작위 대조시험, 2–3상 시험 또는 체계적 문헌고찰)가 확인되었습니다.
</p>

의약품 목록은 MFDS [의약품안전나라](https://nedrug.mfds.go.kr/searchDrug)의 허가 데이터를 바탕으로 하며, 이 목록은 {{ latest_date }}에 마지막으로 갱신된 약물 보고서를 반영합니다.

<div class="key-takeaway">
예측 적응증에 대한 시험 근거가 효과를 입증하는 것은 아닙니다. 아래 후보는 모두 임상 사용 전에 여전히 <strong>임상 검증</strong>과 규제 심사가 필요합니다.
</div>

---

## 시험 근거가 있는 의약품 (L1–L2)

<div class="table-wrapper"><table>
<thead>
<tr><th>의약품</th><th>예측 신규 적응증</th><th>근거 수준</th><th>인용된 등록 임상시험 (NCT)</th></tr>
</thead>
<tbody>
{%- for drug in trial_drugs -%}
{%- assign indication = "" -%}
{%- for lab in ind_labels -%}{%- if indication == "" -%}{%- assign needle = "<td>" | append: lab | append: "</td>" -%}{%- assign qo = drug.content | split: needle -%}{%- if qo.size > 1 -%}{%- assign indication = qo[1] | split: "</td>" | first | split: "<td>" | last | strip -%}{%- endif -%}{%- endif -%}{%- endfor -%}
{%- assign level_cell = "" -%}
{%- for lab in lev_labels -%}{%- if level_cell == "" -%}{%- assign needle = "<td>" | append: lab | append: "</td>" -%}{%- assign lv = drug.content | split: needle -%}{%- if lv.size > 1 -%}{%- assign level_cell = lv[1] | split: "</td>" | first | split: "<td>" | last | strip -%}{%- endif -%}{%- endif -%}{%- endfor -%}
{%- assign parts = drug.content | split: "NCT" -%}
{%- capture nct_ids -%}{%- for p in parts offset: 1 -%}{%- assign id = p | slice: 0, 8 -%}{%- assign rest = id | remove: "0" | remove: "1" | remove: "2" | remove: "3" | remove: "4" | remove: "5" | remove: "6" | remove: "7" | remove: "8" | remove: "9" -%}{%- if id.size == 8 and rest == "" -%}{{ id }},{%- endif -%}{%- endfor -%}{%- endcapture -%}
{%- assign nct_count = nct_ids | split: "," | uniq | size %}
<tr><td><a href="{{ drug.url | relative_url }}">{{ drug.title }}</a></td><td>{% if indication != "" %}{{ indication }}{% else %}보고서 참조{% endif %}</td><td>{{ drug.evidence_level }}{% if level_cell != "" and level_cell != drug.evidence_level %} <a href="{{ drug.url | relative_url }}" title="{{ level_cell | strip_html | escape }}">(단서 있음)</a>{% endif %}</td><td>{{ nct_count }}</td></tr>
{%- endfor %}
</tbody>
</table></div>

## 목록 읽는 법

- **근거 수준**은 이 사이트의 [기준]({{ '/evidence-high/' | relative_url }})을 따릅니다: L1 = 다수의 3상 RCT / 체계적 문헌고찰; L2 = 단일 RCT 또는 다수의 2상 시험. "(단서 있음)"은 보고서가 해당 등급에 단서를 달았다는 뜻이므로, 판단 전에 보고서의 설명을 읽으십시오.
- **예측 신규 적응증**은 각 보고서의 주요 예측입니다. TxGNN 지식 그래프에 이미 기록된 적응증과 금기는 제외했지만, 일부 예측은 기존 용도와 겹칠 수 있으며 해당되는 경우 보고서에서 설명합니다.
- **인용된 등록 임상시험**은 보고서에 인용된 ClinicalTrials.gov(NCT) 번호의 수입니다. 보고서는 찾은 시험 중 일부만 인용하며, 0은 보고서가 등록 임상시험을 인용하지 않았다는 뜻으로 등급의 근거는 문헌 근거 섹션에 있습니다.
- 모든 근거 수준과 전체 방법은 [높은 근거 (L1-L2)]({{ '/evidence-high/' | relative_url }}), [전체 의약품]({{ '/drugs/' | relative_url }}), [방법론]({{ '/methodology/' | relative_url }})을 참조하십시오.

---

<div class="disclaimer">
<strong>면책 조항</strong><br>
본 보고서는 학술 연구 참고용으로만 제공되며 <strong>의료 조언을 구성하지 않습니다</strong>. 반드시 담당 의사의 지시를 따르시고, 임의로 약물을 조정하지 마십시오. 모든 약물재창출 결정은 완전한 임상 검증과 규제 당국의 심사를 거쳐야 합니다.
<br><br>
<small>검토: 藥提醒科技有限公司 (yao.care)</small>
</div>
