"""Initial commit

Revision ID: 56e3663d5bc4
Revises: 
Create Date: 2024-06-03 20:21:30.286373

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '56e3663d5bc4'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String, nullable=False),
        sa.Column('email', sa.String, nullable=False),
        sa.Column('hashed_password', sa.String, nullable=False),
    )


# Define the downgrade function to drop the table (optional)
def downgrade():
    op.drop_table('users')
