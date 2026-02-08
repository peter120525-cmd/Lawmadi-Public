# Lawmadi OS — Overview

**"Convert Anxiety into Actionable Logic."**
**"불안을 실행 가능한 논리로 전환하다"**

**Copyright © 2026 Jainam Choe (최재남). All rights reserved.**

---

## What Is Lawmadi OS?

Lawmadi OS is a **Legal Decision Operating System (LDOS)** — an engineering infrastructure that turns messy, anxiety-inducing legal situations into structured, verifiable, and reproducible decision outputs.

It is **not** a chatbot. **Not** a search engine. **Not** a legal database.

It is a **Decision Intelligence Infrastructure** built on a deterministic finite state machine (FSM) that assembles and validates **live evidence** from authoritative government sources before producing any legal decision output.

> **In one sentence:** Use verified evidence to generate traceable legal decisions — and if the evidence can't be verified, **refuse to answer** rather than guess.

---

## The Problem We Solve

Legal AI today is broken in a fundamental way:

| The Problem | What Happens | The Real Cost |
|------------|-------------|---------------|
| LLMs **hallucinate** legal citations | Users receive fake case numbers and statute references | Malpractice risk, sanctions, loss of trust |
| Systems rely on **stale databases** | Repealed statutes and overruled precedents get cited | Wrong legal advice, liability exposure |
| No way to **verify** AI outputs | Users can't trace how a conclusion was reached | "Black box" decisions with no accountability |
| **No safety net** when things go wrong | Systems serve best-guess answers even when uncertain | Dangerous half-truths in high-stakes situations |

Lawmadi OS was designed from the ground up to solve these problems — not by making a better chatbot, but by building a completely different kind of system.

---

## Five Constitutional Principles

Every decision Lawmadi OS makes is governed by five non-negotiable rules. These aren't suggestions — they're **hard-coded into the system runtime** and enforced automatically.

### 1. SSOT — Single Source of Truth

> *"One source. The official one. Nothing else."*

All legal evidence comes **only** from authoritative government APIs (e.g., Korea's National Law Information Center). No copied databases. No downloaded archives. No second-hand data. The system goes to the source, every time.

### 2. Zero Inference

> *"If we don't have evidence for it, we don't say it."*

The system **never** invents, guesses, or "fills in" legal facts. No hallucinated citations. No fabricated case numbers. No creative interpretation. Every legal statement has a verified evidence trail — or it doesn't exist in the output.

### 3. Fail-Closed

> *"Better to say 'I can't answer' than to say something wrong."*

If the evidence can't be retrieved, validated, or verified — the system **stops**. It doesn't serve a half-answer. It doesn't guess. It returns a clear, structured refusal that tells the user exactly what went wrong and what's needed to proceed.

### 4. Live Evidence

> *"The law changed this morning? We know."*

Decisions are built on **real-time evidence**, not yesterday's database snapshot. Legislative amendments, appellate reversals, and new precedents are reflected immediately. Cached data expires in minutes, not days.

### 5. Deterministic Runtime Boundary

> *"The AI writes words. The system makes decisions."*

The AI language model is just a **rendering engine** — it formats the output. The actual decision logic, evidence validation, state management, and cryptographic signing are all handled by the deterministic Kernel. The AI can't skip steps, override validations, or bypass safety checks.

---

## How It Works (The 30-Second Version)

```
You ask a legal question
        │
        ▼
System structures your case         ← Who, what, when, what's claimed
        │
        ▼
Identifies legal issues              ← What needs to be resolved
        │
        ▼
Routes to domain experts             ← Specialist knowledge applied
        │
        ▼
Fetches live evidence                 ← Real-time from official sources
        │
        ▼
Validates everything                  ← Is it current? Authentic? Complete?
        │
        ▼
   ┌────┴────┐
   │         │
PASS       FAIL
   │         │
   ▼         ▼
Builds    STOPS.
decision  Tells you why.
graph     Tells you what's
   │      needed.
   ▼
Signs with
crypto token
   │
   ▼
Delivers verified
decision output
```

**Every step is logged. Every output is traceable. Every decision is reproducible.**

---

## What Makes This Different

| | Traditional Legal AI | Lawmadi OS |
|---|---|---|
| **Data** | Stored/synced database | Live evidence from official APIs |
| **Freshness** | Periodic sync (hours to days) | Real-time + temporal validation |
| **When uncertain** | Serves best guess | **Refuses to answer** (Fail-Closed) |
| **Citations** | LLM-generated (often fake) | Verified from authoritative source |
| **Reproducibility** | Non-deterministic | Deterministic FSM + signed token |
| **Trust model** | "Trust us" | Cryptographic proof chain |
| **Identity** | Chatbot / Search engine | **Decision Operating System** |

---

## Key Technologies

### Decision Graph

Legal decisions are represented as formal directed graphs with strict validity rules. Every legal issue must be backed by at least one statute **and** one piece of verified evidence — or the decision is rejected.

### Evidence Trust Scoring

Evidence isn't just fetched — it's evaluated for trustworthiness based on source authority, citation stability, and temporal consistency.

### Temporal Law Validity Engine

Laws change over time. Lawmadi checks whether statutes are currently in force, detects overruled precedents, and identifies unconstitutional provisions — automatically.

### Leader Swarm Routing

Complex cases are routed to multiple specialist domain experts that collaborate through weighted consensus voting and graph merging.

### Cryptographic Reproducibility

Every decision output carries a **Decision Token** with SHA-256 evidence hashes and an Ed25519 digital signature. Same input + same evidence = same output. Verifiably.

### Constitution DSL

The system's operating rules aren't just documented — they're encoded as executable rules enforced at runtime. No loopholes. No exceptions.

---

## Who Is This For?

### Individuals & Small Businesses

Navigate legal situations with confidence. Get structured decision support instead of vague chatbot answers — and know exactly what evidence supports each conclusion.

### Law Firms & Legal Professionals

Augment your practice with verified evidence retrieval, temporal validity checks, and reproducible decision traces. Every output is auditable.

### Enterprises & Insurers

Integrate legal decision verification into your workflows via B2B APIs. Reduce legal risk with cryptographic proof chains and fail-closed safety guarantees.

### Government & Regulatory Bodies

Standardize legal decision support with authoritative-source-only evidence and full audit trails. No hallucinations. No stale data.

### Legal Tech Developers

Build on a model-agnostic platform. Any LLM that follows the integration contract can power the language layer — while the Kernel handles everything that matters for safety and trust.

---

## Platform Architecture (At a Glance)

```
┌─────────────────────────────────────────────┐
│           PARTNER / B2B LAYER               │
│     APIs for institutions & enterprises      │
├─────────────────────────────────────────────┤
│            SERVICE LAYER                     │
│    Consultation AI · Friendly Secretary UX   │
├─────────────────────────────────────────────┤
│             CORE LAYER                       │
│       (Closed Proprietary Kernel)            │
│                                              │
│  Decision Kernel · Evidence Engine           │
│  Leader Routing · Constitution Validator     │
│  Temporal Validity · Decision Graph          │
│  Crypto Integrity · Audit System             │
└─────────────────────────────────────────────┘
```

**Core** = the engine (proprietary, closed).
**Service** = the experience (user-facing).
**Partner** = the business (institutional APIs).

---

## Global Applicability

Lawmadi OS is built for the Korean legal system first, but the architecture is **jurisdiction-agnostic**. The principles work everywhere:

| Jurisdiction | Official Source |
|-------------|----------------|
| Korea | National Law Information Center (DRF) |
| United States | GovInfo, state legislature APIs, PACER |
| European Union | EUR-Lex |
| United Kingdom | legislation.gov.uk |
| Japan | e-Gov 法令検索 |

**One source of truth per jurisdiction. Zero inference. Fail-closed. Everywhere.**

---

## Development Roadmap

| Phase | What's Being Built |
|-------|--------------------|
| **Phase 1** | Decision OS Kernel — case structuring, routing, issue extraction, FSM runtime |
| **Phase 2** | Evidence Engine — temporal validity, trust protocol, crypto hashing, provenance tracking |
| **Phase 3** | Consultation AI — conversational interface, guided workflows |
| **Phase 4** | Education Platform — case study generation, decision logic visualization |
| **Future** | Formal mathematical models, blockchain-level provenance |

---

## Repository Guide

| File | What It Contains |
|------|-----------------|
| [`README.md`](README.md) | Repository overview and quick start |
| [`ARCHITECTURE.md`](ARCHITECTURE.md) | Detailed architectural reference with diagrams |
| [`llms.txt`](llms.txt) | Complete LLM integration specification (the canonical reference) |
| [`LICENSE.txt`](LICENSE.txt) | Comprehensive proprietary license |
| [`CITATION.cff`](CITATION.cff) | Citation metadata for academic/technical references |
| `docs/` | Public technical whitepaper (PDF) |
| `self_test.py` | Local smoke test |

---

## Try It Locally

```bash
# Requirements: Python 3.10+
python self_test.py
# Expected output: "Self test passed"
```

---

## License

**Proprietary.** This repository is provided for review, evaluation, and authorship proof only.

- ✅ Read, review, local non-production evaluation
- ✅ Academic citation with proper attribution
- ❌ Production use, redistribution, derivatives, AI/ML training, commercial use

See [`LICENSE.txt`](LICENSE.txt) for full terms.

---

## Citation

```
Choe, Jainam (최재남). "Lawmadi OS: Legal Decision Operating System —
Integrated Technical Whitepaper & Kernel Specification."
LDOS Reference Architecture v3.0. Lawmadi Project, February 2026.
```

---

## Contact

**Email:** choepeter@outlook.kr

For licensing inquiries, commercial permissions, or partnership proposals.

---

© 2026 Jainam Choe (최재남). All rights reserved.

**Lawmadi OS** — 법률 영역에서 Computable Trust를 실현하는 의사결정 운영체제.
