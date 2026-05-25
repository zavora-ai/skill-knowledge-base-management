#!/usr/bin/env python3
"""Score KB article relevance to a query using simple TF-IDF-like matching."""
import json, sys, re
from collections import Counter

def tokenize(text):
    return re.findall(r'\w+', text.lower())

def score(query, articles):
    query_tokens = set(tokenize(query))
    results = []
    for article in articles:
        title_tokens = set(tokenize(article.get("title", "")))
        body_tokens = Counter(tokenize(article.get("body", "")))
        # Score: title match = 3x, body match = 1x
        title_overlap = len(query_tokens & title_tokens) * 3
        body_overlap = sum(body_tokens.get(t, 0) for t in query_tokens)
        total = title_overlap + body_overlap
        if total > 0:
            results.append({"id": article.get("id"), "title": article.get("title"), "score": total})
    return sorted(results, key=lambda x: x["score"], reverse=True)[:5]

if __name__ == "__main__":
    data = json.loads(sys.argv[1])
    print(json.dumps(score(data["query"], data["articles"]), indent=2))
