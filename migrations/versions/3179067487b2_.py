"""empty message

Revision ID: 3179067487b2
Revises: 
Create Date: 2017-10-26 18:02:02.206048

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3179067487b2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Books',
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=True),
    sa.Column('author', sa.String(length=60), nullable=True),
    sa.Column('publication_date', sa.Date(), nullable=True),
    sa.Column('rating', sa.Float(), nullable=True),
    sa.Column('review', sa.TEXT(), nullable=True),
    sa.Column('book_count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('book_id')
    )
    op.create_index(op.f('ix_Books_author'), 'Books', ['author'], unique=False)
    op.create_index(op.f('ix_Books_book_count'), 'Books', ['book_count'], unique=False)
    op.create_index(op.f('ix_Books_name'), 'Books', ['name'], unique=False)
    op.create_index(op.f('ix_Books_publication_date'), 'Books', ['publication_date'], unique=False)
    op.create_index(op.f('ix_Books_rating'), 'Books', ['rating'], unique=False)
    op.create_index(op.f('ix_Books_review'), 'Books', ['review'], unique=False)
    op.create_table('Users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=60), nullable=True),
    sa.Column('username', sa.String(length=60), nullable=True),
    sa.Column('first_name', sa.String(length=60), nullable=True),
    sa.Column('last_name', sa.String(length=60), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Users_email'), 'Users', ['email'], unique=False)
    op.create_index(op.f('ix_Users_first_name'), 'Users', ['first_name'], unique=False)
    op.create_index(op.f('ix_Users_last_name'), 'Users', ['last_name'], unique=False)
    op.create_index(op.f('ix_Users_username'), 'Users', ['username'], unique=False)
    op.create_table('Book_Photos',
    sa.Column('image_id', sa.Integer(), nullable=False),
    sa.Column('image_name', sa.String(length=60), nullable=True),
    sa.Column('path', sa.LargeBinary(), nullable=True),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['Books.book_id'], ),
    sa.PrimaryKeyConstraint('image_id')
    )
    op.create_index(op.f('ix_Book_Photos_image_name'), 'Book_Photos', ['image_name'], unique=False)
    op.create_index(op.f('ix_Book_Photos_path'), 'Book_Photos', ['path'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_Book_Photos_path'), table_name='Book_Photos')
    op.drop_index(op.f('ix_Book_Photos_image_name'), table_name='Book_Photos')
    op.drop_table('Book_Photos')
    op.drop_index(op.f('ix_Users_username'), table_name='Users')
    op.drop_index(op.f('ix_Users_last_name'), table_name='Users')
    op.drop_index(op.f('ix_Users_first_name'), table_name='Users')
    op.drop_index(op.f('ix_Users_email'), table_name='Users')
    op.drop_table('Users')
    op.drop_index(op.f('ix_Books_review'), table_name='Books')
    op.drop_index(op.f('ix_Books_rating'), table_name='Books')
    op.drop_index(op.f('ix_Books_publication_date'), table_name='Books')
    op.drop_index(op.f('ix_Books_name'), table_name='Books')
    op.drop_index(op.f('ix_Books_book_count'), table_name='Books')
    op.drop_index(op.f('ix_Books_author'), table_name='Books')
    op.drop_table('Books')
    # ### end Alembic commands ###
