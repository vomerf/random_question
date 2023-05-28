import uvicorn
from fastapi import FastAPI

from app.api.routers import main_router
from app.core.config import settings

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# load_dotenv(os.path.join(BASE_DIR, '.env'))

app = FastAPI(title=settings.app_title)

app.include_router(main_router)

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True, host='0.0.0.0', port=8000)
