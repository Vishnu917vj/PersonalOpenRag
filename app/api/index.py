from fastapi import APIRouter

from app.schemas.index import IndexRequest, IndexResponse
from app.services.indexing import indexing_service
from app.core.logger import logger

router = APIRouter(
    prefix="/index",
    tags=["Index"],
)


@router.post("/", response_model=IndexResponse)
async def index_documents(request: IndexRequest):

    logger.info("Starting document indexing...")

    indexed = await indexing_service.index(
        documents=request.documents,
        namespace=request.namespace,
    )

    logger.info("Completed document indexing.")

    return IndexResponse(
        indexed=indexed,
        namespace=request.namespace,
    )