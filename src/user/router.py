from fastapi import APIRouter, HTTPException, status, Depends

from src.user.services import get_user_service
from src.user.user_model import UserModel, UserUpdateDto

router = APIRouter(
    prefix="/user",
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_all_users(us=Depends(get_user_service)) -> list[UserModel]:
    """
    Get all users
    """
    return us.fetch()


@router.get("/{username}", response_model=UserModel)
async def get_user(username: str, us=Depends(get_user_service)) -> UserModel | dict[str, str]:
    """
    Get a user by username
    """
    user: UserModel | None = us.get_by_field("username", username)

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return user


@router.post("/", response_model=UserModel)
async def create_user(user: UserModel, us=Depends(get_user_service)) -> UserModel:
    """
    Create a new user
    """
    us.insert(user)
    return user


@router.put("/{username}")
async def update_user(username: str, user: UserUpdateDto, us=Depends(get_user_service)):
    """
    Update a user by username
    """
    for u in us.fetch():
        if u.username == username:
            us.update(u, user)
            return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.delete("/{username}", response_model=UserModel)
async def delete_user(username: str, us=Depends(get_user_service)):
    """
    Delete a user by username
    """
    for u in us.fetch():
        if u.username == username:
            us.remove(u)
            return u
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
