from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models.resource_management import ResourceManagement as model
from ..models.orders import Order
from sqlalchemy.exc import SQLAlchemyError
from ..schemas import resource_management as schema

def create(db: Session, request: schema.ResourceManagementCreate):
    new_resource = model(
        item_id=request.item_id,
        ingredient_name=request.ingredient_name,
        ingredient_amount=request.ingredient_amount
    )
    
    try:
        db.add(new_resource)
        db.commit()
        db.refresh(new_resource)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
        
    return new_resource

def read_all(db: Session):
    try:
        result = db.query(model).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result

def read_one(db: Session, item_id: int):
    try:
        resource = db.query(model).filter(model.id == item_id).first()
        if not resource:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource not found")
        return resource
    except SQLAlchemyError as e:
        error = str(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

def update(db: Session, item_id: int, request: schema.ResourceManagementUpdate):
    try:
        resource = db.query(model).filter(model.id == item_id).first()
        if not resource:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource not found")
        
        update_data = request.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(resource, key, value)
        
        db.commit()
        db.refresh(resource)
        return resource
    except SQLAlchemyError as e:
        error = str(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

def delete(db: Session, item_id: int):
    try:
        resource = db.query(model).filter(model.id == item_id).first()
        if not resource:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource not found")
        db.delete(resource)
        db.commit()
        return None
    except SQLAlchemyError as e:
        error = str(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
