from sqlalchemy.schema import Column
from sqlalchemy.sql import func
from sqlalchemy.types import DateTime, Integer


class IdentifiedMixin:
    id = Column(Integer, primary_key=True, autoincrement=True)


class TimestampMixin:
    created_date = Column(DateTime, default=func.now(), nullable=False)
    updated_date = Column(DateTime, default=func.now(), nullable=False)
