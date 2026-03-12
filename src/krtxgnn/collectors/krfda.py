"""韓國 MFDS (식품의약품안전처) 藥品資料收集器

從韓國 MFDS 의약품통합정보시스템 搜尋藥品相關資訊。
資料來源: https://nedrug.mfds.go.kr/
"""

import re
from typing import Optional
from urllib.parse import quote

import requests
from bs4 import BeautifulSoup

from .base import BaseCollector, CollectorResult


class KrFDACollector(BaseCollector):
    """韓國 MFDS 藥品資料收集器"""

    source_name = "krfda"
    base_url = "https://nedrug.mfds.go.kr"

    def __init__(self, timeout: int = 30):
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        })

    def search(self, drug: str, disease: Optional[str] = None) -> CollectorResult:
        """搜尋 MFDS 藥品資訊

        Args:
            drug: 藥品名稱（英文或韓文）
            disease: 疾病名稱（可選）

        Returns:
            CollectorResult 包含搜尋結果
        """
        evidences = []

        try:
            # 搜尋 MFDS 藥品資料庫
            search_results = self._search_mfds(drug)
            evidences.extend(search_results)

            # 如果有疾病參數，進行適應症匹配
            if disease:
                evidences = self._filter_by_indication(evidences, disease)

        except Exception as e:
            return CollectorResult(
                source=self.source_name,
                query=f"{drug} {disease}" if disease else drug,
                evidences=[],
                error=str(e)
            )

        return CollectorResult(
            source=self.source_name,
            query=f"{drug} {disease}" if disease else drug,
            evidences=evidences
        )

    def _search_mfds(self, drug: str) -> list[Evidence]:
        """搜尋 MFDS 藥品資料庫"""
        evidences = []

        # MFDS 搜尋 API 端點
        search_url = f"{self.base_url}/pbp/CCBBB01/getItemList"

        try:
            # 嘗試使用 MFDS 公開 API
            params = {
                "itemName": drug,
                "pageNo": 1,
                "numOfRows": 10
            }

            response = self.session.get(
                search_url,
                params=params,
                timeout=self.timeout
            )

            if response.status_code == 200:
                # 解析回應（可能是 JSON 或 XML）
                try:
                    data = response.json()
                    items = data.get("body", {}).get("items", [])
                    for item in items[:5]:
                        evidence = self._parse_mfds_item(item)
                        if evidence:
                            evidences.append(evidence)
                except:
                    # 嘗試解析為 HTML
                    evidences.extend(self._parse_html_results(response.text, drug))

        except requests.RequestException:
            # 如果 API 失敗，嘗試網頁搜尋
            evidences.extend(self._web_search(drug))

        return evidences

    def _parse_mfds_item(self, item: dict) -> Optional[Evidence]:
        """解析 MFDS API 回應項目"""
        try:
            item_name = item.get("ITEM_NAME", "")
            item_seq = item.get("ITEM_SEQ", "")
            entp_name = item.get("ENTP_NAME", "")
            efcy_qesitm = item.get("EFCY_QESITM", "")  # 效能效果

            if not item_name:
                return None

            url = f"{self.base_url}/pbp/CCBBB01/getItemDetail?itemSeq={item_seq}"

            return Evidence(
                source=self.source_name,
                title=f"{item_name} ({entp_name})",
                url=url,
                snippet=efcy_qesitm[:300] if efcy_qesitm else "MFDS 허가 의약품",
                date=item.get("ITEM_PERMIT_DATE", ""),
                metadata={
                    "item_seq": item_seq,
                    "manufacturer": entp_name,
                    "indication": efcy_qesitm,
                }
            )
        except Exception:
            return None

    def _parse_html_results(self, html: str, drug: str) -> list[Evidence]:
        """解析 HTML 搜尋結果"""
        evidences = []

        try:
            soup = BeautifulSoup(html, "lxml")

            # 尋找搜尋結果列表
            results = soup.select(".search-result-item, .drug-item, tr[data-item]")

            for result in results[:5]:
                try:
                    # 提取標題和連結
                    title_elem = result.select_one("a, .item-name, td:first-child")
                    if not title_elem:
                        continue

                    title = title_elem.get_text(strip=True)
                    href = title_elem.get("href", "")
                    url = href if href.startswith("http") else f"{self.base_url}{href}"

                    # 提取摘要
                    snippet_elem = result.select_one(".description, .efcy, td:nth-child(3)")
                    snippet = snippet_elem.get_text(strip=True)[:300] if snippet_elem else ""

                    evidences.append(Evidence(
                        source=self.source_name,
                        title=title,
                        url=url,
                        snippet=snippet or f"MFDS 의약품 정보: {title}",
                    ))
                except Exception:
                    continue

        except Exception:
            pass

        return evidences

    def _web_search(self, drug: str) -> list[Evidence]:
        """網頁搜尋備用方案"""
        evidences = []

        # 建立搜尋 URL
        encoded_drug = quote(drug)
        search_url = f"{self.base_url}/searchDrug?searchKeyword={encoded_drug}"

        # 返回一個指向搜尋頁面的證據
        evidences.append(Evidence(
            source=self.source_name,
            title=f"MFDS 의약품 검색: {drug}",
            url=search_url,
            snippet=f"한국 식품의약품안전처 의약품통합정보시스템에서 '{drug}' 검색",
        ))

        return evidences

    def _filter_by_indication(
        self,
        evidences: list[Evidence],
        disease: str
    ) -> list[Evidence]:
        """依據適應症過濾結果"""
        disease_lower = disease.lower()

        filtered = []
        for ev in evidences:
            # 檢查適應症是否包含疾病關鍵字
            indication = ev.metadata.get("indication", "") if ev.metadata else ""
            snippet = ev.snippet or ""

            if disease_lower in indication.lower() or disease_lower in snippet.lower():
                ev.relevance_score = 1.0
                filtered.append(ev)
            elif any(kw in indication.lower() or kw in snippet.lower()
                     for kw in disease_lower.split()):
                ev.relevance_score = 0.7
                filtered.append(ev)

        # 如果沒有匹配，返回原始結果
        return filtered if filtered else evidences


# CRIS (韓國臨床試驗註冊) 收集器
class CRISCollector(BaseCollector):
    """韓國臨床試驗資訊服務 (CRIS) 收集器

    Clinical Research Information Service
    https://cris.nih.go.kr/
    """

    source_name = "cris"
    base_url = "https://cris.nih.go.kr"

    def __init__(self, timeout: int = 30):
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        })

    def search(self, drug: str, disease: Optional[str] = None) -> CollectorResult:
        """搜尋 CRIS 臨床試驗

        Args:
            drug: 藥品名稱
            disease: 疾病名稱（可選）

        Returns:
            CollectorResult 包含搜尋結果
        """
        evidences = []
        query = f"{drug} {disease}" if disease else drug

        try:
            # 建立搜尋 URL
            encoded_query = quote(query)
            search_url = f"{self.base_url}/cris/search/search.do?searchTerm={encoded_query}"

            # 添加指向搜尋頁面的證據
            evidences.append(Evidence(
                source=self.source_name,
                title=f"CRIS 임상시험 검색: {query}",
                url=search_url,
                snippet=f"한국 임상시험정보서비스에서 '{query}' 관련 임상시험 검색",
            ))

            # 嘗試獲取實際搜尋結果
            response = self.session.get(search_url, timeout=self.timeout)
            if response.status_code == 200:
                additional = self._parse_cris_results(response.text, query)
                evidences.extend(additional)

        except Exception as e:
            return CollectorResult(
                source=self.source_name,
                query=query,
                evidences=[],
                error=str(e)
            )

        return CollectorResult(
            source=self.source_name,
            query=query,
            evidences=evidences
        )

    def _parse_cris_results(self, html: str, query: str) -> list[Evidence]:
        """解析 CRIS 搜尋結果"""
        evidences = []

        try:
            soup = BeautifulSoup(html, "lxml")
            results = soup.select(".search-result, .trial-item, tr.data-row")

            for result in results[:5]:
                try:
                    title_elem = result.select_one("a, .trial-title")
                    if not title_elem:
                        continue

                    title = title_elem.get_text(strip=True)
                    href = title_elem.get("href", "")
                    url = href if href.startswith("http") else f"{self.base_url}{href}"

                    # 提取試驗狀態和階段
                    status_elem = result.select_one(".status, .trial-status")
                    status = status_elem.get_text(strip=True) if status_elem else ""

                    phase_elem = result.select_one(".phase, .trial-phase")
                    phase = phase_elem.get_text(strip=True) if phase_elem else ""

                    snippet = f"{status} {phase}".strip() or f"CRIS 임상시험: {title}"

                    evidences.append(Evidence(
                        source=self.source_name,
                        title=title,
                        url=url,
                        snippet=snippet,
                        metadata={
                            "status": status,
                            "phase": phase,
                        }
                    ))
                except Exception:
                    continue

        except Exception:
            pass

        return evidences
