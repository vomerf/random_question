from datetime import datetime
from typing import Union

from pydantic import BaseModel, validator


class CountQuestions(BaseModel):
    question_num: int

    @validator('question_num')
    def count_question(cls, v):
        if v <= 0:
            raise ValueError('Число должно быть положительным')
        return v


class LastQuestion(BaseModel):
    id: int
    answer: Union[str, None]
    question: Union[str, None]
    airdate: Union[datetime, None]

    class Config:
        orm_mode = True
