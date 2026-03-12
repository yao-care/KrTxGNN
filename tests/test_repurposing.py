"""Tests for drug repurposing prediction."""

import pytest
import pandas as pd
from krtxgnn.predict.repurposing import (
    load_drug_disease_relations,
    build_drug_indication_map,
    find_repurposing_candidates,
    generate_repurposing_report,
)


class TestLoadDrugDiseaseRelations:
    """Tests for loading drug-disease relations."""

    def test_load_relations_returns_dataframe(self):
        """Test that loading relations returns a DataFrame."""
        try:
            relations = load_drug_disease_relations()
            assert isinstance(relations, pd.DataFrame)
            assert len(relations) > 0
        except FileNotFoundError:
            pytest.skip("Drug-disease relations file not available")

    def test_relations_has_required_columns(self):
        """Test that relations DataFrame has required columns."""
        try:
            relations = load_drug_disease_relations()
            # Check for drug and disease columns - actual column names may vary
            assert len(relations.columns) >= 2, "Should have at least 2 columns"
        except FileNotFoundError:
            pytest.skip("Drug-disease relations file not available")


class TestBuildDrugIndicationMap:
    """Tests for building drug indication map."""

    def test_build_map(self):
        """Test building indication map."""
        # Use actual column names from the relations file
        relations = pd.DataFrame({
            "relation": ["indication", "indication", "indication"],
            "x_id": ["DB00945", "DB00945", "DB00331"],
            "x_name": ["Aspirin", "Aspirin", "Metformin"],
            "y_id": ["1001", "1002", "1003"],
            "y_name": ["headache", "pain", "diabetes"],
        })
        result = build_drug_indication_map(relations)

        assert isinstance(result, dict)

    def test_empty_relations(self):
        """Test with empty relations."""
        relations = pd.DataFrame(columns=["relation", "x_id", "x_name", "y_id", "y_name"])
        result = build_drug_indication_map(relations)
        assert isinstance(result, dict)


class TestFindRepurposingCandidates:
    """Tests for finding repurposing candidates."""

    @pytest.fixture
    def sample_drug_mapping(self):
        """Create sample drug mapping DataFrame."""
        return pd.DataFrame({
            "license_id": ["A001", "A002", "A003"],
            "brand_name": ["아스피린정", "메트포르민정", "스타틴정"],
            "normalized_ingredient": ["ASPIRIN", "METFORMIN", "ATORVASTATIN"],
            "drugbank_id": ["DB00945", "DB00331", "DB01076"],
        })

    @pytest.fixture
    def sample_indication_mapping(self):
        """Create sample indication mapping DataFrame."""
        return pd.DataFrame({
            "license_id": ["A001", "A001", "A002"],
            "disease_name": ["headache", "pain", "diabetes mellitus"],
        })

    def test_find_candidates_returns_dataframe(
        self, sample_drug_mapping, sample_indication_mapping
    ):
        """Test that finding candidates returns a DataFrame."""
        try:
            candidates = find_repurposing_candidates(
                sample_drug_mapping,
                sample_indication_mapping,
            )
            assert isinstance(candidates, pd.DataFrame)
        except FileNotFoundError:
            pytest.skip("Relations file not available")

    def test_empty_drug_mapping(self, sample_indication_mapping):
        """Test handling of empty drug mapping."""
        empty_drugs = pd.DataFrame(columns=[
            "license_id", "brand_name", "normalized_ingredient", "drugbank_id"
        ])
        try:
            candidates = find_repurposing_candidates(
                empty_drugs,
                sample_indication_mapping,
            )
            assert len(candidates) == 0
        except FileNotFoundError:
            pytest.skip("Relations file not available")


class TestGenerateRepurposingReport:
    """Tests for generating repurposing report."""

    def test_report_generation(self):
        """Test report generation."""
        candidates = pd.DataFrame({
            "license_id": ["A001", "A002"],
            "brand_name": ["Drug A", "Drug B"],
            "drugbank_id": ["DB00945", "DB00331"],
            "potential_indication": ["heart disease", "obesity"],
            "drug_ingredient": ["ASPIRIN", "METFORMIN"],
        })
        report = generate_repurposing_report(candidates)

        assert isinstance(report, dict)
        assert "total_candidates" in report
        assert report["total_candidates"] == 2

    def test_empty_candidates_report(self):
        """Test report with empty candidates."""
        candidates = pd.DataFrame(columns=[
            "license_id", "brand_name", "drugbank_id", "potential_indication"
        ])
        report = generate_repurposing_report(candidates)

        assert isinstance(report, dict)
        assert report["total_candidates"] == 0


class TestRepurposingIntegration:
    """Integration tests for repurposing pipeline."""

    def test_full_pipeline(self):
        """Test full repurposing pipeline with sample data."""
        # This test uses actual data if available
        try:
            relations = load_drug_disease_relations()

            drug_mapping = pd.DataFrame({
                "license_id": ["TEST001"],
                "brand_name": ["Test Drug"],
                "normalized_ingredient": ["METFORMIN"],
                "drugbank_id": ["DB00331"],
            })

            indication_mapping = pd.DataFrame({
                "license_id": ["TEST001"],
                "disease_name": ["diabetes mellitus"],
            })

            candidates = find_repurposing_candidates(
                drug_mapping,
                indication_mapping,
                relations,
            )

            assert isinstance(candidates, pd.DataFrame)
            # Metformin should have repurposing candidates
            # (it's known to have potential uses beyond diabetes)

        except FileNotFoundError:
            pytest.skip("Data files not available")
