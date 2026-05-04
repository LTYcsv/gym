from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth.deps import get_current_user
from app.models import User, Program
from app.user_programs import schemas, service

router = APIRouter(prefix="/user-programs", tags=["user-programs"])


@router.post("/", response_model=schemas.UserProgramOut)
def enroll(
    body: schemas.UserProgramCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    program = db.query(Program).filter_by(id=body.program_id).first()
    if not program:
        raise HTTPException(404, "Program not found")
    return service.upsert_user_program(db, str(user.id), str(body.program_id), body.days_per_week)


@router.get("/{program_id}", response_model=schemas.UserProgramOut | None)
def get_enrollment(
    program_id: str,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return service.get_user_program(db, str(user.id), program_id)


@router.get("/", response_model=list[schemas.UserProgramOut])
def get_all_enrollments(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return service.get_all_user_programs(db, str(user.id))
