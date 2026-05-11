"""
Tenant layer — compass enforcement of institutional voice + inventory filter.
"""
from __future__ import annotations

import json
from pathlib import Path

import pytest

from tenant.obp_loader import CompassViolation, load_obp_inventory
from tenant.tenant_filter import TenantConfig, InventoryItem, filter_by_inventory


def test_obp_inventory_loads_clean():
    tc = load_obp_inventory()
    assert tc.store_id == "OBP_NY"
    assert tc.voice_style == "institutional_team_voice"
    assert len(tc.items) > 0


def test_loader_rejects_individual_voice(tmp_path):
    bad = {
        "store_id": "BAD",
        "store_name": "Bad",
        "voice_style": "akio_voice",       # forbidden
        "items": [],
    }
    p = tmp_path / "bad.json"
    p.write_text(json.dumps(bad))
    with pytest.raises(CompassViolation, match="voice_style"):
        load_obp_inventory(p)


def test_loader_rejects_personal_name_in_note(tmp_path):
    bad = {
        "store_id": "OK",
        "store_name": "OK",
        "voice_style": "institutional_team_voice",
        "items": [{"cuvee_id": "cuvee:x", "team_note": "Akio's favourite"}],
    }
    p = tmp_path / "bad.json"
    p.write_text(json.dumps(bad))
    with pytest.raises(CompassViolation, match="personal name"):
        load_obp_inventory(p)


def test_loader_rejects_akio_prefixed_field(tmp_path):
    bad = {
        "store_id": "OK",
        "store_name": "OK",
        "voice_style": "institutional_team_voice",
        "akio_personal_field": "x",        # forbidden prefix
        "items": [],
    }
    p = tmp_path / "bad.json"
    p.write_text(json.dumps(bad))
    with pytest.raises(CompassViolation, match="forbidden field"):
        load_obp_inventory(p)


def test_filter_keeps_carried_cuvees_only():
    tc = TenantConfig(
        store_id="X", store_name="X", voice_style="institutional_team_voice",
        items=[InventoryItem(cuvee_id="cuvee:krug-grande")],
    )
    entities = [
        {"id": "cuvee:krug-grande", "entity_type": "cuvee", "name": "Krug Grande"},
        {"id": "cuvee:bollinger-r-d", "entity_type": "cuvee", "name": "Bollinger R.D."},  # not carried
        {"id": "appellation:champagne", "entity_type": "appellation", "name": "Champagne"},  # context
    ]
    out = filter_by_inventory(entities, tc)
    ids = {e["id"] for e in out}
    assert "cuvee:krug-grande" in ids
    assert "cuvee:bollinger-r-d" not in ids
    assert "appellation:champagne" in ids  # context entities pass through
