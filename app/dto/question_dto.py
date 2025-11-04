
from pydantic import BaseModel


class QuestionDto(BaseModel):
    exam_id: int
    name: str
    answer_one: str
    answer_two: str
    answer_three: str
    answer_four: str
    correct_answer: str
    is_multi_choices: bool = False
