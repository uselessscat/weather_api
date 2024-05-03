from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from weather.settings import settings

engine: AsyncEngine = create_async_engine(
    settings.database_uri,
    pool_pre_ping=True,
)

session_maker: async_sessionmaker[AsyncSession] = async_sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    bind=engine,
)
