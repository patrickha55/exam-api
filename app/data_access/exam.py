from datetime import datetime
import logging
from typing import Any
from app.config.main import get_settings
import psycopg

from app.data_access.question import get_questions_by_exam_id
from app.models.exam import Exam

SETTINGS = get_settings()
logger = logging.getLogger(__name__)


def get_exams() -> list[Exam]:
    try:
        to_return: list[Exam] = []
        query: str = "SELECT * FROM exam.exams"

        with psycopg.connect(SETTINGS.postgres_url) as conn:
            rows = conn.execute(query).fetchall()

            for row in rows:
                created: datetime = row[2]

                updated: datetime | None = row[3] if row[3] else None

                exam = Exam(id=row[0], name=row[1], created_at=created,
                            updated_at=updated, questions=[])

                to_return.append(exam)

        return to_return
    except Exception:
        logger.error("Error fetching exams", exc_info=True)
        raise


def get_exam(id: int) -> Exam | None:
    query = "SELECT * FROM exam.exams WHERE id = %s"
    try:
        with psycopg.connect(SETTINGS.postgres_url) as conn:
            row = conn.execute(query, [id]).fetchone()

            if row is None:
                return None

            created: datetime = row[2]
            updated: datetime | None = row[3] if row[3] else None

            return Exam(id=row[0], name=row[1], created_at=created,
                        updated_at=updated, questions=get_questions_by_exam_id(row[0]))

    except Exception:
        logger.error("Error fetching exam with id %s", id, exc_info=True)
        raise


def create_exam(name: str) -> bool:
    if not name:
        return False

    query = "INSERT INTO exam.exams (name) VALUES (%s);"

    try:
        with psycopg.connect(SETTINGS.postgres_url) as conn:
            conn.execute(query, (name,))
            conn.commit()
    except Exception:
        logger.error("Error creating exam with name %s", name, exc_info=True)
        raise

    return True
