"""empty message

Revision ID: 49fe1c6df959
Revises: 8ad1e0faad5
Create Date: 2016-10-23 00:55:04.913000

"""

# revision identifiers, used by Alembic.
revision = '49fe1c6df959'
down_revision = '8ad1e0faad5'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('body_html', sa.Text(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'body_html')
    ### end Alembic commands ###