# app.py
import os
import shutil
from fastapi import FastAPI, UploadFile, HTTPException

from rag_pipline.ingest import split_text
from rag_pipline.embed import create_vector_store
from rag_pipline.generate import generate_response
from rag_pipline.retrieve import retrieve_chunks
from utils.parser import extract_text_from_pdf
from dotenv import load_dotenv

load_dotenv()


app = FastAPI()

UPLOAD_DIR = "uploads"

# ✅ Ensure folder exists
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.post("/analyze/")
async def analyze(resume: UploadFile, job_description: str):

    # ✅ Validate file type
    if not resume.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported")

    file_path = os.path.join(UPLOAD_DIR, resume.filename)

    # ✅ Save file safely
    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(resume.file, buffer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File save error: {str(e)}")

    # ✅ Extract text
    text = extract_text_from_pdf(file_path)

    if not text or text.strip() == "":
        raise HTTPException(status_code=400, detail="Could not extract text from PDF")

    # ✅ RAG Pipeline
    chunks = split_text(text)
    vectorstore = create_vector_store(chunks)

    retrieved_docs = retrieve_chunks(vectorstore, job_description)
    context = " ".join([doc.page_content for doc in retrieved_docs])

    # ✅ Generate response
    result = generate_response(context, job_description)

    return {
        "status": "success",
        "analysis": result.content
    }