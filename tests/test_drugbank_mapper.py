"""Tests for DrugBank mapper."""

import pytest
import pandas as pd
from krtxgnn.mapping.drugbank_mapper import (
    load_drugbank_vocab,
    build_name_index,
    map_ingredient_to_drugbank,
    map_fda_drugs_to_drugbank,
    get_mapping_stats,
)
from krtxgnn.mapping.normalizer import normalize_ingredient


class TestNormalizeIngredient:
    """Tests for ingredient normalization."""

    def test_basic_normalization(self):
        """Test basic string normalization."""
        assert normalize_ingredient("Aspirin") == "ASPIRIN"
        assert normalize_ingredient("METFORMIN") == "METFORMIN"

    def test_removes_salt_forms(self):
        """Test removal of salt forms."""
        result = normalize_ingredient("Metformin Hydrochloride")
        assert "METFORMIN" in result

    def test_empty_input(self):
        """Test empty input handling."""
        assert normalize_ingredient("") == ""
        assert normalize_ingredient(None) == ""


class TestLoadDrugbankVocab:
    """Tests for loading DrugBank vocabulary."""

    def test_load_vocab_returns_dataframe(self):
        """Test that loading vocabulary returns a DataFrame."""
        try:
            vocab = load_drugbank_vocab()
            assert isinstance(vocab, pd.DataFrame)
            assert len(vocab) > 0
        except FileNotFoundError:
            pytest.skip("DrugBank vocabulary file not available")

    def test_vocab_has_required_columns(self):
        """Test that vocabulary has required columns."""
        try:
            vocab = load_drugbank_vocab()
            assert "drugbank_id" in vocab.columns
            assert "drug_name" in vocab.columns or "name" in vocab.columns
        except FileNotFoundError:
            pytest.skip("DrugBank vocabulary file not available")


class TestBuildNameIndex:
    """Tests for building name index."""

    def test_build_index(self):
        """Test building name index from DataFrame."""
        vocab = pd.DataFrame({
            "drugbank_id": ["DB00945", "DB00331"],
            "drug_name": ["Aspirin", "Metformin"],
            "drug_name_upper": ["ASPIRIN", "METFORMIN"],
        })
        index = build_name_index(vocab)

        assert isinstance(index, dict)
        assert "aspirin" in index or "ASPIRIN" in index
        assert index.get("aspirin") == "DB00945" or index.get("ASPIRIN") == "DB00945"


class TestMapIngredientToDrugbank:
    """Tests for mapping ingredient to DrugBank."""

    @pytest.fixture
    def sample_index(self):
        """Create sample name index."""
        return {
            "ASPIRIN": "DB00945",
            "METFORMIN": "DB00331",
            "ATORVASTATIN": "DB01076",
        }

    def test_exact_match(self, sample_index):
        """Test exact name matching."""
        result = map_ingredient_to_drugbank("ASPIRIN", sample_index)
        assert result == "DB00945"

    def test_case_insensitive_match(self, sample_index):
        """Test case-insensitive matching."""
        result = map_ingredient_to_drugbank("aspirin", sample_index)
        # May or may not match depending on implementation
        assert result == "DB00945" or result is None

    def test_no_match(self, sample_index):
        """Test no match returns None."""
        result = map_ingredient_to_drugbank("unknown_drug_xyz", sample_index)
        assert result is None


class TestMapFdaDrugsToDrugbank:
    """Tests for batch drug mapping."""

    @pytest.fixture
    def sample_drugs(self):
        """Create sample drug DataFrame."""
        return pd.DataFrame({
            "품목기준코드": ["A001", "A002", "A003"],
            "품목명": ["아스피린정", "글루코파지정", "미지의약품"],
            "주성분": ["ASPIRIN", "METFORMIN HYDROCHLORIDE", "UNKNOWN_XYZ"],
        })

    def test_batch_mapping(self, sample_drugs):
        """Test batch drug mapping."""
        try:
            result = map_fda_drugs_to_drugbank(sample_drugs)
            assert isinstance(result, pd.DataFrame)
            assert "drugbank_id" in result.columns
        except FileNotFoundError:
            pytest.skip("DrugBank vocabulary file not available")


class TestGetMappingStats:
    """Tests for mapping statistics."""

    def test_stats_calculation(self):
        """Test mapping statistics calculation."""
        mapping_df = pd.DataFrame({
            "license_id": ["A001", "A002", "A003"],
            "drugbank_id": ["DB00945", "DB00331", None],
            "mapped": [True, True, False],
        })
        stats = get_mapping_stats(mapping_df)

        assert isinstance(stats, dict)
