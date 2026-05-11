"""
Shared pytest fixtures.

Each test gets a fresh tmp THESEUS_KILL_FILE so kill switch tests don't leak across
test cases.
"""
from __future__ import annotations

import os
from pathlib import Path

import pytest


@pytest.fixture(autouse=True)
def isolated_kill_file(tmp_path, monkeypatch):
    """Redirect kill file to a tmp path for every test."""
    p = tmp_path / ".killed"
    monkeypatch.setenv("THESEUS_KILL_FILE", str(p))
    yield p
