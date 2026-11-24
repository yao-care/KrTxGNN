# TxGNN 國際化 SOP - 從初始化包建立地區藥品老藥新用預測系統

## 目標

將此初始化包轉換為您國家的藥品老藥新用預測系統。

**使用方式**：
1. 解壓縮 TxGNN_init.zip
2. 閱讀本文件，按照階段化流程執行
3. 將 `.template` 檔案改名並填入當地資訊
4. 執行預測流程

---

## 一、元件分類總覽

### 1.1 通用元件（直接使用，約 60-70%）

| 類別 | 檔案 | 說明 |
|------|------|------|
| **TxGNN 知識圖譜** | `data/node.csv`, `data/kg.csv` | 知識圖譜基礎資料（需下載） |
| **詞彙表提取** | `scripts/prepare_external_data.py` | 從 TxGNN 提取 DrugBank/疾病詞彙 |
| **藥名正規化** | `src/txgnn/mapping/normalizer.py` | 通用藥名標準化 |
| **DrugBank 映射** | `src/txgnn/mapping/drugbank_mapper.py` | 成分 → DrugBank ID |
| **KG 預測** | `src/txgnn/predict/repurposing.py` | 知識圖譜方法 |
| **DL 預測** | `src/txgnn/predict/txgnn_model.py` | 深度學習方法 |
| **通用收集器** | `collectors/clinicaltrials.py`, `pubmed.py`, `drugbank.py`, `ictrp.py` | 全球資料來源 |
| **收集器基類** | `src/txgnn/collectors/base.py` | 收集器介面 |

### 1.2 需在地化元件（約 30-40%）

| 類別 | 模板檔案 | 需修改內容 |
|------|----------|------------|
| **專案設定** | `pyproject.toml.template` | 專案名稱 |
| **欄位映射** | `config/fields.yaml.template` | 藥監局資料欄位對應 |
| **資料載入** | `src/txgnn/data/loader.py.template` | 載入邏輯 |
| **疾病映射** | `src/txgnn/mapping/disease_mapper.py.template` | DISEASE_DICT（當地語言→英文） |
| **資料處理** | `scripts/process_fda_data.py.template` | ZIP/JSON 解析 |
| **預測腳本** | `scripts/run_kg_prediction.py.template` | 微調欄位名稱 |
| **FHIR 生成** | `scripts/generate_fhir_resources.py.template` | URL 和管轄區域 |
| **新聞同義詞** | `data/news/synonyms.json.template` | 疾病/藥物同義詞 |
| **網站設定** | `docs/_config.yml.template` | 標題、URL |
| **SMART App** | `docs/smart/launch.html.template` | Client ID |
| **CI/CD** | `.github/workflows/pages.yml.template` | 部署設定 |

---

## 二、階段化實施流程

### Phase 0：專案初始化

**目標**：設定專案基礎

#### 步驟：

1. **重新命名專案**
   ```bash
   # 建議命名：{Country}TxGNN
   # 例：JpTxGNN, KrTxGNN, ThTxGNN
   mv TxGNN_init {Country}TxGNN
   cd {Country}TxGNN
   ```

2. **設定 pyproject.toml**
   ```bash
   mv pyproject.toml.template pyproject.toml
   # 編輯 pyproject.toml，修改 name 和 description
   ```

3. **下載 TxGNN 資料**
   ```bash
   mkdir -p data
   curl -L -o data/node.csv "https://dataverse.harvard.edu/api/access/datafile/7144482"
   curl -L -o data/kg.csv "https://dataverse.harvard.edu/api/access/datafile/7144484"
   ```

4. **安裝依賴**
   ```bash
   uv sync
   ```

**品質檢查點**：
- [ ] 專案已重新命名
- [ ] `pyproject.toml` 已修改
- [ ] `uv sync` 執行成功
- [ ] TxGNN 資料下載完成（node.csv ~15MB, kg.csv ~500MB）

---

### Phase 1：FDA 資料整合

**目標**：整合當地藥監局資料

#### 1.1 調查資料來源

常見藥監局資料來源：

| 國家 | 藥監局 | 資料來源 |
|------|--------|----------|
| 日本 | PMDA | https://www.pmda.go.jp/ |
| 韓國 | MFDS | https://nedrug.mfds.go.kr/ |
| 泰國 | Thai FDA | https://www.fda.moph.go.th/ |

**產出**：記錄資料來源 URL、格式、欄位說明

#### 1.2 建立欄位映射設定

```bash
mv config/fields.yaml.template config/fields.yaml
# 編輯 fields.yaml，填入欄位對應
```

**fields.yaml 範例（日本 PMDA）**：
```yaml
country_code: JP
language: ja
regulatory_agency: PMDA

field_mapping:
  license_id: "承認番号"
  brand_name_local: "販売名"
  brand_name_en: "一般名"
  ingredients: "有効成分"
  indication: "効能・効果"
  dosage_form: "剤形"
  status: "承認状況"

withdrawn_statuses:
  - "取消"
  - "回収"
```

#### 1.3 實作資料載入器

```bash
mv src/txgnn/data/loader.py.template src/txgnn/data/loader.py
# 編輯 loader.py，實作載入邏輯
```

#### 1.4 實作資料處理腳本

```bash
mv scripts/process_fda_data.py.template scripts/process_fda_data.py
# 編輯並執行
uv run python scripts/process_fda_data.py
```

**品質檢查點**：
- [ ] `config/fields.yaml` 建立完成
- [ ] `loader.py` 能正確載入資料
- [ ] `process_fda_data.py` 執行成功
- [ ] `data/raw/{country}_fda_drugs.json` 產生

---

### Phase 2：疾病映射

**目標**：建立當地語言 → 英文疾病對照

#### 2.1 建立 DISEASE_DICT

```bash
mv src/txgnn/mapping/disease_mapper.py.template src/txgnn/mapping/disease_mapper.py
# 編輯 disease_mapper.py，填入 DISEASE_DICT
```

**目標數量**：150-200 個疾病詞條

**分類建議**：

| 分類 | 建議數量 |
|------|----------|
| 心血管系統 | 15-20 |
| 呼吸系統 | 10-15 |
| 消化系統 | 15-20 |
| 神經系統 | 10-15 |
| 精神疾病 | 8-12 |
| 內分泌系統 | 10-15 |
| 肌肉骨骼 | 10-15 |
| 皮膚疾病 | 10-15 |
| 泌尿系統 | 8-12 |
| 眼科 | 5-8 |
| 耳鼻喉 | 5-8 |
| 感染症 | 10-15 |
| 過敏 | 5-8 |
| 婦科 | 8-12 |
| 腫瘤/癌症 | 10-15 |
| 一般症狀 | 15-20 |

#### 2.2 建立新聞同義詞

```bash
mv data/news/synonyms.json.template data/news/synonyms.json
# 編輯 synonyms.json，填入當地語言同義詞
```

**品質檢查點**：
- [ ] DISEASE_DICT 有 150+ 詞條
- [ ] 涵蓋所有主要疾病分類
- [ ] `synonyms.json` 建立完成

---

### Phase 3：KG 預測流程

**目標**：執行知識圖譜預測

#### 執行步驟：

```bash
# 1. 準備詞彙表
uv run python scripts/prepare_external_data.py

# 2. 設定預測腳本
mv scripts/run_kg_prediction.py.template scripts/run_kg_prediction.py
# 編輯並執行

# 3. 執行預測
uv run python scripts/run_kg_prediction.py
```

#### 預期產出：

| 檔案 | 預期內容 |
|------|----------|
| `data/external/drugbank_vocab.csv` | ~7,958 個藥物 |
| `data/external/disease_vocab.csv` | ~17,081 個疾病 |
| `data/external/drug_disease_relations.csv` | ~80,127 個關係 |
| `data/processed/repurposing_candidates.csv` | 視藥品數量而定 |

**品質檢查點**：
- [ ] 詞彙表正確產生
- [ ] `repurposing_candidates.csv` 產生
- [ ] DrugBank 映射率 > 30%
- [ ] 疾病映射率 > 20%

---

### Phase 4：網站與 FHIR

**目標**：部署文件網站與 FHIR API

#### 4.1 Jekyll 設定

```bash
mv docs/_config.yml.template docs/_config.yml
# 編輯 _config.yml，修改標題、URL、語言
```

#### 4.2 FHIR 資源設定

```bash
mv scripts/generate_fhir_resources.py.template scripts/generate_fhir_resources.py
# 編輯 BASE_URL 和 JURISDICTION
uv run python scripts/generate_fhir_resources.py
```

#### 4.3 SMART App 設定

```bash
mv docs/smart/launch.html.template docs/smart/launch.html
# 編輯 CLIENT_ID
```

#### 4.4 本地測試

```bash
cd docs
bundle install
bundle exec jekyll serve
# 訪問 http://localhost:4000
```

**品質檢查點**：
- [ ] Jekyll 本地建置成功
- [ ] `/fhir/metadata` 可存取
- [ ] FHIR 資源正確產生

---

### Phase 5：證據收集

**目標**：設定證據收集器

#### 5.1 建立當地 FDA 收集器

建立 `src/txgnn/collectors/{country}fda.py`：

```python
from .base import BaseCollector, CollectorResult

class {Country}FDACollector(BaseCollector):
    source_name = "{country}fda"

    def search(self, drug: str, disease: str | None = None) -> CollectorResult:
        # 實作搜尋邏輯
        pass
```

#### 5.2 區域臨床試驗註冊

ICTRP 涵蓋的區域註冊：
- 日本：JPRN (UMIN-CTR, JapicCTI)
- 韓國：CRIS
- 泰國：TCTR

**品質檢查點**：
- [ ] 當地 FDA 收集器建立
- [ ] ClinicalTrials.gov 收集器正常
- [ ] PubMed 收集器正常

---

### Phase 6：新聞監測

**目標**：設定健康新聞監測

#### 6.1 設定關鍵字模式

建立 `scripts/generate_news_keywords.py`，參考 TwTxGNN 版本。

#### 6.2 新增當地新聞來源

建立 `scripts/fetchers/{country}_news.py`

**品質檢查點**：
- [ ] `keywords.json` 產生
- [ ] 新聞爬蟲正常運作

---

### Phase 7：驗證與部署

**目標**：端對端驗證並部署

#### 7.1 設定 GitHub Actions

```bash
mv .github/workflows/pages.yml.template .github/workflows/pages.yml
# 編輯部署設定
```

#### 7.2 完整流程測試

```bash
uv run python scripts/process_fda_data.py
uv run python scripts/prepare_external_data.py
uv run python scripts/run_kg_prediction.py
uv run python scripts/generate_fhir_resources.py
```

#### 7.3 品質指標

| 指標 | 台灣參考值 | 目標 |
|------|-----------|------|
| FDA 藥品總數 | 71,552 | 記錄 |
| 有效藥品比例 | 33% | > 20% |
| DrugBank 映射率 | 73.87% | > 50% |
| 疾病映射率 | 44.85% | > 30% |
| 預測候選數 | 142,328 | 記錄 |

**品質檢查點**：
- [ ] 端對端流程通過
- [ ] GitHub Pages 部署成功
- [ ] SMART App 可從 SMART Launcher 啟動

---

## 三、關鍵檔案詳解

### 3.1 `config/fields.yaml`

欄位映射設定檔，定義藥監局資料欄位與標準欄位的對應關係。

### 3.2 `src/txgnn/data/loader.py`

資料載入器，根據 `fields.yaml` 載入並過濾藥品資料。

### 3.3 `src/txgnn/mapping/disease_mapper.py`

疾病映射模組，包含 `DISEASE_DICT`（當地語言→英文對照表）。

### 3.4 `scripts/process_fda_data.py`

資料處理腳本，將原始資料轉換為標準 JSON 格式。

---

## 四、GitHub Actions 設定

### 需設定的 Workflow：

| Workflow | 功能 | 需修改 |
|----------|------|--------|
| `pages.yml` | Jekyll 部署 | URL |
| `link-check.yml` | 連結檢查 | 無 |
| `check-new-evidence.yml` | 證據檢查 | 無 |

### 需設定的 Secrets：

| Secret | 用途 |
|--------|------|
| `GITHUB_TOKEN` | 自動提供 |
| `NCBI_API_KEY` | PubMed API（可選，提高速率限制） |

---

## 五、驗證清單

### 總體完成檢查

- [ ] Phase 0：專案初始化完成
- [ ] Phase 1：FDA 資料整合完成
- [ ] Phase 2：疾病映射完成
- [ ] Phase 3：KG 預測完成
- [ ] Phase 4：網站與 FHIR 完成
- [ ] Phase 5：證據收集完成
- [ ] Phase 6：新聞監測完成
- [ ] Phase 7：驗證與部署完成

### YMYL 檢查（醫療內容必檢）

- [ ] 免責聲明：「僅供研究參考，不構成醫療建議」
- [ ] 預測結果標註：「需經臨床驗證」
- [ ] 資料來源標註完整

---

## 六、附錄：區域特殊考量

### 日本 (PMDA)
- 資料格式：可能有 Shift-JIS 編碼
- 藥名：漢字/平假名/片假名混用
- 臨床試驗：JPRN (UMIN-CTR, JapicCTI, JMACCT)

### 韓國 (MFDS)
- 資料格式：UTF-8
- 藥名：韓文 + 英文音譯
- 臨床試驗：CRIS

### 泰國 (Thai FDA)
- 資料格式：UTF-8
- 藥名：泰文 + 英文
- 臨床試驗：TCTR

### 常見挑戰

1. **成分名稱變異**：同一藥物可能有不同鹽類形式
2. **品牌名映射**：當地品牌名需對應到國際名稱
3. **適應症文字解析**：不同語言的標點符號慣例不同
4. **日期格式**：各地區日期格式不同
5. **狀態碼**：有效/註銷的術語不同

---

## 常用命令

```bash
# 安裝依賴
uv sync

# 處理 FDA 資料
uv run python scripts/process_fda_data.py

# 準備詞彙表資料
uv run python scripts/prepare_external_data.py

# 執行知識圖譜預測
uv run python scripts/run_kg_prediction.py

# 生成 FHIR 資源
uv run python scripts/generate_fhir_resources.py

# 本地測試網站
cd docs && bundle exec jekyll serve

# 執行測試
uv run pytest tests/ -v
```

---

## 注意事項

- 本專案結果僅供研究參考，不構成醫療建議
- 老藥新用候選需經過臨床驗證才能應用
- 所有網站頁面需包含 YMYL 免責聲明

---

## 藥物頁查核機制（2026-11-12 起）

用戶 2026-11-12 決定：30 站各有自己的查核機制，核心流程比照 TwTxGNN（Tw 的 CLAUDE.md「藥物頁人工查核紀錄」「藥物頁許可證表與張數」兩節；
做法同 UsTxGNN，見 UsTxGNN/CLAUDE.md 同名一節）。規則與程式都在本 repo；頁面文字用韓文，依據是식품의약품안전처 의약품안전나라（nedrug）허가 자료。本站的在地設定集中在 `src/krtxgnn/regulatory/site.py`。

| 環節 | 本站檔案 | 說明 |
|------|----------|------|
| 查核紀錄 | `docs/_data/drug_reviews.json` | 單一真實來源，欄位同 Tw（correct／annotate／rereview／rereview_result／header_level／description_level、history、status） |
| 套用 | `scripts/apply_drug_reviews.py` | 套到 `docs/_drugs/*.md`：查核框 `<!-- review:begin id -->`、每頁查核紀錄表；可重複執行；`--check` 只檢查、`--touch` 連 last_modified_at 一起改 |
| 頁首等級 | `src/krtxgnn/regulatory/page_format.py`（規則在 site.py 的 HEADER_RULE） | 頁首＝빠른 개요「근거 수준」格的**第一個**等級（主預測）。2026-11-12 實測 685 頁有總覽等級，全部符合；整格取最高會有 8 頁不同 |
| 撤回預測 | `src/krtxgnn/regulatory/withdrawn.py` | verdict=withdraw 的預測不進證據監測（`scripts/extract_drug_list.py`）、搜尋索引與 FHIR（母目錄 `.claude/rebuild_search_index.py`、`.claude/sync_fhir_levels.py` 會讀本站這支） |
| 許可證 | `snapshots/kr_licenses.json.gz`、`scripts/build_license_snapshot.py`、`src/krtxgnn/regulatory/licenses.py` | 快照存本藥號碼與事實層；gate 依快照驗市場段落表格的號碼歸屬、狀態列與張數列、表格列狀態（本站沒有程式產生的許可證表，所以沒有程式區塊標記） |
| 刪改轉紀錄 | `scripts/reviews_from_edits.py` | 依成分重建刪句後（`scripts/license_rebuild_run.py` 有的話會自動跑）或依 git 前後版本，把正文刪改轉成 correct 紀錄 |
| 待查清單 | `docs/_data/drug_reviews_uncertain.json`、`scripts/check_original_indications.py` | 原適應症交叉驗證；證據包沒有適應症文字的頁不比對，程式照實回報 |
| gate | `scripts/check_seo_docs.py` 第 17–20 項 | 紀錄都已套用、許可證＝快照、頁首＝本站規則算出的等級、撤回預測沒有對外發布 |

原則（同 Tw）：基本事實照主管機關資料更正；模型預測原文不刪不改寫，只加註；證據等級與決策只經重審（rereview → rereview_result）變更。

改頁之後要跑：

```bash
python3 scripts/apply_drug_reviews.py          # 重套查核紀錄（sync_notes_to_docs.py、license_rebuild_run.py、每週排程結尾都會自動跑）
python3 scripts/build_license_snapshot.py --ws <工作目錄>   # 證據包或事實層變了才要（排程與重建會自動跑）
python3 scripts/check_seo_docs.py              # 必須 exit 0
```

2026-10-31～11-06 依成分重建後直接刪掉的矛盾子句，2026-11-12 已用 `scripts/reviews_from_edits.py --git` 轉成 94 筆紀錄（73 頁；其中 2 筆因報告在 11 月經 AI 重產、原句已不在頁面，標 resolved_by_regeneration）。
`scripts/sync_notes_to_docs.py` 依 notes 重寫整頁時，會重套紀錄（有程式許可證表的站也保留舊頁的程式區塊），notes 裡的舊錯句會被紀錄再更正一次。

正文許可證張數由程式改寫（2026-11-12 用戶決定；比照 Tw 的 `page_postprocess.rewrite_count_prose`）：`scripts/rewrite_license_counts.py` 依 `snapshots/kr_licenses.json.gz` 的事實層改寫正文的韓文「허가 N건」張數，
規則在 `src/krtxgnn/regulatory/count_prose.py`（只改句型明確的；有保留、講證據包或查詢、相對數、劑型或廠商子集、顯示筆數、partial 頁不動；同一行有句子判斷不了就整行不動；數字已等於總數或有效數任一讀法就不動）。
程式改寫的張數不逐筆寫查核紀錄、頁面不加說明框（同 Tw）；查核紀錄 replacement／anchor 所在的句子不改。`apply_drug_reviews.py`（非 --check）結尾與 `build_license_snapshot.py` 寫完快照後都會跑，
所以每週排程、license_rebuild_run、sync_notes_to_docs 之後張數會跟著事實層更新；gate 第 21 項擋「再跑一次會變」。
判斷不了的句子（說「全部有效／全部單方」而事實不符、沒有限定詞而有效數≠總數、建立在 0 張前提上）不改，`--list` 列出，2026-11-12 已用 `--uncertain` 加進待查清單（source：正文許可證張數程式改寫判斷不了的句子），要改請寫查核紀錄。
2026-11-12 待查清單裡程式判斷不了的 4 句已逐句對照事實層與證據包：codeine（「전체 7건」實為單方 7 張、全部 11 張）、glatiramer_acetate（「現在 0 張」→有效 1 張）、ramipril（單方 4→7 張、另有 felodipine 複方 2 張）以 `kr-lic-20261112-*` 改寫；adenosine 的「4건」是 adenosine 單方 4 張，不用改，標 resolved。事實層的 single_total 把複方也算進去（codeine、ramipril），單方／複方字樣照證據包成分判斷。

## 기존 적응증（原適應症）的 MFDS 原文（2026-11-15）

MFDS 의약품안전나라 허가 자료的效能·效果（EE_DOC）欄位是 PDF 下載網址，產線照抄，頁面「기존 적응증」只有網址或 AI 寫的「確認不到原文」，搜尋索引 original 也是網址。
- `scripts/build_mfds_indications.py`：證據包本藥單方許可證的 EE PDF 轉出的文字（母目錄 `.claude/kr_mfds_ee_20261023.py` 的快取，nedrug 擋雲端主機，要在本機下載）→ `docs/_data/mfds_original_indications.json`（每筆附許可證號與 PDF 網址；不改寫原文，只合併 PDF 折行）。2026-11-15 由 Release data-20261112-162414 的證據包產生，620 個藥有原文。
- `scripts/link_mfds_pdfs.py`（apply_drug_reviews.py 結尾自動跑，gate 第 22 項）：有原文資料、而該列只有連結或寫「確認不到原文」的，改成原文摘要（160 字內）＋PDF 連結，description 同步；本來就有原文的列不動。2026-11-15 改了 523 頁（519 列＋description）。
- search-index original：569 個原本空白的藥填入原文（300 字內）；母目錄 rebuild_search_index.py 會沿用既有 original。仍有 42 個藥取不到原文（32 個 PDF 不在快取、其餘證據包沒有網址），維持空白、SMART 顯示「—」。

## 新資料查不到的許可證（2026-11-17）

11-16 每週排程「新資料查不到」3 張（200607418 Preparation H Maximum Strength Cream、200800968 나라돌주500、201310113 보령필로카르핀정），證據包原本就記為註銷。
nedrug 雲端連不到（connection reset），改用 Release data-20261116-160402 裡 11-16 排程的下載檔（95,254 筆）與 2026-03 的 ItemPermitDetail.xlsx（44,072 筆、有취소일자）對照：
nedrug 엑셀다운로드 收全部정상品目，취소/취하品目只收취소일자在最近約 3 年內的（ItemPermitDetail 裡 2023-06～10 註銷的 1,102 筆 0 筆在下載檔、2023-11 的 124 筆 90 筆在、2023-12 以後全部在）。
3 張的취소일자是 2023-11-08（취하）、2023-11-03（취하）、2023-11-13（유효기간만료），是滑出下載窗口，不是新的狀態變化；沒有「其實還有效」的號，也沒有判斷不了的號。
- `scripts/license_adapter.py`：fetch() 把下載檔的品目記成 CURRENT（少於 50,000 筆不判定），並收證據包裡原本就是註銷的品目；`confirmed_absent()` 只對「不在下載檔、證據包原本就註銷」的品目回真，
  排程把它們列成「主管機關現行清單確認已不列」、不算查不到；preprocess 只加 `mfds_not_listed`（第一次發現日），狀態不動，又出現就取消。原本有效、卻不在下載檔的品目不推定。
- 頁面不用改（3 張原本就以註銷呈現）；正文張數（count_prose）不受影響。
- 同日另修：21 個公開頁（benzonatate、doxofylline、molsidomine、talc 等）front matter 補 drugbank_id（取自證據包），FHIR MedicationKnowledge／ClinicalUseDefinition 從 ec848139 前一版找回（預測跟頁面 predicted_indications 相同），再由 sync_fhir_levels 對齊（MK 673→694、CUD 3,898→4,015）。
  alpha-tocopherol_acetate 跟 alpha-tocopherol 是同一個 DrugBank ID（DB14003）的兩個公開頁，FHIR 只能對到一頁；2026-11-17 用戶決定 alpha-tocopherol_acetate 改成轉址到 alpha-tocopherol（照 11-16 重複頁轉址的格式，layout: id_redirect；該頁沒有查核紀錄），公開藥物頁 698→697，drug_stats、drugs.json、search-index、llms、README、首頁數字照重產，hreflang.json 拿掉該頁一組（他站的 hreflang 表仍列本站這個網址，要等各站重產）。

## 同一 DrugBank ID 的重複公開頁改轉址（2026-11-19）

用戶 2026-11-19 決定（照 ARTxGNN 同日做法）：公開藥物頁同一 DrugBank ID、預測相同的，留一頁、另一頁改轉址（layout: id_redirect、permalink 不變、sitemap: false、search_exclude、nav_exclude）。
2 組（鹽類寫法，預測、等級、許可證號完全相同，都沒有查核紀錄）：amlodipine_maleate→amlodipine_besylate（字數平手，留常用鹽類）、atorvastatin_calcium→atorvastatin_calcium_trihydrate（字數較多）。
公開藥物頁 697→695；被轉址頁自己的 MK 由 sync_fhir_levels 當重複刪（MK 694→692、CUD 4015→4002）；衍生檔、hreflang 照重產。

## 作用機轉段的資料來源與查核機制（2026-11-19）

用戶 2026-11-19 決定把 NZTxGNN 同日的作法推到各站（seo-ops 轉交：搜「<藥名> mechanism of action」落在藥物頁排名 30–99，因為頁面寫「作用機轉資料不可得」）。
2026-11-19 量測：本站公開藥物頁（排除 noindex、轉址頁）有 531 頁在正文章節寫這種句子（證據包 drugbank.source＝vocab_only、沒有作用機轉文字，AI 照實寫「沒有資料」；本站最常見的寫法：「현재 상세한 작용 기전 데이터가 없습니다.」）。
作用機轉是藥物本身的基本藥理事實、不是模型預測，所以照查核機制補：每段都節錄官方仿單或資料庫原文、附可點的出處與取用日期，不自己寫。

- 來源（理由同 NZTxGNN/CLAUDE.md 同名一節）：美國 FDA 核准仿單（openFDA drug label，連結到 NLM DailyMed 同一份 SPL setid；FDA 仿單是美國政府公開資料），美國沒有仿單時用 ChEMBL drug mechanism 表（CC BY-SA 3.0）；證據包的 DrugBank 欄位只有 vocab，DrugBank 文字授權也不允許轉載，不用。
  2026-11-19 這次用 openFDA 的 drug label 全量下載檔（download.open.fda.gov，同一批資料，只留 human prescription 仿單；`--fda-bulk <目錄>`），不吃 API 每日 1,000 次配額；之後少量重跑可直接用 API（不給 `--fda-bulk`）。快取目錄各站共用。
- `scripts/build_mechanism_reviews.py --cache <目錄> [--fda-bulk <目錄>]`：掃公開頁正文章節（排除結論／下一步的待辦、安全性、摘要、總覽表、查核紀錄、免責聲明等）裡同時有「作用機轉」「資料」「沒有」字樣的短句（本站語言的字樣在檔內 L 的 KW／DATA／NEG／EXCL）→ 依 front matter monitor_inn（INN 另對 USAN，表在 US_NAME）查 openFDA，選仿單規則同 NZ：只用單一成分、主成分名（去鹽類；酯類要相同）跟本頁相同的處方藥仿單；排序全身給藥→節錄夠長→有 12.1→有品牌名→版本新；美國只有複方仿單的只節錄 12.1 裡講本藥成分的句子並寫明是複方；節錄照原文 2～4 句、不改寫。
  紀錄寫進 `docs/_data/drug_reviews.json`（action＝mechanism，id `kr-moa-<日期>-<藥>-1`，sources 附 url、accessed、excerpt、label_version、section、set_id 或 chembl_id）；仿單與 ChEMBL 都沒有的，列進 `docs/_data/drug_reviews_uncertain.json`（source＝mechanism of action，附原因）。已有紀錄或已列待查的頁不重抓。`--list` 只列仍寫「不可得」的頁。
- 替換句格式：本站語言（한국어）的出處句＋節錄的忠實翻譯（標明「非官方翻譯」）＋英文原文（照引、為準）＋DailyMed 連結、仿單版本、取用日期（用戶 2026-11-19 決定「當地語言摘要＋英文原文」）。只換「不可得」那一句（英文站句首子句後接 so／but 的後半句是 AI 推論，保留），不加框；查核紀錄表列原句與出處。模型預測與其他正文不動。
- 翻譯：節錄的翻譯是 AI 輔助的忠實翻譯（不增不減，藥名、基因與受體符號、數字、「[…]」照原文），2026-11-19 批次產生，存在紀錄 sources 的 translation（translation_lang、translation_note 註明非官方、英文原文為準）；頁面上同時列英文原文。`--translations <檔>` 讀翻譯、`--need <檔>` 列出還沒翻的節錄（這些頁那次不寫紀錄，gate 會擋，翻好再跑）。
- 2026-11-19 結果：437 頁寫入紀錄（美國仿單 379、ChEMBL 58），94 頁列待查（美國沒有單一成分處方藥仿單、仿單段落不是作用機轉，且 ChEMBL 沒有已核准分子的機轉紀錄；多是胺基酸、維生素、礦物質、賦形劑、生物製劑或只在別國上市的藥）。
- `scripts/apply_drug_reviews.py` 支援 mechanism；gate 第 23 項（`scripts/check_seo_docs.py`，函式在 build_mechanism_reviews.gate_errors）：公開頁仍寫「不可得」、既沒有 mechanism 紀錄也沒列待查的，擋下；有紀錄沒套上的由查核紀錄那一項擋。
- 注意：節錄的是美國仿單，劑型與適應症可能跟本站市場的產品不同（例如取到外用仿單）；文字上已寫明是美國 FDA 核准仿單。`sync_notes_to_docs.py` 整頁重寫後會重套紀錄（claim 是頁面原句）；報告重產、原句改寫後要再跑 build_mechanism_reviews.py。
- 2026-11-20 補做：程式更新：同頁不只一句「不可得」時每句各一筆紀錄（-1、-2…）；同頁別筆紀錄的更正文字、錨點與已套上的節錄不再當成「不可得」句；gate 改成公開頁仍寫「不可得」、又沒列待查就擋（不再只看該頁有沒有紀錄）；ChEMBL 譯文（詞組清單）後補句號 58 筆；同 id 重發，前版 replacement 存 history。
- 2026-11-20 試跑母目錄「交付前驗證」規則時補做：偵測改成原條件不動、另加新增寫法（L2，比中的再用 NOT 排除以缺資料為前提的模型推論），字樣用獨立、更寬的偵測全量掃出的候選句逐句標註校準（A 沒有漏、B 沒有誤中）；偵測漏抓的「不可得」句補 6 筆紀錄；節錄後面接著 AI 說明「上面描述依據」的句子（會讀成美國仿單的出處）2 筆改成那句在節錄前（原文不改，只換順序）；同頁重複引用同一段節錄的 6 筆改成指向上方節錄的一句（附同一個來源連結）；以上同 id 重發，前版存 history。程式另加 reorder_src_tail、同頁已引用同一段節錄時改指向上方（產生器 txgnn/.claude/moa_rollout_20261119/fix_20261120/）。

## 說明頁與證據等級頁的在地資料（2026-11-19）

用戶 2026-11-19 決定的第一批改版（母目錄 `.claude/gen_local_pages_20261119.py` 產生，不逐站手改）：說明頁（about／guide／sources／downloads／methodology，自有結構站只有證據等級頁與隱私頁）加本站資料區塊（`<!-- local-facts -->`）、證據等級頁的事實段與藥名表（`<!-- tier-facts -->`、`<!-- tier-table -->`）、隱私頁的適用法律／權利／著作權與資料來源段（`<!-- privacy-law -->`）；en／es／de 樣板站的共用長段落縮成一段（`<!-- local-condensed -->`）。
資料檔 `docs/_data/local_facts.json`、`docs/_data/evidence_tier_facts.json` 由 `scripts/local_facts.py`（＝母目錄 `.claude/local_facts_lib.py`）依藥物頁、許可證快照、查核紀錄、FHIR 算；`apply_drug_reviews.py`、許可證快照程式結尾會自動 `--write`，`check_seo_docs.py` 跑 `--check` 擋過期。跨站欄位（cross：本站獨有預測、30 站中位數）與頁面區塊只由母目錄產生器更新；藥物頁改等級、noindex 或預測後要在母目錄重跑。

## 藥物頁 description 句尾在地化（2026-11-19）

用戶 2026-11-19 決定（「藥物頁簡述在地化」，SEO 工具判定 30 站藥物頁近似重複，原因之一是 description 句尾都是同一句「原適應症：本地資料未記載」）：公開藥物頁（排除 noindex、轉址頁）front matter description 句尾的「기존 적응증: 국내 허가 자료에 적응증 기재 없음」換成本站許可證快照事實層（`snapshots/*_licenses.json.gz`，經 `src/*/regulatory/licenses.py` 的 snapshot()）的品項數句子，資料名稱照本站口徑：식약처 허가。藥名、預測新適應症、等級字樣不動（母目錄 sync_description_levels.py 照舊對得到）；已有原適應症原文的頁不動。
例：cemiplimab「기존 적응증: 국내 허가 자료에 적응증 기재 없음」→「식약처 허가: 1건 (유효 0건)」；2026-11-19 改了 1 頁。
由母目錄 `.claude/drug_meta_description.py --apply --site KrTxGNN` 產生（站上複本 `tools/txgnn/.claude/drug_meta_description.py --apply --root .`），改動記在 `docs/_data/description_local_log.json`（pages＝目前句尾與原字樣、entries＝每次改動前後整行，可還原）。快照數字變了重跑會換新數字；`apply_drug_reviews.py`、`build_license_snapshot.py` 結尾會自動 --apply，`check_seo_docs.py` 跑 --check 擋「還是未記載句尾」或「數字跟快照不符」。只改 front matter，lastmod_fix 不算正文改動、last_modified_at 不動。
同日修：`apply_drug_reviews.py`、`build_license_snapshot.py` 結尾重算 local_facts 的 atexit 掛鉤在結束時取不到 `__file__`（NameError，之前其實沒跑成），改成先算好路徑。

## 市場段落許可證表改由程式產生（2026-11-24）

用戶 2026-11-24 決定（各站同日；本站只做表 A，正文張數 B 是 2026-11-12 起就有的 rewrite_license_counts.py）：每週許可證排程只改得到概覽表狀態列／張數列，報告（AI）寫的自由格式許可證表（多數「| 허가번호 | 제품명 | 제형 | 허가 적응증 |」，沒有狀態欄）跟著 MFDS 資料過期；改成程式依證據包產生、每週自動同步。
- `scripts/sync_license_tables.py`：「## 한국 시판 정보」段落的第一張表換成程式表「| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |」（欄位照 MFDS 原文、韓文不翻譯；허가사항＝證據包 indication 的 nedrug pdfDownload 連結，沒有就「—」）；前後 `<!-- licenses:begin -->`／`<!-- licenses:end -->`。
  狀態跟事實層同一套判斷（reviewer `_local_regulatory`）：有效「유효」，註銷寫 MFDS 취소/취하 原文（취하、유효기간만료、행정(취소)…；沒有原文、因有效期限已過算註銷的寫유효기간만료）。單方／複方不列（證據包 ingredients 只記比對到的成分，判斷不了）。
  選列：換表當時原表依序列的허가번호（`config/license_table_pins.json`，726 頁 2,450 個號）在前，其餘有效在前、再依號碼；列數＝原表列數（最多 20），所以正文「주요 허가 5건」「5건만 표시」之類說法照樣成立。原表號碼不在現行證據包的 9 頁各 1 個（allantoin、camphor、cefoperazone、crotamiton、epinephrine、esomeprazole、hydrocortisone_acetate、tocopherol、vitamin_a；部分紀錄頁、證據包換過紀錄），由程式排序的下一列補上。
  表下說明句：「위 표는 허가 M건 중 N건입니다.」；證據包只收部分紀錄（事實層 partial）時「위 표는 허가 최소 M건 중 N건입니다.」（同概覽表「최소 M건」），列完全部收錄紀錄時「이 자료에는 허가의 일부(최소 M건)만 수록되어 있습니다.」；沒有紀錄時 NONE_LINE。表下原本只講表上筆數、跟說明句重複的整行句子（CAPTION_RX，kallidinogenase、latanoprost 2 頁）換表時拿掉；句中另有事實的不動。
- 快照 `snapshots/kr_licenses.json.gz` 另存 rows（前 20 列）／nrows／partial；gate 第 18 項（`site.program_block_problems`）擋「段落有表卻不是程式區塊」「程式表（狀態欄除外）≠快照重算」「說明句不對」，狀態欄由 checker row_status_conflicts 驗。
- 誰會跑：`build_license_snapshot.py` 寫完快照後依證據包重排（`--no-rewrite` 不跑），再跑 rewrite_license_counts.py（順序不能反）；`apply_drug_reviews.py`（非 --check）結尾 `--from-snapshot` 重排（不需要 data/）再跑 B；每週排程 `license_adapter.py` 的 `sync_tables`＋`PAGE_NOTE`；`sync_notes_to_docs.py` 整頁重寫時 `carry_block` 移植舊區塊、寫完再重排。`build_license_snapshot.py` 沒給 `--ws` 時用 repo 上一層（母目錄）。
- 2026-11-24 套用（資料 data-20261123-155715）：730 頁換成程式表（公開頁 691 頁原有 AI 表、2 頁段落沒有表補上；連 noindex 共 730 頁；沒有市場段落的 2 頁不動），last_modified_at 改 2026-11-24。沒有查核紀錄錨在舊表上（superseded 0 筆）。
  查核紀錄更正文字裡的舊表筆數／寫死張數同 id 重發 9 筆（doxorubicin、zaltoprofen、doxycycline、felodipine、pemetrexed、talniflumate、temozolomide 的 11-05 紀錄，codeine、ramipril 的 11-12 紀錄；改成不寫數字的寫法、更正的事實保留，前版存 history）。
  正文寫「全部單方」而品目名其實含複方的 3 頁以 `kr-lic-20261124-{ritonavir,lansoprazole,fimasartan}-1` 更正；camphor（品目名看不出成分）與寬偵測找到的 3 句（fluticasone、tretinoin、paliperidone，有保留語或子集、count_prose 不改）列待查。
  另寫的寬偵測（正文張數跟事實層不符）改前 40 句、改後 38 句：部分紀錄頁 18 句（不可驗證）、子集／수출용／「이 외에 N건」＝總數−表列數之類一致的 15 句、待查 4 句、count_prose 原有的 premise／ambiguous 2 句。checker 全量前後 0；gate exit 0。
- 母目錄 `.claude/license_labels/KrTxGNN.json` 只有「유효」；程式表會寫的註銷字樣（취하、유효기간만료、행정(취소)、폐업）要由母目錄加進 labels（cancelled，preferred 취하），本站沒改母目錄。

## 第二輪：舊錯句逐句寫查核紀錄、劑型說法、說明樣板不寫張數（2026-11-24）

用戶 2026-11-24 第二輪決定（各站同日）：第一輪列進待查與寬偵測找到、跟 MFDS 資料（證據包 data-20261123-155715、快照事實層）相反的正文句子逐句寫 correct 紀錄；更正文字不寫死張數（指向빠른 개요與程式表）。
- 36 筆 `kr-lic-20261124b-*`（35 頁）：待查 4 句（fluticasone「총 13건」實為 14 張；tretinoin「7건」實為 14 張（有效 9）；paliperidone「총 6건」只算서방정、另有 7 張注射劑；camphor「총 16건 모두 단일제」與已收紀錄矛盾、已收紀錄有 L-멘톨／살리실산메틸複方與外用液、噴霧）；
  部分紀錄頁（事實層 partial）正文寫的總數或有效數少於已收紀錄、或「모두 단일」而已收紀錄成分欄是別的成分（＝複方）的 19 句（aminocaproic_acid、amoxicillin、arginine、ascorbic_acid、citric_acid、ebastine、entacapone、esomeprazole、hydrocortisone_acetate、lenalidomide、methionine、mometasone、morphine、potassium_iodide、prednisolone_acetate、azithromycin、sucralfate 等）；
  完整頁把有效數寫成「총／전체／허가증은 총」的 4 句（azathioprine、desogestrel、ioversol、polmacoxib）與張數不符的 aminophylline、etoricoxib、rifampicin、adenosine（漏了複方注射劑）、daunorubicin（「취소 여부 정보가 없어」）；
  劑型全稱說法 6 句（mometasone「모두 비강분무제」實有크림、isosorbide_dinitrate 漏了注射劑、epinephrine「모두 주사제」實有보스민액；fusidic_acid、scopolamine、sodium_fluoride 的待辦條目只改前提）。
- 判定成立、不改：count_prose 判斷不了的 adenosine（4 張單方的待辦，11-12 已 resolved）、alfuzosin_hydrochloride（19／16／3、全部單方，與事實層一致，待查清單加一筆 resolved）；ribavirin、tamoxifen、voglibose、bicalutamide、busulfan、sulfasalazine 的수출용張數、daunorubicin／zidovudine 的單方子集、劑型「…뿐／모두」說法 20 多句（deoxycholic_acid、isoniazid、spironolactone、bacitracin、desonide 等，逐句對照證據包全部品項成立）。
  部分紀錄頁上數字不小於已收紀錄、或劑型跟已收紀錄一致的（guaifenesin「단일 성분 8건」、fluconazole「경구 캡슐과 정제뿐」、rivastigmine「모두 경피 패취」、meloxicam 等）無法用資料證明錯，不改。
- `site.py` 的 `_fig`（reviews_from_edits 寫紀錄說明時用）改成不寫數字；說明裡寫死「이 약의 허가는 N건(유효 M건)」的 44 筆與 codeine、ramipril 的 11-12 紀錄同 id 重發（前版存 history）。
- 寬偵測（正文「N건」跟事實層任一讀法都不符；部分紀錄頁只算少於已收紀錄的）改前 29 句、改後 8 句（都是수출용子集或候選數、已逐句確認）；checker 全量前後 0；gate exit 0。
  沒有市場段落的公開頁 2 頁（agomelatine、paclitaxel）照第一輪不補段落。

## 整頁沒有市場段落的公開頁補程式表（2026-11-24 第三輪）

用戶 2026-11-24 第三輪決定（比照 JpTxGNN 第二輪的 `add_section`）：公開頁（非 noindex、非轉址）整頁沒有「## 한국 시판 정보」、但證據包有허가紀錄的，補段落與程式表。
- `scripts/sync_license_tables.py` 的 `add_section`：放在「## 안전성 고려사항」之前（沒有就「## 결론 및 다음 단계」、再沒有就「## 면책 조항」）；表與說明句照 block_for；noindex 頁、沒有紀錄的頁、快照模式（`--from-snapshot`）不補。
  證據包模式（apply_drug_reviews.py 結尾、每週排程 sync_tables）會補；`license_adapter.PAGE_NOTE` 放行補的段落標題行。
- gate 第 18 項（`src/krtxgnn/regulatory/licenses.py` 第 5 條）：公開頁快照有程式表列、卻整頁沒有市場段落就擋。
- 2026-11-24 全量量測 2 頁、補 2 頁：agomelatine（2 張，1 張취하）、paclitaxel（16 張，2 張취소）；正文「아고틴정 단일 성분 제제」「국내 단일 성분 제품」對照證據包成分成立，沒有新紀錄。checker 全量前後都是 0；gate exit 0。

## 事實層單方／複方：不可判定（2026-11-24）

用戶 2026-11-24 決定：事實層依各站成分欄正確切分；本站證據包的成分欄只記比對到的那個成分（例 아모크라주「AMOXICILLIN SODIUM」實為 amoxicillin＋clavulanate），判斷不了就不硬算。
reviewer/drug_evidence_pack.py 的 kind 改成 undetermined、不給 valid_single／valid_combo（標 kind_undeterminable）；母目錄 dump_license_facts 不給 single_total／valid_single、另標 single_undeterminable（1405 藥全部）。
`src/krtxgnn/regulatory/count_prose.py` 遇到單方／複方張數或「모두 단일」句不改，理由 single-undeterminable（`scripts/rewrite_license_counts.py --uncertain` 列進待查清單：2026-11-24 新增 41 句）；要改請依 nedrug 品目的全部成分逐張確認後寫查核紀錄。程式表本來就不列單方／複方。證據包 785 個重算（data-overlay）。
