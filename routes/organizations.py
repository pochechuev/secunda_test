import os

from fastapi import APIRouter, Query, Path, Depends, Security, HTTPException
from fastapi.security.api_key import APIKeyHeader
from sqlalchemy.orm import Session

from services.organizations_service import OrganizationsService
from schemas.organizations import OrganizationResponseSchema
from db.database import get_session

router = APIRouter(
    prefix="/orgs",
    tags=["Organizations"],
)


def check_api_key(api_key: str = Security(APIKeyHeader(name="X-API-Key"))):
    if api_key != os.getenv("API_KEY"):
    # if api_key != "0f1891f5-45f9-4871-8b26-1599e5e45922":
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return api_key


@router.get(
    "/",
    summary="Получить список всех организаций",
    response_model=list[OrganizationResponseSchema | None]
)
def get_all_orgs(
        session: Session = Depends(get_session),
        api_key: str = Depends(check_api_key),
):
    return OrganizationsService.get_all_orgs(session)


@router.get(
    "/get_by_id/{org_id}",
    summary="Найти организацию по уникальному идентификатору.",
    response_model=OrganizationResponseSchema | None
)
def get_org_by_id(
        org_id: int = Path(description="Organization ID."),
        session: Session = Depends(get_session),
        api_key: str = Depends(check_api_key),
):
    return OrganizationsService.get_org_by_id(session=session, org_id=org_id)


@router.get(
    "/get_by_name",
    summary="Найти организацию по названию.",
    response_model=OrganizationResponseSchema | None
)
def get_org_by_name(
        name: str = Query(description="Organization name."),
        session: Session = Depends(get_session),
        api_key: str = Depends(check_api_key),
):
    return OrganizationsService.get_org_by_name(session=session, name=name)


@router.get(
    "/get_by_address",
    summary="Найти организации находящиеся по адресу.",
    response_model=list[OrganizationResponseSchema | None],
)
def get_orgs_by_address(
        address: str = Query(description="Address for organizations search."),
        session: Session = Depends(get_session),
        api_key: str = Depends(check_api_key),
):
    return OrganizationsService.get_orgs_by_address(session=session, address=address)


@router.get(
    "/get_by_location",
    summary="Найти организации в указанной области.",
    description="Организации находятся внутри прямоугольника, построенного по четырем точкам.",
    response_model=list[OrganizationResponseSchema | None]
)
def get_orgs_by_location(
        lat_min: float = Query(description="Min latitude for search location"),
        lat_max: float = Query(description="Max latitude for search location"),
        lon_min: float = Query(description="Min longitude for search location"),
        lon_max: float = Query(description="Max longitude for search location"),
        session: Session = Depends(get_session),
        api_key: str = Depends(check_api_key),
):
    return OrganizationsService.get_orgs_by_location(
        session=session,
        lat_min=lat_min,
        lat_max=lat_max,
        lon_min=lon_min,
        lon_max=lon_max,
    )


@router.get(
    "/get_by_activity_type/{activity_type}",
    summary="Найти организации по виду деятельности.",
    response_model=list[OrganizationResponseSchema | None]
)
def get_orgs_by_activity_type(
        activity_type: str = Path(description="Activity type of organizations."),
        session: Session = Depends(get_session),
        api_key: str = Depends(check_api_key),
):
    return OrganizationsService.get_orgs_by_activity_type(
        session=session,
        activity_type=activity_type,
    )


@router.get(
    "/get_by_activity_type_deep/{activity_type}",
    summary="Найти организации по виду деятельности, включая вложенности.",
    response_model=list[OrganizationResponseSchema | None]
)
def get_orgs_by_activity_type_deep(
        activity_type: str = Path(description="Activity type of organizations."),
        session: Session = Depends(get_session),
        api_key: str = Depends(check_api_key),
):
    return OrganizationsService.get_orgs_by_activity_type_deep(
        session=session,
        activity_type=activity_type,
    )
