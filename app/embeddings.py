import os
from dotenv import load_dotenv
from openai import OpenAI
import chromadb
from chromadb.utils import embedding_functions

from app.loaders import load_pdfs_from_directory, chunk_text


# Load environment variables
load_dotenv(dotenv_path=".env")

print("DEBUG KEY:", os.getenv("OPENAI_API_KEY"))


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in environment variables.")


def create_vector_store():
    # Load and chunk documents
    print("Loading documents...")
    text = load_pdfs_from_directory("data/raw_docs")
    chunks = chunk_text(text)

    print(f"Total chunks to embed: {len(chunks)}")

    # Initialize Chroma client
    client = chromadb.Client()

    # OpenAI embedding function
    embedding_function = embedding_functions.OpenAIEmbeddingFunction(
        api_key=OPENAI_API_KEY,
        model_name="text-embedding-3-small"
    )

    # Create or get collection
    collection = client.get_or_create_collection(
        name="enterprise_docs",
        embedding_function=embedding_function
    )

    # Add documents
    print("Creating embeddings and storing in vector DB...")
    collection.add(
        documents=chunks,
        ids=[f"id_{i}" for i in range(len(chunks))]
    )

    print("Vector store created successfully!")


if __name__ == "__main__":
    create_vector_store()
