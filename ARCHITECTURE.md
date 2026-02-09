Lawmadi OS — Architecture Reference (Public / Sanitized)
Document Version: 3.0 (Public/Sanitized) · Repository Release: v2.0.0 · 2026-02-09
Copyright © 2026 Jainam Choe (최재남). All rights reserved.
> "Convert Anxiety into Actionable Logic."
> "불안을 실행 가능한 논리로 전환하다."
> 
This document provides a public, sanitized architectural overview of Lawmadi OS — a deterministic, FSM-based Legal Decision Operating System (LDOS). Proprietary scoring formulas, routing weights, deployment configurations, and operational secrets are intentionally excluded.
Lawmadi OS is not a chatbot, not a search engine, and not a legal database. It is a Decision Intelligence Infrastructure that generates reproducible, verifiable decision artifacts (non-binding) grounded in live evidence.
Evidence is fetched from designated SSOT endpoints in real time; the system does not maintain a durable replica of legal texts.
For the complete LLM integration specification, see llms.txt (Directive v2.1-Unified).
For licensing terms, see LICENSE.txt.
Disclaimer: This document is for technical reference only. It does not provide legal recommendations, constitute legal advice, or replace licensed legal professionals.
Table of Contents
 * System Identity
 * Foundational Operating Constitution
 * Platform Layer Architecture
 * Runtime State Machine (FSM)
 * Core Kernel Engines
 * Decision Graph Formal Semantics
 * Evidence Pipeline & Trust Scoring
 * Cryptographic Integrity & Reproducibility
 * Security Architecture
 * Data Governance
 * Output Contract
 * LLM Integration Architecture
 * Concurrency & Scalability (Conceptual)
 * Infrastructure Topology (Non-operational)
 * Global Multi-Jurisdiction Design
 * Non-Public Assets (Redacted Index)
 * Cross-Reference Map (Public Artifacts)
1. System Identity
It is a Decision Intelligence Infrastructure designed for Computable Trust — outputs are reproducible and auditable through evidence lineage, integrity checks, and deterministic state transitions.
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

Strategic Service Hierarchy
 * P1: Legal Decision OS — Foundation engine; the kernel basis for all downstream services.
 * P2: Evidence Verification Engine — Trust layer providing authoritative-source validation.
 * P3: Consultation Interface — User-facing UX (informational; non-recommendation).
 * P4: Education Platform — Automated case study generation & decision logic visualization.
OS → Engine → Service → Platform
2. Foundational Operating Constitution
The system enforces five non-negotiable principles at the kernel level. These serve as hard constraints on the runtime environment, overriding any AI model inference or user prompt injection.
 * SSOT (Single Source of Truth): All legal data must originate from the designated official government API endpoints (e.g., DRF). Local storage of statutes or precedents is strictly prohibited to prevent data staleness. For non-KR jurisdictions, SSOT MUST be the designated official government legal database/API (or its equivalent authoritative source).
 * Zero Inference: The system is barred from fabricating legal facts, dates, or citations. If a fact is missing, the system must ask the user or fail—it cannot guess.
 * Fail-Closed: Upon any validation failure (integrity, temporal, or schema), the system halts immediately. No "partial" or "best-effort" unverified legal conclusions are ever delivered.
 * Live Evidence: Decisions are constructed using only real-time verified evidence. The system reflects the law as it exists at the moment of execution.
 * Deterministic Runtime: The LLM acts solely as a rendering engine. Critical logic (state transitions, evidence validation) is executed by the deterministic Kernel code, not the probabilistic model.
3. Platform Layer Architecture
Lawmadi OS utilizes a strict three-layer architecture to isolate proprietary logic from user interfaces and external partners.
 * Core Layer (Closed Kernel): Contains the FSM runtime, Constitution Validator, and Swarm Routing Engine. This layer is strictly proprietary and inaccessible to the public internet except through secured internal interfaces.
 * Service Layer (User Experience): Handles user interaction (Consultation Interface, Friendly Secretary UX). This layer sanitizes inputs and renders Kernel outputs but contains no legal decision logic itself.
 * Partner / B2B Layer: Provides structured APIs (Verification, Evidence Validation) for institutional integration. Access is governed by strict IAM and rate-limiting policies.
4. Runtime State Machine (FSM)
The core execution flow is modeled as a Deterministic Finite State Machine. This ensures that every decision follows an auditable, linear path.
 * Sequential Enforcement: The process moves from INPUT_RECEIVED → EVIDENCE_FETCHING → EVIDENCE_VALIDATED → TOKEN_MINTED → RESPONSE_DELIVERED.
 * Mandatory Gates: The EVIDENCE_VALIDATED state is a hard gate. If the Kernel cannot cryptographically verify the evidence source and temporal validity, the FSM transitions to HALT (Fail-Closed).
 * Kernel Control: State transitions are managed by Kernel-controlled code, not by LLM token generation. This prevents "jailbreaks" where an LLM might skip validation steps.
5. Core Kernel Engines
The Kernel is composed of specialized engines that handle distinct aspects of the legal decision process.
 * Case Structure Parser: Converts unstructured natural language into a canonical JSON object (CaseStructure), identifying parties, timelines, and claim objects.
 * Issue Extraction Engine: Analyzes the case structure to generate a dependency graph of legal issues (IssueGraph) that need resolution.
 * Leader Swarm Routing Engine: (Conceptual) Selects domain-expert modules under policy-governed arbitration. Selection logic, weights, and ranking formulas are non-public.
 * Temporal Law Validity Engine: Checks the "effective date" of statutes and the "overruled" status of precedents to ensure only currently valid law is applied.
6. Decision Graph Formal Semantics
Legal reasoning is represented internally as a directed acyclic graph (DAG), ensuring logical consistency.
 * Node Typology: The graph consists of strictly typed nodes: FACT_NODE (user input), ISSUE_NODE (legal question), LAW_NODE (statute), EVIDENCE_NODE (precedent/regulation), and DECISION_NODE (conclusion).
 * Edge Semantics: Edges define relationships such as SUPPORTS, CONTRADICTS, DEPENDS_ON, and OVERRULES.
 * Validity Condition: A decision node is only valid if every parent ISSUE_NODE is supported by at least one LAW_NODE and one EVIDENCE_NODE. Unsupported issues trigger a rejection.
7. Evidence Pipeline & Trust Scoring
The system treats legal evidence as a supply chain that must be secured.
 * Pipeline Flow: Authoritative API Query → Normalization → Temporal Validation → Canonical Hashing.
 * Evidence Evaluation: Evidence may be evaluated for operational confidence based on source authority and temporal validity. All evaluation logic is implementation-specific and non-public.
 * Integrity Rules: Evidence is rejected if it originates from non-official domains, lacks required provenance/temporal metadata, or has been marked as repealed/unconstitutional by the Temporal Engine.
8. Cryptographic Integrity & Reproducibility
Lawmadi OS implements a "Chain of Trust" to guarantee that outputs have not been tampered with.
 * Reproducibility: A specific Input Hash + Evidence Hash Set must always yield the same Decision Token.
 * Hashing Strategy: All inputs and evidence are serialized into canonical JSON (sorted keys) and hashed using SHA-256.
 * Digital Signature: The final Decision Token is signed using Ed25519 (Edwards-curve Digital Signature Algorithm). In public builds, a placeholder signature demonstrates the interface contract; production builds use managed keys (KMS/HSM).
9. Security Architecture
Security is designed around "Zero Trust" principles for both user inputs and AI model outputs.
 * Prompt Injection Defense: User inputs are treated as untrusted data. Instructions to "ignore previous rules" are neutralized before processing.
 * Secret Management: API keys and cryptographic secrets are stored in a dedicated Key Management Service (KMS), never in the code or prompts.
 * Tool Sandbox: The LLM cannot execute arbitrary code. It can only request execution of allow-listed Kernel tools, which validate all arguments before running.
10. Data Governance
The system strictly adheres to an Anti-Reconstruction Policy regarding legal data.
 * Prohibited: Creating a persistent database of statutes or precedents. Building mapping tables that allow reconstruction of the original legal corpus.
 * Allowed: Caching data ephemerally (TTL 10-30 minutes) for performance. Storing abstract "pattern data" (e.g., workflow states, checklist metadata) that contains no original legal text.
 * Audit Trail: All data access is logged in an append-only ledger for compliance auditing.
11. Output Contract
All system outputs adhere to a strict JSON Schema (defined in llms.txt).
 * Decision Mode: Returns a decision token and evidence citations, plus an informational summary grounded in cited evidence. No legal recommendations are provided.
 * Reference-Only Mode: Returns citations only (no conclusions/recommendations), per policy.
 * Fail-Closed Mode: Returns a standardized error code (e.g., LC-001) and a description of the failure stage with required inputs.
 * Disclaimer: Every output includes a mandatory disclaimer stating the non-binding nature of the response.
12. LLM Integration Architecture
Lawmadi OS is model-agnostic and treats the LLM as a "Rendering Engine."
 * Role: The LLM formats the logic derived by the Kernel into human-readable text. It does not perform the legal reasoning or evidence validation autonomously.
 * Contracts: Integration is governed by strict contracts (Prompt, Tool, Evidence, Token) that define the boundaries between the deterministic Kernel and the probabilistic Model.
 * Safety: The Kernel verifies the LLM's output against the schema. Hallucinated keys or invalid JSON structures cause the pipeline to fail safely.
13. Concurrency & Scalability (Conceptual)
The architecture supports high-throughput processing without state leakage.
 * Stateless Design: Each request is processed independently. No context is shared between sessions unless explicitly linked by a Case ID.
 * Async Processing: Evidence fetching from external APIs is handled asynchronously to prevent blocking the FSM runtime.
 * Circuit Breakers: Automated mechanisms prevent cascading failures if an external SSOT API becomes unresponsive.
14. Infrastructure Topology (Non-operational)
(Conceptual Overview Only)
 * Gateway: Handles JSON Schema validation, IAM authentication, and rate limiting.
 * Compute: Containerized runtime (managed compute) hosting the Kernel.
 * Caching: Ephemeral TTL cache for acceleration; no durable corpus of legal texts.
 * Key Management: Managed KMS/HSM for production signing keys (non-public).
 * Audit: Append-only audit logs for traceability and compliance.
 * Configuration: Centralized policy/config registry (e.g., config.json) controlling SSOT targets and runtime flags.
15. Global Multi-Jurisdiction Design
The core logic of Lawmadi OS is universal, while data sources are modular.
 * Universal Logic: The FSM, Zero Inference, and Fail-Closed principles apply to all legal systems.
 * Modular SSOT: Each jurisdiction (e.g., Korea, US, EU) has a specific "Adapter" that connects the Evidence Verification Engine to the local authoritative API (e.g., official government legal database/APIs).
 * Isolation: Evidence from one jurisdiction's SSOT is never commingled with another's unless explicitly modeled for cross-jurisdiction referencing (non-conclusive) under strict policy controls.
16. Non-Public Assets (Redacted Index)
The following components are part of the internal production system and are excluded from this public reference:
 * Scoring Algorithms: Exact formulas for Evidence Trust Scores and Leader Routing weights.
 * Production Keys: Private Ed25519 signing keys and API credentials.
 * Operational Config: Specific IP addresses, internal endpoints, and detailed firewall rules.
 * Full DSL Rulebook: The complete set of constitutional enforcement rules (only examples are provided).
 * Proprietary Pattern Data: The historical case decision logic database.
17. Cross-Reference Map (Public Artifacts)
 * Integration Directive: llms.txt (Directive v2.1-Unified) — The canonical guide for AI agents.
 * License Terms: LICENSE.txt (v2.0) — Legal terms of use and IP restrictions.
 * Citation Metadata: CITATION.cff (2.0.0) — Standard metadata for citing this system.
Copyright © 2026 Jainam Choe (최재남). All rights reserved.
