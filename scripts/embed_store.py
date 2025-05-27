import numpy as np
import os
import pickle
import faiss
from extract_text import extract_text_from_pdfs

# Dummy embedding function — replace with your own embedder
def embed_texts(texts):
    import numpy as np
    embeddings = []
    for text in texts:
        # For example, embedding size 128, random vector
        vec = np.random.rand(128).astype('float32')
        embeddings.append(vec)
    return embeddings

def main():
    pdf_folder = 'docs'
    texts = extract_text_from_pdfs(pdf_folder)
    embeddings = embed_texts(texts)

    dim = len(embeddings[0])
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))

    if not os.path.exists('embeddings'):
        os.makedirs('embeddings')

    faiss.write_index(index, 'embeddings/faiss_index.idx')
    with open('embeddings/sentences.pkl', 'wb') as f:
        pickle.dump(texts, f)

    print("Embedding and index creation complete.")

if __name__ == "__main__":
    main()
