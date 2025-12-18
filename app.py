from rag.classifier import classify_query
from rag.decomposer import decompose
from rag.retriever import retrieve
from rag.assembler import assemble
from rag.generator import generate_answer

from evaluation.evaluator import evaluate


def main():
    print("Algo-Aware RAG Tutor\n")

    query = input("Ask an algorithm question: ").strip()
    if not query:
        print("Please enter a valid question.")
        return

    # 1. Classify what information is needed
    needs = classify_query(query)

    # 2. Decompose query into sub-queries
    sub_queries = decompose(query)

    # 3. Retrieve relevant context
    contexts = {}
    for category in needs:
        contexts[category] = retrieve(sub_queries[category], category)

    # 4. Assemble context
    context = assemble(contexts)

    # 5. Generate answer using Gemini
    answer = generate_answer(context, query)

    # 6. Evaluate answer quality
    report = evaluate(answer, context, query)

    # 7. Print answer
    print("\n=== ANSWER ===\n")
    print(answer)

    # 8. Print evaluation report
    print("\n=== EVALUATION REPORT ===\n")

    print("Completeness:")
    print(report["completeness"])

    print("\nHallucination:")
    print(report["hallucination"])

    print("\nRelevance:")
    print(report["relevance"])



if __name__ == "__main__":
    main()
