"""
Funnel Instrumentation v0 — Phase 0 captures, Phase 1 SaaS decisions data-driven.

Modules:
  - lead_signals  : detect head-sommelier behaviour from usage patterns
  - invite_tracker: 1 month free per invite, 3+ invites → store lead promotion
  - b2b_pipeline  : flag individual → B2B (sends to #b2b-leads)
  - usage_analytics: aggregate stats per user/tenant
"""
from .lead_signals import score_lead, LEAD_THRESHOLD
from .invite_tracker import record_invite, invite_count, is_store_lead, STORE_LEAD_THRESHOLD
from .b2b_pipeline import flag_for_b2b, b2b_pipeline_status
from .usage_analytics import record_event, usage_summary

__all__ = [
    "score_lead", "LEAD_THRESHOLD",
    "record_invite", "invite_count", "is_store_lead", "STORE_LEAD_THRESHOLD",
    "flag_for_b2b", "b2b_pipeline_status",
    "record_event", "usage_summary",
]
