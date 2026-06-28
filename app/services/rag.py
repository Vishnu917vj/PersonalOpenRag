from app.core.prompts import SYSTEM_PROMPT, build_prompt
from app.services.llm import llm_service
from app.services.retrieval import retrieval_service
from app.schemas.response import Source, RAGResponse


class RAGService:

    async def ask(
        self,
        question: str,
        namespace: str = "qa-dataset",
        top_k: int = 5,
    ):

        # Retrieve relevant chunks
        matches = await retrieval_service.retrieve(
            query=question,
            namespace=namespace,
            top_k=top_k,
        )

        # Extract context
        contexts = []

        for match in matches:

            metadata = match.get("metadata", {})

            text = metadata.get("text")

            if text:
                contexts.append(text)

        # Build prompt
        prompt = build_prompt(
            question=question,
            contexts=contexts,
        )

        # Generate answer
        answer = await llm_service.generate(
            system_prompt=SYSTEM_PROMPT,
            user_prompt=prompt,
        )

        sources = []

        for match in matches:

            metadata = match.get("metadata", {})

            sources.append(
                Source(
                    id=match["id"],
                    score=match["score"],
                    text=metadata.get("text", ""),
                )
            )

        return RAGResponse(
            answer=answer,
            sources=sources,
        )


rag_service = RAGService()