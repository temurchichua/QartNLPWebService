"""empty message

Revision ID: 4073b078cc47
Revises: f2f61d2d1fb7
Create Date: 2021-07-09 19:47:03.291662

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4073b078cc47'
down_revision = 'f2f61d2d1fb7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('status', schema=None) as batch_op:
        batch_op.add_column(sa.Column('active', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('status', schema=None) as batch_op:
        batch_op.drop_column('active')

    # ### end Alembic commands ###