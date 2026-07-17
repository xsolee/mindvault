# MVP Requirements

Status: Approved

## Objective

Deliver a multi-user personal knowledge service that captures voice, text, and supported documents; retrieves related evidence across those sources; and answers questions with verifiable citations.

## Functional requirements

### Accounts and isolation

- `FR-001`: A user can create an account, authenticate, sign out, and recover access through an approved secure flow.
- `FR-002`: A user can access only their own sources, derived content, conversations, exports, and deletion operations.
- `FR-003`: The service supports multiple independent accounts without shared workspaces.

### Voice capture

- `FR-010`: An Android user can start, pause, resume, finish, and discard a recording through a low-interaction flow.
- `FR-011`: Recording can continue during temporary network loss and, where Android permits, while the screen is locked.
- `FR-012`: A completed offline recording uploads when connectivity returns, with visible progress and recoverable failure states.
- `FR-013`: A recording is limited to a configurable 30 minutes for MVP.
- `FR-014`: The system preserves the original audio and produces a timestamped transcript.

### Text and document capture

- `FR-020`: A user can create a plain-text note through web or Android.
- `FR-021`: A user can upload PDF, DOCX, TXT, and Markdown documents through web or Android.
- `FR-022`: A document is limited to a configurable 25 MB for MVP.
- `FR-023`: The system preserves the original upload and extracts searchable content without modifying the source.
- `FR-024`: Processing status exposes queued, processing, ready, and failed states with safe retry behavior.

### Language processing

- `FR-030`: The system accepts English, Filipino, and mixed-language sources and questions.
- `FR-031`: The system preserves original text or transcription and creates a separate English normalized representation when needed.
- `FR-032`: Citations always resolve to original source evidence, not only translated or normalized text.

### Retrieval and answers

- `FR-040`: Retrieval combines exact identifiers, lexical matching, metadata, and semantic vector similarity.
- `FR-041`: A user can ask questions across all of their ready sources.
- `FR-042`: Follow-up questions may use messages from the current conversation only.
- `FR-043`: Every substantive answer claim must be supported by citations to authorized source evidence.
- `FR-044`: A citation can open the original source and the most precise available location: extracted passage, document location, or audio timestamp.
- `FR-045`: The system refuses to generate a factual answer when evidence does not satisfy the approved retrieval policy.
- `FR-046`: The system never requires users to create tags; exact references such as `JIRA-100` are detected and retrieved from content.

### Content lifecycle

- `FR-050`: Users cannot edit source-derived transcripts, extracted text, or generated answers in MVP.
- `FR-051`: A user can delete an owned source and remove it from active retrieval along with its derived data.
- `FR-052`: Deleted data may remain encrypted in backups for at most 30 days and is then permanently expired.
- `FR-053`: A user can request a ZIP export containing original sources, transcripts, notes, and JSON metadata.

### Plans and usage

- `FR-060`: The product model supports Free Trial, Starter, and Pro plans.
- `FR-061`: Plan limits for transcription, storage, ingestion, and questions are configurable and enforceable.
- `FR-062`: Billing collection and final allowances are deferred until unit economics are approved.

## Quality requirements

- `QR-001 Security`: Enforce authorization before storage access, processing, retrieval, model input, citation resolution, export, or deletion.
- `QR-002 Privacy`: Design for Philippine users and document applicable privacy obligations before production launch.
- `QR-003 Provenance`: Maintain traceability from every searchable chunk and answer citation to an owned original source.
- `QR-004 Reliability`: Make uploads and asynchronous processing idempotent, retry-safe, and observable.
- `QR-005 Safety`: Do not require reading or multi-step navigation during the driving capture flow.
- `QR-006 Accessibility`: Web and mobile user flows meet the accessibility criteria selected in frontend architecture.
- `QR-007 Portability`: Keep provider integrations replaceable and support managed-cloud and self-hosted Docker deployments.
- `QR-008 Recoverability`: Document backup, restore, deletion-expiry, and disaster-recovery behavior before launch.
- `QR-009 Testability`: Critical authorization, provenance, retrieval, refusal, retry, deletion, and export paths require automated coverage.

## MVP non-goals

- Shared workspaces or collaboration
- Native iOS application
- Manual tags
- Editing source-derived content or generated answers
- Searching prior conversations outside the current conversation
- Final billing implementation before commercial approval
- Training custom foundation models
- Provider-specific business logic

## Product acceptance boundary

The MVP is product-complete when an authenticated Android or web user can capture supported content, observe reliable processing, ask a grounded question across multiple source types, inspect each citation, receive a refusal when evidence is insufficient, export their data, and delete it under the documented retention policy without crossing another user's data boundary.
