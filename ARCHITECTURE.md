# Lawmadi OS — Architecture Reference (Public / Sanitized)

**Version 2.0-Unified** · **2026-02-08**
**Copyright © 2026 Jainam Choe (최재남). All rights reserved.**

> *"Convert Anxiety into Actionable Logic."*
> *"불안을 실행 가능한 논리로 전환하다"*

This document provides a public, sanitized architectural overview of **Lawmadi OS** — a deterministic, FSM-based **Legal Decision Operating System (LDOS)**. Proprietary scoring formulas, routing weights, deployment configurations, and operational secrets are intentionally excluded.

For the complete LLM integration specification, see [`llms.txt`](llms.txt).
For licensing terms, see [`LICENSE.txt`](LICENSE.txt).

---

## Table of Contents

1. [System Identity](#1-system-identity)
2. [Foundational Operating Constitution](#2-foundational-operating-constitution)
3. [Platform Layer Architecture](#3-platform-layer-architecture)
4. [Runtime State Machine (FSM)](#4-runtime-state-machine-fsm)
5. [Core Kernel Engines](#5-core-kernel-engines)
6. [Decision Graph Formal Semantics](#6-decision-graph-formal-semantics)
7. [Evidence Pipeline & Trust Scoring](#7-evidence-pipeline--trust-scoring)
8. [Cryptographic Integrity & Reproducibility](#8-cryptographic-integrity--reproducibility)
9. [Security Architecture](#9-security-architecture)
10. [Data Governance](#10-data-governance)
11. [Output Contract](#11-output-contract)
12. [LLM Integration Architecture](#12-llm-integration-architecture)
13. [Concurrency & Scalability](#13-concurrency--scalability)
14. [Infrastructure Topology](#14-infrastructure-topology)
15. [Global Multi-Jurisdiction Design](#15-global-multi-jurisdiction-design)
16. [Non-Public Assets](#16-non-public-assets)
17. [Document Cross-References](#17-document-cross-references)

---

## 1. System Identity

Lawmadi OS is **not** a chatbot. **Not** a search engine. **Not** a legal database.

It is a **Decision Intelligence Infrastructure** — an engineering system that generates **reproducible, verifiable legal decision outputs** by assembling and validating **live evidence** from authoritative sources.

```
┌─────────────────────────────────────────────────────────────┐
│                      LAWMADI OS                             │
│          Legal Decision Operating System (LDOS)             │
│                                                             │
│   "Decision Infrastructure, not a chatbot."                 │
│                                                             │
│   ┌─────────────┐  ┌──────────────┐  ┌─────────────────┐   │
│   │ Deterministic│  │ Live Evidence│  │ Cryptographic   │   │
│   │ FSM Runtime  │  │ Architecture │  │ Trust Chain     │   │
│   └─────────────┘  └──────────────┘  └─────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

### Strategic Service Hierarchy

| Priority | Service | Role |
|----------|---------|------|
| **P1** | Legal Decision OS | Foundation engine — basis for all downstream services |
| **P2** | Evidence Verification Engine | Trust layer via authoritative-source validation |
| **P3** | Consultation AI | User-facing conversational interface |
| **P4** | Education Platform | Automated case study & decision logic visualization |

**OS → Engine → Service → Platform**

---

## 2. Foundational Operating Constitution

Five **non-negotiable** principles govern every architectural and business decision. These are not guidelines — they are **inviolable constitutional rules** enforced at runtime.

```
┌──────────────────────────────────────────────────────────────────┐
│                   OPERATING CONSTITUTION                         │
│                                                                  │
│  ┌──────┐   ┌────────────┐   ┌────────────┐   ┌──────────────┐  │
│  │ SSOT │──>│ Zero       │──>│ Fail-      │──>│ Live         │  │
│  │      │   │ Inference  │   │ Closed     │   │ Evidence     │  │
│  └──────┘   └────────────┘   └────────────┘   └──────────────┘  │
│                        │                                         │
│               ┌────────────────────┐                             │
│               │ Deterministic      │                             │
│               │ Runtime Boundary   │                             │
│               └────────────────────┘                             │
└──────────────────────────────────────────────────────────────────┘
```

### 2.1 SSOT — Single Source of Truth

All legal evidence from **authoritative official APIs only**. Permanent storage or replication of statute/precedent/regulation datasets is **prohibited**.

### 2.2 Zero Inference

**Never** fabricate, guess, or hallucinate legal facts, citations, case numbers, dates, parties, or conclusions. If evidence is missing — ask or refuse.

### 2.3 Fail-Closed

If any verification fails → **halt immediately**. Return a structured refusal. Never output unverified legal conclusions. **Safety over responsiveness.**

### 2.4 Live Evidence

Decisions from **real-time validated evidence** only. Legislative amendments, appellate reversals, and new precedents reflected immediately.

### 2.5 Deterministic Runtime Boundary

LLM = **rendering engine** under strict Kernel control. The Kernel owns: state transitions, evidence retrieval/validation, token generation, policy enforcement.

### 2.6 Constitution DSL

The constitution is enforced via executable DSL rules at runtime:

```
RULE Enforce_Source_Integrity
  IF evidence.source_origin != OFFICIAL_API
  THEN reject_decision

RULE Validate_Effective_Date
  IF evidence.effective_date > current_timestamp
  THEN exclude_evidence

RULE Enforce_Decision_Completeness
  FOR_EACH issue_node IN decision_graph
    IF NOT EXISTS (law_node SUPPORTS issue_node)
    OR NOT EXISTS (evidence_node SUPPORTS issue_node)
    THEN reject_decision

RULE Enforce_Crypto_Integrity
  IF decision_token.digital_signature == MISSING OR INVALID
  THEN reject_delivery
```

> **Note:** The above are illustrative examples. The full rule set, priorities, and exception handling are proprietary and confidential.

---

## 3. Platform Layer Architecture

```
┌───────────────────────────────────────────────────────────────────┐
│                                                                   │
│   ┌───────────────────────────────────────────────────────────┐   │
│   │                  PARTNER / B2B LAYER                      │   │
│   │  Decision Verification API · Evidence Validation API      │   │
│   │  Case Structuring API · Rate Limit · IAM · Audit          │   │
│   └───────────────────────────┬───────────────────────────────┘   │
│                               │                                   │
│   ┌───────────────────────────┴───────────────────────────────┐   │
│   │                    SERVICE LAYER                          │   │
│   │  Consultation AI · Friendly Secretary UX                  │   │
│   │  Case Exploration · Contextual Conversation               │   │
│   │  *** No access to Core internal logic ***                 │   │
│   └───────────────────────────┬───────────────────────────────┘   │
│                               │                                   │
│   ┌───────────────────────────┴───────────────────────────────┐   │
│   │                     CORE LAYER                            │   │
│   │              (Closed Proprietary Kernel)                  │   │
│   │                                                           │   │
│   │  Decision OS Kernel · Evidence Verification Engine        │   │
│   │  Leader Swarm Routing · Constitution Validator            │   │
│   │  Temporal Law Validity · Decision Graph Generator         │   │
│   │                                                           │   │
│   │  Security: Zero Trust · Crypto Integrity · Tamper-Evident │   │
│   └───────────────────────────────────────────────────────────┘   │
│                                                                   │
└───────────────────────────────────────────────────────────────────┘
```

### 3.1 Core Layer — Closed Kernel Engine

The intellectual property and constitutional logic. **Absolute proprietary closed engine.**

| Component | Function |
|-----------|----------|
| **Decision OS Kernel** | Core decision logic, case structuring, FSM runtime management |
| **Evidence Verification Engine** | Authoritative-source evidence fetch, validation, integrity checks |
| **Leader Swarm Routing Engine** | Specialist legal domain expert routing & orchestration |
| **Constitution Validator** | DSL-based policy compliance enforcement |
| **Temporal Law Validity Engine** | Effective date verification, precedent change detection, void clause identification |
| **Decision Graph Generator** | Formal semantic graph construction & visualization |

### 3.2 Service Layer — User Experience

Consultation AI, Friendly Secretary UX, case exploration assistant. **No access** to Core internal logic — communicates only through defined interfaces.

### 3.3 Partner / B2B Layer — Institutional Services

For law firms, corporations, insurers, government agencies. Provides:
- Decision Verification API
- Evidence Validation API
- Case Structuring API

All under access control, logging, and rate limiting.

---

## 4. Runtime State Machine (FSM)

Every decision session follows a **deterministic, sequential** state machine. No state may be skipped. The Kernel controls all transitions.

### 4.1 Happy Path

```
INPUT_RECEIVED
  │
  ▼
INPUT_VALIDATED
  │
  ▼
CASE_STRUCTURED ──────────── CaseStructure object created
  │
  ▼
ISSUE_IDENTIFIED ─────────── IssueGraph extracted
  │
  ▼
LEADER_ROUTED ────────────── Domain expert(s) selected
  │
  ▼
EVIDENCE_FETCHING ────────── Authoritative API queries
  │
  ▼
EVIDENCE_VALIDATED ───────── *** MANDATORY GATE ***
  │                           No output without passing this state.
  ▼
DECISION_GRAPH_BUILT ─────── Formal semantic graph constructed
  │
  ▼
TOKEN_MINTED ─────────────── Decision Token with hashes
  │
  ▼
TOKEN_SIGNED ─────────────── Ed25519 signature (KMS/HSM)
  │
  ▼
RESPONSE_DELIVERED ───────── Strict JSON output to user
```

### 4.2 Fail-Closed Path

```
Any verification failure at any state:
  EVIDENCE_VALIDATION_FAILED
  TEMPORAL_VALIDATION_FAILED
  CONSTITUTION_VIOLATION
  SOURCE_INTEGRITY_FAILURE
      │
      ▼
    HALT
      │
      ▼
  FAIL_CLOSED_RESPONSE ──── Error code + reason + required inputs
```

### 4.3 Critical FSM Rules

- Every session follows the **exact** state sequence — no shortcuts.
- `EVIDENCE_VALIDATED` is an **absolute mandatory gate**.
- LLM does not control state transitions; the **Kernel** does.
- If the LLM model lacks function calling, the Kernel performs all tools externally and provides results for rendering only.

---

## 5. Core Kernel Engines

### 5.1 Case Structure Parser

Converts natural language input into a structured case object:

```
CaseStructure {
  case_id               // Unique case identifier
  case_type             // Case type classification
  parties               // Parties information
  timeline              // Chronological sequence
  claim_object          // Claim target
  fact_vector           // Facts vector
}
```

### 5.2 Issue Extraction Engine

Extracts legal issues and constructs a dependency graph:

```
IssueGraph {
  issue_nodes[]         // Legal issue nodes
  dependency_edges[]    // Inter-issue dependency edges
}
```

### 5.3 Leader Swarm Routing Engine

Routes cases to specialist legal domain experts based on a multi-factor scoring function.

```
                    ┌─────────────┐
                    │   Incoming   │
                    │    Case      │
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │   Routing    │
                    │   Score      │
                    │  Calculation │
                    └──────┬──────┘
                           │
              ┌────────────┼────────────┐
              │            │            │
        ┌─────▼────┐ ┌────▼─────┐ ┌────▼─────┐
        │ Leader A  │ │ Leader B │ │ Leader C │
        │(Primary)  │ │(Secondary│ │(Fallback)│
        └─────┬────┘ └────┬─────┘ └────┬─────┘
              │            │            │
              └────────────┼────────────┘
                           │
                    ┌──────▼──────┐
                    │  Multi-Leader│
                    │  Consensus   │
                    └─────────────┘
```

**Consensus mechanisms:**
- **Weighted Confidence Voting** — aggregate judgments by confidence weights
- **Decision Graph Merge** — unify graphs from multiple leaders
- **Fallback Leader Escalation** — auto-escalate on primary failure

**Leader Profile Schema:**

```
LeaderProfile {
  leader_id                     // Unique leader ID
  specialization_domain         // Legal domain specialization
  capability_tags               // Capability tags
  routing_weight                // Routing weight
  trust_score                   // Trust score
  supported_constitution_ver    // Supported constitution versions
  dependency_modules            // Dependency modules
}
```

> **Note:** Specific scoring formulas and routing weights are proprietary and confidential.

### 5.4 Temporal Law Validity Engine

Beyond simple statute lookup — dedicated temporal validation:

- **Statute effective date verification:** Is it currently in force?
- **Precedent change detection:** Appellate reversal, superior court changes
- **Unconstitutional / void clause detection:** Constitutional court rulings
- **"As-of" time validation:** Current time or user-specified date
- **Unknown temporal status:** → Fail-Closed or Reference-Only mode

---

## 6. Decision Graph Formal Semantics

Legal decisions are represented as a **directed graph with formal semantics**.

### 6.1 Node Typology

```
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│  FACT_NODE   │    │  ISSUE_NODE  │    │   LAW_NODE   │
│ (objective   │    │ (legal issue │    │ (statute     │
│  facts)      │    │  to resolve) │    │  provision)  │
└──────────────┘    └──────────────┘    └──────────────┘

┌──────────────┐    ┌──────────────┐
│ PRECEDENT_   │    │ DECISION_    │
│ NODE         │    │ NODE         │
│ (judicial    │    │ (final       │
│  precedent)  │    │  output)     │
└──────────────┘    └──────────────┘
```

### 6.2 Edge Semantics

| Edge Type | Meaning |
|-----------|---------|
| `SUPPORTS` | Provides grounds / backing |
| `CONTRADICTS` | Conflicts with target |
| `DEPENDS_ON` | Prerequisite dependency |
| `RESOLVES` | Issue resolution link |
| `REFERENCES` | Reference link |
| `APPLIES` | Statute applies to facts |
| `OVERRULES` | Higher precedent overrules lower |
| `TEMPORAL_DEPENDS` | Depends on effective date / amendment |

### 6.3 Graph Validity Condition (Mandatory)

```
∀ ISSUE_NODE:
  ∃ at least one LAW_NODE       that SUPPORTS it
  AND
  ∃ at least one EVIDENCE_NODE  that SUPPORTS it
```

If this condition is not met → **reject_decision**.

### 6.4 Example Decision Graph Structure

```
  FACT_NODE ─── SUPPORTS ───> ISSUE_NODE
                                  │
                    ┌─────────────┼──────────────┐
                    │             │              │
              DEPENDS_ON     SUPPORTS        SUPPORTS
                    │             │              │
              ISSUE_NODE     LAW_NODE     PRECEDENT_NODE
                                  │              │
                                  └──── SUPPORTS ┘
                                          │
                                    DECISION_NODE
```

---

## 7. Evidence Pipeline & Trust Scoring

### 7.1 Evidence Processing Pipeline

```
┌─────────────────────┐
│  Authoritative API   │    (e.g., DRF Open API)
│  Query               │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Evidence            │    Normalize format, structure,
│  Normalization       │    and metadata
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Temporal            │    Effective date, repeal status,
│  Validation          │    constitutional validity
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Evidence            │    SHA-256 canonical hash
│  Hashing             │    (sort_keys, stable separators)
└──────────┬──────────┘
           │
           ▼
     evidence_set           Ready for decision graph
```

### 7.2 Evidence Trust Score (Conceptual)

Three components contribute to evidence trustworthiness:

```
EvidenceTrustScore =
    source_authority_weight         // Source authority
  + citation_stability_score        // Citation stability
  + temporal_consistency_score      // Temporal consistency
```

> **Note:** Specific weights and formulas are proprietary and confidential.

### 7.3 Evidence Integrity Rules

- **REJECT** if `source_origin != OFFICIAL_API`
- **REJECT** if `missing == true`
- **REJECT** if temporal validation fails
- **REJECT** if status is `REPEALED`, `UNCONSTITUTIONAL`, or `INVALIDATED`

### 7.4 Provenance Lineage Tracking

Full audit trail of evidence creation, modification, and validation history is maintained.

---

## 8. Cryptographic Integrity & Reproducibility

### 8.1 Reproducibility Trust Chain

**Core guarantee:** Same Input + Same Evidence State → Same Token.

```
Input Hash (SHA-256)
    │
    ▼
Evidence Hash Set (SHA-256 per item, aggregated)
    │
    ▼
Decision Graph Hash (SHA-256)
    │
    ▼
Decision Token Signature (Ed25519)
```

### 8.2 Decision Token Standard

```
DecisionToken {
  decision_id               // Unique decision identifier
  created_at                // ISO-8601 timestamp
  input_hash                // SHA-256 of input query
  constitution_version      // Applied constitution version
  drf_evidence_hash         // SHA-256 of all evidence used
  decision_graph_hash       // Hash of the decision graph
  decision_graph_summary    // Compressed decision path
  digital_signature         // Ed25519 (KMS/HSM in production; PLACEHOLDER in public)
}
```

### 8.3 Integrity Mechanisms

| Mechanism | Purpose |
|-----------|---------|
| **Ed25519 Digital Signature** | Decision output authenticity & non-repudiation |
| **SHA-256 Evidence Hashing** | Evidence integrity guarantee |
| **Deterministic Decision ID** | Reproducibility verification |

---

## 9. Security Architecture

### 9.1 Gateway Protections

```
┌──────────────────────────────────────────────┐
│                API GATEWAY                    │
│                                              │
│  Input Schema Validation (JSON Schema)       │
│  Authentication / Authorization (IAM)        │
│  Rate Limiting                               │
│  Full Audit Logging                          │
│  Output Masking (PII redaction)              │
└──────────────────────────────────────────────┘
```

### 9.2 Prompt Injection Defense

- User input treated as **untrusted** at all times
- "Ignore previous instructions" patterns stripped/neutralized
- Tool call allow-list: LLM requests, **Kernel validates**
- Arbitrary URL fetch prohibited unless Kernel provides vetted tool
- Secrets, PII, raw logs masked from output

### 9.3 Secret Management

- **Never** place API keys in prompts
- Keys only in KMS / Secret Manager / Vault
- Model requests for keys → **refuse + log as security event**
- Runtime config (public) separated from secure config (private)
- Key rotation and least-privilege IAM enforced

### 9.4 Signature Boundary

Signing keys are **never** inside the Kernel. They reside in external trust systems (KMS/HSM). Public builds use placeholder signatures to demonstrate the interface contract.

---

## 10. Data Governance

### 10.1 Allowed vs. Prohibited

| ✅ Allowed | ❌ Prohibited |
|-----------|--------------|
| Real-time authoritative API calls | Permanent storage of statutes/precedents |
| Redis ephemeral cache (TTL 10–30 min) | Replication of official legal datasets |
| In-memory session-scoped cache | "Precedent replication database" |
| Proprietary case decision pattern data | Aggregated law database warehousing |
| Provenance lineage metadata | Any local copy serving stale legal data |

### 10.2 Ephemeral Cache Policy

- Cache key: canonical `query_struct` hash
- Cache value: `evidence_set` + `evidence_hash` + `retrieved_at`
- **Must** revalidate temporal conditions if "as-of" time differs
- Cache is an **acceleration mechanism**, not a data store

### 10.3 DRF Resilience Strategy

| Mode | Behavior |
|------|----------|
| **Normal** | Real-time evidence retrieval + full decision output |
| **Degraded** | Reference-only response + degradation notice (if policy permits) |
| **Fail-Closed** | Complete refusal of decision output |

---

## 11. Output Contract

All outputs follow **strict JSON**. Two modes:

### 11.1 Success Response

```json
{
  "fail_closed": false,
  "request_id": "uuid",
  "fsm_state": "RESPONSE_DELIVERED",
  "decision_token": {
    "decision_id": "string",
    "created_at": "ISO-8601",
    "input_hash": "sha256",
    "drf_evidence_hash": "sha256",
    "decision_graph_hash": "sha256",
    "constitution_version": "string",
    "digital_signature": "string | PLACEHOLDER"
  },
  "summary": "plain-language summary",
  "known_facts": ["..."],
  "unknown_facts": ["..."],
  "evidence_citations": [
    {"ref": "OFFICIAL:ID", "type": "STATUTE", "note": "what it supports"}
  ],
  "decision_graph_summary": "compressed logic path",
  "next_actions": ["..."],
  "disclaimer": "..."
}
```

### 11.2 Fail-Closed Response

```json
{
  "fail_closed": true,
  "request_id": "uuid",
  "fsm_state": "HALT",
  "code": "LC-001",
  "message": "human-readable reason",
  "stage": "FSM state where failure occurred",
  "required_user_inputs": ["what would unblock"],
  "disclaimer": "..."
}
```

### 11.3 Standard Error Codes

| Code | Meaning | Action |
|------|---------|--------|
| `LC-001` | Evidence source unreachable | Retry or Fail-Closed |
| `LC-002` | Evidence mismatch / non-authoritative / integrity failure | Reject evidence |
| `LC-003` | Constitution violation / invalid schema | Reject decision |
| `LC-004` | Temporal invalidity (not effective / expired) | Exclude evidence |
| `LC-005` | Policy restriction (disallowed category) | Refuse with reason |
| `LC-006` | Rate limited / throttled | Retry after delay |

---

## 12. LLM Integration Architecture

Lawmadi OS is **model-agnostic**. Any LLM that follows structured instructions can be integrated.

### 12.1 Core Principle: LLM as Rendering Engine

```
┌──────────────────────────────────────────────────────────────┐
│                     KERNEL (Non-LLM Code)                    │
│                                                              │
│  Owns: FSM transitions, evidence fetch/validate,             │
│        token/hashes, policy enforcement, tool execution       │
│                                                              │
│  ┌──────────────────────────────────┐                        │
│  │         LLM (Rendering Engine)   │                        │
│  │                                  │                        │
│  │  Receives: case_struct,          │                        │
│  │            evidence_set,         │                        │
│  │            graph_summary,        │                        │
│  │            token_payload         │                        │
│  │                                  │                        │
│  │  Returns:  Formatted JSON only   │                        │
│  │                                  │                        │
│  │  Cannot: override tool outputs,  │                        │
│  │          skip EVIDENCE_VALIDATED, │                        │
│  │          access secrets           │                        │
│  └──────────────────────────────────┘                        │
└──────────────────────────────────────────────────────────────┘
```

### 12.2 Nine Required Integration Contracts

| Contract | Purpose |
|----------|---------|
| **A. Prompt Contract** | System / Developer / User prompt rules |
| **B. Tool Contract** | Function calling schema (7 tools) |
| **C. Evidence Contract** | Canonical `evidence_set` schema + hashing |
| **D. DecisionToken Contract** | Token schema |
| **E. Error Code Contract** | Fail-Closed codes (LC-001–006) |
| **F. Output Schema** | Strict JSON response format |
| **G. Evaluation Harness** | Unit / regression / load / red-team tests |
| **H. Security Controls** | Injection defense, secret management |
| **I. Observability** | Audit log, metrics, trace IDs |

### 12.3 Tool Contract (Recommended Tools)

```
fetch_evidence(query_struct)                → evidence_set
validate_evidence(evidence_set)             → {ok, code}
temporal_validate(evidence_set)             → {ok, code}
build_decision_graph(case_struct, evidence) → graph
mint_decision_token(case, evidence, graph)  → token
sign_token(token_payload)                   → signature
audit_log(event_type, payload)              → append-only record
```

**Strict policy:** LLM requests tools; **Kernel decides** tool order and validates arguments. Tool outputs are **ground truth** — LLM cannot override them.

### 12.4 Multi-LLM Portability

- Adapter layer maps: system prompt format, function calling schema, streaming behavior, token limits
- Model output **always validated** with JSON Schema; invalid outputs rejected
- Keep prompts short, explicit, and contract-first
- Avoid model-specific features unless behind adapters

### 12.5 Safe Streaming Policy

- **Do not** stream final conclusions before evidence validation
- Allowed: "working" status messages, clarifying questions
- Final decision output must be **atomic** (complete JSON)

---

## 13. Concurrency & Scalability

```
┌─────────────────────────────────────────────────┐
│              Concurrency Model                   │
│                                                  │
│  ┌─────────────────────────────────────────────┐ │
│  │  Parallel Leader Execution                  │ │
│  │  Multiple leaders run concurrently          │ │
│  └─────────────────────────────────────────────┘ │
│                                                  │
│  ┌─────────────────────────────────────────────┐ │
│  │  Async Evidence Query Queue                 │ │
│  │  Non-blocking authoritative API calls       │ │
│  └─────────────────────────────────────────────┘ │
│                                                  │
│  ┌─────────────────────────────────────────────┐ │
│  │  Circuit Breaker Protocol                   │ │
│  │  Prevent cascading failures                 │ │
│  └─────────────────────────────────────────────┘ │
│                                                  │
│  ┌─────────────────────────────────────────────┐ │
│  │  Timeout Retry Policy                       │ │
│  │  Configurable exponential backoff           │ │
│  └─────────────────────────────────────────────┘ │
│                                                  │
│  Guarantee: No state leakage between requests    │
└─────────────────────────────────────────────────┘
```

### Observability (Audit-First)

- `request_id`, `decision_id`, `input_hash` always logged
- FSM state transitions as append-only audit events
- Tool calls: name, arguments hash, result hash
- Fail-Closed events: code + stage
- Metrics: evidence fetch success rate, fail-closed rate, latency per state, cache hit rate

---

## 14. Infrastructure Topology

> **Note:** This is a conceptual overview. Operational endpoints, IaC configurations, and deployment secrets are excluded.

```
┌──────────────────────────────────────────────────────────────────┐
│                     INFRASTRUCTURE                               │
│                                                                  │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │  API Gateway                                               │  │
│  │  JSON Schema validation · IAM authz · Rate limiting        │  │
│  │  Full audit logging                                        │  │
│  └──────────────────────────┬─────────────────────────────────┘  │
│                             │                                    │
│  ┌──────────────────────────▼─────────────────────────────────┐  │
│  │  Private Cloud Run (Containerized Microservices)           │  │
│  │  Autoscaling · VPC Isolation                               │  │
│  └──┬────────────────┬────────────────┬───────────────────────┘  │
│     │                │                │                          │
│  ┌──▼──────┐  ┌──────▼──────┐  ┌─────▼──────────┐              │
│  │ Redis   │  │ Cloud KMS   │  │ Append-Only    │              │
│  │ Cache   │  │ Signature   │  │ Audit Log      │              │
│  │(TTL     │  │ Service     │  │(Tamper-        │              │
│  │ 10-30m) │  │(Ed25519 HW) │  │ Resistant)     │              │
│  └─────────┘  └─────────────┘  └────────────────┘              │
│                                                                  │
│  Config SSOT: Single config.json                                 │
│  (DRF endpoints, cache TTL, feature flags, constitution ver)     │
│                                                                  │
│  Scalability:                                                    │
│  · Distributed Leader Swarm processing                           │
│  · Horizontal evidence query scaling                             │
│  · Multi-region failover                                         │
└──────────────────────────────────────────────────────────────────┘
```

---

## 15. Global Multi-Jurisdiction Design

Lawmadi OS principles are **universally applicable** to any legal system.

### 15.1 Jurisdiction-Specific SSOT Designation

| Jurisdiction | Designated SSOT |
|-------------|-----------------|
| **Korea** | National Law Information Center DRF Open API |
| **United States** | GovInfo API, state legislature APIs, PACER |
| **European Union** | EUR-Lex, national legal databases |
| **United Kingdom** | legislation.gov.uk API |
| **Japan** | e-Gov 法令検索 API |
| **Other** | Official government legal information API |

### 15.2 Universal Requirements

All five constitutional principles apply **regardless of jurisdiction**:
- One authoritative source per jurisdiction (SSOT)
- Zero Inference — universal
- Fail-Closed — universal
- Temporal validity checking — universal
- Cryptographic trust chain — universal
- FSM-based deterministic processing — universal

### 15.3 Multi-Jurisdiction Operations

- Each jurisdiction **must** have its own designated SSOT
- Cross-jurisdiction decisions require evidence from **all** relevant SSOTs
- Conflict-of-law rules must be **explicitly modeled** in the decision graph
- No jurisdiction may "borrow" evidence from another's SSOT

---

## 16. Non-Public Assets

This document intentionally **excludes** the following proprietary and confidential information:

- Routing scoring formulas (weights, rule priorities, exception handling)
- Full Constitution DSL rule set and exception logic
- Evidence Trust Score specific formulas and weights
- Operational config, endpoints, API keys, request patterns
- Deployment infrastructure (IaC, CI/CD, security policy details)
- LLM provider routing logic details
- Production data, user data, internal evaluation datasets
- KMS/HSM key material and production signature configurations

---

## 17. Document Cross-References

| Document | Purpose | Version |
|----------|---------|---------|
| [`llms.txt`](llms.txt) | Unified LLM Directive & Global Legal Decision Intelligence Standard | v2.0-Unified |
| [`LICENSE.txt`](LICENSE.txt) | Comprehensive Proprietary License (14 IP categories, 60+ components) | v2.0 |
| [`CITATION.cff`](CITATION.cff) | Machine-readable citation metadata | v2.0-Unified |
| [`README.md`](README.md) | Repository overview and quick start | v2.0-Unified |
| `Lawmadi_OS_통합기술백서_v3_Final.docx` | Internal Reference Architecture (Confidential) | v3.0-Final |
| `Public Whitepaper PDF` | Public Technical Whitepaper (Sanitized) | v2.0 |

---

## Disclaimer

This document is for technical architectural reference purposes only and does not constitute legal advice. Specific outcomes depend on the facts of each case. Professional legal consultation is recommended before making important decisions.

본 문서는 기술 아키텍처 참조 목적이며, 법률자문이 아닙니다. 구체적 사안은 사실관계에 따라 달라질 수 있으므로, 중요한 의사결정 전에는 전문가 상담을 권장합니다.

---

**Copyright © 2026 Jainam Choe (최재남). All rights reserved.**

**Lawmadi OS — 법률 의사결정을 위한 운영체제이며, 법률 영역에서 Computable Trust를 실현한다.**
