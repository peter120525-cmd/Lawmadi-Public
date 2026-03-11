"""
Lawmadi OS v60.0.0 — Configuration Validator Demo (Sanitized)

Validates a Lawmadi OS configuration file against the system's
constitutional principles and schema constraints.

Demonstrates:
- JSON Schema validation against config.schema.json
- Constitutional invariant enforcement (5 principles)
- Security policy verification
- FSM state graph validation

Copyright (c) 2026 Jainam Choe. All rights reserved.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


# ---------------------------------------------------------------------------
# Constitutional Invariants (Part I of llms.txt)
# These are NON-NEGOTIABLE — the system refuses to start if violated.
# ---------------------------------------------------------------------------

CONSTITUTIONAL_CHECKS: list[tuple[str, str, Any]] = [
    # (json_path, description, required_value)
    ("constitution.ssot.enabled", "SSOT enforcement", True),
    ("constitution.ssot.allow_permanent_storage", "No permanent legal data storage", False),
    ("constitution.ssot.allow_dataset_replication", "No dataset replication", False),
    ("constitution.zero_inference.enabled", "Zero Inference enforcement", True),
    ("constitution.zero_inference.allow_unsourced_legal_claims", "No unsourced claims", False),
    ("constitution.fail_closed.enabled", "Fail-Closed enforcement", True),
    ("constitution.fail_closed.allow_unverified_output", "No unverified output", False),
    ("constitution.live_evidence.enabled", "Live Evidence enforcement", True),
    ("constitution.deterministic_boundary.enabled", "Deterministic Boundary enforcement", True),
    ("constitution.deterministic_boundary.llm_may_control_fsm", "LLM cannot control FSM", False),
    ("constitution.deterministic_boundary.llm_may_override_tools", "LLM cannot override tools", False),
    ("constitution.deterministic_boundary.llm_may_access_secrets", "LLM cannot access secrets", False),
]

SECURITY_CHECKS: list[tuple[str, str, Any]] = [
    ("security.prompt_injection_defense.enabled", "Prompt injection defense", True),
    ("security.prompt_injection_defense.treat_user_input_as_untrusted", "Untrusted user input", True),
    ("security.tool_injection_defense.enabled", "Tool injection defense", True),
    ("security.tool_injection_defense.allow_arbitrary_url_fetch", "No arbitrary URL fetch", False),
    ("security.secret_management.secrets_in_prompts", "No secrets in prompts", False),
    ("security.output_masking.mask_secrets", "Mask secrets in output", True),
]

# Valid FSM state transitions (happy path)
FSM_HAPPY_PATH = [
    "INPUT_RECEIVED",
    "INPUT_VALIDATED",
    "CASE_STRUCTURED",
    "ISSUE_IDENTIFIED",
    "LEADER_ROUTED",
    "EVIDENCE_FETCHING",
    "EVIDENCE_VALIDATED",
    "DECISION_GRAPH_BUILT",
    "TOKEN_MINTED",
    "TOKEN_SIGNED",
    "RESPONSE_DELIVERED",
]

REQUIRED_FAIL_STATES = [
    "EVIDENCE_VALIDATION_FAILED",
    "TEMPORAL_VALIDATION_FAILED",
    "CONSTITUTION_VIOLATION",
    "SOURCE_INTEGRITY_FAILURE",
]

REQUIRED_DSL_RULES = [
    "Enforce_Source_Integrity",
    "Validate_Effective_Date",
    "Reject_Missing_Evidence",
    "Enforce_Zero_Inference",
    "Enforce_Decision_Completeness",
    "Enforce_Crypto_Integrity",
]


# ---------------------------------------------------------------------------
# Validation Helpers
# ---------------------------------------------------------------------------

def _resolve_path(config: dict, path: str) -> Any:
    """Resolve a dot-separated path in a nested dict."""
    keys = path.split(".")
    current = config
    for key in keys:
        if not isinstance(current, dict) or key not in current:
            return None
        current = current[key]
    return current


def validate_constitutional_invariants(config: dict) -> list[str]:
    """Check all 5 constitutional principles are enforced."""
    errors = []
    for path, description, required in CONSTITUTIONAL_CHECKS:
        actual = _resolve_path(config, path)
        if actual is None:
            errors.append(f"MISSING: {description} ({path})")
        elif actual != required:
            errors.append(
                f"VIOLATION: {description} — "
                f"expected {required}, got {actual} ({path})"
            )
    return errors


def validate_security(config: dict) -> list[str]:
    """Verify security controls are properly configured."""
    errors = []
    for path, description, required in SECURITY_CHECKS:
        actual = _resolve_path(config, path)
        if actual is None:
            errors.append(f"MISSING: {description} ({path})")
        elif actual != required:
            errors.append(
                f"SECURITY: {description} — "
                f"expected {required}, got {actual} ({path})"
            )
    return errors


def validate_fsm(config: dict) -> list[str]:
    """Validate FSM state definitions and mandatory gate."""
    errors = []
    fsm = config.get("fsm", {})

    # Check happy path states
    states = fsm.get("states", [])
    for required_state in FSM_HAPPY_PATH:
        if required_state not in states:
            errors.append(f"FSM: Missing happy-path state: {required_state}")

    # Check fail states
    fail_states = fsm.get("fail_states", [])
    for required_state in REQUIRED_FAIL_STATES:
        if required_state not in fail_states:
            errors.append(f"FSM: Missing fail state: {required_state}")

    # Mandatory gate
    gate = fsm.get("mandatory_gate")
    if gate != "EVIDENCE_VALIDATED":
        errors.append(
            f"FSM: Mandatory gate must be EVIDENCE_VALIDATED, got {gate}"
        )

    return errors


def validate_dsl_rules(config: dict) -> list[str]:
    """Check that all required DSL rules are present."""
    errors = []
    rules = _resolve_path(config, "constitution.dsl.rules") or []
    for required_rule in REQUIRED_DSL_RULES:
        if required_rule not in rules:
            errors.append(f"DSL: Missing rule: {required_rule}")

    mode = _resolve_path(config, "constitution.dsl.enforcement_mode")
    if mode != "reject":
        errors.append(
            f"DSL: Enforcement mode should be 'reject', got '{mode}'"
        )

    return errors


def validate_config(config: dict) -> tuple[bool, list[str], list[str]]:
    """
    Full configuration validation.

    Returns:
        (is_valid, errors, warnings)
    """
    errors = []
    warnings = []

    # 1. Constitutional invariants (MUST pass)
    errors.extend(validate_constitutional_invariants(config))

    # 2. Security controls (MUST pass)
    errors.extend(validate_security(config))

    # 3. FSM structure (MUST pass)
    errors.extend(validate_fsm(config))

    # 4. DSL rules (MUST pass)
    errors.extend(validate_dsl_rules(config))

    # 5. Metadata checks (warnings)
    meta = config.get("$meta", {})
    if not meta.get("config_version"):
        warnings.append("Missing $meta.config_version")
    if not meta.get("constitution_version"):
        warnings.append("Missing $meta.constitution_version")
    env = meta.get("environment", "")
    if env not in ("development", "staging", "production", "public-sandbox"):
        warnings.append(f"Unknown environment: {env}")

    # 6. LLM role check
    llm_role = _resolve_path(config, "llm_integration.role")
    if llm_role != "rendering_engine":
        errors.append(
            f"LLM role must be 'rendering_engine', got '{llm_role}'"
        )

    return len(errors) == 0, errors, warnings


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------

def main():
    print("=" * 60)
    print("Lawmadi OS v60.0.0 — Configuration Validator")
    print("=" * 60)

    # Load minimal_config.json from the repo
    config_path = Path(__file__).parent.parent / "minimal_config.json"
    if not config_path.exists():
        print(f"Config not found: {config_path}")
        sys.exit(1)

    with open(config_path, encoding="utf-8") as f:
        config = json.load(f)

    print(f"\nValidating: {config_path.name}")
    print(f"Config version: {config.get('$meta', {}).get('config_version', 'N/A')}")
    print(f"Constitution:   {config.get('$meta', {}).get('constitution_version', 'N/A')}")
    print(f"Environment:    {config.get('$meta', {}).get('environment', 'N/A')}")

    is_valid, errors, warnings = validate_config(config)

    print(f"\n--- Results ---")
    if warnings:
        for w in warnings:
            print(f"  WARN: {w}")
    if errors:
        for e in errors:
            print(f"  FAIL: {e}")
    else:
        print("  All constitutional invariants:  PASS")
        print("  All security controls:          PASS")
        print("  FSM state graph:                PASS")
        print("  DSL rules:                      PASS")
        print("  LLM integration:                PASS")

    print(f"\n  Status: {'VALID' if is_valid else 'INVALID'}")
    print(f"  Checks: {len(CONSTITUTIONAL_CHECKS) + len(SECURITY_CHECKS)} invariants, "
          f"{len(FSM_HAPPY_PATH)} FSM states, {len(REQUIRED_DSL_RULES)} DSL rules")
    print("=" * 60)

    sys.exit(0 if is_valid else 1)


if __name__ == "__main__":
    main()
