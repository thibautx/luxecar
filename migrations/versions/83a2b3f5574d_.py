"""empty message

Revision ID: 83a2b3f5574d
Revises: 54064edf1d86
Create Date: 2016-09-16 23:25:02.281711

"""

# revision identifiers, used by Alembic.
revision = '83a2b3f5574d'
down_revision = '54064edf1d86'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('phone', sa.String(length=250), nullable=True))
    op.create_unique_constraint(None, 'user', ['phone'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'phone')
    ### end Alembic commands ###