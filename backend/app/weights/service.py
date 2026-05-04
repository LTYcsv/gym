from sqlalchemy.orm import Session
from app.models import UserExerciseWeight, UserWeightLog, WorkoutExercise


def upsert_weight(
    db: Session,
    user_id: str,
    workout_exercise_id: str,
    weight_kg: float,
    exercise_id: str | None = None,
) -> UserExerciseWeight:
    record = (
        db.query(UserExerciseWeight)
        .filter_by(user_id=user_id, workout_exercise_id=workout_exercise_id)
        .first()
    )
    if record:
        record.weight_kg = weight_kg
    else:
        record = UserExerciseWeight(
            user_id=user_id,
            workout_exercise_id=workout_exercise_id,
            weight_kg=weight_kg,
        )
        db.add(record)

    # exercise_id может быть переопределён, если юзер сделал swap упражнения
    log_exercise_id = exercise_id
    if not log_exercise_id:
        we = db.query(WorkoutExercise).filter_by(id=workout_exercise_id).first()
        if we:
            log_exercise_id = str(we.exercise_id)

    if log_exercise_id:
        db.add(UserWeightLog(
            user_id=user_id,
            exercise_id=log_exercise_id,
            weight_kg=weight_kg,
        ))

    db.commit()
    db.refresh(record)
    return record


def get_weights_for_day(db: Session, user_id: str, workout_exercise_ids: list[str]) -> dict[str, float]:
    rows = (
        db.query(UserExerciseWeight)
        .filter(
            UserExerciseWeight.user_id == user_id,
            UserExerciseWeight.workout_exercise_id.in_(workout_exercise_ids),
        )
        .all()
    )
    return {str(r.workout_exercise_id): r.weight_kg for r in rows}
