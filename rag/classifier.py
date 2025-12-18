def classify_query(query: str):
    needs = ["theory"]
    q = query.lower()

    if "code" in q or "implement" in q:
        needs.append("code")
    if "edge" in q:
        needs.append("edge_cases")
    if "complexity" in q:
        needs.append("complexity")

    return needs
