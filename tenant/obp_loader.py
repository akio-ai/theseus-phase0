"""
Load OBP inventory JSON → TenantConfig.

Compass enforcement:
- Top-level voice_style MUST be "institutional_team_voice"
- Reject any field starting with "akio_" or containing personal-name patterns
"""
from __future__ import annotations

import json
import os
import re
from pathlib import Path

from .tenant_filter import InventoryItem, TenantConfig


# Forbidden field patterns (compass: no individual naming)
_FORBIDDEN_FIELD_RE = re.compile(r"^(akio_|matsumoto_|owner_)", re.IGNORECASE)
_FORBIDDEN_VALUE_RE = re.compile(r"\b(akio|matsumoto)\b", re.IGNORECASE)


class CompassViolation(ValueError):
    """Raised when tenant config violates public/private layer separation."""


def _validate(raw: dict) -> None:
    if raw.get("voice_style") != "institutional_team_voice":
        raise CompassViolation(
            f"voice_style must be 'institutional_team_voice', got {raw.get('voice_style')!r}"
        )
    for k in raw.keys():
        if _FORBIDDEN_FIELD_RE.match(k):
            raise CompassViolation(f"forbidden field name: {k}")
    # Field values must not name individuals
    for item in raw.get("items", []):
        if isinstance(item.get("team_note"), str) and _FORBIDDEN_VALUE_RE.search(item["team_note"]):
            raise CompassViolation(
                f"item team_note contains personal name: {item.get('cuvee_id')}"
            )


def load_obp_inventory(path: str | os.PathLike | None = None) -> TenantConfig:
    if path is None:
        path = Path(__file__).resolve().parent / "obp_inventory.json"
    raw = json.loads(Path(path).read_text())
    _validate(raw)
    return TenantConfig(
        store_id=raw["store_id"],
        store_name=raw["store_name"],
        voice_style=raw["voice_style"],
        items=[InventoryItem(**{k: v for k, v in it.items() if not k.startswith("_")})
               for it in raw.get("items", [])],
    )
