from ingestion.loader import load_docs_from_folder
from ingestion.indexer import build_index
from retrieval.retriever import retrieve_relevant_chunks
from pathlib import Path

DOCS_DIR = Path("docs")

# Queries mapped to expected concepts (not titles)
TEST_CASES = [
    {
        "query": "How to create an NFS export?",
        "expected_keywords": ["nfs", "export", "create"]
    },
    {
        "query": "How do I mount an NFS export?",
        "expected_keywords": ["mount", "nfs"]
    },
    {
        "query": "What is SMB used for?",
        "expected_keywords": ["smb", "windows", "active directory"]
    },
    {
        "query": "Why am I getting access denied on SMB share?",
        "expected_keywords": ["access denied", "permissions", "ad"]
    },
    {
        "query": "What protocols does file storage support?",
        "expected_keywords": ["smb", "nfs", "protocol"]
    }
]


def is_relevant(chunk_text: str, keywords: list[str]) -> bool:
    """Check if chunk contains expected keywords."""
    text = chunk_text.lower()
    return any(keyword in text for keyword in keywords)


def evaluate():
    docs = load_docs_from_folder(DOCS_DIR)
    index = build_index(docs)

    total_queries = len(TEST_CASES)
    total_relevant_retrieved = 0
    total_retrieved = 0
    queries_with_hit = 0  # for recall

    for test in TEST_CASES:
        query = test["query"]
        keywords = test["expected_keywords"]

        retrieved = retrieve_relevant_chunks(query, index, top_k=3)

        relevant_found = 0

        print(f"\nQuery: {query}")

        for chunk in retrieved:
            total_retrieved += 1

            if is_relevant(chunk["text"], keywords):
                relevant_found += 1
                total_relevant_retrieved += 1

        if relevant_found > 0:
            queries_with_hit += 1

        print(f"Relevant chunks found: {relevant_found} / {len(retrieved)}")

    precision = total_relevant_retrieved / total_retrieved if total_retrieved else 0
    recall = queries_with_hit / total_queries if total_queries else 0

    print("\n--- Evaluation ---")
    print(f"Precision@3: {precision:.2f}")
    print(f"Recall@3: {recall:.2f}")


if __name__ == "__main__":
    evaluate()