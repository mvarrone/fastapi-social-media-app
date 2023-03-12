"""add last few columns to posts table

Revision ID: 43dc29ba67aa
Revises: ca69dda65659
Create Date: 2023-03-12 09:52:57.673183

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '43dc29ba67aa'
down_revision = 'ca69dda65659'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(),
                  nullable=False, server_default='TRUE'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                                     nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
