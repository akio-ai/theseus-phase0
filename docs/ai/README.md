# AI Collaboration Workspace

Governance and coordination records for THÉSEUS. Nothing here is application code.

## Start here

Two documents govern how work happens, and they are meant to be read together.

**[`ai_autonomous_execution_policy.md`](ai_autonomous_execution_policy.md)** — who decides what,
what the Execution Agent does without asking, the short list of things it must stop for, the Git
safety rules, and the Projects permission position.

**[`github_projects_operations.md`](github_projects_operations.md)** — the GitHub Projects
operating model: the Status lifecycle, every field, the six views, which workflows are enabled and
which are deliberately off, and the rule that decides when implementation may begin.

> **Execution boundary.** Claude may implement only when **Status = Ready** and
> **Gate = None or Approved**. **Gate = CTO Review or CEO Decision prohibits implementation.**
>
> Within an authorized Issue, everything from branch creation to commit runs without further
> approval. Push and pull-request creation run without stopping **when the Issue authorizes them**.

## Index

| File | What it holds |
|---|---|
| [`ai_autonomous_execution_policy.md`](ai_autonomous_execution_policy.md) | How work is executed — roles, autonomous scope, stop conditions, Git safety, PR rules, Projects authority |
| [`github_projects_operations.md`](github_projects_operations.md) | The operating model — statuses, fields, views, workflows, gates |
| [`project_state.md`](project_state.md) | Where the programme stands right now |
| [`work_queue.md`](work_queue.md) | What is queued, in progress, gated or finished |
| [`claude_report.md`](claude_report.md) | Claude's report for the current task |
| [`cto_review.md`](cto_review.md) | External CTO review record |
| [`ceo_decisions.md`](ceo_decisions.md) | Approved CEO decisions only |

## Source of truth

The **THÉSEUS Development** Project is authoritative for execution state — Status, Gate, Health,
Priority. The files in this directory record and explain that state; where the two disagree, the
Project is right and the file is stale.
