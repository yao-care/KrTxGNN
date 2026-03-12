#!/usr/bin/env python3
"""
Korea Health News Fetcher

한국 건강 뉴스 수집:
- Google News Korea 건강 카테고리
- Naver News 건강 카테고리

출력: data/news/korea_news.json
"""

import hashlib
import json
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

import feedparser

# 프로젝트 루트 디렉토리
PROJECT_ROOT = Path(__file__).parent.parent.parent
DATA_DIR = PROJECT_ROOT / "data" / "news"

# Google News Korea 건강 카테고리 RSS
GOOGLE_NEWS_HEALTH_RSS = (
    "https://news.google.com/rss/topics/"
    "CAAqJQgKIh9DQkFTRVFvSUwyMHZNR3QwTlRFU0JXdHZMVXRTS0FBUAE"
    "?hl=ko&gl=KR&ceid=KR:ko"
)

# Google News Korea 과학/기술 카테고리 RSS
GOOGLE_NEWS_SCIENCE_RSS = (
    "https://news.google.com/rss/topics/"
    "CAAqKggKIiRDQkFTRlFvSUwyMHZNRFp0Y1RjU0JXdHZMVXRTR2dKTFVpZ0FQAQ"
    "?hl=ko&gl=KR&ceid=KR:ko"
)

# 요청 간격
REQUEST_DELAY = 1.0  # 초


def generate_id(title: str, link: str) -> str:
    """뉴스 ID 생성 (제목과 링크의 해시 기반)"""
    content = f"{title}:{link}"
    return hashlib.md5(content.encode()).hexdigest()[:12]


def parse_source(entry, default_source: str = "Unknown") -> dict:
    """RSS 엔트리에서 출처 정보 추출"""
    source_name = default_source
    if hasattr(entry, "source") and hasattr(entry.source, "title"):
        source_name = entry.source.title

    return {
        "name": source_name,
        "link": entry.get("link", "")
    }


def parse_published(entry) -> str:
    """발행 시간 파싱 및 ISO 8601 형식 변환"""
    published = entry.get("published_parsed")
    if published:
        try:
            dt = datetime(*published[:6], tzinfo=timezone.utc)
            return dt.isoformat()
        except Exception:
            pass

    # 파싱 실패 시 현재 시각 사용
    return datetime.now(timezone.utc).isoformat()


def clean_summary(summary: str) -> str:
    """요약 텍스트 정리 (HTML 태그 제거 등)"""
    # HTML 태그 제거
    clean = re.sub(r"<[^>]+>", "", summary)
    # 불필요한 공백 제거
    clean = re.sub(r"\s+", " ", clean).strip()
    return clean[:500] if len(clean) > 500 else clean


def fetch_rss(url: str, source_name: str) -> list[dict]:
    """RSS URL에서 뉴스 가져오기"""
    print(f"  수집 중: {source_name}")
    print(f"    URL: {url[:70]}...")

    try:
        # 사용자 정의 헤더로 가져오기
        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; KrTxGNN/1.0; +https://krtxgnn.yao.care)",
            "Accept": "application/rss+xml, application/xml, text/xml",
            "Accept-Language": "ko,en;q=0.9",
        }
        request = Request(url, headers=headers)
        with urlopen(request, timeout=30) as response:
            content = response.read()
    except (HTTPError, URLError) as e:
        print(f"    오류: {e}")
        return []

    feed = feedparser.parse(content)

    if feed.bozo:
        print(f"    경고: RSS 파싱 문제 발생 - {feed.bozo_exception}")

    news_items = []

    for entry in feed.entries:
        title = entry.get("title", "")
        link = entry.get("link", "")

        if not title or not link:
            continue

        news_id = generate_id(title, link)
        source = parse_source(entry, source_name)
        published = parse_published(entry)
        summary = clean_summary(entry.get("summary", "") or entry.get("description", ""))

        news_items.append({
            "id": news_id,
            "title": title,
            "published": published,
            "summary": summary,
            "sources": [source]
        })

    print(f"    수집: {len(news_items)} 건의 뉴스")
    return news_items


def fetch_google_news_korea_health() -> list[dict]:
    """Google News Korea 건강 카테고리 수집"""
    return fetch_rss(GOOGLE_NEWS_HEALTH_RSS, "Google News Korea Health")


def fetch_google_news_korea_science() -> list[dict]:
    """Google News Korea 과학 카테고리 수집"""
    return fetch_rss(GOOGLE_NEWS_SCIENCE_RSS, "Google News Korea Science")


def deduplicate_news(news_items: list[dict]) -> list[dict]:
    """중복 뉴스 제거 (ID 기반)"""
    seen_ids = set()
    unique_items = []

    for item in news_items:
        if item["id"] not in seen_ids:
            seen_ids.add(item["id"])
            unique_items.append(item)

    return unique_items


def filter_health_keywords(news_items: list[dict]) -> list[dict]:
    """건강 관련 키워드로 필터링"""
    health_keywords = [
        # 의료 / 건강 일반
        "의료", "의약", "약", "치료", "진단", "수술", "병원", "클리닉",
        "건강", "질병", "질환", "증상", "감염", "바이러스", "세균",
        # 질환명
        "암", "당뇨병", "고혈압", "심장", "뇌졸중", "치매",
        "우울증", "불면증", "천식", "알레르기", "간염", "신장",
        # 약 / 치료법
        "신약", "임상시험", "승인", "FDA", "식약처", "MFDS",
        "백신", "항체", "면역", "유전자", "줄기세포", "재생의료",
        # 연구
        "연구", "발견", "개발", "효과", "부작용", "위험",
        # 영어 키워드 (국제 뉴스용)
        "drug", "medicine", "treatment", "therapy", "clinical trial",
        "cancer", "diabetes", "cardiovascular", "vaccine",
    ]

    filtered = []
    for item in news_items:
        text = f"{item['title']} {item.get('summary', '')}"
        if any(keyword in text for keyword in health_keywords):
            filtered.append(item)

    return filtered


def main():
    print("한국 건강 뉴스 수집 중...")

    # 디렉토리 확보
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    all_news = []

    # Google News Korea Health
    news = fetch_google_news_korea_health()
    all_news.extend(news)
    time.sleep(REQUEST_DELAY)

    # Google News Korea Science
    news = fetch_google_news_korea_science()
    all_news.extend(news)

    # 중복 제거
    unique_news = deduplicate_news(all_news)
    print(f"\n중복 제거 후: {len(unique_news)} 건")

    # 건강 관련 필터링
    health_news = filter_health_keywords(unique_news)
    print(f"건강 관련 필터링 후: {len(health_news)} 건")

    # 발행일 정렬 (최신순)
    health_news.sort(key=lambda x: x["published"], reverse=True)

    # 출력
    output = {
        "source": "korea_news",
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "total_fetched": len(all_news),
        "unique_count": len(unique_news),
        "health_related_count": len(health_news),
        "news": health_news
    }

    output_path = DATA_DIR / "korea_news.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"\n출력: {output_path}")
    print(f"  - 총 수집: {len(all_news)}")
    print(f"  - 유니크: {len(unique_news)}")
    print(f"  - 건강 관련: {len(health_news)}")


if __name__ == "__main__":
    main()
