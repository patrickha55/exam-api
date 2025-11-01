import logging
import psycopg
from app.config.main import get_settings
from app.dto.question_dto import QuestionDto
from app.models.question import Question

SETTINGS = get_settings()

logger = logging.getLogger(__name__)


def get_questions_by_exam_id(exam_id: int) -> list[Question]:
    query = "SELECT * FROM exam.questions WHERE exam_id = %s"
    to_return: list[Question] = []
    try:
        with psycopg.connect(SETTINGS.postgres_url) as conn:
            rows = conn.execute(query, [exam_id]).fetchall()

            for row in rows:
                q = Question(
                    id=row[0],
                    exam_id=row[1],
                    name=row[2],
                    answer_one=row[3],
                    answer_two=row[4],
                    answer_three=row[5],
                    answer_four=row[6],
                    correct_answer=row[7],
                    is_multi_choices=row[8],
                    created_at=row[9],
                    updated_at=row[10] if row[10] else None
                )

                to_return.append(q)

            return to_return
    except Exception:
        logger.error("Error fetching questions for exam_id %s",
                     exam_id, exc_info=True)
        raise


def create_question(question: QuestionDto) -> None:
    query = """INSERT INTO exam.questions 
                (exam_id, name, answer_one, answer_two, answer_three, answer_four, correct_answer, is_multi_choices)
                values (%s,%s,%s,%s,%s,%s,%s,%s)"""

    try:
        with psycopg.connect(SETTINGS.postgres_url) as conn:
            conn.execute(query, (
                question.exam_id,
                question.name,
                question.answer_one,
                question.answer_two,
                question.answer_three,
                question.answer_four,
                question.correct_answer,
                question.is_multi_choices
            ))
            conn.commit()
    except Exception:
        logger.error("Error creating question", exc_info=True)
