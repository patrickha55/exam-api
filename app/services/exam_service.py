import logging
from fastapi import HTTPException
from app.data_access.exam import get_exam
from app.data_access.question import create_question
from app.dto.question_dto import QuestionDto


logger = logging.getLogger(__name__)


def handle_question_creation(questionDTO: QuestionDto) -> None:
    try:
        if not questionDTO:
            raise HTTPException(
                status_code=400,
                detail="Invalid payload."
            )

        exam = get_exam(questionDTO.exam_id)

        if exam is None:
            raise HTTPException(
                status_code=404,
                detail="No exam found."
            )

        create_question(questionDTO)
    except Exception:
        logger.error("Error handling question creation", exc_info=True)
        raise
