from pydantic import BaseModel, Field


class Document(BaseModel):
    id: str = Field(..., description="Unique document ID")
    text: str = Field(..., description="Text to index")


class IndexRequest(BaseModel):
    namespace: str = "default"
    documents: list[Document]


class IndexResponse(BaseModel):
    indexed: int
    namespace: str