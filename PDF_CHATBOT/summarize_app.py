from streamlit_pdf_viewer import pdf_viewer
import streamlit as st
from sentence_transformers import SentenceTransformer



def pdf_summarizer():
    st.title("PDF Summarizer")
    pdf_file = st.file_uploader("Upload PDF file", type=('pdf'))
    if pdf_file:
        binary_data = pdf_file.getvalue()
        with st.sidebar:
            pdf_viewer(input=binary_data,
                    width=500)

        with fitz.open("uplands.pdf") as doc:  # open document
            text = chr(12).join([page.get_text() for page in doc])



selector = st.sidebar.radio("Summarizer",["youtube","pdf"])

if selector == "youtube":
    youtube_summarizer()
else:
    pdf_summarizer()

