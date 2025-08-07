"""add_test_data

Revision ID: 0c5ba43d0d43
Revises: 2b9c1df940ca
Create Date: 2025-08-07 07:51:03.986770

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.orm import Session
from db.models.organizations import (
    Organizations,
    ActivityTypes,
    Buildings,
    OrganizationsActivityTypes,
)
from utils.db_mock import (
    organizations,
    buildings,
    activity_types,
    organizations_activity_types,
)


# revision identifiers, used by Alembic.
revision: str = '0c5ba43d0d43'
down_revision: Union[str, Sequence[str], None] = '2b9c1df940ca'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    bind = op.get_bind()
    session = Session(bind=bind)

    session.add_all([Organizations(**org) for org in organizations])
    session.add_all([Buildings(**building) for building in buildings])
    session.add_all([ActivityTypes(**act) for act in activity_types])
    session.commit()
    session.add_all(
        [OrganizationsActivityTypes(**org_act) for org_act in organizations_activity_types]
    )

    session.commit()


def downgrade() -> None:
    """Downgrade schema."""
    pass
