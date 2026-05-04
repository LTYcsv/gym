from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth.deps import get_current_user
from app.models import User
from app.stats import schemas, service

router = APIRouter(prefix="/stats", tags=["stats"])


@router.get("/", response_model=schemas.StatsOut)
def get_stats(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return service.get_stats(db, str(user.id))
