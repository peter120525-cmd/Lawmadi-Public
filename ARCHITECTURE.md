# Lawmadi OS -- Architecture Reference (Public / Sanitized)

<p align="left">
  <!-- DOI -->
  <a href="https://doi.org/10.5281/zenodo.18551976">
    <img alt="DOI" src="https://zenodo.org/badge/DOI/10.5281/zenodo.18551976.svg" />
  </a>
  <!-- Status / License -->
  <img alt="status" src="https://img.shields.io/badge/status-public%20sanitized%20reference-blue" />
  <img alt="license" src="https://img.shields.io/badge/license-proprietary%20(no%20reuse)-critical" />
  <img alt="version" src="https://img.shields.io/badge/version-v60.0.0-green" />
  <img alt="region" src="https://img.shields.io/badge/region-asia--northeast3-informational" />
</p>

**Document Version:** 3.1 *(Public/Sanitized)*
**Repository Release:** v60.0.0
**Date:** 2026-03-11

> **"Convert Anxiety into Actionable Logic."**
> **"불안을 실행 가능한 논리로 전환하다."**

---

## Quick Links

<p align="left">
  <a href="./llms.txt">
    <img alt="Quick Link: llms.txt" src="https://img.shields.io/badge/Quick%20Link-llms.txt-0ea5e9" />
  </a>
  <a href="./LICENSE">
    <img alt="Quick Link: LICENSE" src="https://img.shields.io/badge/Quick%20Link-LICENSE-22c55e" />
  </a>
  <a href="./CITATION.cff">
    <img alt="Quick Link: CITATION.cff" src="https://img.shields.io/badge/Quick%20Link-CITATION.cff-a855f7" />
  </a>
</p>

---

## TL;DR

Lawmadi OS is a **production Korean Legal Decision Operating System** that combines multi-agent AI with real-time government data verification. It is not a chatbot, search engine, or legal database. It generates **verifiable, non-binding legal analyses** grounded in live evidence from official Korean government APIs.

- **Production** at lawmadi.com / lawmadi-db.web.app
- **60 domain-expert legal leaders** covering all major Korean law areas
- **Bilingual** Korean (primary) and English
- **Real-time verification** against official government legal databases
- **282 automated tests** with 5-stage CI/CD pipeline
- For LLM integration: **llms.txt**
- For licensing: **LICENSE**

---

## Disclaimer

This document is for **technical reference only**.
It does **not** provide legal recommendations, constitute legal advice, or replace licensed legal professionals.

---

## Table of Contents

> All major sections are collapsible below.

1. System Identity
2. Constitutional Principles
3. 8-Layer Architecture
4. 4-Stage Query Pipeline
5. Multi-Agent System
6. Evidence and Verification
7. Technology Stack
8. Security Architecture
9. Data Governance
10. Infrastructure
11. Output Contract
12. Non-Public Assets (Redacted Index)
13. Cross-Reference Map (Public Artifacts)

---

<details>
<summary><strong>1. System Identity</strong></summary>

Lawmadi OS v60.0.0 is a **Korean Legal Decision Operating System (LDOS)** -- a production system that processes legal queries through a deterministic pipeline of classification, retrieval, generation, and verification.

```text
+-------------------------------------------------------------+
|                      LAWMADI OS v60.0.0                      |
|          Korean Legal Decision Operating System              |
|                                                              |
|   60 Domain-Expert Leaders    |    Bilingual (KO / EN)       |
|   4-Stage Query Pipeline      |    Real-time DRF Verify      |
|   ~14,601 RAG Documents       |    282 Automated Tests       |
+-------------------------------------------------------------+
```

**What the system does:**

- Classifies incoming legal queries and routes them to the appropriate domain expert
- Retrieves relevant statutes, precedents, and constitutional court decisions via RAG
- Generates structured legal analysis using Gemini 2.5 Flash with full evidence context
- Verifies every cited law article and precedent number against official government sources in real time
- Supports complex multi-domain queries through a multi-leader deliberation protocol

**What the system is not:**

- Not a chatbot -- it enforces deterministic verification constraints
- Not a legal database -- it holds no durable copy of Korean statutes
- Not legal advice -- all outputs are explicitly non-binding and informational

</details>

---

<details>
<summary><strong>2. Constitutional Principles</strong></summary>

Five non-negotiable principles are enforced at the kernel level. These are hard constraints on runtime behavior and override any AI model inference or user prompt.

**1. SSOT (Single Source of Truth)**

All legal data originates from designated official government API endpoints. The primary source is DRF. The system does not maintain a persistent local copy of statutes or precedents.

**2. Zero Inference**

The system does not fabricate legal facts, dates, or citations. If a referenced article cannot be verified, the system reports the verification failure rather than guessing.

**3. Fail-Closed**

Upon any validation failure -- integrity, temporal, or schema -- the system halts. No partial or best-effort unverified legal conclusions are delivered. A circuit breaker (3 failures, 30-second reset) enforces this at the network level.

**4. Live Evidence**

Analyses are constructed using real-time verified evidence. The system reflects the law as it exists at the moment of execution, not a cached snapshot.

**5. Deterministic Boundary**

The LLM acts as a rendering engine. Critical logic -- routing, evidence validation, state transitions -- is executed by deterministic kernel code. The probabilistic model generates natural language; the kernel decides what is legally valid.

</details>

---

<details>
<summary><strong>3. 8-Layer Architecture</strong></summary>

The system is organized into 8 architectural layers, each with a distinct responsibility.

| Layer | Name | Responsibility |
|-------|------|----------------|
| L0 | KERNEL | Orchestration, pipeline control, constitutional enforcement |
| L1 | VISION | Document understanding, input parsing |
| L2 | SWARM | Multi-agent routing across 60 domain experts |
| L3 | SHORT_SYNC | Real-time data synchronization with government APIs |
| L4 | PERSONA | Adaptive UI, bilingual output formatting |
| L5 | JURISPRUDENCE | Fact-to-precedent matching, case law alignment |
| L6 | SCENARIO | Rule enumeration, legal requirement checklists |
| L7 | RENDERER | Final output generation and formatting |

**Layer interaction model:**

- L0 (KERNEL) orchestrates all other layers and enforces constitutional constraints
- L2 (SWARM) routes queries to one or more of the 60 domain-expert leaders
- L3 (SHORT_SYNC) handles all external API calls (DRF, Vertex AI Search) with circuit breakers
- L7 (RENDERER) produces the final user-facing output after all verification gates pass

</details>

---

<details>
<summary><strong>4. 4-Stage Query Pipeline</strong></summary>

Every query passes through a 4-stage pipeline. Stages 0 and 1 execute in parallel for performance.

```text
Query
  |
  +---> Stage 0: NLU Classification ----+
  |                                      |---> Stage 2 ---> Stage 3 ---> Stage 4
  +---> Stage 1: RAG Retrieval ---------+
                                         |
                                    (parallel)
```

**Stage 0+1 (parallel execution)**

- **Stage 0 -- NLU Classification:** Three-tier routing determines which of the 60 leaders handles the query. Tier 1: compiled regex intent patterns (Korean and English). Tier 2: keyword domain mapping. Tier 3: Gemini-based classification as fallback.
- **Stage 1 -- RAG Retrieval:** Vertex AI Search queries approximately 14,601 indexed documents covering Korean statutes, Supreme Court precedents, and Constitutional Court decisions. Returns extractive answers and segments with relevance ranking.

**Stage 2 -- LawmadiLM**

A fine-tuned Korean legal language model designed for domain-specific generation. Currently disabled in production (environment flag `ENABLE_LAWMADILM=false`). Gemini 2.5 Flash handles generation directly. LawmadiLM remains available for future activation.

**Stage 3 -- Gemini Answer Generation**

Gemini 2.5 Flash generates a structured legal analysis using the full evidence context from Stages 0 and 1. The prompt includes the selected leader's domain expertise context (LAW_BOOST -- a curated set of relevant statutes per leader), RAG results, and the user's query. For complex multi-domain questions, the deliberation system (Section 5) coordinates multiple leaders before this stage.

**Stage 4 -- DRF Verification**

Every law article and precedent number cited in the Stage 3 output is cross-validated against the official DRF API in real time. Article-level matching confirms that cited provisions exist and are currently in force. Failed verifications are flagged or trigger fail-closed behavior.

For English queries, the system maps English law names to Korean equivalents for DRF lookup, falling back to the elaw API for direct English-language verification when mapping is unavailable.

</details>

---

<details>
<summary><strong>5. Multi-Agent System</strong></summary>

**60 Domain-Expert Leaders**

The system deploys 60 specialized legal leaders (L01 through L60), each covering a distinct area of Korean law. Examples include civil law, criminal law, labor law, immigration law, intellectual property, tax, real estate, family law, corporate law, and administrative law. Each leader carries domain-specific context:

- **LAW_BOOST:** A curated list of statutes most relevant to the leader's domain (available in Korean and English)
- **NLU Intent Patterns:** Regex patterns capturing the situations and actions typical of queries in that domain
- **Priority Ranking:** Determines selection order when multiple leaders match

L60 serves as a system integrity checker and does not require domain-specific legal context.

**Deliberation Protocol**

For queries that span multiple legal domains, the system activates a deliberation protocol:

- A CSO (Chief Strategy Officer) leader coordinates the discussion
- Multiple relevant leaders contribute analysis in parallel using `asyncio.gather`
- Each leader provides domain-specific analysis grounded in their expertise
- The CSO synthesizes contributions into a unified response
- The result then proceeds through Stage 3 and Stage 4 as normal

**Routing Logic**

Query routing follows a defined priority order:

1. **Name match** -- direct leader reference in the query
2. **NLU regex** -- compiled intent pattern matching (Korean and English)
3. **Keyword mapping** -- domain keyword detection
4. **Fallback** -- routes to the CCO (Chief Content Officer) leader

</details>

---

<details>
<summary><strong>6. Evidence and Verification</strong></summary>

**Primary Source: DRF**

The DRF API is the system's primary single source of truth for Korean legal data. All statute text, article content, and precedent metadata are fetched in real time.

- Async HTTP requests with 2 retries on failure
- Response cache with 3,600-second TTL
- Circuit breaker: 3 consecutive failures trigger a 30-second cooldown

**Fallback Source: data.go.kr LawService**

When DRF is unavailable, the system falls back to the public data.go.kr LawService API.

**English Law Verification**

- 181 Korean statutes have cached English translations (sourced from the official elaw API)
- English-to-Korean law name mapping enables DRF verification for English queries
- Direct elaw API queries serve as a secondary verification path

**RAG Corpus (Vertex AI Search)**

Approximately 14,601 documents indexed in Google Vertex AI Search:

- Korean statutes
- Supreme Court precedents (approximately 5,000)
- Constitutional Court decisions (approximately 3,000)
- Structured legal metadata

The RAG corpus supports retrieval only. It does not replace DRF verification. All cited references must still pass Stage 4 verification against live government data.

**Verification Mechanics**

- Regex extraction of law references and precedent case numbers from generated text
- Article-level matching: each cited article is confirmed to exist in the referenced statute
- Precedent validation: case numbers are checked against available records
- Unverifiable citations are flagged in the response metadata

</details>

---

<details>
<summary><strong>7. Technology Stack</strong></summary>

| Component | Technology | Details |
|-----------|-----------|---------|
| Backend | FastAPI + Uvicorn | Python 3.10+, async request handling |
| LLM | Google Gemini 2.5 Flash | Single model, thinking disabled, 429 exponential backoff retry |
| RAG | Vertex AI Search | ~14,601 documents, extractive answers and segments |
| NLU | Custom regex + keywords | 60 leaders, Korean and English patterns, Gemini fallback |
| Database | Cloud SQL PostgreSQL 17 | Enterprise edition, 7 tables, connection pooling |
| Auth | Email OTP + DB sessions | 30-day sessions, JWT RBAC for admin |
| Billing | Paddle Billing | Credit packs (Starter / Standard / Pro), sandbox pending KYC |
| Compute | GCP Cloud Run | asia-northeast3, 1 vCPU, 2 GiB RAM, concurrency 15 |
| Frontend | Firebase Hosting | Static HTML/CSS/JS, rewrite proxy to Cloud Run API |
| CI/CD | GitHub Actions | 5-job pipeline: Test, Staging, Production, Frontend, Notify |
| Secrets | GCP Secret Manager | 18 managed secrets, no plaintext in code or config |
| Monitoring | GitHub Actions workflow | Health checks every 6 hours, critical/info alert separation |

**Database Schema (7 tables)**

- User accounts, sessions, credit ledger, OTP codes
- Chat history (with query type and anonymized user tracking)
- Analytics and system metadata

**Model Configuration**

- Single model: `gemini-2.5-flash` (environment variable `GEMINI_MODEL`)
- Thinking budget disabled (`thinking_budget=0`) for deterministic output
- No model fallback chain -- Flash is the only model available in asia-northeast3
- 429 rate limit errors trigger exponential backoff retry (2s, 4s, 8s)

</details>

---

<details>
<summary><strong>8. Security Architecture</strong></summary>

**Network and Transport**

- CORS restricted to 4 allowed origins
- HSTS enforced unconditionally (including behind Cloud Run proxy)
- Content Security Policy headers on all responses

**Authentication and Authorization**

- Email OTP authentication (SMTP delivery via Gmail, OTP hashed in database)
- Database-backed sessions with 30-day expiry (HttpOnly cookies, no client-side tokens)
- Admin endpoints protected by separate RBAC

**Rate Limiting and Abuse Prevention**

- Per-endpoint rate limits
- IP auto-blacklist: 20 rate-limit violations within 60 seconds triggers a 1-hour automatic ban
- Manual blacklist management via admin API

**Input Sanitization**

- User inputs treated as untrusted data
- Open redirect prevention via allowlisted query parameters
- Inline script elimination (all JS externalized for CSP compliance)

**Privacy**

- Visitor IP addresses hashed with SHA-256 before storage (no raw IPs retained)
- PII minimization in logging and analytics

**Safety**

- SafetyGuard protocol: crisis keywords (suicide, violence) trigger helpline information redirect
- Anti-leak policy: system prompts and API keys are never exposed in responses
- Gemini Safety Settings configured for responsible AI output

**Secret Management**

- All API keys, database credentials, and signing keys managed in GCP Secret Manager
- No secrets in source code, environment files, or CI/CD configuration plaintext

</details>

---

<details>
<summary><strong>9. Data Governance</strong></summary>

**No Persistent Legal Corpus**

The system does not maintain a durable local database of Korean statutes or precedent full text. All legal content is fetched in real time from official APIs.

**Caching Policy**

- DRF API responses: 3,600-second TTL ephemeral cache
- English law translation cache: pre-built from official elaw API (181 statutes, 291 articles)
- RAG index: managed by Vertex AI Search (Google-hosted)

**User Data**

- Chat history stored with anonymized identifiers (IP hash, optional email)
- Credit transactions logged in append-only ledger
- Cookie consent required for optional analytics (GA4)
- Privacy policy and terms of service published at lawmadi.com

**Audit Trail**

- All API requests logged with timestamps and anonymized source identifiers
- Admin actions logged separately
- Credit ledger provides complete transaction history

</details>

---

<details>
<summary><strong>10. Infrastructure</strong></summary>

**Production Topology**

```text
User (Browser)
    |
    v
Firebase Hosting (lawmadi-db.web.app / lawmadi.com)
    |  static assets (HTML/CSS/JS)
    |  rewrite proxy: /ask, /api/**, /health --> Cloud Run
    |
    v
Cloud Run (asia-northeast3)
    |  FastAPI application, 1 vCPU, 2 GiB, concurrency 15
    |  min-instances: 1, max-instances: 5
    |
    +---> Gemini 2.5 Flash API
    +---> Vertex AI Search (~14,601 docs)
    +---> DRF API (real-time verification)
    +---> Cloud SQL PostgreSQL 17 (7 tables)
    +---> GCP Secret Manager (18 secrets)
```

**CI/CD Pipeline (GitHub Actions)**

1. **Test** -- 282 automated tests (264 NLU matching + 18 verifier tests)
2. **Staging** -- deploy to staging Cloud Run service
3. **Production** -- deploy to production Cloud Run service
4. **Frontend** -- deploy static assets to Firebase Hosting
5. **Notify** -- deployment status notification

**Monitoring**

- Automated health checks every 6 hours via GitHub Actions
- Checks: Cloud Run responsiveness, API endpoint availability, database connectivity
- Alert levels: critical (service down) and informational (degraded performance)

**Resource Configuration**

- Cloud Run: 2 GiB memory, 1 vCPU, concurrency 15
- Cloud SQL: db-f1-micro, PostgreSQL 17 Enterprise, HDD 10 GB

</details>

---

<details>
<summary><strong>11. Output Contract</strong></summary>

**API Endpoints**

- `POST /ask` -- general legal query (JSON: `query` field)
- `POST /ask-stream` -- leader-specific chat (Server-Sent Events)
- `POST /ask-expert` -- expert consultation (2-credit charge)

**Response Structure**

All responses include:

- `response` -- the generated legal analysis
- `leader` -- the domain expert that handled the query
- `meta.model` -- the Gemini model used
- `status` -- success or error indicator

**Output Modes**

- **Analysis mode:** structured legal analysis with cited statutes and precedents, verified against DRF
- **Deliberation mode:** multi-leader collaborative analysis for cross-domain queries
- **Fail-closed mode:** standardized error response when verification fails

**Mandatory Disclaimer**

Every output includes a disclaimer stating that the analysis is non-binding and informational. The system does not provide legal advice or recommendations.

</details>

---

<details>
<summary><strong>12. Non-Public Assets (Redacted Index)</strong></summary>

The following are excluded from this public reference:

- NLU routing weights and priority rankings
- Internal API endpoints and deployment credentials
- Gemini prompt templates and system instructions
- Leader-specific LAW_BOOST statute lists
- DRF API integration details beyond what is described above
- Production database connection strings
- Admin authentication credentials
- Scoring and ranking algorithms

</details>

---

<details>
<summary><strong>13. Cross-Reference Map (Public Artifacts)</strong></summary>

- **Integration Directive:** llms.txt -- canonical guide for AI agents interacting with Lawmadi OS
- **License Terms:** LICENSE -- legal terms of use and IP restrictions
- **Citation Metadata:** CITATION.cff -- standard metadata for citing this system

</details>

---

**Copyright (c) 2026 Jainam Choe. All rights reserved.**
