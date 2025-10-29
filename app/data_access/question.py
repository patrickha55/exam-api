import psycopg
from app.config.main import get_settings
from app.models.question import Question

SETTINGS = get_settings()


def create_questions(question: Question) -> None:
    query = """INSERT INTO question.questions 
                (exam_id, name, answer_one, answer_two, answer_three, answer_three, answer_four, correct_answer, is_multi_choices)
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
    except Exception as ex:
        print('An exception occurred')
        print(ex)
