from fastapi import UploadFile
import os
import uuid

UPLOAD_DIRECTORY = "uploads/product/images/"

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

def save_product_image ( file: UploadFile ) -> str:
    extension = file.filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{extension}"
    filepath = os.path.join(UPLOAD_DIRECTORY, filename)

    with open(filepath, "wb") as buffer:
        buffer.write( file.file.read() )

    return filepath