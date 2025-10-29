from typing import Any
from fastapi import FastAPI

from app.data_access.exam import create_exam, get_exam, get_exams
from app.dto.exam_input import ExamInput

app = FastAPI()


@app.get("/exams")
async def exams():
    exams = get_exams()
    return {"exam": exams}


@app.get("/exams/{id}")
async def exam(id: int) -> Any:
    exam = get_exam(id)
    return {"result": exam}


@app.post("/exams")
async def exam_post(input: ExamInput) -> dict[str, bool]:
    result = create_exam(input.name)
    return {"result": result}


# @app.post("/submit")
# async def submit(answer: Answer) -> bool:
#     question = [q for q in questions if q.id == answer.exam_id][0]

#     if not question:
#         raise HTTPException(
#             status_code=404,
#             detail="No question found."
#         )

#     return question.correct_answer == answer.answer
