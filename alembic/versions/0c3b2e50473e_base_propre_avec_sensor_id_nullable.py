"""Base propre avec sensor_id nullable

Revision ID: 0c3b2e50473e
Revises: 
Create Date: 2025-04-02 22:35:14.763742

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0c3b2e50473e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('raw_sensor_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('accelerometer', sa.String(), nullable=True),
    sa.Column('gyroscope', sa.String(), nullable=True),
    sa.Column('magnetometer', sa.String(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_raw_sensor_data_id'), 'raw_sensor_data', ['id'], unique=False)
    op.create_table('sensor_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sensor_id', sa.Integer(), nullable=True),
    sa.Column('repetitions', sa.Integer(), nullable=False),
    sa.Column('duration', sa.Float(), nullable=False),
    sa.Column('difficulty', sa.Float(), nullable=False),
    sa.Column('speed', sa.Float(), nullable=False),
    sa.Column('amplitude', sa.Float(), nullable=False),
    sa.Column('left_side_force', sa.Float(), nullable=False),
    sa.Column('right_side_force', sa.Float(), nullable=False),
    sa.Column('imbalance_percentage', sa.Float(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_sensor_data_id'), 'sensor_data', ['id'], unique=False)
    op.create_table('sensor_status',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sensor_id', sa.Integer(), nullable=False),
    sa.Column('battery_level', sa.Float(), nullable=False),
    sa.Column('firmware_version', sa.String(), nullable=False),
    sa.Column('is_functional', sa.Boolean(), nullable=True),
    sa.Column('last_update', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_sensor_status_id'), 'sensor_status', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_sensor_status_id'), table_name='sensor_status')
    op.drop_table('sensor_status')
    op.drop_index(op.f('ix_sensor_data_id'), table_name='sensor_data')
    op.drop_table('sensor_data')
    op.drop_index(op.f('ix_raw_sensor_data_id'), table_name='raw_sensor_data')
    op.drop_table('raw_sensor_data')
    # ### end Alembic commands ###
