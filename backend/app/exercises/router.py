from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.exercises import schemas, service
from app.models import Exercise, WorkoutExercise, WorkoutDay, Program

router = APIRouter(prefix="/exercises", tags=["exercises"])


@router.get("/", response_model=list[schemas.ExerciseOut])
def list_exercises(
    muscle_group: str | None = Query(None),
    type: str | None = Query(None),
    equipment: str | None = Query(None),
    db: Session = Depends(get_db),
):
    return service.list_exercises(db, muscle_group=muscle_group, type_=type, equipment=equipment)


@router.get("/alternatives", response_model=list[schemas.ExerciseOut])
def get_alternatives(
    exercise_id: str = Query(...),
    program_type: str = Query(...),
    db: Session = Depends(get_db),
):
    return service.get_alternatives(db, exercise_id=exercise_id, program_type=program_type)


@router.get("/{exercise_id}/programs")
def get_exercise_programs(exercise_id: str, db: Session = Depends(get_db)):
    rows = (
        db.query(Program.name, Program.slug, WorkoutDay.label, WorkoutDay.title)
        .join(WorkoutDay, Program.id == WorkoutDay.program_id)
        .join(WorkoutExercise, WorkoutDay.id == WorkoutExercise.workout_day_id)
        .filter(WorkoutExercise.exercise_id == exercise_id)
        .all()
    )
    return [
        {"program_name": r.name, "program_slug": r.slug, "day_label": r.label, "day_title": r.title}
        for r in rows
    ]


@router.get("/{exercise_id}", response_model=schemas.ExerciseOut)
def get_exercise(exercise_id: str, db: Session = Depends(get_db)):
    ex = db.query(Exercise).filter_by(id=exercise_id).first()
    if not ex:
        raise HTTPException(404, "Exercise not found")
    return ex
