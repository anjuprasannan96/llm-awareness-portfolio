from utils.llama3_utils import query_llama3
from utils.whisper_utils import transcribe_audio

def extract_meeting_notes(audio_file_path):
    """Extract meeting notes and action items from audio."""
    transcript = transcribe_audio(audio_file_path)
    prompt = f"""
You are an AI assistant that extracts structured meeting notes and action items.

Meeting transcript:
{transcript}

Return output in the following format:
- Summary:
- Action Items:
"""
    return query_llama3(prompt)
