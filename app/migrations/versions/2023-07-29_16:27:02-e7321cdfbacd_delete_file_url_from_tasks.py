"""delete file url from tasks

Revision ID: e7321cdfbacd
Revises: 225a3e639cb6
Create Date: 2023-07-29 16:27:02.712739

"""
import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = 'e7321cdfbacd'
down_revision = '225a3e639cb6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tasks', 'file_url')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('file_url', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###