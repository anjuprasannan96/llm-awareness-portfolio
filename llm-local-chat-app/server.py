from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import requests
import logging

logging.basicConfig(level=logging.DEBUG)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    prompt = data.get("prompt")

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "llama3", "prompt": prompt, "stream": False},
            timeout=60
        )
        response.raise_for_status()

        result = response.json()
        answer = result.get("response", "No response from model")

        return {"response": answer}

    except requests.exceptions.RequestException as e:
        logging.error(f"Error connecting to model API: {e}")
        return {"response": "Error: Unable to connect to model API"}
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return {"response": f"Error: {str(e)}"}
