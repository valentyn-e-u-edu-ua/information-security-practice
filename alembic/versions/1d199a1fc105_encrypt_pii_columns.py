"""encrypt pii columns

Revision ID: 1d199a1fc105
Revises: f9294c6a8089
Create Date: 2026-10-16 06:20:01.839864

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1d199a1fc105'
down_revision: Union[str, None] = 'f9294c6a8089'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("users") as batch:
        batch.add_column(sa.Column("encrypted_email", sa.String(500), nullable=True))
        batch.add_column(sa.Column("email_index", sa.String(64), nullable=True))
        batch.add_column(sa.Column("encrypted_phone", sa.String(500), nullable=True))
        batch.create_index("ix_users_email_index", ["email_index"], unique=True)


def downgrade() -> None:
    with op.batch_alter_table("users") as batch:
        batch.drop_index("ix_users_email_index")
        batch.drop_column("encrypted_phone")
        batch.drop_column("email_index")
        batch.drop_column("encrypted_email")