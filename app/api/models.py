from pydantic import BaseModel, Field
from typing import List, Optional

class TextInput(BaseModel):
    text: str = Field(..., max_length=2000)
    context_texts: Optional[List[str]] = Field(
        None,
        max_items=5,
        example=["Additional context 1", "Additional context 2"]
    )

class BatchTextInput(BaseModel):
    texts: List[TextInput] = Field(..., max_items=20)

class AnalysisResponse(BaseModel):
    sentiment: str = Field(..., example="POSITIVE")
    score: float = Field(..., ge=0, le=1, example=0.95)
    rag_response: str = Field(..., example="Text with relevant context")