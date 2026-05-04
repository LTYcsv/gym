from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, field_validator


class UserProgramCreate(BaseModel):
    program_id: UUID
    days_per_week: int

    @field_validator("days_per_week")
    @classmethod
    def validate_days(cls, v: int) -> int:
        if not 1 <= v <= 7:
            raise ValueError("days_per_week must be between 1 and 7")
        return v


class UserProgramOut(BaseModel):
    id: UUID
    program_id: UUID
    days_per_week: int
    started_at: datetime

    model_config = {"from_attributes": True}
