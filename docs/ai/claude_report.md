# Claude Report

## Task

Establish the AI Autonomous Execution Policy (v1) as one complete governance task.

## Branch / Base

Branch **`docs/ai-autonomous-execution-policy`**, cut from canonical **`origin/main` at
`30d90d1`**, carrying a single commit.

Local `main` and `origin/main` are **divergent** (local +30, origin +11). Nothing was merged,
rebased, reset, or overwritten: this branch was created directly from `origin/main`, which is what
keeps the diff to the approved files only.

## Summary

Records how work is executed on THÉSEUS: the three roles and what each owns, the nine steps the
Execution Agent runs without intermediate approval, the approval envelope for push and PR
creation, the ten mandatory stop conditions, Git safety rules, PR keyword rules, the Projects
permission position, and the reporting contract.

## Diff

| File | Change |
|---|---|
| `docs/ai/ai_autonomous_execution_policy.md` | **New.** The policy — roles, autonomous scope, approval envelope, stop conditions, Git safety, PR rules, Projects authority, reporting, unresolved matters |
| `docs/ai/README.md` | Policy added to the index and to "Start here"; the execution boundary note now covers the autonomous run and the approval envelope |
| `docs/ai/github_projects_operations.md` | One row added to §9 pointing at the policy |
| `docs/ai/project_state.md` | Execution-source-of-truth section now references the policy, the autonomous scope, and the Project field authority |
| `docs/ai/work_queue.md` | Header references the policy; this task listed under In Review; Issue #2 moved to Completed |
| `docs/ai/claude_report.md` | This file |

Documentation only. No application code, no GitHub configuration, no test changes.

## Tests

`python3 -m pytest -q` — **85 passed**. Unchanged from the pre-existing baseline on `origin/main`;
a documentation-only change cannot affect it, and it was run to confirm exactly that.

## Risks

- **Divergent local `main`.** Local `main` carries 30 unpushed commits that `origin/main` does not
  have. This task did not touch it. Any future attempt to reconcile the two is a separate,
  explicitly-approved decision.
- **Untracked local research data.** On a branch based on `origin/main`, this repository's
  gitignored working data appears as untracked, because the `.gitignore` protecting it lives on a
  branch that is not checked out. It was not staged, moved or deleted. The policy's Git rules
  exist to keep it that way.
- **Policy scope.** The policy governs execution only. It does not alter the Project's fields,
  views or workflows, and does not change any approved architecture decision.

## Decisions

| Decision | Source |
|---|---|
| Branch cut from `origin/main`, not from local `main` | The instruction to work from canonical `origin/main` and not reconcile divergent history |
| `project` scope neither requested nor granted; `read:project` recommended as the next step | Instructed, and consistent with the existing CTO position |
| Gate recorded as a human-authorized field | Instructed |
| The PR body does not carry `Tracks #N` | No Issue exists for this task — see Stop conditions |
| Issue #2 moved to Completed in `work_queue.md` | It is merged (`30d90d1`) and closed; leaving it under In Review would have been stale |

## Required Project field transitions

The Execution Agent cannot write Project fields. A human needs to set, for this task's item:

| Field | Value |
|---|---|
| Status | **In Review** |
| Gate | **Approved** |
| Health | **On Track** |

## Stop conditions encountered

**One, and it did not block delivery.**

**No Issue exists for this task.** The only open Issue is `#1 [TASK] Phase 3B-U3`. The instruction
was to open the PR with `Tracks #<issue-number>`, and there is no number to use. Creating an Issue
was not in the approved external-action envelope, which authorized push and pull-request creation
only, so no Issue was created and no number was invented. The PR states this in its body; adding
`Tracks #N` later is a one-line edit once a number exists.

## Existing unresolved matters

- **IQ-6** — open in the `theseus-project` repository, concerning `required_for_complete`. Not
  inspected, decided, or modified.
- **U1 / U2 behaviour** — unchanged.

## Last Updated

2026-07-30
