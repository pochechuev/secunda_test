from pydantic import BaseModel


class ActivityTypeSchema(BaseModel):
    activity_id: int
    activity_type: str
    parent: int | None

    class Config:
        from_attributes = True


class OrganizationResponseSchema(BaseModel):
    org_id: int
    name: str
    phones: list[str]
    address: str
    activity_types: list[str]

    class Config:
        from_attributes = True
