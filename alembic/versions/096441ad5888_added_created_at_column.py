"""added created_at column

Revision ID: 096441ad5888
Revises: d9443c0ee7f5
Create Date: 2024-09-25 12:05:35.979416

"""

from typing import Sequence

import sqlalchemy as sa

from alembic import op  # type: ignore

# revision identifiers, used by Alembic.
revision: str = "096441ad5888"
down_revision: str | None = "d9443c0ee7f5"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "weatherdata",
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
    )
    op.create_index(
        op.f("ix_weatherdata_created_at"), "weatherdata", ["created_at"], unique=False
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_weatherdata_created_at"), table_name="weatherdata")
    op.drop_column("weatherdata", "created_at")
    # ### end Alembic commands ###
