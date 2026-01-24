# High-Level Design (HLD)

## 1. Purpose

This document describes the high-level architecture and design decisions of the
**Document AI Agent** system.

The objective of the design is to create a **scalable, secure, and modular**
document-based AI agent that can ingest documents, index them, and answer
user questions strictly grounded in the document content.

---

## 2. System Overview

The system is designed as a **multi-layered architecture** with clear separation
of responsibilities between frontend, backend services, storage, and AI models.

At a high level, the system consists of:
- A user-facing frontend
- A document ingestion and processing backend
- A vector-based retrieval layer
- An AI reasoning layer using Azure OpenAI

---

## 3. High-Level Architecture Diagram

┌────────────────────┐
│ User │
│ (Web Browser) │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ Streamlit UI │
│ (Frontend Layer) │
└─────────┬──────────┘
          │
          ▼
┌───────────────────────────┐
│ Document Ingestion Layer │
│ - Generate document_id │
│ - Store metadata │
└─────────┬─────────────────┘
          │
          ▼
┌───────────────────────────┐
│ Azure Blob Storage │
│ (Private Container) │
└─────────┬─────────────────┘
          │
          ▼
┌───────────────────────────┐
│ Document Processing Layer │
│ - Text extraction │
│ - Chunking │
└─────────┬─────────────────┘
          │
          ▼
┌───────────────────────────┐
│ Embedding Layer │
│ Azure OpenAI │
│ (text-embedding-3-small) │
└─────────┬─────────────────┘
          │
          ▼
┌───────────────────────────┐
│ Vector Store │
│ (FAISS) │
└─────────┬─────────────────┘
          │
          ▼
┌───────────────────────────┐
│ Agent Orchestration │
│ - Context retrieval │
│ - Prompt enforcement │
└─────────┬─────────────────┘
          │
          ▼
┌───────────────────────────┐
│ Azure OpenAI Chat Model │
│ (GPT-5-nano) │
└─────────┬─────────────────┘
          │
          ▼
┌────────────────────┐
│ Grounded Answer │
│ + Page References │
└────────────────────┘


---

## 4. Component-Level Design

### 4.1 Frontend Layer
- Built using Streamlit
- Responsible for:
  - Document upload
  - User question input
  - Displaying answers and references
- Does not contain business logic

---

### 4.2 Document Ingestion Layer
- Accepts uploaded files
- Generates a unique `document_id`
- Stores documents in Azure Blob Storage
- Records metadata such as filename and timestamp

---

### 4.3 Document Processing Layer
- Extracts text from documents
- Splits text into overlapping chunks
- Associates metadata (page number, chunk index)
- Designed to support OCR as a future enhancement

---

### 4.4 Embedding & Vector Store Layer
- Converts text chunks into embeddings using Azure OpenAI
- Stores embeddings in FAISS for fast similarity search
- Enables semantic retrieval of document content

---

### 4.5 Agent Orchestration Layer
- Receives user question
- Retrieves relevant chunks using vector similarity
- Injects retrieved content into a strict system prompt
- Ensures no external knowledge is used

---

### 4.6 AI Reasoning Layer
- Uses Azure OpenAI chat model (GPT-5-nano)
- Generates concise, factual answers
- Explicitly states when information is not present
- Includes page-level references

---

## 5. Design Principles

- **Separation of concerns**
- **Security-first architecture**
- **Strict grounding guarantees**
- **Scalability and extensibility**
- **Cloud-native design**

---

## 6. Scalability Considerations

The design supports future scaling by:
- Replacing FAISS with Azure AI Search
- Adding Azure Functions for automated ingestion
- Supporting multi-document and multi-user scenarios
- Horizontal scaling of frontend and backend services

---

## 7. Non-Functional Requirements

| Requirement | Approach |
|------------|---------|
| Security | Private Blob Storage, RBAC (planned) |
| Performance | Chunking + vector search |
| Reliability | Stateless frontend |
| Maintainability | Modular backend |
| Extensibility | Pluggable OCR and vector DB |

---

## 8. Conclusion

This High-Level Design ensures the system is:
- Robust and secure
- Easy to extend
- Aligned with enterprise and Azure best practices
- Suitable for production evolution beyond the prototype stage
