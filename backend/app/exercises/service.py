from sqlalchemy.orm import Session
from app.models import Exercise


def list_exercises(
    db: Session,
    muscle_group: str | None = None,
    type_: str | None = None,
    equipment: str | None = None,
) -> list[Exercise]:
    q = db.query(Exercise)
    if muscle_group:
        q = q.filter(Exercise.muscle_group == muscle_group)
    if type_:
        q = q.filter(Exercise.types.any(type_))
    if equipment:
        q = q.filter(Exercise.equipment.any(equipment))
    return q.order_by(Exercise.name).all()


def get_alternatives(db: Session, exercise_id: str, program_type: str) -> list[Exercise]:
    source = db.query(Exercise).filter(Exercise.id == exercise_id).first()
    if not source:
        return []
    return (
        db.query(Exercise)
        .filter(
            Exercise.muscle_group == source.muscle_group,
            Exercise.types.any(program_type),
            Exercise.id != source.id,
        )
        .all()
    )
