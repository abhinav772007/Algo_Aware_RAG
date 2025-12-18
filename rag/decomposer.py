def decompose(query: str):
    return {
        "theory": f"Explain {query}",
        "code": f"{query} implementation",
        "edge_cases": f"{query} edge cases",
        "complexity": f"{query} time and space complexity"
    }
