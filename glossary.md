# Lawmadi OS — Glossary / 용어집

<p align="left">
  <a href="https://doi.org/10.5281/zenodo.18525310">
    <img alt="DOI" src="https://zenodo.org/badge/DOI/10.5281/zenodo.18525310.svg" />
  </a>
  <img alt="glossary" src="https://img.shields.io/badge/glossary-v2.0--Unified-0ea5e9" />
  <img alt="repo" src="https://img.shields.io/badge/repo-v2.0.0-informational" />
  <img alt="classification" src="https://img.shields.io/badge/classification-public%20%2F%20sanitized-22c55e" />
  <img alt="license" src="https://img.shields.io/badge/license-all%20rights%20reserved-critical" />
</p>

**Legal Decision Operating System (LDOS) · v2.0-Unified**
**Copyright © 2026 Jainam Choe (최재남). All rights reserved.**

This glossary defines every technical term, acronym, and concept used across the Lawmadi OS documentation.
Terms are organized by domain and presented **bilingually (English / Korean)**.

> **Cross-references:** Entries marked with **→** refer to other glossary entries.
> **Tip:** Use GitHub page search: press **`t`** (file finder) and **`Ctrl/⌘ + F`** (in-page).

---

## Quick Links

<p align="left">
  <a href="./INDEX.md"><img alt="Quick Link: INDEX" src="https://img.shields.io/badge/Quick%20Link-INDEX-0ea5e9" /></a>
  <a href="./OVERVIEW.md"><img alt="Quick Link: OVERVIEW" src="https://img.shields.io/badge/Quick%20Link-OVERVIEW-0ea5e9" /></a>
  <a href="./README.md"><img alt="Quick Link: README" src="https://img.shields.io/badge/Quick%20Link-README-0ea5e9" /></a>
  <a href="./ARCHITECTURE.md"><img alt="Quick Link: ARCHITECTURE" src="https://img.shields.io/badge/Quick%20Link-ARCHITECTURE-0ea5e9" /></a>
  <a href="./llms.md"><img alt="Quick Link: llms.md" src="https://img.shields.io/badge/Quick%20Link-llms.md-2563eb" /></a>
  <a href="./llms.txt"><img alt="Quick Link: llms.txt" src="https://img.shields.io/badge/Quick%20Link-llms.txt-2563eb" /></a>
  <a href="./LICENSE"><img alt="Quick Link: LICENSE" src="https://img.shields.io/badge/Quick%20Link-LICENSE-ef4444" /></a>
  <a href="./CITATION.cff"><img alt="Quick Link: CITATION.cff" src="https://img.shields.io/badge/Quick%20Link-CITATION.cff-a855f7" /></a>
</p>

---

## Table of Contents (Foldable)

<details>
<summary><strong>Open / 펼치기</strong></summary>

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

</details>

---

## How to Use (Fast)

* **Search a term quickly:** `Ctrl/⌘ + F` on this page
* **Jump between terms:** look for **→ Cross-reference** arrows
* **Find docs that define behavior:** go to **`llms.md` / `ARCHITECTURE.md`**
* **Confirm binding rights/limits:** **`LICENSE` is the only legal authority**

---

## 1. Core Identity & Philosophy

<details>
<summary><strong>Expand / 펼치기</strong></summary>

### Lawmadi OS / 법률 의사결정 운영체제

The full system name. A deterministic, FSM-based Legal Decision Operating System.
Not a chatbot, not a search engine, not a legal database — a → **Decision Intelligence Infrastructure**.

### LDOS / Legal Decision Operating System (법률 의사결정 운영체제)

The formal system type designation. Lawmadi OS is an instance of an LDOS.

### Decision Intelligence Infrastructure / 의사결정 인텔리전스 인프라

A system category that generates reproducible, verifiable decision outputs by assembling and validating live evidence from authoritative sources.
Distinguished from “AI assistants” by deterministic processing, cryptographic integrity, and → **Fail-Closed** safety.

### Computable Trust / 계산 가능한 신뢰

The ability to verify, reproduce, and cryptographically prove that an output was generated correctly from validated evidence—without blind trust.

### “Convert Anxiety into Actionable Logic” / “불안을 실행 가능한 논리로 전환하다"

The Lawmadi OS tagline. Transform legal uncertainty into structured, evidence-based decision support.

<p align="right"><a href="#lawmadi-os--glossary--용어집">↑ Back to top</a></p>

</details>

---

## 2. Constitutional Principles

<details>
<summary><strong>Expand / 펼치기</strong></summary>

### SSOT (Single Source of Truth) / 단일 진실 공급원

All legal evidence must originate from **one designated authoritative source** per jurisdiction (e.g., Korea’s → **DRF Open API**).
Permanent storage/replication of official datasets is prohibited. Every legal statement must be traceable to SSOT.

### Zero Inference / 제로 추론 원칙

The system must never fabricate, guess, infer, estimate, or “fill in” legal facts, citations, case numbers, statute refs, dates, parties, amounts, or legal conclusions.
If evidence is missing: ask for clarification or refuse output.

### Fail-Closed / 페일 클로즈드 정책

If any verification fails (retrieval/validation/temporal/integrity), the system **halts** and returns a structured refusal. Safety over responsiveness.

### Live Evidence Architecture / 실시간 증거 아키텍처

Legal outputs are generated from **real-time validated evidence**, not stale synced DBs. Amendments/reversals/new precedents are reflected immediately.

### Deterministic Runtime Boundary / 결정론적 런타임 경계

The → **LLM** is strictly a rendering engine. The → **Kernel** owns state transitions, evidence validation, token generation, and policy enforcement.

### Operating Constitution / 운영 헌법

The non-negotiable principles (SSOT, Zero Inference, Fail-Closed, Live Evidence, Deterministic Boundary), enforced at runtime via → **Constitution DSL**.

<p align="right"><a href="#lawmadi-os--glossary--용어집">↑ Back to top</a></p>

</details>

---

## 3. Runtime & State Machine

<details>
<summary><strong>Expand / 펼치기</strong></summary>

### FSM (Finite State Machine) / 유한 상태 기계

A model where the system is always in exactly one state, transitioning deterministically.

### FSM State / FSM 상태

A discrete stage in the pipeline (example sequence):
`INPUT_RECEIVED → INPUT_VALIDATED → CASE_STRUCTURED → ISSUE_IDENTIFIED → LEADER_ROUTED → EVIDENCE_FETCHING → EVIDENCE_VALIDATED → DECISION_GRAPH_BUILT → TOKEN_MINTED → TOKEN_SIGNED → RESPONSE_DELIVERED`

### Happy Path / 정상 경로

The successful FSM sequence when all validations pass.

### Fail-Closed Path / 페일 클로즈드 경로

Failure path: `HALT → FAIL_CLOSED_RESPONSE` triggered by evidence/temporal/integrity/constitution violations.

### Mandatory Gate / 필수 게이트

`EVIDENCE_VALIDATED` — the hard gate that must be passed before any decision output.

### Deterministic Processing / 결정론적 처리

Same input + same evidence state → same output (enabled by FSM + → Reproducibility Trust Chain).

<p align="right"><a href="#lawmadi-os--glossary--용어집">↑ Back to top</a></p>

</details>

---

## 4. Kernel Engines

<details>
<summary><strong>Expand / 펼치기</strong></summary>

### Kernel / 커널

The non-LLM deterministic core. Controls state transitions, evidence processing, enforcement, cryptography.

### Decision OS Kernel / 의사결정 OS 커널

Orchestrates the pipeline: structuring → routing → evidence → graph → token → output.

### Case Structure Parser / 사건 구조 파서

Converts natural language into → **CaseStructure** (parties/timeline/claims/facts).

### CaseStructure / 사건 구조

Canonical structured case representation:

```text
CaseStructure {
  case_id
  case_type
  parties
  timeline
  claim_object
  fact_vector
}
```

### Issue Extraction Engine / 쟁점 추출 엔진

Builds → **IssueGraph** from a CaseStructure.

### IssueGraph / 쟁점 그래프

```text
IssueGraph {
  issue_nodes[]
  dependency_edges[]
}
```

### Leader Swarm Routing Engine / 리더 스웜 라우팅 엔진

Routes cases to specialist Leaders (scoring formula proprietary). Supports → Multi-Leader Consensus.

### Leader / 리더

A modular specialist profile/toolchain for a legal domain. Selected via routing.

### LeaderProfile / 리더 프로필

Leader metadata schema (weights/formulas proprietary; description only in public builds).

### Constitution Validator / 헌법 검증기

Enforces → Constitution DSL at runtime.

### Constitution DSL / 헌법 도메인 특화 언어

Executable policy rules (e.g., source integrity, effective date checks, decision completeness).

### Temporal Law Validity Engine / 시간적 법령 유효성 엔진

Validates in-force status: effective dates, repeal/amendment, overrule, unconstitutional/void detection.

### Decision Graph Generator / 의사결정 그래프 생성기

Constructs the formal → Decision Graph and produces its canonical structure/hashes.

<p align="right"><a href="#lawmadi-os--glossary--용어집">↑ Back to top</a></p>

</details>

---

## 5. Decision Graph

<details>
<summary><strong>Expand / 펼치기</strong></summary>

### Decision Graph / 의사결정 그래프

A formal directed graph representing the logic of a decision, with typed nodes and labeled edges.

### Node Typology / 노드 유형론

* `FACT_NODE` / 사실관계 노드
* `ISSUE_NODE` / 법적 쟁점 노드
* `LAW_NODE` / 법령 노드
* `PRECEDENT_NODE` / 판례 노드
* `DECISION_NODE` / 의사결정 노드

### Edge Semantics / 엣지 의미론

* `SUPPORTS` / 지지
* `CONTRADICTS` / 상충
* `DEPENDS_ON` / 의존
* `RESOLVES` / 해결
* `REFERENCES` / 참조
* `APPLIES` / 적용
* `OVERRULES` / 번복
* `TEMPORAL_DEPENDS` / 시간적 의존

### Graph Validity Condition / 그래프 유효성 조건

For every `ISSUE_NODE`, there must exist at least one `LAW_NODE` **and** at least one `EVIDENCE_NODE` that supports it. Otherwise, decision rejected.

```text
∀ ISSUE_NODE: ∃ LAW_NODE ∧ EVIDENCE_NODE that SUPPORTS it
```

<p align="right"><a href="#lawmadi-os--glossary--용어집">↑ Back to top</a></p>

</details>

---

## 6. Evidence & Trust

<details>
<summary><strong>Expand / 펼치기</strong></summary>

### Evidence / 증거

Legal information (statute/case/regulation/guidance) retrieved from authoritative official sources and validated.

### evidence_set / 증거 세트

Canonical evidence structure:

```json
{
  "source_origin": "OFFICIAL_API",
  "items": [],
  "missing": false,
  "evidence_hash": "sha256(hex)",
  "retrieved_at": "ISO-8601",
  "ttl_seconds": 600
}
```

### Evidence Processing Pipeline / 증거 처리 파이프라인

Authoritative API Query → Normalization → Temporal Validation → SHA-256 Hashing

### Evidence Trust Score / 증거 신뢰도 점수

Conceptual composite score (formula proprietary): source authority + citation stability + temporal consistency.

### Temporal Validity / 시간적 유효성

Whether authority is in force at “as-of” time (effective date, repeal, overrule, unconstitutional, etc).

### “As-of” Validation / 기준일 검증

Temporal validation against a specific date (now or user-specified).

### Provenance Lineage Tracking / 출처 계보 추적

Audit trail of how evidence was fetched/validated/used.

### Reference-Only Mode / 참고용 모드

Policy-permitted degraded mode that provides citations only (no conclusions).

<p align="right"><a href="#lawmadi-os--glossary--용어집">↑ Back to top</a></p>

</details>

---

## 7. Cryptographic Integrity

<details>
<summary><strong>Expand / 펼치기</strong></summary>

### Reproducibility Trust Chain / 재현성 신뢰 체인

Input Hash → Evidence Hash → Decision Graph Hash → Decision Token Signature
Same input + same evidence state = same token.

### Decision Token / 의사결정 토큰

Cryptographic artifact attached to outputs (hashes + signature):

```text
DecisionToken {
  decision_id, created_at, input_hash,
  constitution_version, evidence_hash,
  decision_graph_hash, decision_graph_summary,
  digital_signature
}
```

### Evidence Hash / 증거 해시

SHA-256 over canonical evidence data. Enables tamper detection.

### Input Hash / 입력 해시

SHA-256 of original user input.

### Decision Graph Hash / 의사결정 그래프 해시

SHA-256 of the decision graph structure.

### Digital Signature / 디지털 서명

Ed25519 signature over token payload. Production: via → KMS/HSM. Public: placeholder allowed by policy.

### Ed25519

Signature algorithm used for token signing (fast, secure).

### SHA-256

Hash function used throughout for integrity.

<p align="right"><a href="#lawmadi-os--glossary--용어집">↑ Back to top</a></p>

</details>

---

## 8. Security

<details>
<summary><strong>Expand / 펼치기</strong></summary>

### Zero Trust Access Model / 제로 트러스트 접근 모델

No component is trusted by default; every request is verified.

### Gateway Protection / 게이트웨이 보호

Entry security: JSON Schema validation, auth, rate limiting, audit logging, output masking.

### Prompt Injection / 프롬프트 인젝션

Attack that tries to override instructions. Defense: user input treated as untrusted; allow-list tool calls; Kernel-enforced FSM.

### Tool Injection / 도구 인젝션

Attack that attempts unauthorized tool execution. Defense: Kernel validates all tool calls and arguments.

### Signature Boundary / 서명 경계

Signing keys never reside in Kernel; held in external trust systems (KMS/HSM).

### IAM / 신원 및 접근 관리

Authentication/authorization system.

### Tamper-Evident / 위변조 감지

Audit log property: modifications are detectable (append-only).

<p align="right"><a href="#lawmadi-os--glossary--용어집">↑ Back to top</a></p>

</details>

---

## 9. Data & Cache

<details>
<summary><strong>Expand / 펼치기</strong></summary>

### Ephemeral Cache / 임시 캐시

Short-lived cache (Redis/in-memory) with TTL 10–30 minutes max; acceleration only, never SSOT replacement.

### TTL (Time To Live) / 생존 시간

Max time cached data is valid before expiration.

### Cache Key / 캐시 키

Lookup identifier computed as canonical hash of query structure.

### config.json / 구성 파일

Single configuration SSOT controlling runtime (endpoints, TTL, flags, constitution version).

### Case Decision Pattern Data / 사건 의사결정 패턴 데이터

Proprietary pattern intelligence (not statute/precedent text). Allowed for storage when non-reconstructive.

<p align="right"><a href="#lawmadi-os--glossary--용어집">↑ Back to top</a></p>

</details>

---

## 10. LLM Integration

<details>
<summary><strong>Expand / 펼치기</strong></summary>

### LLM (Large Language Model) / 대규모 언어 모델

Used strictly as → Rendering Engine under Kernel authority.

### Rendering Engine / 렌더링 엔진

LLM formats verified evidence & outputs into human-readable language. No decision-making, no validation, no state control.

### Model-Agnostic / 모델 비의존적

Any LLM can integrate if it follows the contracts.

### Integration Contracts / 통합 계약

Required contracts: Prompt / Tool / Evidence / Token / Error Codes / Output Schema / Security / Observability / Evaluation harness.

### Adapter Layer / 어댑터 레이어

Maps model-specific formats (function calling, streaming, limits) to Lawmadi contracts.

### Safe Streaming / 안전 스트리밍

Never stream final conclusions before evidence validation. Final output should be atomic (complete JSON).

<p align="right"><a href="#lawmadi-os--glossary--용어집">↑ Back to top</a></p>

</details>

---

## 11. Output & Error Codes

<details>
<summary><strong>Expand / 펼치기</strong></summary>

### Success Response / 성공 응답

Strict JSON output containing request id, fsm_state, token, evidence citations, summary, disclaimer.

### Fail-Closed Response / 페일 클로즈드 응답

Strict JSON refusal including code, stage, required_user_inputs.

### Error Codes / 오류 코드

Stable identifiers:

* `LC-001` Evidence Unreachable / 증거 소스 연결 불가
* `LC-002` Evidence Mismatch / 증거 불일치
* `LC-003` Constitution Violation / 헌법 위반(스키마/필수 사실 누락 포함)
* `LC-004` Temporal Invalidity / 시간적 무효
* `LC-005` Policy Restriction / 정책 제한
* `LC-006` Rate Limited / 속도 제한

### Disclaimer / 면책 조항

Standard disclaimer appended to every output.

<p align="right"><a href="#lawmadi-os--glossary--용어집">↑ Back to top</a></p>

</details>

---

## 12. Infrastructure

<details>
<summary><strong>Expand / 펼치기</strong></summary>

### Cloud Run / 클라우드 런

Containerized microservice platform used for deployment (autoscaling, isolation).

### VPC / 가상 사설 클라우드

Network isolation for security boundaries.

### KMS / 키 관리 서비스

Hardware-backed key storage for signing keys.

### HSM / 하드웨어 보안 모듈

Dedicated cryptographic processor safeguarding keys.

### Append-Only Audit Log / 추가 전용 감사 로그

Records can be appended only; tamper-evident.

### Circuit Breaker / 회로 차단기

Resilience pattern to avoid cascading failures.

### Decision Trace ID / 의사결정 추적 ID

Unique ID tracing an execution across FSM, tools, evidence, outputs.

<p align="right"><a href="#lawmadi-os--glossary--용어집">↑ Back to top</a></p>

</details>

---

## 13. Platform & Business

<details>
<summary><strong>Expand / 펼치기</strong></summary>

### Core Layer / 코어 레이어

Closed proprietary kernel layer containing IP & constitutional enforcement.

### Service Layer / 서비스 레이어

User-facing UX layer; no access to Core internal logic.

### Partner / B2B Layer / 파트너·기관 서비스 레이어

Institutional APIs (verification/validation/case structuring), governed by IAM and audit.

### Friendly Secretary UX / 친절한 비서 UX

Guided, structured, step-by-step experience for non-experts.

<p align="right"><a href="#lawmadi-os--glossary--용어집">↑ Back to top</a></p>

</details>

---

## 14. Legal Domain

<details>
<summary><strong>Expand / 펼치기</strong></summary>

### DRF (Open Data API) / 국가법령정보센터 오픈 API

Designated SSOT for Korean law evidence retrieval.

### Statute / 법령·법률

Law enacted by legislature (→ LAW_NODE).

### Precedent / 판례

Judicial decision used as authority (→ PRECEDENT_NODE).

### Regulation / 규정·규칙

Agency rules implementing statutes.

### Effective Date / 시행일

Date a statute/regulation comes into force (key for temporal validity).

### Repeal / 폐지

Revocation of a statute (no longer in force).

### Unconstitutional / 위헌

Constitutional invalidation rendering a provision void.

### Overrule / 번복·파기

Higher court reversal (→ `OVERRULES` edge).

### Conflict of Law / 준거법·법률 충돌

Which jurisdiction’s law applies in multi-jurisdiction cases.

<p align="right"><a href="#lawmadi-os--glossary--용어집">↑ Back to top</a></p>

</details>

---

## 15. Acronyms

<details>
<summary><strong>Expand / 펼치기</strong></summary>

* **LDOS** — Legal Decision Operating System / 법률 의사결정 운영체제
* **FSM** — Finite State Machine / 유한 상태 기계
* **SSOT** — Single Source of Truth / 단일 진실 공급원
* **DSL** — Domain Specific Language / 도메인 특화 언어
* **DRF** — National Law Info Center API / 국가법령정보센터 API
* **LLM** — Large Language Model / 대규모 언어 모델
* **KMS** — Key Management Service / 키 관리 서비스
* **HSM** — Hardware Security Module / 하드웨어 보안 모듈
* **IAM** — Identity and Access Management / 신원 및 접근 관리
* **VPC** — Virtual Private Cloud / 가상 사설 클라우드
* **TTL** — Time To Live / 생존 시간
* **PII** — Personally Identifiable Information / 개인 식별 정보
* **RAG** — Retrieval-Augmented Generation / 검색 증강 생성
* **IaC** — Infrastructure as Code / 코드형 인프라
* **CI/CD** — Continuous Integration / Deployment / 지속적 통합·배포

<p align="right"><a href="#lawmadi-os--glossary--용어집">↑ Back to top</a></p>

</details>

---

## Document Cross-References

<p align="left">
  <a href="./INDEX.md"><img alt="INDEX" src="https://img.shields.io/badge/INDEX-navigation-0ea5e9" /></a>
  <a href="./OVERVIEW.md"><img alt="OVERVIEW" src="https://img.shields.io/badge/OVERVIEW-intro-0ea5e9" /></a>
  <a href="./README.md"><img alt="README" src="https://img.shields.io/badge/README-repo%20overview-0ea5e9" /></a>
  <a href="./ARCHITECTURE.md"><img alt="ARCHITECTURE" src="https://img.shields.io/badge/ARCHITECTURE-reference-0ea5e9" /></a>
  <a href="./llms.md"><img alt="llms.md" src="https://img.shields.io/badge/llms.md-canonical%20spec-2563eb" /></a>
  <a href="./LICENSE"><img alt="LICENSE" src="https://img.shields.io/badge/LICENSE-legal%20authority-ef4444" /></a>
  <a href="./CITATION.cff"><img alt="CITATION.cff" src="https://img.shields.io/badge/CITATION.cff-cite-a855f7" /></a>
</p>

---

© 2026 Jainam Choe (최재남). All rights reserved.
