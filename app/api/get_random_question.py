import json
from typing import Union

import requests
from fastapi import APIRouter, Depends
from requests.exceptions import RequestException
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.db import get_session
from app.models.models import RandomQuestion
from app.schemas.get_random_questions import CountQuestions, LastQuestion

router = APIRouter()


@router.post("/", response_model=Union[LastQuestion, None])
def get_random_question(
    count: CountQuestions,
    session: Session = Depends(get_session)
):
    url = settings.url
    query = session.query(
        RandomQuestion).order_by(RandomQuestion.created_at.desc()).first()
    try:
        response = requests.get(url, params={'count': count.question_num})
    except RequestException:
        raise RequestException('Ошибка при выполнении запроса')
    all_random_question = json.loads(response.text)
    add_all_random_questions = []
    all_random_question_copy = all_random_question.copy()
    while len(add_all_random_questions) != len(all_random_question):
        response = all_random_question_copy.pop()
        stmt = session.query(
            RandomQuestion).filter(
                RandomQuestion.id == response.get('id')).count()
        if stmt:
            response = requests.get(url, params={'count': 1})
            response = json.loads(response.text)[0]
            stmt = session.query(
                RandomQuestion).filter(
                    RandomQuestion.id == response.get('id')).count()
        else:
            add_all_random_questions.append(RandomQuestion(
                id_question=response.get('id'),
                answer=response.get('answer'),
                question=response.get('question'),
                airdate=response.get('airdate')
            ))
    try:
        session.add_all(add_all_random_questions)
        session.commit()
    except Exception:
        session.rollback()
    return query
