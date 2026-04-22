from google import genai
import os

# shared client
client = genai.Client(api_key=os.getenv("GOOGLE_GENAI_API_KEY"))

CHAT_MODEL = "gemini-3-flash-preview"

def generate_answer(prompt: str) -> str:
    """Send prompt to model and get answer."""
    resp = client.models.generate_content(
        model=CHAT_MODEL,
        contents=prompt,
    )

    return resp.text