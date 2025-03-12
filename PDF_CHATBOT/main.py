from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from src.pdf_utils import download_pdf,read_pdf
from src.vector_db import store_documents
from src.response import get_response,update_history


app = FastAPI(title="PDF CHATBOT")


class PdfUpload(BaseModel):
    url:str
    session_id:str

@app.post("/upload_pdf")
def upload_pdf(request:PdfUpload):
    file_path = download_pdf(url=request.url,session_id=request.session_id)
    chunks = read_pdf(file_path=file_path)
    msg = store_documents(chunks=chunks,session_id=request.session_id)
    return msg


class Chat(BaseModel):
    query:str
    session_id:str

@app.post("/chat")
def upload_pdf(request:Chat):
    response = get_response(query=request.query,session_id=request.session_id)
    update_history(session_id=request.session_id,user_input=request.query,bot_response=response)
    return response


if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0",port=7777)