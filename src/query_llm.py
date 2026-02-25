import os
import requests

PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")

def query_llm(chunks, question):
    context = "\n\n".join(chunks)

    prompt = f"""
    Answer the question using ONLY the context below.

    Context:
    {context}

    Question: {question}
    """

    response = requests.post(
        "https://api.perplexity.ai/v1/generate",
        headers={
            "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "prompt": prompt,
            "max_tokens": 200
        }
    )

    return response.json()