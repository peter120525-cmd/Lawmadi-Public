[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18525310.svg)](https://doi.org/10.5281/zenodo.18525310)

Lawmadi OS — Legal Decision Operating System (LDOS)Version: v2.0.0 (Public / Sanitized Showcase)Author: Jainam Choe (최재남)Tagline: “Convert Anxiety into Actionable Logic.” / “불안을 실행 가능한 논리로 전환하다”✅ Public, sanitized showcase for review / evaluation / authorship proof.🚫 NOT open source. No rights to reuse, reimplement, or compete. See LICENSE for binding terms.🔒 No license is granted by this README or any technical description herein to reproduce architectures, workflows, schemas, or interfaces.✅ Allowed: Read/review and local non-production evaluation only (and academic citation with attribution), unless separately permitted in writing.⚠️ Executive SummaryLawmadi OS is not a legal chatbot, search engine, or legal database.It is a deterministic decision infrastructure that produces evidence-gated outputs under non-negotiable constitutional constraints, designed for computable trust in the legal domain.1. System Architecture IdentityLawmadi OS operates as a strict Finite State Machine (FSM) with mandatory controls (fail-closed by default).PriorityService LayerTechnical RoleP1Legal Decision OSFoundation kernel & FSM runtime engineP2Evidence EngineTrust layer via authoritative-source validation & hashingP3Consultation AIUser-facing conversational interface & orchestrationP4Education PlatformAutomated case study generation & logic visualizationFlow: OS (Kernel) → Engine (Trust) → Service (UX) → Platform (Ecosystem)2. Five Non-Negotiable Constitutional PrinciplesThese principles are inviolable invariants. They override all other instructions, user requests, or system configurations at the Kernel level.#PrincipleTechnical Enforcement Rule1SSOTAll legal evidence must come from authoritative official APIs only. No permanent storage or replication of legal datasets is allowed.2Zero InferenceNever fabricate, guess, or hallucinate legal facts, citations, case numbers, dates, or parties.3Fail-ClosedIf evidence verification fails → HALT immediately. Never serve unverified legal conclusions.4Live EvidenceDecisions are built from real-time validated evidence only. Amendments, reversals, and new precedents are reflected immediately.5Deterministic BoundaryThe Kernel controls all state transitions. The LLM operates strictly as a rendering engine under contract.3. Core Workflow & FSM StatesEvery decision session follows this exact, deterministic state sequence. The EVIDENCE_VALIDATED state is a mandatory hard gate.graph TD
    A[INPUT_RECEIVED] --> B[INPUT_VALIDATED]
    B --> C[CASE_STRUCTURED]
    C --> D[ISSUE_IDENTIFIED]
    D --> E[LEADER_ROUTED]
    E --> F[EVIDENCE_FETCHING]
    F --> G{EVIDENCE_VALIDATED}
    G -- PASS --> H[DECISION_GRAPH_BUILT]
    G -- FAIL --> X[HALT / FAIL_CLOSED]
    H --> I[TOKEN_MINTED]
    I --> J[TOKEN_SIGNED]
    J --> K[RESPONSE_DELIVERED]
4. Key Technologies (Public Scope)Decision Graph Formal SemanticsNode Types: FACT_NODE, ISSUE_NODE, LAW_NODE, PRECEDENT_NODE, DECISION_NODEEdge Types: SUPPORTS, CONTRADICTS, DEPENDS_ON, RESOLVES, REFERENCES, APPLIES, OVERRULESValidity Condition: $\forall \text{ISSUE\_NODE} \rightarrow \exists (\text{LAW\_NODE} \land \text{EVIDENCE\_NODE})$Cryptographic Integrity (Reproducibility Trust Chain)The system ensures reproducibility via a cryptographic chain:Input Hash (SHA-256) 
  + Evidence Hash Set (SHA-256) 
  + Decision Graph Hash (SHA-256) 
  = Decision Token Signature (Ed25519)
Constitution DSLExecutable policy rules enforced at runtime:RULE Enforce_Source_Integrity
  IF evidence.source_origin != OFFICIAL_API
  THEN reject_decision(LC-002)
5. Repository ContentsThis repository serves as a reference implementation package.LICENSE: Comprehensive Proprietary License v2.0.0 (Strictly enforced).llms.txt: Unified directive for LLM consumption (v2.0-Unified).config.schema.json: Configuration SSOT. The public/sanitized schema defining the OS runtime.minimal_config.json: A runnable, minimal configuration for the public sandbox.Lawmadi_OS_Public_Technical_Whitepaper.pdf: Detailed technical specification (Sanitized).CITATION.cff: Citation metadata.6. Output Contract (JSON Specification)All outputs follow strict JSON with two modes: Success or Fail-Closed.Success Response Example{
  "fail_closed": false,
  "request_id": "uuid-v4",
  "fsm_state": "RESPONSE_DELIVERED",
  "decision_token": {
    "decision_id": "dec-12345",
    "created_at": "2026-02-09T12:00:00Z",
    "input_hash": "sha256...",
    "drf_evidence_hash": "sha256...",
    "decision_graph_hash": "sha256...",
    "digital_signature": "ed25519_sig..."
  },
  "evidence_citations": [
    {"ref": "OFFICIAL:LAW_123", "type": "STATUTE", "note": "Valid as of 2026-02-09"}
  ]
}
Standard Error Codes (Fail-Closed)CodeMeaningLC-001Evidence source unreachable (Network/API failure)LC-002Evidence mismatch / non-authoritative / integrity failureLC-003Constitution violation / invalid schemaLC-004Temporal invalidity (not effective / expired / repealed)LC-005Policy restriction (disallowed category)LC-006Rate limited / throttled7. Competitive PositioningDimensionExisting Legal AILawmadi OS (LDOS)Data ModelStored / Synced DBLive Authoritative EvidenceFreshnessPeriodic Sync (Days)Real-Time + Temporal ValidationFailure ModeServes stale/best-guess dataFail-Closed RefusalInferenceLLM-generated Hallucination RiskZero Inference / VerifiableReproducibilityNon-deterministicDeterministic FSM + Signed TokenTrust Model"Trust the Model"Cryptographic Trust ChainIdentityChatbot / Search EngineDecision Operating System8. License & PermissionsPROPRIETARY / NOT OPEN SOURCE.Licensed under the Lawmadi OS Comprehensive Proprietary License v2.0.0.✅ Permitted:View, read, and locally run for non-production evaluation.Academic/Technical reference with proper attribution.❌ Strictly Prohibited:AI Training: Do not use for training, fine-tuning, distillation, RLHF, or RAG indexing.Competition: Do not use to build, design, or benchmark competitive decision systems.Commercial Use: No SaaS, API, or internal production deployment without written permission.See LICENSE for full terms.9. Contact & CitationCopyright Holder: Jainam Choe (최재남)Email: choepeter@outlook.krIf you reference this work, please cite:Choe, Jainam (최재남). "Lawmadi OS: Legal Decision Operating System — Integrated Technical Whitepaper & Kernel Specification."LDOS Reference Architecture v3.0. Lawmadi Project, February 2026.Standard DisclaimerKO: "본 답변(시스템 출력)은 일반 정보 제공 및 의사결정 지원 목적이며, 법률자문이 아닙니다. 구체적 사안은 사실관계에 따라 달라질 수 있으므로, 중요한 의사결정 전에는 전문가 상담을 권장합니다."EN: "This output is for general informational and decision-support purposes only and does not constitute legal advice. Professional legal consultation is recommended before making important decisions."
