from evaluation.completeness import check_completeness
from evaluation.hallucination import check_hallucination
from evaluation.relevance import check_relevance

def evaluate(answer: str, context: str, query: str):
    return {
        "completeness": check_completeness(answer),
        "hallucination": check_hallucination(answer, context),
        "relevance": check_relevance(answer, query),
    }
