from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from src.auth.schemas import Token
from src.auth.utils import create_access_token, get_current_user
from src.config import settings
from src.user.services import get_user_service
from src.user.user_model import UserModel

router = APIRouter(
    prefix="/login",
    responses={401: {"description": "Unauthorized"}},
)


@router.post("/", response_model=Token)
async def login_for_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        us=Depends(get_user_service)
):
    user = us.get_by_field('username', form_data.username)

    if not user or user.password != form_data.password:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token_expires = timedelta(seconds=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "Bearer"}


@router.get("/", response_model=UserModel)
async def read_users_me(
        current_user: Annotated[UserModel, Depends(get_current_user)]
):
    return current_user
