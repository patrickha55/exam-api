from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Question(BaseModel):
    id: int
    name: str
    answer_one: str
    answer_two: str
    answer_three: str
    answer_four: str
    correct_answer: int


class Exam(BaseModel):
    id: int
    name: str
    questions: list[Question]


class Answer(BaseModel):
    exam_id: int
    answer: int


questions = [
    Question(
        id=1,
        name="What is love?",
        answer_one="Baby don't hurt me",
        answer_two="Don't hurt me",
        answer_three="No more",
        answer_four="I don't know",
        correct_answer=1
    ),
    Question(
        id=2,
        name="What is the capital of France?",
        answer_one="Berlin",
        answer_two="London",
        answer_three="Paris",
        answer_four="Madrid",
        correct_answer=3
    ),
    Question(
        id=3,
        name="What is 2 + 2?",
        answer_one="3",
        answer_two="4",
        answer_three="5",
        answer_four="6",
        correct_answer=2
    )
]

exam = Exam(id=1, name="Sample Exam", questions=questions)


@app.get("/exams")
async def exams():
    return {"exam": exam}


@app.post("/submit")
async def submit(answer: Answer) -> bool:
    question = [q for q in questions if q.id == answer.exam_id][0]

    if not question:
        raise HTTPException(
            status_code=404,
            detail="No question found."
        )

    return question.correct_answer == answer.answer
