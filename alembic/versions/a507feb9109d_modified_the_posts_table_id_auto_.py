"""modified the posts table id auto-increatement

Revision ID: a507feb9109d
Revises: cd0f67a52a6f
Create Date: 2025-03-29 15:41:00.777679

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a507feb9109d'
down_revision: Union[str, None] = 'cd0f67a52a6f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("CREATE SEQUENCE IF NOT EXISTS posts_id_seq")
    op.execute("ALTER TABLE posts ALTER COLUMN id SET DEFAULT nextval('posts_id_seq')")
    op.execute("ALTER SEQUENCE posts_id_seq OWNED BY posts.id")
    op.execute("SELECT setval('posts_id_seq', COALESCE((SELECT MAX(id) FROM posts), 1) + 1)")
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    op.execute("ALTER TABLE posts ALTER COLUMN id DROP DEFAULT")
    op.execute("DROP SEQUENCE IF EXISTS posts_id_seq")
    pass
    # ### end Alembic commands ###
