"""change transaction pk

Revision ID: b963b490cda4
Revises: a56fd82904c1
Create Date: 2024-05-12 20:20:14.507913

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b963b490cda4'
down_revision: Union[str, None] = 'a56fd82904c1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transactions')
    op.create_table('transactions',
                    sa.Column('id', sa.Integer(), nullable=False, autoincrement=True),
                    sa.Column('volume', sa.Integer(), nullable=False),
                    sa.Column('price', sa.Float(), nullable=False),
                    sa.Column('security', sa.String(), nullable=False),
                    sa.Column('portfolio', sa.Integer(), nullable=False),
                    sa.Column('timestamp', sa.DateTime(timezone=True), nullable=False),
                    sa.ForeignKeyConstraint(['portfolio'], ['portfolio.id'], ),
                    sa.ForeignKeyConstraint(['security'], ['securities.ticker'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transactions')
    op.create_table('transactions',
                    sa.Column('id', sa.String(), nullable=False),
                    sa.Column('volume', sa.Integer(), nullable=False),
                    sa.Column('price', sa.Float(), nullable=False),
                    sa.Column('security', sa.String(), nullable=False),
                    sa.Column('portfolio', sa.Integer(), nullable=False),
                    sa.Column('timestamp', sa.DateTime(timezone=True), nullable=False),
                    sa.ForeignKeyConstraint(['portfolio'], ['portfolio.id'], ),
                    sa.ForeignKeyConstraint(['security'], ['securities.ticker'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###
