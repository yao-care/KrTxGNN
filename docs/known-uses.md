---
layout: default
title: "기존 용도만 (신규 예측 없음)"
nav_order: 24
permalink: /known-uses/
description: "이 약물들은 TxGNN 모델의 후보가 모두 이미 알려진 용도(지식 그래프 또는 허가 정보에 기록됨)이므로 새로운 예측 적응증이 없습니다. 각 페이지에 기존 용도와 국내 시판 현황을 정리했습니다."
---

# 기존 용도만 (신규 예측 없음)

이 약물들은 TxGNN 모델의 후보가 모두 이미 알려진 용도(지식 그래프 또는 허가 정보에 기록됨)이므로 새로운 예측 적응증이 없습니다. 각 페이지에 기존 용도와 국내 시판 현황을 정리했습니다.

{% assign known_drugs = site.drugs | where: "evidence_level", "N/A" | sort: "title" %}

**{{ known_drugs.size }} 개 약물**

| 약물 | 보고서 |
|------|------|
{% for drug in known_drugs %}| **{{ drug.title }}** | [보기]({{ drug.url | relative_url }}) |
{% endfor %}
