"""Add weather data table.

Revision ID: 9e995222de98
Revises:
Create Date: 2021-10-20 01:43:12.914090
"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '9e995222de98'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'weather_data',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created_date', sa.DateTime(), nullable=False),
        sa.Column('updated_date', sa.DateTime(), nullable=False),
        sa.Column('city', sa.String(length=50), nullable=True),
        sa.Column('country', sa.String(length=20), nullable=True),
        sa.Column(
            'wind_speed', sa.DECIMAL(precision=5, scale=1), nullable=True
        ),
        sa.Column('wind_deg', sa.Integer(), nullable=True),
        sa.Column('cloudiness', sa.Float(), nullable=True),
        sa.Column(
            'temperature', sa.DECIMAL(precision=5, scale=2), nullable=True
        ),
        sa.Column('pressure', sa.Integer(), nullable=True),
        sa.Column('humidity', sa.Integer(), nullable=True),
        sa.Column('sunrise', sa.DateTime(), nullable=True),
        sa.Column('sunset', sa.DateTime(), nullable=True),
        sa.Column('lat', sa.DECIMAL(precision=11, scale=7), nullable=True),
        sa.Column('lng', sa.DECIMAL(precision=11, scale=7), nullable=True),
        sa.Column('requested_time', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
    )


def downgrade():
    op.drop_table('weather_data')
