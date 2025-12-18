import streamlit as st

from rag.classifier import classify_query
from rag.decomposer import decompose
from rag.retriever import retrieve
from rag.assembler import assemble
from rag.generator import generate_answer
from rag.splitter import split_query

from evaluation.evaluator import evaluate


# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Algo-Aware RAG Tutor",
    layout="wide"
)

st.title("📘 Algo-Aware RAG Tutor")
st.write(
    "Ask algorithm questions and get **hallucination-safe, structured explanations** "
    "powered by Retrieval-Augmented Generation."
)

# ---------------- Input ----------------
query = st.text_input(
    "Ask an algorithm question",
    placeholder="e.g. Explain how to implement BFS and Binary Search"
)

# ---------------- Run Pipeline ----------------
if st.button("Generate Answer"):
    if not query.strip():
        st.warning("Please enter a valid question.")
    else:
        with st.spinner("Retrieving knowledge and generating answers..."):
            # Split query into individual algorithms
            algorithms = split_query(query)

            for algo in algorithms:
                st.markdown(f"## 🔹 {algo.upper()}")

                # 1. Classify required knowledge
                needs = classify_query(algo)

                # 2. Decompose query
                sub_queries = decompose(algo)

                # 3. Retrieve context
                contexts = {}
                for cat in needs:
                    contexts[cat] = retrieve(sub_queries[cat], cat)

                # 4. Assemble context
                context = assemble(contexts)

                # 5. Generate answer
                answer = generate_answer(context, algo)

                # 6. Evaluate
                report = evaluate(answer, context, algo)

                # -------- Display Answer --------
                st.markdown("### ✅ Answer")
                st.markdown(answer)

                # -------- Display Evaluation --------
                with st.expander("📊 Evaluation Report"):
                    col1, col2, col3 = st.columns(3)

                    with col1:
                        st.markdown("**Completeness**")
                        st.json(report["completeness"])

                    with col2:
                        st.markdown("**Hallucination**")
                        st.json(report["hallucination"])

                    with col3:
                        st.markdown("**Relevance**")
                        st.json(report["relevance"])
