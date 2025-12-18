import faiss
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index("indexes/theory.index")

query = "Explain BFS traversal"
q_emb = model.encode([query])

D, I = index.search(q_emb, 1)
print("Retrieved index:", I[0][0])
