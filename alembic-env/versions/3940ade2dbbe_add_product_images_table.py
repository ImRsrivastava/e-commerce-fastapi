"""Add product_images table

Revision ID: 3940ade2dbbe
Revises: a9b071b64f9f
Create Date: 2026-02-22 17:21:36.974303

"""
from operator import index
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3940ade2dbbe'
down_revision: Union[str, Sequence[str], None] = 'a9b071b64f9f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "product_images",
        sa.Column ("id", sa.Integer, primary_key= True, index= True),
        sa.Column ("product_id", sa.Integer(), sa.ForeignKey("products.id"), index=True),
        sa.Column ("image_url", sa.String(200), nullable= True),

        sa.Column ("created_at", sa.DateTime(), nullable= True, server_default=sa.text("NOW()")),
        sa.Column ("updated_at", sa.DateTime(), nullable= True, server_default=sa.text("NOW()"))
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("product_images")
