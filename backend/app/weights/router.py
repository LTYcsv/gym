from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth.deps import get_current_user
from app.models import User, WorkoutExercise
from app.weights import schemas, service

router = APIRouter(prefix="/weights", tags=["weights"])


@router.put("/{workout_exercise_id}", response_model=schemas.WeightOut)
def save_weight(
    workout_exercise_id: str,
    body: schemas.WeightUpsert,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return service.upsert_weight(
        db, str(user.id), workout_exercise_id, body.weight_kg,
        exercise_id=str(body.exercise_id) if body.exercise_id else None,
    )


@router.get("/day/{workout_day_id}")
def get_day_weights(
    workout_day_id: str,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    ids = [str(r.id) for r in db.query(WorkoutExercise.id).filter_by(workout_day_id=workout_day_id).all()]
    return service.get_weights_for_day(db, str(user.id), ids)
