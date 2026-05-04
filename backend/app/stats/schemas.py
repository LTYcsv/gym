from pydantic import BaseModel
from datetime import datetime


class MuscleGroupCount(BaseModel):
    muscle_group: str
    count: int


class RecordItem(BaseModel):
    exercise_name: str
    weight_kg: float
    achieved_at: datetime


class StatsOut(BaseModel):
    weekly_done: int
    weekly_planned: int
    weekly_muscle_groups: list[MuscleGroupCount]
    workout_dates: list[str]       # "YYYY-MM-DD" за последние 30 дней
    week_streak: int               # недель подряд с >=1 тренировкой
    workout_streak: int            # тренировок подряд без пропуска недели
    records: list[RecordItem]      # лучший вес по каждому упражнению
