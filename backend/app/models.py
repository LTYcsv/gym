import uuid
from datetime import datetime
from sqlalchemy import Column, String, Integer, BigInteger, Float, Text, Boolean, ForeignKey, DateTime, UniqueConstraint, Index
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from sqlalchemy.orm import relationship
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    telegram_id = Column(BigInteger, unique=True, nullable=False)
    username = Column(String(100))
    first_name = Column(String(100))
    last_name = Column(String(100))
    created_at = Column(DateTime, default=datetime.utcnow)


class Program(Base):
    __tablename__ = "programs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), nullable=False)
    slug = Column(String(100), unique=True, nullable=False)
    description = Column(Text)
    type = Column(String(50), nullable=False)
    days_per_week = Column(Integer)
    difficulty = Column(String(20))
    goal = Column(String(100))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    workout_days = relationship(
        "WorkoutDay", back_populates="program",
        cascade="all, delete-orphan", order_by="WorkoutDay.day_number"
    )


class Exercise(Base):
    __tablename__ = "exercises"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(200), nullable=False)
    muscle_group = Column(String(50), nullable=False)
    types = Column(ARRAY(String), nullable=False)
    equipment = Column(ARRAY(String), nullable=False)
    technique = Column(Text)
    difficulty = Column(String(20), default="intermediate")


class WorkoutDay(Base):
    __tablename__ = "workout_days"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    program_id = Column(UUID(as_uuid=True), ForeignKey("programs.id"), nullable=False)
    label = Column(String(50), nullable=False)
    title = Column(String(100), nullable=False)
    subtitle = Column(String(100))
    day_number = Column(Integer, nullable=False)

    program = relationship("Program", back_populates="workout_days")
    workout_exercises = relationship(
        "WorkoutExercise", back_populates="workout_day",
        cascade="all, delete-orphan", order_by="WorkoutExercise.order"
    )


class WorkoutExercise(Base):
    __tablename__ = "workout_exercises"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    workout_day_id = Column(UUID(as_uuid=True), ForeignKey("workout_days.id"), nullable=False)
    exercise_id = Column(UUID(as_uuid=True), ForeignKey("exercises.id"), nullable=False)
    sets = Column(Integer)
    reps = Column(String(20))
    rest_seconds = Column(Integer)
    order = Column(Integer, nullable=False)
    notes = Column(Text)

    workout_day = relationship("WorkoutDay", back_populates="workout_exercises")
    exercise = relationship("Exercise")


class WorkoutSession(Base):
    """Запись о выполненном дне тренировки."""
    __tablename__ = "workout_sessions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    workout_day_id = Column(UUID(as_uuid=True), ForeignKey("workout_days.id"), nullable=False)
    program_id = Column(UUID(as_uuid=True), ForeignKey("programs.id"), nullable=False)
    completed_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User")
    workout_day = relationship("WorkoutDay")
    program = relationship("Program")

    __table_args__ = (
        Index("ix_workout_sessions_user_completed", "user_id", "completed_at"),
    )


class UserProgram(Base):
    """Участие пользователя в программе с его персональными настройками."""
    __tablename__ = "user_programs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    program_id = Column(UUID(as_uuid=True), ForeignKey("programs.id"), nullable=False)
    days_per_week = Column(Integer, nullable=False)
    started_at = Column(DateTime, default=datetime.utcnow)

    __table_args__ = (
        UniqueConstraint("user_id", "program_id"),
        Index("ix_user_programs_user_id", "user_id"),
    )

    user = relationship("User")
    program = relationship("Program")


class UserExerciseWeight(Base):
    """Рабочий вес пользователя для конкретного упражнения в конкретной программе."""
    __tablename__ = "user_exercise_weights"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    workout_exercise_id = Column(UUID(as_uuid=True), ForeignKey("workout_exercises.id"), nullable=False)
    weight_kg = Column(Float, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    __table_args__ = (UniqueConstraint("user_id", "workout_exercise_id"),)

    user = relationship("User")
    workout_exercise = relationship("WorkoutExercise")


class UserWeightLog(Base):
    """История весов — каждое сохранение веса пишется сюда для PR и прогресса."""
    __tablename__ = "user_weight_logs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    exercise_id = Column(UUID(as_uuid=True), ForeignKey("exercises.id"), nullable=False)
    weight_kg = Column(Float, nullable=False)
    logged_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User")
    exercise = relationship("Exercise")

    __table_args__ = (
        Index("ix_user_weight_logs_user_exercise", "user_id", "exercise_id"),
    )
