import json
import faiss
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

indexes = {}
texts = {}

for cat in ["theory", "code", "edge_cases", "complexity"]:
    indexes[cat] = faiss.read_index(f"indexes/{cat}.index")
    with open(f"indexes/{cat}_texts.json", "r", encoding="utf-8") as f:
        texts[cat] = json.load(f)

def retrieve(query, category, k=1):
    q_emb = model.encode([query])
    D, I = indexes[category].search(q_emb, k)
    return texts[category][I[0][0]]
