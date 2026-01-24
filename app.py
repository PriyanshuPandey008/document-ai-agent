import streamlit as st
from dotenv import load_dotenv
from backend.ingestion import ingest_file
from backend.processing import process_document
from backend.vector_store import store_chunks
from backend.agent import ask_agent



# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Document AI Agent",
    page_icon="📄",
    layout="wide"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>
/* Typography */
.main-title {
    font-size: 2.4rem;
    font-weight: 700;
}
.subtle-text {
    color: #9ca3af;
}

/* Cards */
.card {
    background-color: #0f172a;
    padding: 1.2rem;
    border-radius: 12px;
    border: 1px solid #1e293b;
}

/* Answer Box */
.answer-box {
    background-color: #020617;
    padding: 1.2rem;
    border-radius: 10px;
    border-left: 4px solid #22c55e;
}

/* Buttons */
.stButton > button {
    background-color: #22c55e;
    color: black;
    font-weight: 600;
    border-radius: 8px;
    padding: 0.6rem 1.4rem;
}
.stButton > button:hover {
    background-color: #16a34a;
}

/* ✅ REMOVE "Press Enter to apply" */
[data-testid="stTextInput"] small {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# SIDEBAR
# -----------------------------
with st.sidebar:
    st.markdown("## 📊 Document Status")
    st.markdown("---")
    st.markdown("**Upload → Process → Ask Questions**")
    st.markdown(
        "<span class='subtle-text'>All answers are grounded strictly in the uploaded document.</span>",
        unsafe_allow_html=True
    )

# -----------------------------
# MAIN HEADER
# -----------------------------
st.markdown("<div class='main-title'>📄 Document AI Agent</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='subtle-text'>Upload a document and ask questions strictly grounded in its content.</div>",
    unsafe_allow_html=True
)
st.markdown("---")

# -----------------------------
# UPLOAD SECTION
# -----------------------------
st.markdown("### 📤 Upload Document")

uploaded = st.file_uploader(
    "",
    type=["pdf", "docx", "png", "jpg", "jpeg"]
)

document_ready = False
document_meta = None

if uploaded:
    with st.spinner("Uploading document to Azure Blob Storage..."):
        document_meta = ingest_file(uploaded)

    st.success("✅ Upload successful")

    with st.expander("📄 Document Metadata"):
        st.json(document_meta)

    # -----------------------------
    # PROCESS + INDEX
    # -----------------------------
    with st.spinner("Extracting, chunking, and indexing document..."):
        chunks = process_document(
            local_path=document_meta["local_path"],
            filename=document_meta["filename"]
        )
        store_chunks(chunks)

    st.success("✅ Document indexed and ready for questions")
    document_ready = True

# -----------------------------
# QUESTION SECTION
# -----------------------------
st.markdown("---")
st.markdown("### ❓ Ask a Question")

question = st.text_input(
    "Type your question here",
    placeholder="e.g. What is the main recommendation in the document?",
    disabled=not document_ready
)

ask_clicked = st.button("🔍 Ask Question", disabled=not document_ready)

if not document_ready:
    st.info("ℹ️ Please upload and process a document first.")

# -----------------------------
# ANSWER SECTION
# -----------------------------
if ask_clicked and question and document_ready:
    with st.spinner("Thinking..."):
        answer = ask_agent(question)

    st.markdown("### 🧠 Answer")
    st.markdown(f"<div class='answer-box'>{answer}</div>", unsafe_allow_html=True)
    st.success("✅ Answer generated")