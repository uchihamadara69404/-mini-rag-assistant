# src/query_llm.py
import os
from perplexity import Perplexity

# Load API key from environment
PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")

# Initialize the Perplexity client
# No need to pass api_key here; by default it uses PERPLEXITY_API_KEY env var
client = Perplexity()

def query_llm(chunks, question):
    """
    Queries Perplexity's grounded LLM using the Agent API.
    """
    context = "\n\n".join(chunks)

    # Build the input combining context + question
    prompt = f"""
    You are an assistant that answers questions based on the context below.

    Context:
    {context}

    Question: {question}
    """

    # Use the responses API with a preset that does grounding
    response = client.responses.create(
        preset="pro-search",
        input=prompt
    )
    
    # The SDK provides .output_text which aggregates all text
    return response.output_text