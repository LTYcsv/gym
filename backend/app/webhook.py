from fastapi import APIRouter, Request
from app.config import settings
import httpx

router = APIRouter()

@router.post("/webhook")
async def telegram_webhook(request: Request):
    return {"ok": True}
