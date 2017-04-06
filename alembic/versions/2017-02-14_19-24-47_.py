revision = 'f5258cb0f15b'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blob',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('media_file',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('probe', postgresql.JSONB(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('media_file_variant',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('variant_name', sa.Text(), nullable=False),
    sa.Column('media_file_id', sa.Integer(), nullable=False),
    sa.Column('probe', postgresql.JSONB(), nullable=False),
    sa.Column('blob_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['blob_id'], ['blob.id'], ),
    sa.ForeignKeyConstraint(['media_file_id'], ['media_file.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('variant_name', 'media_file_id', name='ix__media_file_variant__variant_name__media_file_id')
    )
    op.create_table('uploaded_media_file',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('state', postgresql.ENUM('processing', 'converting', 'ready', 'error', name='uploaded_media_file_state'), nullable=False),
    sa.Column('tmp_path', sa.Text(), nullable=True),
    sa.Column('media_file_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['media_file_id'], ['media_file.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('uploaded_media_file')
    op.drop_table('media_file_variant')
    op.drop_table('media_file')
    op.drop_table('blob')
    # ### end Alembic commands ###
