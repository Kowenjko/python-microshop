from pydantic import EmailStr, BaseModel, Field
from annotated_types import MinLen, MaxLen
from typing import Annotated


class CreateUser(BaseModel):
    email: EmailStr
    first_name: str = Field(..., min_length=3, max_length=20)
    last_name: Annotated[str, MinLen(3), MaxLen(20)]
