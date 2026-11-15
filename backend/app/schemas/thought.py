from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, ConfigDict, Field

class ThoughtCreate(BaseModel):
    title: str | None = Field(default=None, max_length=200)
    content: str = Field(min_length=1)
    category: str | None = Field(default=None, max_length=50)

class ThoughtRead(ThoughtCreate):
    id: UUID
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True)
