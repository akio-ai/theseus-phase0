"""Theseus central control — kill switch + emergency stop (gap #1)."""
from .kill_switch import is_killed, engage_kill, clear_kill, KillReason

__all__ = ["is_killed", "engage_kill", "clear_kill", "KillReason"]
