"""empty message

Revision ID: 20c3e2065cbe
Revises: 
Create Date: 2018-09-06 16:19:06.135711

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '20c3e2065cbe'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('governates',
    sa.Column('id', postgresql.UUID(as_uuid=True), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('name', sa.String(length=191), nullable=False),
    sa.Column('code', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('areas',
    sa.Column('id', postgresql.UUID(as_uuid=True), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('name', sa.String(length=191), nullable=False),
    sa.Column('code', sa.String(length=30), nullable=False),
    sa.Column('governates_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.ForeignKeyConstraint(['governates_id'], ['governates.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('villages',
    sa.Column('id', postgresql.UUID(as_uuid=True), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('name', sa.String(length=191), nullable=False),
    sa.Column('code', sa.String(length=30), nullable=False),
    sa.Column('areas_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.ForeignKeyConstraint(['areas_id'], ['areas.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('villages')
    op.drop_table('areas')
    op.drop_table('governates')
    # ### end Alembic commands ###
