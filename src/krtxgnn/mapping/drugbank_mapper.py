"""DrugBank 映射模組"""

import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import pandas as pd

from .normalizer import extract_ingredients, get_all_synonyms


def load_drugbank_vocab(filepath: Optional[Path] = None) -> pd.DataFrame:
    """載入 DrugBank 詞彙表

    Args:
        filepath: CSV 檔案路徑，預設為 data/external/drugbank_vocab.csv

    Returns:
        DrugBank 詞彙表 DataFrame
    """
    if filepath is None:
        filepath = Path(__file__).parent.parent.parent.parent / "data" / "external" / "drugbank_vocab.csv"

    return pd.read_csv(filepath)


def build_name_index(drugbank_df: pd.DataFrame) -> Dict[str, str]:
    """建立名稱索引（名稱 -> DrugBank ID）

    Args:
        drugbank_df: DrugBank 詞彙表

    Returns:
        名稱到 ID 的對照字典
    """
    index = {}

    for _, row in drugbank_df.iterrows():
        name_upper = row["drug_name_upper"]
        drugbank_id = row["drugbank_id"]

        # 完整名稱
        index[name_upper] = drugbank_id

        # 移除常見鹽類後綴，建立別名
        # 例如 "METFORMIN HCL" -> "METFORMIN"
        salt_suffixes = [
            " HCL", " HYDROCHLORIDE", " SODIUM", " POTASSIUM",
            " SULFATE", " SULPHATE", " MALEATE", " ACETATE",
            " CITRATE", " PHOSPHATE", " BROMIDE", " CHLORIDE",
            " TARTRATE", " FUMARATE", " SUCCINATE", " MESYLATE",
            " BESYLATE", " CALCIUM", " MAGNESIUM", " NITRATE",
            " LACTATE", " GLUCONATE", " DISODIUM", " MONOHYDRATE",
            " DIHYDRATE", " TRIHYDRATE", " ANHYDROUS",
            " DIPROPIONATE", " PROPIONATE", " ACETONIDE",
            " VALERATE", " BUTYRATE", " HEXAHYDRATE",
        ]

        for suffix in salt_suffixes:
            if name_upper.endswith(suffix):
                base_name = name_upper[:-len(suffix)].strip()
                if base_name and base_name not in index:
                    index[base_name] = drugbank_id

    # 添加常見同義詞對照
    # 格式：{FDA 成分名稱: DrugBank 名稱}
    synonym_map = {
        # ===== 維生素（通用名 -> DrugBank 化學名）=====
        "NIACINAMIDE": "NICOTINAMIDE",
        "NICOTINIC ACID": "NIACIN",
        "VITAMIN B1": "THIAMINE",
        "THIAMINE HCL": "THIAMINE",
        "THIAMINE MONONITRATE": "THIAMINE",
        "VITAMIN B2": "RIBOFLAVIN",
        "VITAMIN B6": "PYRIDOXINE",
        "PYRIDOXINE HCL": "PYRIDOXINE",
        "VITAMIN B12": "CYANOCOBALAMIN",
        "VITAMIN C": "ASCORBIC ACID",
        "VITAMIN E": "TOCOPHEROL",
        "TOCOPHEROL ACETATE": "ALPHA-TOCOPHEROL ACETATE",
        "ALPHA-TOCOPHEROL": "TOCOPHEROL",
        "VITAMIN A": "RETINOL",
        "RETINOL PALMITATE": "RETINOL",
        "VITAMIN D3": "CHOLECALCIFEROL",
        "VITAMIN D2": "ERGOCALCIFEROL",
        "VITAMIN K1": "PHYTONADIONE",
        "PANTOTHENATE CALCIUM": "PANTOTHENIC ACID",
        "CALCIUM PANTOTHENATE": "PANTOTHENIC ACID",
        "PANTHENOL": "DEXPANTHENOL",
        "D-PANTHENOL": "DEXPANTHENOL",
        # ===== 常見藥物別名 =====
        "ASPIRIN": "ACETYLSALICYLIC ACID",
        "PARACETAMOL": "ACETAMINOPHEN",
        "ADRENALINE": "EPINEPHRINE",
        "L-ADRENALINE": "EPINEPHRINE",
        "NORADRENALINE": "NOREPINEPHRINE",
        "LIGNOCAINE": "LIDOCAINE",
        "FRUSEMIDE": "FUROSEMIDE",
        "SALBUTAMOL": "ALBUTEROL",
        "SIMETHICONE": "DIMETHICONE",
        "ALUMINUM HYDROXIDE DRIED GEL": "ALUMINUM HYDROXIDE",
        "ALUMINIUM HYDROXIDE": "ALUMINUM HYDROXIDE",
        # ===== 葡萄糖/右旋糖 =====
        "DEXTROSE": "D-GLUCOSE",
        "DEXTROSE MONOHYDRATE": "D-GLUCOSE",
        "GLUCOSE": "D-GLUCOSE",
        "GLUCOSE MONOHYDRATE": "D-GLUCOSE",
        # ===== L-/D-/DL- 前綴處理 =====
        "L-MENTHOL": "LEVOMENTHOL",
        "MENTHOL": "LEVOMENTHOL",
        "DL-MENTHOL": "RACEMENTHOL",
        "DL-METHIONINE": "METHIONINE",
        "L-METHIONINE": "METHIONINE",
        "L-LYSINE HCL": "LYSINE",
        "L-LYSINE": "LYSINE",
        # ===== 水合物/無水形式 =====
        "CAFFEINE ANHYDROUS": "CAFFEINE",
        "ATORVASTATIN CALCIUM TRIHYDRATE": "ATORVASTATIN",
        "LIDOCAINE HCL MONOHYDRATE": "LIDOCAINE",
        # ===== 抗生素 =====
        "AMOXYCILLIN": "AMOXICILLIN",
        "CEPHRADINE": "CEFRADINE",
        "RIFAMPIN": "RIFAMPICIN",
        "GENTAMYCIN": "GENTAMICIN",
        # ===== 心血管藥物 =====
        "AMLODIPINE BESILATE": "AMLODIPINE",
        # ===== 免疫抑制劑 =====
        "CYCLOSPORIN": "CYCLOSPORINE",
        "CICLOSPORIN": "CYCLOSPORINE",
        # ===== 通用映射 =====
        "ALCOHOL": "ETHANOL",
        "L-CARNITINE": "LEVOCARNITINE",
        "L-CYSTEINE": "CYSTEINE",
        "PHYTOMENADIONE": "PHYLLOQUINONE",
        "HYOSCINE": "SCOPOLAMINE",
        "ISOPROTERENOL": "ISOPRENALINE",
        "TORSEMIDE": "TORASEMIDE",
        "URSODIOL": "URSODEOXYCHOLIC ACID",
        "VALACYCLOVIR": "VALACICLOVIR",
        # ===== 常見化合物 =====
        "CALCIUM": "CALCIUM",
        "MAGNESIUM": "MAGNESIUM",
        "ZINC": "ZINC",
        "BIOTIN": "BIOTIN",
        "FOLIC ACID": "FOLIC ACID",
        "CHARCOAL": "ACTIVATED CHARCOAL",
        "CAMPHOR": "CAMPHOR",
        "WARFARIN": "WARFARIN",
        "IBUPROFEN": "IBUPROFEN",
        "METFORMIN": "METFORMIN",
        "ATROPINE": "ATROPINE",
        "EPINEPHRINE": "EPINEPHRINE",
        "THEOPHYLLINE": "THEOPHYLLINE",
        "CAFFEINE": "CAFFEINE",
        # ===== 韓國 MFDS 특유 변형 =====
        # 수화물/무수물 형태
        "ANHYDROUS CAFFEINE": "CAFFEINE",
        "CAFFEINE ANHYDROUS": "CAFFEINE",
        "MAGNESIUM SULFATE HYDRATE": "MAGNESIUM SULFATE",
        "CALCIUM CHLORIDE HYDRATE": "CALCIUM CHLORIDE",
        "ATROPINE SULFATE HYDRATE": "ATROPINE",
        "DEXTROMETHORPHAN HYDROBROMIDE HYDRATE": "DEXTROMETHORPHAN",
        "AMINOPHYLLINE HYDRATE": "AMINOPHYLLINE",
        "SODIUM LACTATE SOLUTION": "SODIUM LACTATE",
        # 복합 성분
        "CAFFEINE·SODIUM BENZOATE": "CAFFEINE",
        "CAFFEINE SODIUM BENZOATE": "CAFFEINE",
        # 건조 형태
        "DRIED ALUMINIUM HYDROXIDE GEL": "ALUMINUM HYDROXIDE",
        "DRIED ALUMINUM HYDROXIDE GEL": "ALUMINUM HYDROXIDE",
        "PRECIPITATED CALCIUM CARBONATE": "CALCIUM CARBONATE",
        # 비타민
        "PHYTONADIONE": "PHYTONADIONE",
        "FURSULTIAMINE": "THIAMINE",
        "BENFOTIAMINE": "THIAMINE",
        "THIAMINE DISULFIDE": "THIAMINE",
        "MECOBALAMIN": "VITAMIN B12",
        "METHYLCOBALAMIN": "VITAMIN B12",
        "HYDROXOCOBALAMIN": "VITAMIN B12",
        # 일반적인 약물 별칭
        "GLIBENCLAMIDE": "GLYBURIDE",
        "GLIPIZIDE": "GLIPIZIDE",
        "BROMELAIN": "BROMELAIN",
        "HUMAN NORMAL SERUM ALBUMIN": "ALBUMIN HUMAN",
        "HUMAN SERUM ALBUMIN": "ALBUMIN HUMAN",
        # 효소/소화제
        "BIODIASTASE": "DIASTASE",
        "BIODIASTASE 500": "DIASTASE",
        "PANCREATIN": "PANCRELIPASE",
        # 한방/생약 성분 (일부 DrugBank에 있는 것만)
        "EPHEDRA HERB": "EPHEDRINE",
        "EPHEDRAE HERBA": "EPHEDRINE",
        "GINSENG": "GINSENG",
        "GINSENG RADIX": "GINSENG",
        "GLYCYRRHIZA": "GLYCYRRHIZIC ACID",
        "GLYCYRRHIZAE RADIX": "GLYCYRRHIZIC ACID",
        "LICORICE": "GLYCYRRHIZIC ACID",
        "LICORICE ROOT": "GLYCYRRHIZIC ACID",
        "GINGER": "GINGER",
        "ZINGIBERIS RHIZOMA": "GINGER",
        "CINNAMON": "CINNAMON",
        "CINNAMOMI CORTEX": "CINNAMON",
        "MENTHA": "MENTHOL",
        "MENTHAE HERBA": "MENTHOL",
        "PLATYCODON ROOT": "PLATYCODIN",
        "PLATYCODON ROOT POWDER": "PLATYCODIN",
        "SCUTELLARIA": "BAICALIN",
        "SCUTELLARIAE RADIX": "BAICALIN",
        # 항생제 변형
        "CEFACLOR": "CEFACLOR",
        "CEPHALEXIN MONOHYDRATE": "CEPHALEXIN",
        "AMOXICILLIN TRIHYDRATE": "AMOXICILLIN",
        "AMPICILLIN TRIHYDRATE": "AMPICILLIN",
        "PENICILLIN G POTASSIUM": "BENZYLPENICILLIN",
        "PENICILLIN G SODIUM": "BENZYLPENICILLIN",
        # 진통소염제
        "ACETYLSALICYLIC ACID": "ASPIRIN",
        "MEFENAMIC ACID": "MEFENAMIC ACID",
        "PIROXICAM": "PIROXICAM",
        "TENOXICAM": "TENOXICAM",
        "LORNOXICAM": "LORNOXICAM",
        "ACECLOFENAC": "ACECLOFENAC",
        # 위장약
        "RANITIDINE HYDROCHLORIDE": "RANITIDINE",
        "CIMETIDINE": "CIMETIDINE",
        "NIZATIDINE": "NIZATIDINE",
        "SUCRALFATE": "SUCRALFATE",
        "BISMUTH SUBCITRATE": "BISMUTH",
        "BISMUTH SUBSALICYLATE": "BISMUTH",
        # 심혈관계
        "NIFEDIPINE": "NIFEDIPINE",
        "DILTIAZEM HYDROCHLORIDE": "DILTIAZEM",
        "VERAPAMIL HYDROCHLORIDE": "VERAPAMIL",
        "PROPRANOLOL HYDROCHLORIDE": "PROPRANOLOL",
        "ATENOLOL": "ATENOLOL",
        "METOPROLOL TARTRATE": "METOPROLOL",
        "CAPTOPRIL": "CAPTOPRIL",
        "ENALAPRIL MALEATE": "ENALAPRIL",
        "LOSARTAN POTASSIUM": "LOSARTAN",
        "CANDESARTAN CILEXETIL": "CANDESARTAN",
        "IRBESARTAN": "IRBESARTAN",
        "TELMISARTAN": "TELMISARTAN",
        "HYDROCHLOROTHIAZIDE": "HYDROCHLOROTHIAZIDE",
        "FUROSEMIDE": "FUROSEMIDE",
        "SPIRONOLACTONE": "SPIRONOLACTONE",
        # 신경계/정신과
        "DIAZEPAM": "DIAZEPAM",
        "LORAZEPAM": "LORAZEPAM",
        "ALPRAZOLAM": "ALPRAZOLAM",
        "CLONAZEPAM": "CLONAZEPAM",
        "ZOLPIDEM TARTRATE": "ZOLPIDEM",
        "AMITRIPTYLINE HYDROCHLORIDE": "AMITRIPTYLINE",
        "FLUOXETINE HYDROCHLORIDE": "FLUOXETINE",
        "SERTRALINE HYDROCHLORIDE": "SERTRALINE",
        "PAROXETINE HYDROCHLORIDE": "PAROXETINE",
        "HALOPERIDOL": "HALOPERIDOL",
        "RISPERIDONE": "RISPERIDONE",
        "OLANZAPINE": "OLANZAPINE",
        "QUETIAPINE FUMARATE": "QUETIAPINE",
        "CARBAMAZEPINE": "CARBAMAZEPINE",
        "VALPROIC ACID": "VALPROIC ACID",
        "PHENYTOIN SODIUM": "PHENYTOIN",
        "LEVODOPA": "LEVODOPA",
        "CARBIDOPA": "CARBIDOPA",
        # 호흡기계
        "SALBUTAMOL SULFATE": "ALBUTEROL",
        "TERBUTALINE SULFATE": "TERBUTALINE",
        "IPRATROPIUM BROMIDE": "IPRATROPIUM",
        "MONTELUKAST SODIUM": "MONTELUKAST",
        "ZAFIRLUKAST": "ZAFIRLUKAST",
        "CETIRIZINE HYDROCHLORIDE": "CETIRIZINE",
        "LORATADINE": "LORATADINE",
        "FEXOFENADINE HYDROCHLORIDE": "FEXOFENADINE",
        "CHLORPHENIRAMINE MALEATE": "CHLORPHENIRAMINE",
        "DIPHENHYDRAMINE HYDROCHLORIDE": "DIPHENHYDRAMINE",
        # 당뇨병약
        "METFORMIN HYDROCHLORIDE": "METFORMIN",
        "GLICLAZIDE": "GLICLAZIDE",
        "GLIMEPIRIDE": "GLIMEPIRIDE",
        "PIOGLITAZONE HYDROCHLORIDE": "PIOGLITAZONE",
        "ROSIGLITAZONE MALEATE": "ROSIGLITAZONE",
        "ACARBOSE": "ACARBOSE",
        "VOGLIBOSE": "VOGLIBOSE",
        "SITAGLIPTIN PHOSPHATE": "SITAGLIPTIN",
        # 고지혈증
        "ATORVASTATIN CALCIUM": "ATORVASTATIN",
        "SIMVASTATIN": "SIMVASTATIN",
        "PRAVASTATIN SODIUM": "PRAVASTATIN",
        "ROSUVASTATIN CALCIUM": "ROSUVASTATIN",
        "FENOFIBRATE": "FENOFIBRATE",
        "GEMFIBROZIL": "GEMFIBROZIL",
        "EZETIMIBE": "EZETIMIBE",
        # 항응고제
        "WARFARIN SODIUM": "WARFARIN",
        "HEPARIN SODIUM": "HEPARIN",
        "ENOXAPARIN SODIUM": "ENOXAPARIN",
        "CLOPIDOGREL BISULFATE": "CLOPIDOGREL",
        "ASPIRIN": "ASPIRIN",
        "TICLOPIDINE HYDROCHLORIDE": "TICLOPIDINE",
        # 스테로이드
        "PREDNISOLONE": "PREDNISOLONE",
        "METHYLPREDNISOLONE": "METHYLPREDNISOLONE",
        "DEXAMETHASONE": "DEXAMETHASONE",
        "BETAMETHASONE": "BETAMETHASONE",
        "HYDROCORTISONE": "HYDROCORTISONE",
        "TRIAMCINOLONE": "TRIAMCINOLONE",
        # 피부과
        "TRETINOIN": "TRETINOIN",
        "ADAPALENE": "ADAPALENE",
        "CLOTRIMAZOLE": "CLOTRIMAZOLE",
        "MICONAZOLE NITRATE": "MICONAZOLE",
        "KETOCONAZOLE": "KETOCONAZOLE",
        "TERBINAFINE HYDROCHLORIDE": "TERBINAFINE",
        # 안과
        "TIMOLOL MALEATE": "TIMOLOL",
        "LATANOPROST": "LATANOPROST",
        "TRAVOPROST": "TRAVOPROST",
        "BRIMONIDINE TARTRATE": "BRIMONIDINE",
        "PILOCARPINE HYDROCHLORIDE": "PILOCARPINE",
        # 비뇨기계
        "TAMSULOSIN HYDROCHLORIDE": "TAMSULOSIN",
        "ALFUZOSIN HYDROCHLORIDE": "ALFUZOSIN",
        "FINASTERIDE": "FINASTERIDE",
        "DUTASTERIDE": "DUTASTERIDE",
        "SILDENAFIL CITRATE": "SILDENAFIL",
        "TADALAFIL": "TADALAFIL",
        # 갑상선
        "LEVOTHYROXINE SODIUM": "LEVOTHYROXINE",
        "PROPYLTHIOURACIL": "PROPYLTHIOURACIL",
        "METHIMAZOLE": "METHIMAZOLE",
        # 골다공증
        "ALENDRONATE SODIUM": "ALENDRONIC ACID",
        "RISEDRONATE SODIUM": "RISEDRONIC ACID",
        "IBANDRONATE SODIUM": "IBANDRONIC ACID",
        "RALOXIFENE HYDROCHLORIDE": "RALOXIFENE",
        "CALCITONIN": "CALCITONIN",
        # 통풍
        "ALLOPURINOL": "ALLOPURINOL",
        "COLCHICINE": "COLCHICINE",
        "FEBUXOSTAT": "FEBUXOSTAT",
        "BENZBROMARONE": "BENZBROMARONE",
        # 면역억제제
        "TACROLIMUS": "TACROLIMUS",
        "CICLOSPORIN": "CYCLOSPORINE",
        "CYCLOSPORINE": "CYCLOSPORINE",
        "AZATHIOPRINE": "AZATHIOPRINE",
        "MYCOPHENOLATE MOFETIL": "MYCOPHENOLIC ACID",
        "METHOTREXATE": "METHOTREXATE",
        # 항암제 일부
        "TAMOXIFEN CITRATE": "TAMOXIFEN",
        "LETROZOLE": "LETROZOLE",
        "ANASTROZOLE": "ANASTROZOLE",
        "IMATINIB MESYLATE": "IMATINIB",
        "GEFITINIB": "GEFITINIB",
        "ERLOTINIB HYDROCHLORIDE": "ERLOTINIB",
    }

    for alias, canonical in synonym_map.items():
        if canonical in index and alias not in index:
            index[alias] = index[canonical]

    return index


def map_ingredient_to_drugbank(
    ingredient: str,
    name_index: Dict[str, str],
) -> Optional[str]:
    """將單一成分映射到 DrugBank ID

    映射策略（優先順序）：
    1. 完全匹配
    2. 移除鹽類後綴後匹配
    3. 使用基本名稱匹配

    Args:
        ingredient: 標準化後的成分名稱
        name_index: 名稱索引

    Returns:
        DrugBank ID，若無法映射則回傳 None
    """
    if not ingredient:
        return None

    ingredient = ingredient.upper().strip()

    # 1. 完全匹配
    if ingredient in name_index:
        return name_index[ingredient]

    # 2. 移除台灣 FDA 常見的鹽類後綴
    salt_patterns = [
        r"\s+HCL$", r"\s+HYDROCHLORIDE$", r"\s+SODIUM$",
        r"\s+POTASSIUM$", r"\s+SULFATE$", r"\s+MALEATE$",
        r"\s+ACETATE$", r"\s+CITRATE$", r"\s+PHOSPHATE$",
        r"\s+BROMIDE$", r"\s+CHLORIDE$", r"\s+TARTRATE$",
        r"\s+HBR$", r"\s+HYDROBROMIDE$", r"\s+FUMARATE$",
        r"\s+SUCCINATE$", r"\s+MESYLATE$", r"\s+BESYLATE$",
        r"\s+CALCIUM$", r"\s+MAGNESIUM$", r"\s+NITRATE$",
        r"\s+LACTATE$", r"\s+GLUCONATE$", r"\s+DISODIUM$",
        r"\s+ANHYDROUS$", r"\s+MONOHYDRATE$", r"\s+DIHYDRATE$",
        r"\s+TRIHYDRATE$", r"\s+HEXAHYDRATE$",
        r"\s+DIPROPIONATE$", r"\s+PROPIONATE$", r"\s+ACETONIDE$",
        r"\s+VALERATE$", r"\s+BUTYRATE$", r"\s+MONONITRATE$",
    ]

    base_ingredient = ingredient
    for pattern in salt_patterns:
        base_ingredient = re.sub(pattern, "", base_ingredient)

    if base_ingredient != ingredient and base_ingredient in name_index:
        return name_index[base_ingredient]

    # 2b. 移除 L-/D-/DL- 前綴
    prefix_patterns = [r"^L-", r"^D-", r"^DL-"]
    base_ingredient = ingredient
    for pattern in prefix_patterns:
        base_ingredient = re.sub(pattern, "", base_ingredient)

    if base_ingredient != ingredient and base_ingredient in name_index:
        return name_index[base_ingredient]

    # 3. 嘗試移除括號內容
    base_ingredient = re.sub(r"\s*\([^)]*\)", "", ingredient).strip()
    if base_ingredient != ingredient and base_ingredient in name_index:
        return name_index[base_ingredient]

    return None


def map_fda_drugs_to_drugbank(
    fda_df: pd.DataFrame,
    drugbank_df: Optional[pd.DataFrame] = None,
    ingredient_field: str = "주성분",
    license_field: str = "품목기준코드",
    name_field: str = "품목명",
) -> pd.DataFrame:
    """將藥品映射到 DrugBank

    Args:
        fda_df: FDA 藥品 DataFrame
        drugbank_df: DrugBank 詞彙表（可選）
        ingredient_field: 成分欄位名稱
        license_field: 許可證欄位名稱
        name_field: 品名欄位名稱

    Returns:
        包含映射結果的 DataFrame
    """
    if drugbank_df is None:
        drugbank_df = load_drugbank_vocab()

    # 建立索引
    name_index = build_name_index(drugbank_df)

    results = []

    for _, row in fda_df.iterrows():
        ingredient_str = row.get(ingredient_field, "")
        if not ingredient_str or pd.isna(ingredient_str):
            continue

        # 提取所有成分及同義詞
        synonyms_data = get_all_synonyms(str(ingredient_str))

        for main_name, synonyms in synonyms_data:
            drugbank_id = None
            mapping_source = "failed"

            # 先嘗試主名稱
            drugbank_id = map_ingredient_to_drugbank(main_name, name_index)
            if drugbank_id:
                mapping_source = "drugbank"

            # 若失敗，嘗試同義詞
            if drugbank_id is None:
                for syn in synonyms:
                    drugbank_id = map_ingredient_to_drugbank(syn, name_index)
                    if drugbank_id:
                        mapping_source = "drugbank_synonym"
                        break

            results.append({
                "license_id": row.get(license_field, ""),
                "brand_name": row.get(name_field, ""),
                "original_ingredient": str(ingredient_str),
                "normalized_ingredient": main_name,
                "synonyms": "; ".join(synonyms) if synonyms else "",
                "drugbank_id": drugbank_id,
                "mapping_success": drugbank_id is not None,
                "mapping_source": mapping_source,
            })

    return pd.DataFrame(results)


def get_mapping_stats(mapping_df: pd.DataFrame) -> dict:
    """計算映射統計

    Args:
        mapping_df: 映射結果 DataFrame

    Returns:
        統計字典
    """
    total = len(mapping_df)
    success = mapping_df["mapping_success"].sum() if "mapping_success" in mapping_df.columns else 0
    unique_ingredients = mapping_df["normalized_ingredient"].nunique() if "normalized_ingredient" in mapping_df.columns else 0
    unique_drugbank = mapping_df[mapping_df["mapping_success"]]["drugbank_id"].nunique() if "mapping_success" in mapping_df.columns else 0

    return {
        "total_ingredients": total,
        "mapped_ingredients": int(success),
        "mapping_rate": success / total if total > 0 else 0,
        "unique_ingredients": unique_ingredients,
        "unique_drugbank_ids": unique_drugbank,
    }
