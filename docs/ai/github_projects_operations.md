# GitHub Projects Operating Model

How work is tracked, gated and executed for THÉSEUS. This document is the operating model
itself — the Project's fields and views are the mechanism, and this file is the rule they
enforce.

| | |
|---|---|
| **Project** | THÉSEUS Development |
| **Default repository** | `akio-ai/theseus-phase0` |
| **Visibility** | Private |

---

## 1. Execution boundary — the rule that matters most

**Claude may begin implementation only when both hold:**

- **Status = Ready**, and
- **Gate = None** or **Gate = Approved**

**Gate = CTO Review or Gate = CEO Decision prohibits implementation.** Not "discouraged" —
prohibited. An item sitting behind either gate is waiting on a human decision, and starting work
on it pre-empts that decision rather than informing it.

Any other combination is not an invitation to proceed. `Status = Ready` with an open gate is
still blocked; an approved gate on an item that is not Ready is still not startable.

### Which gate an item needs

| Work | Gate |
|---|---|
| Routine, local, reversible | **None** |
| Architecture or boundary decisions | **CTO Review** |
| Data model decisions | **CTO Review** |
| Security-sensitive changes | **CTO Review** |
| Production-impacting changes | **CEO Decision** |
| Costly work, or anything with an external dependency | **CEO Decision** |
| Anything difficult to reverse | **CEO Decision** |

When it is unclear whether a change is reversible, treat it as irreversible and take the gate.

---

## 2. Status lifecycle

```
Inbox → Design → Ready → In Progress → In Review → Done
```

| Status | Meaning |
|---|---|
| **Inbox** | Newly added work, not yet triaged or approved |
| **Design** | Requirements, boundaries, acceptance criteria or architecture are being defined |
| **Ready** | Design is approved and implementation may begin |
| **In Progress** | Implementation is actively in progress |
| **In Review** | Implementation is awaiting technical or product review |
| **Done** | Changes are **merged**, **validated**, **required documentation is updated**, and **acceptance criteria are satisfied** |

**Done requires all four.** A merge alone is not Done, a passing test run alone is not Done, and
an item whose documentation has not been updated is not Done regardless of what the code does.
See §8.

---

## 3. Fields

### Priority

| Value | Meaning |
|---|---|
| **P0 — Critical** | Highest urgency |
| **P1 — High** | |
| **P2 — Normal** | |
| **P3 — Later** | |

### Workstream

Product · Architecture · Domain & Data · Backend · Frontend · AI · Infrastructure ·
Developer Experience · Documentation · Governance

### Size

**XS · S · M · L · XL**

**XL should normally be decomposed before implementation.** An XL item is usually a sign that the
boundaries are not yet settled — split it during Design rather than discovering the seams while
implementing.

### Risk

**Low · Medium · High · Critical**

Risk is about consequence, not difficulty. A one-line change to a production boundary is
higher-risk than a large change to a local document.

### Health

| Value | Meaning |
|---|---|
| **On Track** | Progressing as expected |
| **At Risk** | Progress is threatened but work continues |
| **Blocked** | Work cannot continue |

**Blocked is an attribute, not a workflow Status.** An item does not move backwards along the
lifecycle because it became blocked — it keeps its Status and carries `Health = Blocked`. This
keeps "where the work stands" and "whether it can move" as two separate facts.

**A blocked item must state all three:**

1. **the blocker** — what specifically is preventing progress;
2. **the required decision or owner** — who must act, or what must be decided;
3. **the unblock condition** — what has to become true for work to resume.

A `Blocked` item without those three is not actionable and cannot be triaged by anyone else.

### Gate

**None · CTO Review · CEO Decision · Approved**

See §1 for what each permits.

---

## 4. Views

| # | View | Layout | Filter |
|---|---|---|---|
| 1 | **01 — Intake** | Table | `status:Inbox,Design` |
| 2 | **02 — Execution** | Board grouped by Status | `status:Ready,"In Progress","In Review"` |
| 3 | **03 — CTO Review** | Table | `gate:"CTO Review"` |
| 4 | **04 — CEO Decisions** | Table | `gate:"CEO Decision"` |
| 5 | **05 — Risks & Blocks** | Table | `health:"At Risk",Blocked` |
| 6 | **06 — Completed** | Table | `status:Done` |

Views 03 and 04 are the queues that hold up implementation; views 01 and 02 are where work is
shaped and executed; view 05 exists so that a blocked item cannot quietly stall.

---

## 5. Enabled workflows

| Workflow | Effect |
|---|---|
| **Auto-add to project** | Repository `akio-ai/theseus-phase0`, filter `is:issue is:open` |
| **Item added to project** | → `Status: Inbox` |
| **Item closed** | → `Status: Done` |
| **Item reopened** | → `Status: Design` |
| **Auto-close issue when Status becomes Done** | Closes the issue |
| **Pull request linked to issue** | → `Status: In Progress` |
| **Code changes requested** | → `Status: In Progress` |
| **Auto-archive closed issues after four weeks** | `is:issue is:closed updated:<@today-4w` |

Reopening returns an item to **Design**, not to Ready — if something came back, its requirements
or acceptance criteria are in question until someone says otherwise.

---

## 6. Disabled workflows

| Workflow | Why it is off |
|---|---|
| **Pull request merged → Done** | See §8 |
| **Auto-add sub-issues to project** | Sub-issues enter deliberately, not automatically |
| **Code review approved automation** | An approving review is not by itself completion |

---

## 7. Automation boundary

**A merged pull request must not automatically produce Done.**

Merge is only one part of completion. The other three — validation, required documentation
updates, and satisfaction of the acceptance criteria — are not observable from a merge event, so
no automation can assert them.

**A human, or an authorized review, must confirm validation, documentation and acceptance
criteria before Status is set to Done.**

This is why `Pull request merged → Done` and the code-review-approved automation are both
disabled while `Item closed → Status: Done` stays on: closing an issue is a deliberate human act
that can carry that judgement, and merging a branch is not.

---

## 8. What Done actually requires

Before an item may be set to Done, all four must be true:

1. **Merged** — the change is in its target branch.
2. **Validated** — the repository's documented checks were run and their results recorded.
3. **Documentation updated** — every document the change makes stale has been brought current.
4. **Acceptance criteria satisfied** — each criterion on the item is met, not merely attempted.

If any one is unmet, the correct Status is **In Review**, not Done.

---

## 9. Relationship to the other files here

| File | Role |
|---|---|
| `project_state.md` | Where the programme stands right now |
| `work_queue.md` | What is queued, in progress, gated or finished |
| `claude_report.md` | Claude's report for the current task |
| `cto_review.md` | The External CTO's review record |
| `ceo_decisions.md` | Approved CEO decisions only |

**The Project is the execution source of truth.** These files record and explain; where a file and
the Project disagree about Status, Gate or Health, the Project is authoritative and the file is
stale.
