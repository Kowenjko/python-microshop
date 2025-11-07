from pydantic import EmailStr, BaseModel, Field, ConfigDict
from annotated_types import MinLen, MaxLen
from typing import Annotated


class CreateUser(BaseModel):
    email: EmailStr
    first_name: str = Field(..., min_length=3, max_length=20)
    last_name: Annotated[str, MinLen(3), MaxLen(20)]


class UserSchema(BaseModel):
    model_config = ConfigDict(strict=True)

    username: str
    password: bytes
    email: EmailStr | None = None
    active: bool = True
