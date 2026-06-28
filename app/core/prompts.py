SYSTEM_PROMPT = """
You are a helpful AI assistant.

Answer ONLY using the supplied context.

If the answer cannot be found in the context,
say that you don't know.

Do not hallucinate.

Be concise and accurate.
"""


def build_prompt(question: str, contexts: list[str]) -> str:

    context = "\n\n".join(contexts)

    return f"""
Context:
{context}

Question:
{question}
"""