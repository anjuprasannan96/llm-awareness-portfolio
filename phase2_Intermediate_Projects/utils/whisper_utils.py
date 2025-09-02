import whisper

def transcribe_audio(file_path):
    """Transcribe audio file using Whisper."""
    model = whisper.load_model("medium")
    result = model.transcribe(file_path)
    return result["text"]
