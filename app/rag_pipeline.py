from loaders import load_pdfs_from_directory, chunk_text
from embeddings import get_embeddings
from vector_store import create_faiss_index


def build_pipeline():
    text = load_pdfs_from_directory("data/raw_docs")
    chunks = chunk_text(text)

    embeddings = get_embeddings(chunks)
    index = create_faiss_index(embeddings)

    print("RAG pipeline built successfully")
    print(f"Total chunks: {len(chunks)}")

    return chunks, index


if __name__ == "__main__":
    build_pipeline()
