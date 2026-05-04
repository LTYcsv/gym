"""workout_day label title not null

Revision ID: a1b2c3d4e5f6
Revises: f4770111e3d2
Create Date: 2025-05-04
"""
from alembic import op

revision = 'a1b2c3d4e5f6'
down_revision = 'f4770111e3d2'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('workout_days', 'label', nullable=False)
    op.alter_column('workout_days', 'title', nullable=False)


def downgrade():
    op.alter_column('workout_days', 'label', nullable=True)
    op.alter_column('workout_days', 'title', nullable=True)
