# System Architecture

## Overview

The Document AI Agent is designed as a modular, scalable system that separates concerns between
document ingestion, processing, retrieval, and answer generation.

The architecture prioritizes:
- Correctness and grounding
- Security-first design
- Easy extensibility
- Azure-native services

---

## High-Level Components

### 1. Frontend (Streamlit)
- Provides a simple web interface for document upload and question answering
- Handles user interaction and feedback
- Does not perform any business logic

---

### 2. Document Ingestion Layer
- Receives uploaded documents
- Generates a unique `document_id`
- Stores documents securely in Azure Blob Storage
- Maintains metadata such as filename and timestamp

---

### 3. Document Processing Layer
- Extracts text from documents
- Splits content into overlapping chunks
- Associates metadata (page number, chunk index) with each chunk
- Designed to support OCR as a pluggable extension

---

### 4. Embedding & Vector Store
- Uses Azure OpenAI embeddings (`text-embedding-3-small`)
- Stores embeddings in a FAISS vector index
- Enables fast semantic similarity search

---

### 5. Agent Orchestration Layer
- Receives user queries
- Retrieves relevant document chunks using vector search
- Injects retrieved context into a strict system prompt
- Calls Azure OpenAI chat model (`gpt-5-nano`) for answer generation

---

### 6. Answer Generation
- Produces concise, grounded answers
- Includes page-level references
- Explicitly denies answers when information is not present

---

## Design Decisions

| Decision | Rationale |
|--------|-----------|
| FAISS | Lightweight, fast prototyping |
| Azure OpenAI | Enterprise-grade AI models |
| Blob Storage | Secure and scalable file storage |
| Streamlit | Rapid prototyping and demos |

---

## Scalability Path

The architecture is designed to evolve into:
- Azure AI Search instead of FAISS
- Event-driven ingestion using Azure Functions
- Managed identity–based authentication
- Multi-tenant document isolation
