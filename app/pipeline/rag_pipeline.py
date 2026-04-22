from retrieval.retriever import retrieve_relevant_chunks
from llm.prompt_builder import build_prompt
from llm.client import generate_answer

def answer_question(question, index):
    """
    Full flow:
    find docs → build prompt → get answer
    """
    chunks = retrieve_relevant_chunks(question, index)

    if not chunks:
        return "No relevant docs found."

    prompt = build_prompt(question, chunks)

    return generate_answer(prompt)