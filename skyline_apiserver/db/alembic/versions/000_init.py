# Copyright 2021 99cloud
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""init

Revision ID: 000
Revises:
Create Date: 2020-11-22 06:43:23.717511

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "000"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "revoked_token",
        sa.Column("uuid", sa.String(length=128), nullable=False),
        sa.Column("expire", sa.Integer(), nullable=False),
    )
    op.create_index(op.f("ix_revoked_token_uuid"), "revoked_token", ["uuid"], unique=False)
    op.create_table(
        "settings",
        sa.Column("key", sa.String(length=128), nullable=False),
        sa.Column("value", sa.JSON(), nullable=True),
    )
    op.create_index(op.f("ix_settings_key"), "settings", ["key"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_settings_key"), table_name="settings")
    op.drop_table("settings")
    op.drop_index(op.f("ix_revoked_token_uuid"), table_name="revoked_token")
    op.drop_table("revoked_token")
    # ### end Alembic commands ###