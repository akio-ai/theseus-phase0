"""
Emergency Stop CLI — `python -m control.emergency_stop --reason "..."`.

Always sets KillReason.MANUAL. For programmatic engagement from other modules,
call kill_switch.engage_kill() directly with the appropriate reason.
"""
from __future__ import annotations

import argparse
import sys

from .kill_switch import KillReason, clear_kill, engage_kill, is_killed, last_engagement


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Theseus emergency stop / kill switch")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_stop = sub.add_parser("stop", help="Engage kill switch (default)")
    p_stop.add_argument("--reason", "-r", required=True, help="Short human-readable reason")
    p_stop.add_argument("--actor", "-a", default="cli", help="Actor name (default: cli)")

    sub.add_parser("status", help="Show current kill state")

    p_clear = sub.add_parser("clear", help="Clear kill switch (archives history)")
    p_clear.add_argument("--confirm", required=True, help='Must be exactly "yes-clear-kill"')

    args = parser.parse_args(argv)

    if args.cmd == "status":
        if is_killed():
            rec = last_engagement()
            print(f"KILLED — last engagement: {rec}")
            return 0
        print("not killed")
        return 0

    if args.cmd == "stop":
        path = engage_kill(KillReason.MANUAL, actor=args.actor, note=args.reason)
        print(f"engaged kill switch — {path}")
        return 0

    if args.cmd == "clear":
        if args.confirm != "yes-clear-kill":
            print("confirm token mismatch — aborting", file=sys.stderr)
            return 2
        archived = clear_kill()
        if archived is None:
            print("not killed — nothing to clear")
        else:
            print(f"cleared; history archived → {archived}")
        return 0

    return 1


if __name__ == "__main__":
    sys.exit(main())
