import re

STOPWORDS = {
    "the", "is", "a", "an", "and", "or", "to", "of", "in", "for", "on", "with",
    "that", "this", "it", "as", "are", "be", "by", "from"
}

def tokenize(text):
    words = re.findall(r"[a-zA-Z]+", text.lower())
    return {w for w in words if w not in STOPWORDS}


def check_hallucination(answer: str, retrieved_context: str):
    hallucinated = []

    context_tokens = tokenize(retrieved_context)

    for line in answer.splitlines():
        line = line.strip()

        # Skip headings, code fences, empty lines
        if (
            not line
            or line.startswith(("1.", "2.", "3.", "4.", "5.", "6."))
            or line.startswith("```")
            or "Not found in context" in line
        ):
            continue

        line_tokens = tokenize(line)

        # If line introduces mostly unseen concepts
        if line_tokens and len(line_tokens & context_tokens) / len(line_tokens) < 0.3:
            hallucinated.append(line)

    return {
        "hallucinated_lines": hallucinated,
        "is_hallucinated": len(hallucinated) > 0
    }
