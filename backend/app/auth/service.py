import hashlib
import hmac
import json
from urllib.parse import parse_qsl
from sqlalchemy.orm import Session
from app.config import settings
from app.models import User


def validate_init_data(init_data: str) -> dict:
    """Validate Telegram WebApp initData and return parsed user dict."""
    parsed = dict(parse_qsl(init_data, keep_blank_values=True))
    received_hash = parsed.pop("hash", None)
    if not received_hash:
        raise ValueError("Missing hash")

    data_check_string = "\n".join(
        f"{k}={v}" for k, v in sorted(parsed.items())
    )
    secret_key = hmac.new(
        b"WebAppData", settings.BOT_TOKEN.encode(), hashlib.sha256
    ).digest()
    computed_hash = hmac.new(
        secret_key, data_check_string.encode(), hashlib.sha256
    ).hexdigest()

    if not hmac.compare_digest(computed_hash, received_hash):
        raise ValueError("Invalid initData hash")

    user_data = parsed.get("user")
    if not user_data:
        raise ValueError("No user in initData")

    return json.loads(user_data)


def get_or_create_user(db: Session, tg_user: dict) -> User:
    user = db.query(User).filter(User.telegram_id == tg_user["id"]).first()
    if not user:
        user = User(
            telegram_id=tg_user["id"],
            username=tg_user.get("username"),
            first_name=tg_user.get("first_name", ""),
            last_name=tg_user.get("last_name"),
        )
        db.add(user)
        db.commit()
        db.refresh(user)
    return user
