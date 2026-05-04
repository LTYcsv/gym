from uuid import UUID
from pydantic import BaseModel


class ExerciseOut(BaseModel):
    id: UUID
    name: str
    muscle_group: str
    types: list[str]
    equipment: list[str]
    technique: str | None
    difficulty: str

    model_config = {"from_attributes": True}


class ExerciseCreate(BaseModel):
    name: str
    muscle_group: str
    types: list[str]
    equipment: list[str]
    technique: str | None = None
    difficulty: str = "intermediate"
