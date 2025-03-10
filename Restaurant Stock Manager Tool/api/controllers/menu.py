from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import menu as model
from sqlalchemy.exc import SQLAlchemyError
from ..schemas import menu as schema

def create(db: Session, request: schema.MenuItemCreate):
    try:
        new_item = model.Menu(**request.dict())
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
        return new_item
    except SQLAlchemyError as e:
        error = str(e)
        print("Item was inserted Successfully")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="SUCCESS ITEM INSERTED IN MENU AND RESOURCES", headers={"SUCCESS": "ITEM INSERTED IN MENU AND RESOURCES"},)


def read_all(db: Session):
    try:
        result = db.query(model.Menu).all()
        return result
    except SQLAlchemyError as e:
        error = str(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

def read_one(db: Session, item_id):
    try:
        item = db.query(model.Menu).filter(model.Menu.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found!")
        return item
    except SQLAlchemyError as e:
        error = str(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

def update(db: Session, item_id, request: schema.MenuItemUpdate):
    try:
        item = db.query(model.Menu).filter(model.Menu.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found!")
        update_data = request.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(item, key, value)
        db.commit()
        db.refresh(item)
        return item
    except SQLAlchemyError as e:
        error = str(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

def delete(db: Session, item_id):
    try:
        item = db.query(model.Menu).filter(model.Menu.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found!")
        db.delete(item)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except SQLAlchemyError as e:
        error = str(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
