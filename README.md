# Lawmadi OS — Decision Kernel (Public/Sanitized)  
**v1.2 FINAL (Author: 최재남 / Jainam Choe)**  
**“Convert Anxiety into Actionable Logic.”**

> ✅ This package is a **public, sanitized showcase** of the **deterministic Decision Kernel** of a Legal Decision Operating System (LDOS).  
> 🚫 It is **NOT open source** and is provided for **review/evaluation/authorship proof** (see `LICENSE`).

---

## What this is

**Lawmadi OS Decision Kernel** is the *runtime core* that:

- Structures an input query into a case representation
- Enforces the Lawmadi Constitution:
  - **SSOT** (evidence must be authoritative)
  - **Zero-Inference** (no invented legal facts/citations)
  - **Fail-Closed** (refuse conclusions when verification fails)
- Builds a decision-flow summary (graph concept)
- Mints a **Decision Token** (reproducibility + integrity hashes)
- Provides a **signature boundary interface** (KMS/HSM in production; placeholder in public build)

---

## What is included (public/sanitized)

- Deterministic runtime modules (FSM-oriented flow)
- Constitution rule evaluation (concept-level)
- Evidence hashing and integrity pipeline (concept-level)
- Decision token minting (reproducibility scaffold)
- Audit logging scaffold
- **Signature interface** (`security/signature_interface.py`)  
  - Shows **input/output contract** while keeping real KMS keys and configs private
- `self_test.py` to demonstrate local execution
- Integration playbook for any LLM: `llms.txt`
- Citation metadata: `CITATION.cff`
- Proprietary license: `LICENSE`
- Program description files for submission: `PROGRAM_DESCRIPTION.txt`, `README_IP_Showcase.txt`

---

## What is excluded (intentionally)

To protect security and trade secrets, this package does **not** include:

- Production deployment configs (Cloud Run, VPC, IAM, CI/CD)
- Real API keys / endpoints / request patterns
- Proprietary scoring formulas, routing weights, or full leader policy logic
- Full connectors to external legal-data systems (only interface-level scaffolding)
- Any persistent legal database replication logic

---

## Core guarantees (non-negotiable)

1. **SSOT**: All legal evidence must originate from authoritative sources.  
2. **Zero-Inference**: Never fabricate statutes, cases, dates, parties, or citations.  
3. **Fail-Closed**: If evidence cannot be verified → **refuse to conclude**.  
4. **Deterministic boundary**: Kernel controls state transitions; LLM is a renderer only.

For the complete LLM-agnostic integration spec, see: **`llms.txt`**.

---

## Repository layout (high-level)

```
kernel/         Runtime FSM & coordinator
constitution/   Constitution rules & validation engine
decision/       Decision engine, graph summary, token generator
evidence/       Evidence builder (sanitized), hashing, citation scaffolds
swarm/          Routing concept modules (sanitized)
temporal/       Temporal validity scaffolds
security/       Audit logger + signature interface boundary
schemas/        Canonical schemas (case/evidence/decision/token)
core/           Parser/extractor/tree builder scaffolds
self_test.py    Local smoke test
llms.txt        Model-agnostic LLM integration playbook
CITATION.cff    Citation metadata
LICENSE         Proprietary license (evaluation-only)
```

---

## Quick start (local)

### Requirements
- Python 3.10+ recommended

### Run the smoke test
From the project root:

```bash
python self_test.py
```

Expected output:

```
Self test passed
```

> If you see import errors, ensure you are running from the repository root.

---

## Output contract (public/sanitized)

Kernel-aligned responses should follow a strict JSON schema with two modes:

### Success
- `fail_closed: false`
- includes `decision_token` with hashes and (placeholder) signature

### Fail-Closed
- `fail_closed: true`
- includes stable error `code` (e.g., `LC-001`..`LC-006`)
- lists `required_user_inputs` to unblock

See: `llms.txt` → **Output Schema** section.

---

## Whitepaper (Public Release)

- Public Technical Whitepaper (Sanitized):  
  `Lawmadi OS 공개 기술백서 (Public Release v1.0 · Sanitized)`  

If you package this repository for distribution, include the PDF in a `docs/` folder.

---

## Citation

If you use this work in research or documentation, cite using:

- `CITATION.cff`

---

## License & permissions

This repository is under a **Proprietary License**.

- Allowed: read, review, local evaluation/testing (non-production)
- Not allowed: production use, redistribution, derivatives, training ML/LLMs, or commercial use without written permission

See: **`LICENSE`**

---

## Security note (signature boundary)

`security/signature_interface.py` exists to demonstrate the **signing input/output contract**.

- Production deployments should back it with **KMS/HSM** (e.g., Cloud KMS)
- Public builds intentionally keep signatures as placeholders

---

## Contact

For licensing or commercial permissions:

- Email: **choepeter@outlook.kr**

---

© 2026 Jaenam Choi (최재남). All rights reserved.
