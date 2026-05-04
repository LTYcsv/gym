from uuid import UUID
from pydantic import BaseModel


class WeightUpsert(BaseModel):
    weight_kg: float


class WeightOut(BaseModel):
    workout_exercise_id: UUID
    weight_kg: float

    model_config = {"from_attributes": True}
