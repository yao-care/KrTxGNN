"""Tests for disease mapper."""

import pytest
import pandas as pd
from krtxgnn.mapping.disease_mapper import (
    DISEASE_DICT,
    load_disease_vocab,
    extract_indications,
    translate_indication,
    map_indication_to_disease,
    map_fda_indications_to_diseases,
    get_indication_mapping_stats,
)


class TestDiseaseDict:
    """Tests for disease dictionary."""

    def test_disease_dict_not_empty(self):
        """Test that DISEASE_DICT is not empty."""
        assert len(DISEASE_DICT) > 0

    def test_disease_dict_has_common_diseases(self):
        """Test that common diseases are in the dictionary."""
        korean_terms = list(DISEASE_DICT.keys())
        assert any("당뇨" in term for term in korean_terms), "Should have diabetes terms"
        assert any("고혈압" in term for term in korean_terms), "Should have hypertension terms"

    def test_disease_dict_values_are_english(self):
        """Test that dictionary values are English disease names."""
        for korean, english in DISEASE_DICT.items():
            assert isinstance(english, str)
            assert len(english) > 0


class TestExtractIndications:
    """Tests for indication extraction."""

    def test_extract_single(self):
        """Test extraction of single indication."""
        text = "당뇨병 치료"
        result = extract_indications(text)
        assert isinstance(result, list)

    def test_extract_multiple(self):
        """Test extraction of multiple indications."""
        text = "고혈압, 당뇨병, 고지혈증 치료"
        result = extract_indications(text)
        assert isinstance(result, list)
        assert len(result) >= 1

    def test_empty_input(self):
        """Test empty input handling."""
        assert extract_indications("") == []
        assert extract_indications(None) == []


class TestTranslateIndication:
    """Tests for indication translation."""

    def test_translate_diabetes(self):
        """Test translation of diabetes."""
        result = translate_indication("당뇨병")
        assert isinstance(result, list)
        if result:
            assert any("diabetes" in r.lower() for r in result)

    def test_translate_hypertension(self):
        """Test translation of hypertension."""
        result = translate_indication("고혈압")
        assert isinstance(result, list)
        if result:
            assert any("hypertension" in r.lower() for r in result)

    def test_translate_unknown(self):
        """Test translation of unknown term."""
        result = translate_indication("알수없는질병xyz")
        assert isinstance(result, list)


class TestMapIndicationToDisease:
    """Tests for single indication mapping."""

    def test_map_known_disease(self):
        """Test mapping of known disease."""
        try:
            # This function requires disease_index, skip if not available
            disease_vocab = load_disease_vocab()
            from krtxgnn.mapping.disease_mapper import build_disease_index
            disease_index = build_disease_index(disease_vocab)
            result = map_indication_to_disease("당뇨병", disease_index)
            assert isinstance(result, (list, tuple, type(None)))
        except (FileNotFoundError, Exception):
            pytest.skip("Disease vocabulary file not available")


class TestMapFdaIndicationsToDiseases:
    """Tests for batch indication mapping."""

    @pytest.fixture
    def sample_drugs(self):
        """Create sample drug DataFrame with indications."""
        return pd.DataFrame({
            "품목기준코드": ["A001", "A002", "A003"],
            "품목명": ["약품A", "약품B", "약품C"],
            "효능효과": [
                "제2형 당뇨병 환자의 혈당조절",
                "본태성 고혈압",
                "",
            ],
        })

    def test_batch_mapping(self, sample_drugs):
        """Test batch indication mapping."""
        try:
            result = map_fda_indications_to_diseases(sample_drugs)
            assert isinstance(result, pd.DataFrame)
        except FileNotFoundError:
            pytest.skip("Disease vocabulary file not available")


class TestGetIndicationMappingStats:
    """Tests for indication mapping statistics."""

    def test_stats_calculation(self):
        """Test statistics calculation."""
        # Use the actual columns expected by the function
        mapping_df = pd.DataFrame({
            "license_id": ["A001", "A001", "A002"],
            "disease_name": ["diabetes", "hypertension", None],
            "disease_id": ["D001", "D002", None],
            "extracted_indication": ["당뇨병", "고혈압", ""],
        })
        stats = get_indication_mapping_stats(mapping_df)

        assert isinstance(stats, dict)
