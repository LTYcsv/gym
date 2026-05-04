from uuid import UUID
from pydantic import BaseModel
from app.exercises.schemas import ExerciseOut


class WorkoutExerciseOut(BaseModel):
    id: UUID
    exercise: ExerciseOut
    sets: int | None
    reps: str | None
    rest_seconds: int | None
    order: int
    notes: str | None

    model_config = {"from_attributes": True}


class WorkoutDayOut(BaseModel):
    id: UUID
    program_id: UUID
    program_type: str        # тип программы — нужен для фильтрации свапа
    program_slug: str
    label: str | None
    title: str | None
    subtitle: str | None
    day_number: int
    workout_exercises: list[WorkoutExerciseOut]

    model_config = {"from_attributes": True}


class WorkoutDaySummary(BaseModel):
    id: UUID
    label: str | None
    title: str | None
    subtitle: str | None
    day_number: int
    exercise_count: int

    model_config = {"from_attributes": True}


class ProgramOut(BaseModel):
    id: UUID
    name: str
    slug: str
    description: str | None
    type: str
    days_per_week: int | None       # максимум дней в программе
    difficulty: str | None
    goal: str | None
    weekly_sessions: int = 0        # выполнено тренировок на этой неделе
    user_days_per_week: int | None = None  # персональная цель юзера (None = не настроено)

    model_config = {"from_attributes": True}


class ProgramDetail(ProgramOut):
    workout_days: list[WorkoutDaySummary]
