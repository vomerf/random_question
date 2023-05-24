from schemas.get_random_questions import CountQuestions
import requests
import requests_cache
from app.main import app


@app.post("/")
def get_random_question(count: CountQuestions):
    session = requests_cache.CachedSession('demo_cache')
    url = 'https://jservice.io/api/random'
    response = session.get(url, params={'count': count.question_num})
    print(type(response.text))
    return response.text