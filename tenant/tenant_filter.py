"""
Tenant filter: given a TenantConfig + a candidate entity set, return only entities
in the tenant's inventory (or related to inventory items).

Use case: when sommelier staff app queries "show me what we have", Theseus filters
the master DB to just the OBP-carried cuvées + their producers/vineyards.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable


@dataclass
class InventoryItem:
    cuvee_id: str
    format: str = "750ml"
    available: bool = True
    price_usd: float | None = None
    team_note: str = ""             # must NOT contain personal names — validator in obp_loader


@dataclass
class TenantConfig:
    store_id: str
    store_name: str
    voice_style: str
    items: list[InventoryItem] = field(default_factory=list)

    def carried_cuvee_ids(self) -> set[str]:
        return {it.cuvee_id for it in self.items if it.available}


def filter_by_inventory(entities: Iterable[dict], tenant: TenantConfig) -> list[dict]:
    """
    Pass-through entities whose id is in the tenant inventory (cuvee) OR who is
    a producer of a carried cuvee. Other types (appellation/vintage) pass through
    since they are context, not stocked items.
    """
    carried = tenant.carried_cuvee_ids()
    # producer ids inferred from carried cuvee ids by slug prefix convention
    # ('cuvee:<producer>-<rest>' → 'producer:<producer>') — best-effort.
    producer_ids: set[str] = set()
    for cid in carried:
        if cid.startswith("cuvee:"):
            rest = cid[len("cuvee:"):]
            # producer slug = first hyphen segment if recognisable; otherwise leave empty
            first = rest.split("-")[0]
            producer_ids.add(f"producer:{first}")

    out: list[dict] = []
    for e in entities:
        et = e.get("entity_type")
        eid = e.get("id", "")
        if et == "cuvee":
            if eid in carried:
                out.append(e)
        elif et == "producer":
            if eid in producer_ids:
                out.append(e)
        else:
            out.append(e)   # appellations / vintages / vineyards = context, pass through
    return out
