import logging
from logging.config import dictConfig
import uvicorn

from typing import Any
from fastapi import FastAPI
from app.config import my_logging_config
from app.data_access.exam import create_exam, get_exam, get_exams
from app.dto.exam_input import ExamInput
from app.dto.question_dto import QuestionDto
from app.services.exam_service import handle_question_creation

# Configure basic logging
dictConfig(my_logging_config.log_config)

# Create a logger instance
logger = logging.getLogger(__name__)

app = FastAPI(title="Exam API")


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


@app.post("/questions")
async def questions(input: QuestionDto) -> Any:
    try:
        handle_question_creation(input)
    except Exception:
        logger.error("Error handling question creation", exc_info=True)
        raise


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    logger.info("Starting Exam API server on http://0.0.0.0:8000")
    logger.info("Press CTRL+C to stop the server")
