"""empty message

Revision ID: 613d006ab2ec
Revises: 9567f1b42dca
Create Date: 2018-03-25 12:43:32.754460

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '613d006ab2ec'
down_revision = '9567f1b42dca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('payments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('payment_type', sa.String(length=20), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('payments')
    # ### end Alembic commands ###
