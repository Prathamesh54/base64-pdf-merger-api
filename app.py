from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import base64
import binascii
from io import BytesIO
from pypdf import PdfReader, PdfWriter

app = FastAPI(title="Base64 PDF Merger API", version="1.0")


class MergeRequest(BaseModel):
    pdf1_base64: str
    pdf2_base64: str


class MergeResponse(BaseModel):
    merged_pdf_base64: str


def decode_base64_to_bytes(b64str: str, field_name: str) -> bytes:
    if not isinstance(b64str, str) or b64str.strip() == "":
        raise HTTPException(status_code=400, detail=f"{field_name} must be a non-empty Base64 string.")
    try:
        data = base64.b64decode(b64str, validate=True)
    except (binascii.Error, ValueError):
        raise HTTPException(status_code=400, detail=f"{field_name} is not valid Base64.")
    return data


def ensure_valid_pdf(pdf_bytes: bytes, field_name: str) -> BytesIO:
    stream = BytesIO(pdf_bytes)
    try:
        # Try to read PDF pages to validate
        PdfReader(stream)
    except Exception:
        raise HTTPException(status_code=400, detail=f"{field_name} does not appear to be a valid PDF or is corrupted.")
    stream.seek(0)
    return stream


@app.post("/merge-pdfs", response_model=MergeResponse)
def merge_pdfs(payload: MergeRequest):
    # 1. Decode inputs
    pdf1_bytes = decode_base64_to_bytes(payload.pdf1_base64, "pdf1_base64")
    pdf2_bytes = decode_base64_to_bytes(payload.pdf2_base64, "pdf2_base64")

    # 2. Validate PDFs and get streams
    pdf1_stream = ensure_valid_pdf(pdf1_bytes, "pdf1_base64")
    pdf2_stream = ensure_valid_pdf(pdf2_bytes, "pdf2_base64")

    # 3. Merge in-memory using PdfWriter (works across pypdf versions)
    writer = PdfWriter()
    try:
        reader1 = PdfReader(pdf1_stream)
        for p in reader1.pages:
            writer.add_page(p)

        reader2 = PdfReader(pdf2_stream)
        for p in reader2.pages:
            writer.add_page(p)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to read PDF pages: {str(e)}")

    output_stream = BytesIO()
    try:
        writer.write(output_stream)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to write merged PDF: {str(e)}")

    merged_bytes = output_stream.getvalue()
    merged_b64 = base64.b64encode(merged_bytes).decode("ascii")

    return {"merged_pdf_base64": merged_b64}
