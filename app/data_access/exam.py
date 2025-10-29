from typing import Any
from app.config.main import get_settings
import psycopg

from app.models.exam import Exam

SETTINGS = get_settings()


def get_exams() -> Any:
    to_return = []
    print(SETTINGS)

    with psycopg.connect(SETTINGS.postgres_url) as conn:
        to_return = conn.execute("SELECT * FROM exam.exams").fetchall()

    return to_return


def get_exam(id: int) -> Exam | None:
    query = "SELECT * FROM exam.exams WHERE id = %s"
    try:
        with psycopg.connect(SETTINGS.postgres_url) as conn:
            row = conn.execute(query, [id]).fetchone()

            if row is None:
                return None

            return Exam(id=row[0], name=row[1], created_at=row[2], updated_at=row[3], questions=[])

    except Exception as ex:
        print(ex)
        raise

# def get_exam(id: int) -> Exam | None:
#     query = "SELECT * FROM exam.exams WHERE id = %s"
#     try:
#         with psycopg.connect(SETTINGS.postgres_url) as conn:
#             row = conn.execute(query, [id]).fetchone()
#             if row is None:
#                 return None

#             # Assuming Exam model has id and name fields
#             return Exam(
#                 id=row[0],
#                 name=row[1],
#                 created_at=row[2], updated_at=row[3], questions=[]
#             )

#     except Exception as ex:
#         print(ex)
#         raise


def create_exam(name: str) -> bool:
    if not name:
        return False

    query = "INSERT INTO exam.exams (name) VALUES (%s);"

    try:
        with psycopg.connect(SETTINGS.postgres_url) as conn:
            conn.execute(query, (name,))
            conn.commit()
    except Exception as ex:
        print(ex)
        raise

    return True
