from sqlalchemy.orm import Session

from db.organizations_repository import OrganizationsRepository
from db.models.organizations import Organizations


class OrganizationsService:
    @classmethod
    def get_all_orgs(cls, session: Session):
        orgs = OrganizationsRepository(session=session).get_all_orgs()

        return cls.process_orgs_list(orgs)

    @classmethod
    def get_org_by_id(cls, session: Session, org_id: int):
        org = OrganizationsRepository(session=session).get_org_by_id(org_id=org_id)

        return cls.process_org(org)

    @classmethod
    def get_org_by_name(cls, session: Session, name: str):
        org = OrganizationsRepository(session=session).get_org_by_name(name=name)

        return cls.process_org(org)

    @classmethod
    def get_orgs_by_address(cls, session: Session, address: str):
        orgs = OrganizationsRepository(session=session).get_orgs_by_address(address=address)

        return cls.process_orgs_list(orgs)

    @classmethod
    def get_orgs_by_location(
            cls,
            session: Session,
            lat_min: float,
            lat_max: float,
            lon_min: float,
            lon_max: float,
    ):
        orgs = (
            OrganizationsRepository(session=session)
            .get_orgs_by_location(
                lat_min=lat_min,
                lat_max=lat_max,
                lon_min=lon_min,
                lon_max=lon_max,
            )
        )

        return cls.process_orgs_list(orgs)

    @classmethod
    def get_orgs_by_activity_type(cls, session: Session, activity_type: str):
        orgs = (
            OrganizationsRepository(session=session)
            .get_orgs_by_activity_type(activity_type=activity_type)
        )

        return cls.process_orgs_list(orgs)

    @classmethod
    def get_orgs_by_activity_type_deep(cls, session: Session, activity_type: str):
        orgs = (
            OrganizationsRepository(session=session)
            .get_orgs_by_activity_type_deep(activity_type=activity_type)
        )

        return cls.process_orgs_list(orgs)

    @staticmethod
    def process_orgs_list(organizations: list[Organizations]):
        result = []
        if organizations:
            for org in organizations:
                org.address = org.building.address
                activity_type_list = [
                    el.activity_type for el in org.activity_types
                ]

                result.append({
                    "org_id": org.org_id,
                    "name": org.name,
                    "phones": org.phones,
                    "address": org.address,
                    "activity_types": activity_type_list,
                })

        return result

    @staticmethod
    def process_org(organization: Organizations):
        if organization:
            organization.address = organization.building.address
            activity_type_list = [
                el.activity_type for el in organization.activity_types
            ]

            return {
                "org_id": organization.org_id,
                "name": organization.name,
                "phones": organization.phones,
                "address": organization.address,
                "activity_types": activity_type_list,
            }