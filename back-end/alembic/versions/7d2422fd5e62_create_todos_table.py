"""create todos table

Revision ID: 7d2422fd5e62
Revises: 
Create Date: 2024-08-12 19:36:18.459578

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7d2422fd5e62'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
     op.execute("""
        create table todos(
        id bigserial primary key,
        name text,
        completed boolean not null default false
    )
     """)

def downgrade():
     op.execute("drop table todos;")

def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
