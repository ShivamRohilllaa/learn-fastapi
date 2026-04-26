"""add unique in email

Revision ID: cecfc9f339ba
Revises: 409e1d96f168
Create Date: 2026-04-26 16:13:04.090582

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cecfc9f339ba'
down_revision: Union[str, Sequence[str], None] = '409e1d96f168'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("users") as batch_op:
        batch_op.create_unique_constraint('uq_users_email', ['email'])


def downgrade() -> None:
    """Downgrade schema."""
    pass
