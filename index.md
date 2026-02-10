# Lawmadi OS — Repository Index

<p align="left">
  <a href="https://doi.org/10.5281/zenodo.18551976">
    <img alt="DOI" src="https://zenodo.org/badge/DOI/10.5281/zenodo.18551976.svg" />
  </a>
  <img alt="release" src="https://img.shields.io/badge/release-v2.0.0-informational" />
  <img alt="ldos" src="https://img.shields.io/badge/LDOS-deterministic%20FSM-2563eb" />
  <img alt="policy" src="https://img.shields.io/badge/policy-SSOT%20%7C%20Zero%20Inference%20%7C%20Fail--Closed-0ea5e9" />
  <img alt="license" src="https://img.shields.io/badge/license-proprietary-critical" />
</p>

**Legal Decision Operating System (LDOS) · v2.0.0 (Public / Sanitized)**  
**Copyright © 2026 Jainam Choe (최재남). All rights reserved.**

> **Lawmadi OS is NOT a chatbot, NOT a search engine, NOT a legal database.**  
> It is a **deterministic decision infrastructure** that generates **evidence-gated outputs** under non-negotiable constitutional constraints.

---

## Quick Links (Start Here)

<p align="left">
  <a href="./OVERVIEW.md"><img alt="OVERVIEW" src="https://img.shields.io/badge/Start-OVERVIEW.md-22c55e" /></a>
  <a href="./README.md"><img alt="README" src="https://img.shields.io/badge/Guide-README.md-0ea5e9" /></a>
  <a href="./ARCHITECTURE.md"><img alt="ARCHITECTURE" src="https://img.shields.io/badge/Design-ARCHITECTURE.md-6366f1" /></a>
  <a href="./llms.md"><img alt="LLMS (Readable)" src="https://img.shields.io/badge/Human%20Spec-llms.md-a855f7" /></a>
  <a href="./llms.txt"><img alt="LLMS (Canonical)" src="https://img.shields.io/badge/Canonical-llms.txt-111827" /></a>
  <a href="./glossary.md"><img alt="GLOSSARY" src="https://img.shields.io/badge/Terms-glossary.md-f59e0b" /></a>
  <a href="./minimal_config.json"><img alt="CONFIG" src="https://img.shields.io/badge/Run-minimal__config.json-64748b" /></a>
</p>

**What should I click?**
- 처음 오셨다면 → **[OVERVIEW.md](OVERVIEW.md)**  
- 빠르게 레포를 평가/실행하고 싶다면 → **[README.md](README.md)** + **[minimal_config.json](minimal_config.json)**  
- 설계/철학/규칙(SSOT·Fail-Closed)까지 깊게 보고 싶다면 → **[ARCHITECTURE.md](ARCHITECTURE.md)**  
- LLM 통합 스펙(사람용) → **[llms.md](llms.md)**  
- LLM 통합 스펙(표준본, 텍스트) → **[llms.txt](llms.txt)**  
- 용어가 헷갈리면 → **[glossary.md](glossary.md)**

---

## What’s Inside (At a Glance)

### Orientation (비기너/비기술도 OK)
- **[OVERVIEW.md](OVERVIEW.md)** — Lawmadi OS가 무엇인지/왜 필요한지
- **[README.md](README.md)** — 설치/실행/구성 요약
- **[glossary.md](glossary.md)** — 핵심 용어 사전(참조용)

### Architecture & Specs (설계/검증/표준)
- **[ARCHITECTURE.md](ARCHITECTURE.md)** — 플랫폼 레이어, FSM, 엔진, 증거 파이프라인, 보안/데이터 거버넌스
- **[llms.md](llms.md)** — GitHub 렌더링 최적화 “사람용” LLM 통합 스펙
- **[llms.txt](llms.txt)** — “기계/에이전트용” Canonical 텍스트 표준 (렌더링 없음)

### Configuration (구성/배포/통합)
- **[config.schema.json](config.schema.json)** — 런타임 설정 스키마(전체 계약)
- **[minimal_config.json](minimal_config.json)** — 바로 실행 가능한 최소 구성 예시(공개/샌드박스)

### Legal & Citation (라이선스/인용)
- **[LICENSE](LICENSE)** — Proprietary License (재사용/학습/경쟁 제한 포함)
- **[CITATION.cff](CITATION.cff)** — 인용 메타데이터(학술/기술문서)

### Whitepaper (PDF)
- **Lawmadi_OS_Public_Technical_Whitepaper_… .pdf** — 공개/정제 기술백서 (레포 루트에 존재)

---

## Recommended Reading Paths

<details>
<summary><strong>🟢 Path A — “이게 뭔지 10분 안에 이해하고 싶어요”</strong></summary>

1) [OVERVIEW.md](OVERVIEW.md)  
2) [README.md](README.md)  
3) (필요시) [glossary.md](glossary.md)

</details>

<details>
<summary><strong>🔵 Path B — “코드/구성을 평가하고 싶어요”</strong></summary>

1) [README.md](README.md)  
2) [minimal_config.json](minimal_config.json)  
3) [config.schema.json](config.schema.json)  
4) [ARCHITECTURE.md](ARCHITECTURE.md)

</details>

<details>
<summary><strong>🟣 Path C — “LLM 통합을 만들고 있어요”</strong></summary>

1) [llms.md](llms.md) (사람용 빠른 스캔)  
2) [llms.txt](llms.txt) (Canonical 표준본)  
3) [config.schema.json](config.schema.json)  
4) [minimal_config.json](minimal_config.json)  
5) (용어 막히면) [glossary.md](glossary.md)

</details>

<details>
<summary><strong>🟠 Path D — “파트너/투자/리뷰 목적이에요”</strong></summary>

1) [OVERVIEW.md](OVERVIEW.md)  
2) Whitepaper PDF (레포 루트)  
3) (IP/제한 확인) [LICENSE](LICENSE)

</details>

<details>
<summary><strong>🔴 Path E — “인용하려고 합니다”</strong></summary>

1) [CITATION.cff](CITATION.cff)  
2) [LICENSE](LICENSE) (인용/표기 조건 확인)

</details>

---

## System at a Glance

```text
OS (Kernel)  →  Evidence Engine (Trust)  →  Service (UX)  →  Platform (Ecosystem)
Deterministic     Live Evidence + Hash       Conversational     Education / B2B
FSM Runtime       SSOT Validation            Rendering only     Controlled access
