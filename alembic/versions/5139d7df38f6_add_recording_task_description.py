"""add Recording.task_description

Revision ID: 5139d7df38f6
Revises: b206c80f7640
Create Date: 2023-04-17 13:28:07.525123

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5139d7df38f6'
down_revision = 'b206c80f7640'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recording', schema=None) as batch_op:
        batch_op.add_column(sa.Column('task_description', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recording', schema=None) as batch_op:
        batch_op.drop_column('task_description')

    # ### end Alembic commands ###
