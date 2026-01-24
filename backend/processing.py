from pypdf import PdfReader
from services.docx_reader import read_docx
from services.ocr import extract_text_from_image
from utils.text_splitter import split_text


def process_document(local_path: str, filename: str):
    """
    Extract text from a locally stored document and return chunks
    with page references.
    """

    chunks = []

    # ---------- PDF ----------
    if filename.lower().endswith(".pdf"):
        reader = PdfReader(local_path)
        for page_number, page in enumerate(reader.pages, start=1):
            text = page.extract_text() or ""
            for chunk in split_text(text):
                chunks.append({
                    "text": chunk,
                    "page": page_number
                })

    # ---------- DOCX ----------
    elif filename.lower().endswith(".docx"):
        text = read_docx(local_path)
        for chunk in split_text(text):
            chunks.append({
                "text": chunk,
                "page": "N/A"
            })

    # ---------- IMAGE ----------
    elif filename.lower().endswith((".png", ".jpg", ".jpeg")):
        text = extract_text_from_image(local_path)
        for chunk in split_text(text):
            chunks.append({
                "text": chunk,
                "page": "N/A"
            })

    return chunks
