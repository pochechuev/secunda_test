from sqlalchemy import Column, ForeignKey, Integer, Float, String
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.dialects.postgresql import ARRAY

Base = declarative_base()


class OrganizationsActivityTypes(Base):
    __tablename__ = "organizations_activity_types"

    org_activity_id = Column(Integer, primary_key=True, index=True)
    organization_id = Column(ForeignKey("organizations.org_id"), nullable=False)
    activity_type_id = Column(ForeignKey("activity_types.activity_id"), nullable=False)


class Organizations(Base):
    __tablename__ = "organizations"

    org_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phones = Column(ARRAY(String), nullable=False)
    address = Column(ForeignKey("buildings.building_id"), nullable=False)

    building = relationship("Buildings")
    activity_types = relationship(
        "ActivityTypes",
        secondary="organizations_activity_types",
        back_populates="organizations",
    )


class Buildings(Base):
    __tablename__ = "buildings"

    building_id = Column(Integer, primary_key=True, index=True)
    address = Column(String, nullable=False)
    point_x = Column(Float, nullable=False)
    point_y = Column(Float, nullable=False)


class ActivityTypes(Base):
    __tablename__ = "activity_types"

    activity_id = Column(Integer, primary_key=True, index=True)
    activity_type = Column(String, nullable=False)
    parent_id = Column(ForeignKey("activity_types.activity_id"), nullable=True)

    organizations = relationship(
        "Organizations",
        secondary="organizations_activity_types",
        back_populates="activity_types",
    )
    parent = relationship(
        "ActivityTypes",
        backref="children",
        remote_side=[activity_id],
        uselist=True,
    )
