# Quality Attributes and Requirement Traceability

Status: Proposed for approval

## Requirement mapping

| Requirements | Architecture capability | Primary verification |
| --- | --- | --- |
| FR-001, FR-002, FR-003, QR-001 | Identity/session model; owner-scoped repositories; RLS defense | Two-user adversarial authorization suite |
| FR-010, FR-011, FR-012, FR-013, FR-014, QR-005 | Android foreground recording; encrypted durable outbox; idempotent upload | Physical-device lock/offline/process-death matrix |
| FR-020, FR-021, FR-022, FR-023, FR-024, QR-004 | Common source/upload workflow; staged durable jobs; immutable originals | Format, corruption, retry, duplicate and reconciliation tests |
| FR-030, FR-031, FR-032, QR-003 | Original + aligned English-normalized representations | English/Filipino/code-switch provenance corpus |
| FR-040, FR-041, FR-042, FR-043, FR-044, FR-045, FR-046 | Hybrid retrieval; evidence bundle; claim validation; refusal | Golden retrieval/citation/no-answer evaluation |
| FR-050, FR-051, FR-052, FR-053, QR-008 | Tombstone/purge, 30-day backups and async exports | Deletion races, export completeness and restore drills |
| FR-060, FR-061, FR-062 | Configurable entitlement ledger separate from billing | Boundary, concurrency and retry accounting tests |
| QR-002 | PIA, data-flow inventory, retention, rights and incident plan | Privacy/legal production review |
| QR-006 | WCAG 2.2 AA and mobile equivalent | Automated + manual + TalkBack/keyboard testing |
| QR-007 | Provider ports, Docker/managed profiles and conformance tests | Adapter contract tests and Compose recovery tests |
| QR-009 | Layered automated suite and deterministic fixtures | CI/release evidence report |

## Architecture fitness checks

- No provider SDK types in domain/application interfaces.
- No owned query without `account_id` scope.
- Every citation resolves through the provenance invariant.
- Every asynchronous stage has an idempotency key, retry class and reconciliation path.
- No durable data exists only in a container filesystem.
- OpenAPI generation and TypeScript-client drift are checked in CI.
- Database schema changes are migration-tested forward and backward where safe.
- Provider adapters pass common conformance suites.

## Critical scenarios

1. Duplicate upload/job delivery converges on one source and one active derived version.
2. Crash after object storage but before enqueue is repaired by reconciliation.
3. Provider timeout retries without double quota consumption.
4. Cross-user planted matches never enter candidates, prompts, citations or logs.
5. Prompt injection in a source remains inert evidence.
6. Deletion racing a job/query immediately prevents new disclosure.
7. Normalized-language retrieval cites exact original evidence.
8. Conflicting evidence is cited explicitly or refused.
9. Compose restart preserves data and recovers leased jobs.
10. Restore proves RPO/RTO while backup data expires by day 30.

## Test layers

- Domain and state-machine unit tests
- PostgreSQL, object-store and worker integration tests
- Provider contract tests with recorded/redacted fixtures
- Retrieval evaluation corpus and regression thresholds
- Web and Android component/integration tests
- Browser, emulator and physical-device E2E
- Isolation, upload security, prompt-injection and dependency/container scans
- Backup restore and incident-response exercises

## Architecture approval checklist

- [ ] Proposed ADRs accepted or revised
- [ ] Evidence metrics and refusal policy accepted
- [ ] WCAG 2.2 AA/mobile target accepted
- [ ] RPO 24 hours and RTO 8 hours accepted
- [ ] Managed provider shortlist and Singapore data flow accepted
- [ ] Malware scanning and scanned-PDF OCR exclusion accepted
- [ ] Initial plan prices/allowances and 70% margin target accepted or deferred explicitly
- [ ] Privacy/legal review acknowledged as a production gate
- [ ] Proposed administrative account-erasure workflow and retention schedule accepted or revised
