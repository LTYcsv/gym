from uuid import UUID
from pydantic import BaseModel, Field


class WeightUpsert(BaseModel):
    weight_kg: float = Field(gt=0, le=1000)
    exercise_id: UUID | None = None


class WeightOut(BaseModel):
    workout_exercise_id: UUID
    weight_kg: float

    model_config = {"from_attributes": True}
