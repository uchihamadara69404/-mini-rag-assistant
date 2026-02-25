import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def load_index():
    index = faiss.read_index("embeddings/vector_index.faiss")
    with open("embeddings/chunks.pkl", "rb") as f:
        chunks = pickle.load(f)
    return index, chunks

def search(query, top_k=3):
    index, chunks = load_index()
    query_emb = model.encode([query])
    D, I = index.search(np.array(query_emb), top_k)
    return [chunks[i] for i in I[0]]