import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3"

def query_llama3(prompt: str) -> str:
    """Send prompt to LLaMA3 via Ollama."""
    response = requests.post(
        OLLAMA_URL,
        json={"model": MODEL_NAME, "prompt": prompt, "stream": False}
    )
    if response.status_code == 200:
        return response.json().get("response", "")
    else:
        return f"Error: {response.text}"
