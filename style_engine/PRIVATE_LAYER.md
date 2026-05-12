# Style Engine — PRIVATE LAYER

This module captures human-in-the-loop interaction data (Akio's flags, edits,
pairing choices, quiz answers) for **internal training material only**.

## Compass posture

The Theseus project compass (see `project_theseus_compass.md`) holds that the
system is a **collective knowledge layer**, not an individual's externalization.
Therefore:

- Interaction data captured here is INPUT to the system's learning loop, never
  surfaced as a sellable artifact.
- The product offered to customers under the name "Style Learning Engine" is
  generic — it learns from each tenant's head sommelier as an institutional
  pattern, not from a named individual.
- This file's contents do not enter Anki staff decks, tenant briefings, public
  API responses, or any marketing material.

## Enforcement

| Layer | Mechanism |
|---|---|
| File system | Default DB path is `style_engine/private/interactions.db` — gitignored |
| Code | `interaction_logger.log_interaction()` writes only to the private DB |
| Test | `tests/test_style_engine.py::test_db_under_private_dir` asserts path |
| Test | `tests/test_anki_layer_isolation.py` asserts no Akio/Matsumoto name in staff output |
| Loader | `tenant/obp_loader.py` rejects `akio_*` fields and personal names in notes |

## Commercialization ban

Every row carries `commercialization_ban = 1`. This is a permanent flag — there
is no API to clear it. If you find a code path that exports any of this data to
a customer-visible surface, **stop and escalate**; that path violates the
compass.

## What IS commercializable (the public Style Learning Engine)

- Generic learning of "this tenant's style" without naming the head sommelier
- Patterns derived from interactions, after aggregation + anonymization at Phase 2
- The Theseus Core knowledge base itself (Tier 1-4 public sources)
- Tier 5 Akio's Notes — but only as institutional content under "OBP sommelier
  team", never attributed individually

## What is NOT commercializable

- Raw interaction logs from this module
- Akio's identifier in any form (name, email, kanji)
- Per-tenant data without that tenant's consent

## Phase 2 plan

When training begins:
1. Bulk export from `interactions.db`
2. Strip identifiers (replace with stable opaque tenant id)
3. Aggregate to pattern level (no per-event records cross the boundary)
4. Train style classifier in a separate environment
5. Model artifacts are commercializable; training data stays here
