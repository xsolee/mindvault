# Security and Privacy Architecture

Status: Proposed for approval; legal review required before production

This document is engineering guidance, not legal advice.

## Security model

- Deny by default and authorize by `account_id` at HTTP, application, repository, worker, storage, retrieval, citation, export and deletion boundaries.
- TLS in transit; provider-managed encryption or encrypted volumes at rest; sensitive mobile data in device-private storage.
- Least-privilege identities for API, worker, database, storage and CI. Secrets come from a secret manager or runtime environment and are rotatable.
- Private object buckets, opaque keys and short-lived scoped URLs issued only after authorization.
- Structured logs exclude source text, prompts, answers, credentials, tokens and signed URLs by default.
- Security events and administrative operations use an append-only audit trail with retention approved before launch.

## Threat controls

| Threat | Controls |
| --- | --- |
| Cross-user access | Owner-scoped repositories, RLS defense in depth, non-enumerable IDs, worker rechecks, adversarial two-user tests |
| Session theft | Short access lifetime, rotating refresh sessions, hashed server storage, secure cookies/Secure Store, revocation |
| CSRF/CORS | SameSite cookies, CSRF token for unsafe web requests, explicit origins, no wildcard credentials |
| Unsafe uploads | Signature validation, limits, constrained parsing, malware scan, no executable rendering |
| Zip/parser bombs | Expansion, recursion, time, memory and output caps |
| Prompt injection | Treat sources as delimited evidence, no generator tools/secrets, structured output and claim validation |
| Signed URL leakage | Short TTL, owner check, content disposition, private bucket, no URL logging |
| Deletion races | Synchronous tombstone, authorization recheck, job cancellation/neutralization, asynchronous purge |
| Provider compromise | Minimal disclosed data, processor agreements, retention/training controls, regional review and replaceable adapters |
| Abuse/cost exhaustion | Rate limits, quotas, transactional reservations, file/duration limits and spend alerts |

## Philippine privacy baseline

MindVault expects to act as a Personal Information Controller and its managed providers as Personal Information Processors where applicable. Before production:

- Conduct and approve a privacy impact assessment covering data inventory, flows, purposes, lawful basis, proportionality, subprocessors, cross-border transfer and risks.
- Publish a privacy notice covering purposes, methods, recipients, controller/DPO contact, retention and user rights.
- Support access, portability/export, objection where applicable, erasure/blocking, correction through new source/reprocessing where immutable-derived design applies, and complaint handling.
- Execute processor/data-processing agreements and review international-transfer safeguards.
- Designate accountable privacy/security roles and assess NPC registration/reporting obligations.
- Maintain an incident register and a breach-response playbook capable of the applicable 72-hour notification workflow.

The National Privacy Commission describes access, erasure/blocking and data portability as data-subject rights, requires PIAs for personal-data processing projects, and states that qualifying breaches require notification within 72 hours. See [NPC data-subject rights](https://privacy.gov.ph/data-subject-rights/), [third-party/PIA guidance](https://privacy.gov.ph/third-parties/), and [breach procedures](https://privacy.gov.ph/exercising-breach-reporting-procedures/).

## Retention proposal

| Data | Active retention | Deletion behavior |
| --- | --- | --- |
| Original/derived source | Until user deletes | Immediate retrieval exclusion; active purge target 24 hours |
| Generated answers/conversations | Until account erasure; source-derived quotations are redacted when that source is deleted | Redaction target 24 hours |
| Export artifact | 24 hours after ready | Object removed; request metadata retained without content for 30 days |
| Failed/incomplete uploads | 24 hours | Automatic purge |
| Security/audit metadata | 12 months, content-free | Scheduled purge |
| Encrypted backups | Rolling 30 days | Expire no later than day 30 |

Proposed production privacy capability: account erasure through an authorized support/administrative request, even though self-service account deletion is not an MVP UI requirement. It would immediately revoke all sessions, tombstone the account and every owned resource, then run the exhaustive source, conversation, export and identity purge workflows. Only legally/security-required content-free records would remain for their approved retention. This capability and retention basis require product-owner and privacy/legal approval before production; a self-service surface remains a separate product decision.

## Deletion-safe backup restore

Maintain a minimal append-only deletion ledger in a separately protected recovery store with account/source opaque IDs, deletion timestamp and purge scope, but no source content. Its retention exceeds the maximum backup age. Restore procedure is:

1. Restore database and object manifests into an isolated environment with public/API access disabled.
2. Replay all deletion-ledger entries newer than the restored snapshot and tombstone matching data.
3. Run purge and integrity checks across database, object storage, search/vector indexes and exports.
4. Verify no expired deletion can resolve through retrieval, citation or signed URL.
5. Only then enable service access.

The ledger is replicated and backed up independently. Quarterly drills include restoration from a snapshot taken before a deletion and prove non-resurrection.

## Required reviews

Independent security testing, dependency/container scanning, privacy/legal review, restore drill and incident tabletop are production gates.
