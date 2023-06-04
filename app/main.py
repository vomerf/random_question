import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routers import main_router
from app.core.config import settings


app = FastAPI(title=settings.app_title)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(main_router)

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True, host='0.0.0.0', port=8000)
