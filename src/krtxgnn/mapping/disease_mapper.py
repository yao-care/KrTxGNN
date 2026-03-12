"""疾病映射模組 - 韓文適應症映射至 TxGNN 疾病本體

韓文 (한국어) 適應症 → 英文疾病名稱對照與 TxGNN 疾病 ID 映射。
"""

import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import pandas as pd


# 韓文→英文疾病/症狀對照表 (약 180개 항목)
DISEASE_DICT = {
    # === 심혈관계 (心血管系統, 20개) ===
    "고혈압": "hypertension",
    "저혈압": "hypotension",
    "심장병": "heart disease",
    "심근경색": "myocardial infarction",
    "협심증": "angina",
    "부정맥": "arrhythmia",
    "심계항진": "palpitation",
    "심부전": "heart failure",
    "울혈성심부전": "congestive heart failure",
    "동맥경화": "atherosclerosis",
    "정맥류": "varicose veins",
    "혈전증": "thrombosis",
    "심부정맥혈전증": "deep vein thrombosis",
    "뇌졸중": "stroke",
    "뇌경색": "cerebral infarction",
    "뇌출혈": "cerebral hemorrhage",
    "고지혈증": "hyperlipidemia",
    "이상지질혈증": "dyslipidemia",
    "관상동맥질환": "coronary artery disease",
    "말초혈관질환": "peripheral vascular disease",

    # === 호흡기계 (呼吸系統, 15개) ===
    "천식": "asthma",
    "기관지천식": "bronchial asthma",
    "기관지염": "bronchitis",
    "만성기관지염": "chronic bronchitis",
    "폐렴": "pneumonia",
    "폐결핵": "tuberculosis",
    "결핵": "tuberculosis",
    "기침": "cough",
    "만성폐쇄성폐질환": "chronic obstructive pulmonary disease",
    "감기": "common cold",
    "독감": "influenza",
    "인플루엔자": "influenza",
    "비염": "rhinitis",
    "알레르기비염": "allergic rhinitis",
    "부비동염": "sinusitis",
    "호흡곤란": "dyspnea",
    "폐기종": "emphysema",

    # === 소화기계 (消化系統, 20개) ===
    "위염": "gastritis",
    "급성위염": "acute gastritis",
    "만성위염": "chronic gastritis",
    "위궤양": "gastric ulcer",
    "십이지장궤양": "duodenal ulcer",
    "소화불량": "dyspepsia",
    "설사": "diarrhea",
    "변비": "constipation",
    "장염": "enteritis",
    "대장염": "colitis",
    "과민성대장증후군": "irritable bowel syndrome",
    "크론병": "crohn disease",
    "이질": "dysentery",
    "간염": "hepatitis",
    "B형간염": "hepatitis b",
    "C형간염": "hepatitis c",
    "간경변": "cirrhosis",
    "담석": "gallstone",
    "담낭염": "cholecystitis",
    "췌장염": "pancreatitis",
    "구역": "nausea",
    "구토": "vomiting",
    "위산과다": "hyperacidity",
    "역류성식도염": "gastroesophageal reflux disease",

    # === 신경계 (神經系統, 15개) ===
    "간질": "epilepsy",
    "뇌전증": "epilepsy",
    "두통": "headache",
    "편두통": "migraine",
    "현기증": "vertigo",
    "어지러움": "dizziness",
    "불면증": "insomnia",
    "신경통": "neuralgia",
    "좌골신경통": "sciatica",
    "파킨슨병": "parkinson disease",
    "알츠하이머병": "alzheimer disease",
    "치매": "dementia",
    "다발성경화증": "multiple sclerosis",
    "뇌막염": "meningitis",
    "말초신경병증": "peripheral neuropathy",

    # === 정신과 (精神疾病, 12개) ===
    "우울증": "depression",
    "불안장애": "anxiety disorder",
    "공황장애": "panic disorder",
    "조울증": "bipolar disorder",
    "양극성장애": "bipolar disorder",
    "조현병": "schizophrenia",
    "정신분열증": "schizophrenia",
    "강박장애": "obsessive-compulsive disorder",
    "외상후스트레스장애": "post-traumatic stress disorder",
    "주의력결핍과잉행동장애": "attention deficit hyperactivity disorder",
    "ADHD": "attention deficit hyperactivity disorder",
    "불안": "anxiety",

    # === 내분비계 (內分泌系統, 15개) ===
    "당뇨병": "diabetes mellitus",
    "제1형당뇨병": "type 1 diabetes",
    "제2형당뇨병": "type 2 diabetes",
    "갑상선기능항진증": "hyperthyroidism",
    "갑상선기능저하증": "hypothyroidism",
    "갑상선염": "thyroiditis",
    "비만": "obesity",
    "통풍": "gout",
    "고요산혈증": "hyperuricemia",
    "골다공증": "osteoporosis",
    "쿠싱증후군": "cushing syndrome",
    "애디슨병": "addison disease",
    "뇌하수체기능저하증": "hypopituitarism",
    "성장호르몬결핍증": "growth hormone deficiency",
    "대사증후군": "metabolic syndrome",

    # === 근골격계 (肌肉骨骼系統, 15개) ===
    "관절염": "arthritis",
    "류마티스관절염": "rheumatoid arthritis",
    "퇴행성관절염": "osteoarthritis",
    "골절": "fracture",
    "근육통": "myalgia",
    "요통": "back pain",
    "허리통증": "low back pain",
    "견통": "shoulder pain",
    "어깨통증": "shoulder pain",
    "경부통": "neck pain",
    "목통증": "neck pain",
    "염좌": "sprain",
    "타박상": "contusion",
    "건염": "tendinitis",
    "섬유근육통": "fibromyalgia",

    # === 피부과 (皮膚疾病, 15개) ===
    "습진": "eczema",
    "두드러기": "urticaria",
    "건선": "psoriasis",
    "피부염": "dermatitis",
    "아토피피부염": "atopic dermatitis",
    "무좀": "tinea pedis",
    "조갑진균증": "onychomycosis",
    "여드름": "acne",
    "옴": "scabies",
    "대상포진": "herpes zoster",
    "단순포진": "herpes simplex",
    "소양증": "pruritus",
    "가려움증": "pruritus",
    "화상": "burn",
    "백반증": "vitiligo",

    # === 비뇨기계 (泌尿系統, 12개) ===
    "요도염": "urethritis",
    "방광염": "cystitis",
    "신장염": "nephritis",
    "신우신염": "pyelonephritis",
    "신결석": "kidney stone",
    "요로결석": "urolithiasis",
    "전립선비대증": "prostatic hyperplasia",
    "양성전립선비대증": "benign prostatic hyperplasia",
    "요실금": "urinary incontinence",
    "빈뇨": "urinary frequency",
    "배뇨장애": "dysuria",
    "만성신장질환": "chronic kidney disease",

    # === 안과 (眼科, 8개) ===
    "결막염": "conjunctivitis",
    "녹내장": "glaucoma",
    "백내장": "cataract",
    "안구건조증": "dry eye syndrome",
    "근시": "myopia",
    "원시": "hyperopia",
    "황반변성": "macular degeneration",
    "망막병증": "retinopathy",

    # === 이비인후과 (耳鼻喉, 8개) ===
    "중이염": "otitis media",
    "외이염": "otitis externa",
    "이명": "tinnitus",
    "인두염": "pharyngitis",
    "편도염": "tonsillitis",
    "후두염": "laryngitis",
    "난청": "hearing loss",
    "메니에르병": "meniere disease",

    # === 감염증 (感染症, 15개) ===
    "세균감염": "bacterial infection",
    "바이러스감염": "viral infection",
    "진균감염": "fungal infection",
    "기생충감염": "parasitic infection",
    "패혈증": "sepsis",
    "봉와직염": "cellulitis",
    "요로감염": "urinary tract infection",
    "성병": "sexually transmitted infection",
    "AIDS": "acquired immunodeficiency syndrome",
    "HIV감염": "hiv infection",
    "말라리아": "malaria",
    "수막염": "meningitis",
    "폐렴": "pneumonia",
    "상기도감염": "upper respiratory infection",
    "하기도감염": "lower respiratory infection",

    # === 알레르기 (過敏, 8개) ===
    "알레르기": "allergy",
    "알레르기반응": "allergic reaction",
    "화분증": "hay fever",
    "꽃가루알레르기": "pollen allergy",
    "식품알레르기": "food allergy",
    "약물알레르기": "drug allergy",
    "아나필락시스": "anaphylaxis",
    "접촉성피부염": "contact dermatitis",

    # === 산부인과 (婦科, 12개) ===
    "월경불순": "menstrual disorder",
    "생리통": "dysmenorrhea",
    "월경통": "dysmenorrhea",
    "갱년기증후군": "menopause syndrome",
    "폐경증후군": "menopausal syndrome",
    "자궁내막증": "endometriosis",
    "질염": "vaginitis",
    "자궁근종": "uterine fibroid",
    "다낭성난소증후군": "polycystic ovary syndrome",
    "자궁경부암": "cervical cancer",
    "난소암": "ovarian cancer",
    "임신오조": "hyperemesis gravidarum",

    # === 종양/암 (腫瘤/癌症, 15개) ===
    "암": "cancer",
    "종양": "tumor",
    "악성종양": "malignant tumor",
    "양성종양": "benign tumor",
    "백혈병": "leukemia",
    "림프종": "lymphoma",
    "폐암": "lung cancer",
    "유방암": "breast cancer",
    "위암": "gastric cancer",
    "대장암": "colorectal cancer",
    "간암": "liver cancer",
    "전립선암": "prostate cancer",
    "췌장암": "pancreatic cancer",
    "갑상선암": "thyroid cancer",
    "신장암": "kidney cancer",

    # === 일반증상 (一般症狀, 20개) ===
    "발열": "fever",
    "열": "fever",
    "통증": "pain",
    "염증": "inflammation",
    "부종": "edema",
    "피로": "fatigue",
    "권태감": "malaise",
    "빈혈": "anemia",
    "출혈": "bleeding",
    "경련": "spasm",
    "근육경련": "muscle cramp",
    "쥐": "cramp",
    "식욕부진": "anorexia",
    "체중감소": "weight loss",
    "체중증가": "weight gain",
    "발진": "rash",
    "홍반": "erythema",
    "수면장애": "sleep disorder",
    "무력증": "asthenia",
    "탈수": "dehydration",
}


def load_disease_vocab(filepath: Optional[Path] = None) -> pd.DataFrame:
    """載入 TxGNN 疾病詞彙表"""
    if filepath is None:
        filepath = Path(__file__).parent.parent.parent.parent / "data" / "external" / "disease_vocab.csv"
    return pd.read_csv(filepath)


def build_disease_index(disease_df: pd.DataFrame) -> Dict[str, Tuple[str, str]]:
    """建立疾病名稱索引（關鍵詞 -> (disease_id, disease_name)）"""
    index = {}

    for _, row in disease_df.iterrows():
        disease_id = row["disease_id"]
        disease_name = row["disease_name"]
        name_upper = row["disease_name_upper"]

        # 完整名稱
        index[name_upper] = (disease_id, disease_name)

        # 提取關鍵詞（按空格和逗號分割）
        keywords = re.split(r"[,\s\-]+", name_upper)
        for kw in keywords:
            kw = kw.strip()
            if len(kw) > 3 and kw not in index:  # 只保留較長的關鍵詞
                index[kw] = (disease_id, disease_name)

    return index


def extract_indications(indication_str: str) -> List[str]:
    """從適應症文字提取個別適應症

    韓文適應症常見分隔符：
    - 句號 (。) - 主要分段
    - 逗號 (,) - 列舉項目
    - 分號 (;) - 項目分隔
    - 數字列表 (1. 2. 等)
    """
    if not indication_str:
        return []

    # 正規化
    text = indication_str.strip()

    # 移除數字列表標記
    text = re.sub(r'\d+[.)\]]\s*', '', text)

    # 使用分隔符分割
    parts = re.split(r'[。；;]', text)

    indications = []
    for part in parts:
        # 再用逗號細分
        sub_parts = re.split(r'[,，、]', part)
        for sub in sub_parts:
            sub = sub.strip()
            # 移除常見的非疾病描述前綴 (韓文)
            sub = re.sub(r'^(다음|아래|이하)의?\s*(질환|증상|경우)?[의에]?\s*', '', sub)
            sub = re.sub(r'^(치료|예방|완화|개선|경감)[을를에]?\s*(위한|사용)?\s*', '', sub)
            # 移除後綴
            sub = re.sub(r'(등|등의 질환|의 치료|에 사용|에 효과)$', '', sub)
            sub = sub.strip()
            if sub and len(sub) >= 2:
                indications.append(sub)

    return indications


def translate_indication(indication: str) -> List[str]:
    """將韓文適應症翻譯為英文關鍵詞"""
    keywords = []

    for ko_term, en_term in DISEASE_DICT.items():
        if ko_term in indication:
            keywords.append(en_term.upper())

    return keywords


def map_indication_to_disease(
    indication: str,
    disease_index: Dict[str, Tuple[str, str]],
) -> List[Tuple[str, str, float]]:
    """將單一適應症映射到 TxGNN 疾病

    Returns:
        [(disease_id, disease_name, confidence), ...]
    """
    results = []

    # 翻譯為英文關鍵詞
    keywords = translate_indication(indication)

    for kw in keywords:
        # 完全匹配
        if kw in disease_index:
            disease_id, disease_name = disease_index[kw]
            results.append((disease_id, disease_name, 1.0))
            continue

        # 部分匹配
        for index_kw, (disease_id, disease_name) in disease_index.items():
            if kw in index_kw or index_kw in kw:
                results.append((disease_id, disease_name, 0.8))

    # 去重並按信心度排序
    seen = set()
    unique_results = []
    for disease_id, disease_name, conf in sorted(results, key=lambda x: -x[2]):
        if disease_id not in seen:
            seen.add(disease_id)
            unique_results.append((disease_id, disease_name, conf))

    return unique_results[:5]  # 最多返回 5 個匹配


def map_fda_indications_to_diseases(
    fda_df: pd.DataFrame,
    disease_df: Optional[pd.DataFrame] = None,
    indication_field: str = "효능효과",
    license_field: str = "품목기준코드",
    brand_field: str = "품목명",
) -> pd.DataFrame:
    """將韓國 MFDS 藥品適應症映射到 TxGNN 疾病"""
    if disease_df is None:
        disease_df = load_disease_vocab()

    disease_index = build_disease_index(disease_df)

    results = []

    for _, row in fda_df.iterrows():
        indication_str = row.get(indication_field, "")
        if not indication_str or pd.isna(indication_str):
            continue

        # 提取個別適應症
        indications = extract_indications(str(indication_str))

        for ind in indications:
            # 翻譯並映射
            matches = map_indication_to_disease(ind, disease_index)

            if matches:
                for disease_id, disease_name, confidence in matches:
                    results.append({
                        "license_id": row.get(license_field, ""),
                        "brand_name": row.get(brand_field, ""),
                        "original_indication": str(indication_str)[:100],
                        "extracted_indication": ind,
                        "disease_id": disease_id,
                        "disease_name": disease_name,
                        "confidence": confidence,
                    })
            else:
                results.append({
                    "license_id": row.get(license_field, ""),
                    "brand_name": row.get(brand_field, ""),
                    "original_indication": str(indication_str)[:100],
                    "extracted_indication": ind,
                    "disease_id": None,
                    "disease_name": None,
                    "confidence": 0,
                })

    return pd.DataFrame(results)


def get_indication_mapping_stats(mapping_df: pd.DataFrame) -> dict:
    """計算適應症映射統計"""
    total = len(mapping_df)
    mapped = mapping_df["disease_id"].notna().sum()
    unique_indications = mapping_df["extracted_indication"].nunique()
    unique_diseases = mapping_df[mapping_df["disease_id"].notna()]["disease_id"].nunique()

    return {
        "total_indications": total,
        "mapped_indications": int(mapped),
        "mapping_rate": mapped / total if total > 0 else 0,
        "unique_indications": unique_indications,
        "unique_diseases": unique_diseases,
    }
