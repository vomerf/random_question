from datetime import datetime
from typing import Union

from pydantic import BaseModel


class CountQuestions(BaseModel):
    question_num: int


class LastQuestion(BaseModel):
    id: int
    answer: Union[str, None]
    question: Union[str, None]
    airdate: Union[datetime, None]

    class Config:
        orm_mode = True