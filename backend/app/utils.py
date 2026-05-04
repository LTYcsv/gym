from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


def get_week_start_utc(tz_name: str = "UTC") -> datetime:
    try:
        tz = ZoneInfo(tz_name)
    except (ZoneInfoNotFoundError, Exception):
        tz = ZoneInfo("UTC")

    now_local = datetime.now(tz)
    monday_local = (now_local - timedelta(days=now_local.weekday())).replace(
        hour=0, minute=0, second=0, microsecond=0
    )
    return monday_local.astimezone(timezone.utc).replace(tzinfo=None)


def get_now_utc(tz_name: str = "UTC") -> datetime:
    """Returns current UTC time, but anchored to the user's local 'now' for streak calculations."""
    try:
        tz = ZoneInfo(tz_name)
    except (ZoneInfoNotFoundError, Exception):
        tz = ZoneInfo("UTC")
    return datetime.now(tz).astimezone(timezone.utc).replace(tzinfo=None)
