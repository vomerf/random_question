from fastapi import APIRouter

from app.api import random_question_router

main_router = APIRouter()

main_router.include_router(
    random_question_router, tags=["Random question"], prefix='/random_question'
)
