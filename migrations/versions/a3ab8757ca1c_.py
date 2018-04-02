"""Create Initial Schema

Revision ID: a3ab8757ca1c
Revises:
Create Date: 2018-04-01 16:24:53.625283

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a3ab8757ca1c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('application',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=5000), nullable=True),
    sa.Column('team', sa.Integer(), nullable=True),
    sa.Column('gender', sa.Enum('Male', 'Female', 'Other', name='gender_enum'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('criteria',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=25), nullable=True),
    sa.Column('description', sa.String(length=100), nullable=True),
    sa.Column('min_score', sa.Integer(), nullable=True),
    sa.Column('max_score', sa.Integer(), nullable=True),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.Column('medium', sa.Enum('Paper', 'Phone', name='interview_enum'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('members',
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('team', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('username')
    )
    op.create_table('submission',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('application', sa.Integer(), nullable=True),
    sa.Column('member', sa.String(length=50), nullable=True),
    sa.Column('medium', sa.Enum('Paper', 'Phone', name='interview_enum'), nullable=True),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['application'], ['application.id'], ),
    sa.ForeignKeyConstraint(['member'], ['members.username'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('submission')
    op.drop_table('members')
    op.drop_table('criteria')
    op.drop_table('application')
    # ### end Alembic commands ###