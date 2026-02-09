# Lawmadi OS — Repository Index

**Legal Decision Operating System (LDOS) · v2.0-Unified**
**Copyright © 2026 Jainam Choe (최재남). All rights reserved.**

---

## Quick Navigation

> **First time here?** Start with [OVERVIEW.md](OVERVIEW.md).
> **Developer / Evaluator?** Go to [README.md](README.md).
> **Architect / Engineer?** Read [ARCHITECTURE.md](ARCHITECTURE.md).
> **Building an LLM integration?** The canonical spec is [llms.txt](llms.txt).
> **Looking up a term?** See [GLOSSARY.md](GLOSSARY.md).
> **Setting up a runtime?** Start with [minimal_config.json](minimal_config.json).

---

## Document Map

### 📘 Orientation

| Document | Purpose | Audience | Read Time |
|----------|---------|----------|-----------|
| **[INDEX.md](INDEX.md)** | This file — master navigation hub | Everyone | 3 min |
| **[OVERVIEW.md](OVERVIEW.md)** | What Lawmadi OS is, why it matters, who it's for | Anyone (non-technical OK) | 8 min |
| **[README.md](README.md)** | Repository overview, quick start, tech summary | Developers, evaluators | 10 min |
| **[GLOSSARY.md](GLOSSARY.md)** | Comprehensive bilingual glossary — 100+ terms across 15 domains | Everyone | Reference |

### 🏗️ Architecture & Specification

| Document | Purpose | Audience | Read Time |
|----------|---------|----------|-----------|
| **[ARCHITECTURE.md](ARCHITECTURE.md)** | Detailed architectural reference with ASCII diagrams — platform layers, FSM, engines, pipelines, infrastructure | Architects, system engineers | 25 min |
| **[llms.txt](llms.txt)** | **Canonical reference.** Unified LLM Directive & Global Legal Decision Intelligence Standard — all principles, contracts, schemas, error codes, security, and testing requirements | LLMs, AI agents, integration developers | 40 min |
| **[docs/Whitepaper (PDF)](docs/)** | Public Technical Whitepaper v2.0 (Sanitized) — formal bilingual (KR/EN) document covering architecture, engines, security, data governance, global applicability, roadmap | Partners, investors, regulatory reviewers | 30 min |

### ⚙️ Configuration & Schemas

| Document | Purpose | Audience |
|----------|---------|----------|
| **[config.schema.json](config.schema.json)** | JSON Schema (Draft 2020-12) defining all 15 configurable sections of the runtime — constitution enforcement, FSM, evidence, temporal, graph, token, routing, cache, security, gateway, observability, output, LLM integration, safety | Developers, DevOps, integrators |
| **[minimal_config.json](minimal_config.json)** | Copy-paste-ready minimal configuration example conforming to the schema — public-sandbox defaults, all constitutional constraints enforced, PLACEHOLDER signatures, SECRET: references for production values | Developers, evaluators |

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

## Complete File Inventory

All public repository files at a glance:

```
Lawmadi-Public/
│
├── INDEX.md                    ← You are here (master navigation)
├── OVERVIEW.md                 ← What & why (plain language)
├── README.md                   ← Repo overview & quick start
├── GLOSSARY.md                 ← 100+ terms, 15 domains, bilingual
├── ARCHITECTURE.md             ← Detailed design with diagrams
├── llms.txt                    ← Canonical LLM integration spec
│
├── config.schema.json          ← Runtime config JSON Schema
├── minimal_config.json         ← Copy-paste config example
│
├── LICENSE.txt                 ← Proprietary license (14 IP categories)
├── CITATION.cff                ← Citation metadata
│
├── self_test.py                ← Local smoke test
├── PROGRAM_DESCRIPTION.txt     ← IP submission description
├── README_IP_Showcase.txt      ← IP showcase documentation
│
├── Lawmadi_OS_Public_Technical_Whitepaper_v2_0_Sanitized.pdf
│
├── kernel/                     ← FSM & coordinator (sanitized)
├── constitution/               ← DSL rules & validation (sanitized)
├── decision/                   ← Graph, token generator (sanitized)
├── evidence/                   ← Hashing, trust scoring (sanitized)
├── swarm/                      ← Leader routing (sanitized)
├── temporal/                   ← Temporal validity (sanitized)
├── security/                   ← Audit, signature boundary (sanitized)
├── schemas/                    ← Canonical data schemas (sanitized)
├── core/                       ← Parser, extractor (sanitized)
└── docs/                       ← Whitepaper & supporting docs
```

---

## Reading Paths

Different readers need different paths through the documentation. Choose yours:

### 🟢 Path A: "I just want to understand what this is"

```
INDEX.md (you are here)
  └──> OVERVIEW.md               What & why, in plain language
         └──> docs/Whitepaper    Formal bilingual reference (optional)
                └──> GLOSSARY.md Look up any unfamiliar term
```

### 🔵 Path B: "I want to evaluate the code"

```
INDEX.md (you are here)
  └──> README.md                 Quick start + repo layout
         ├──> self_test.py       Run the smoke test
         ├──> minimal_config.json  See the runtime config
         └──> ARCHITECTURE.md    Understand the design
                └──> llms.txt    Deep-dive into contracts & schemas
```

### 🟣 Path C: "I'm building an LLM integration"

```
INDEX.md (you are here)
  └──> llms.txt                  THE canonical spec (start here)
         ├──> config.schema.json Full config schema reference
         ├──> minimal_config.json Copy-paste starting point
         ├──> ARCHITECTURE.md    Visual architecture reference
         ├──> schemas/           Canonical data schemas
         └──> GLOSSARY.md        Term reference
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

### 🟡 Path F: "I'm configuring or deploying the system"

```
INDEX.md (you are here)
  └──> config.schema.json        Full schema with all 15 sections
         └──> minimal_config.json  Copy-paste baseline config
                ├──> ARCHITECTURE.md § Infrastructure  Deployment topology
                └──> llms.txt § Tool Contract          Required tools
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

## Configuration Quick Reference

The runtime is controlled by a single `config.json` (Configuration SSOT). Key sections:

| Section | Controls | Constitutional Constraints |
|---------|----------|--------------------------|
| `constitution` | 5 principles enforcement | All `const: true` — cannot disable |
| `fsm` | State sequence, timeouts | `mandatory_gate: EVIDENCE_VALIDATED` fixed |
| `evidence` | SSOT sources, pipeline, integrity | `reject_non_official_source: true` fixed |
| `temporal` | Validity checks, unknown status action | `enabled: true` fixed |
| `decision_graph` | Node/edge types, validity condition | `validity_condition_enabled: true` fixed |
| `decision_token` | Signature algorithm, key source | `Ed25519` fixed, key in KMS/HSM |
| `leader_swarm` | Concurrent leaders, consensus method | Weights proprietary |
| `cache` | Backend, TTL, revalidation | Max 1800s (30 min constitutional limit) |
| `security` | Injection defense, secret management | `secrets_in_prompts: false` fixed |
| `gateway` | Rate limiting, auth, input validation | `audit_logging: true` fixed |
| `observability` | Audit log, metrics, trace | `append_only: true` fixed |
| `output` | Format, error codes, disclaimer, streaming | `atomic_final_output: true` fixed |
| `llm_integration` | LLM role, contracts, adapter | `role: rendering_engine` fixed |
| `safety` | Operating mode, compliance | `informational_decision_support` fixed |

→ Full schema: [config.schema.json](config.schema.json)
→ Ready-to-use example: [minimal_config.json](minimal_config.json)

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| **v2.0-Unified** | 2026-02-09 | Added: GLOSSARY.md (100+ terms, 15 domains, bilingual), config.schema.json (JSON Schema Draft 2020-12, 15 configurable sections), minimal_config.json (copy-paste config). Updated INDEX.md with complete file inventory, configuration quick reference, and Path F for deployers. |
| v2.0-Unified | 2026-02-08 | Unified all documents from whitepaper v3.0-Final + llms.txt v1.0 + index. Added: 5th constitutional principle (Deterministic Runtime Boundary), Decision Graph semantics, Evidence Trust Protocol, Constitution DSL rules, global multi-jurisdiction framework, output schema with LC-001–006, LLM integration contracts, ARCHITECTURE.md, OVERVIEW.md, INDEX.md, updated LICENSE v2.0 (14 IP categories), CITATION.cff v2.0, Public Whitepaper PDF v2.0. |
| v1.2 FINAL | 2026-01-27 | Original Decision Kernel release. README, llms.txt v1.0, LICENSE v1.0, CITATION.cff v1.0. |
| v1.0 | 2026-01 | Initial public/sanitized showcase. |

---

## Excluded from Public Repository

To protect security and trade secrets, this repository **does not contain**:

- Routing scoring formulas, weights, and exception handling
- Full Constitution DSL rule set and exception logic
- Evidence Trust Score specific formulas and weights
- Operational configs, endpoints, API keys, request patterns
- Deployment infrastructure (IaC, CI/CD, security policies)
- LLM provider routing logic
- Production data, user data, evaluation datasets
- KMS/HSM key material and production signature configurations

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
