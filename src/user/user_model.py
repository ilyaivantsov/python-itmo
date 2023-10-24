from typing import Optional, Annotated

from pydantic import BaseModel, AfterValidator

from src.user.validators import validate_password, validate_email_by_regex

Password = Annotated[str, AfterValidator(validate_password)]
Email = Annotated[str, AfterValidator(validate_email_by_regex)]


class UserModel(BaseModel):
    username: str
    email: Optional[Email] = None
    first_name: str
    last_name: str
    password: Password


class UserUpdateDto(UserModel):
    username: Optional[str]
    email: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    password: Optional[str]
