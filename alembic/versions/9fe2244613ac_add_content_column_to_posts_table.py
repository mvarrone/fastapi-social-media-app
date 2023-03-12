"""add content column to posts table

Revision ID: 9fe2244613ac
Revises: 7fdf3bb2ae58
Create Date: 2023-03-12 09:18:42.766539

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9fe2244613ac'
down_revision = '7fdf3bb2ae58'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
