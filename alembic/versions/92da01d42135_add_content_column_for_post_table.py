"""add content column for post table

Revision ID: 92da01d42135
Revises: 42ebd5d9a1a3
Create Date: 2025-03-29 04:36:22.182777

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '92da01d42135'
down_revision: Union[str, None] = '42ebd5d9a1a3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
