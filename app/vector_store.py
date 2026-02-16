import faiss
import numpy as np


def create_faiss_index(embeddings):
    """
    Store embeddings in FAISS index.
    """
    dimension = len(embeddings[0])
    index = faiss.IndexFlatL2(dimension)

    vectors = np.array(embeddings).astype("float32")
    index.add(vectors)

    return index


def search_index(index, query_embedding, k=3):
    """
    Retrieve most relevant chunks.
    """
    query_vector = np.array([query_embedding]).astype("float32")
    distances, indices = index.search(query_vector, k)

    return indices[0]
