from datetime import timezone
from app.utils import get_week_start_utc, get_now_utc


def test_week_start_is_monday():
    result = get_week_start_utc("UTC")
    assert result.weekday() == 0


def test_week_start_midnight():
    result = get_week_start_utc("UTC")
    assert result.hour == 0
    assert result.minute == 0
    assert result.second == 0


def test_week_start_naive():
    result = get_week_start_utc("UTC")
    assert result.tzinfo is None


def test_week_start_invalid_tz_falls_back():
    result = get_week_start_utc("Not/ATimezone")
    assert result.weekday() == 0


def test_now_utc_naive():
    result = get_now_utc("UTC")
    assert result.tzinfo is None


def test_now_utc_invalid_tz_falls_back():
    result = get_now_utc("Bad/Timezone")
    assert result is not None
