from fastapi import APIRouter

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.rag import rag_service
from app.core.logger import logger
from app.schemas.response import RAGResponse

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@router.post("/", response_model=RAGResponse)
async def chat(request: ChatRequest):
    logger.info("Starting chat response generation...")
    result = await rag_service.ask(
        question=request.message
    )
    logger.info("Completed chat response generation.")

    return result