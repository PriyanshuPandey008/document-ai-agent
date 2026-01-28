import os
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

load_dotenv()

CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
CONTAINER_NAME = os.getenv("AZURE_STORAGE_CONTAINER_NAME")

if not CONNECTION_STRING:
    raise ValueError("AZURE_STORAGE_CONNECTION_STRING missing in .env")

if not CONTAINER_NAME:
    raise ValueError("AZURE_STORAGE_CONTAINER_NAME missing in .env")

blob_service = BlobServiceClient.from_connection_string(CONNECTION_STRING)
container_client = blob_service.get_container_client(CONTAINER_NAME)


def upload_file(file_bytes: bytes, filename: str) -> str:
    blob_client = container_client.get_blob_client(filename)

    blob_client.upload_blob(
        file_bytes,           
        overwrite=True
    )

    return blob_client.url
