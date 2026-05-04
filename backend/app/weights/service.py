from sqlalchemy.orm import Session
from app.models import UserExerciseWeight, UserWeightLog, WorkoutExercise


def upsert_weight(db: Session, user_id: str, workout_exercise_id: str, weight_kg: float) -> UserExerciseWeight:
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

    we = db.query(WorkoutExercise).filter_by(id=workout_exercise_id).first()
    if we:
        db.add(UserWeightLog(
            user_id=user_id,
            exercise_id=str(we.exercise_id),
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
