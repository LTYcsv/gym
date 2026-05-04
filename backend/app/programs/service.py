from sqlalchemy.orm import Session, joinedload
from app.models import Program, WorkoutDay, WorkoutExercise


def list_programs(db: Session) -> list[Program]:
    return db.query(Program).filter(Program.is_active == True).order_by(Program.name).all()


def get_program(db: Session, slug: str) -> Program | None:
    return (
        db.query(Program)
        .options(joinedload(Program.workout_days).joinedload(WorkoutDay.workout_exercises))
        .filter(Program.slug == slug)
        .first()
    )


def get_workout_day(db: Session, day_id: str) -> WorkoutDay | None:
    return (
        db.query(WorkoutDay)
        .options(
            joinedload(WorkoutDay.program),
            joinedload(WorkoutDay.workout_exercises).joinedload(WorkoutExercise.exercise),
        )
        .filter(WorkoutDay.id == day_id)
        .first()
    )
