import requests
import pymupdf




def download_pdf(url,session_id):
    res = requests.get(url).content
    file_path = f"data/pdf/{session_id}.pdf"
    with open(file_path,"wb") as f:
        f.write(res)
    return file_path
    



def read_pdf(file_path):
    doc = pymupdf.open(file_path) 
    return [page.get_text() for page in doc]
