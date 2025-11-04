# POSTGRES

# TABLES
CREATE TABLE exam.exams (
    id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name text NOT NULL,
    created_at timestamp NOT NULL DEFAULT now(),
    updated_at timestamp
);

CREATE TABLE exam.questions (
    id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    exam_id bigint NOT NULL REFERENCES exam.exams ON DELETE CASCADE,
    name text NOT NULL,
    answer_one text NOT NULL,
    answer_two text NOT NULL,
    answer_three text NOT NULL,
    answer_four text NOT NULL,
    correct_answer text NOT NULL,
    is_multi_choices boolean NOT NULL DEFAULT false,
    created_at timestamp NOT NULL DEFAULT now(),
    updated_at timestamp
);