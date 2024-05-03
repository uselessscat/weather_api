from datetime import datetime

from fastapi import APIRouter

router = APIRouter(tags=['Status'])


@router.get('/status')
def status() -> dict[str, str]:
    """Sanity check.

    This will let the user know that the service is operational.
    """
    return {'status': 'running', 'timestamp': datetime.now().isoformat()}


__all__ = ['router']
