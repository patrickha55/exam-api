
from datetime import datetime
from pydantic import BaseModel


class Question(BaseModel):
    id: int
    exam_id: int
    name: str
    answer_one: str
    answer_two: str
    answer_three: str
    answer_four: str
    correct_answer: str
    is_multi_choices: bool
    created_at: datetime
    updated_at: datetime | None
