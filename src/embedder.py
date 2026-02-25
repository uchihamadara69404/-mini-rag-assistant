from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle
import os

model = SentenceTransformer("all-MiniLM-L6-v2")

def create_index(chunks):
    embeddings = model.encode(chunks)
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))
    return index, embeddings

def save_index(index, chunks):
    os.makedirs("embeddings", exist_ok=True)
    faiss.write_index(index, "embeddings/vector_index.faiss")
    with open("embeddings/chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)