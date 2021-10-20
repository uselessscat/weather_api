from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from weather.settings import settings

engine = create_engine(
    settings.database_uri,
    pool_pre_ping=True
)

session_maker = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
