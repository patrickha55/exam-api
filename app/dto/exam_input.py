from pydantic import BaseModel


class ExamInput(BaseModel):
    name: str
