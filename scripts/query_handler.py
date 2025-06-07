import pickle
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
def load_index_and_sentences():
    index = faiss.read_index("embeddings/faiss_index.idx")
    with open("embeddings/sentences.pkl", "rb") as f:
        sentences = pickle.load(f)
    return index, sentences
# Load model once for efficiency
model = SentenceTransformer('all-MiniLM-L6-v2')
def embed_query(query):
    return model.encode([query], convert_to_numpy=True)[0]

def get_answer(query, top_k=1, threshold=1.0):
    index, sentences = load_index_and_sentences()
    query_vector = embed_query(query).reshape(1, -1)
    distances, indices = index.search(query_vector, top_k)

    results = []
    for dist, idx in zip(distances[0], indices[0]):
        if dist < threshold:
            results.append(sentences[idx])
    return results