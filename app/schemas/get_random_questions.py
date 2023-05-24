from pydantic import BaseModel


class CountQuestions(BaseModel):
    question_num: int