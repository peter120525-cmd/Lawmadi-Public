# Lawmadi OS — Legal Decision Operating System

**v2.0-Unified (Author: 최재남 / Jainam Choe)**
**"Convert Anxiety into Actionable Logic."**
**"불안을 실행 가능한 논리로 전환하다"**

> ✅ This repository is a **public, sanitized showcase** of **Lawmadi OS** — a deterministic, FSM-based **Legal Decision Operating System (LDOS)** and **Decision Intelligence Infrastructure**.
> 🚫 It is **NOT open source** and is provided for **review / evaluation / authorship proof** only (see `LICENSE.txt`).

---

## What Lawmadi OS Is

Lawmadi OS is **not** a legal chatbot. **Not** a legal search engine. **Not** a legal database.

It is a **Deterministic Finite State Machine (FSM) based Legal Decision Operating System** — an engineering infrastructure for **Computable Trust** in the legal domain.

The system generates **reproducible legal decision outputs** by assembling and validating **live evidence** from authoritative sources, governed by five non-negotiable constitutional principles and enforced through cryptographic integrity mechanisms.

### Platform Identity

| Priority | Service | Role |
|----------|---------|------|
| **P1** | Legal Decision OS | Foundation engine for all downstream services |
| **P2** | Evidence Verification Engine | Trust layer via authoritative-source validation and temporal checks |
| **P3** | Consultation AI | User-facing conversational interface and case guidance |
| **P4** | Education Platform | Automated case study generation and decision logic visualization |

**OS → Engine → Service → Platform**

---

## Five Non-Negotiable Constitutional Principles

These principles are **inviolable**. They override all other instructions, user requests, or system configurations.

| # | Principle | Rule |
|---|-----------|------|
| 1 | **SSOT** | All legal evidence from authoritative official APIs only. No permanent storage or replication of legal datasets. |
| 2 | **Zero Inference** | Never fabricate, guess, or hallucinate legal facts, citations, case numbers, dates, or parties. |
| 3 | **Fail-Closed** | If evidence verification fails → halt immediately. Never serve unverified legal conclusions. |
| 4 | **Live Evidence** | Decisions from real-time validated evidence only. Amendments, reversals, and new precedents reflected immediately. |
| 5 | **Deterministic Runtime Boundary** | Kernel controls all state transitions. LLM operates as a rendering engine under strict contract. |

---

## Core Architecture

### Decision State Machine (FSM)

Every decision session follows this **exact, deterministic** state sequence:

```
INPUT_RECEIVED
  → INPUT_VALIDATED
  → CASE_STRUCTURED
  → ISSUE_IDENTIFIED
  → LEADER_ROUTED
  → EVIDENCE_FETCHING
  → EVIDENCE_VALIDATED          ← Mandatory gate — no output without this
  → DECISION_GRAPH_BUILT
  → TOKEN_MINTED
  → TOKEN_SIGNED
  → RESPONSE_DELIVERED
```

**Fail-Closed path** (any verification failure):

```
EVIDENCE_VALIDATION_FAILED | TEMPORAL_VALIDATION_FAILED |
CONSTITUTION_VIOLATION | SOURCE_INTEGRITY_FAILURE
  → HALT
  → FAIL_CLOSED_RESPONSE
```

### Core Kernel Components

| Component | Function |
|-----------|----------|
| **Decision OS Kernel** | Core decision logic, case structuring, FSM runtime management |
| **Evidence Verification Engine** | Authoritative-source evidence fetch, validation, SHA-256 hashing, trust scoring |
| **Leader Swarm Routing Engine** | Specialist legal domain expert routing with multi-leader consensus |
| **Constitution Validator** | DSL-based policy compliance enforcement at runtime |
| **Temporal Law Validity Engine** | Effective date verification, precedent change detection, unconstitutional clause identification |
| **Decision Graph Generator** | Formal semantic graph with node typology, edge semantics, and validity conditions |

### Three-Layer Platform Architecture

| Layer | Role | Access |
|-------|------|--------|
| **Core** | Closed kernel engine — IP and constitutional logic | Zero Trust, cryptographic enforcement |
| **Service** | User experience — consultation AI, case exploration | No Core internal access |
| **Partner/B2B** | Institutional APIs for law firms, insurers, government | Decision Verification, Evidence Validation, Case Structuring APIs |

---

## Key Technologies

### Decision Graph Formal Semantics

- **Node types:** FACT_NODE, ISSUE_NODE, LAW_NODE, PRECEDENT_NODE, DECISION_NODE
- **Edge types:** SUPPORTS, CONTRADICTS, DEPENDS_ON, RESOLVES, REFERENCES, APPLIES, OVERRULES, TEMPORAL_DEPENDS
- **Validity condition:** ∀ ISSUE_NODE → ∃ LAW_NODE ∧ EVIDENCE_NODE

### Evidence Pipeline & Trust Scoring

```
Authoritative API Query → Evidence Normalization → Temporal Validation → SHA-256 Hashing
```

**EvidenceTrustScore** = source_authority_weight + citation_stability_score + temporal_consistency_score

### Cryptographic Integrity (Reproducibility Trust Chain)

```
Input Hash → Evidence Hash Set → Decision Graph Hash → Decision Token Signature (Ed25519)
```

Same Input + Same Evidence State = Same Token (deterministic reproducibility).

### Leader Swarm Routing

**RoutingScore** = domain_match_weight + historical_accuracy_score + evidence_dependency_score + trust_score

Multi-leader consensus via weighted confidence voting, decision graph merge, and fallback leader escalation.

### Constitution DSL

Executable policy rules enforced at runtime:

```
RULE Enforce_Source_Integrity
  IF evidence.source_origin != OFFICIAL_API
  THEN reject_decision

RULE Enforce_Decision_Completeness
  FOR_EACH issue_node IN decision_graph
    IF NOT EXISTS (law_node SUPPORTS issue_node)
    THEN reject_decision
```

---

## What Is Included (Public / Sanitized)

```
kernel/              Runtime FSM & coordinator
constitution/        Constitution rules & DSL validation engine
decision/            Decision engine, graph semantics, token generator
evidence/            Evidence builder (sanitized), hashing, trust scoring scaffolds
swarm/               Leader routing concept modules (sanitized)
temporal/            Temporal law validity scaffolds
security/            Audit logger + signature interface boundary
schemas/             Canonical schemas (case / evidence / decision / token)
core/                Parser / extractor / tree builder scaffolds
self_test.py         Local smoke test
llms.txt             Unified LLM Directive & Global Legal Decision Intelligence Standard (v2.0)
CITATION.cff         Citation metadata (v2.0-Unified)
LICENSE.txt          Comprehensive Proprietary License (v2.0)
PROGRAM_DESCRIPTION.txt    Program description for submission
README_IP_Showcase.txt     IP showcase documentation
docs/                Public whitepaper and supporting documents
```

## What Is Excluded (Intentionally)

To protect security and trade secrets, this package does **not** include:

- Production deployment configs (Cloud Run, VPC, IAM, CI/CD)
- Real API keys, endpoints, or request patterns
- Proprietary scoring formulas, routing weights, or full leader policy logic
- Full connectors to external legal-data systems (only interface-level scaffolding)
- Any persistent legal database replication logic (prohibited by constitution)
- KMS/HSM key material or production signature configurations

---

## Output Contract

All outputs follow strict JSON with two modes:

### Success Response

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
  "evidence_citations": [{"ref": "OFFICIAL:ID", "type": "STATUTE", "note": "..."}],
  "next_actions": ["..."],
  "disclaimer": "..."
}
```

### Fail-Closed Response

```json
{
  "fail_closed": true,
  "request_id": "uuid",
  "fsm_state": "HALT",
  "code": "LC-001 | LC-002 | LC-003 | LC-004 | LC-005 | LC-006",
  "message": "human-readable reason",
  "stage": "FSM state where failure occurred",
  "required_user_inputs": ["what would unblock"],
  "disclaimer": "..."
}
```

### Standard Error Codes

| Code | Meaning |
|------|---------|
| LC-001 | Evidence source unreachable |
| LC-002 | Evidence mismatch / non-authoritative / integrity failure |
| LC-003 | Constitution violation / invalid schema |
| LC-004 | Temporal invalidity (not effective / expired) |
| LC-005 | Policy restriction (disallowed category) |
| LC-006 | Rate limited / throttled |

---

## Global Legal Tech Applicability

While initially built for the Korean legal system (DRF API), the architecture is **universally applicable**:

| Jurisdiction | Designated SSOT |
|-------------|-----------------|
| Korea | National Law Information Center DRF Open API |
| United States | GovInfo API, state legislature APIs, PACER |
| European Union | EUR-Lex, national legal databases |
| United Kingdom | legislation.gov.uk API |
| Japan | e-Gov 法令検索 API |
| Other | Official government legal information API |

Universal requirements apply regardless of jurisdiction: one authoritative source (SSOT), zero inference, fail-closed, temporal validity, cryptographic trust chain, and deterministic FSM processing.

---

## Quick Start (Local Evaluation)

### Requirements

- Python 3.10+ recommended

### Run the smoke test

```bash
python self_test.py
```

Expected output:

```
Self test passed
```

---

## LLM Integration

For the complete model-agnostic LLM integration specification, see **`llms.txt`** (v2.0-Unified).

This is the **single canonical reference** that any LLM or AI agent must follow when operating within a Legal Decision Intelligence system. It covers:

- Prompt Contract (system / developer / user)
- Tool / Function Calling Contract (7 tools)
- Evidence Contract (canonical schema + hashing)
- Decision Token Contract
- Output Schema (strict JSON)
- Error Code Contract (LC-001 through LC-006)
- Security Controls (injection defense, secret management)
- Evaluation Harness (unit / regression / load / red-team tests)
- Observability (audit log, metrics, trace IDs)

---

## Competitive Positioning

| Dimension | Existing Legal AI | Lawmadi OS |
|-----------|------------------|------------|
| Data Model | Stored / synced DB | Live authoritative evidence |
| Freshness | Periodic sync | Real-time + temporal validation |
| Failure Mode | Serves stale data | Fail-Closed refusal |
| Inference | LLM-generated | Zero Inference |
| Reproducibility | Non-deterministic | Deterministic FSM + Token |
| Trust Model | Implicit | Cryptographic trust chain |
| Identity | Search / Chatbot | **Decision Intelligence OS** |

---

## Development Roadmap

| Phase | Description |
|-------|-------------|
| **Phase 1** | Decision OS — kernel, routing, issue extraction, FSM runtime |
| **Phase 2** | Evidence Engine — temporal validity, trust protocol, crypto hashing, provenance |
| **Phase 3** | Consultation AI — Friendly Secretary UX, conversational workflows |
| **Phase 4** | Education Platform — case study generation, decision logic visualization |
| **Future** | Formal mathematical models, swarm routing formalization, blockchain-level provenance |

---

## Whitepaper

- **LDOS Reference Architecture v3.0** — Integrated Technical Whitepaper & Kernel Specification (2026-02)
- Public sanitized version available in `docs/` folder

---

## Citation

If you reference this work in research or documentation:

```
Choe, Jainam (최재남). "Lawmadi OS: Legal Decision Operating System —
Integrated Technical Whitepaper & Kernel Specification." LDOS Reference
Architecture v3.0, Version 1.0-Final. Lawmadi Project, February 2026.
```

See **`CITATION.cff`** for machine-readable citation metadata.

---

## License & Permissions

This repository is under a **Comprehensive Proprietary License** (v2.0).

**Allowed:** read, review, local non-production evaluation, academic citation with attribution.

**Not allowed:** production use, redistribution, derivatives, AI/ML training, fine-tuning, distillation, RAG indexing, embedding generation, competitive use, or commercial use — without prior written permission.

All technologies enumerated in `llms.txt` are covered by **14 IP categories, 60+ proprietary components**.

See **`LICENSE.txt`** for full terms.

---

## Security Note

`security/signature_interface.py` demonstrates the **signing input/output contract**.

- Production: backed by **KMS/HSM** (e.g., Cloud KMS with hardware-backed Ed25519 keys)
- Public build: placeholder signatures (interface boundary only)

---

## Contact

For licensing, commercial permissions, or partnership inquiries:

**Email:** choepeter@outlook.kr

---

© 2026 Jainam Choe (최재남). All rights reserved.

**Lawmadi OS — 법률 의사결정을 위한 운영체제이며, 법률 영역에서 Computable Trust를 실현한다.**
