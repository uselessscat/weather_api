from sqlalchemy.orm import as_declarative

from .mixins import (
    IdentifiedMixin,
    TimestampMixin,
)


@as_declarative()
class BaseModel(IdentifiedMixin, TimestampMixin):
    __abstract__ = True
