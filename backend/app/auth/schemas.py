from pydantic import BaseModel
from uuid import UUID


class AuthRequest(BaseModel):
    init_data: str


class UserOut(BaseModel):
    id: UUID
    telegram_id: int
    username: str | None
    first_name: str | None

    model_config = {"from_attributes": True}


class AuthResponse(BaseModel):
    token: str
    user: UserOut
