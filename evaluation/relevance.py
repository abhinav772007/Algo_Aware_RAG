def check_relevance(answer: str, query: str):
    keywords = query.lower().split()
    answer_lower = answer.lower()

    hits = sum(1 for k in keywords if k in answer_lower)

    return {
        "keyword_hits": hits,
        "is_relevant": hits >= max(1, len(keywords)//3)
    }
