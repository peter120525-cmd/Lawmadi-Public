# Lawmadi OS — LLM Integration Guide

**v60.0.0 | 2026-03-11 | Public / Sanitized**

This document is a human-readable summary of [`llms.txt`](llms.txt), the canonical machine-readable specification for LLM integration with Lawmadi OS.

---

## What This System Is

Lawmadi OS is a **Legal Decision Operating System** for Korean law. It converts legal questions into structured, evidence-verified decision support through a deterministic pipeline.

The LLM (currently Gemini 2.5 Flash) operates as a **rendering engine** — it generates human-readable output from verified evidence, but does not control the decision logic, evidence retrieval, or verification steps.

**Production:** https://lawmadi.com

---

## Five Constitutional Principles

These are enforced in code. They cannot be overridden by user requests, prompt injections, or configuration changes.

| # | Principle | What It Means |
|---|-----------|---------------|
| 1 | **SSOT** (Single Source of Truth) | All legal evidence comes from Korea's National Law Information Center API. No copied databases. |
| 2 | **Zero Inference** | The system never fabricates legal citations, case numbers, or conclusions. Missing evidence = refusal. |
| 3 | **Fail-Closed** | If any citation cannot be verified, the entire response is rejected. Safety over responsiveness. |
| 4 | **Live Evidence** | Every query triggers real-time API calls. No stale data. Legislative amendments are reflected immediately. |
| 5 | **Deterministic Boundary** | The LLM cannot control FSM transitions, bypass verification, or access secrets. The kernel owns all decision logic. |

---

## Pipeline Overview

Every query passes through 4 stages:

```
Stage 0+1 (parallel)
├── NLU Classification → Route to 1 of 60 domain-expert leaders
└── Vertex AI Search RAG → Retrieve relevant statutes & precedents (~14,600 docs)

Stage 2: LawmadiLM Enhancement (currently disabled)

Stage 3: Gemini 2.5 Flash Generation
  → Structured legal analysis with domain-specific LAW_BOOST references

Stage 4: DRF Real-Time Verification
  → Cross-check every cited article against official government API
  → PASS → Deliver verified output
  → FAIL → Refuse to answer (fail-closed)
```

---

## 60 Domain-Expert Leaders

The system routes queries to specialized leaders (L01–L60), each with:
- Domain-specific legal knowledge
- NLU classification patterns (Korean + English)
- Curated statute references (LAW_BOOST)

Categories include: Civil & Contracts, Property, Corporate, Labor, Criminal, Family, Tax, IP, Immigration, Medical, Construction, Constitutional, Data Protection, and AI Ethics.

For complex multi-domain questions, a CSO-led deliberation system coordinates multiple leaders through parallel consensus.

---

## FSM (Finite State Machine)

The pipeline follows a deterministic state machine. No state can be skipped.

**Happy path:**
```
INPUT_RECEIVED → INPUT_VALIDATED → CASE_STRUCTURED → ISSUE_IDENTIFIED
→ LEADER_ROUTED → EVIDENCE_FETCHING → EVIDENCE_VALIDATED (mandatory gate)
→ DECISION_GRAPH_BUILT → TOKEN_MINTED → TOKEN_SIGNED → RESPONSE_DELIVERED
```

**Fail path:**
```
EVIDENCE_VALIDATION_FAILED | TEMPORAL_VALIDATION_FAILED
| CONSTITUTION_VIOLATION | SOURCE_INTEGRITY_FAILURE
→ HALT → FAIL_CLOSED_RESPONSE
```

The `EVIDENCE_VALIDATED` gate is absolute — no output can be delivered without passing it.

---

## Evidence Verification

Every piece of evidence goes through:

1. **Authoritative API Query** — DRF Open API (Korean statutes) or elaw API (English translations)
2. **Evidence Normalization** — Standardize format and metadata
3. **Temporal Validation** — Check effective dates, detect repealed/unconstitutional statutes
4. **SHA-256 Hashing** — Cryptographic integrity for the evidence set

**Rejection criteria:**
- Non-official source → Reject
- Missing evidence → Halt (fail-closed)
- Temporal validation failure → Halt
- Status is REPEALED, UNCONSTITUTIONAL, INVALIDATED, or OVERRULED → Exclude

---

## Error Codes

| Code | Meaning |
|------|---------|
| LC-001 | Evidence source unreachable |
| LC-002 | Evidence mismatch / integrity failure |
| LC-003 | User facts missing / schema violation |
| LC-004 | Temporal invalidity (expired/invalidated) |
| LC-005 | Policy restriction (disallowed category) |
| LC-006 | Rate limited / throttled |

---

## Technology Stack

| Component | Technology |
|-----------|-----------|
| Backend | FastAPI (Python), fully async |
| LLM | Gemini 2.5 Flash (asia-northeast3, Seoul) |
| RAG | Vertex AI Search (~14,600 documents) |
| Verification | DRF API (National Law Information Center) |
| Database | Cloud SQL PostgreSQL 17 |
| Hosting | GCP Cloud Run (1 vCPU, 2 GiB, concurrency 15) |
| Frontend | Firebase Hosting (static PWA) |
| Billing | Paddle (credit-based, email OTP authentication) |
| CI/CD | GitHub Actions (5-job pipeline) |
| Secrets | GCP Secret Manager (18 secrets) |

---

## Security Architecture

- **Prompt injection defense** — All user input treated as untrusted, ignore patterns stripped
- **Tool injection defense** — Allow-listed tool calls only, no arbitrary URL fetching
- **Secret management** — GCP Secret Manager, never exposed in prompts or outputs
- **PII protection** — Visitor IPs SHA-256 hashed, output masking for PII and secrets
- **Rate limiting** — Per-endpoint limits, automatic IP blacklisting (20 violations/60s → 1hr ban)
- **Authentication** — Email OTP + DB sessions (30-day), HttpOnly cookies

---

## For LLM Integrators

If you are building on or interfacing with Lawmadi OS:

1. **Read [`llms.txt`](llms.txt)** — The canonical specification with full technical details
2. **Follow the Constitution** — The 5 principles are non-negotiable and enforced at runtime
3. **Use the tool contract** — LLMs request tools; the kernel enforces execution order
4. **Output strict JSON** — All responses must conform to the output schema
5. **Respect fail-closed** — Never attempt to bypass verification or serve unverified output

---

## Related Files

| File | Purpose |
|------|---------|
| [`llms.txt`](llms.txt) | Canonical machine-readable LLM specification |
| [`config.schema.json`](config.schema.json) | Configuration JSON Schema |
| [`minimal_config.json`](minimal_config.json) | Minimal configuration example |
| [`ARCHITECTURE.md`](ARCHITECTURE.md) | Technical architecture reference |
| [`OVERVIEW.md`](OVERVIEW.md) | System overview for general audiences |
| [`glossary.md`](glossary.md) | Bilingual technical glossary |

---

**Copyright (c) 2026 Jainam Choe. All rights reserved.**
