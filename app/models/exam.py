from datetime import datetime
from pydantic import BaseModel

from app.models.question import Question


class Exam(BaseModel):
    id: int
    name: str
    created_at: datetime
    updated_at: datetime | None
    questions: list[Question]
