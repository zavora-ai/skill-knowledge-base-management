# Knowledge Base Tool Sequences

## Tools (9)
| Tool | Purpose |
|------|---------|
| `search_articles` | TF-IDF ranked search |
| `get_article` | Full article content |
| `find_related` | Related articles |
| `create_draft` | Draft new article |
| `suggest_update` | Propose edit to existing |
| `publish_article` | Make draft live |
| `record_feedback` | Helpful/not helpful |
| `list_articles` | All articles by category |
| `get_knowledge_gaps` | Queries with no matches |

## Sequence: Search-First Resolution (1-2 calls)
```
1. search_articles(query: "VPN connection timeout")
   → [{title: "VPN Troubleshooting", score: 13.3, id: "kb_12"}]
2. get_article(id: "kb_12") → full steps
→ If score > 10: resolve from KB, no ticket needed
```

## Sequence: Create from Resolution (2 calls)
```
1. create_draft(title: "Fix: Payment webhook timeout", body: "## Problem\n...\n## Solution\n...", category: "engineering", tags: ["payments", "webhooks"])
2. publish_article(id: "draft_123") → {status: "published", url: "..."}
```

## Sequence: Gap Analysis (1 call)
```
1. get_knowledge_gaps() → [{query: "SSO setup", frequency: 12, articles: 0}, ...]
→ Top gaps = articles that need to be written
```
