# app.py

import streamlit as st
import fitz  # PyMuPDF
from summarizer import summarize_text

st.set_page_config(page_title="PDF Summarizer", layout="wide")
st.title("📄 PDF Document Summarizer")

# PDF Text Extraction Function
def extract_text_from_pdf(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Upload PDF
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file:
    with st.spinner("Extracting text from PDF..."):
        pdf_text = extract_text_from_pdf(uploaded_file)
        st.success("Text extracted successfully!")
        st.text_area("📜 Extracted Text (first 3000 chars)", pdf_text[:3000], height=200)

    # Summarize button
    if st.button("Summarize"):
        with st.spinner("Summarizing using BART model..."):
            summary = summarize_text(pdf_text)
            st.success("Summary generated!")
            st.text_area("📝 Summary", summary, height=200)
