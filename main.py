from fastapi import FastAPI
from contextlib import asynccontextmanager

from items_views import router as items_router
from users.views import router as users_router
from api_v1 import router as router_v1

from core.models import db_helper, Base
from core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Не потребовалось создавать таблицы при старте приложения,
    # так как используется Alembic для управления миграциями.
    # async with db_helper.engine.begin() as conn:
    #     await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router_v1, prefix=settings.api_v1_prefix)
app.include_router(items_router)
app.include_router(users_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
