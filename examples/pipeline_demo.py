"""
Lawmadi OS v60.0.0 — 4-Stage Pipeline Demo (Sanitized)

Demonstrates the conceptual flow of Lawmadi OS's legal decision pipeline:
  Stage 0+1: NLU Classification + RAG Retrieval (parallel)
  Stage 2:   LawmadiLM Enhancement (currently disabled)
  Stage 3:   Gemini Generation with domain-specific LAW_BOOST
  Stage 4:   DRF Real-Time Verification (fail-closed)

This is a sanitized architectural demo. Production code includes
additional security layers, circuit breakers, and async parallelization.

Copyright (c) 2026 Jainam Choe. All rights reserved.
"""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Optional


# ---------------------------------------------------------------------------
# FSM States (Part V of llms.txt)
# ---------------------------------------------------------------------------

class PipelineState(Enum):
    INPUT_RECEIVED = "INPUT_RECEIVED"
    INPUT_VALIDATED = "INPUT_VALIDATED"
    LEADER_ROUTED = "LEADER_ROUTED"
    EVIDENCE_FETCHING = "EVIDENCE_FETCHING"
    EVIDENCE_VALIDATED = "EVIDENCE_VALIDATED"
    DECISION_GRAPH_BUILT = "DECISION_GRAPH_BUILT"
    TOKEN_MINTED = "TOKEN_MINTED"
    RESPONSE_DELIVERED = "RESPONSE_DELIVERED"
    # Fail states
    EVIDENCE_VALIDATION_FAILED = "EVIDENCE_VALIDATION_FAILED"
    HALT = "HALT"


# ---------------------------------------------------------------------------
# Data Classes
# ---------------------------------------------------------------------------

@dataclass
class LegalQuery:
    text: str
    lang: str = "ko"
    timestamp: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )


@dataclass
class LeaderAssignment:
    leader_id: str
    leader_name: str
    domain: str
    confidence: float


@dataclass
class EvidenceItem:
    law_name: str
    article: str
    status: str  # IN_FORCE, REPEALED, etc.
    source: str  # OFFICIAL_API
    verified: bool = False


@dataclass
class PipelineResult:
    state: PipelineState
    leader: Optional[LeaderAssignment] = None
    evidence: list[EvidenceItem] = field(default_factory=list)
    response_text: str = ""
    error_code: str = ""
    evidence_hash: str = ""


# ---------------------------------------------------------------------------
# Stage 0+1: NLU Classification (simplified demo)
# ---------------------------------------------------------------------------

# In production, this uses regex patterns, keyword matching,
# and Gemini-based classification with 60 domain-expert leaders.
_DEMO_LEADER_ROUTING: dict[str, LeaderAssignment] = {
    "임대차": LeaderAssignment("L06", "민준", "부동산임대차", 0.95),
    "이혼": LeaderAssignment("L21", "하윤", "이혼·양육", 0.92),
    "해고": LeaderAssignment("L13", "도윤", "근로기준법·부당해고", 0.94),
    "상속": LeaderAssignment("L23", "유진", "상속·유류분", 0.91),
    "계약": LeaderAssignment("L01", "온유", "민법총칙·계약", 0.90),
    "lease": LeaderAssignment("L06", "민준", "부동산임대차", 0.93),
    "divorce": LeaderAssignment("L21", "하윤", "이혼·양육", 0.91),
    "dismissal": LeaderAssignment("L13", "도윤", "근로기준법·부당해고", 0.92),
}


def classify_query(query: LegalQuery) -> LeaderAssignment:
    """
    Stage 0: NLU classification — route to the appropriate domain leader.

    Production uses a 4-tier routing cascade:
      1. Name-based routing (direct leader reference)
      2. NLU regex patterns (situation + action combinations)
      3. Keyword matching (domain-specific terms)
      4. Fallback to CCO (Chief Coordination Officer)
    """
    text_lower = query.text.lower()
    for keyword, leader in _DEMO_LEADER_ROUTING.items():
        if keyword in text_lower:
            return leader
    # Fallback: CCO routes the query
    return LeaderAssignment("CCO", "수호", "법률총괄", 0.50)


# ---------------------------------------------------------------------------
# Stage 1: RAG Retrieval (conceptual)
# ---------------------------------------------------------------------------

def retrieve_evidence(leader: LeaderAssignment, query: LegalQuery) -> list[EvidenceItem]:
    """
    Stage 1: Vertex AI Search RAG retrieval (~14,600 indexed documents).

    In production:
    - Queries Vertex AI Search with domain-specific boosting
    - Retrieves statutes, precedents, and constitutional court decisions
    - Returns extractive answers and segments
    - Runs in parallel with NLU classification (asyncio.gather)
    """
    # Demo: return sample evidence based on leader domain
    _DEMO_EVIDENCE: dict[str, list[EvidenceItem]] = {
        "L06": [
            EvidenceItem("주택임대차보호법", "제3조", "IN_FORCE", "OFFICIAL_API"),
            EvidenceItem("주택임대차보호법", "제8조", "IN_FORCE", "OFFICIAL_API"),
        ],
        "L21": [
            EvidenceItem("민법", "제834조", "IN_FORCE", "OFFICIAL_API"),
            EvidenceItem("민법", "제837조", "IN_FORCE", "OFFICIAL_API"),
        ],
        "L13": [
            EvidenceItem("근로기준법", "제23조", "IN_FORCE", "OFFICIAL_API"),
            EvidenceItem("근로기준법", "제30조", "IN_FORCE", "OFFICIAL_API"),
        ],
    }
    return _DEMO_EVIDENCE.get(leader.leader_id, [])


# ---------------------------------------------------------------------------
# Stage 4: DRF Verification (fail-closed)
# ---------------------------------------------------------------------------

def verify_evidence(evidence: list[EvidenceItem]) -> tuple[bool, str]:
    """
    Stage 4: DRF real-time verification against Korea's National Law
    Information Center API.

    In production:
    - Extracts law references from generated text via regex
    - Calls DRF API for each referenced statute + article
    - Cross-validates article existence and current status
    - Supports both Korean (DRF lawSearch) and English (elaw) APIs
    - Fail-closed: if ANY citation cannot be verified, the entire
      response is rejected
    """
    for item in evidence:
        if item.status in ("REPEALED", "UNCONSTITUTIONAL", "INVALIDATED"):
            return False, f"LC-004: {item.law_name} {item.article} — {item.status}"
        if item.source != "OFFICIAL_API":
            return False, f"LC-002: {item.law_name} — non-authoritative source"
        # In production: actual DRF API call here
        item.verified = True
    return True, ""


def compute_evidence_hash(evidence: list[EvidenceItem]) -> str:
    """Compute SHA-256 hash of the canonical evidence set."""
    canonical = json.dumps(
        [{"law": e.law_name, "article": e.article, "status": e.status}
         for e in evidence],
        sort_keys=True, separators=(",", ":"), ensure_ascii=False,
    )
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# Pipeline Orchestrator
# ---------------------------------------------------------------------------

def run_pipeline(query: LegalQuery) -> PipelineResult:
    """
    Execute the 4-stage legal decision pipeline.

    This demo shows the sequential flow. Production uses:
    - asyncio.gather for parallel Stage 0+1
    - Circuit breakers for external API calls
    - Exponential backoff retry (429 handling)
    - LAW_BOOST injection for domain-specific statute grounding
    """
    result = PipelineResult(state=PipelineState.INPUT_RECEIVED)

    # --- Stage 0: Input Validation ---
    if not query.text.strip():
        result.state = PipelineState.HALT
        result.error_code = "LC-003"
        return result
    result.state = PipelineState.INPUT_VALIDATED

    # --- Stage 0+1 (parallel in production): NLU + RAG ---
    leader = classify_query(query)
    result.leader = leader
    result.state = PipelineState.LEADER_ROUTED

    evidence = retrieve_evidence(leader, query)
    result.evidence = evidence
    result.state = PipelineState.EVIDENCE_FETCHING

    # --- Stage 4: DRF Verification (fail-closed) ---
    if not evidence:
        result.state = PipelineState.EVIDENCE_VALIDATION_FAILED
        result.error_code = "LC-001"
        return result

    verified, error = verify_evidence(evidence)
    if not verified:
        result.state = PipelineState.EVIDENCE_VALIDATION_FAILED
        result.error_code = error
        return result

    result.state = PipelineState.EVIDENCE_VALIDATED
    result.evidence_hash = compute_evidence_hash(evidence)

    # --- Stage 3: Generation (Gemini 2.5 Flash in production) ---
    # In production, Gemini generates a structured legal analysis
    # using the leader's domain expertise and LAW_BOOST references.
    # Stage 2 (LawmadiLM) is currently disabled.
    law_refs = ", ".join(f"{e.law_name} {e.article}" for e in evidence)
    result.response_text = (
        f"[{leader.leader_name} ({leader.domain})] "
        f"근거 법령: {law_refs} | "
        f"검증 완료 (evidence_hash: {result.evidence_hash[:16]}...)"
    )

    result.state = PipelineState.RESPONSE_DELIVERED
    return result


# ---------------------------------------------------------------------------
# Demo Execution
# ---------------------------------------------------------------------------

def main():
    print("=" * 60)
    print("Lawmadi OS v60.0.0 — Pipeline Demo (Sanitized)")
    print("=" * 60)

    test_queries = [
        LegalQuery("전세 보증금을 돌려받지 못하고 있습니다", lang="ko"),
        LegalQuery("부당해고를 당했습니다", lang="ko"),
        LegalQuery("이혼 시 양육권은 어떻게 되나요?", lang="ko"),
        LegalQuery("I was unfairly dismissed from work", lang="en"),
        LegalQuery("", lang="ko"),  # Empty query — should fail
    ]

    for i, query in enumerate(test_queries, 1):
        print(f"\n--- Query {i}: {query.text or '(empty)'} ---")
        result = run_pipeline(query)

        print(f"  State:  {result.state.value}")
        if result.leader:
            print(f"  Leader: {result.leader.leader_name} "
                  f"({result.leader.leader_id}, {result.leader.domain})")
        if result.evidence:
            print(f"  Evidence: {len(result.evidence)} items, "
                  f"all verified: {all(e.verified for e in result.evidence)}")
        if result.response_text:
            print(f"  Output: {result.response_text}")
        if result.error_code:
            print(f"  Error:  {result.error_code}")
        print(f"  Hash:   {result.evidence_hash[:32] or 'N/A'}...")

    print("\n" + "=" * 60)
    print("Pipeline demo complete.")
    print("Production: https://lawmadi.com")
    print("=" * 60)


if __name__ == "__main__":
    main()
