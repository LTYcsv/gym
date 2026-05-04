from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth.deps import get_current_user
from app.models import User
from app.programs import schemas, service
from app.sessions.service import get_weekly_sessions
from app.user_programs.service import get_all_user_programs

router = APIRouter(prefix="/programs", tags=["programs"])


@router.get("/", response_model=list[schemas.ProgramOut])
def list_programs(db: Session = Depends(get_db)):
    programs = service.list_programs(db)
    return [schemas.ProgramOut.model_validate(p) for p in programs]


@router.get("/with-progress", response_model=list[schemas.ProgramOut])
def list_programs_with_progress(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
    x_timezone: str = Header(default="UTC"),
):
    programs = service.list_programs(db)
    weekly = get_weekly_sessions(db, str(user.id), tz=x_timezone)
    counts: dict[str, int] = {}
    for s in weekly:
        key = str(s.program_id)
        counts[key] = counts.get(key, 0) + 1

    enrollments = {str(e.program_id): e for e in get_all_user_programs(db, str(user.id))}

    result = []
    for p in programs:
        out = schemas.ProgramOut.model_validate(p)
        out.weekly_sessions = counts.get(str(p.id), 0)
        enrollment = enrollments.get(str(p.id))
        out.user_days_per_week = enrollment.days_per_week if enrollment else None
        result.append(out)
    return result


@router.get("/{slug}", response_model=schemas.ProgramDetail)
def get_program(slug: str, db: Session = Depends(get_db)):
    program = service.get_program(db, slug)
    if not program:
        raise HTTPException(404, "Program not found")
    days = [
        schemas.WorkoutDaySummary(
            id=d.id,
            label=d.label,
            title=d.title,
            subtitle=d.subtitle,
            day_number=d.day_number,
            exercise_count=len(d.workout_exercises),
        )
        for d in program.workout_days
    ]
    return schemas.ProgramDetail(
        **schemas.ProgramOut.model_validate(program).model_dump(),
        workout_days=days,
    )


@router.get("/{slug}/days/{day_id}", response_model=schemas.WorkoutDayOut)
def get_workout_day(slug: str, day_id: str, db: Session = Depends(get_db)):
    day = service.get_workout_day(db, day_id)
    if not day or day.program.slug != slug:
        raise HTTPException(404, "Workout day not found")
    return schemas.WorkoutDayOut(
        id=day.id,
        program_id=day.program_id,
        program_type=day.program.type,
        program_slug=day.program.slug,
        label=day.label,
        title=day.title,
        subtitle=day.subtitle,
        day_number=day.day_number,
        workout_exercises=day.workout_exercises,
    )
