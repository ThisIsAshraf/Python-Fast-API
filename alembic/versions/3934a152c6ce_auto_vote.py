"""auto-vote

Revision ID: 3934a152c6ce
Revises: 8c7f131d0fd3
Create Date: 2025-03-29 13:43:50.908201

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from sqlalchemy import inspect

# revision identifiers, used by Alembic.
revision: str = '3934a152c6ce'
down_revision: Union[str, None] = '8c7f131d0fd3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('votes',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', 'post_id')
    )
    
    # Only drop products table if it exists
    conn = op.get_bind()
    inspector = inspect(conn)
    if inspector.has_table('products'):
        op.drop_table('products')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('votes')
    
    # Only create products table if it doesn't exist
    conn = op.get_bind()
    inspector = inspect(conn)
    if not inspector.has_table('products'):
        op.create_table('products',
        sa.Column('product_id', sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column('price', sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column('is_sale', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=True),
        sa.Column('inventory', sa.INTEGER(), server_default=sa.text('0'), autoincrement=False, nullable=False),
        sa.Column('timestamps', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint('product_id', name='products_pkey')
        )
    # ### end Alembic commands ###