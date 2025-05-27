import pickle
import faiss
import numpy as np

def load_index_and_sentences():
    index = faiss.read_index("embeddings/faiss_index.idx")
    with open("embeddings/sentences.pkl", "rb") as f:
        sentences = pickle.load(f)
    return index, sentences

def embed_query(query):
    import numpy as np
    return np.random.rand(128).astype('float32')

def get_answer(query, top_k=1):
    index, sentences = load_index_and_sentences()
    query_vector = embed_query(query).reshape(1, -1)
    distances, indices = index.search(query_vector, top_k)

    results = []
    for idx in indices[0]:
        results.append(sentences[idx])
    return results
