from pathlib import Path

def load_docs_from_folder(folder: Path) -> list[dict]:
    """Load all markdown files from a folder."""
    docs = []

    for path in folder.glob("*.md"):
        text = path.read_text(encoding="utf-8")

        docs.append({
            "id": path.stem,
            "title": path.stem.replace("_", " ").title(),
            "content": text,
            "path": str(path),
        })

    return docs