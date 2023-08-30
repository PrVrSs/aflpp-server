from contextlib import asynccontextmanager

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from .logger import logger
from .settings import settings


async_engine = create_async_engine(
    settings.DB_URI,
    pool_pre_ping=True,
    echo=settings.ECHO_SQL,
)

AsyncSessionLocal = async_sessionmaker(
    bind=async_engine,
    autoflush=False,
    future=True,
    expire_on_commit=False,
)


@asynccontextmanager
async def get_session() -> async_sessionmaker:
    try:
        async with AsyncSessionLocal() as session:
            yield session
    except SQLAlchemyError as exc:
        logger.exception(exc)
