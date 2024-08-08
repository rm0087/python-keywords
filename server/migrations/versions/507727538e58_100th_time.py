"""100th time

Revision ID: 507727538e58
Revises: 4461ec3baaa1
Create Date: 2024-08-08 00:10:16.600483

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '507727538e58'
down_revision = '4461ec3baaa1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('keyword_table')
    op.drop_table('type_table')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('type_table',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('keyword_table',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(), nullable=False),
    sa.Column('type_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['type_id'], ['type_table.id'], name='fk_keyword_table_type_id_type_table'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
