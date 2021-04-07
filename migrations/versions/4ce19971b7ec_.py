"""empty message

Revision ID: 4ce19971b7ec
Revises: 4f77228af1bc
Create Date: 2020-12-30 19:58:57.672376

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ce19971b7ec'
down_revision = '4f77228af1bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('albums', sa.Column('country', sa.String(), nullable=True))
    op.add_column('albums', sa.Column('publisher', sa.String(), nullable=True))
    op.add_column('albums', sa.Column('record_label', sa.String(), nullable=True))
    op.add_column('albums', sa.Column('region', sa.String(), nullable=True))
    op.add_column('albums', sa.Column('release_date', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('albums', 'release_date')
    op.drop_column('albums', 'region')
    op.drop_column('albums', 'record_label')
    op.drop_column('albums', 'publisher')
    op.drop_column('albums', 'country')
    # ### end Alembic commands ###
