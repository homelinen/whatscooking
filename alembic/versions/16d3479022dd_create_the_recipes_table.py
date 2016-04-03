"""Create the recipes table

Revision ID: 16d3479022dd
Revises: 
Create Date: 2016-04-03 21:33:39.793774

"""

# revision identifiers, used by Alembic.
revision = '16d3479022dd'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
import sqlalchemy.dialects.postgresql as pg


def upgrade():
    op.create_table(
        'recipes',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(80), nullable=False),
        sa.Column('ingredients', pg.HSTORE(), nullable=False),
    )


def downgrade():
    op.drop_table('recipes')
