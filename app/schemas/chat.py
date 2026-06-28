from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    message: str

class Source(BaseModel):
    id: str = Field(..., description="Vector ID")
    score: float = Field(..., description="Similarity score")
    text: str = Field(..., description="Retrieved chunk")
class ChatResponse(BaseModel):
    response: str
    sources: list[Source]  