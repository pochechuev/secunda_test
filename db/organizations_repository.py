from sqlalchemy.orm import selectinload, joinedload

from .models.organizations import Organizations, Buildings, ActivityTypes
from .repository import SQLAlchemyRepository


class OrganizationsRepository(SQLAlchemyRepository):
    """Organizations repository."""

    model = Organizations

    def get_all_orgs(self):
        return self.session.query(self.model).all()

    def get_org_by_id(self, org_id: int):
        return (
            self.session.query(self.model)
            .options(
                selectinload(self.model.activity_types),
                selectinload(self.model.building)
            )
            .filter(self.model.org_id == org_id)
            .first()
        )

    def get_org_by_name(self, name: str):
        return (
            self.session.query(self.model)
            .options(
                selectinload(self.model.activity_types),
                selectinload(self.model.building)
            )
            .filter(self.model.name == name)
            .first()
        )

    def get_orgs_by_address(self, address: str):
        return (
            self.session.query(self.model)
            .join(self.model.building)
            .options(
                selectinload(self.model.activity_types),
                selectinload(self.model.building)
            )
            .filter(Buildings.address == address)
            .distinct()
            .all()
        )

    def get_orgs_by_location(
            self,
            lat_min: float,
            lat_max: float,
            lon_min: float,
            lon_max: float,
    ):
        return (
            self.session.query(self.model)
            .join(self.model.building)
            .options(
                selectinload(self.model.activity_types),
                selectinload(self.model.building)
            )
            .filter(
                Buildings.point_x >= lat_min,
                Buildings.point_x <= lat_max,
                Buildings.point_y >= lon_min,
                Buildings.point_y <= lon_max,
            )
            .distinct()
            .all()
        )

    def get_orgs_by_activity_type(self, activity_type: str):
        return (
            self.session.query(self.model)
            .join(self.model.activity_types)
            .options(
                selectinload(self.model.activity_types),
                selectinload(self.model.building)
            )
            .filter(ActivityTypes.activity_type == activity_type)
            .distinct()
            .all()
        )

    def get_orgs_by_activity_type_deep(self, activity_type: str):
        root = (
            self.session.query(ActivityTypes)
            .options(selectinload(ActivityTypes.children))
            .filter(ActivityTypes.activity_type == activity_type)
            .first()
        )

        if not root:
            return []

        activity_type_ids = set()

        def activity_types_recurse_check(node):
            activity_type_ids.add(node.activity_id)
            if node.children:
                for child in node.children:
                    activity_types_recurse_check(child)

        activity_types_recurse_check(root)

        return (
            self.session.query(self.model)
            .join(self.model.activity_types)
            .options(
                selectinload(self.model.activity_types),
                selectinload(self.model.building)
            )
            .filter(ActivityTypes.activity_id.in_(activity_type_ids))
            .distinct()
            .all()
        )
