import numpy as np
import os
import pickle
import faiss
from extract_text import extract_text_from_pdfs
# Use sentence-transformers for real embeddings
from sentence_transformers import SentenceTransformer
def embed_texts(texts):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(texts, convert_to_numpy=True)
    return embeddings

def main():
    pdf_folder = 'docs'
    texts = extract_text_from_pdfs(pdf_folder)
    embeddings = embed_texts(texts)

    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    if not os.path.exists('embeddings'):
        os.makedirs('embeddings')

    faiss.write_index(index, 'embeddings/faiss_index.idx')
    with open('embeddings/sentences.pkl', 'wb') as f:
        pickle.dump(texts, f)

    print("Embedding and index creation complete.")

if __name__ == "__main__":
    main()