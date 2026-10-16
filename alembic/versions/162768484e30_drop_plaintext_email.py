"""drop plaintext email

Revision ID: 162768484e30
Revises: 1d199a1fc105
Create Date: 2026-10-16 06:20:09.182148

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '162768484e30'
down_revision: Union[str, None] = '1d199a1fc105'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("users") as batch:
        batch.drop_index("ix_users_email")
        batch.drop_column("email")


def downgrade() -> None:
    with op.batch_alter_table("users") as batch:
        batch.add_column(sa.Column("email", sa.String(100), nullable=True))