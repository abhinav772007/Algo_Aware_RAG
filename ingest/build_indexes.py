import os
import json

os.environ["TRANSFORMERS_NO_TF"] = "1"

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


model = SentenceTransformer("all-MiniLM-L6-v2")

CATEGORIES = ["theory", "code", "edge_cases", "complexity"]
DATA_DIR = "data"
INDEX_DIR = "indexes"

os.makedirs(INDEX_DIR, exist_ok=True)

for category in CATEGORIES:
    texts = []

    for algo in os.listdir(DATA_DIR):
        if category == "code":


            path = os.path.join(DATA_DIR, algo, "code.cpp")
        else:
             
            path = os.path.join(DATA_DIR, algo, f"{category}.txt")

        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                texts.append(f.read())

    print(f"{category}: number of texts =", len(texts))

    embeddings = model.encode(texts, convert_to_numpy=True)

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    faiss.write_index(index, f"{INDEX_DIR}/{category}.index")
    with open(f"{INDEX_DIR}/{category}_texts.json", "w", encoding="utf-8") as f:
        

        json.dump(texts, f, indent=2)


    print(f" Built index for {category} with {len(texts)} entries")





