# 🧠 PDF Document Summarization Tool

This tool allows users to upload a PDF document, extract its text, and generate an AI-powered summary using Hugging Face's `facebook/bart-large-cnn` model.

## 🔧 Tech Stack
- Python 3.10+
- Streamlit (Web UI)
- PyMuPDF (PDF text extraction)
- Hugging Face Transformers (Summarization)

## 🚀 How to Use
1. Upload any `.pdf` document.
2. Wait for the text to be extracted.
3. Click "Summarize" to generate a summary.
4. Review and copy your results.

## 💻 Local Setup

```bash
pip install -r requirements.txt
streamlit run app.py
