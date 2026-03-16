import requests

OLLAMA_URL = "http://localhost:11434/api/generate"


def generate_response(prompt):

    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }

    try:
        r = requests.post(OLLAMA_URL, json=payload, timeout=30)

        data = r.json()

        return data.get("response", "No response from model.")

    except Exception:

        # fallback if ollama not running
        return f"AI Response (fallback): {prompt}"