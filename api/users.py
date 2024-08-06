from fastapi import APIRouter, HTTPException
from models.user import User, users
import logging

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/users/", response_model=User)
async def create_user(user: User):
    logger.info(f"Creating user: {user.name}")
    if any(u.id == user.id for u in users):
        logger.warning(f"User with id {user.id} already exists")
        raise HTTPException(status_code=400, detail="User already exists")
    users.append(user)
    return user
