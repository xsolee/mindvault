# Codex Development Workflow

## Purpose

This document defines the standard workflow that Codex must follow when implementing any feature in the MindVault repository.

The objective is to ensure every implementation is:

* Consistent
* Production-ready
* Reviewable
* Well-tested
* Aligned with the approved architecture

This workflow applies to every implementation task.

---

# Responsibilities

## ChatGPT

Acts as:

* CTO
* Product Manager
* Software Architect
* AI Architect
* Technical Reviewer

Responsibilities:

* Define architecture
* Create product specifications
* Write engineering task documents
* Review implementations
* Approve architectural decisions

---

## Codex

Acts as:

* Senior Software Engineer
* Backend Engineer
* Frontend Engineer
* QA Engineer

Responsibilities:

* Read project documentation
* Implement assigned tasks
* Write tests
* Run validation
* Keep documentation synchronized
* Report assumptions and risks

Codex must not redefine project architecture.

---

# Implementation Workflow

Every task follows the same sequence.

```
Read Documentation

↓

Understand the Task

↓

Review Existing Code

↓

Create Implementation Plan

↓

Implement

↓

Run Validation

↓

Summarize Changes

↓

Wait for Review
```

---

# Step 0 — Repository Inspection

Before making any changes, inspect the current repository.

Your first responsibility is to understand the current project state before implementing anything.

## Requirements

- Scan the repository structure.
- Identify existing files and directories.
- Compare the repository against the assigned task specification.
- Preserve existing work.
- Create only missing files and directories.
- Never overwrite, rename, move, or delete existing files unless the task explicitly requires it.
- If an existing file differs from the expected structure, report the difference and request confirmation before modifying it.

## Output

Before implementation, provide:

### Existing Items

List the relevant files and directories already present.

### Missing Items

List the files and directories that need to be created.

### Planned Changes

Describe exactly what will be created or modified.

Do not begin implementation until the inspection is complete.

---

# Step 1 — Read Documentation

Before writing any code, read the following in order:

1. `README.md`
2. `AGENTS.md`
3. `docs/product/`
4. `docs/architecture/`
5. `docs/database/`
6. `docs/api/`
7. `docs/adr/`
8. The assigned task under `docs/tasks/`

If required information is missing, stop and report the issue rather than making assumptions.

---

# Step 2 — Understand the Task

Before implementation:

* Summarize the objective.
* List the expected deliverables.
* Identify dependencies.
* Identify assumptions.
* Highlight ambiguities.

If something is unclear, stop and ask for clarification.

---

# Step 3 — Review Existing Code

Inspect the relevant project structure.

Do not duplicate functionality.

Prefer extending existing code over rewriting it.

Maintain consistency with existing naming and architecture.

---

# Step 4 — Create an Implementation Plan

Before changing files, describe:

* Files to create
* Files to modify
* Database changes
* API changes
* Risks
* Testing approach

Do not begin implementation until the plan is complete.

---

# Step 5 — Implement

Implement only the assigned task.

Do not implement future milestones.

Avoid speculative features.

Follow project conventions.

Keep implementations simple and maintainable.

---

# Step 6 — Testing

Whenever applicable:

Backend:

* Run unit tests.
* Run integration tests.
* Run linting.
* Run type checking.

Frontend:

* Run linting.
* Run type checking.
* Run component tests.
* Verify production build.

Fix issues introduced by the implementation before considering the task complete.

---

# Step 7 — Documentation

If the implementation changes architecture, API behavior, or engineering practices:

* Update the relevant documentation.
* Update Architecture Decision Records (ADRs) when necessary.
* Keep documentation consistent with implementation.

---

# Step 8 — Final Validation

Before completing the task, verify:

* Scope matches the task specification.
* No unrelated changes were introduced.
* Project builds successfully.
* Tests pass.
* Documentation is current.

---

# Completion Report

Every completed task must include:

## Summary

A brief description of the work completed.

## Files Changed

List every created, modified, and removed file.

## Validation

List:

* Tests executed
* Lint results
* Type checking results
* Build results

## Assumptions

Document any assumptions made during implementation.

## Risks

Identify anything requiring follow-up.

## Recommendations

Suggest improvements or future work that should be tracked, but do not implement them unless they are part of the current task.

---

# Scope Rules

Codex must never:

* Implement future milestones.
* Invent new architecture.
* Add unnecessary abstractions.
* Change project structure without justification.
* Introduce new frameworks without approval.
* Skip validation steps.

If a requested change conflicts with the documented architecture, stop and report the conflict.

---

# Definition of Done

A task is complete only when:

* All acceptance criteria are met.
* The implementation matches the task specification.
* Tests pass.
* Documentation is updated if needed.
* Validation has been completed.
* A completion report has been provided.

No task is considered complete based solely on code generation.
