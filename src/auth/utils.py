from datetime import datetime, timedelta

from fastapi.security import HTTPAuthorizationCredentials
from jose import jwt, JWTError

from src.auth.schemas import oauth2_scheme, TokenData
from src.config import settings
from typing import Annotated
from fastapi import Depends, HTTPException, status

from src.user.services import get_user_service


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(seconds=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


async def get_current_user(credentials: Annotated[HTTPAuthorizationCredentials, Depends(oauth2_scheme)],
                           us=Depends(get_user_service)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(credentials.credentials, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = us.get_by_field("username", token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def has_access(credentials: Annotated[HTTPAuthorizationCredentials, Depends(oauth2_scheme)],
                     us=Depends(get_user_service)):
    try:
        payload = jwt.decode(credentials.credentials, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            return False
    except JWTError:
        return False
    user = us.get_by_field("username", username)
    if user is None:
        return False
    return True


PROTECTED = [Depends(has_access)]
