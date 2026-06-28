from app.core.embedding_client import embedding_client
from app.core.pinecone import pinecone_client
from app.core.logger import logger


class RetrievalService:

    async def retrieve(
        self,
        query: str,
        namespace: str = "default",
        top_k: int = 5,
    ):

        embedding = await embedding_client.embed(query)
        logger.info("Generating embedding for user query...")

        results = pinecone_client.index.query(
            vector=embedding,
            top_k=top_k,
            namespace=namespace,
            include_metadata=True,
        )
        logger.info("Comleted retrieval of relevant chunks from Pinecone index.")
        return results.matches


retrieval_service = RetrievalService()