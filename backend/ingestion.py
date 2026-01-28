import uuid
import os
from services.blob_storage import upload_file

UPLOAD_DIR = "data/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


def ingest_file(uploaded_file):
    document_id = str(uuid.uuid4())
    filename = uploaded_file.name

    # ✅ SAVE LOCALLY
    local_path = os.path.join(UPLOAD_DIR, f"{document_id}_{filename}")
    with open(local_path, "wb") as f:
        f.write(uploaded_file.getvalue())

    # ✅ UPLOAD TO BLOB (BYTES, NOT BUFFER)
    blob_url = upload_file(
        file_bytes=uploaded_file.getvalue(),
        filename=f"{document_id}_{filename}"
    )

    return {
        "document_id": document_id,
        "filename": filename,
        "local_path": local_path,
        "blob_url": blob_url
    }
