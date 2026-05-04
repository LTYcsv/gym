from datetime import datetime, timedelta
from types import SimpleNamespace
from app.stats.service import _calc_week_streak, _calc_workout_streak


def session(days_ago: int, anchor: datetime) -> SimpleNamespace:
    return SimpleNamespace(completed_at=anchor - timedelta(days=days_ago))


# ── _calc_week_streak ────────────────────────────────────────────────────────

class TestCalcWeekStreak:
    # Wednesday: days 0/1/2 all stay in week 19; day 7 steps exactly into week 18
    NOW = datetime(2025, 5, 7)  # Wednesday, ISO week 19

    def test_no_sessions_returns_zero(self):
        assert _calc_week_streak([], self.NOW) == 0

    def test_single_session_this_week(self):
        sessions = [session(0, self.NOW)]
        assert _calc_week_streak(sessions, self.NOW) == 1

    def test_two_consecutive_weeks(self):
        # week 19 + week 18
        sessions = [session(0, self.NOW), session(7, self.NOW)]
        assert _calc_week_streak(sessions, self.NOW) == 2

    def test_three_consecutive_weeks(self):
        sessions = [session(0, self.NOW), session(7, self.NOW), session(14, self.NOW)]
        assert _calc_week_streak(sessions, self.NOW) == 3

    def test_gap_in_weeks_breaks_streak(self):
        # week 19 + week 17 (week 18 missing)
        sessions = [session(0, self.NOW), session(14, self.NOW)]
        assert _calc_week_streak(sessions, self.NOW) == 1

    def test_no_session_this_week_returns_zero(self):
        # only previous week
        sessions = [session(7, self.NOW)]
        assert _calc_week_streak(sessions, self.NOW) == 0

    def test_multiple_sessions_same_week_count_as_one(self):
        # three sessions this week still = streak of 1
        sessions = [session(0, self.NOW), session(1, self.NOW), session(2, self.NOW)]
        assert _calc_week_streak(sessions, self.NOW) == 1


# ── _calc_workout_streak ─────────────────────────────────────────────────────

class TestCalcWorkoutStreak:
    NOW = datetime(2025, 5, 5)

    def test_no_sessions_returns_zero(self):
        assert _calc_workout_streak([], self.NOW) == 0

    def test_last_session_over_7_days_ago_returns_zero(self):
        sessions = [session(8, self.NOW)]
        assert _calc_workout_streak(sessions, self.NOW) == 0

    def test_last_session_exactly_7_days_ago_counts(self):
        sessions = [session(7, self.NOW)]
        assert _calc_workout_streak(sessions, self.NOW) == 1

    def test_single_recent_session(self):
        sessions = [session(1, self.NOW)]
        assert _calc_workout_streak(sessions, self.NOW) == 1

    def test_three_sessions_within_7_day_gaps(self):
        sessions = [session(0, self.NOW), session(4, self.NOW), session(7, self.NOW)]
        assert _calc_workout_streak(sessions, self.NOW) == 3

    def test_gap_over_7_days_breaks_streak(self):
        sessions = [session(0, self.NOW), session(3, self.NOW), session(12, self.NOW)]
        assert _calc_workout_streak(sessions, self.NOW) == 2

    def test_streak_stops_at_first_gap(self):
        # gaps: 3, 8, 2 — stops at second gap
        sessions = [
            session(0, self.NOW),
            session(3, self.NOW),
            session(11, self.NOW),
            session(13, self.NOW),
        ]
        assert _calc_workout_streak(sessions, self.NOW) == 2
