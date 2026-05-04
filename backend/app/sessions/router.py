from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth.deps import get_current_user
from app.models import User
from app.sessions import schemas, service
from typing import Optional

router = APIRouter(prefix="/sessions", tags=["sessions"])


@router.post("/", response_model=schemas.SessionOut)
def complete_workout(
    body: schemas.SessionCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return service.create_session(db, str(user.id), str(body.workout_day_id), str(body.program_id))


@router.get("/weekly", response_model=list[schemas.SessionOut])
def weekly_sessions(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
    x_timezone: str = Header(default="UTC"),
):
    return service.get_weekly_sessions(db, str(user.id), tz=x_timezone)


@router.get("/count/{program_id}")
def program_session_count(
    program_id: str,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
    x_timezone: str = Header(default="UTC"),
):
    return service.get_program_session_counts(db, str(user.id), program_id, tz=x_timezone)


@router.get("/history", response_model=list[schemas.SessionOut])
def session_history(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return service.get_history(db, str(user.id))
