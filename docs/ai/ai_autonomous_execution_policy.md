# AI Autonomous Execution Policy

**v1.** How work is executed on THÉSEUS: who decides what, what the Execution Agent does without
asking, and the short list of things it must stop for.

The purpose is to run AI as an **execution agent**, not an assistant. The CEO decides product and
business direction and approves what cannot be undone; the External CTO owns architecture and the
GO/NO-GO; the Execution Agent takes an Issue and carries it to a reportable finish. Nobody should
be clicking through a UI on someone else's behalf.

This document governs *execution*. The Project's fields, views and workflows are governed by
[`github_projects_operations.md`](github_projects_operations.md), and the two are meant to be read
together.

---

## 1. Roles

| Role | Owns |
|---|---|
| **CEO** | Product direction · business decisions · approval of irreversible or externally consequential actions |
| **External CTO** | Architecture · boundaries · ADRs · risk · long-term maintainability · GO / NO-GO |
| **Execution Agent** | Repository work · implementation · tests · documentation · Git · approved GitHub operations |

Each role stays inside its own scope. The Execution Agent does not make product calls; the CTO
does not drive the keyboard; the CEO is not an operator for technical steps.

---

## 2. Default autonomous scope

Given an Issue, the Execution Agent proceeds **without intermediate approval** through:

1. repository identification and remote-state verification
2. branch creation
3. implementation
4. tests and validation
5. documentation
6. explicit-file staging
7. commit
8. diff review
9. completion reporting

No step in that list requires a check-in. Asking permission for a reversible local action is
itself a failure mode: it converts a decision-maker into an operator and slows the work without
reducing risk.

---

## 3. Approval envelope

An Issue may authorize external actions **in advance**. Where it does, they are part of the
autonomous run:

- **push of the task branch**
- **pull request creation**

**When these are inside the approved Issue scope, do not stop again before performing them.**
The approval was given when the Issue was written; asking twice is asking once too often.

Anything not named in the Issue's approval envelope remains subject to §4.

---

## 4. Mandatory stop conditions

Stop, report, and wait — for these only:

- unapproved architecture or domain-model changes
- CEO product decisions
- merge to a protected branch
- production changes
- security or permission changes
- cost or external-service commitments
- deletion of non-generated data
- Git history rewriting
- destructive or difficult-to-reverse actions
- **material conflict between approved requirements**

The last one matters as much as the rest. When two approved documents disagree, or an Issue asks
for something an accepted decision forbids, the correct output is the contradiction — not a
resolution invented to keep moving.

**Stopping is not failure.** An agent that stops at the right line is worth more than one that
guesses past it.

---

## 5. Git safety

**Prohibited by default:**

| Command | Why |
|---|---|
| `git add -A` | Sweeps in whatever happens to be untracked, including gitignored local data that exists on one branch and not another |
| `git add .` | Same, scoped to a directory |
| `git clean -fd` | Deletes untracked files with no way back |
| `git clean -fdx` | Also deletes ignored files — the ones most likely to be irreplaceable local data |
| `git reset --hard` | Discards work with no reflog trail for the working tree |
| rebase of shared history | Rewrites commits others may hold |
| force push | Overwrites the remote's version of history |

**Required:**

```
git add <explicit paths>
```

Every path named. If a file was not deliberately chosen, it is not staged.

*This is not theoretical.* A branch based on an older commit can expose a repository's gitignored
working data as untracked — research inputs, generated exports, local stores — because the
`.gitignore` that protects them lives on a branch that is not checked out. A single `-A` or
`-fdx` in that state commits or destroys them.

### Ordering rule

**Repository identification and remote-state verification come before file discovery or
implementation.** Confirm the origin URL, fetch, and establish ahead/behind/divergence *first*.
Searching the filesystem before knowing which repository and which commit is being looked at
produces confident answers about the wrong thing.

---

## 6. Pull request rules

- **Use `Tracks #N` by default.**
- **Do not use `Closes #N`, `Fixes #N`, `Resolves #N`** or any equivalent auto-closing keyword,
  unless the Issue explicitly authorizes automatic closure.
- **A merged PR must not automatically imply Done.**

### Why the keyword matters

An auto-closing keyword creates this chain:

```
PR body: Closes #N  →  PR merged  →  Issue auto-closed
                    →  "Item closed" workflow  →  Status: Done
```

That reaches Done through a merge alone, which is exactly what disabling
`Pull request merged → Done` was meant to prevent. The keyword routes around the control rather
than tripping it.

### Done

Done requires **all four**:

1. **merged**
2. **validated**
3. **required documentation updated**
4. **acceptance criteria satisfied**

If any one is unmet, the item is **In Review**, not Done.

---

## 7. GitHub Projects authority

Current policy, pending a separate permission decision:

- The Execution Agent **may report** required Project transitions.
- The Execution Agent **must not modify Project fields** without separately approved GitHub
  Projects write permission.
- **Gate remains a human-authorized decision field.**

### The permission position

`project` scope is **not requested and not granted** by this policy, and authentication is not
changed by it.

**Recommended next least-privilege step: `read:project`.** It would let the Execution Agent verify
and report Project state — which it currently cannot see at all — without gaining the ability to
change it.

**A constraint worth stating plainly:** GitHub Projects permissions are not per-field. A token
with write access to a Project can write **every** field, Gate included. So "the Execution Agent
does not change Gate" can be enforced *mechanically* only by withholding write scope; with write
scope granted, it is a rule the agent keeps, not a barrier it cannot cross. Whichever is chosen,
the distinction should be recorded rather than assumed.

---

## 8. Reporting

**No routine step-by-step updates.** Report **once, at completion**, with:

| Section | Contents |
|---|---|
| **Summary** | What was done |
| **Diff** | Files changed, and the shape of the change |
| **Tests** | Commands run and their actual results |
| **Risks** | What could go wrong, and what was done about it |
| **Decisions** | Choices made, and the source that authorized each |
| **Required Project field transitions** | What a human needs to set, since the agent cannot |
| **Any stop condition encountered** | Which one, and what it blocks |

Report what was actually executed. A check that was not run is reported as not run, never as
passing.

---

## 9. Existing unresolved matters

- **IQ-6** — an open Implementation Question concerning `required_for_complete` in the
  `theseus-project` repository. Recorded here only so that it is not lost. **Not to be inspected,
  decided, or modified** under this policy.
- **U1 and U2 behaviour** is not changed by this policy.

---

## 10. Relationship to the other governance documents

| Document | Governs |
|---|---|
| **This policy** | How work is executed, and who approves what |
| [`github_projects_operations.md`](github_projects_operations.md) | The Project: lifecycle, fields, views, workflows |
| [`project_state.md`](project_state.md) | Where the programme stands |
| [`work_queue.md`](work_queue.md) | What is queued, in flight, gated or finished |
| [`cto_review.md`](cto_review.md) | External CTO review records |
| [`ceo_decisions.md`](ceo_decisions.md) | Approved CEO decisions only |

Where this policy and the Projects operating model overlap, they agree by construction: the
operating model says a gate blocks implementation, and this policy says what the agent does with
that fact.
