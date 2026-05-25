# Knowledge Base Management Skill

> Search-first knowledge management for AI agents — find articles, detect gaps, create content, collect feedback, and grow the KB from resolved issues via mcp-knowledge-base.

[![Skill Standard](https://img.shields.io/badge/standard-agentskills.io-blue)](https://agentskills.io)
[![MCP Server](https://img.shields.io/badge/mcp--server-mcp--knowledge--base-green)](https://github.com/zavora-ai/mcp-knowledge-base)
[![ADK-Rust Enterprise](https://img.shields.io/badge/ADK--Rust-Enterprise-purple.svg)](https://enterprise.adk-rust.com)
[![License](https://img.shields.io/badge/license-Apache--2.0-orange)](LICENSE)

## What This Skill Does

| Workflow | Tool Calls | What It Achieves |
|----------|-----------|------------------|
| Search & Resolve | 1-2 | Find answer without creating a ticket |
| Create Article | 2 | Draft + publish from resolved issues |
| Gap Analysis | 1 | Identify missing content by query frequency |
| Feedback Loop | 1 | Track article helpfulness |

### Without this skill:
- Same questions answered manually every time
- No knowledge grows from resolved incidents
- Gaps invisible (don't know what's missing)
- Stale articles served without warning

### With this skill:
- KB searched before creating tickets (40%+ deflection)
- Articles auto-created from resolutions
- Gaps detected by unmatched query frequency
- Freshness tracked, stale content flagged

## Installation

```bash
git clone https://github.com/zavora-ai/skill-knowledge-base-management.git \
  ~/.skills/skills/knowledge-base-management
```

## Requirements

**Required:** `mcp-knowledge-base` (9 tools)

**Cross-MCP:**
- `mcp-itsm` — resolve tickets from KB, create articles from resolutions
- `mcp-customer-service` — answer customer questions from KB

## Folder Structure

```
knowledge-base-management/
├── SKILL.md                       # Decision tree + search-first principle
├── scripts/
│   └── score_relevance.py         # TF-IDF-like article scoring
├── references/
│   ├── tool-sequences.md          # 9 tools
│   ├── cross-mcp-workflows.md     # KB + ITSM + CS
│   └── examples.md                # Search, create, gap analysis
├── README.md
└── LICENSE
```

## Example

**User:** "How do I reset my password?"

**Agent behavior:**
1. Searches KB: `search_articles(query: "password reset")`
2. Finds match (score: 15.2) → presents steps directly
3. No ticket created — resolved from knowledge base

## Scripts

### `score_relevance.py`
```bash
python scripts/score_relevance.py '{"query": "VPN timeout", "articles": [{"title": "VPN Troubleshooting", "body": "..."}]}'
# → [{"title": "VPN Troubleshooting", "score": 13}]
```

## Success Criteria

| Metric | Target |
|--------|--------|
| KB deflection rate | 40%+ issues resolved without ticket |
| Gap detection | Surface top unmatched queries weekly |
| Article freshness | Flag stale content (> 90 days unreviewed) |

## Contributors

| [<img src="https://github.com/jkmaina.png" width="80px;"/><br /><sub><b>James Karanja Maina</b></sub>](https://github.com/jkmaina) |
|:---:|

## License

Apache-2.0 — Part of [ADK-Rust Enterprise](https://enterprise.adk-rust.com). Built with ❤️ by [Zavora AI](https://zavora.ai)
