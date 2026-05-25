# Knowledge Base Cross-MCP Workflows

## KB + ITSM: Resolve from Knowledge
```
ITSM: handle_support_request(subject: "VPN timeout") → checks KB first
KB: search_articles(query: "VPN timeout") → {title: "VPN Troubleshooting", score: 13.3}
→ If match: resolve without ticket

## KB + ITSM: Create Article from Resolution
```
ITSM: close_ticket(id: "INC-1001", resolution: "Cleared DNS cache")
KB: create_draft(title: "Fix: VPN timeout — clear DNS cache", body: "## Steps\n1. ...", tags: ["vpn", "network"])
KB: publish_article(id: "draft_new")
```

## KB + Customer Service: Answer from KB
```
CS: get_conversation(id: "conv-5") → customer asks about billing
KB: search_articles(query: "billing pro-rated charges") → match found
CS: suggest_response(conversation_id: "conv-5") → uses KB article
CS: reply_conversation(id: "conv-5", body: response_from_kb)
```
