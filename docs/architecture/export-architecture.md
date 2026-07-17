# Export Architecture

Status: Proposed for approval

## Contract

An authenticated user requests an asynchronous account export. The API records a repeatable snapshot boundary and returns `202` with an export status resource. Only resources owned by the requesting account and active at the snapshot boundary are included.

The ZIP contains:

```text
manifest.json
sources/<source-id>/metadata.json
sources/<source-id>/original/<safe-original-name>
sources/<source-id>/transcript.json
sources/<source-id>/transcript.txt
sources/<source-id>/note.txt
sources/<source-id>/extracted.json
sources/<source-id>/normalized-english.json
conversations/conversations.json
answers/answers.json
```

Files appear only when applicable. Originals, transcripts, notes, conversations, answers, citations and machine-readable metadata are included. Embedding vectors, password/session data, internal provider credentials, job payloads and security logs are excluded.

## Manifest

`manifest.json` is UTF-8 JSON with schema version, export ID, account ID alias, snapshot time, generated time, application version, included resource counts, exclusions, and an entry for every file containing path, media type, byte size and SHA-256 checksum. JSON schemas and timestamp/encoding conventions are versioned and documented.

Filenames are generated from opaque IDs plus sanitized display names; traversal, reserved names and collisions are prevented. The archive builder enforces size, path and compression-ratio limits.

## Consistency and races

- Export reads a repeatable database snapshot and records source/version/object IDs before archive construction.
- Queued/processing sources are listed in the manifest with status but include only durable artifacts available at the snapshot.
- Failed sources include original content plus safe failure metadata when the original is durable.
- Sources deleted before the snapshot are excluded.
- A deletion after the snapshot cancels an unfinished export containing that source and removes any partial/final artifact; the user may request a fresh export.
- Account erasure cancels every export immediately.
- Export generation is idempotent by export ID and never follows mutable display filenames as storage keys.

## Delivery and retention

The completed artifact is stored privately for 24 hours. Download requires current account authorization and a short-lived, single-purpose signed URL. The ZIP is encrypted at rest by the object store; optional user-held archive encryption is deferred. Artifact expiry deletes the object; content-free request/audit metadata follows the retention schedule.

## Verification

Tests validate every required content type, manifest schema, checksums, UTF-8 Filipino/English text, filename attacks, snapshot consistency, authorization, URL expiry, large archives, failed/in-flight sources, and delete/export races. A round-trip verifier extracts the ZIP in a sandbox and confirms manifest completeness and checksums.
