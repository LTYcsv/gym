from uuid import UUID
from datetime import datetime
from pydantic import BaseModel


class SessionCreate(BaseModel):
    workout_day_id: UUID
    program_id: UUID


class SessionOut(BaseModel):
    id: UUID
    workout_day_id: UUID
    program_id: UUID
    completed_at: datetime

    model_config = {"from_attributes": True}
