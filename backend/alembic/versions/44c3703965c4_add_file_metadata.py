"""add file metadata

Revision ID: 44c3703965c4
Revises: be962dd770db
Create Date: 2026-07-16 19:27:21.544252

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "44c3703965c4"
down_revision: Union[str, Sequence[str], None] = "be962dd770db"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    op.add_column(
        "images",
        sa.Column(
            "file_category",
            sa.String(length=50),
            nullable=True,
        ),
    )

    op.add_column(
        "images",
        sa.Column(
            "ai_status",
            sa.String(length=50),
            nullable=True,
        ),
    )

    op.add_column(
        "images",
        sa.Column(
            "ai_summary",
            sa.Text(),
            nullable=True,
        ),
    )

    op.add_column(
        "images",
        sa.Column(
            "ai_tags",
            sa.Text(),
            nullable=True,
        ),
    )


def downgrade() -> None:

    op.drop_column(
        "images",
        "ai_tags",
    )

    op.drop_column(
        "images",
        "ai_summary",
    )

    op.drop_column(
        "images",
        "ai_status",
    )

    op.drop_column(
        "images",
        "file_category",
    )
