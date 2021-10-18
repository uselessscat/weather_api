from typing import Dict

from fastapi import APIRouter

router = APIRouter(
    tags=['Status']
)


@router.get('/ping')
def ping() -> Dict[str, str]:
    '''
    Sanity check. This will let the user know that the service is operational.
    '''
    return {'ping': 'pong'}


__all__ = [
    router
]
