from pydantic import BaseModel


class Answer(BaseModel):
    exam_id: int
    answer: int
