# End-to-End Data Flow

This document describes how data flows through the system from upload to answer.

---

## Step 1: Document Upload

- User uploads a document via the Streamlit UI
- Supported formats: PDF, DOCX, PNG, JPG
- A unique `document_id` is generated

---

## Step 2: Secure Storage

- Document is uploaded to Azure Blob Storage
- Blob container has public access disabled
- Metadata is recorded:
  - document_id
  - filename
  - timestamp

---

## Step 3: Local Processing

- A local copy of the document is used for processing
- Prevents the need for public blob access
- Improves performance and security

---

## Step 4: Text Extraction

- PDF: extracted using PyPDF
- DOCX: extracted using python-docx
- Images: OCR-ready (future enhancement)

---

## Step 5: Chunking

- Extracted text is split into overlapping chunks
- Each chunk stores:
  - document_id
  - page number
  - chunk index

---

## Step 6: Embedding Generation

- Chunks are converted into vectors using Azure OpenAI embeddings
- Model used: `text-embedding-3-small`

---

## Step 7: Vector Indexing

- Embeddings stored in FAISS index
- Enables semantic similarity search

---

## Step 8: Question Answering

- User submits a question
- Vector search retrieves top-k relevant chunks
- Retrieved context is passed to the AI agent

---

## Step 9: Answer Generation

- Azure OpenAI chat model generates an answer
- Answer is strictly grounded in retrieved context
- Page references are included
- If information is missing, the agent explicitly states so
