import os
import faiss
import numpy as np
from openai import AzureOpenAI

# -----------------------------
# Azure OpenAI Client
# -----------------------------
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
)

# -----------------------------
# Vector Store Setup
# -----------------------------
VECTOR_DIR = "data/vector_store"
VECTOR_PATH = os.path.join(VECTOR_DIR, "index.faiss")

os.makedirs(VECTOR_DIR, exist_ok=True)

EMBEDDING_DIM = 1536  # text-embedding-3-small
index = faiss.IndexFlatL2(EMBEDDING_DIM)

documents = []  # Stores metadata aligned with FAISS index


# -----------------------------
# Embeddings
# -----------------------------
def embed_texts(texts):
    response = client.embeddings.create(
        model=os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT"),
        input=texts
    )
    return [item.embedding for item in response.data]


# -----------------------------
# Store Chunks
# -----------------------------
def store_chunks(chunks):
    texts = [c["text"] for c in chunks]
    embeddings = embed_texts(texts)

    index.add(np.array(embeddings).astype("float32"))
    documents.extend(chunks)

    faiss.write_index(index, VECTOR_PATH)


# -----------------------------
# Search
# -----------------------------
def search_chunks(query, k=3):
    query_embedding = embed_texts([query])[0]

    distances, indices = index.search(
        np.array([query_embedding]).astype("float32"),
        k
    )

    return [documents[i] for i in indices[0]]
