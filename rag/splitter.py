import re

KNOWN_ALGOS = [
    "bfs",
    "dfs",
    "binary search",
    "merge sort",
    "quick sort",
    "dijkstra",
]

def split_query(query: str):
    query = query.lower()
    found = []

    for algo in KNOWN_ALGOS:
        if re.search(rf"\b{algo}\b", query):
            found.append(algo)

    # fallback: treat as single query
    if not found:
        return [query]

    return found
