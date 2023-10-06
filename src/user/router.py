from fastapi import APIRouter, HTTPException, status

from src.database import Db
from src.user.user_model import UserModel, UserUpdateDto

router = APIRouter(
    prefix="/user",
    responses={404: {"description": "Not found"}},
)

us = Db[UserModel]()


@router.get("/")
async def get_all_users() -> list[UserModel]:
    """
    Get all users
    """
    return us.fetch()


@router.get("/{username}", response_model=UserModel)
async def get_user(username: str) -> UserModel | dict[str, str]:
    """
    Get a user by username
    """
    for u in us.fetch():
        if u.username == username:
            return u
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.post("/", response_model=UserModel)
async def create_user(user: UserModel) -> UserModel:
    """
    Create a new user
    """
    us.insert(user)
    return user


@router.put("/{username}")
async def update_user(username: str, user: UserUpdateDto):
    """
    Update a user by username
    """
    for u in us.fetch():
        if u.username == username:
            us.update(u, user)
            return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.delete("/{username}", response_model=UserModel)
async def delete_user(username: str):
    """
    Delete a user by username
    """
    for u in us.fetch():
        if u.username == username:
            us.remove(u)
            return u
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
