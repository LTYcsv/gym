from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models import WorkoutSession, WorkoutExercise, Exercise, UserWeightLog, UserProgram
from app.stats.schemas import StatsOut, MuscleGroupCount, RecordItem


def get_stats(db: Session, user_id: str) -> StatsOut:
    now = datetime.utcnow()
    week_start = (now - timedelta(days=now.weekday())).replace(hour=0, minute=0, second=0, microsecond=0)
    month_ago = now - timedelta(days=30)

    # ── Weekly done ──────────────────────────────────────────────
    weekly_sessions = (
        db.query(WorkoutSession)
        .filter(WorkoutSession.user_id == user_id, WorkoutSession.completed_at >= week_start)
        .all()
    )
    weekly_done = len(weekly_sessions)

    # ── Weekly planned (sum of all enrolled programs) ────────────
    enrollments = db.query(UserProgram).filter_by(user_id=user_id).all()
    weekly_planned = sum(e.days_per_week for e in enrollments)

    # ── Muscle groups this week ──────────────────────────────────
    day_ids = [str(s.workout_day_id) for s in weekly_sessions]
    muscle_counts: dict[str, int] = {}
    if day_ids:
        rows = (
            db.query(Exercise.muscle_group, func.count().label("cnt"))
            .join(WorkoutExercise, WorkoutExercise.exercise_id == Exercise.id)
            .filter(WorkoutExercise.workout_day_id.in_(day_ids))
            .group_by(Exercise.muscle_group)
            .all()
        )
        muscle_counts = {r.muscle_group: r.cnt for r in rows}

    weekly_muscle_groups = [
        MuscleGroupCount(muscle_group=mg, count=cnt)
        for mg, cnt in sorted(muscle_counts.items(), key=lambda x: -x[1])
    ]

    # ── Workout dates (last 30 days) ─────────────────────────────
    month_sessions = (
        db.query(WorkoutSession)
        .filter(WorkoutSession.user_id == user_id, WorkoutSession.completed_at >= month_ago)
        .all()
    )
    workout_dates = sorted({s.completed_at.date().isoformat() for s in month_sessions})

    # ── Week streak ──────────────────────────────────────────────
    all_sessions = (
        db.query(WorkoutSession)
        .filter(WorkoutSession.user_id == user_id)
        .order_by(WorkoutSession.completed_at.desc())
        .all()
    )
    week_streak = _calc_week_streak(all_sessions, now)

    # ── Workout streak (consecutive sessions, gap <= 7 days) ─────
    workout_streak = _calc_workout_streak(all_sessions)

    # ── Personal records ─────────────────────────────────────────
    pr_rows = (
        db.query(
            Exercise.name,
            func.max(UserWeightLog.weight_kg).label("best"),
            func.max(UserWeightLog.logged_at).label("when"),
        )
        .join(UserWeightLog, UserWeightLog.exercise_id == Exercise.id)
        .filter(UserWeightLog.user_id == user_id)
        .group_by(Exercise.id, Exercise.name)
        .order_by(func.max(UserWeightLog.logged_at).desc())
        .limit(10)
        .all()
    )
    records = [
        RecordItem(exercise_name=r.name, weight_kg=r.best, achieved_at=r.when)
        for r in pr_rows
    ]

    return StatsOut(
        weekly_done=weekly_done,
        weekly_planned=weekly_planned,
        weekly_muscle_groups=weekly_muscle_groups,
        workout_dates=workout_dates,
        week_streak=week_streak,
        workout_streak=workout_streak,
        records=records,
    )


def _calc_week_streak(sessions: list, now: datetime) -> int:
    if not sessions:
        return 0
    weeks_with_sessions: set[int] = set()
    for s in sessions:
        # ISO week number as unique key: (year, week)
        iso = s.completed_at.isocalendar()
        weeks_with_sessions.add((iso[0], iso[1]))

    streak = 0
    check = now
    while True:
        iso = check.isocalendar()
        if (iso[0], iso[1]) in weeks_with_sessions:
            streak += 1
            check -= timedelta(weeks=1)
        else:
            break
    return streak


def _calc_workout_streak(sessions: list) -> int:
    if not sessions:
        return 0
    sorted_sessions = sorted(sessions, key=lambda s: s.completed_at, reverse=True)
    streak = 1
    for i in range(1, len(sorted_sessions)):
        gap = (sorted_sessions[i - 1].completed_at - sorted_sessions[i].completed_at).days
        if gap <= 7:
            streak += 1
        else:
            break
    return streak
