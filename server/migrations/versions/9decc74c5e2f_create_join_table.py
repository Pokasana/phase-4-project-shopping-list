"""create join table

Revision ID: 9decc74c5e2f
Revises: b6d4ef67b3b9
Create Date: 2024-03-20 18:48:58.490929

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9decc74c5e2f'
down_revision = 'b6d4ef67b3b9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users_shops',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('shop_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['shop_id'], ['shops.id'], name=op.f('fk_users_shops_shop_id_shops')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_users_shops_user_id_users')),
    sa.PrimaryKeyConstraint('user_id', 'shop_id')
    )
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('shop_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.alter_column('shop_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    op.drop_table('users_shops')
    # ### end Alembic commands ###
