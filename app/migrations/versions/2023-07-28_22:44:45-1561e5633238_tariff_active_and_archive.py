"""tariff active and archive

Revision ID: 1561e5633238
Revises: 245907d587fd
Create Date: 2023-07-28 22:44:45.840998

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = '1561e5633238'
down_revision = '245907d587fd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tariffs', sa.Column('active', sa.Boolean(), server_default=sa.text('true'), nullable=False))
    op.add_column('tariffs', sa.Column('archive', sa.Boolean(), server_default=sa.text('false'), nullable=False))
    op.add_column('user_subscribe', sa.Column('end_date', sa.DateTime(), nullable=False))
    op.drop_column('user_subscribe', 'start_date')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_subscribe', sa.Column('start_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
    op.drop_column('user_subscribe', 'end_date')
    op.drop_column('tariffs', 'archive')
    op.drop_column('tariffs', 'active')
    # ### end Alembic commands ###
