import numpy as np
from google import genai
import os

# create client once
client = genai.Client(api_key=os.getenv("GOOGLE_GENAI_API_KEY"))

EMBEDDING_MODEL = "gemini-embedding-001"

def embed_text(text: str) -> np.ndarray:
    """Convert text into a vector."""
    resp = client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=text,
    )

    return np.array(resp.embeddings[0].values, dtype=np.float32)