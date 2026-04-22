def chunk_doc(doc: dict, max_chars: int = 800, overlap: int = 150) -> list[dict]:
    """
    Split document into chunks with overlap.
    Overlap helps keep context between chunks.
    """
    text = doc["content"].strip()
    
    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + max_chars
        chunk_text = text[start:end]

        chunks.append(chunk_text)

        # move forward but keep some overlap
        start = end - overlap

    return [
        {
            "id": f"{doc['id']}_chunk_{i}",
            "title": doc["title"],
            "path": doc["path"],
            "text": chunk_text,
        }
        for i, chunk_text in enumerate(chunks)
    ]