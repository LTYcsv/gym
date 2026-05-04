"""initial

Revision ID: f4770111e3d2
Revises:
Create Date: 2026-05-04 12:05:06.070104

"""
from typing import Sequence, Union

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from alembic import op


revision: str = 'f4770111e3d2'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('telegram_id', sa.BigInteger(), nullable=False),
        sa.Column('username', sa.String(100)),
        sa.Column('first_name', sa.String(100)),
        sa.Column('last_name', sa.String(100)),
        sa.Column('created_at', sa.DateTime()),
        sa.UniqueConstraint('telegram_id'),
    )

    op.create_table(
        'programs',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('slug', sa.String(100), nullable=False),
        sa.Column('description', sa.Text()),
        sa.Column('type', sa.String(50), nullable=False),
        sa.Column('days_per_week', sa.Integer()),
        sa.Column('difficulty', sa.String(20)),
        sa.Column('goal', sa.String(100)),
        sa.Column('is_active', sa.Boolean()),
        sa.Column('created_at', sa.DateTime()),
        sa.UniqueConstraint('slug'),
    )

    op.create_table(
        'exercises',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('name', sa.String(200), nullable=False),
        sa.Column('muscle_group', sa.String(50), nullable=False),
        sa.Column('types', postgresql.ARRAY(sa.String()), nullable=False),
        sa.Column('equipment', postgresql.ARRAY(sa.String()), nullable=False),
        sa.Column('technique', sa.Text()),
        sa.Column('difficulty', sa.String(20)),
    )

    op.create_table(
        'workout_days',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('program_id', postgresql.UUID(as_uuid=True), sa.ForeignKey('programs.id'), nullable=False),
        sa.Column('label', sa.String(50), nullable=False),
        sa.Column('title', sa.String(100), nullable=False),
        sa.Column('subtitle', sa.String(100)),
        sa.Column('day_number', sa.Integer(), nullable=False),
    )

    op.create_table(
        'workout_exercises',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('workout_day_id', postgresql.UUID(as_uuid=True), sa.ForeignKey('workout_days.id'), nullable=False),
        sa.Column('exercise_id', postgresql.UUID(as_uuid=True), sa.ForeignKey('exercises.id'), nullable=False),
        sa.Column('sets', sa.Integer()),
        sa.Column('reps', sa.String(20)),
        sa.Column('rest_seconds', sa.Integer()),
        sa.Column('order', sa.Integer(), nullable=False),
        sa.Column('notes', sa.Text()),
    )

    op.create_table(
        'workout_sessions',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('user_id', postgresql.UUID(as_uuid=True), sa.ForeignKey('users.id'), nullable=False),
        sa.Column('workout_day_id', postgresql.UUID(as_uuid=True), sa.ForeignKey('workout_days.id'), nullable=False),
        sa.Column('program_id', postgresql.UUID(as_uuid=True), sa.ForeignKey('programs.id'), nullable=False),
        sa.Column('completed_at', sa.DateTime()),
    )
    op.create_index('ix_workout_sessions_user_completed', 'workout_sessions', ['user_id', 'completed_at'])

    op.create_table(
        'user_programs',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('user_id', postgresql.UUID(as_uuid=True), sa.ForeignKey('users.id'), nullable=False),
        sa.Column('program_id', postgresql.UUID(as_uuid=True), sa.ForeignKey('programs.id'), nullable=False),
        sa.Column('days_per_week', sa.Integer(), nullable=False),
        sa.Column('started_at', sa.DateTime()),
        sa.UniqueConstraint('user_id', 'program_id'),
    )
    op.create_index('ix_user_programs_user_id', 'user_programs', ['user_id'])

    op.create_table(
        'user_exercise_weights',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('user_id', postgresql.UUID(as_uuid=True), sa.ForeignKey('users.id'), nullable=False),
        sa.Column('workout_exercise_id', postgresql.UUID(as_uuid=True), sa.ForeignKey('workout_exercises.id'), nullable=False),
        sa.Column('weight_kg', sa.Float(), nullable=False),
        sa.Column('updated_at', sa.DateTime()),
        sa.UniqueConstraint('user_id', 'workout_exercise_id'),
    )

    op.create_table(
        'user_weight_logs',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('user_id', postgresql.UUID(as_uuid=True), sa.ForeignKey('users.id'), nullable=False),
        sa.Column('exercise_id', postgresql.UUID(as_uuid=True), sa.ForeignKey('exercises.id'), nullable=False),
        sa.Column('weight_kg', sa.Float(), nullable=False),
        sa.Column('logged_at', sa.DateTime()),
    )
    op.create_index('ix_user_weight_logs_user_exercise', 'user_weight_logs', ['user_id', 'exercise_id'])


def downgrade() -> None:
    op.drop_index('ix_user_weight_logs_user_exercise', table_name='user_weight_logs')
    op.drop_table('user_weight_logs')
    op.drop_table('user_exercise_weights')
    op.drop_index('ix_user_programs_user_id', table_name='user_programs')
    op.drop_table('user_programs')
    op.drop_index('ix_workout_sessions_user_completed', table_name='workout_sessions')
    op.drop_table('workout_sessions')
    op.drop_table('workout_exercises')
    op.drop_table('workout_days')
    op.drop_table('exercises')
    op.drop_table('programs')
    op.drop_table('users')
