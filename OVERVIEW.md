# Lawmadi OS -- Overview

**Korean Legal Decision Operating System**
**v60.0.0 | Bilingual (Korean + English)**

**Copyright (c) 2026 Jainam Choe. All rights reserved.**

---

## What Lawmadi OS Is

Lawmadi OS is a Legal Decision Operating System -- an infrastructure layer that converts legal questions into structured, evidence-verified decision support.

It is not a chatbot. It does not generate plausible-sounding legal text and hope the citations are real. It retrieves live evidence from official government sources, verifies every citation at the article level, and refuses to answer if verification fails.

**Production:** https://lawmadi.com / https://lawmadi-db.web.app

---

## The Problem

Legal AI has a fundamental reliability problem:

| Problem | What Happens | Consequence |
|---------|-------------|-------------|
| LLMs hallucinate legal citations | Users receive fabricated statute numbers and case references | Malpractice risk, sanctions, loss of trust |
| Systems rely on stale databases | Repealed statutes and overruled precedents get cited | Wrong legal advice, liability exposure |
| No verification layer | Users cannot trace how a conclusion was reached | Unaccountable "black box" outputs |
| No safety net | Systems serve best-guess answers even when uncertain | Dangerous half-truths in high-stakes situations |

These are not edge cases. They are structural defects in how current legal AI products work. Lawmadi OS was built to solve them at the architecture level.

---

## How It Works

Lawmadi OS processes every query through a 4-stage pipeline with real-time verification:

```
1. User asks a legal question (Korean or English)
       |
       v
2. NLU classifies and routes to one of 60 domain-expert leaders
   (regex pattern matching -> keyword matching -> Gemini classification -> fallback)
       |
       v
3. RAG retrieves relevant statutes, precedents, and constitutional
   court decisions from Vertex AI Search (~14,600 indexed documents)
       |
       v
4. Gemini 2.5 Flash generates a structured answer with full legal context,
   informed by the retrieved evidence and the leader's domain expertise
       |
       v
5. DRF Verification cross-checks every cited article against
   Korea's National Law Information Center API in real-time
       |
       v
   +--------+---------+
   |                   |
 PASS                FAIL
   |                   |
   v                   v
 Delivers           Refuses to answer.
 verified            Returns structured
 output              explanation of what
                     could not be verified.
```

This is a fail-closed system. If any citation cannot be verified against the official source, the system does not serve the answer.

---

## 60 Domain Expert Leaders

The system operates 60 specialized legal leaders (L01--L60), each with domain-specific legal knowledge, NLU patterns, and curated statute references:

- **Civil & Contracts** -- obligations, torts, consumer protection
- **Property & Real Estate** -- registration, leasing, reconstruction
- **Corporate & Commercial** -- company law, securities, M&A
- **Labor & Employment** -- labor standards, unions, workplace safety
- **Criminal** -- criminal law, procedure, juvenile, military
- **Family** -- marriage, divorce, custody, inheritance, adoption
- **Tax** -- income, corporate, VAT, local, customs, international
- **IP & Technology** -- patents, trademarks, copyright, trade secrets
- **Immigration** -- visas, nationality, foreign investment
- **Medical & Insurance** -- medical disputes, insurance, pharmaceutical
- **Construction & Environment** -- construction disputes, environmental law
- **Constitutional & Administrative** -- constitutional rights, administrative litigation
- **Data Protection & AI Ethics** -- personal information, AI governance

For complex questions spanning multiple domains, a CSO-led deliberation system coordinates multiple leaders through parallel consensus.

Each leader is assigned curated statute references (LAW_BOOST) that are injected into the generation prompt, ensuring domain-relevant legal grounding before Gemini generates any output.

---

## What Makes This Different

|  | Typical Legal AI | Lawmadi OS |
|---|---|---|
| **Evidence source** | Stored/synced database | Live retrieval from official government APIs |
| **Citation accuracy** | LLM-generated (frequently fabricated) | Verified against authoritative source in real-time |
| **When uncertain** | Serves best guess | Refuses to answer (fail-closed) |
| **Domain expertise** | Single generic model | 60 specialist leaders with domain-specific knowledge |
| **Language** | Usually monolingual | Bilingual Korean + English (NLU, RAG, verification) |
| **Freshness** | Periodic sync (hours to days) | Real-time API calls on every request |

---

## Five Operating Principles

These are enforced in code, not aspirational guidelines.

1. **SSOT (Single Source of Truth)** -- All legal evidence comes from authoritative government APIs. No copied databases or second-hand data.

2. **Zero Inference** -- The system never invents or fills in legal facts. Every legal statement has a verified evidence trail or it does not appear in the output.

3. **Fail-Closed** -- If evidence cannot be retrieved or verified, the system stops and returns a structured refusal explaining what went wrong.

4. **Live Evidence** -- Decisions are built on real-time evidence retrieval, not database snapshots. Legislative amendments are reflected immediately.

5. **Deterministic Runtime Boundary** -- The LLM is a rendering engine. Decision logic, evidence validation, and verification are handled by the deterministic pipeline. The LLM cannot skip steps or bypass safety checks.

---

## Platform Architecture

| Layer | Technology |
|-------|-----------|
| **API / Backend** | FastAPI (Python), async pipeline |
| **LLM** | Gemini 2.5 Flash (Google, Seoul region) |
| **RAG** | Vertex AI Search (~14,600 documents: statutes, precedents, constitutional court decisions) |
| **Verification** | DRF API (Korea National Law Information Center, real-time) |
| **Database** | Cloud SQL PostgreSQL 17 |
| **Hosting** | GCP Cloud Run (asia-northeast3, Seoul) |
| **Frontend** | Firebase Hosting (static PWA) |
| **CI/CD** | GitHub Actions (5-job pipeline: test, staging, production, firebase deploy, monitoring) |
| **Billing** | Paddle (credit-based pricing, email OTP authentication) |

**LawmadiLM** (fine-tuned Korean legal language model) has been built but is currently disabled. Gemini 2.5 Flash handles all generation. LawmadiLM may be re-enabled in future versions as a specialized layer.

---

## Current Capabilities (v60.0.0)

| Feature | Status |
|---------|--------|
| 60 Domain Expert Leaders (L01--L60) | Active |
| 4-Stage Legal Pipeline (NLU + RAG + Generation + Verification) | Active |
| Vertex AI Search RAG (~14,600 documents) | Active |
| Real-time DRF Verification (article-level cross-check) | Active |
| Bilingual Support (Korean + English) | Active |
| Leader Deliberation (CSO-led multi-expert consensus) | Active |
| Paddle Billing (credit packs, email OTP auth) | Active |
| English Law Cache (181 statutes via elaw API) | Active |
| Automated Health Monitoring (6-hour intervals) | Active |
| LawmadiLM (fine-tuned Korean legal LLM) | Built, currently disabled |

---

## Target Users

**Individuals with legal questions** -- Structured decision support for Korean law, replacing vague chatbot answers with verified, source-backed analysis.

**Small businesses** -- Navigate regulatory requirements with confidence. Each answer traces back to specific statutes and articles.

**Foreign nationals** -- Full English support for Korean legal questions, including English-language statute retrieval and NLU classification.

**Legal professionals** -- Expert mode with enhanced multi-leader analysis for complex, multi-domain questions.

---

## Repository Guide

| File | Contents |
|------|----------|
| [`README.md`](README.md) | Repository overview and quick start |
| [`ARCHITECTURE.md`](ARCHITECTURE.md) | Technical architecture reference with diagrams |
| [`OVERVIEW.md`](OVERVIEW.md) | This document -- system overview for general audiences |
| [`llms.txt`](llms.txt) | LLM system specification (canonical machine-readable reference) |
| [`llms.md`](llms.md) | Human-readable LLM integration specification |
| [`glossary.md`](glossary.md) | Bilingual glossary of technical terms (Korean/English) |
| [`index.md`](index.md) | Documentation index |
| [`config.schema.json`](config.schema.json) | Configuration JSON Schema |
| [`minimal_config.json`](minimal_config.json) | Minimal configuration example |
| [`LICENSE`](LICENSE) | Proprietary license |
| [`CITATION.cff`](CITATION.cff) | Citation metadata for academic/technical references |
| [Whitepaper PDF](Lawmadi_OS_Public_Technical_Whitepaper_v2_0_Sanitized.pdf) | Public technical whitepaper (sanitized) |

---

## License

**Proprietary.** This repository is provided for review, evaluation, and authorship proof only.

- Read, review, and local non-production evaluation: permitted
- Academic citation with proper attribution: permitted
- Production use, redistribution, derivatives, AI/ML training, commercial use: not permitted

See [`LICENSE`](LICENSE) for full terms.

---

## Citation

```
Choe, Jainam. "Lawmadi OS: Legal Decision Operating System --
Integrated Technical Whitepaper & Kernel Specification."
LDOS Reference Architecture v3.0. Lawmadi Project, February 2026.
```

---

## Contact

**Email:** choepeter@outlook.kr

For licensing inquiries, commercial permissions, or partnership proposals.

---

(c) 2026 Jainam Choe. All rights reserved.
