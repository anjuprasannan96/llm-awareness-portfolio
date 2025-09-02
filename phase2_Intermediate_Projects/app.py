import streamlit as st
from news_tracker import fetch_google_news, summarize_headlines_with_llama3
from multimodal_assistant import analyze_image_and_answer
from meeting_notes import extract_meeting_notes
import tempfile

st.set_page_config(page_title="Phase 2 Projects", layout="wide")
st.title("🚀 Phase 2 – Intermediate LLM Projects")

tab1, tab2, tab3 = st.tabs(["📰 Global News Tracker", "🖼 Multi-Modal Assistant", "🎤 Meeting Notes Extractor"])

# 📰 Tab 1 - News Tracker
with tab1:
    st.header("📰 Global News Topic Tracker")
    if st.button("Fetch Latest News"):
        headlines = fetch_google_news()
        st.write("### Latest Headlines:")
        for h in headlines:
            st.write(f"- {h}")
        st.write("### Summary of Trends:")
        st.write(summarize_headlines_with_llama3(headlines))

# 🖼 Tab 2 - Multi-Modal Assistant
with tab2:
    st.header("🖼 Multi-Modal Assistant")
    uploaded_image = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])
    question = st.text_input("Ask a question about the image")
    if uploaded_image and question:
        from PIL import Image
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        st.write("### Answer:")
        st.write(analyze_image_and_answer(image, question))

# 🎤 Tab 3 - Meeting Notes Extractor
with tab3:
    st.header("🎤 Meeting Notes & Action Item Extractor")
    uploaded_audio = st.file_uploader("Upload Meeting Audio", type=["mp3", "wav", "m4a"])
    if uploaded_audio:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
            tmp_file.write(uploaded_audio.read())
            audio_path = tmp_file.name
        st.write("### Extracted Notes & Actions:")
        st.write(extract_meeting_notes(audio_path))
