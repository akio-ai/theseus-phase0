-- Theseus Core — initial schema (Phase 0)
-- Run after CREATE DATABASE theseus and CREATE EXTENSION vector;

-- ===== Extensions =====
CREATE EXTENSION IF NOT EXISTS vector;
CREATE EXTENSION IF NOT EXISTS pgcrypto;   -- for gen_random_uuid (audit log)
CREATE EXTENSION IF NOT EXISTS pg_trgm;    -- fuzzy match for dedup

-- ===== Enums =====
DO $$ BEGIN
    CREATE TYPE layer_t AS ENUM ('public', 'private');
EXCEPTION WHEN duplicate_object THEN NULL; END $$;

DO $$ BEGIN
    CREATE TYPE source_tier_t AS ENUM (
        'government', 'regional', 'producer', 'public_data', 'akios_notes', 'licensed'
    );
EXCEPTION WHEN duplicate_object THEN NULL; END $$;


-- ===== Entities =====
-- Single polymorphic table keyed by entity_type + slug-style id.
-- JSONB carries entity-specific fields; pgvector for semantic search.
CREATE TABLE IF NOT EXISTS entities (
    id              TEXT PRIMARY KEY,                      -- 'producer:krug' / 'cuvee:krug-grande-cuvee-170'
    entity_type     TEXT NOT NULL,                         -- 'producer' | 'cuvee' | 'vineyard' | 'appellation' | 'vintage'
    name            TEXT NOT NULL,
    layer           layer_t NOT NULL DEFAULT 'public',
    confidence      REAL NOT NULL DEFAULT 0.0,             -- 0.0–1.0
    facts           JSONB NOT NULL DEFAULT '{}'::jsonb,    -- entity-specific structured facts
    embedding       vector(1536),                          -- text-embedding semantics, populated later
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    CHECK (confidence >= 0.0 AND confidence <= 1.0)
);

CREATE INDEX IF NOT EXISTS idx_entities_type      ON entities (entity_type);
CREATE INDEX IF NOT EXISTS idx_entities_name_trgm ON entities USING gin (name gin_trgm_ops);
CREATE INDEX IF NOT EXISTS idx_entities_facts     ON entities USING gin (facts);
CREATE INDEX IF NOT EXISTS idx_entities_layer     ON entities (layer);
-- pgvector ANN index (HNSW preferred over IVFFlat for our query patterns)
CREATE INDEX IF NOT EXISTS idx_entities_embedding
    ON entities USING hnsw (embedding vector_cosine_ops);


-- ===== Source refs (provenance) =====
CREATE TABLE IF NOT EXISTS source_refs (
    id              BIGSERIAL PRIMARY KEY,
    entity_id       TEXT NOT NULL REFERENCES entities (id) ON DELETE CASCADE,
    url             TEXT NOT NULL,
    tier            source_tier_t NOT NULL,
    license         TEXT NOT NULL,
    fetched_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    excerpt_hash    TEXT,                                  -- SHA256, NOT raw text (ethical guardrails)
    note            TEXT DEFAULT ''
);
CREATE INDEX IF NOT EXISTS idx_sourcerefs_entity ON source_refs (entity_id);
CREATE INDEX IF NOT EXISTS idx_sourcerefs_tier   ON source_refs (tier);


-- ===== Relations (typed edges) =====
CREATE TABLE IF NOT EXISTS relations (
    id              BIGSERIAL PRIMARY KEY,
    subject_id      TEXT NOT NULL REFERENCES entities (id) ON DELETE CASCADE,
    predicate       TEXT NOT NULL,                         -- RelationType enum value
    object_id       TEXT NOT NULL REFERENCES entities (id) ON DELETE CASCADE,
    confidence      REAL NOT NULL DEFAULT 0.0,
    extra           JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    UNIQUE (subject_id, predicate, object_id),
    CHECK (confidence >= 0.0 AND confidence <= 1.0)
);
CREATE INDEX IF NOT EXISTS idx_relations_subject ON relations (subject_id, predicate);
CREATE INDEX IF NOT EXISTS idx_relations_object  ON relations (object_id, predicate);


-- ===== Conflict log (gap #2 — disaster guard) =====
-- When upsert detects contradicting source data for the same field, a row is
-- written here and the entity flagged provisional until human review.
CREATE TABLE IF NOT EXISTS conflicts (
    id              BIGSERIAL PRIMARY KEY,
    entity_id       TEXT NOT NULL REFERENCES entities (id) ON DELETE CASCADE,
    field_path      TEXT NOT NULL,                         -- JSONB path, e.g. 'facts.dosage_g_l'
    old_value       JSONB,
    new_value       JSONB,
    old_source_url  TEXT,
    new_source_url  TEXT,
    detected_at     TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    resolved_at     TIMESTAMPTZ,
    resolution_note TEXT
);
CREATE INDEX IF NOT EXISTS idx_conflicts_unresolved ON conflicts (entity_id) WHERE resolved_at IS NULL;


-- ===== Audit log =====
-- Every mutation logs here for disaster recovery / 矛盾巻き戻し.
CREATE TABLE IF NOT EXISTS audit_log (
    id              BIGSERIAL PRIMARY KEY,
    op              TEXT NOT NULL,                         -- 'insert' | 'update' | 'delete'
    entity_id       TEXT,
    actor           TEXT NOT NULL,                         -- 'crawler:civc' / 'akio_manual' / 'verifier:reconcile'
    payload_before  JSONB,
    payload_after   JSONB,
    occurred_at     TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
CREATE INDEX IF NOT EXISTS idx_audit_entity ON audit_log (entity_id, occurred_at DESC);
CREATE INDEX IF NOT EXISTS idx_audit_time   ON audit_log (occurred_at DESC);


-- ===== Health view =====
CREATE OR REPLACE VIEW v_health AS
SELECT
    (SELECT COUNT(*) FROM entities)                                AS total_entities,
    (SELECT COUNT(*) FROM entities WHERE entity_type='producer')   AS producers,
    (SELECT COUNT(*) FROM entities WHERE entity_type='cuvee')      AS cuvees,
    (SELECT COUNT(*) FROM entities WHERE entity_type='vineyard')   AS vineyards,
    (SELECT COUNT(*) FROM entities WHERE entity_type='appellation') AS appellations,
    (SELECT COUNT(*) FROM entities WHERE entity_type='vintage')    AS vintages,
    (SELECT COUNT(*) FROM conflicts WHERE resolved_at IS NULL)     AS open_conflicts,
    (SELECT COUNT(*) FROM entities WHERE confidence < 0.5)         AS low_confidence_entities,
    (SELECT COUNT(*) FROM source_refs)                             AS total_sources,
    NOW()                                                          AS as_of;
