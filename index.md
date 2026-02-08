# Lawmadi OS — Repository Index

**Legal Decision Operating System (LDOS) · v2.0-Unified**
**Copyright © 2026 Jainam Choe (최재남). All rights reserved.**

---

## Quick Navigation

> **First time here?** Start with [OVERVIEW.md](OVERVIEW.md).
> **Developer / Evaluator?** Go to [README.md](README.md).
> **Architect / Engineer?** Read [ARCHITECTURE.md](ARCHITECTURE.md).
> **Building an LLM integration?** The canonical spec is [llms.txt](llms.txt).

---

## Document Map

### 📘 Orientation

| Document | Purpose | Audience | Read Time |
|----------|---------|----------|-----------|
| **[INDEX.md](INDEX.md)** | This file — master navigation hub | Everyone | 2 min |
| **[OVERVIEW.md](OVERVIEW.md)** | What Lawmadi OS is, why it matters, who it's for | Anyone (non-technical OK) | 8 min |
| **[README.md](README.md)** | Repository overview, quick start, tech summary | Developers, evaluators | 10 min |

### 🏗️ Architecture & Specification

| Document | Purpose | Audience | Read Time |
|----------|---------|----------|-----------|
| **[ARCHITECTURE.md](ARCHITECTURE.md)** | Detailed architectural reference with ASCII diagrams — platform layers, FSM, engines, pipelines, infrastructure | Architects, system engineers | 25 min |
| **[llms.txt](llms.txt)** | **Canonical reference.** Unified LLM Directive & Global Legal Decision Intelligence Standard — all principles, contracts, schemas, error codes, security, and testing requirements | LLMs, AI agents, integration developers | 40 min |
| **[docs/Whitepaper (PDF)](docs/)** | Public Technical Whitepaper v2.0 (Sanitized) — formal bilingual (KR/EN) document covering architecture, engines, security, data governance, global applicability, roadmap | Partners, investors, regulatory reviewers | 30 min |

### ⚖️ Legal & Citation

| Document | Purpose | Audience |
|----------|---------|----------|
| **[LICENSE.txt](LICENSE.txt)** | Comprehensive Proprietary License v2.0 — 14 IP categories, 60+ components, AI training prohibition, competitive use restrictions | Anyone using or referencing this repository |
| **[CITATION.cff](CITATION.cff)** | Machine-readable citation metadata (CFF 1.2.0) with preferred citation format, keywords, and cross-references | Researchers, academic/technical publications |

### 🔧 Runtime

| File | Purpose |
|------|---------|
| **[self_test.py](self_test.py)** | Local smoke test — run `python self_test.py` to verify basic kernel operation |
| **[PROGRAM_DESCRIPTION.txt](PROGRAM_DESCRIPTION.txt)** | Program description for IP submission |
| **[README_IP_Showcase.txt](README_IP_Showcase.txt)** | IP showcase documentation |

### 📁 Source Directories

| Directory | Contents | Public Status |
|-----------|----------|---------------|
| `kernel/` | Runtime FSM & coordinator | Sanitized |
| `constitution/` | Constitution rules & DSL validation engine | Sanitized |
| `decision/` | Decision engine, graph semantics, token generator | Sanitized |
| `evidence/` | Evidence builder, hashing, trust scoring scaffolds | Sanitized |
| `swarm/` | Leader routing concept modules | Sanitized |
| `temporal/` | Temporal law validity scaffolds | Sanitized |
| `security/` | Audit logger + signature interface boundary | Sanitized |
| `schemas/` | Canonical schemas (case / evidence / decision / token) | Sanitized |
| `core/` | Parser / extractor / tree builder scaffolds | Sanitized |
| `docs/` | Public whitepaper and supporting documents | Public |

---

## Reading Paths

Different readers need different paths through the documentation. Choose yours:

### 🟢 Path A: "I just want to understand what this is"

```
INDEX.md (you are here)
  └──> OVERVIEW.md               What & why, in plain language
         └──> docs/Whitepaper    Formal bilingual reference (optional)
```

### 🔵 Path B: "I want to evaluate the code"

```
INDEX.md (you are here)
  └──> README.md                 Quick start + repo layout
         ├──> self_test.py       Run the smoke test
         └──> ARCHITECTURE.md    Understand the design
                └──> llms.txt    Deep-dive into contracts & schemas
```

### 🟣 Path C: "I'm building an LLM integration"

```
INDEX.md (you are here)
  └──> llms.txt                  THE canonical spec (start here)
         ├──> ARCHITECTURE.md    Visual architecture reference
         └──> schemas/           Canonical data schemas
```

### 🟠 Path D: "I'm a partner / investor / regulator"

```
INDEX.md (you are here)
  └──> OVERVIEW.md               High-level value proposition
         └──> docs/Whitepaper    Formal reference document
                ├──> ARCHITECTURE.md    Technical depth (optional)
                └──> LICENSE.txt        IP protection terms
```

### 🔴 Path E: "I want to cite this work"

```
INDEX.md (you are here)
  └──> CITATION.cff              Machine-readable citation
         └──> LICENSE.txt        Attribution requirements (Section 8)
```

---

## System at a Glance

```
                    ┌──────────────────────────────┐
                    │         LAWMADI OS            │
                    │  Legal Decision Operating     │
                    │         System                │
                    └──────────────┬───────────────┘
                                   │
                 ┌─────────────────┼─────────────────┐
                 │                 │                 │
          ┌──────▼──────┐  ┌──────▼──────┐  ┌──────▼──────┐
          │   CORE      │  │  SERVICE    │  │  PARTNER    │
          │   LAYER     │  │  LAYER      │  │  / B2B      │
          │             │  │             │  │             │
          │ Decision    │  │ Consultation│  │ Verification│
          │ Kernel      │  │ AI          │  │ API         │
          │ Evidence    │  │ Friendly    │  │ Evidence    │
          │ Engine      │  │ Secretary   │  │ Validation  │
          │ Routing     │  │ UX          │  │ API         │
          │ Constitution│  │ Case        │  │ Case        │
          │ Temporal    │  │ Explorer    │  │ Structuring │
          │ Graph       │  │             │  │ API         │
          │ Crypto      │  │             │  │             │
          └─────────────┘  └─────────────┘  └─────────────┘
               Closed          Open UX         Controlled
            Proprietary      No Core Access     IAM + Audit
```

### Five Constitutional Principles

| # | Principle | One-Liner |
|---|-----------|-----------|
| 1 | **SSOT** | One source. The official one. Nothing else. |
| 2 | **Zero Inference** | If we don't have evidence, we don't say it. |
| 3 | **Fail-Closed** | Better to refuse than to guess wrong. |
| 4 | **Live Evidence** | The law changed today? We know. |
| 5 | **Deterministic Boundary** | AI writes words. The Kernel makes decisions. |

### Decision Flow

```
Input → Structure → Issues → Route → Fetch → Validate → Graph → Token → Sign → Deliver
                                                  │
                                              FAIL? → HALT → Refuse (with reason)
```

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| **v2.0-Unified** | 2026-02-08 | Unified all documents from whitepaper v3.0-Final + llms.txt v1.0 + index. Added: 5th constitutional principle (Deterministic Runtime Boundary), Decision Graph semantics, Evidence Trust Protocol, Constitution DSL rules, global multi-jurisdiction framework, output schema with LC-001–006, LLM integration contracts, ARCHITECTURE.md, OVERVIEW.md, INDEX.md, updated LICENSE v2.0 (14 IP categories), CITATION.cff v2.0. |
| v1.2 FINAL | 2026-01-27 | Original Decision Kernel release. README, llms.txt v1.0, LICENSE v1.0, CITATION.cff v1.0. |
| v1.0 | 2026-01 | Initial public/sanitized showcase. |

---

## Excluded from Public Repository

To protect security and trade secrets, this repository **does not contain**:

- Routing scoring formulas, weights, and exception handling
- Full Constitution DSL rule set
- Evidence Trust Score formulas
- Operational configs, endpoints, API keys, request patterns
- Deployment infrastructure (IaC, CI/CD, security policies)
- LLM provider routing logic
- Production data, user data, evaluation datasets
- KMS/HSM key material

See [Section 16 of ARCHITECTURE.md](ARCHITECTURE.md#16-non-public-assets) for the complete list.

---

## License

**Proprietary.** All technologies enumerated in [llms.txt](llms.txt) are protected under [LICENSE.txt](LICENSE.txt) — 14 IP categories covering 60+ proprietary components.

- ✅ Read, review, local non-production evaluation, academic citation
- ❌ Production use, redistribution, derivatives, AI/ML training, competitive use, commercial use

---

## Contact

**Jainam Choe (최재남)**
**Email:** choepeter@outlook.kr

For licensing, commercial permissions, partnership proposals, or technical inquiries.

---

© 2026 Jainam Choe (최재남). All rights reserved.

**Lawmadi OS** — Decision Intelligence Infrastructure for Computable Trust in Law.
**법률 의사결정을 위한 운영체제이며, 법률 영역에서 Computable Trust를 실현한다.**
