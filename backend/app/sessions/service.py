from datetime import datetime, timedelta
from sqlalchemy.orm import Session as DBSession
from app.models import WorkoutSession


def create_session(db: DBSession, user_id: str, workout_day_id: str, program_id: str) -> WorkoutSession:
    session = WorkoutSession(
        user_id=user_id,
        workout_day_id=workout_day_id,
        program_id=program_id,
    )
    db.add(session)
    db.commit()
    db.refresh(session)
    return session


def get_weekly_sessions(db: DBSession, user_id: str) -> list[WorkoutSession]:
    now = datetime.utcnow()
    week_start = (now - timedelta(days=now.weekday())).replace(hour=0, minute=0, second=0, microsecond=0)
    return (
        db.query(WorkoutSession)
        .filter(WorkoutSession.user_id == user_id, WorkoutSession.completed_at >= week_start)
        .order_by(WorkoutSession.completed_at.desc())
        .all()
    )


def get_program_session_counts(db: DBSession, user_id: str, program_id: str) -> dict:
    total = (
        db.query(WorkoutSession)
        .filter_by(user_id=user_id, program_id=program_id)
        .count()
    )
    now = datetime.utcnow()
    week_start = (now - timedelta(days=now.weekday())).replace(hour=0, minute=0, second=0, microsecond=0)
    weekly = (
        db.query(WorkoutSession)
        .filter(
            WorkoutSession.user_id == user_id,
            WorkoutSession.program_id == program_id,
            WorkoutSession.completed_at >= week_start,
        )
        .count()
    )
    return {"total": total, "weekly": weekly}


def get_history(db: DBSession, user_id: str, limit: int = 50) -> list[WorkoutSession]:
    return (
        db.query(WorkoutSession)
        .filter(WorkoutSession.user_id == user_id)
        .order_by(WorkoutSession.completed_at.desc())
        .limit(limit)
        .all()
    )
