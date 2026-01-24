import os
from openai import AzureOpenAI
from backend.vector_store import search_chunks

# -----------------------------
# Azure OpenAI Client
# -----------------------------
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
)


# -----------------------------
# Agent
# -----------------------------
def ask_agent(question: str):
    retrieved_chunks = search_chunks(question)

    if not retrieved_chunks:
        return "The document does not contain relevant information to answer this question."

    context = "\n\n".join(
        f"(Page {c['page']}): {c['text']}"
        for c in retrieved_chunks
    )

    system_prompt = """
You are a document-based AI assistant.
Answer ONLY using the provided document context.
If the answer is not present in the document, say so clearly.
Include page references where applicable.
"""

    response = client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT"),
        messages=[
            {"role": "system", "content": system_prompt},
            {
                "role": "user",
                "content": f"Document context:\n{context}\n\nQuestion:\n{question}"
            }
        ]
    )

    return response.choices[0].message.content
