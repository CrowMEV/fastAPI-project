"""lastname and firstname in user model not required

Revision ID: b3d9f56436a7
Revises: 280610ccc91c
Create Date: 2023-06-26 10:30:35.651669

"""
import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = 'b3d9f56436a7'
down_revision = '280610ccc91c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'firstname',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('users', 'lastname',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("UPDATE users SET lastname = '' WHERE lastname is null")
    op.execute("UPDATE users SET firstname = '' WHERE firstname is null")
    op.alter_column('users', 'lastname',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('users', 'firstname',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###
