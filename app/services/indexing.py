from app.core.embedding_client import embedding_client
from app.core.pinecone import pinecone_client
from app.schemas.index import Document
from app.core.logger import logger


class IndexingService:

    async def index(
        self,
        documents: list[Document],
        namespace: str,
    ):

        vectors = []
        logger.info("Starting document indexing...")
        for document in documents:

            embedding = await embedding_client.embed(
                document.text
            )

            vectors.append(
                {
                    "id": document.id,
                    "values": embedding,
                    "metadata": {
                        "text": document.text,
                    },
                }
            )

        logger.info("Completed document embedding.")
        pinecone_client.index.upsert(
            vectors=vectors,
            namespace=namespace,
        )
        logger.info("Completed document indexing in Pinecone.")
        return len(vectors)


indexing_service = IndexingService()