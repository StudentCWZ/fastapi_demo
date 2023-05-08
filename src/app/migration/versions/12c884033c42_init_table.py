"""init_table

Revision ID: 12c884033c42
Revises: 5742abd377ae
Create Date: 2023-03-19 18:46:42.088136

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "12c884033c42"
down_revision = "5742abd377ae"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "article",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("title", sa.String(length=500), nullable=True),
        sa.Column("body", sa.Text(), nullable=True),
        sa.Column("create_time", sa.DateTime(), nullable=False),
        sa.Column("update_time", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        mysql_collate="utf8mb4_general_ci",
        mysql_engine="InnoDB",
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("article")
    # ### end Alembic commands ###
