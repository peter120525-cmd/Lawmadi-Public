# Lawmadi OS — Glossary / 용어집

**Legal Decision Operating System (LDOS) · v2.0-Unified**
**Copyright © 2026 Jainam Choe (최재남). All rights reserved.**

This glossary defines every technical term, acronym, and concept used across the Lawmadi OS documentation. Terms are organized by domain and presented bilingually (English / Korean).

> **Cross-references:** Terms marked with → refer to other entries in this glossary.

---

## Table of Contents

1. [Core Identity & Philosophy](#1-core-identity--philosophy)
2. [Constitutional Principles](#2-constitutional-principles)
3. [Runtime & State Machine](#3-runtime--state-machine)
4. [Kernel Engines](#4-kernel-engines)
5. [Decision Graph](#5-decision-graph)
6. [Evidence & Trust](#6-evidence--trust)
7. [Cryptographic Integrity](#7-cryptographic-integrity)
8. [Security](#8-security)
9. [Data & Cache](#9-data--cache)
10. [LLM Integration](#10-llm-integration)
11. [Output & Error Codes](#11-output--error-codes)
12. [Infrastructure](#12-infrastructure)
13. [Platform & Business](#13-platform--business)
14. [Legal Domain](#14-legal-domain)
15. [Acronyms](#15-acronyms)

---

## 1. Core Identity & Philosophy

### Lawmadi OS

**법률 의사결정 운영체제**

The full system name. A deterministic, FSM-based Legal Decision Operating System. Not a chatbot, not a search engine, not a legal database — a → Decision Intelligence Infrastructure.

### LDOS

**Legal Decision Operating System** (법률 의사결정 운영체제)

The formal system type designation. Lawmadi OS is an instance of an LDOS.

### Decision Intelligence Infrastructure

**의사결정 인텔리전스 인프라**

A system category that generates reproducible, verifiable decision outputs by assembling and validating live evidence from authoritative sources. Distinguished from "AI assistants" or "chatbots" by its deterministic processing, cryptographic integrity, and → Fail-Closed safety guarantees.

### Computable Trust

**계산 가능한 신뢰**

The ability to verify, reproduce, and cryptographically prove that a legal decision output was generated correctly from validated evidence, without requiring blind trust in the system. Lawmadi OS's ultimate design goal.

### "Convert Anxiety into Actionable Logic"

**"불안을 실행 가능한 논리로 전환하다"**

The Lawmadi OS tagline. Expresses the core mission: transforming legal uncertainty and anxiety into structured, evidence-based, actionable decision support.

---

## 2. Constitutional Principles

### SSOT (Single Source of Truth)

**단일 진실 공급원**

The principle that all legal evidence must originate from one designated authoritative source per jurisdiction (e.g., Korea's → DRF Open API). Permanent storage or replication of official legal datasets is prohibited. Every legal statement must be directly traceable to this source.

### Zero Inference

**제로 추론 원칙**

The principle that the system must never fabricate, guess, infer, estimate, or "fill in" any legal facts, citations, case numbers, statute references, dates, parties, amounts, or legal conclusions. If evidence is missing — ask for clarification or refuse output.

### Fail-Closed

**페일 클로즈드 정책**

A safety policy where the system immediately halts decision generation upon any verification failure (evidence retrieval, validation, temporal checks, integrity checks). The system returns a structured refusal rather than serving unverified legal conclusions. Safety over responsiveness.

### Live Evidence Architecture

**실시간 증거 아키텍처**

The architectural principle that legal decisions are generated from real-time validated evidence, not from stale, synced, or cached databases. Legislative amendments, appellate reversals, and new precedents are reflected immediately.

### Deterministic Runtime Boundary

**결정론적 런타임 경계**

The architectural boundary that confines the → LLM to a "rendering engine" role. The → Kernel owns all state transitions, evidence retrieval/validation, token generation, and policy enforcement. The LLM cannot bypass, override, or shortcut any Kernel-controlled process.

### Operating Constitution

**운영 헌법**

The set of non-negotiable principles (SSOT, Zero Inference, Fail-Closed, Live Evidence, Deterministic Runtime Boundary) that govern all technical and business decisions within Lawmadi OS. Enforced at runtime via → Constitution DSL.

---

## 3. Runtime & State Machine

### FSM (Finite State Machine)

**유한 상태 기계**

A computational model where the system exists in exactly one of a finite number of states at any time, transitioning between states according to deterministic rules. Lawmadi OS processes every decision session as a deterministic FSM.

### FSM State

**FSM 상태**

A discrete processing stage in the decision pipeline. The complete sequence:

| State | Description |
|-------|-------------|
| `INPUT_RECEIVED` | User query received |
| `INPUT_VALIDATED` | Input schema and format validated |
| `CASE_STRUCTURED` | Natural language converted to → CaseStructure |
| `ISSUE_IDENTIFIED` | Legal issues extracted into → IssueGraph |
| `LEADER_ROUTED` | Domain expert(s) selected via → Leader Swarm |
| `EVIDENCE_FETCHING` | Authoritative API queries in progress |
| `EVIDENCE_VALIDATED` | **Mandatory gate** — evidence verified |
| `DECISION_GRAPH_BUILT` | Formal → Decision Graph constructed |
| `TOKEN_MINTED` | → Decision Token created with hashes |
| `TOKEN_SIGNED` | Ed25519 signature applied |
| `RESPONSE_DELIVERED` | Strict JSON output delivered to user |
| `HALT` | System stopped due to verification failure |
| `FAIL_CLOSED_RESPONSE` | Structured refusal delivered |

### Happy Path

**정상 경로**

The complete FSM state sequence from `INPUT_RECEIVED` through `RESPONSE_DELIVERED` when all validations pass successfully.

### Fail-Closed Path

**페일 클로즈드 경로**

The FSM path triggered by any verification failure: → `HALT` → `FAIL_CLOSED_RESPONSE`. Possible triggers: `EVIDENCE_VALIDATION_FAILED`, `TEMPORAL_VALIDATION_FAILED`, `CONSTITUTION_VIOLATION`, `SOURCE_INTEGRITY_FAILURE`.

### Mandatory Gate

**필수 게이트**

The `EVIDENCE_VALIDATED` state — no output can be produced without passing through this state. The single most important safety mechanism in the FSM.

### Deterministic Processing

**결정론적 처리**

The guarantee that the same input, processed against the same evidence state, will always produce the same output. Enabled by the FSM architecture and → Reproducibility Trust Chain.

---

## 4. Kernel Engines

### Kernel

**커널**

The non-LLM deterministic core of Lawmadi OS. Controls all state transitions, evidence processing, policy enforcement, and cryptographic operations. The LLM operates under Kernel authority.

### Decision OS Kernel

**의사결정 OS 커널**

The central engine that orchestrates the entire decision pipeline: case structuring, FSM runtime management, and coordination of all other engines.

### Case Structure Parser

**사건 구조 파서**

Engine that converts natural language input into a structured → CaseStructure object, extracting parties, timeline, claims, and facts.

### CaseStructure

**사건 구조**

The canonical structured representation of a legal case:

```
CaseStructure {
  case_id          // Unique case identifier
  case_type        // Case type classification
  parties          // Parties information
  timeline         // Chronological sequence
  claim_object     // Claim target
  fact_vector      // Facts vector
}
```

### Issue Extraction Engine

**쟁점 추출 엔진**

Engine that analyzes a → CaseStructure to identify legal issues and construct an → IssueGraph with dependency relationships.

### IssueGraph

**쟁점 그래프**

A directed graph of legal issues and their dependencies:

```
IssueGraph {
  issue_nodes[]         // Legal issue nodes
  dependency_edges[]    // Inter-issue dependency edges
}
```

### Leader Swarm Routing Engine

**리더 스웜 라우팅 엔진**

Engine that routes cases to specialist legal domain experts based on a multi-factor scoring function. Supports → Multi-Leader Consensus for complex cases.

### Leader

**리더**

A modular prompt profile or specialist toolchain representing domain expertise in a specific area of law. Selected via → Routing Score.

### LeaderProfile

**리더 프로필**

The metadata schema for a Leader: `leader_id`, `specialization_domain`, `capability_tags`, `routing_weight`, `trust_score`, `supported_constitution_ver`, `dependency_modules`.

### Routing Score

**라우팅 점수**

The composite score used to select Leaders, incorporating domain match, historical accuracy, evidence dependency alignment, and trust score. Specific formula is proprietary.

### Multi-Leader Consensus

**멀티 리더 합의**

The process of combining judgments from multiple Leaders through three mechanisms: → Weighted Confidence Voting, → Decision Graph Merge, and → Fallback Leader Escalation.

### Weighted Confidence Voting

**가중 신뢰도 투표**

A consensus mechanism where multiple Leaders' judgments are aggregated by confidence weights.

### Decision Graph Merge

**의사결정 그래프 병합**

A consensus mechanism where → Decision Graphs from multiple Leaders are unified into a single coherent graph.

### Fallback Leader Escalation

**폴백 리더 에스컬레이션**

Automatic escalation to a senior or alternative Leader when the primary Leader fails or produces insufficient confidence.

### Constitution Validator

**헌법 검증기**

Engine that enforces → Constitution DSL rules at runtime, validating policy compliance at every stage of the decision pipeline.

### Constitution DSL

**헌법 도메인 특화 언어**

A Domain Specific Language that encodes the → Operating Constitution as executable rules enforced at runtime. Example rules include `Enforce_Source_Integrity`, `Validate_Effective_Date`, `Enforce_Decision_Completeness`.

### DSL (Domain Specific Language)

**도메인 특화 언어**

A programming language specialized for a particular application domain. Lawmadi's Constitution DSL is specialized for legal decision policy enforcement.

### Temporal Law Validity Engine

**시간적 법령 유효성 엔진**

Engine that validates whether legal authorities are currently in force, detecting: statute effective dates, precedent changes (appellate reversal, superior court changes), and unconstitutional/void provisions.

### Decision Graph Generator

**의사결정 그래프 생성기**

Engine that constructs formal semantic → Decision Graphs and generates visual decision tree representations.

---

## 5. Decision Graph

### Decision Graph

**의사결정 그래프**

A formal directed graph representing the logical structure of a legal decision. Contains typed nodes (→ Node Typology) connected by semantically labeled edges (→ Edge Semantics). Subject to → Graph Validity Condition.

### Node Typology

**노드 유형론**

The five types of nodes in a Decision Graph:

| Node | Korean | Description |
|------|--------|-------------|
| `FACT_NODE` | 사실관계 노드 | Objective facts from the case |
| `ISSUE_NODE` | 법적 쟁점 노드 | Legal issues requiring resolution |
| `LAW_NODE` | 법령 노드 | Applicable statute provisions |
| `PRECEDENT_NODE` | 판례 노드 | Relevant judicial precedents |
| `DECISION_NODE` | 의사결정 노드 | Final decision output |

### Edge Semantics

**엣지 의미론**

The eight types of edges connecting nodes in a Decision Graph:

| Edge | Korean | Meaning |
|------|--------|---------|
| `SUPPORTS` | 지지 | Provides grounds / backing |
| `CONTRADICTS` | 상충 | Conflicts with target node |
| `DEPENDS_ON` | 의존 | Prerequisite dependency |
| `RESOLVES` | 해결 | Issue resolution link |
| `REFERENCES` | 참조 | Reference link |
| `APPLIES` | 적용 | Statute applies to facts |
| `OVERRULES` | 번복 | Higher precedent overrules lower |
| `TEMPORAL_DEPENDS` | 시간적 의존 | Depends on effective date / amendment |

### Graph Validity Condition

**그래프 유효성 조건**

The mandatory rule: for every `ISSUE_NODE`, there must exist at least one `LAW_NODE` AND at least one `EVIDENCE_NODE` that `SUPPORTS` it. If not satisfied → decision rejected.

```
∀ ISSUE_NODE: ∃ LAW_NODE ∧ EVIDENCE_NODE that SUPPORTS it
```

---

## 6. Evidence & Trust

### Evidence

**증거**

A piece of legal information (statute, case law, regulation, guidance) retrieved from an authoritative official source, validated for integrity and temporal validity.

### evidence_set

**증거 세트**

The canonical data structure containing all evidence for a decision:

```
{
  "source_origin": "OFFICIAL_API",
  "items": [...],
  "missing": false,
  "evidence_hash": "sha256(hex)",
  "retrieved_at": "ISO-8601",
  "ttl_seconds": 600
}
```

### Evidence Processing Pipeline

**증거 처리 파이프라인**

The four-stage process: Authoritative API Query → Evidence Normalization → Temporal Validation → Evidence Hashing (SHA-256).

### Evidence Trust Score

**증거 신뢰도 점수**

A composite score evaluating evidence trustworthiness based on three conceptual components: source authority weight, citation stability score, and temporal consistency score. Specific formula is proprietary.

### Source Authority Weight

**출처 권위 가중치**

A component of → Evidence Trust Score measuring the authoritativeness of the evidence source.

### Citation Stability Score

**인용 안정성 점수**

A component of → Evidence Trust Score measuring how stable and consistent a legal citation has been over time.

### Temporal Consistency Score

**시간적 일관성 점수**

A component of → Evidence Trust Score measuring whether evidence remains consistent across temporal checks.

### Temporal Validity

**시간적 유효성**

The verification that a legal authority (statute, precedent, regulation) is currently in force at the relevant point in time. Includes effective date checks, repeal/amendment detection, and constitutional validity.

### "As-of" Validation

**기준일 검증**

Temporal validation against a specific date — either the current date or a user-specified historical/future date.

### Provenance Lineage Tracking

**출처 계보 추적**

The complete audit trail of evidence creation, modification, and validation history. Ensures full traceability of how evidence entered and was processed by the system.

### Reference-Only Mode

**참고용 모드**

A degraded output mode (when policy permits) where the system provides citations and references without generating legal conclusions. Used when evidence is available but cannot be fully validated.

---

## 7. Cryptographic Integrity

### Reproducibility Trust Chain

**재현성 신뢰 체인**

The cryptographic chain guaranteeing deterministic reproducibility: Input Hash → Evidence Hash Set → Decision Graph Hash → Decision Token Signature. Same input + same evidence state = same token.

### Decision Token

**의사결정 토큰**

The cryptographic artifact attached to every decision output, containing hashes and a signature that enable verification and reproducibility:

```
DecisionToken {
  decision_id, created_at, input_hash,
  constitution_version, drf_evidence_hash,
  decision_graph_hash, decision_graph_summary,
  digital_signature
}
```

### Evidence Hash

**증거 해시**

A SHA-256 hash computed over canonicalized evidence data (sorted keys, stable separators). Guarantees evidence integrity and enables tamper detection.

### Input Hash

**입력 해시**

A SHA-256 hash of the original user input query. Part of the → Reproducibility Trust Chain.

### Decision Graph Hash

**의사결정 그래프 해시**

A SHA-256 hash of the complete → Decision Graph structure. Part of the → Reproducibility Trust Chain.

### Digital Signature

**디지털 서명**

An Ed25519 signature applied to the → Decision Token for authenticity and non-repudiation. In production: hardware-backed via → KMS/HSM. In public builds: placeholder value.

### Ed25519

An elliptic-curve digital signature algorithm used by Lawmadi OS for → Decision Token signing. Chosen for speed, security, and deterministic signature generation.

### SHA-256

A cryptographic hash function producing a 256-bit digest. Used for → Evidence Hash, → Input Hash, and → Decision Graph Hash throughout the system.

---

## 8. Security

### Zero Trust Access Model

**제로 트러스트 접근 모델**

A security model where no component, user, or service is trusted by default. Every access request is verified regardless of origin. Applied to the → Core Layer.

### Gateway Protection

**게이트웨이 보호**

The security boundary at the system's entry point: input schema validation (JSON Schema), authentication/authorization (→ IAM), rate limiting, full audit logging, and output masking (PII redaction).

### Prompt Injection

**프롬프트 인젝션**

An attack where malicious user input attempts to override system instructions. Lawmadi OS defenses: user input treated as untrusted, "ignore previous instructions" patterns stripped, tool call allow-list enforced by Kernel.

### Tool Injection

**도구 인젝션**

An attack where malicious input attempts to trigger unauthorized tool calls. Defense: LLM may request tools, but Kernel validates all arguments and enforces the allow-list.

### Signature Boundary

**서명 경계**

The design principle that signing keys never reside inside the Kernel. They are held in external trust systems (→ KMS/HSM). Public builds use placeholder signatures.

### IAM (Identity and Access Management)

**신원 및 접근 관리**

The system for authenticating users and authorizing their access to specific resources and operations.

### Tamper-Evident

**위변조 감지**

A property of the audit log system: any modification to logged records is detectable. Achieved through append-only log architecture.

---

## 9. Data & Cache

### Ephemeral Cache

**임시 캐시**

Short-lived data storage (Redis or in-memory) with a TTL of 10–30 minutes maximum. Used purely for performance acceleration, never as a substitute for → SSOT evidence retrieval. Must be revalidated for temporal conditions.

### TTL (Time To Live)

**생존 시간**

The maximum duration that cached data remains valid before automatic expiration. Lawmadi OS enforces 10–30 minutes for evidence cache.

### Cache Key

**캐시 키**

The lookup identifier for cached data, computed as a canonical hash of the `query_struct`.

### config.json

**구성 파일**

The single configuration file that centrally controls all runtime parameters: API endpoints, cache TTL, feature flags, constitution version, etc. Functions as the configuration → SSOT.

### Case Decision Pattern Data

**사건 의사결정 패턴 데이터**

Proprietary strategic intelligence asset: aggregated patterns of case type → issue structure → selected legal authorities → decision flow → outcome pattern. This data is NOT statute/precedent data and IS permitted for permanent storage.

---

## 10. LLM Integration

### LLM (Large Language Model)

**대규모 언어 모델**

An AI language model (e.g., Claude, GPT, Gemini) used as a → Rendering Engine within the Lawmadi OS architecture. Operates under strict → Kernel control.

### Rendering Engine

**렌더링 엔진**

The designated role of the LLM within Lawmadi OS: formatting verified evidence and decision outputs into human-readable language. The LLM does NOT make decisions, validate evidence, or control state transitions.

### Model-Agnostic

**모델 비의존적**

The design principle that Lawmadi OS can integrate with any LLM that follows the → Integration Contracts, without dependency on specific model features.

### Integration Contracts

**통합 계약**

The nine contracts any LLM must satisfy:

| Contract | Purpose |
|----------|---------|
| Prompt Contract | System / Developer / User prompt rules |
| Tool Contract | Function calling schema |
| Evidence Contract | `evidence_set` schema + hashing |
| DecisionToken Contract | Token schema |
| Error Code Contract | Fail-Closed codes |
| Output Schema | Strict JSON format |
| Evaluation Harness | Testing requirements |
| Security Controls | Injection defense |
| Observability | Audit and metrics |

### Prompt Contract

**프롬프트 계약**

Rules governing system prompt, developer prompt, and user prompt handling. Defines required instructions, forbidden operations, and the principle that user content is always untrusted input.

### Tool Contract

**도구 계약**

The specification for function calling between the LLM and Kernel. Seven recommended tools: `fetch_evidence`, `validate_evidence`, `temporal_validate`, `build_decision_graph`, `mint_decision_token`, `sign_token`, `audit_log`.

### Adapter Layer

**어댑터 레이어**

A software layer that maps model-specific features (prompt format, function calling schema, streaming behavior, token limits) to the Lawmadi OS standard contracts. Enables → Model-Agnostic integration.

### Safe Streaming

**안전 스트리밍**

The policy that final legal conclusions must never be streamed before evidence validation. Allowed streaming: "working" status messages and clarifying questions. Final output must be atomic (complete JSON).

---

## 11. Output & Error Codes

### Success Response

**성공 응답**

A JSON output with `fail_closed: false`, containing: `request_id`, `fsm_state`, → Decision Token, summary, known/unknown facts, evidence citations, next actions, and disclaimer.

### Fail-Closed Response

**페일 클로즈드 응답**

A JSON output with `fail_closed: true`, containing: `request_id`, `fsm_state: "HALT"`, error `code`, human-readable message, the FSM stage where failure occurred, and `required_user_inputs` to unblock.

### Error Codes

**오류 코드**

Stable, semantic error identifiers:

| Code | Name | Korean | Meaning |
|------|------|--------|---------|
| `LC-001` | Evidence Unreachable | 증거 소스 연결 불가 | Authoritative source cannot be reached |
| `LC-002` | Evidence Mismatch | 증거 불일치 | Non-authoritative source, integrity failure |
| `LC-003` | Constitution Violation | 헌법 위반 | Invalid schema, missing required fields |
| `LC-004` | Temporal Invalidity | 시간적 무효 | Statute not effective, expired, or repealed |
| `LC-005` | Policy Restriction | 정책 제한 | Request in disallowed category |
| `LC-006` | Rate Limited | 속도 제한 | Throttled, retry after delay |

### Disclaimer

**면책 조항**

Standard text appended to every output:

> "본 답변은 일반 정보 제공 및 의사결정 지원 목적이며, 법률자문이 아닙니다. 구체적 사안은 사실관계에 따라 달라질 수 있으므로, 중요한 의사결정 전에는 전문가 상담을 권장합니다."

---

## 12. Infrastructure

### Cloud Run

**클라우드 런**

Google Cloud's containerized microservice platform used for Lawmadi OS deployment. Provides autoscaling and VPC isolation.

### VPC (Virtual Private Cloud)

**가상 사설 클라우드**

Network-level isolation for all system components, ensuring security boundaries between services.

### KMS (Key Management Service)

**키 관리 서비스**

A cloud service (e.g., Google Cloud KMS) providing hardware-backed key storage for → Ed25519 signing keys. Keys never leave the HSM boundary.

### HSM (Hardware Security Module)

**하드웨어 보안 모듈**

A dedicated cryptographic processor that safeguards signing keys. Used in production for → Digital Signature generation.

### Append-Only Audit Log

**추가 전용 감사 로그**

A tamper-resistant logging system where records can only be appended, never modified or deleted. Ensures complete traceability and → Tamper-Evident properties.

### Circuit Breaker

**회로 차단기**

A resilience pattern that prevents cascading failures: when a downstream service (e.g., authoritative API) fails repeatedly, the circuit "opens" and requests are immediately refused rather than queued.

### Decision Trace ID

**의사결정 추적 ID**

A unique identifier that traces the complete path of a decision through all FSM states, tool calls, and evidence operations. Enables full reproducibility and debugging.

---

## 13. Platform & Business

### Core Layer

**코어 레이어**

The innermost platform layer containing the closed proprietary kernel engine. Houses all IP and constitutional logic. Protected by → Zero Trust Access.

### Service Layer

**서비스 레이어**

The user-facing platform layer providing consultation AI, → Friendly Secretary UX, and case exploration. Has no access to Core internal logic.

### Partner / B2B Layer

**파트너 / B2B 레이어**

The institutional platform layer providing APIs for law firms, corporations, insurers, and government agencies: Decision Verification API, Evidence Validation API, Case Structuring API.

### Friendly Secretary UX

**친절한 비서 UX**

The user experience design philosophy for the → Service Layer: guiding users through legal situations with a warm, structured, step-by-step conversational interface rather than exposing raw system complexity.

---

## 14. Legal Domain

### DRF (Open Data API)

**국가법령정보센터 오픈 API**

The Korean National Law Information Center's public API providing access to statutes, precedents, and regulations. Lawmadi OS's designated → SSOT for Korean law.

### Statute

**법령 / 법률**

A law enacted by a legislative body. Represented as → LAW_NODE in the Decision Graph.

### Precedent

**판례**

A judicial decision that serves as authority for future cases. Represented as → PRECEDENT_NODE in the Decision Graph.

### Regulation

**규정 / 규칙**

A rule issued by a government agency to implement a statute.

### Effective Date

**시행일**

The date on which a statute or regulation comes into legal force. A critical input to → Temporal Validity checking.

### Repeal

**폐지**

The legislative act of revoking a statute, rendering it no longer in force. Detected by the → Temporal Law Validity Engine.

### Unconstitutional

**위헌**

A ruling by a constitutional court that a statute or provision violates the constitution, rendering it void. Detected by the → Temporal Law Validity Engine.

### Overrule

**번복 / 파기**

A higher court's reversal of a lower court's precedent. Represented by the `OVERRULES` edge in → Edge Semantics.

### Conflict of Law

**준거법 / 법률 충돌**

Rules determining which jurisdiction's law applies when multiple jurisdictions are involved. Must be explicitly modeled in the → Decision Graph for multi-jurisdiction operations.

---

## 15. Acronyms

| Acronym | Full Term | Korean |
|---------|-----------|--------|
| LDOS | Legal Decision Operating System | 법률 의사결정 운영체제 |
| FSM | Finite State Machine | 유한 상태 기계 |
| SSOT | Single Source of Truth | 단일 진실 공급원 |
| DSL | Domain Specific Language | 도메인 특화 언어 |
| DRF | Data Request Framework (National Law Info Center API) | 국가법령정보센터 API |
| LLM | Large Language Model | 대규모 언어 모델 |
| KMS | Key Management Service | 키 관리 서비스 |
| HSM | Hardware Security Module | 하드웨어 보안 모듈 |
| IAM | Identity and Access Management | 신원 및 접근 관리 |
| VPC | Virtual Private Cloud | 가상 사설 클라우드 |
| TTL | Time To Live | 생존 시간 |
| PII | Personally Identifiable Information | 개인 식별 정보 |
| API | Application Programming Interface | 응용 프로그램 인터페이스 |
| UX | User Experience | 사용자 경험 |
| B2B | Business to Business | 기업 간 거래 |
| DOI | Digital Object Identifier | 디지털 객체 식별자 |
| RAG | Retrieval-Augmented Generation | 검색 증강 생성 |
| SaaS | Software as a Service | 서비스형 소프트웨어 |
| IaC | Infrastructure as Code | 코드형 인프라 |
| CI/CD | Continuous Integration / Continuous Deployment | 지속적 통합 / 배포 |

---

## Document Cross-References

| Document | Relationship |
|----------|-------------|
| [INDEX.md](INDEX.md) | Master navigation hub |
| [OVERVIEW.md](OVERVIEW.md) | Plain-language introduction |
| [README.md](README.md) | Repository overview |
| [ARCHITECTURE.md](ARCHITECTURE.md) | Detailed architectural reference |
| [llms.txt](llms.txt) | Canonical LLM integration specification |
| [LICENSE.txt](LICENSE.txt) | Proprietary license terms |
| [CITATION.cff](CITATION.cff) | Citation metadata |

---

© 2026 Jainam Choe (최재남). All rights reserved.
