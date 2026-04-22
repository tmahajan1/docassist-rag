def build_prompt(question: str, chunks: list[dict]) -> str:
    """
    Combine question and retrieved chunks into one prompt.
    This helps the model answer using the right context.
    """
    system_prompt = """You are DocBot.
Answer only using the given docs.
If you don't know, say you don't know."""

    context = "\n\n---\n\n".join(
        f"[{i}] {c['title']}\n{c['text']}"
        for i, c in enumerate(chunks, 1)
    )

    return f"{system_prompt}\n\nContext:\n{context}\n\nQuestion:\n{question}"