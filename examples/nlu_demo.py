"""
Lawmadi OS v60.0.0 — NLU Classification Demo (Sanitized)

Demonstrates the Natural Language Understanding classification system
that routes legal queries to one of 60 domain-expert leaders.

Production routing cascade:
  1. Name-based routing (user directly addresses a leader)
  2. NLU regex patterns (situation + action pattern matching)
  3. Keyword matching (domain-specific legal terms)
  4. Gemini-based classification (LLM fallback)
  5. CCO fallback (Chief Coordination Officer)

This demo shows a simplified version of tiers 2-3.
Actual regex patterns and priority weights are proprietary.

Copyright (c) 2026 Jainam Choe. All rights reserved.
"""

from __future__ import annotations

import re
from dataclasses import dataclass


# ---------------------------------------------------------------------------
# Leader Registry (60 Leaders, L01-L60)
# ---------------------------------------------------------------------------

@dataclass
class Leader:
    id: str
    name_ko: str
    name_en: str
    domain_ko: str
    domain_en: str
    priority: int  # lower = higher priority


# Subset of 60 leaders for demo purposes
LEADERS: list[Leader] = [
    Leader("L01", "온유", "Onyu", "민법총칙·계약", "Civil Code / Contracts", 10),
    Leader("L02", "서연", "Seoyeon", "채권·손해배상", "Obligations / Torts", 15),
    Leader("L06", "민준", "Minjun", "부동산임대차", "Real Estate Leasing", 8),
    Leader("L13", "도윤", "Doyun", "근로기준법·부당해고", "Labor Standards", 7),
    Leader("L14", "하은", "Haeun", "산업안전·산재", "Workplace Safety", 12),
    Leader("L17", "지안", "Jian", "형법·형사절차", "Criminal Law", 9),
    Leader("L21", "하윤", "Hayun", "이혼·양육", "Divorce / Custody", 6),
    Leader("L23", "유진", "Yujin", "상속·유류분", "Inheritance", 11),
    Leader("L25", "소율", "Soyul", "소득세·종합소득", "Income Tax", 13),
    Leader("L33", "지호", "Jiho", "특허·실용신안", "Patents", 14),
    Leader("L41", "수아", "Sua", "비자·체류자격", "Visa / Immigration", 5),
    Leader("L49", "다온", "Daon", "건설분쟁·하자", "Construction Disputes", 16),
    Leader("L55", "이준", "Ijun", "헌법·기본권", "Constitutional Rights", 17),
    Leader("L57", "시우", "Siu", "개인정보보호", "Data Protection", 18),
]


# ---------------------------------------------------------------------------
# Tier 2: NLU Regex Patterns (simplified demo subset)
# ---------------------------------------------------------------------------
# Production uses _NLU_INTENT_PATTERNS with situation+action combinations
# and _NLU_PRIORITY ordering for disambiguation.

_NLU_PATTERNS_KO: list[tuple[str, re.Pattern]] = [
    ("L06", re.compile(r"(전세|월세|임대차|보증금|임차인|임대인|주택임대)")),
    ("L13", re.compile(r"(해고|부당해고|퇴직금|임금체불|근로계약|야근)")),
    ("L21", re.compile(r"(이혼|양육권|위자료|재산분할|혼인|별거)")),
    ("L23", re.compile(r"(상속|유류분|유언|상속포기|한정승인)")),
    ("L17", re.compile(r"(형사|고소|고발|폭행|사기|절도|횡령)")),
    ("L25", re.compile(r"(소득세|종합소득|연말정산|세금신고|원천징수)")),
    ("L41", re.compile(r"(비자|체류|외국인등록|귀화|영주권|워킹홀리데이)")),
    ("L01", re.compile(r"(계약|매매|대금|채무불이행|계약해제|약정)")),
    ("L33", re.compile(r"(특허|실용신안|발명|특허침해|특허출원)")),
    ("L57", re.compile(r"(개인정보|정보보호|데이터|GDPR|동의철회)")),
    ("L55", re.compile(r"(헌법|기본권|위헌|헌법소원|평등권)")),
    ("L49", re.compile(r"(건설|하자|시공|도급|건축물)")),
    ("L14", re.compile(r"(산재|산업재해|업무상재해|안전사고)")),
    ("L02", re.compile(r"(손해배상|불법행위|과실|위법행위|배상)")),
]

_NLU_PATTERNS_EN: list[tuple[str, re.Pattern]] = [
    ("L06", re.compile(r"(lease|rent|deposit|tenant|landlord)", re.IGNORECASE)),
    ("L13", re.compile(r"(dismissal|fired|termination|wage|overtime)", re.IGNORECASE)),
    ("L21", re.compile(r"(divorce|custody|alimony|marriage|separation)", re.IGNORECASE)),
    ("L23", re.compile(r"(inheritance|heir|will|estate|probate)", re.IGNORECASE)),
    ("L17", re.compile(r"(criminal|prosecution|assault|fraud|theft)", re.IGNORECASE)),
    ("L41", re.compile(r"(visa|immigration|residency|citizenship|foreigner)", re.IGNORECASE)),
    ("L01", re.compile(r"(contract|agreement|breach|obligation|sale)", re.IGNORECASE)),
    ("L33", re.compile(r"(patent|invention|infringement|utility model)", re.IGNORECASE)),
    ("L57", re.compile(r"(personal data|privacy|GDPR|data protection)", re.IGNORECASE)),
]


# ---------------------------------------------------------------------------
# Tier 3: Keyword Matching (simplified demo subset)
# ---------------------------------------------------------------------------

_KEYWORD_MAP_KO: dict[str, str] = {
    "전세": "L06", "월세": "L06", "임대차": "L06",
    "해고": "L13", "퇴직금": "L13", "임금": "L13",
    "이혼": "L21", "양육권": "L21", "위자료": "L21",
    "상속": "L23", "유류분": "L23", "유언": "L23",
    "사기": "L17", "폭행": "L17", "절도": "L17",
    "비자": "L41", "체류": "L41", "귀화": "L41",
    "계약": "L01", "매매": "L01",
    "특허": "L33", "발명": "L33",
    "개인정보": "L57",
    "헌법소원": "L55",
    "건설": "L49", "하자": "L49",
    "산재": "L14",
    "손해배상": "L02",
}


# ---------------------------------------------------------------------------
# Classification Engine
# ---------------------------------------------------------------------------

def _get_leader(leader_id: str) -> Leader | None:
    return next((l for l in LEADERS if l.id == leader_id), None)


def classify(query: str, lang: str = "ko") -> tuple[Leader | None, str, float]:
    """
    Classify a legal query and return (leader, method, confidence).

    Returns:
        tuple: (Leader, routing_method, confidence_score)
    """
    # Tier 2: NLU regex patterns
    patterns = _NLU_PATTERNS_KO if lang == "ko" else _NLU_PATTERNS_EN
    matches: list[tuple[str, int]] = []
    for leader_id, pattern in patterns:
        if pattern.search(query):
            leader = _get_leader(leader_id)
            if leader:
                matches.append((leader_id, leader.priority))

    if matches:
        # Select highest priority (lowest number)
        matches.sort(key=lambda x: x[1])
        best_id = matches[0][0]
        leader = _get_leader(best_id)
        confidence = 0.85 if len(matches) == 1 else 0.70
        return leader, "nlu_regex", confidence

    # Tier 3: Keyword matching
    if lang == "ko":
        for keyword, leader_id in _KEYWORD_MAP_KO.items():
            if keyword in query:
                leader = _get_leader(leader_id)
                return leader, "keyword", 0.60

    # Tier 5: CCO fallback
    return Leader("CCO", "수호", "Suho", "법률총괄", "General Counsel", 99), "fallback", 0.30


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------

def main():
    print("=" * 65)
    print("Lawmadi OS v60.0.0 — NLU Classification Demo (Sanitized)")
    print("60 Domain-Expert Leaders | Bilingual KO + EN")
    print("=" * 65)

    test_cases = [
        # (query, lang)
        ("전세 보증금 반환 소송을 하고 싶습니다", "ko"),
        ("부당해고를 당했는데 어떻게 해야 하나요?", "ko"),
        ("이혼 시 재산분할은 어떻게 되나요?", "ko"),
        ("상속 포기 절차가 궁금합니다", "ko"),
        ("사기를 당했습니다 고소하고 싶어요", "ko"),
        ("E-7 비자 변경 절차를 알고 싶습니다", "ko"),
        ("I need help with my lease deposit", "en"),
        ("I was unfairly dismissed from my job", "en"),
        ("How does divorce custody work in Korea?", "en"),
        ("I need a visa extension for Korea", "en"),
        ("날씨가 좋습니다", "ko"),  # Non-legal query -> CCO fallback
    ]

    for query, lang in test_cases:
        leader, method, confidence = classify(query, lang)
        flag = "!" if method == "fallback" else " "
        print(
            f"  {flag} [{lang.upper()}] {query[:40]:<40s} "
            f"-> {leader.id:>3s} {leader.name_ko} "
            f"({method}, {confidence:.0%})"
        )

    print("\n" + "-" * 65)
    print(f"  Leaders shown: {len(LEADERS)} of 60")
    print(f"  KO patterns:   {len(_NLU_PATTERNS_KO)} (production: 60)")
    print(f"  EN patterns:   {len(_NLU_PATTERNS_EN)} (production: 48)")
    print("  Full system:    https://lawmadi.com")
    print("=" * 65)


if __name__ == "__main__":
    main()
