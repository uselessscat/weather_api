from typing import Generator

from .session import session_maker


def session_dependency() -> Generator:
    try:
        session = session_maker()

        yield session
    finally:
        session.close()
