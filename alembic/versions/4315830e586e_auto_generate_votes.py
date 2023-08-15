"""auto-generate votes

Revision ID: 4315830e586e
Revises: d49f96850d54
Create Date: 2023-08-12 08:43:35.384489

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4315830e586e'
down_revision = 'd49f96850d54'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table("likes",
                    sa.Column("post_id", sa.Integer, nullable=False),
                    sa.Column("user_id", sa.Integer, nullable=False),
                    sa.ForeignKeyConstraint(
                        ["post_id"], ["posts.id"], ondelete="CASCADE"),
                    sa.ForeignKeyConstraint(
                        ["user_id"], ["users.id"], ondelete="CASCADE"),
                    sa.PrimaryKeyConstraint("user_id", "post_id")
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("likes")
    # ### end Alembic commands ###