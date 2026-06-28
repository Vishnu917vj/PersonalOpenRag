from typing import List

import httpx

from app.core.config import settings
from app.core.logger import logger


class EmbeddingClient:
    """
    Client for communicating with the OpenEmbedd microservice.
    """

    async def embed(self, text: str) -> List[float]:

        payload = {
            "input": text
        }
        logger.info("Sending request to Embedding API...")
        async with httpx.AsyncClient(timeout=120) as client:

            response = await client.post(
                settings.EMBEDDING_API,
                json=payload,
            )

            response.raise_for_status()

            data = response.json()
            logger.info("Received response from Embedding API.")

            return data["data"][0]["embedding"]


embedding_client = EmbeddingClient()