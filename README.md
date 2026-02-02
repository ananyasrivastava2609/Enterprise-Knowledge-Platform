# Enterprise-Knowledge-Platform using RAG

This project aims to build an enterprise-grade knowledge platform using Retrieval-Augmented Generation (RAG) that enables users to query internal documents and receive real-time, document-accurate responses. The system focuses on reducing hallucinations by grounding LLM outputs strictly in retrieved document context and is deployed using DevOps automation for continuous integration and delivery.

overview
This project aims to build an enterprise-grade knowledge platform using Retrieval-Augmented Generation (RAG) that enables users to query internal documents and receive real-time, document-accurate responses. The system focuses on reducing hallucinations by grounding LLM outputs strictly in retrieved document context and is deployed using DevOps automation for continuous integration and delivery.

## Architecture Overview

1. Document ingestion and preprocessing
2. Text chunking and embedding generation
3. Vector storage using FAISS/Chroma
4. Query-based retrieval of relevant chunks
5. LLM-based response generation grounded in retrieved context
6. Automated deployment using Docker and GitHub Actions


## Tech Stack

- Language: Python
- Backend: FastAPI
- LLM: OpenAI / Gemini / Claude
- Embeddings: OpenAI Embeddings
- Vector Store: FAISS / Chroma
- Containerization: Docker
- CI/CD: GitHub Actions
- Deployment: Cloud VM / Platform-as-a-Service


## Project Structure

enterprise-knowledge-rag/
├── app/
├── data/
├── tests/
├── .github/workflows
├── Dockerfile
├── requirements.txt
└── README.md
