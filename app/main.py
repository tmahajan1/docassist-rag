from pathlib import Path
from ingestion.loader import load_docs_from_folder
from ingestion.indexer import build_index
from pipeline.rag_pipeline import answer_question

DOCS_DIR = Path("docs")

if __name__ == "__main__":
    # load docs and create index once
    docs = load_docs_from_folder(DOCS_DIR)
    index = build_index(docs)

    print("DocBot ready. Type 'exit' to quit.")

    while True:
        q = input("\nYou: ")

        if q.lower() in {"exit", "quit"}:
            break

        print("\nDocBot:", answer_question(q, index))