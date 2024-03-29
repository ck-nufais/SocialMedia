"""empty message

Revision ID: 8c9362e554b5
Revises: 3d333925f45f
Create Date: 2024-01-10 22:00:26.356140

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c9362e554b5'
down_revision = '3d333925f45f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('roomassociate',
    sa.Column('userid', sa.Integer(), nullable=False),
    sa.Column('roomid', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['roomid'], ['rooms.id'], ),
    sa.ForeignKeyConstraint(['userid'], ['users.id'], ),
    sa.PrimaryKeyConstraint('userid', 'roomid')
    )
    op.drop_table('room_r')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('room_r',
    sa.Column('userid', sa.INTEGER(), nullable=False),
    sa.Column('roomid', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['roomid'], ['rooms.id'], ),
    sa.ForeignKeyConstraint(['userid'], ['users.id'], ),
    sa.PrimaryKeyConstraint('userid', 'roomid')
    )
    op.drop_table('roomassociate')
    # ### end Alembic commands ###
