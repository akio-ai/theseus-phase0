"""
PostgreSQL connection management.

Uses psycopg3 (modern, async-capable). Connection params from environment so the
new VPS PostgreSQL instance can sit on a non-default port (5433 推奨) separate
from Win³.

Isolation guarantee:
- DSN is read ONLY from THESEUS_* env vars
- If THESEUS_PG_PORT == WIN3_PG_PORT (when both exposed), startup aborts
  → tests/test_isolation.py enforces
"""
from __future__ import annotations

import os
from contextlib import contextmanager
from typing import Iterator, Optional

try:
    import psycopg
    from psycopg.rows import dict_row
    from psycopg_pool import ConnectionPool
    _PSYCOPG_AVAILABLE = True
except ImportError:
    # Allow import-time loading without psycopg installed (for test scaffolding /
    # static analysis). Actual DB calls will raise.
    _PSYCOPG_AVAILABLE = False
    psycopg = None  # type: ignore
    dict_row = None  # type: ignore
    ConnectionPool = None  # type: ignore


_POOL: Optional["ConnectionPool"] = None


def _dsn() -> str:
    host = os.environ.get("THESEUS_PG_HOST", "127.0.0.1")
    port = os.environ.get("THESEUS_PG_PORT", "5433")    # Win³ と分離
    db   = os.environ.get("THESEUS_PG_DB",   "theseus")
    user = os.environ.get("THESEUS_PG_USER", "theseus")
    pw   = os.environ.get("THESEUS_PG_PASSWORD", "")

    # Isolation hard check
    win3_port = os.environ.get("WIN3_PG_PORT")
    if win3_port and win3_port == port:
        raise RuntimeError(
            f"Isolation violation: THESEUS_PG_PORT ({port}) == WIN3_PG_PORT ({win3_port}). "
            f"Theseus must run on a separate PostgreSQL instance."
        )

    return f"host={host} port={port} dbname={db} user={user} password={pw}"


def get_pool() -> "ConnectionPool":
    """Get or create the connection pool (lazy init)."""
    if not _PSYCOPG_AVAILABLE:
        raise RuntimeError("psycopg not installed — run `pip install -r requirements.txt`")
    global _POOL
    if _POOL is None:
        _POOL = ConnectionPool(
            conninfo=_dsn(),
            min_size=1,
            max_size=int(os.environ.get("THESEUS_PG_POOL_MAX", "5")),
            kwargs={"row_factory": dict_row},
        )
    return _POOL


def close_pool() -> None:
    global _POOL
    if _POOL is not None:
        _POOL.close()
        _POOL = None


@contextmanager
def get_connection() -> Iterator["psycopg.Connection"]:
    """Context-managed connection from the pool."""
    pool = get_pool()
    with pool.connection() as conn:
        yield conn
