from sqlalchemy.orm import Session
from app.models import UserProgram


def get_user_program(db: Session, user_id: str, program_id: str) -> UserProgram | None:
    return (
        db.query(UserProgram)
        .filter_by(user_id=user_id, program_id=program_id)
        .first()
    )


def upsert_user_program(db: Session, user_id: str, program_id: str, days_per_week: int) -> UserProgram:
    record = get_user_program(db, user_id, program_id)
    if record:
        record.days_per_week = days_per_week
    else:
        record = UserProgram(user_id=user_id, program_id=program_id, days_per_week=days_per_week)
        db.add(record)
    db.commit()
    db.refresh(record)
    return record


def get_all_user_programs(db: Session, user_id: str) -> list[UserProgram]:
    return db.query(UserProgram).filter_by(user_id=user_id).all()
