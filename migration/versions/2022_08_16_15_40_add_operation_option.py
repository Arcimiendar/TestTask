"""add operation option

Revision ID: 007a5036d58a
Revises: e59df2bf1ec5
Create Date: 2022-08-16 15:40:56.939251

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '007a5036d58a'
down_revision = 'e59df2bf1ec5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("""
        CREATE TYPE operation_option as ENUM ('+', '-', '*', '/');
        ALTER TABLE calculation_result ADD operation operation_option default '+';
    """)


def downgrade() -> None:
    op.execute("""
        ALTER TABLE calculation_result DROP COLUMN operation;
        DROP TYPE operation_option;
    """)
