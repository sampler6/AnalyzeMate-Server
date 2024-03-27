"""change options -> config

Revision ID: 088c06118695
Revises: dca9a766464f
Create Date: 2024-03-28 01:57:29.038580

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '088c06118695'
down_revision: Union[str, None] = 'dca9a766464f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('config', postgresql.JSON(astext_type=sa.Text()), nullable=True))
    op.drop_column('users', 'options')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('options', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('users', 'config')
    # ### end Alembic commands ###
