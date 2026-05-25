---
name: knowledge-base-management
description: Manage knowledge base — search articles, find related content, create drafts, publish articles, collect feedback, and detect knowledge gaps. Use when searching for solutions, creating KB articles, finding related content, identifying gaps, or improving article quality.
version: "1.0.0"
license: Apache-2.0
allowed-tools: [search_articles, get_article, find_related, create_draft, suggest_update, publish_article, record_feedback, list_articles, get_knowledge_gaps]
tags: [communication, knowledge-base, documentation, search]
metadata:
  author: Zavora AI
  mcp-server: mcp-knowledge-base
---

# Knowledge Base Management

Search-first knowledge management. Find answers before creating tickets. Grow the KB from resolved issues.

## Decision Tree
```
├── "search", "find article", "how to"? → search_articles / find_related
├── "create article", "document this"? → create_draft → publish_article
├── "update", "improve", "outdated"? → suggest_update
├── "gaps", "missing", "what's needed"? → get_knowledge_gaps
├── "feedback", "helpful?"? → record_feedback
```

## MUST DO
- Always search before creating (avoid duplicates)
- Cite sources — never present ungrounded info as KB content
- Track article freshness — flag stale content
- Create articles from resolved incidents (grow the KB)

## MUST NOT DO
- Don't publish without review
- Don't present outdated articles without flagging staleness
