# Cost Model and Plan Proposal

Status: Preliminary; revalidate prices before implementation

## Fixed managed baseline

Current public starting prices include Vercel Pro at USD 20/month and Supabase Pro at USD 25/month. Render API and worker compute, email, monitoring, Android store fees and AI usage are additional. See [Vercel pricing](https://vercel.com/pricing) and [Supabase pricing](https://supabase.com/pricing).

The managed launch should budget approximately USD 75-150/month before meaningful AI usage, depending on API/worker sizing and observability. This is an estimate, not a provider quote.

## Variable-cost drivers

1. Audio transcription minutes
2. Answer and normalization input/output tokens
3. Reranking/grounding calls
4. Stored audio/documents and egress
5. Embedding tokens, usually small relative to transcription/generation

For reference, OpenAI currently lists `text-embedding-3-small` at USD 0.02 per million input tokens and `text-embedding-3-large` at USD 0.13 per million. Model catalog and prices change, so adapters and configuration must not encode these names in domain logic. See [OpenAI embedding models](https://developers.openai.com/api/docs/models/text-embedding-3-small) and [model catalog](https://developers.openai.com/api/docs/models).

## Metering units

- accepted audio seconds
- original stored bytes and derived bytes
- extracted input characters/pages for reporting
- embedding input tokens
- generation/normalization/rerank input and output tokens
- successful questions and provider calls

Use an immutable ledger with reserve, commit and release entries. Plans configure hard/soft limits; billing remains separate.

## Initial commercial proposal

Target at least 70% gross margin after AI, storage, egress and variable compute; exclude payment fees and fixed development cost from per-operation estimates but include them in business planning.

| Plan | Price proposal | Monthly allowances proposal |
| --- | --- | --- |
| Free Trial | 7 days, no card | 30 audio minutes, 100 MB storage, 20 questions |
| Starter | USD 9.99 | 180 audio minutes, 2 GB storage, 200 questions |
| Pro | USD 19.99 | 600 audio minutes, 10 GB storage, 750 questions |

Do not promise document pages as the primary hard limit; byte size and processing/token usage are more enforceable. Apply fair-use and abuse controls. Before approval, run provider-specific calculations for typical/light/heavy users plus a beta measurement period. If modeled variable cost exceeds 30% of price, reduce allowances, choose a cheaper validated provider/model, or raise price.

## Cost controls

- Per-plan reservations before expensive work and reconciliation after completion.
- Provider timeouts, token caps, bounded evidence bundles and output limits.
- Organization/provider spend alerts and hard caps where supported.
- Cache only safe deterministic derived work keyed by content and model version.
- Track contribution margin by anonymized usage cohort, not by storing content in analytics.
