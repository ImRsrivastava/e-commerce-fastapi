"""Add products table

Revision ID: a9b071b64f9f
Revises: 
Create Date: 2026-02-22 17:21:24.111254

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a9b071b64f9f'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "products",
        sa.Column ( "id", sa.Integer(), primary_key = True, index = True ),
        sa.Column ( "shop_id", sa.Integer(), sa.ForeignKey("shops.id"), index= True),
        sa.Column ("category_id", sa.Integer(), sa.ForeignKey("categories.id"), index=True),
        sa.Column ("auth_id", sa.Integer(), sa.ForeignKey("auths.id"), index=True),
        sa.Column ("name", sa.String(150), nullable=True),
        sa.Column ("description", sa.Text(), nullable=True),
        sa.Column ("price", sa.Float(), nullable=True, server_default="0.00"),
        sa.Column ("stock", sa.Integer(), server_default="0" ),

        sa.Column ("is_active", sa.Boolean(), server_default=sa.text("TRUE")),

        sa.Column ("created_at", sa.DateTime(), nullable=False, server_default=sa.text("NOW()")),
        sa.Column ("updated_at", sa.DateTime(), nullable=False, server_default=sa.text("NOW()"))
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("products")
