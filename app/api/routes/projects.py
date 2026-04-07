from fastapi import APIRouter, Depends, Header
from app.schemas.project import Project, ProjectCreate, ProjectUpdate
from app.services.project_service import ProjectService
from app.services.auth_service import AuthService

router = APIRouter()

@router.get("", response_model=list[Project])
async def list_projects(
    tenant_id: str = Header(..., alias="X-Tenant-ID"),
    user=Depends(AuthService.get_current_user)
):
    return await ProjectService.list_projects(user, tenant_id)

@router.post("", response_model=Project, status_code=201)
async def create_project(
    payload: ProjectCreate,
    tenant_id: str = Header(..., alias="X-Tenant-ID"),
    user=Depends(AuthService.get_current_user)
):
    return await ProjectService.create_project(user, tenant_id, payload)

@router.get("/{project_id}", response_model=Project)
async def get_project(
    project_id: str,
    tenant_id: str = Header(..., alias="X-Tenant-ID"),
    user=Depends(AuthService.get_current_user)
):
    return await ProjectService.get_project(user, tenant_id, project_id)

@router.patch("/{project_id}", response_model=Project)
async def update_project(
    project_id: str,
    payload: ProjectUpdate,
    tenant_id: str = Header(..., alias="X-Tenant-ID"),
    user=Depends(AuthService.get_current_user)
):
    return await ProjectService.update_project(user, tenant_id, project_id, payload)

@router.delete("/{project_id}", status_code=204)
async def delete_project(
    project_id: str,
    tenant_id: str = Header(..., alias="X-Tenant-ID"),
    user=Depends(AuthService.get_current_user)
):
    return await ProjectService.delete_project(user, tenant_id, project_id)
