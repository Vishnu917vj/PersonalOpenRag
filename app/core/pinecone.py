from pinecone import Pinecone

from app.core.config import settings
from app.core.logger import logger

class PineconeClient:
    """
    Client for interacting with an existing Pinecone index.
    """

    def __init__(self):
        self.pc = Pinecone(
            api_key=settings.PINECONE_API_KEY
        )
        logger.info("Initialized Pinecone client.")
        self.index = self.pc.Index(
            settings.PINECONE_INDEX
        )


pinecone_client = PineconeClient()