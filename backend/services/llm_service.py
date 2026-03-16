import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_response(prompt):

    payload = {
        "model":"llama3",
        "prompt":prompt,
        "stream":False
    }

    r = requests.post(OLLAMA_URL,json=payload)

    data = r.json()

    return data["response"]