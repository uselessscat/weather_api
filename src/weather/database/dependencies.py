from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from .session import session_maker


async def session_dependency() -> AsyncGenerator[AsyncSession, None]:
    async with session_maker() as session:
        yield session
