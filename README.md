# 📄 Document AI Agent (Azure OpenAI)

A document-grounded AI assistant that allows users to upload documents and ask questions **strictly based on the uploaded content**, with clear page-level references.

This prototype demonstrates end-to-end document ingestion, processing, semantic retrieval, and answer generation using **Azure OpenAI foundation models** and **Azure Blob Storage**, following scalable and secure architectural principles.

---

## 🎯 Objective

Build a prototype AI agent that can:

- Read arbitrary user-uploaded documents (PDF, DOCX, PNG, JPG, etc.)
- Extract and index document content
- Retrieve relevant information using semantic search
- Generate answers **grounded only in the uploaded document**
- Explicitly state when information is not present
- Demonstrate architectural thinking, scalability, and Azure integration

---

## 🚀 Key Features

- 📤 Upload documents via a modern web UI
- ☁️ Secure storage in Azure Blob Storage
- 📄 Text extraction and intelligent chunking
- 🧠 Vector embeddings using Azure OpenAI
- 🔍 Semantic retrieval via vector search
- 💬 Context-grounded question answering
- 📑 Page-level references in answers
- 🎨 Enhanced Streamlit UI

---

## 🧠 Supported Document Formats

| Format | Status |
|------|-------|
| PDF (text-based) | ✅ Supported |
| DOCX | ✅ Supported |
| PNG / JPG / JPEG | ⚠️ OCR-ready |
| Scanned PDFs | ⚠️ OCR-ready |

> Image-based documents are architected for OCR support and can be enabled using **Azure AI Vision** or **Tesseract OCR** in future iterations.