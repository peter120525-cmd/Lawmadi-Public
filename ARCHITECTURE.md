Lawmadi OS — Architecture Reference (Public / Sanitized)
​Document Version: 3.0 (Public/Sanitized) · Repository Release: v2.0.0 · 2026-02-09
Copyright © 2026 Jainam Choe (최재남). All rights reserved.
​"Convert Anxiety into Actionable Logic."
"불안을 실행 가능한 논리로 전환하다."
​This document provides a public, sanitized architectural overview of Lawmadi OS — a deterministic, FSM-based Legal Decision Operating System (LDOS). Proprietary scoring formulas, routing weights, deployment configurations, and operational secrets are intentionally excluded.
​Lawmadi OS is not a chatbot, not a search engine, and not a legal database. It is a Decision Intelligence Infrastructure that generates reproducible, verifiable decision artifacts (non-binding) grounded in live evidence.
​Evidence is fetched from designated SSOT endpoints in real time; the system does not maintain a durable replica of legal texts.
​For the complete LLM integration specification, see llms.txt (Directive v2.1-Unified).
For licensing terms, see LICENSE.txt.
​Disclaimer: This document is for technical reference only. It does not provide legal recommendations, constitute legal advice, or replace licensed legal professionals.
​Table of Contents
​System Identity
​Foundational Operating Constitution
​Platform Layer Architecture
​Runtime State Machine (FSM)
​Core Kernel Engines
​Decision Graph Formal Semantics
​Evidence Pipeline & Trust Scoring
​Cryptographic Integrity & Reproducibility
​Security Architecture
​Data Governance
​Output Contract
​LLM Integration Architecture
​Concurrency & Scalability (Conceptual)
​Infrastructure Topology (Non-operational)
​Global Multi-Jurisdiction Design
​Non-Public Assets (Redacted Index)
​Cross-Reference Map (Public Artifacts)
​1. System Identity
​It is a Decision Intelligence Infrastructure designed for Computable Trust — outputs are reproducible and auditable through evidence lineage, integrity checks, and deterministic state transitions.