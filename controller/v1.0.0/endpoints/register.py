from fastapi import APIRouter, status

from models import container, database, app, policy

router = APIRouter(prefix="/api/register")

@router.post("/container", status_code=status.)

@router.get("")
def test():
    return {"hello": "hello"}
