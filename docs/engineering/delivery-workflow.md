# Delivery Workflow

## Stage gates

1. Product discovery: resolve blocking questions and approve the MVP specification.
2. Architecture: define components, data model, security, ingestion, retrieval, citations, and deployment; accept ADRs.
3. Planning: split work into vertical milestones with acceptance criteria and dependencies.
4. Implementation: complete one approved task at a time.
5. Verification: QA checks acceptance criteria, regression risks, security-sensitive behavior, and operational failure paths.
6. Integration: the main agent reviews changes, runs the full applicable validation suite, and synchronizes documentation.

## Task handoff

Every implementation task must provide:

- objective and user outcome
- in-scope and out-of-scope behavior
- relevant source-of-truth links
- interfaces and file ownership
- acceptance criteria
- validation commands
- dependencies and known risks

Tasks that introduce or change a runnable service must update its Docker image and the local Docker Compose environment. Validation must include image builds and container health checks when Docker is available.

Backend and frontend work may run in parallel only when the API contract is approved and file ownership does not overlap. QA should review acceptance criteria before implementation and verify the completed integrated behavior afterward.
