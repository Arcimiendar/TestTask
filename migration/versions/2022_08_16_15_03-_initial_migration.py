"""initial migration

Revision ID: e59df2bf1ec5
Revises: 
Create Date: 2022-08-16 15:03:11.960839

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e59df2bf1ec5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("""
        CREATE TABLE calculation_result(
            id SERIAL PRIMARY KEY,
            left_operand FLOAT NOT NULL,
            right_operand FLOAT NOT NULL,
            result FLOAT NOT NULL,
            created_at DATE DEFAULT NOW()
        );
    """)


def downgrade() -> None:
    op.execute("""
        DROP TABLE calculation_result;
    """)
