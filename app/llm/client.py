from google import genai
import os

client = genai.Client(api_key=os.getenv("GOOGLE_GENAI_API_KEY"))

CHAT_MODEL = "gemini-3-flash-preview"

def generate_answer(prompt: str) -> str:
    """Send prompt to model with controlled generation settings."""
    
    resp = client.models.generate_content(
        model=CHAT_MODEL,
        contents=prompt,
        generation_config={
            "temperature": 0.3,   # lower = more factual
            "top_p": 0.9,         # controls randomness
            "max_output_tokens": 400
        }
    )

    return resp.text