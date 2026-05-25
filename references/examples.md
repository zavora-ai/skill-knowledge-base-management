# Knowledge Base Examples

## Example 1: "How do I reset my password?"
```
search_articles(query: "password reset") → [{title: "Password Reset Guide", score: 15.2}]
get_article(id: "kb_01") → step-by-step instructions
```
Response: Present article steps directly. No ticket needed.

## Example 2: "Create an article about the new SSO setup"
```
create_draft(title: "SSO Setup Guide", body: "...", category: "IT", tags: ["sso", "auth"])
publish_article(id: "draft_new")
```
Response: "✅ Published: SSO Setup Guide. This fills a knowledge gap (12 searches, 0 articles)."

## Example 3: "What knowledge gaps do we have?"
```
get_knowledge_gaps() → [{query: "SSO setup", freq: 12}, {query: "VPN split tunnel", freq: 8}]
```
Response: "Top gaps: SSO setup (12 searches, no article), VPN split tunnel (8 searches)."
