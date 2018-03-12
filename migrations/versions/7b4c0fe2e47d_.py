"""Create tables `domains`, `projects`, `roles`, `users`

Revision ID: 7b4c0fe2e47d
Revises: dcf9e4a81439
Create Date: 2018-03-08 03:12:20.818577

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b4c0fe2e47d'
down_revision = 'dcf9e4a81439'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'domains',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=128), nullable=False),
        sa.Column('description', sa.String(length=128), nullable=True),
        sa.Column('enabled', sa.Integer(), nullable=False, default=0),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        'projects',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('domain', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=128), nullable=False),
        sa.Column('description', sa.String(length=128), nullable=True),
        sa.Column('enabled', sa.Integer(), nullable=False, default=0),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        'roles',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('project', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=128), nullable=False),
        sa.Column('description', sa.String(length=128), nullable=True),
        sa.Column('enabled', sa.Integer(), nullable=False, default=0),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(length=128), nullable=False),
        sa.Column('password', sa.String(length=32), nullable=True),
        sa.Column('enabled', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('domains')
    op.drop_table('projects')
    op.drop_table('roles')
    op.drop_table('users')
