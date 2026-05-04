from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, HTTPException
from jose import jwt
from sqlalchemy.orm import Session
from app.config import settings
from app.database import get_db
from app.auth import schemas, service

router = APIRouter(prefix="/auth", tags=["auth"])


def create_token(user_id: str) -> str:
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return jwt.encode(
        {"sub": user_id, "exp": expire},
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )


@router.post("/telegram", response_model=schemas.AuthResponse)
def auth_telegram(body: schemas.AuthRequest, db: Session = Depends(get_db)):
    try:
        tg_user = service.validate_init_data(body.init_data)
    except ValueError as e:
        raise HTTPException(401, str(e))

    user = service.get_or_create_user(db, tg_user)
    token = create_token(str(user.id))
    return {"token": token, "user": user}


@router.post("/dev", response_model=schemas.AuthResponse)
def auth_dev(db: Session = Depends(get_db)):
    """Только для локальной разработки."""
    if settings.SECRET_KEY != "dev-secret-change-in-prod":
        raise HTTPException(403, "Not available in production")

    user = service.get_or_create_user(db, {"id": 0, "first_name": "Dev", "username": "dev"})
    token = create_token(str(user.id))
    return {"token": token, "user": user}
