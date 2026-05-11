"""Per-source extractors. Each yields (entity_kind, source_url, excerpt) tuples."""
from . import civc, wikidata, inao_fr, producer_websites

__all__ = ["civc", "wikidata", "inao_fr", "producer_websites"]
