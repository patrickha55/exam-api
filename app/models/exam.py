from datetime import date
from pydantic import BaseModel

from app.models.question import Question


class Exam(BaseModel):
    id: int
    name: str
    created_at: date
    updated_at: date
    questions: list[Question]
