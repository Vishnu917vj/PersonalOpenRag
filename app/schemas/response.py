from pydantic import BaseModel, Field


class Source(BaseModel):
    id: str = Field(..., description="Vector ID")
    score: float = Field(..., description="Similarity score")
    text: str = Field(..., description="Retrieved chunk")


class RAGResponse(BaseModel):
    answer: str
    sources: list[Source]