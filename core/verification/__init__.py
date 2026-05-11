"""Verification — confidence calculation + source tracking."""
from .confidence import compute_confidence
from .source_tracking import distinct_source_count

__all__ = ["compute_confidence", "distinct_source_count"]
