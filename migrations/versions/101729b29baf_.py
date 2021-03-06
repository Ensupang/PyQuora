"""empty message

Revision ID: 101729b29baf
Revises: 517cf2912db4
Create Date: 2018-12-27 16:54:57.941123

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '101729b29baf'
down_revision = '517cf2912db4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('question',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('question')
    # ### end Alembic commands ###
