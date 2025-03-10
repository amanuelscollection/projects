from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..controllers import resource_management as controller
from ..schemas import resource_management as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Resource Management'],
    prefix="/resourcemangement"
)

@router.post("/", response_model=schema.ResourceManagementBase)
def create_resource(request: schema.ResourceManagementCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[schema.ResourceManagementBase])
def read_all_resources(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{item_id}", response_model=schema.ResourceManagementBase)
def read_one_resource(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)

@router.put("/{item_id}", response_model=schema.ResourceManagementBase)
def update_resource(item_id: int, request: schema.ResourceManagementUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, item_id=item_id, request=request)

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_resource(item_id: int, db: Session = Depends(get_db)):
    controller.delete(db=db, item_id=item_id)
    return None