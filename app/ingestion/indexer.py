from .chunker import chunk_doc
from .embedder import embed_text

def build_index(docs: list[dict]) -> list[dict]:
    """
    Create a list of chunks with embeddings.
    This acts like a simple vector database.
    """
    index = []

    for doc in docs:
        chunks = chunk_doc(doc)

        for chunk in chunks:
            # create embedding for each chunk
            chunk["embedding"] = embed_text(chunk["text"])
            index.append(chunk)

    return index