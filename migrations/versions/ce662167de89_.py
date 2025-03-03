"""empty message

Revision ID: ce662167de89
Revises: b90154cbbfc1
Create Date: 2021-07-28 19:49:07.423323

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ce662167de89'
down_revision = 'b90154cbbfc1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('chat', sa.Column('name', sa.String(length=64), nullable=True))
    op.add_column('chat', sa.Column('hash_key', sa.String(length=10), nullable=True))
    op.create_index(op.f('ix_chat_hash_key'), 'chat', ['hash_key'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_chat_hash_key'), table_name='chat')
    op.drop_column('chat', 'hash_key')
    op.drop_column('chat', 'name')
    # ### end Alembic commands ###
