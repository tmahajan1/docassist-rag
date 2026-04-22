import numpy as np
from ingestion.embedder import embed_text

def cosine_similarity(a, b):
    """Measure how similar two vectors are."""
    denom = (np.linalg.norm(a) * np.linalg.norm(b))
    return float(np.dot(a, b) / denom) if denom else 0.0


def retrieve_relevant_chunks(question, index, top_k=3):
    """
    Find the most relevant chunks for the question.
    """
    q_emb = embed_text(question)

    scored = [
        (cosine_similarity(q_emb, chunk["embedding"]), chunk)
        for chunk in index
    ]

    # sort from most relevant to least
    scored.sort(key=lambda x: x[0], reverse=True)

    return [chunk for _, chunk in scored[:top_k]]