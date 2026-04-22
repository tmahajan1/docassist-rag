def chunk_doc(doc: dict, max_chars: int = 800) -> list[dict]:
    """
    Split a document into smaller parts.
    Smaller chunks help in better search results.
    """
    text = doc["content"].strip()
    paragraphs = text.split("\n\n")

    chunks = []
    current = ""

    for p in paragraphs:
        # keep adding text until we reach size limit
        if len(current) + len(p) <= max_chars:
            current = f"{current}\n\n{p}" if current else p
        else:
            if current:
                chunks.append(current)
            current = p

    if current:
        chunks.append(current)

    return [
        {
            "id": f"{doc['id']}_chunk_{i}",
            "title": doc["title"],
            "path": doc["path"],
            "text": chunk_text,
        }
        for i, chunk_text in enumerate(chunks)
    ]