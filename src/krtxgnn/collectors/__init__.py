"""Data collectors for evidence gathering.

KrTxGNN - 韓國版本
"""

from .base import BaseCollector, CollectorResult
from .clinicaltrials import ClinicalTrialsCollector
from .drugbank import DrugBankCollector
from .ictrp import ICTRPCollector
from .pubmed import PubMedCollector
from .krfda import KrFDACollector, CRISCollector

__all__ = [
    "BaseCollector",
    "ClinicalTrialsCollector",
    "CollectorResult",
    "CRISCollector",
    "DrugBankCollector",
    "ICTRPCollector",
    "KrFDACollector",
    "PubMedCollector",
]
