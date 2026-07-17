---
name: verify-mindvault-quality
description: Independently assess MindVault requirements, implementations, or releases. Use when Codex must review acceptance criteria, create a test strategy, inspect test coverage, execute validation, investigate defects, verify security and privacy behavior, or issue an evidence-based release recommendation.
---

# Verify MindVault Quality

1. Read `AGENTS.md`, the complete task, acceptance criteria, relevant architecture, and changed implementation.
2. Review acceptance criteria for ambiguity and testability before implementation when requested.
3. Build a risk-based test set covering the happy path, boundaries, failure recovery, authorization, privacy, provenance, and regression risks.
4. For retrieval answers, verify grounding, citation-to-source correctness, access isolation, exact identifier retrieval, semantic retrieval, and insufficient-evidence behavior.
5. For ingestion, verify supported formats, size and duration limits, duplicate or retried processing, corrupt inputs, extraction failures, and status transitions as applicable.
6. Execute applicable automated checks and record exact commands and results. Never infer a pass from code inspection alone.
7. Report defects with severity, reproduction steps, expected and actual behavior, and file references when known.
8. Do not fix implementation unless explicitly assigned a fix. Do not weaken tests to make a build pass.

Return a pass, conditional pass, or fail recommendation with evidence and residual risks. The main agent owns final acceptance.
